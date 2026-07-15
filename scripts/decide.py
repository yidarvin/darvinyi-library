#!/usr/bin/env python3
"""Choose the next safe action in the library's build/critique lifecycle.

The runner consumes this instead of guessing from the Markdown queue table.  It is
read-only: build, critique, resolve, and record actions are performed by agents and
scripts/mark.py.
"""
from __future__ import annotations

import argparse
import json
import os
import shlex
import sys

import validate as V


def load_state(repo: str) -> list[dict]:
    data = V.load_registry(repo)
    chapters = data.get("chapters", [])
    return chapters if isinstance(chapters, list) else []


def verdict(repo: str, slug: str) -> str | None:
    return V.critique_verdict(repo, slug)


def next_action(repo: str) -> dict[str, object]:
    chapters = load_state(repo)
    for chapter in chapters:
        if chapter.get("status") == "draft" and verdict(repo, chapter["slug"]) == "revise":
            return {"action": "resolve", "chapter": chapter}
    for chapter in chapters:
        if chapter.get("status") == "draft" and verdict(repo, chapter["slug"]) in (None, "resolved"):
            return {"action": "critique", "chapter": chapter}
    for chapter in chapters:
        if chapter.get("status") == "draft" and verdict(repo, chapter["slug"]) == "approve":
            return {"action": "record", "chapter": chapter}
    for chapter in chapters:
        if chapter.get("status") == "pending":
            return {"action": "build", "chapter": chapter}
    return {"action": "noop", "chapter": None}


def counts(repo: str) -> dict[str, int]:
    chapters = load_state(repo)
    status_counts = {status: sum(1 for c in chapters if c.get("status") == status) for status in ("pending", "draft", "done")}
    verdict_counts = {status: 0 for status in ("approve", "revise", "resolved", "unreviewed")}
    for chapter in chapters:
        if chapter.get("status") != "draft":
            continue
        v = verdict(repo, chapter["slug"])
        verdict_counts[v if v in verdict_counts else "unreviewed"] += 1
    return {**status_counts, **{f"critique_{k}": v for k, v in verdict_counts.items()}}


def emit_env(decision: dict[str, object]) -> None:
    chapter = decision.get("chapter")
    values = {"ACTION": str(decision["action"])}
    if isinstance(chapter, dict):
        values.update({
            "SLUG": str(chapter.get("slug", "")),
            "TITLE": str(chapter.get("title", "")),
            "NUM": str(chapter.get("num", "")),
        })
    for key, value in values.items():
        print(f"{key}={shlex.quote(value)}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Inspect the next library workflow action.")
    parser.add_argument("command", choices=("next", "status", "counts"))
    parser.add_argument("--format", choices=("text", "json", "env"), default="text")
    parser.add_argument("--repo", default=os.getcwd())
    args = parser.parse_args(argv[1:])
    repo = os.path.abspath(args.repo)

    errors, _warnings = V.validate(repo)
    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    if args.command == "next":
        result = next_action(repo)
        if args.format == "env":
            emit_env(result)
        elif args.format == "json":
            print(json.dumps(result, ensure_ascii=False))
        else:
            chapter = result.get("chapter")
            if isinstance(chapter, dict):
                print(f"{result['action']}: {chapter['num']} {chapter['slug']} ({chapter['title']})")
            else:
                print("noop: no build, critique, or resolution is pending")
        return 0

    result = counts(repo)
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False))
    else:
        print(
            "library: {done} done, {draft} draft, {pending} pending; "
            "draft critiques: {critique_unreviewed} unreviewed, {critique_revise} revise, "
            "{critique_resolved} resolved".format(**result)
        )
        if args.command == "status":
            decision = next_action(repo)
            chapter = decision.get("chapter")
            if isinstance(chapter, dict):
                print(f"next: {decision['action']} {chapter['num']} {chapter['slug']} ({chapter['title']})")
            else:
                print("next: no-op")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
