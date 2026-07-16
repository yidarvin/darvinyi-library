#!/usr/bin/env bash
# runqueue.sh -- Codex-driven build, critique, and resolution loop for the library.
#
# Terra builds and resolves chapters. Sol independently critiques them. The driver
# owns validation, commits, and pushes, so agents cannot silently fold unrelated work
# into a chapter commit. It stops on an agent error, failed gate, unexpected changed
# path, dirty tree, timeout, push failure, or too many critique rounds.
#
# Usage:
#   ./runqueue.sh [-a] [-n N] [options]
#
#   -a, --all                 finish every actionable chapter (default)
#   -n, --count N             finish at most N chapters, then stop
#   -m, --model MODEL         deprecated alias for --build-model
#       --build-model MODEL   Terra build/resolution model (default: gpt-5.6-terra)
#       --critic-model MODEL  Sol critic model (default: gpt-5.6-sol)
#   -e, --effort LEVEL        Codex reasoning effort (default: high)
#   -p, --prompt TEXT         append instructions to every agent role
#   -t, --timeout SEC         stop one Codex run after SEC seconds (needs timeout/gtimeout)
#       --max-review-rounds N stop after N revise verdicts for one chapter (default: 3)
#       --no-push             commit locally but do not push
#       --no-check            skip the independent npm run check gate (not recommended)
#       --allow-dirty         allow an initial dirty worktree
#       --dry-run             print the current action and commands, then exit
#   -y, --yes                 do not confirm an unbounded run on a TTY
#   -h, --help                show this help and exit
#       --version             print the runner version and exit
#
# Exit status: 0 on a clean no-op, queue drain, or requested count; 1 when a run stops
# for review; 2 on invalid use or failed preflight; 130 on an interrupt.

set -uo pipefail

BUILD_MODEL='gpt-5.6-terra'
CRITIC_MODEL='gpt-5.6-sol'
EFFORT='high'
EXTRA_PROMPT=''
NO_PUSH=0
RUN_CHECK=1
ALLOW_DIRTY=0
DRY_RUN=0
ASSUME_YES=0
TIMEOUT=0
TIMEOUT_BIN=''
MAX=''
MAX_REVIEW_ROUNDS=3
CHILD_PID=''
RUNQUEUE_STATE_DIR=''
RUNQUEUE_LOCK_DIR=''
LOCK_HELD=0

usage() { sed -n '2,/^# Exit status/{/^# Exit status/d;s/^# \{0,1\}//;p;}' "$0"; }
die() { printf '\033[31m%s\033[0m\n' "runqueue: $*" >&2; exit 2; }
stop() { printf '\033[31m%s\033[0m\n' "runqueue: $*" >&2; exit 1; }

parse_positive() {
  local flag="$1" value="$2"
  case "$value" in ''|*[!0-9]*) die "$flag needs a positive integer, got '$value'" ;; esac
  [ "${#value}" -le 9 ] || die "$flag value '$value' is out of range"
  local number=$((10#$value))
  [ "$number" -ge 1 ] || die "$flag must be at least 1"
  printf '%s' "$number"
}

while [ $# -gt 0 ]; do
  case "$1" in
    -a|--all)                 MAX=''; shift ;;
    -n|--count)               [ $# -ge 2 ] || die "$1 needs a value"; MAX="$(parse_positive "$1" "$2")"; shift 2 ;;
    -m|--model)               [ $# -ge 2 ] || die "$1 needs a value"; BUILD_MODEL="$2"; printf '%s\n' "runqueue: --model is deprecated; use --build-model." >&2; shift 2 ;;
    --build-model)            [ $# -ge 2 ] || die "$1 needs a value"; BUILD_MODEL="$2"; shift 2 ;;
    --critic-model)           [ $# -ge 2 ] || die "$1 needs a value"; CRITIC_MODEL="$2"; shift 2 ;;
    -e|--effort)              [ $# -ge 2 ] || die "$1 needs a value"; EFFORT="$2"; shift 2 ;;
    -p|--prompt)              [ $# -ge 2 ] || die "$1 needs a value"; EXTRA_PROMPT="$2"; shift 2 ;;
    -t|--timeout)             [ $# -ge 2 ] || die "$1 needs a value"; TIMEOUT="$(parse_positive "$1" "$2")"; shift 2 ;;
    --max-review-rounds)      [ $# -ge 2 ] || die "$1 needs a value"; MAX_REVIEW_ROUNDS="$(parse_positive "$1" "$2")"; shift 2 ;;
    --no-push)                NO_PUSH=1; shift ;;
    --no-check)               RUN_CHECK=0; shift ;;
    --allow-dirty)            ALLOW_DIRTY=1; shift ;;
    --dry-run)                DRY_RUN=1; shift ;;
    -y|--yes)                 ASSUME_YES=1; shift ;;
    -h|--help)                usage; exit 0 ;;
    --version)                echo "runqueue 0.2.0"; exit 0 ;;
    --)                       shift; break ;;
    -*)                       die "unknown option '$1' (try --help)" ;;
    *)                        die "unexpected argument '$1' (try --help)" ;;
  esac
