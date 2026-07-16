#!/usr/bin/env bash
# Install or refresh the per-user macOS LaunchAgent for the unattended queue.

set -eu

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)"
LABEL='com.darvinyi.library.runqueue'
TEMPLATE="$REPO_ROOT/ops/${LABEL}.plist.template"
TARGET_DIR="$HOME/Library/LaunchAgents"
TARGET="$TARGET_DIR/${LABEL}.plist"
LOG_DIR="$HOME/Library/Logs"
TEMP="$TARGET.tmp"
UID_VALUE="$(id -u)"

[ -f "$TEMPLATE" ] || { echo "missing $TEMPLATE" >&2; exit 2; }
mkdir -p "$TARGET_DIR" "$LOG_DIR"
sed -e "s|__REPO_ROOT__|$REPO_ROOT|g" -e "s|__HOME__|$HOME|g" "$TEMPLATE" > "$TEMP"
plutil -lint "$TEMP" >/dev/null
mv "$TEMP" "$TARGET"

launchctl bootout "gui/$UID_VALUE/$LABEL" 2>/dev/null || true
launchctl bootstrap "gui/$UID_VALUE" "$TARGET"
launchctl kickstart "gui/$UID_VALUE/$LABEL"
printf 'Installed %s. Logs: %s/darvinyi-library-runqueue.log\n' "$LABEL" "$LOG_DIR"
