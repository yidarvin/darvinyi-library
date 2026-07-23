#!/usr/bin/env bash
# runqueue.sh -- durable Codex build, critique, and resolution loop.
#
# Terra builds and resolves. Sol independently critiques. The driver journals
# every action before model work, validates it, and commits it before beginning
# another action. It pushes the accumulated chapter commits only after approval.
# Interrupted ready/committed work is recovered first.
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
#   -t, --timeout SEC         hard limit for one Codex attempt (default: 7200)
#       --max-agent-attempts N retry one action at most N times (default: 3)
#       --max-review-rounds N halt after N revise verdicts (default: 6; 0 unlimited)
#       --max-push-attempts N cap persisted push attempts (default: 8)
#       --push-timeout SEC    hard limit for one git push (default: 300)
#       --no-push             disable the push after chapter approval
#       --no-check            skip the independent npm run check gate (not recommended)
#       --allow-dirty         permit dirty state for --dry-run only
#       --recover-only        recover a ready/committed transaction, then exit
#       --health-check        read-only Git identity/tree/transaction check, then exit
#       --dry-run             print the current action and commands, then exit
#   -y, --yes                 do not confirm an unbounded run on a TTY
#   -h, --help                show this help and exit
#       --version             print the runner version and exit
#
# Exit status: 0 on success/drain; 1 on a safe deterministic halt; 2 on invalid
# use or failed preflight; 69 on synchronization infrastructure failure; 75 on
# another transient failure; 130 on an interrupt. A transaction is never cleared
# until any required approval push is synchronized.

set -uo pipefail

RUNQUEUE_VERSION='0.5.1'
BUILD_MODEL='gpt-5.6-terra'
CRITIC_MODEL='gpt-5.6-sol'
EFFORT='high'
EXTRA_PROMPT=''
NO_PUSH=0
RUN_CHECK=1
ALLOW_DIRTY=0
DRY_RUN=0
HEALTH_CHECK=0
RECOVER_ONLY=0
ASSUME_YES=0
TIMEOUT=7200
MAX_AGENT_ATTEMPTS=3
MAX_REVIEW_ROUNDS=6
MAX_PUSH_ATTEMPTS=8
PUSH_TIMEOUT=300
MAX=''
CHILD_PID=''
RUNQUEUE_STATE_DIR="${RUNQUEUE_STATE_DIR:-}"
RUNQUEUE_LOCK_DIR=''
LOCK_HELD=0
STATE_READY=0

usage() { sed -n '2,/^# Exit status/{/^# Exit status/d;s/^# \{0,1\}//;p;}' "$0"; }

write_status() {
  [ "$STATE_READY" -eq 1 ] || return 0
  python3 "$SCRIPT_DIR/scripts/runqueue_state.py" --dir "$RUNQUEUE_STATE_DIR" status "$1" \
    --action "${2:-}" --slug "${3:-}" --message "${4:-}" >/dev/null 2>&1 ||
    printf '%s\n' "runqueue: warning: could not persist status '$1'" >&2
}
clear_keepalive() {
  [ -n "${RUNQUEUE_KEEPALIVE_FILE:-}" ] || return 0
  rm -f "$RUNQUEUE_KEEPALIVE_FILE" 2>/dev/null || true
}
die() {
  write_status halted '' '' "$*"; clear_keepalive
  printf '\033[31m%s\033[0m\n' "runqueue: $*" >&2; exit 2
}
stop() {
  write_status halted '' '' "$*"; clear_keepalive
  printf '\033[31m%s\033[0m\n' "runqueue: $*" >&2; exit 1
}
retry_later() {
  write_status retrying '' '' "$*"
  printf '\033[33m%s\033[0m\n' "runqueue: transient failure: $*" >&2; exit 75
}
sync_failure() {
  write_status retrying "${TXN_ACTION:-}" "${TXN_SLUG:-}" "$*"
  printf '\033[33m%s\033[0m\n' "runqueue: synchronization infrastructure failure: $*" >&2
  exit 69
}

parse_positive() {
  local flag="$1" value="$2" number
  case "$value" in ''|*[!0-9]*) die "$flag needs a positive integer, got '$value'" ;; esac
  [ "${#value}" -le 9 ] || die "$flag value '$value' is out of range"
  number=$((10#$value)); [ "$number" -ge 1 ] || die "$flag must be at least 1"
  printf '%s' "$number"
}
parse_nonnegative() {
  local flag="$1" value="$2"
  case "$value" in ''|*[!0-9]*) die "$flag needs a non-negative integer, got '$value'" ;; esac
  [ "${#value}" -le 9 ] || die "$flag value '$value' is out of range"
  printf '%s' "$((10#$value))"
}

is_transient_exit() {
  local rc="$1"
  [ "$rc" -eq 75 ] || [ "$rc" -eq 124 ] || { [ "$rc" -ge 128 ] && [ "$rc" -le 192 ]; }
}

