#!/usr/bin/env bash
# Entrypoint for the macOS LaunchAgent installed by install-runqueue-launchd.sh.
# Keep the environment explicit because launchd does not load a login shell profile.

set -uo pipefail

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)" || exit 2
REPO_ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)" || exit 2
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"

cd "$REPO_ROOT" || exit 2
exec ./runqueue.sh --all --yes
