#!/usr/bin/env bash
# Stop and remove the per-user macOS LaunchAgent for the unattended queue.

set -eu

LABEL='com.darvinyi.library.runqueue'
TARGET="$HOME/Library/LaunchAgents/${LABEL}.plist"
UID_VALUE="$(id -u)"

launchctl bootout "gui/$UID_VALUE/$LABEL" "$TARGET" 2>/dev/null || true
rm -f "$TARGET"
printf 'Removed %s.\n' "$LABEL"