while [ $# -gt 0 ]; do
  case "$1" in
    -a|--all) MAX=''; shift ;;
    -n|--count) [ $# -ge 2 ] || die "$1 needs a value"; MAX="$(parse_positive "$1" "$2")"; shift 2 ;;
    -m|--model) [ $# -ge 2 ] || die "$1 needs a value"; BUILD_MODEL="$2"; printf '%s\n' "runqueue: --model is deprecated; use --build-model." >&2; shift 2 ;;
    --build-model) [ $# -ge 2 ] || die "$1 needs a value"; BUILD_MODEL="$2"; shift 2 ;;
    --critic-model) [ $# -ge 2 ] || die "$1 needs a value"; CRITIC_MODEL="$2"; shift 2 ;;
    -e|--effort) [ $# -ge 2 ] || die "$1 needs a value"; EFFORT="$2"; shift 2 ;;
    -p|--prompt) [ $# -ge 2 ] || die "$1 needs a value"; EXTRA_PROMPT="$2"; shift 2 ;;
    -t|--timeout) [ $# -ge 2 ] || die "$1 needs a value"; TIMEOUT="$(parse_positive "$1" "$2")"; shift 2 ;;
    --max-agent-attempts) [ $# -ge 2 ] || die "$1 needs a value"; MAX_AGENT_ATTEMPTS="$(parse_positive "$1" "$2")"; shift 2 ;;
    --max-review-rounds) [ $# -ge 2 ] || die "$1 needs a value"; MAX_REVIEW_ROUNDS="$(parse_nonnegative "$1" "$2")"; shift 2 ;;
    --max-push-attempts) [ $# -ge 2 ] || die "$1 needs a value"; MAX_PUSH_ATTEMPTS="$(parse_positive "$1" "$2")"; shift 2 ;;
    --push-timeout) [ $# -ge 2 ] || die "$1 needs a value"; PUSH_TIMEOUT="$(parse_positive "$1" "$2")"; shift 2 ;;
    --no-push) NO_PUSH=1; shift ;;
    --no-check) RUN_CHECK=0; shift ;;
    --allow-dirty) ALLOW_DIRTY=1; shift ;;
    --recover-only) RECOVER_ONLY=1; shift ;;
    --health-check) HEALTH_CHECK=1; shift ;;
    --dry-run) DRY_RUN=1; shift ;;
    -y|--yes) ASSUME_YES=1; shift ;;
    -h|--help) usage; exit 0 ;;
    --version) echo "runqueue $RUNQUEUE_VERSION"; exit 0 ;;
    --) shift; break ;;
    -*) die "unknown option '$1' (try --help)" ;;
    *) die "unexpected argument '$1' (try --help)" ;;
  esac
done
[ $# -eq 0 ] || die "unexpected argument(s): $* (try --help)"
[ "$ALLOW_DIRTY" -eq 0 ] || [ "$DRY_RUN" -eq 1 ] || die "--allow-dirty is restricted to --dry-run"
[ "$DRY_RUN" -eq 0 ] || [ "$RECOVER_ONLY" -eq 0 ] || die "--dry-run and --recover-only cannot be combined"

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)" || die "cannot resolve script directory"
REPO_ROOT="$SCRIPT_DIR"
SERVICE_BIN="$REPO_ROOT/scripts/service-bin"
GIT_HELPER="$REPO_ROOT/scripts/pipeline-git.sh"
export PIPELINE_GIT_BIN="${PIPELINE_GIT_BIN:-/usr/bin/git}"
export PATH="$SERVICE_BIN:${PATH:-/usr/bin:/bin}"

gitq() { "$GIT_HELPER" "$@"; }

command -v python3 >/dev/null 2>&1 || die "python3 is required"
[ -x "$PIPELINE_GIT_BIN" ] || die "operational Git is not executable: $PIPELINE_GIT_BIN"
[ -x "$GIT_HELPER" ] || die "parent Git helper is not executable: $GIT_HELPER"
[ -x "$SERVICE_BIN/git" ] || die "service Git shim is not executable: $SERVICE_BIN/git"
gitq rev-parse --is-inside-work-tree >/dev/null 2>&1 || die "Git cannot access the configured worktree"

tree_dirty() {
  local status
  status="$(gitq status --porcelain)" || return 2
  [ -n "$status" ]
}

RUNQUEUE_STATE_DIR="${RUNQUEUE_STATE_DIR:-${HOME:?HOME is required}/Library/Application Support/darvinyi-library/runqueue}"
RUNQUEUE_LOCK_DIR="$RUNQUEUE_STATE_DIR/active.lock"

if [ "$HEALTH_CHECK" -eq 1 ]; then
  GIT_OPTIONAL_LOCKS=0 tree_dirty; health_dirty=$?
  eval "$(python3 "$SCRIPT_DIR/scripts/runqueue_state.py" --dir "$RUNQUEUE_STATE_DIR" txn-env)" ||
    die "cannot inspect recovery transaction during health check"
  case "$health_dirty" in
    0) [ "$TXN_PRESENT" -eq 1 ] || die "working tree has uncommitted changes" ;;
    1) ;;
    *) die "git status failed during health check" ;;
  esac
  printf 'runqueue health check OK: PATH git=%s; parent git=%s; neutral-cwd read-only probes passed.\n' \
    "$(command -v git)" "$PIPELINE_GIT_BIN"
  exit 0
fi

