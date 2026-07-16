#!/usr/bin/env bash
# Entrypoint for the macOS LaunchAgent installed by install-runqueue-launchd.sh.
# Keep the environment explicit because launchd does not load a login shell profile.

set -uo pipefail

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)" || exit 2
REPO_ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)" || exit 2
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
export RUNQUEUE_STATE_DIR="$HOME/Library/Application Support/darvinyi-library/runqueue"
export RUNQUEUE_KEEPALIVE_FILE="$RUNQUEUE_STATE_DIR/keepalive"

mkdir -p "$RUNQUEUE_STATE_DIR" || exit 2
chmod 700 "$RUNQUEUE_STATE_DIR" || exit 2
: > "$RUNQUEUE_KEEPALIVE_FILE" || exit 2
cd / || exit 2
exec "$REPO_ROOT/runqueue.sh" --all --yes