done
[ $# -eq 0 ] || die "unexpected argument(s): $* (try --help)"

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)" || die "cannot resolve script directory"
cd "$SCRIPT_DIR" || die "cannot cd to $SCRIPT_DIR"
resolve_git_dir() {
  local dotgit="$SCRIPT_DIR/.git" record gitdir
  if [ -d "$dotgit" ]; then
    printf '%s' "$dotgit"
    return 0
  fi
  [ -f "$dotgit" ] || return 1
  IFS= read -r record < "$dotgit" || return 1
  case "$record" in
    'gitdir: '*) gitdir="${record#gitdir: }" ;;
    *) return 1 ;;
  esac
  case "$gitdir" in
    /*) ;;
    *) gitdir="$SCRIPT_DIR/$gitdir" ;;
  esac
  [ -d "$gitdir" ] || return 1
  printf '%s' "$gitdir"
}
GIT_DIR_PATH="$(resolve_git_dir)" || die "cannot resolve Git metadata directory"
# A LaunchAgent may enter the repository but still be denied getcwd() for its
# Documents ancestor. Run Git from a safe directory; callers that need paths must
# pass the worktree explicitly.
gitq() (
  cd / || return 1
  GIT_DIR="$GIT_DIR_PATH" GIT_WORK_TREE="$SCRIPT_DIR" command git "$@"
)

RUNQUEUE_STATE_DIR="${TMPDIR:-/tmp}/darvinyi-runqueue"
RUNQUEUE_LOCK_DIR="$RUNQUEUE_STATE_DIR/active.lock"

release_lock() {
  [ "$LOCK_HELD" -eq 1 ] || return 0
  rm -f "$RUNQUEUE_LOCK_DIR/pid" 2>/dev/null || true
  rmdir "$RUNQUEUE_LOCK_DIR" 2>/dev/null || true
  LOCK_HELD=0
}

acquire_lock() {
  mkdir -p "$RUNQUEUE_STATE_DIR" || die "cannot create state directory $RUNQUEUE_STATE_DIR"
  if ! mkdir "$RUNQUEUE_LOCK_DIR" 2>/dev/null; then
    local incumbent=''
    if [ -r "$RUNQUEUE_LOCK_DIR/pid" ]; then read -r incumbent < "$RUNQUEUE_LOCK_DIR/pid" || true; fi
    if case "$incumbent" in ''|*[!0-9]*) false ;; *) kill -0 "$incumbent" 2>/dev/null ;; esac; then
      die "another runqueue process is active (pid $incumbent)"
    fi
    rm -f "$RUNQUEUE_LOCK_DIR/pid" || die "cannot clear stale lock file"
    rmdir "$RUNQUEUE_LOCK_DIR" || die "cannot clear stale lock directory $RUNQUEUE_LOCK_DIR"
    mkdir "$RUNQUEUE_LOCK_DIR" || die "cannot acquire queue lock"
  fi
  printf '%s\n' "$$" > "$RUNQUEUE_LOCK_DIR/pid" || { rmdir "$RUNQUEUE_LOCK_DIR"; die "cannot write queue lock"; }
  LOCK_HELD=1
}

acquire_lock
trap release_lock EXIT

command -v codex >/dev/null 2>&1 || die "the 'codex' CLI is not on PATH"
command -v python3 >/dev/null 2>&1 || die "python3 is required"
[ -f prompts/queue.md ] || die "prompts/queue.md not found"
[ -f content/registry.json ] || die "content/registry.json not found"
if [ "$RUN_CHECK" -eq 1 ]; then command -v npm >/dev/null 2>&1 || die "npm is required for the check gate"; fi
if [ "$TIMEOUT" -gt 0 ]; then
  if command -v timeout >/dev/null 2>&1; then TIMEOUT_BIN=timeout
  elif command -v gtimeout >/dev/null 2>&1; then TIMEOUT_BIN=gtimeout
  else die "--timeout needs timeout or gtimeout on PATH"; fi
fi

HAVE_GIT=0
if gitq rev-parse --is-inside-work-tree >/dev/null 2>&1; then HAVE_GIT=1; fi
tree_dirty() {
  local status
  status="$(gitq status --porcelain)" || return 2
  [ -n "$status" ]
}
if [ "$HAVE_GIT" -eq 1 ] && [ "$ALLOW_DIRTY" -eq 0 ]; then
  tree_dirty
  dirty_rc=$?
  case "$dirty_rc" in
    0) die "working tree has uncommitted changes; commit or stash first, or pass --allow-dirty" ;;
    1) ;;
    *) die "git status failed during preflight" ;;
  esac
fi

next_env() { python3 scripts/decide.py next --format env; }
done_count() {
  python3 scripts/decide.py counts --format json | python3 -c 'import json,sys; print(json.load(sys.stdin)["done"])'
}
chapter_status() {
  python3 - "$1" <<'PY'
import json, sys
with open("content/registry.json", encoding="utf-8") as fh:
    data = json.load(fh)
slug = sys.argv[1]
print(next(c["status"] for c in data["chapters"] if c["slug"] == slug))
PY
}
chapter_verdict() {
  python3 - "$1" <<'PY'
import sys
sys.path.insert(0, "scripts")
import validate
print(validate.critique_verdict(".", sys.argv[1]) or "")
PY
}

agent_prompt() {
  local action="$1" slug="$2" title="$3"
  case "$action" in
    build) cat <<EOF
You are the Terra builder for darvinyi-library. Build exactly one pending book: ${slug} (${title}).

Read AGENTS.md, prompts/notes/${slug}.md, docs/authoring-spec.md, and docs/diagram-vocabulary.md before editing. Research primary sources with web search. Write original prose and original in-vocabulary diagrams; do not reproduce book text, figures, or cover art. Follow the fixed page anatomy and house prose rules. Run npm run check and fix failures. Then run: python3 scripts/mark.py ${slug} draft.

Do not critique, do not mark done, do not commit, and do not push. Touch only this chapter's content and the registry/queue status needed to mark it draft.
EOF
      ;;
    critique) cat <<EOF
You are the independent Sol critic for darvinyi-library. Critique exactly this draft: ${slug} (${title}).

Read AGENTS.md, docs/authoring-spec.md, prompts/critique-rubric.md, src/chapters/${slug}.mdx, and every chapter-specific component it imports. Re-derive factual claims from the chapter brief and recorded evidence where practical; do not begin a new external web search in this review. Run npm run check. Do not edit page content, shared components, or build tooling.

Create or append content/critiques/${slug}.md. Its first line must be verdict: approve or verdict: revise. Add a dated Critique round with REQUIRED findings first and optional ADVISORY findings after. Approve only when there are no REQUIRED findings; on approve, run: python3 scripts/mark.py ${slug} done. Do not commit or push.
EOF
      ;;
    resolve) cat <<EOF
You are the Terra resolver for darvinyi-library. Resolve the current REQUIRED critique findings for ${slug} (${title}).

Read AGENTS.md, the full content/critiques/${slug}.md history, prompts/notes/${slug}.md, docs/authoring-spec.md, and every current chapter artifact. Apply every REQUIRED finding, preserve prior fixes, run npm run check, then append a dated Builder resolution section naming the concrete changes. Set the first line of the critique file to verdict: resolved. Use the recorded evidence; do not begin a new external web search unless a required finding cannot be resolved otherwise.

Do not mark the chapter done, do not change unrelated chapters, and do not commit or push.
EOF
      ;;
    *) die "unknown action '$action'" ;;
  esac
  if [ -n "$EXTRA_PROMPT" ]; then printf '\nAdditional operator instructions:\n%s\n' "$EXTRA_PROMPT"; fi
}

run_agent() {
  local action="$1" slug="$2" title="$3" model="$4" prompt transcript final rc
  prompt="$(agent_prompt "$action" "$slug" "$title")"
  transcript="${RUNQUEUE_STATE_DIR}/${slug}-${action}-$(date +%Y%m%d-%H%M%S).log"
  final="${transcript}.final"
  local args=(codex)
  [ "$action" = build ] && args+=(--search)
  args+=(-m "$model" -c "model_reasoning_effort=\"${EFFORT}\"" -s workspace-write -a never exec --ephemeral -o "$final" "$prompt")
  if [ "$TIMEOUT" -gt 0 ]; then "$TIMEOUT_BIN" "$TIMEOUT" "${args[@]}" </dev/null >"$transcript" 2>&1 &
  else "${args[@]}" </dev/null >"$transcript" 2>&1 &
  fi
  CHILD_PID=$!
  wait "$CHILD_PID"
  rc=$?
  CHILD_PID=''
  if [ -s "$final" ]; then
    printf '\n%s\n' "agent summary:"
    sed -n '1,80p' "$final"
  fi
  if [ "$rc" -ne 0 ]; then
    printf '\n%s\n' "agent transcript (last 80 lines): $transcript" >&2
    tail -n 80 "$transcript" >&2
  fi
  return "$rc"
}

changed_paths() {
  local unstaged staged untracked
  unstaged="$(gitq diff --name-only)" || return 2
  staged="$(gitq diff --cached --name-only)" || return 2
  untracked="$(gitq ls-files --others --exclude-standard)" || return 2
  printf '%s\n%s\n%s\n' "$unstaged" "$staged" "$untracked" | sed '/^$/d' | sort -u
}

changed_paths_are_allowed() {
  local action="$1" slug="$2" path paths
  paths="$(changed_paths)" || return 2
  [ -n "$paths" ] || return 0
  while IFS= read -r path; do
    case "$action:$path" in
      build:src/chapters/"$slug".mdx|build:content/registry.json|build:prompts/queue.md) ;;
      build:src/chapters/_figures/*|build:src/chapters/_widgets/*) ;;
      critique:content/critiques/"$slug".md|critique:content/registry.json|critique:prompts/queue.md) ;;
      resolve:src/chapters/"$slug".mdx|resolve:src/chapters/_figures/*|resolve:src/chapters/_widgets/*|resolve:content/critiques/"$slug".md|resolve:content/registry.json) ;;
      record:content/registry.json|record:prompts/queue.md) ;;
      *) printf '%s\n' "$path"; return 1 ;;
    esac
  done <<< "$paths"
  return 0
}

commit_action() {
  local action="$1" slug="$2" title="$3" verdict message
  case "$action" in
    build) message="build: ${slug} -- ${title}" ;;
    critique) verdict="$(chapter_verdict "$slug")"; message="critique: ${slug} -- ${verdict}" ;;
    resolve) message="resolve critique: ${slug}" ;;
    record) message="critique: ${slug} -- approve (recorded)" ;;
    *) stop "cannot commit unknown action '$action'" ;;
  esac
  gitq add -A -- "$SCRIPT_DIR" || return 1
  gitq commit -m "$message" || return 1
  if [ "$NO_PUSH" -eq 0 ]; then gitq push || return 1; fi
}

on_signal() {
  printf '\n\033[33m%s\033[0m\n' "runqueue: interrupted; stopping."
  if [ -n "$CHILD_PID" ]; then kill -TERM "$CHILD_PID" 2>/dev/null; wait "$CHILD_PID" 2>/dev/null; fi
  exit 130
}
trap on_signal INT TERM

eval "$(next_env)" || exit 1
limit_desc="all actionable chapters"
[ -n "$MAX" ] && limit_desc="up to $MAX completed chapters"
printf '\033[1m%s\033[0m\n' "runqueue plan"
printf '  items:         %s\n' "$limit_desc"
printf '  builder:       %s (effort %s)\n' "$BUILD_MODEL" "$EFFORT"
printf '  critic:        %s (effort %s)\n' "$CRITIC_MODEL" "$EFFORT"
printf '  push:          %s\n' "$([ "$NO_PUSH" -eq 1 ] && echo disabled || echo enabled)"
printf '  gate:          %s\n' "$([ "$RUN_CHECK" -eq 1 ] && echo 'npm run check after every action' || echo 'skipped')"
printf '  next action:   %s%s\n' "$ACTION" "${SLUG:+ ($SLUG)}"

if [ "$DRY_RUN" -eq 1 ]; then
  printf '\n%s\n' "dry run: no agent, check, commit, or push was executed."
  exit 0
fi
if [ "$ACTION" = noop ]; then
  printf '\n%s\n' "no-op: no build, critique, or resolution is pending."
  exit 0
fi
if [ -z "$MAX" ] && [ "$ASSUME_YES" -eq 0 ] && [ -t 0 ]; then
  printf '\n%s ' "About to run $limit_desc with automatic commits and pushes. Continue? [y/N]"
  read -r reply
  case "$reply" in [Yy]|[Yy][Ee][Ss]) ;; *) echo "aborted."; exit 0 ;; esac
fi

completed=0
while :; do
  eval "$(next_env)" || exit 1
  if [ "$ACTION" = noop ]; then
    printf '\n\033[32m%s\033[0m\n' "queue drained: no build, critique, or resolution is pending."
    break
  fi
  if [ -n "$MAX" ] && [ "$completed" -ge "$MAX" ]; then
    printf '\n\033[32m%s\033[0m\n' "reached limit of $MAX completed chapters."
    break
  fi

  before_done="$(done_count)"
  printf '\n\033[1m\033[36m==== %s: %s (%s) ====\033[0m\n' "$ACTION" "$SLUG" "$TITLE"
  if [ "$ACTION" = record ]; then
    python3 scripts/mark.py "$SLUG" done || stop "could not record approval for $SLUG"
  else
    model="$BUILD_MODEL"
    [ "$ACTION" = critique ] && model="$CRITIC_MODEL"
    run_agent "$ACTION" "$SLUG" "$TITLE" "$model"
    rc=$?
    if [ "$rc" -ne 0 ]; then
      [ "$TIMEOUT" -gt 0 ] && [ "$rc" -eq 124 ] && stop "$ACTION timed out for $SLUG"
      stop "$ACTION agent exited $rc for $SLUG"
    fi
  fi

  changed_paths_are_allowed "$ACTION" "$SLUG"
  changed_rc=$?
  [ "$changed_rc" -eq 2 ] && stop "could not inspect changed paths after $ACTION for $SLUG"
  [ "$changed_rc" -eq 0 ] || stop "unexpected changed path after $ACTION for $SLUG"
  if [ "$RUN_CHECK" -eq 1 ] && ! npm run check; then stop "npm run check failed after $ACTION for $SLUG"; fi

  if [ "$ACTION" = build ] && [ "$(chapter_status "$SLUG")" != draft ]; then stop "$SLUG was not marked draft by the builder"; fi
  if [ "$ACTION" = critique ]; then
    verdict="$(chapter_verdict "$SLUG")"
    case "$verdict" in approve|revise) ;; *) stop "$SLUG critique did not set approve or revise" ;; esac
    if [ "$verdict" = revise ]; then
      rounds="$(grep -c '^## Critique round' "content/critiques/${SLUG}.md" 2>/dev/null || true)"
      [ "$rounds" -le "$MAX_REVIEW_ROUNDS" ] || stop "$SLUG exceeded $MAX_REVIEW_ROUNDS critique rounds"
    fi
  fi
  if [ "$ACTION" = resolve ] && [ "$(chapter_verdict "$SLUG")" != resolved ]; then stop "$SLUG resolution did not set verdict: resolved"; fi
  if [ "$ACTION" = record ] && [ "$(chapter_status "$SLUG")" != done ]; then stop "$SLUG approval was not recorded as done"; fi

  tree_dirty
  dirty_rc=$?
  [ "$dirty_rc" -eq 2 ] && stop "git status failed after $ACTION for $SLUG"
  [ "$dirty_rc" -eq 0 ] || stop "$ACTION for $SLUG made no changes"
  commit_action "$ACTION" "$SLUG" "$TITLE" || stop "commit or push failed after $ACTION for $SLUG"
  if [ "$HAVE_GIT" -eq 1 ]; then
    tree_dirty
    dirty_rc=$?
    [ "$dirty_rc" -eq 2 ] && stop "git status failed after committing $ACTION for $SLUG"
    [ "$dirty_rc" -ne 0 ] || stop "$ACTION for $SLUG left a dirty worktree"
  fi

  after_done="$(done_count)"
  if [ "$after_done" -gt "$before_done" ]; then completed=$((completed + after_done - before_done)); fi
done

exit 0
