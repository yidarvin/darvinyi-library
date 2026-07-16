#!/usr/bin/env bash
# Install or refresh the per-user macOS LaunchAgent for the unattended queue.

set -eu

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)"
export PIPELINE_GIT_BIN='/usr/bin/git'
export PATH="$REPO_ROOT/scripts/service-bin:$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
LABEL='com.darvinyi.library.runqueue'
TEMPLATE="$REPO_ROOT/ops/${LABEL}.plist.template"
TARGET_DIR="$HOME/Library/LaunchAgents"
TARGET="$TARGET_DIR/${LABEL}.plist"
LOG_DIR="$HOME/Library/Logs"
STATE_DIR="$HOME/Library/Application Support/darvinyi-library/runqueue"
KEEPALIVE="$STATE_DIR/keepalive"
TEMP="$TARGET.tmp.$$"
UID_VALUE="$(id -u)"
STAMP="$(date +%Y%m%d-%H%M%S)"
OUT_LOG="$LOG_DIR/darvinyi-library-runqueue.log"
ERR_LOG="$LOG_DIR/darvinyi-library-runqueue.err.log"

[ -f "$TEMPLATE" ] || { echo "missing $TEMPLATE" >&2; exit 2; }
mkdir -p "$TARGET_DIR" "$LOG_DIR" "$STATE_DIR"
chmod 700 "$STATE_DIR"
trap 'rm -f "$TEMP"' EXIT
sed -e "s|__REPO_ROOT__|$REPO_ROOT|g" -e "s|__HOME__|$HOME|g" "$TEMPLATE" > "$TEMP"
plutil -lint "$TEMP" >/dev/null

RUNQUEUE_STATE_DIR="$STATE_DIR" "$REPO_ROOT/runqueue.sh" --health-check

if launchctl print "gui/$UID_VALUE/$LABEL" >/dev/null 2>&1; then
  launchctl bootout "gui/$UID_VALUE/$LABEL"
fi
if launchctl print "gui/$UID_VALUE/$LABEL" >/dev/null 2>&1; then
  echo "could not unload existing $LABEL" >&2
  exit 1
fi
python3 "$REPO_ROOT/scripts/runqueue_state.py" --dir "$STATE_DIR" reset-push-attempts
mv "$TEMP" "$TARGET"
trap - EXIT
[ ! -e "$OUT_LOG" ] || mv "$OUT_LOG" "$OUT_LOG.$STAMP"
[ ! -e "$ERR_LOG" ] || mv "$ERR_LOG" "$ERR_LOG.$STAMP"
: > "$KEEPALIVE"
launchctl bootstrap "gui/$UID_VALUE" "$TARGET"
launchctl kickstart "gui/$UID_VALUE/$LABEL"
launchctl print "gui/$UID_VALUE/$LABEL" >/dev/null
printf 'Installed %s. Status: bash %s/scripts/runqueue-status.sh\n' "$LABEL" "$REPO_ROOT"
