#!/usr/bin/env python3
"""Atomic persistent state and transaction journal for runqueue.sh."""
from __future__ import annotations

import argparse
import json
import os
import shlex
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def timestamp() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def state_dir(value: str | None) -> Path:
    if value:
        return Path(value).expanduser().resolve()
    configured = os.environ.get("RUNQUEUE_STATE_DIR")
    if configured:
        return Path(configured).expanduser().resolve()
    return Path.home() / "Library" / "Application Support" / "darvinyi-library" / "runqueue"


def read_json(path: Path) -> dict[str, Any] | None:
    try:
        with path.open(encoding="utf-8") as fh:
            value = json.load(fh)
    except FileNotFoundError:
        return None
    if not isinstance(value, dict):
        raise SystemExit(f"runqueue state is not an object: {path}")
    return value


def atomic_write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    os.chmod(path.parent, 0o700)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent, text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(value, fh, indent=2, sort_keys=True)
            fh.write("\n")
            fh.flush()
            os.fsync(fh.fileno())
        os.chmod(temp_name, 0o600)
        os.replace(temp_name, path)
        fsync_directory(path.parent)
    finally:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass


def fsync_directory(path: Path) -> None:
    descriptor = os.open(path, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def transaction_path(root: Path) -> Path:
    return root / "transaction.json"


def status_path(root: Path) -> Path:
    return root / "status.json"


def command_begin(args: argparse.Namespace, root: Path) -> None:
    path = transaction_path(root)
    if path.exists():
        raise SystemExit(f"transaction already exists: {path}")
    publish_enabled = args.publish_enabled
    if publish_enabled is None:
        publish_enabled = args.push_required
    atomic_write(
        path,
        {
            "version": 2,
            "phase": "agent",
            "action": args.action,
            "slug": args.slug,
            "title": args.title,
            "base_head": args.base_head,
            "commit_head": "",
            "push_required": args.push_required == "true",
            "publish_enabled": publish_enabled == "true",
            "push_remote": args.push_remote,
            "push_ref": args.push_ref,
            "check_required": args.check_required == "true",
            "attempt": 0,
            "push_attempt": 0,
            "halt_reason": "",
            "created_at": timestamp(),
            "updated_at": timestamp(),
        },
    )


def command_phase(args: argparse.Namespace, root: Path) -> None:
    path = transaction_path(root)
    value = read_json(path)
    if value is None:
        raise SystemExit(f"no transaction exists: {path}")
    value["phase"] = args.phase
    if args.commit_head is not None:
        value["commit_head"] = args.commit_head
    if args.attempt is not None:
        value["attempt"] = args.attempt
    if args.push_attempt is not None:
        value["push_attempt"] = args.push_attempt
    if args.push_required is not None:
        value["push_required"] = args.push_required == "true"
    if args.push_remote is not None:
        value["push_remote"] = args.push_remote
    if args.push_ref is not None:
        value["push_ref"] = args.push_ref
    if args.halt_reason is not None:
        value["halt_reason"] = args.halt_reason
    value["updated_at"] = timestamp()
    atomic_write(path, value)


def command_status(args: argparse.Namespace, root: Path) -> None:
    atomic_write(
        status_path(root),
        {
            "version": 1,
            "state": args.state,
            "action": args.action,
            "slug": args.slug,
            "message": args.message,
            "pid": os.getppid(),
            "updated_at": timestamp(),
        },
    )


def command_show(args: argparse.Namespace, root: Path) -> None:
    value = read_json(status_path(root)) or {
        "version": 1,
        "state": "unknown",
        "action": "",
        "slug": "",
        "message": "no status has been recorded",
        "pid": None,
        "updated_at": None,
    }
    transaction = read_json(transaction_path(root))
    if transaction is not None:
        value["transaction"] = transaction
    if args.json:
        print(json.dumps(value, sort_keys=True))
        return
    print(f"state:   {value.get('state', 'unknown')}")
    print(f"updated: {value.get('updated_at') or 'never'}")
    if value.get("action"):
        print(f"action:  {value['action']} ({value.get('slug', '')})")
    if value.get("message"):
        print(f"message: {value['message']}")
    if transaction is not None:
        print(
            "txn:     "
            f"{transaction.get('phase', '?')} "
            f"{transaction.get('action', '?')} ({transaction.get('slug', '?')})"
        )


def command_txn_env(_args: argparse.Namespace, root: Path) -> None:
    value = read_json(transaction_path(root))
    if value is None:
        print("TXN_PRESENT=0")
        return
    print("TXN_PRESENT=1")
    defaults: dict[str, Any] = {
        "push_required": True,
        "publish_enabled": value.get("push_required", True),
        "check_required": True,
        "attempt": 0,
        "push_attempt": 0,
        "push_remote": "",
        "push_ref": "",
        "halt_reason": "",
    }
    for source, target in (
        ("phase", "TXN_PHASE"),
        ("action", "TXN_ACTION"),
        ("slug", "TXN_SLUG"),
        ("title", "TXN_TITLE"),
        ("base_head", "TXN_BASE_HEAD"),
        ("commit_head", "TXN_COMMIT_HEAD"),
        ("push_required", "TXN_PUSH_REQUIRED"),
        ("publish_enabled", "TXN_PUBLISH_ENABLED"),
        ("check_required", "TXN_CHECK_REQUIRED"),
        ("attempt", "TXN_ATTEMPT"),
        ("push_attempt", "TXN_PUSH_ATTEMPT"),
        ("push_remote", "TXN_PUSH_REMOTE"),
        ("push_ref", "TXN_PUSH_REF"),
        ("halt_reason", "TXN_HALT_REASON"),
    ):
        raw = value.get(source, defaults.get(source, ""))
        if isinstance(raw, bool):
            raw = "1" if raw else "0"
        print(f"{target}={shlex.quote(str(raw))}")


def command_clear(_args: argparse.Namespace, root: Path) -> None:
    try:
        transaction_path(root).unlink()
        fsync_directory(root)
    except FileNotFoundError:
        pass


def command_reset_push(_args: argparse.Namespace, root: Path) -> None:
    path = transaction_path(root)
    value = read_json(path)
    if value is None:
        return
    value["push_attempt"] = 0
    value["updated_at"] = timestamp()
    atomic_write(path, value)


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--dir", help="state directory (defaults to RUNQUEUE_STATE_DIR)")
    commands = result.add_subparsers(dest="command", required=True)

    begin = commands.add_parser("begin")
    begin.add_argument("--action", required=True)
    begin.add_argument("--slug", required=True)
    begin.add_argument("--title", required=True)
    begin.add_argument("--base-head", required=True)
    begin.add_argument("--push-required", choices=("true", "false"), default="true")
    begin.add_argument("--publish-enabled", choices=("true", "false"))
    begin.add_argument("--push-remote", default="")
    begin.add_argument("--push-ref", default="")
    begin.add_argument("--check-required", choices=("true", "false"), default="true")
    begin.set_defaults(handler=command_begin)

    phase = commands.add_parser("phase")
    phase.add_argument("phase", choices=("agent", "ready", "committed", "halted"))
    phase.add_argument("--commit-head")
    phase.add_argument("--attempt", type=int)
    phase.add_argument("--push-attempt", type=int)
    phase.add_argument("--push-required", choices=("true", "false"))
    phase.add_argument("--push-remote")
    phase.add_argument("--push-ref")
    phase.add_argument("--halt-reason")
    phase.set_defaults(handler=command_phase)

    status = commands.add_parser("status")
    status.add_argument("state")
    status.add_argument("--action", default="")
    status.add_argument("--slug", default="")
    status.add_argument("--message", default="")
    status.set_defaults(handler=command_status)

    show = commands.add_parser("show")
    show.add_argument("--json", action="store_true")
    show.set_defaults(handler=command_show)

    txn_env = commands.add_parser("txn-env")
    txn_env.set_defaults(handler=command_txn_env)

    clear = commands.add_parser("clear")
    clear.set_defaults(handler=command_clear)

    reset_push = commands.add_parser("reset-push-attempts")
    reset_push.set_defaults(handler=command_reset_push)
    return result


def main() -> int:
    args = parser().parse_args()
    root = state_dir(args.dir)
    args.handler(args, root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
