#!/usr/bin/env bash
# Read-only status report for the unattended queue and its LaunchAgent.

set -uo pipefail

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)" || exit 2
REPO_ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)" || exit 2
LABEL='com.darvinyi.library.runqueue'
STATE_DIR="${RUNQUEUE_STATE_DIR:-$HOME/Library/Application Support/darvinyi-library/runqueue}"
export PIPELINE_GIT_BIN="${PIPELINE_GIT_BIN:-/usr/bin/git}"
export PATH="$REPO_ROOT/scripts/service-bin:$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
GIT_HELPER="$REPO_ROOT/scripts/pipeline-git.sh"

printf '%s\n' 'runner state'
python3 "$SCRIPT_DIR/runqueue_state.py" --dir "$STATE_DIR" show

printf '\n%s\n' 'launchd'
if launchctl print "gui/$(id -u)/$LABEL" >/dev/null 2>&1; then
  launchctl print "gui/$(id -u)/$LABEL" | sed -n '/state =/p;/pid =/p;/last exit code =/p'
else
  printf '%s\n' 'not loaded'
fi

printf '\n%s\n' 'queue'
(cd "$REPO_ROOT" && python3 scripts/decide.py status)

printf '\n%s\n' 'worktree'
status="$(GIT_OPTIONAL_LOCKS=0 "$GIT_HELPER" status --short)" || exit 2
if [ -n "$status" ]; then printf '%s\n' "$status"; else printf '%s\n' 'clean'; fi

printf '\n%s\n' 'git identity'
printf 'PATH git:    %s\n' "$(command -v git)"
printf 'parent git:  %s\n' "$PIPELINE_GIT_BIN"
"$PIPELINE_GIT_BIN" --version