mkdir -p "$RUNQUEUE_STATE_DIR" || die "cannot create state directory $RUNQUEUE_STATE_DIR"
chmod 700 "$RUNQUEUE_STATE_DIR" || die "cannot secure state directory $RUNQUEUE_STATE_DIR"
STATE_READY=1
release_lock() {
  [ "$LOCK_HELD" -eq 1 ] || return 0
  rm -f "$RUNQUEUE_LOCK_DIR/pid" 2>/dev/null || true
  rmdir "$RUNQUEUE_LOCK_DIR" 2>/dev/null || true
  LOCK_HELD=0
}
acquire_lock() {
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

[ -f "$SCRIPT_DIR/scripts/runqueue_state.py" ] || die "scripts/runqueue_state.py not found"
[ -f "$SCRIPT_DIR/scripts/run_with_timeout.py" ] || die "scripts/run_with_timeout.py not found"

command -v codex >/dev/null 2>&1 || die "the 'codex' CLI is not on PATH"
[ -f "$SCRIPT_DIR/prompts/queue.md" ] || die "prompts/queue.md not found"
[ -f "$SCRIPT_DIR/content/registry.json" ] || die "content/registry.json not found"
if [ "$RUN_CHECK" -eq 1 ]; then command -v npm >/dev/null 2>&1 || die "npm is required for the check gate"; fi
cd "$SCRIPT_DIR" || die "cannot cd to $SCRIPT_DIR"

state_cmd() { python3 "$SCRIPT_DIR/scripts/runqueue_state.py" --dir "$RUNQUEUE_STATE_DIR" "$@"; }
load_txn() {
  TXN_PRESENT=0 TXN_PHASE='' TXN_ACTION='' TXN_SLUG='' TXN_TITLE='' TXN_BASE_HEAD=''
  TXN_COMMIT_HEAD='' TXN_PUSH_REQUIRED='' TXN_PUBLISH_ENABLED='' TXN_CHECK_REQUIRED=''
  TXN_ATTEMPT=0 TXN_PUSH_ATTEMPT=0
  TXN_PUSH_REMOTE='' TXN_PUSH_REF='' TXN_HALT_REASON=''
  eval "$(state_cmd txn-env)" || die "cannot read transaction journal"
}
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
  local action="$1" slug="$2" title="$3" attempt="$4"
  case "$action" in
    build) cat <<EOF
You are the Terra builder for darvinyi-library. Build exactly one pending book: ${slug} (${title}).

Read AGENTS.md, prompts/notes/${slug}.md, docs/authoring-spec.md, and docs/diagram-vocabulary.md before editing. Research primary sources with web search. Write original prose and original in-vocabulary diagrams; do not reproduce book text, figures, or cover art. Follow the fixed page anatomy and house prose rules. Run npm run check and fix failures. Then run: python3 scripts/mark.py ${slug} draft.

Do not critique, do not mark done, do not commit, and do not push. Touch only this chapter, its registry/queue status, and any strictly required reusable diagram primitive or diagram-vocabulary update.
EOF
      ;;
    critique) cat <<EOF
You are the independent Sol critic for darvinyi-library. Critique exactly this draft: ${slug} (${title}).

Your job is to find defects, not to approve. A wrong approval is the worst outcome. Read AGENTS.md, docs/authoring-spec.md, prompts/critique-rubric.md, src/chapters/${slug}.mdx, and every chapter-specific component it imports. Re-derive factual claims from the chapter brief and recorded evidence where practical; do not begin a new external web search in this review. Run npm run check. Do not edit page content, shared components, or build tooling.

Create or append content/critiques/${slug}.md. Its first line must be verdict: approve or verdict: revise. Add a dated Critique round with REQUIRED findings first and optional ADVISORY findings after. Approve only when there are no REQUIRED findings; on approve, run: python3 scripts/mark.py ${slug} done. Do not commit or push.
EOF
      ;;
    resolve) cat <<EOF
You are the Terra resolver for darvinyi-library. Resolve the current REQUIRED critique findings for ${slug} (${title}).

Read AGENTS.md, the full content/critiques/${slug}.md history, prompts/notes/${slug}.md, docs/authoring-spec.md, and every current chapter artifact. Apply every REQUIRED finding, preserve prior fixes, run npm run check, then append a dated Builder resolution section naming the concrete changes. Set the first line of the critique file to verdict: resolved. Use the recorded evidence; do not begin a new external web search unless a required finding cannot be resolved otherwise.

Do not mark the chapter done, do not change unrelated chapters, and do not commit or push. A strictly required reusable diagram primitive or diagram-vocabulary update is allowed.
EOF
      ;;
    *) die "unknown action '$action'" ;;
  esac
  if [ "$attempt" -gt 1 ]; then
    printf '\nRecovery context: attempt %s is continuing an interrupted or incomplete prior attempt. Inspect the existing allowed changes, preserve correct work, finish the same action, and leave all gates green.\n' "$attempt"
  fi
  if [ -n "$EXTRA_PROMPT" ]; then printf '\nAdditional operator instructions:\n%s\n' "$EXTRA_PROMPT"; fi
}

