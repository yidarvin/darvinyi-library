#!/bin/bash
# Parent-process Git entrypoint. Keep Git's executable identity and cwd stable
# under launchd, regardless of the caller's inherited shell environment.

set -u

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)" || exit 69
REPO_ROOT="${PIPELINE_REPO_ROOT:-$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)}" || exit 69
GIT_BIN="${PIPELINE_GIT_BIN:-/usr/bin/git}"
NEUTRAL_CWD="${PIPELINE_GIT_NEUTRAL_CWD:-${HOME:?HOME is required}}"

case "$GIT_BIN" in
  /*) ;;
  *) printf '%s\n' "pipeline-git: PIPELINE_GIT_BIN must be absolute: $GIT_BIN" >&2; exit 69 ;;
esac
[ -x "$GIT_BIN" ] || { printf '%s\n' "pipeline-git: Git is not executable: $GIT_BIN" >&2; exit 69; }
cd "$NEUTRAL_CWD" || { printf '%s\n' "pipeline-git: cannot enter neutral cwd: $NEUTRAL_CWD" >&2; exit 69; }
exec "$GIT_BIN" -C "$REPO_ROOT" "$@"
