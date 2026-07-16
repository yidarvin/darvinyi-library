#!/usr/bin/env bash
# Stop and remove the per-user macOS LaunchAgent for the unattended queue.

set -eu

LABEL='com.darvinyi.library.runqueue'
TARGET="$HOME/Library/LaunchAgents/${LABEL}.plist"
KEEPALIVE="$HOME/Library/Application Support/darvinyi-library/runqueue/keepalive"
UID_VALUE="$(id -u)"

if launchctl print "gui/$UID_VALUE/$LABEL" >/dev/null 2>&1; then
  launchctl bootout "gui/$UID_VALUE/$LABEL"
fi
if launchctl print "gui/$UID_VALUE/$LABEL" >/dev/null 2>&1; then
  echo "could not unload $LABEL" >&2
  exit 1
fi
rm -f "$KEEPALIVE"
rm -f "$TARGET"
printf 'Removed %s.\n' "$LABEL"
