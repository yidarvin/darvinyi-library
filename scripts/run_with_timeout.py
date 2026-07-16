#!/usr/bin/env python3
"""Run one command in its own process group with a portable hard timeout."""
from __future__ import annotations

import os
import signal
import subprocess
import sys
import time
from collections.abc import Sequence


TERMINATE_GRACE_SECONDS = float(os.environ.get("RUN_TIMEOUT_GRACE_SECONDS", "10"))


def usage() -> int:
    print("usage: run_with_timeout.py SECONDS -- COMMAND [ARG ...]", file=sys.stderr)
    return 2


def parse(argv: Sequence[str]) -> tuple[float, list[str]]:
    if len(argv) < 3 or argv[1] == "--":
        raise ValueError
    try:
        seconds = float(argv[1])
    except ValueError as error:
        raise ValueError from error
    if seconds <= 0 or argv[2] != "--" or len(argv) < 4:
        raise ValueError
    return seconds, list(argv[3:])


def main(argv: Sequence[str] = sys.argv) -> int:
    try:
        seconds, command = parse(argv)
    except ValueError:
        return usage()

    child = subprocess.Popen(command, start_new_session=True)

    def group_exists() -> bool:
        try:
            os.killpg(child.pid, 0)
        except ProcessLookupError:
            return False
        except PermissionError:
            return True
        return True

    def terminate_group(signum: int) -> None:
        try:
            os.killpg(child.pid, signum)
        except ProcessLookupError:
            return
        deadline = time.monotonic() + TERMINATE_GRACE_SECONDS
        while time.monotonic() < deadline:
            child.poll()
            if not group_exists():
                return
            time.sleep(0.05)
        if group_exists():
            try:
                os.killpg(child.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
        child.wait()
        kill_deadline = time.monotonic() + TERMINATE_GRACE_SECONDS
        while group_exists() and time.monotonic() < kill_deadline:
            time.sleep(0.05)

    def forward(signum: int, _frame: object) -> None:
        terminate_group(signum)
        raise SystemExit(128 + signum)

    signal.signal(signal.SIGINT, forward)
    signal.signal(signal.SIGTERM, forward)
    try:
        return child.wait(timeout=seconds)
    except subprocess.TimeoutExpired:
        terminate_group(signal.SIGTERM)
        return 124


if __name__ == "__main__":
    raise SystemExit(main())
