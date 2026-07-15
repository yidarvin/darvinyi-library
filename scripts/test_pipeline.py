#!/usr/bin/env python3
"""Focused regression tests for the queue lifecycle contract."""
from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(__file__))
import decide  # noqa: E402
import validate  # noqa: E402


class PipelineTests(unittest.TestCase):
    def make_repo(self, status: str = "pending") -> str:
        root = tempfile.mkdtemp(prefix="library-pipeline-")
        os.makedirs(os.path.join(root, "content"), exist_ok=True)
        os.makedirs(os.path.join(root, "prompts"), exist_ok=True)
        os.makedirs(os.path.join(root, "src", "chapters"), exist_ok=True)
        with open(os.path.join(root, "content", "registry.json"), "w", encoding="utf-8") as fh:
            json.dump(
                {
                    "title": "test", "subtitle": "test", "mode": "book",
                    "chapters": [{"num": 1, "slug": "sample", "title": "Sample", "status": status}],
                }, fh,
            )
        queue_status = "DONE" if status == "done" else "PENDING"
        with open(os.path.join(root, "prompts", "queue.md"), "w", encoding="utf-8") as fh:
            fh.write("| # | slug | item | status |\n|---|---|---|---|\n| 1 | sample | Sample | " + queue_status + " |\n")
        with open(os.path.join(root, "src", "chapters", "sample.mdx"), "w", encoding="utf-8") as fh:
            fh.write("A complete chapter.\n")
        return root

    def write_verdict(self, root: str, verdict: str) -> None:
        os.makedirs(os.path.join(root, "content", "critiques"), exist_ok=True)
        with open(os.path.join(root, "content", "critiques", "sample.md"), "w", encoding="utf-8") as fh:
            fh.write(f"verdict: {verdict}\n\n## Critique round 1 — 2026-07-15\n")

    def test_done_requires_approving_critique(self) -> None:
        root = self.make_repo("done")
        errors, _warnings = validate.validate(root)
        self.assertTrue(any("no approving critique" in error for error in errors))
        self.write_verdict(root, "approve")
        errors, _warnings = validate.validate(root)
        self.assertEqual(errors, [])

    def test_decide_selects_build_critique_resolve_and_record(self) -> None:
        root = self.make_repo("pending")
        self.assertEqual(decide.next_action(root)["action"], "build")
        data = validate.load_registry(root)
        data["chapters"][0]["status"] = "draft"
        validate.write_registry(root, data)
        self.assertEqual(decide.next_action(root)["action"], "critique")
        self.write_verdict(root, "revise")
        self.assertEqual(decide.next_action(root)["action"], "resolve")
        self.write_verdict(root, "resolved")
        self.assertEqual(decide.next_action(root)["action"], "critique")
        self.write_verdict(root, "approve")
        self.assertEqual(decide.next_action(root)["action"], "record")


if __name__ == "__main__":
    unittest.main(verbosity=2)