run_agent() {
  local action="$1" slug="$2" title="$3" model="$4" attempt="$5"
  local prompt transcript final rc
  prompt="$(agent_prompt "$action" "$slug" "$title" "$attempt")"
  transcript="${RUNQUEUE_STATE_DIR}/${slug}-${action}-attempt${attempt}-$(date +%Y%m%d-%H%M%S).log"
  final="${transcript}.final"
  local args=(codex)
  [ "$action" = build ] && args+=(--search)
  args+=(-C "$SCRIPT_DIR" -m "$model" -c "model_reasoning_effort=\"${EFFORT}\"" -s workspace-write -a never exec --ephemeral -o "$final" "$prompt")
  env -u RUNQUEUE_STATE_DIR -u RUNQUEUE_KEEPALIVE_FILE \
    python3 "$SCRIPT_DIR/scripts/run_with_timeout.py" "$TIMEOUT" -- "${args[@]}" \
    </dev/null >"$transcript" 2>&1 &
  CHILD_PID=$!
  wait "$CHILD_PID"; rc=$?; CHILD_PID=''
  if [ -s "$final" ]; then printf '\n%s\n' "agent summary:"; sed -n '1,80p' "$final"; fi
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
paths_are_allowed() {
  local action="$1" slug="$2" paths="$3" path
  [ -n "$paths" ] || return 0
  while IFS= read -r path; do
    case "$action:$path" in
      build:src/chapters/"$slug".mdx|build:content/registry.json|build:prompts/queue.md) ;;
      build:src/chapters/_figures/*|build:src/chapters/_widgets/*|build:src/components/diagrams/*|build:docs/diagram-vocabulary.md) ;;
      critique:content/critiques/"$slug".md|critique:content/registry.json|critique:prompts/queue.md) ;;
      resolve:src/chapters/"$slug".mdx|resolve:src/chapters/_figures/*|resolve:src/chapters/_widgets/*) ;;
      resolve:src/components/diagrams/*|resolve:src/test/chapters.test.tsx|resolve:docs/diagram-vocabulary.md|resolve:content/critiques/"$slug".md|resolve:content/registry.json) ;;
      record:content/registry.json|record:prompts/queue.md) ;;
      *) printf '%s\n' "$path"; return 1 ;;
    esac
  done <<< "$paths"
  return 0
}
changed_paths_are_allowed() {
  local paths
  paths="$(changed_paths)" || return 2
  paths_are_allowed "$1" "$2" "$paths"
}
committed_paths_are_allowed() {
  local paths
  paths="$(gitq diff --name-only "$3" "$4")" || return 2
  paths_are_allowed "$1" "$2" "$paths"
}

index_matches_worktree() {
  local untracked
  gitq diff --quiet || return 1
  untracked="$(gitq ls-files --others --exclude-standard)" || return 2
  [ -z "$untracked" ]
}

validate_action() {
  local action="$1" slug="$2" changed_rc verdict check_rc
  changed_paths_are_allowed "$action" "$slug"; changed_rc=$?
  if [ "$changed_rc" -eq 2 ]; then
    printf '%s\n' "runqueue: could not inspect changed paths after $action for $slug" >&2; return 2
  fi
  if [ "$changed_rc" -ne 0 ]; then
    printf '%s\n' "runqueue: unexpected changed path after $action for $slug" >&2; return 3
  fi
  if [ "$TXN_CHECK_REQUIRED" = 1 ]; then
    check_rc=0
    npm run check || check_rc=$?
    if [ "$check_rc" -ne 0 ]; then
      if is_transient_exit "$check_rc"; then
        retry_later "npm run check interrupted with exit $check_rc after $action for $slug"
      fi
      printf '%s\n' "runqueue: npm run check failed after $action for $slug" >&2
      return 1
    fi
  fi
  case "$action" in
    build)
      [ "$(chapter_status "$slug")" = draft ] || { printf '%s\n' "runqueue: $slug was not marked draft" >&2; return 1; }
      ;;
    critique)
      verdict="$(chapter_verdict "$slug")"
      case "$verdict" in approve|revise) ;; *) printf '%s\n' "runqueue: $slug critique did not set approve or revise" >&2; return 1 ;; esac
      ;;
    resolve)
      [ "$(chapter_verdict "$slug")" = resolved ] || { printf '%s\n' "runqueue: $slug resolution did not set verdict: resolved" >&2; return 1; }
      ;;
    record)
      [ "$(chapter_status "$slug")" = done ] || { printf '%s\n' "runqueue: $slug approval was not recorded as done" >&2; return 1; }
      ;;
  esac
  return 0
}

review_limit_message() {
  local action="$1" slug="$2" verdict rounds
  [ "$action" = critique ] || return 1
  [ "$MAX_REVIEW_ROUNDS" -gt 0 ] || return 1
  verdict="$(chapter_verdict "$slug")"
  [ "$verdict" = revise ] || return 1
  rounds="$(grep -c '^## Critique round' "content/critiques/${slug}.md" 2>/dev/null || true)"
  [ "$rounds" -ge "$MAX_REVIEW_ROUNDS" ] || return 1
  printf '%s' "$slug reached the configured limit of $MAX_REVIEW_ROUNDS revise rounds"
}

commit_message() {
  case "$1" in
    build) printf 'build: %s -- %s' "$2" "$3" ;;
    critique) printf 'critique: %s -- %s' "$2" "$(chapter_verdict "$2")" ;;
    resolve) printf 'resolve critique: %s' "$2" ;;
    record) printf 'critique: %s -- approve (recorded)' "$2" ;;
    *) return 1 ;;
  esac
}
failpoint() {
  [ "${RUNQUEUE_TEST_FAILPOINT:-}" = "$1" ] || return 0
  retry_later "test failpoint $1"
}
determine_upstream_ahead() {
  local branch configured_remote configured_ref target_branch tracking_ref count
  branch="$(gitq symbolic-ref --quiet --short HEAD)" || return 1
  configured_remote="$(gitq config --get "branch.${branch}.remote" 2>/dev/null || true)"
  configured_ref="$(gitq config --get "branch.${branch}.merge" 2>/dev/null || true)"
  if [ "$configured_remote" = "$TXN_PUSH_REMOTE" ] && [ "$configured_ref" = "$TXN_PUSH_REF" ]; then
    PUSH_UPSTREAM="$(gitq rev-parse --abbrev-ref --symbolic-full-name "${branch}@{upstream}")" || return 1
  else
    target_branch="${TXN_PUSH_REF#refs/heads/}"
    [ "$target_branch" != "$TXN_PUSH_REF" ] || return 1
    tracking_ref="refs/remotes/${TXN_PUSH_REMOTE}/${target_branch}"
    if gitq show-ref --verify --quiet "$tracking_ref"; then
      PUSH_UPSTREAM="$tracking_ref"
    else
      PUSH_UPSTREAM='<unpublished>'
      count="$(gitq rev-list --count "$TXN_COMMIT_HEAD")" || return 1
      case "$count" in ''|*[!0-9]*) return 1 ;; esac
      PUSH_AHEAD="$count"
      return 0
    fi
  fi
  count="$(gitq rev-list --count "${PUSH_UPSTREAM}..${TXN_COMMIT_HEAD}")" || return 1
  case "$count" in ''|*[!0-9]*) return 1 ;; esac
  PUSH_AHEAD="$count"
}
push_committed_transaction() {
  local attempt delay rc current dirty_rc
  [ "$TXN_PUSH_REQUIRED" = 1 ] || return 0
  ensure_push_target
  PUSH_UPSTREAM='' PUSH_AHEAD=''
  determine_upstream_ahead || sync_failure "cannot determine upstream ahead count for $TXN_SLUG"
  printf '%s\n' "runqueue: upstream $PUSH_UPSTREAM; ahead by $PUSH_AHEAD commit(s)."
  if [ "$PUSH_AHEAD" -eq 0 ]; then
    printf '%s\n' "runqueue: upstream is synchronized; skipping git push."
    return 0
  fi
  attempt="$TXN_PUSH_ATTEMPT"
  if remote_has_journaled_commit; then
    printf '%s\n' "runqueue: remote already contains $TXN_COMMIT_HEAD; treating the journaled push as complete."
    return 0
  fi
  if [ "$attempt" -ge "$MAX_PUSH_ATTEMPTS" ]; then
    sync_failure "push attempts already exhausted for $TXN_ACTION $TXN_SLUG"
  fi
  while [ "$attempt" -lt "$MAX_PUSH_ATTEMPTS" ]; do
    attempt=$((attempt + 1))
    state_cmd phase committed --push-attempt "$attempt" >/dev/null ||
      retry_later "cannot journal push attempt $attempt"
    write_status pushing "$TXN_ACTION" "$TXN_SLUG" "push attempt $attempt of $MAX_PUSH_ATTEMPTS"
    rc=0
    python3 "$SCRIPT_DIR/scripts/run_with_timeout.py" "$PUSH_TIMEOUT" -- \
      "$GIT_HELPER" push -- "$TXN_PUSH_REMOTE" "${TXN_COMMIT_HEAD}:${TXN_PUSH_REF}" || rc=$?
    if [ "$rc" -eq 0 ]; then return 0; fi
    if remote_has_journaled_commit; then
      printf '%s\n' "runqueue: remote received $TXN_COMMIT_HEAD despite push exit $rc; treating it as complete."
      return 0
    fi
    current="$(gitq rev-parse HEAD)" || sync_failure "cannot inspect HEAD after failed push for $TXN_SLUG"
    [ "$current" = "$TXN_COMMIT_HEAD" ] || stop "HEAD moved during failed push for $TXN_SLUG"
    tree_dirty; dirty_rc=$?
    case "$dirty_rc" in
      0) stop "failed push for $TXN_SLUG mutated the worktree" ;;
      1) ;;
      *) sync_failure "cannot inspect worktree after failed push for $TXN_SLUG" ;;
    esac
    [ "$attempt" -lt "$MAX_PUSH_ATTEMPTS" ] || break
    case "$attempt" in 1) delay=5 ;; 2) delay=15 ;; 3) delay=30 ;; *) delay=60 ;; esac
    printf '%s\n' "runqueue: push attempt $attempt failed; retrying in ${delay}s." >&2
    sleep "$delay"
  done
  sync_failure "push failed $MAX_PUSH_ATTEMPTS times for $TXN_ACTION $TXN_SLUG"
}

remote_has_journaled_commit() {
  local urls url output remote_head rc found
  [ -n "$TXN_PUSH_REMOTE" ] && [ -n "$TXN_PUSH_REF" ] || return 1
  urls="$(gitq remote get-url --all --push "$TXN_PUSH_REMOTE" 2>/dev/null)" ||
    urls="$TXN_PUSH_REMOTE"
  found=0
  while IFS= read -r url; do
    [ -n "$url" ] || continue
    found=1; output=''; rc=0
    output="$(python3 "$SCRIPT_DIR/scripts/run_with_timeout.py" "$PUSH_TIMEOUT" -- \
      "$GIT_HELPER" ls-remote --exit-code "$url" "$TXN_PUSH_REF")" || rc=$?
    [ "$rc" -eq 0 ] || return 1
    remote_head="${output%%[[:space:]]*}"
    [ -n "$remote_head" ] && [ "$remote_head" = "$TXN_COMMIT_HEAD" ] || return 1
  done <<< "$urls"
  [ "$found" -eq 1 ]
}

resolve_push_target() {
  local branch remote branch_remote merge mode current_ref
  branch="$(gitq symbolic-ref --quiet --short HEAD)" || return 1
  branch_remote="$(gitq config --get "branch.${branch}.remote" 2>/dev/null || true)"
  remote="$(gitq config --get "branch.${branch}.pushRemote" 2>/dev/null || true)"
  [ -n "$remote" ] || remote="$(gitq config --get remote.pushDefault 2>/dev/null || true)"
  [ -n "$remote" ] || remote="$branch_remote"
  merge="$(gitq config --get "branch.${branch}.merge" 2>/dev/null || true)"
  mode="$(gitq config --get push.default 2>/dev/null || true)"
  [ -n "$mode" ] || mode=simple
  [ -n "$remote" ] && [ "$remote" != . ] || return 1
  current_ref="refs/heads/${branch}"
  case "$mode" in
    current) PUSH_REF_RESOLVED="$current_ref" ;;
    upstream)
      [ -n "$branch_remote" ] && [ "$remote" = "$branch_remote" ] || return 1
      case "$merge" in refs/heads/*) PUSH_REF_RESOLVED="$merge" ;; *) return 1 ;; esac
      ;;
    simple)
      if [ -n "$branch_remote" ] && [ "$remote" = "$branch_remote" ]; then
        [ "$merge" = "$current_ref" ] || return 1
      fi
      PUSH_REF_RESOLVED="$current_ref"
      ;;
    matching|nothing|*) return 1 ;;
  esac
  PUSH_REMOTE_RESOLVED="$remote"
}

ensure_push_target() {
  [ -n "$TXN_PUSH_REMOTE" ] && [ -n "$TXN_PUSH_REF" ] && return 0
  resolve_push_target || stop "cannot resolve one explicit push target for $TXN_SLUG"
  state_cmd phase committed --push-remote "$PUSH_REMOTE_RESOLVED" --push-ref "$PUSH_REF_RESOLVED" >/dev/null ||
    retry_later "cannot journal the explicit push target"
  load_txn
}

configure_transaction_publish() {
  local push_required=false push_remote='' push_ref=''
  [ "$TXN_PHASE" = ready ] || stop "cannot configure publishing in phase '$TXN_PHASE'"
  if [ "$TXN_PUBLISH_ENABLED" = 1 ] && [ "$(chapter_status "$TXN_SLUG")" = done ]; then
    resolve_push_target || stop "cannot resolve one explicit push target for approved chapter $TXN_SLUG"
    push_required=true
    push_remote="$PUSH_REMOTE_RESOLVED"
    push_ref="$PUSH_REF_RESOLVED"
  fi
  state_cmd phase ready --push-required "$push_required" \
    --push-remote "$push_remote" --push-ref "$push_ref" >/dev/null ||
    retry_later "cannot journal publish policy for $TXN_ACTION $TXN_SLUG"
  load_txn
}

complete_transaction() {
  local already_validated="${1:-0}"
  local current dirty_rc message commit_head commit_tree validated_tree valid_rc
  local parent_head actual_message limit_message index_rc
  load_txn
  [ "$TXN_PRESENT" -eq 1 ] || die "transaction disappeared before completion"
  case "$TXN_PHASE" in
    ready)
      current="$(gitq rev-parse HEAD)" || retry_later "cannot read HEAD before commit"
      message="$(commit_message "$TXN_ACTION" "$TXN_SLUG" "$TXN_TITLE")" || stop "unknown transaction action $TXN_ACTION"
      if [ "$current" != "$TXN_BASE_HEAD" ]; then
        parent_head="$(gitq rev-parse HEAD^)" || stop "HEAD moved unexpectedly during $TXN_ACTION for $TXN_SLUG"
        actual_message="$(gitq log -1 --format=%s)" || stop "cannot inspect intervening commit for $TXN_SLUG"
        tree_dirty; dirty_rc=$?
        if [ "$parent_head" != "$TXN_BASE_HEAD" ] || [ "$actual_message" != "$message" ] || [ "$dirty_rc" -ne 1 ]; then
          stop "HEAD moved unexpectedly during $TXN_ACTION for $TXN_SLUG"
        fi
        committed_paths_are_allowed "$TXN_ACTION" "$TXN_SLUG" "$TXN_BASE_HEAD" "$current" ||
          stop "unexpected committed path while recovering $TXN_ACTION for $TXN_SLUG"
        validate_action "$TXN_ACTION" "$TXN_SLUG"; valid_rc=$?
        [ "$valid_rc" -eq 0 ] || stop "recovered commit no longer passes for $TXN_SLUG"
        configure_transaction_publish
        state_cmd phase committed --commit-head "$current" >/dev/null || retry_later "cannot adopt completed commit"
        load_txn
      else
        tree_dirty; dirty_rc=$?
        [ "$dirty_rc" -eq 0 ] || stop "$TXN_ACTION for $TXN_SLUG has no changes to commit"
        if [ "$already_validated" -ne 1 ]; then
          gitq add -A -- "$SCRIPT_DIR" || retry_later "git add failed for $TXN_ACTION $TXN_SLUG"
          validate_action "$TXN_ACTION" "$TXN_SLUG"; valid_rc=$?
          [ "$valid_rc" -eq 0 ] || stop "validated transaction no longer passes for $TXN_SLUG"
        fi
        index_matches_worktree; index_rc=$?
        case "$index_rc" in
          0) ;;
          1) stop "worktree changed after validation for $TXN_ACTION $TXN_SLUG" ;;
          *) retry_later "cannot compare the validated index and worktree for $TXN_SLUG" ;;
        esac
        validated_tree="$(gitq write-tree)" || retry_later "cannot record validated tree for $TXN_SLUG"
        configure_transaction_publish
        write_status committing "$TXN_ACTION" "$TXN_SLUG" "$message"
        gitq commit --no-verify -m "$message" || retry_later "git commit failed for $TXN_ACTION $TXN_SLUG"
        commit_head="$(gitq rev-parse HEAD)" || retry_later "cannot read committed HEAD"
        commit_tree="$(gitq rev-parse 'HEAD^{tree}')" || retry_later "cannot read committed tree for $TXN_SLUG"
        [ "$commit_tree" = "$validated_tree" ] || stop "commit tree differs from validated tree for $TXN_SLUG"
        committed_paths_are_allowed "$TXN_ACTION" "$TXN_SLUG" "$TXN_BASE_HEAD" "$commit_head" ||
          stop "unexpected committed path after $TXN_ACTION for $TXN_SLUG"
        state_cmd phase committed --commit-head "$commit_head" >/dev/null || retry_later "cannot journal committed transaction"
        failpoint after_commit
        load_txn
      fi
      ;;
    committed) ;;
    *) stop "cannot complete transaction in phase '$TXN_PHASE'" ;;
  esac
  current="$(gitq rev-parse HEAD)" || retry_later "cannot read HEAD during push recovery"
  [ "$current" = "$TXN_COMMIT_HEAD" ] || stop "HEAD does not match journaled commit for $TXN_SLUG"
  tree_dirty; dirty_rc=$?
  [ "$dirty_rc" -eq 1 ] || stop "committed transaction for $TXN_SLUG left a dirty worktree"
  push_committed_transaction
  failpoint after_push
  current="$(gitq rev-parse HEAD)" || retry_later "cannot read HEAD after pushing $TXN_SLUG"
  [ "$current" = "$TXN_COMMIT_HEAD" ] || stop "HEAD moved while pushing $TXN_SLUG"
  tree_dirty; dirty_rc=$?
  [ "$dirty_rc" -eq 1 ] || stop "push for $TXN_SLUG left a dirty worktree"
  limit_message="$(review_limit_message "$TXN_ACTION" "$TXN_SLUG" || true)"
  if [ -n "$limit_message" ]; then
    state_cmd phase halted --halt-reason "$limit_message" >/dev/null ||
      retry_later "cannot journal critique-limit halt"
    stop "$limit_message"
  fi
  state_cmd clear >/dev/null || retry_later "cannot clear completed transaction"
  if [ "$TXN_PUSH_REQUIRED" = 1 ]; then
    printf '%s\n' "runqueue: committed and published approved chapter $TXN_SLUG."
    write_status running "$TXN_ACTION" "$TXN_SLUG" "committed and published approved chapter"
  else
    printf '%s\n' "runqueue: committed $TXN_ACTION for $TXN_SLUG locally; publish deferred until approval."
    write_status running "$TXN_ACTION" "$TXN_SLUG" "committed locally; publish deferred until approval"
  fi
}

recover_transaction() {
  local current dirty_rc valid_rc scope_rc
  load_txn
  [ "$TXN_PRESENT" -eq 1 ] || return 0
  write_status recovering "$TXN_ACTION" "$TXN_SLUG" "recovering $TXN_PHASE transaction"
  printf '%s\n' "runqueue: recovering $TXN_PHASE transaction for $TXN_ACTION $TXN_SLUG."
  case "$TXN_PHASE" in
    committed|ready)
      complete_transaction
      ;;
    halted)
      if limit_message="$(review_limit_message "$TXN_ACTION" "$TXN_SLUG" || true)" &&
        [ -n "$limit_message" ]; then
        stop "$limit_message"
      fi
      [ -z "$TXN_HALT_REASON" ] || stop "$TXN_HALT_REASON"
      stop "transaction for $TXN_SLUG is durably halted"
      ;;
    agent)
      current="$(gitq rev-parse HEAD)" || retry_later "cannot read HEAD during recovery"
      [ "$current" = "$TXN_BASE_HEAD" ] || stop "HEAD moved during interrupted $TXN_ACTION for $TXN_SLUG"
      tree_dirty; dirty_rc=$?
      case "$dirty_rc" in
        1) return 0 ;;
        2) retry_later "git status failed during transaction recovery" ;;
      esac
      changed_paths_are_allowed "$TXN_ACTION" "$TXN_SLUG"; scope_rc=$?
      [ "$scope_rc" -eq 0 ] || stop "interrupted $TXN_ACTION for $TXN_SLUG touched an unexpected path"
      gitq add -A -- "$SCRIPT_DIR" || retry_later "git add failed during recovery for $TXN_ACTION $TXN_SLUG"
      validate_action "$TXN_ACTION" "$TXN_SLUG"; valid_rc=$?
      if [ "$valid_rc" -eq 0 ]; then
        state_cmd phase ready >/dev/null || retry_later "cannot journal recovered ready transaction"
        complete_transaction 1
      fi
      ;;
    *) stop "unknown transaction phase '$TXN_PHASE'" ;;
  esac
}

begin_transaction() {
  local publish_enabled check_required base_head
  base_head="$(gitq rev-parse HEAD)" || retry_later "cannot read HEAD before $1"
  if [ "$NO_PUSH" -eq 0 ]; then
    publish_enabled=true
  else
    publish_enabled=false
  fi
  [ "$RUN_CHECK" -eq 1 ] && check_required=true || check_required=false
  state_cmd begin --action "$1" --slug "$2" --title "$3" --base-head "$base_head" \
    --push-required false --publish-enabled "$publish_enabled" \
    --check-required "$check_required" >/dev/null ||
    die "cannot create transaction journal"
}

run_transaction() {
  local attempt rc model dirty_rc valid_rc scope_rc
  load_txn
  [ "$TXN_PRESENT" -eq 1 ] || die "no transaction to run"
  if [ "$TXN_PHASE" = agent ]; then
    attempt="$TXN_ATTEMPT"
    if [ "$attempt" -ge "$MAX_AGENT_ATTEMPTS" ]; then
      stop "$TXN_ACTION for $TXN_SLUG already exhausted $MAX_AGENT_ATTEMPTS agent attempts"
    fi
    while [ "$attempt" -lt "$MAX_AGENT_ATTEMPTS" ]; do
      attempt=$((attempt + 1))
      state_cmd phase agent --attempt "$attempt" >/dev/null || retry_later "cannot journal attempt $attempt"
      write_status running "$TXN_ACTION" "$TXN_SLUG" "agent attempt $attempt of $MAX_AGENT_ATTEMPTS"
      printf '\n\033[1m\033[36m==== %s: %s (%s), attempt %s/%s ====\033[0m\n' \
        "$TXN_ACTION" "$TXN_SLUG" "$TXN_TITLE" "$attempt" "$MAX_AGENT_ATTEMPTS"
      rc=0
      if [ "$TXN_ACTION" = record ]; then
        python3 scripts/mark.py "$TXN_SLUG" done || rc=$?
      else
        model="$BUILD_MODEL"; [ "$TXN_ACTION" = critique ] && model="$CRITIC_MODEL"
        run_agent "$TXN_ACTION" "$TXN_SLUG" "$TXN_TITLE" "$model" "$attempt" || rc=$?
      fi
      changed_paths_are_allowed "$TXN_ACTION" "$TXN_SLUG"; scope_rc=$?
      [ "$scope_rc" -eq 0 ] || stop "$TXN_ACTION for $TXN_SLUG touched an unexpected path"
      tree_dirty; dirty_rc=$?
      [ "$dirty_rc" -ne 2 ] || retry_later "git status failed after $TXN_ACTION for $TXN_SLUG"
      valid_rc=1
      if [ "$dirty_rc" -eq 0 ]; then
        gitq add -A -- "$SCRIPT_DIR" || retry_later "git add failed after $TXN_ACTION for $TXN_SLUG"
        validate_action "$TXN_ACTION" "$TXN_SLUG"; valid_rc=$?
      fi
      if [ "$valid_rc" -eq 0 ]; then
        state_cmd phase ready >/dev/null || retry_later "cannot journal ready transaction"
        failpoint after_ready
        complete_transaction 1
        return 0
      fi
      if [ "$attempt" -ge "$MAX_AGENT_ATTEMPTS" ]; then
        [ "$rc" -eq 124 ] && stop "$TXN_ACTION timed out $MAX_AGENT_ATTEMPTS times for $TXN_SLUG"
        stop "$TXN_ACTION for $TXN_SLUG failed validation after $MAX_AGENT_ATTEMPTS attempts"
      fi
      printf '%s\n' "runqueue: attempt $attempt incomplete (agent exit $rc); retrying the same transaction." >&2
    done
  else
    complete_transaction
  fi
}

on_signal() {
  printf '\n\033[33m%s\033[0m\n' "runqueue: interrupted; transaction retained for recovery."
  write_status interrupted '' '' "signal received; transaction retained"
  if [ -n "$CHILD_PID" ]; then kill -TERM "$CHILD_PID" 2>/dev/null; wait "$CHILD_PID" 2>/dev/null; fi
  exit 130
}
trap on_signal INT TERM

load_txn
if [ "$TXN_PRESENT" -eq 0 ]; then
  tree_dirty; initial_dirty=$?
  case "$initial_dirty" in
    0) [ "$ALLOW_DIRTY" -eq 1 ] || die "working tree has uncommitted changes and no recovery transaction" ;;
    1) ;;
    *) die "git status failed during preflight" ;;
  esac
fi

if [ "$DRY_RUN" -eq 1 ]; then
  if [ "$TXN_PRESENT" -eq 1 ]; then
    ACTION="$TXN_ACTION"; SLUG="$TXN_SLUG"; TITLE="$TXN_TITLE"; transaction_desc="$TXN_PHASE transaction"
  else
    eval "$(next_env)" || exit 1; transaction_desc='none'
  fi
  printf '\033[1m%s\033[0m\n' "runqueue plan"
  printf '  builder:       %s (effort %s)\n' "$BUILD_MODEL" "$EFFORT"
  printf '  critic:        %s (effort %s)\n' "$CRITIC_MODEL" "$EFFORT"
  printf '  timeout:       %ss per attempt\n' "$TIMEOUT"
  printf '  transaction:   %s\n' "$transaction_desc"
  printf '  next action:   %s%s\n' "$ACTION" "${SLUG:+ ($SLUG)}"
  printf '\n%s\n' "dry run: no recovery, agent, check, commit, or push was executed."
  exit 0
fi

completed=0
recovered_completion=0
load_txn
if [ "$TXN_PRESENT" -eq 1 ]; then
  case "$TXN_ACTION" in
    critique|record) [ "$(chapter_status "$TXN_SLUG")" = done ] && recovered_completion=1 ;;
  esac
fi
recover_transaction
completed="$recovered_completion"
load_txn
if [ "$RECOVER_ONLY" -eq 1 ]; then
  [ "$TXN_PRESENT" -eq 0 ] || stop "transaction for $TXN_SLUG is incomplete and needs another agent attempt"
  printf '%s\n' "runqueue: recovery complete; no transaction remains."
  exit 0
fi

if [ -z "$MAX" ] && [ "$ASSUME_YES" -eq 0 ] && [ -t 0 ]; then
  printf '\n%s ' "About to run all actionable chapters with automatic stage commits and one push per approved chapter. Continue? [y/N]"
  read -r reply
  case "$reply" in [Yy]|[Yy][Ee][Ss]) ;; *) echo "aborted."; exit 0 ;; esac
fi

write_status running '' '' "queue loop started"
while :; do
  load_txn
  if [ "$TXN_PRESENT" -eq 0 ]; then
    eval "$(next_env)" || stop "cannot determine the next queue action"
    if [ "$ACTION" = noop ]; then
      write_status complete '' '' "queue drained"; clear_keepalive
      printf '\n\033[32m%s\033[0m\n' "queue drained: no build, critique, or resolution is pending."
      break
    fi
    if [ -n "$MAX" ] && [ "$completed" -ge "$MAX" ]; then
      write_status complete '' '' "requested chapter limit reached"; clear_keepalive
      printf '\n\033[32m%s\033[0m\n' "reached limit of $MAX completed chapters."
      break
    fi
    tree_dirty; between_dirty=$?
    case "$between_dirty" in
      1) ;;
      0) stop "worktree became dirty between transactions" ;;
      *) retry_later "git status failed between transactions" ;;
    esac
    before_done="$(done_count)"
    begin_transaction "$ACTION" "$SLUG" "$TITLE"
  else
    before_done="$(done_count)"
  fi

  run_transaction
  after_done="$(done_count)"
  if [ "$after_done" -gt "$before_done" ]; then completed=$((completed + after_done - before_done)); fi
done

exit 0
