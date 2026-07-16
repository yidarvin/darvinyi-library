#!/usr/bin/env bash
# Supervisor for the macOS LaunchAgent installed by install-runqueue-launchd.sh.
# Keep the environment explicit because launchd does not load a login shell profile.

set -uo pipefail

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)" || exit 2
REPO_ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)" || exit 2
export PIPELINE_GIT_BIN="${PIPELINE_GIT_BIN:-/usr/bin/git}"
export PATH="$REPO_ROOT/scripts/service-bin:$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
export RUNQUEUE_STATE_DIR="${RUNQUEUE_STATE_DIR:-$HOME/Library/Application Support/darvinyi-library/runqueue}"
export RUNQUEUE_KEEPALIVE_FILE="${RUNQUEUE_KEEPALIVE_FILE:-$RUNQUEUE_STATE_DIR/keepalive}"

RUNNER="${PIPELINE_RUNNER_BIN:-$REPO_ROOT/runqueue.sh}"
RETRY_BASE="${PIPELINE_INFRA_RETRY_BASE_SECONDS:-15}"
RETRY_CAP="${PIPELINE_INFRA_RETRY_MAX_SECONDS:-300}"

case "$RETRY_BASE:$RETRY_CAP" in
  *[!0-9:]*|:*|*:) printf '%s\n' 'runqueue supervisor: retry delays must be non-negative integers' >&2; exit 2 ;;
esac
[ -x "$PIPELINE_GIT_BIN" ] || { printf '%s\n' "runqueue supervisor: missing $PIPELINE_GIT_BIN" >&2; exit 69; }
[ -x "$REPO_ROOT/scripts/service-bin/git" ] || { printf '%s\n' 'runqueue supervisor: Git shim is not executable' >&2; exit 69; }
[ -x "$RUNNER" ] || { printf '%s\n' "runqueue supervisor: runner is not executable: $RUNNER" >&2; exit 2; }

mkdir -p "$RUNQUEUE_STATE_DIR" || exit 2
chmod 700 "$RUNQUEUE_STATE_DIR" || exit 2
: > "$RUNQUEUE_KEEPALIVE_FILE" || exit 2
cd "$HOME" || exit 69

printf 'runqueue supervisor: PATH git=%s; operational git=%s; ' "$(command -v git)" "$PIPELINE_GIT_BIN"
"$PIPELINE_GIT_BIN" --version

infra_failures=0
while :; do
  rc=0
  "$RUNNER" --all --yes || rc=$?
  [ "$rc" -eq 69 ] || exit "$rc"

  infra_failures=$((infra_failures + 1))
  python3 "$REPO_ROOT/scripts/runqueue_state.py" --dir "$RUNQUEUE_STATE_DIR" reset-push-attempts || exit 69
  delay="$RETRY_BASE"
  remaining=$((infra_failures - 1))
  while [ "$remaining" -gt 0 ] && [ "$delay" -lt "$RETRY_CAP" ]; do
    delay=$((delay * 2))
    [ "$delay" -le "$RETRY_CAP" ] || delay="$RETRY_CAP"
    remaining=$((remaining - 1))
  done
  printf '%s\n' "runqueue supervisor: synchronization infrastructure failure $infra_failures; retrying in ${delay}s." >&2
  [ "$delay" -eq 0 ] || sleep "$delay"
done
