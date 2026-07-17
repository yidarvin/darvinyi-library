#!/usr/bin/env python3
"""Behavioral regression tests for the unattended queue runner."""
from __future__ import annotations

import json
import os
import plistlib
import shutil
import signal
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
RUNNER = ROOT / "runqueue.sh"
STATE_TOOL = ROOT / "scripts" / "runqueue_state.py"
TIMEOUT_TOOL = ROOT / "scripts" / "run_with_timeout.py"
PLIST_TEMPLATE = ROOT / "ops" / "com.darvinyi.library.runqueue.plist.template"
INSTALLER = ROOT / "scripts" / "install-runqueue-launchd.sh"
LAUNCH_SUPERVISOR = ROOT / "scripts" / "runqueue-launchd.sh"
GIT_HELPER = ROOT / "scripts" / "pipeline-git.sh"
SERVICE_GIT = ROOT / "scripts" / "service-bin" / "git"


class RunqueueTests(unittest.TestCase):
    def run_command(
        self,
        *args: str,
        cwd: Path | str | None = None,
        env: dict[str, str] | None = None,
        timeout: float = 10,
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            args,
            cwd=cwd,
            env=env,
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )

    def git(self, repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return self.run_command("git", *args, cwd=repo)

    def make_git_fixture(self, name: str = "repo with spaces") -> tuple[Path, Path]:
        root = Path(tempfile.mkdtemp(prefix="runqueue-test-"))
        repo = root / name
        (repo / "scripts").mkdir(parents=True)
        shutil.copy2(RUNNER, repo / "runqueue.sh")
        shutil.copy2(GIT_HELPER, repo / "scripts" / GIT_HELPER.name)
        (repo / "scripts" / "service-bin").mkdir()
        shutil.copy2(SERVICE_GIT, repo / "scripts" / "service-bin" / "git")
        if STATE_TOOL.exists():
            shutil.copy2(STATE_TOOL, repo / "scripts" / STATE_TOOL.name)
        if TIMEOUT_TOOL.exists():
            shutil.copy2(TIMEOUT_TOOL, repo / "scripts" / TIMEOUT_TOOL.name)
        (repo / "tracked.txt").write_text("clean\n", encoding="utf-8")
        self.assertEqual(self.git(repo, "init", "-q").returncode, 0)
        self.assertEqual(self.git(repo, "config", "user.name", "Queue Test").returncode, 0)
        self.assertEqual(self.git(repo, "config", "user.email", "queue@example.invalid").returncode, 0)
        self.assertEqual(self.git(repo, "add", "-A").returncode, 0)
        self.assertEqual(self.git(repo, "commit", "-qm", "fixture").returncode, 0)
        return root, repo

    def make_pipeline_fixture(self) -> tuple[Path, Path, Path, dict[str, str]]:
        root = Path(tempfile.mkdtemp(prefix="runqueue-recovery-"))
        repo = root / "pipeline repo"
        for directory in ("content", "prompts", "scripts", "src/chapters"):
            (repo / directory).mkdir(parents=True, exist_ok=True)
        for source in (
            RUNNER,
            STATE_TOOL,
            TIMEOUT_TOOL,
            GIT_HELPER,
            SERVICE_GIT,
            ROOT / "scripts" / "decide.py",
            ROOT / "scripts" / "validate.py",
            ROOT / "scripts" / "mark.py",
        ):
            destination = repo / source.relative_to(ROOT)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        (repo / "content" / "registry.json").write_text(
            json.dumps(
                {
                    "title": "test",
                    "subtitle": "test",
                    "mode": "book",
                    "chapters": [
                        {"num": 1, "slug": "sample", "title": "Sample", "status": "pending"}
                    ],
                }
            ),
            encoding="utf-8",
        )
        (repo / "prompts" / "queue.md").write_text(
            "| # | slug | item | status |\n"
            "|---|---|---|---|\n"
            "| 1 | sample | Sample | PENDING |\n",
            encoding="utf-8",
        )
        fake_bin = root / "bin"
        fake_bin.mkdir()
        fake_codex = fake_bin / "codex"
        fake_codex.write_text("#!/bin/sh\nexit 99\n", encoding="utf-8")
        fake_codex.chmod(0o755)
        state = root / "state"
        env = os.environ.copy()
        env["PATH"] = f"{fake_bin}:{env['PATH']}"
        env["RUNQUEUE_STATE_DIR"] = str(state)
        self.assertEqual(self.git(repo, "init", "-q").returncode, 0)
        self.assertEqual(self.git(repo, "config", "user.name", "Queue Test").returncode, 0)
        self.assertEqual(self.git(repo, "config", "user.email", "queue@example.invalid").returncode, 0)
        self.assertEqual(self.git(repo, "add", "-A").returncode, 0)
        self.assertEqual(self.git(repo, "commit", "-qm", "fixture").returncode, 0)
        self.assertEqual(self.git(repo, "branch", "-M", "main").returncode, 0)
        return root, repo, state, env

    def test_state_tool_round_trips_transaction_and_status_atomically(self) -> None:
        with tempfile.TemporaryDirectory(prefix="runqueue-state-") as temp:
            state_dir = Path(temp)
            begin = self.run_command(
                sys.executable,
                str(STATE_TOOL),
                "--dir",
                str(state_dir),
                "begin",
                "--action",
                "build",
                "--slug",
                "sample",
                "--title",
                "Sample Title",
                "--base-head",
                "abc123",
            )
            self.assertEqual(begin.returncode, 0, begin.stderr)

            update = self.run_command(
                sys.executable,
                str(STATE_TOOL),
                "--dir",
                str(state_dir),
                "phase",
                "ready",
                "--push-required",
                "false",
            )
            self.assertEqual(update.returncode, 0, update.stderr)

            transaction = json.loads((state_dir / "transaction.json").read_text(encoding="utf-8"))
            self.assertEqual(transaction["phase"], "ready")
            self.assertEqual(transaction["title"], "Sample Title")
            self.assertFalse(transaction["push_required"])
            self.assertTrue(transaction["publish_enabled"])
            self.assertFalse((state_dir / "transaction.json.tmp").exists())

            status = self.run_command(
                sys.executable,
                str(STATE_TOOL),
                "--dir",
                str(state_dir),
                "status",
                "running",
                "--action",
                "build",
                "--slug",
                "sample",
                "--message",
                "validating output",
            )
            self.assertEqual(status.returncode, 0, status.stderr)
            shown = self.run_command(
                sys.executable,
                str(STATE_TOOL),
                "--dir",
                str(state_dir),
                "show",
                "--json",
            )
            self.assertEqual(shown.returncode, 0, shown.stderr)
            self.assertEqual(json.loads(shown.stdout)["message"], "validating output")

    def test_timeout_wrapper_terminates_a_hung_process(self) -> None:
        started = time.monotonic()
        result = self.run_command(
            sys.executable,
            str(TIMEOUT_TOOL),
            "1",
            "--",
            sys.executable,
            "-c",
            "import time; time.sleep(30)",
            timeout=6,
        )
        elapsed = time.monotonic() - started
        self.assertEqual(result.returncode, 124, result.stderr)
        self.assertLess(elapsed, 5)

    def test_external_sigterm_kills_a_term_resistant_child_group(self) -> None:
        with tempfile.TemporaryDirectory(prefix="runqueue-signal-") as temp:
            pidfile = Path(temp) / "child.pid"
            env = os.environ.copy()
            env["PIDFILE"] = str(pidfile)
            env["RUN_TIMEOUT_GRACE_SECONDS"] = "1"
            wrapper = subprocess.Popen(
                [
                    sys.executable,
                    str(TIMEOUT_TOOL),
                    "30",
                    "--",
                    sys.executable,
                    "-c",
                    (
                        "import os,pathlib,signal,time;"
                        "pathlib.Path(os.environ['PIDFILE']).write_text(str(os.getpid()));"
                        "signal.signal(signal.SIGTERM, signal.SIG_IGN);"
                        "time.sleep(30)"
                    ),
                ],
                env=env,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            for _ in range(30):
                if pidfile.exists():
                    break
                time.sleep(0.05)
            self.assertTrue(pidfile.exists())
            child_pid = int(pidfile.read_text(encoding="utf-8"))
            wrapper.send_signal(signal.SIGTERM)
            self.assertEqual(wrapper.wait(timeout=4), 128 + signal.SIGTERM)
            with self.assertRaises(ProcessLookupError):
                os.kill(child_pid, 0)

    def test_timeout_kills_a_resistant_grandchild_after_its_parent_exits(self) -> None:
        with tempfile.TemporaryDirectory(prefix="runqueue-grandchild-") as temp:
            pidfile = Path(temp) / "grandchild.pid"
            env = os.environ.copy()
            env["PIDFILE"] = str(pidfile)
            env["RUN_TIMEOUT_GRACE_SECONDS"] = "0.5"
            program = (
                "import os,pathlib,signal,subprocess,sys,time;"
                "subprocess.Popen([sys.executable,'-c',"
                "\"import os,pathlib,signal,time;"
                "pathlib.Path(os.environ['PIDFILE']).write_text(str(os.getpid()));"
                "signal.signal(signal.SIGTERM,signal.SIG_IGN);time.sleep(30)\"]);"
                "time.sleep(30)"
            )
            wrapper = subprocess.Popen(
                [sys.executable, str(TIMEOUT_TOOL), "30", "--", sys.executable, "-c", program],
                env=env,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            for _ in range(40):
                if pidfile.exists():
                    break
                time.sleep(0.05)
            self.assertTrue(pidfile.exists())
            grandchild_pid = int(pidfile.read_text(encoding="utf-8"))
            try:
                wrapper.send_signal(signal.SIGTERM)
                self.assertEqual(wrapper.wait(timeout=4), 128 + signal.SIGTERM)
                with self.assertRaises(ProcessLookupError):
                    os.kill(grandchild_pid, 0)
            finally:
                try:
                    os.kill(grandchild_pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass

    def test_health_check_supports_external_git_metadata_from_safe_cwd(self) -> None:
        root, repo = self.make_git_fixture()
        external_git = root / "external metadata.git"
        shutil.move(str(repo / ".git"), external_git)
        (repo / ".git").write_text(f"gitdir: {external_git}\n", encoding="utf-8")
        env = os.environ.copy()
        env["RUNQUEUE_STATE_DIR"] = str(root / "state")

        result = self.run_command(str(repo / "runqueue.sh"), "--health-check", cwd="/", env=env)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("health check OK", result.stdout)

    def test_parent_git_helper_uses_neutral_home_and_explicit_repo(self) -> None:
        with tempfile.TemporaryDirectory(prefix="pipeline-git-helper-") as temp:
            home = Path(temp) / "home"
            home.mkdir()
            log = Path(temp) / "git-call.json"
            fake_git = Path(temp) / "git"
            fake_git.write_text(
                "#!/bin/bash\n"
                "python3 -c 'import json,os,sys; "
                "json.dump({\"cwd\": os.getcwd(), \"args\": sys.argv[1:]}, "
                "open(os.environ[\"GIT_CALL_LOG\"], \"w\"))' \"$@\"\n"
                "exec /usr/bin/git \"$@\"\n",
                encoding="utf-8",
            )
            fake_git.chmod(0o755)
            env = os.environ.copy()
            env["HOME"] = str(home)
            env["PIPELINE_GIT_BIN"] = str(fake_git)
            env["GIT_CALL_LOG"] = str(log)

            result = self.run_command(str(GIT_HELPER), "rev-parse", "--show-toplevel", env=env)

            self.assertEqual(result.returncode, 0, result.stderr)
            call = json.loads(log.read_text(encoding="utf-8"))
            self.assertEqual(Path(call["cwd"]).resolve(), home.resolve())
            self.assertEqual(call["args"][:2], ["-C", str(ROOT)])

    def test_service_path_resolves_shim_and_shim_executes_apple_git(self) -> None:
        env = os.environ.copy()
        env["PATH"] = f"{SERVICE_GIT.parent}:/usr/bin:/bin"
        resolved = self.run_command("/bin/bash", "-c", "command -v git", env=env)
        shim_version = self.run_command(str(SERVICE_GIT), "--version")
        apple_version = self.run_command("/usr/bin/git", "--version")

        self.assertEqual(resolved.returncode, 0, resolved.stderr)
        self.assertEqual(resolved.stdout.strip(), str(SERVICE_GIT))
        self.assertEqual(shim_version.returncode, 0, shim_version.stderr)
        self.assertEqual(shim_version.stdout, apple_version.stdout)
        self.assertEqual(
            SERVICE_GIT.read_text(encoding="utf-8"),
            '#!/bin/bash\nexec /usr/bin/git "$@"\n',
        )

    def test_health_check_does_not_create_or_update_service_state(self) -> None:
        root, repo = self.make_git_fixture("doctor repo")
        state = root / "missing state"
        env = os.environ.copy()
        env["RUNQUEUE_STATE_DIR"] = str(state)

        result = self.run_command(str(repo / "runqueue.sh"), "--health-check", cwd=repo, env=env)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(state.exists())

    def test_health_check_rejects_a_dirty_worktree(self) -> None:
        root, repo = self.make_git_fixture("dirty repo")
        (repo / "tracked.txt").write_text("dirty\n", encoding="utf-8")
        env = os.environ.copy()
        env["RUNQUEUE_STATE_DIR"] = str(root / "state")

        result = self.run_command(str(repo / "runqueue.sh"), "--health-check", cwd="/", env=env)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("uncommitted changes", result.stderr)

    def test_health_check_accepts_dirty_work_owned_by_a_transaction(self) -> None:
        root, repo, state, env = self.make_pipeline_fixture()
        base_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "begin",
                "--action",
                "build",
                "--slug",
                "sample",
                "--title",
                "Sample",
                "--base-head",
                base_head,
            ).returncode,
            0,
        )
        (repo / "content" / "registry.json").write_text("transaction work\n", encoding="utf-8")

        result = self.run_command(str(repo / "runqueue.sh"), "--health-check", cwd="/", env=env)

        self.assertEqual(result.returncode, 0, result.stderr)

    def test_launchd_restarts_only_while_the_queue_marker_exists_or_after_a_crash(self) -> None:
        with PLIST_TEMPLATE.open("rb") as fh:
            plist = plistlib.load(fh)

        keep_alive = plist["KeepAlive"]
        self.assertTrue(keep_alive["Crashed"])
        self.assertNotIn("SuccessfulExit", keep_alive)
        paths = keep_alive["PathState"]
        self.assertEqual(len(paths), 1)
        marker = next(iter(paths))
        self.assertTrue(marker.endswith("/Library/Application Support/darvinyi-library/runqueue/keepalive"))
        self.assertNotIn("WorkingDirectory", plist)
        environment = plist["EnvironmentVariables"]
        self.assertEqual(environment["PIPELINE_GIT_BIN"], "/usr/bin/git")
        self.assertTrue(environment["PATH"].startswith("__REPO_ROOT__/scripts/service-bin:"))
        installer = INSTALLER.read_text(encoding="utf-8")
        self.assertLess(installer.index("--health-check"), installer.index("launchctl bootout"))
        self.assertLess(installer.index("sed -e"), installer.index("launchctl bootout"))
        self.assertLess(installer.index("plutil -lint"), installer.index("launchctl bootout"))
        self.assertLess(installer.index("launchctl bootout"), installer.index('mv "$TEMP" "$TARGET"'))

    def test_supervisor_retries_three_sync_failures_without_model_recovery(self) -> None:
        with tempfile.TemporaryDirectory(prefix="runqueue-supervisor-") as temp:
            root = Path(temp)
            home = root / "home"
            home.mkdir()
            calls = root / "runner-calls"
            model_calls = root / "model-calls"
            fake_runner = root / "runner"
            fake_runner.write_text(
                "#!/bin/bash\n"
                "count=0\n"
                "[ ! -f \"$RUNNER_CALLS\" ] || read -r count < \"$RUNNER_CALLS\"\n"
                "count=$((count + 1))\n"
                "printf '%s\\n' \"$count\" > \"$RUNNER_CALLS\"\n"
                "[ \"$count\" -gt 3 ] && exit 0\n"
                "exit 69\n",
                encoding="utf-8",
            )
            fake_runner.chmod(0o755)
            env = os.environ.copy()
            env.update(
                {
                    "HOME": str(home),
                    "PIPELINE_RUNNER_BIN": str(fake_runner),
                    "PIPELINE_INFRA_RETRY_BASE_SECONDS": "0",
                    "PIPELINE_INFRA_RETRY_MAX_SECONDS": "0",
                    "RUNNER_CALLS": str(calls),
                    "MODEL_CALLS": str(model_calls),
                }
            )

            result = self.run_command(str(LAUNCH_SUPERVISOR), env=env, timeout=10)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(calls.read_text(encoding="utf-8").strip(), "4")
            self.assertFalse(model_calls.exists())
            self.assertGreaterEqual(result.stderr.count("synchronization infrastructure failure"), 3)

    def test_supervisor_retries_three_transient_runner_failures_without_model_recovery(self) -> None:
        with tempfile.TemporaryDirectory(prefix="runqueue-supervisor-transient-") as temp:
            root = Path(temp)
            home = root / "home"
            home.mkdir()
            calls = root / "runner-calls"
            model_calls = root / "model-calls"
            fake_runner = root / "runner"
            fake_runner.write_text(
                "#!/bin/bash\n"
                "count=0\n"
                "[ ! -f \"$RUNNER_CALLS\" ] || read -r count < \"$RUNNER_CALLS\"\n"
                "count=$((count + 1))\n"
                "printf '%s\\n' \"$count\" > \"$RUNNER_CALLS\"\n"
                "[ \"$count\" -gt 3 ] && exit 0\n"
                "exit 75\n",
                encoding="utf-8",
            )
            fake_runner.chmod(0o755)
            env = os.environ.copy()
            env.update(
                {
                    "HOME": str(home),
                    "PIPELINE_RUNNER_BIN": str(fake_runner),
                    "PIPELINE_INFRA_RETRY_BASE_SECONDS": "0",
                    "PIPELINE_INFRA_RETRY_MAX_SECONDS": "0",
                    "RUNNER_CALLS": str(calls),
                    "MODEL_CALLS": str(model_calls),
                }
            )

            result = self.run_command(str(LAUNCH_SUPERVISOR), env=env, timeout=10)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(calls.read_text(encoding="utf-8").strip(), "4")
            self.assertFalse(model_calls.exists())
            self.assertGreaterEqual(result.stderr.count("transient runner failure"), 3)

    def test_supervisor_leaves_normal_stage_failure_to_existing_recovery(self) -> None:
        with tempfile.TemporaryDirectory(prefix="runqueue-supervisor-stage-") as temp:
            root = Path(temp)
            home = root / "home"
            home.mkdir()
            calls = root / "runner-calls"
            fake_runner = root / "runner"
            fake_runner.write_text(
                "#!/bin/bash\n"
                "printf 'called\\n' >> \"$RUNNER_CALLS\"\n"
                "exit 1\n",
                encoding="utf-8",
            )
            fake_runner.chmod(0o755)
            env = os.environ.copy()
            env.update(
                {
                    "HOME": str(home),
                    "PIPELINE_RUNNER_BIN": str(fake_runner),
                    "RUNNER_CALLS": str(calls),
                }
            )

            result = self.run_command(str(LAUNCH_SUPERVISOR), env=env)

            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertEqual(calls.read_text(encoding="utf-8").splitlines(), ["called"])

    def test_interrupted_validation_keeps_the_transaction_restartable(self) -> None:
        _root, repo, state, env = self.make_pipeline_fixture()
        base_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        begin = self.run_command(
            sys.executable,
            str(repo / "scripts" / "runqueue_state.py"),
            "--dir",
            str(state),
            "begin",
            "--action",
            "build",
            "--slug",
            "sample",
            "--title",
            "Sample",
            "--base-head",
            base_head,
            "--push-required",
            "false",
            "--check-required",
            "true",
        )
        self.assertEqual(begin.returncode, 0, begin.stderr)
        registry_path = repo / "content" / "registry.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["chapters"][0]["status"] = "draft"
        registry_path.write_text(json.dumps(registry), encoding="utf-8")
        (repo / "src" / "chapters" / "sample.mdx").write_text("# Sample\n", encoding="utf-8")
        ready = self.run_command(
            sys.executable,
            str(repo / "scripts" / "runqueue_state.py"),
            "--dir",
            str(state),
            "phase",
            "ready",
        )
        self.assertEqual(ready.returncode, 0, ready.stderr)
        fake_npm = Path(env["PATH"].split(":", 1)[0]) / "npm"
        fake_npm.write_text("#!/bin/sh\nexit 143\n", encoding="utf-8")
        fake_npm.chmod(0o755)
        keepalive = state / "keepalive"
        keepalive.touch()
        env["RUNQUEUE_KEEPALIVE_FILE"] = str(keepalive)

        interrupted = self.run_command(
            str(repo / "runqueue.sh"),
            "--recover-only",
            "--no-push",
            cwd="/",
            env=env,
        )

        self.assertEqual(interrupted.returncode, 75, interrupted.stderr)
        self.assertIn("check interrupted with exit 143", interrupted.stderr)
        self.assertTrue(keepalive.exists())
        transaction = json.loads((state / "transaction.json").read_text(encoding="utf-8"))
        self.assertEqual(transaction["phase"], "ready")
        self.assertEqual(self.git(repo, "rev-parse", "HEAD").stdout.strip(), base_head)
        self.assertNotEqual(self.git(repo, "status", "--porcelain").stdout.strip(), "")

    def test_synchronized_upstream_skips_git_push_entirely(self) -> None:
        root, repo, state, env = self.make_pipeline_fixture()
        remote = root / "remote.git"
        self.assertEqual(self.run_command("git", "init", "--bare", "-q", str(remote)).returncode, 0)
        self.assertEqual(self.git(repo, "remote", "add", "origin", str(remote)).returncode, 0)
        self.assertEqual(self.git(repo, "push", "-qu", "origin", "main").returncode, 0)
        head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        begin = self.run_command(
            sys.executable,
            str(repo / "scripts" / "runqueue_state.py"),
            "--dir",
            str(state),
            "begin",
            "--action",
            "record",
            "--slug",
            "sample",
            "--title",
            "Sample",
            "--base-head",
            head,
            "--push-required",
            "true",
            "--push-remote",
            "origin",
            "--push-ref",
            "refs/heads/main",
            "--check-required",
            "false",
        )
        self.assertEqual(begin.returncode, 0, begin.stderr)
        committed = self.run_command(
            sys.executable,
            str(repo / "scripts" / "runqueue_state.py"),
            "--dir",
            str(state),
            "phase",
            "committed",
            "--commit-head",
            head,
        )
        self.assertEqual(committed.returncode, 0, committed.stderr)
        git_dir = Path(self.git(repo, "rev-parse", "--git-dir").stdout.strip())
        if not git_dir.is_absolute():
            git_dir = repo / git_dir
        marker = root / "push-ran"
        hook = git_dir / "hooks" / "pre-push"
        hook.write_text(f"#!/bin/sh\nprintf ran > {marker!s}\nexit 1\n", encoding="utf-8")
        hook.chmod(0o755)

        recovered = self.run_command(
            str(repo / "runqueue.sh"),
            "--recover-only",
            "--no-check",
            cwd=repo,
            env=env,
        )

        self.assertEqual(recovered.returncode, 0, recovered.stderr)
        self.assertIn("ahead by 0 commit(s)", recovered.stdout)
        self.assertIn("skipping git push", recovered.stdout)
        self.assertFalse(marker.exists())
        self.assertFalse((state / "transaction.json").exists())

    def test_intermediate_commit_stays_local_until_approval_publishes_chapter(self) -> None:
        root, repo, state, env = self.make_pipeline_fixture()
        remote = root / "remote.git"
        self.assertEqual(self.run_command("git", "init", "--bare", "-q", str(remote)).returncode, 0)
        self.assertEqual(self.git(repo, "remote", "add", "origin", str(remote)).returncode, 0)
        self.assertEqual(self.git(repo, "push", "-qu", "origin", "main").returncode, 0)
        remote_base = self.git(repo, "rev-parse", "HEAD").stdout.strip()

        registry_path = repo / "content" / "registry.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["chapters"][0]["status"] = "draft"
        registry_path.write_text(json.dumps(registry), encoding="utf-8")
        (repo / "src" / "chapters" / "sample.mdx").write_text("# Sample\n", encoding="utf-8")
        begin_build = self.run_command(
            sys.executable,
            str(repo / "scripts" / "runqueue_state.py"),
            "--dir",
            str(state),
            "begin",
            "--action",
            "build",
            "--slug",
            "sample",
            "--title",
            "Sample",
            "--base-head",
            remote_base,
            "--push-required",
            "false",
            "--publish-enabled",
            "true",
            "--check-required",
            "false",
        )
        self.assertEqual(begin_build.returncode, 0, begin_build.stderr)
        ready_build = self.run_command(
            sys.executable,
            str(repo / "scripts" / "runqueue_state.py"),
            "--dir",
            str(state),
            "phase",
            "ready",
        )
        self.assertEqual(ready_build.returncode, 0, ready_build.stderr)

        built = self.run_command(
            str(repo / "runqueue.sh"),
            "--recover-only",
            "--no-check",
            cwd="/",
            env=env,
        )

        self.assertEqual(built.returncode, 0, built.stderr)
        self.assertIn("publish deferred until approval", built.stdout)
        build_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        remote_after_build = self.run_command(
            "git", "--git-dir", str(remote), "rev-parse", "refs/heads/main"
        )
        self.assertEqual(remote_after_build.stdout.strip(), remote_base)
        self.assertNotEqual(build_head, remote_base)

        registry["chapters"][0]["status"] = "done"
        registry_path.write_text(json.dumps(registry), encoding="utf-8")
        (repo / "prompts" / "queue.md").write_text(
            "| # | slug | item | status |\n"
            "|---|---|---|---|\n"
            "| 1 | sample | Sample | DONE |\n",
            encoding="utf-8",
        )
        critique = repo / "content" / "critiques" / "sample.md"
        critique.parent.mkdir(parents=True)
        critique.write_text("verdict: approve\n\n## Critique round 1\n", encoding="utf-8")
        begin_approval = self.run_command(
            sys.executable,
            str(repo / "scripts" / "runqueue_state.py"),
            "--dir",
            str(state),
            "begin",
            "--action",
            "critique",
            "--slug",
            "sample",
            "--title",
            "Sample",
            "--base-head",
            build_head,
            "--push-required",
            "false",
            "--publish-enabled",
            "true",
            "--check-required",
            "false",
        )
        self.assertEqual(begin_approval.returncode, 0, begin_approval.stderr)
        ready_approval = self.run_command(
            sys.executable,
            str(repo / "scripts" / "runqueue_state.py"),
            "--dir",
            str(state),
            "phase",
            "ready",
        )
        self.assertEqual(ready_approval.returncode, 0, ready_approval.stderr)

        approved = self.run_command(
            str(repo / "runqueue.sh"),
            "--recover-only",
            "--no-check",
            cwd="/",
            env=env,
        )

        self.assertEqual(approved.returncode, 0, approved.stderr)
        self.assertIn("ahead by 2 commit(s)", approved.stdout)
        approval_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        remote_after_approval = self.run_command(
            "git", "--git-dir", str(remote), "rev-parse", "refs/heads/main"
        )
        self.assertEqual(remote_after_approval.stdout.strip(), approval_head)
        self.assertFalse((state / "transaction.json").exists())

    def test_three_sync_failures_preserve_commit_and_never_invoke_codex(self) -> None:
        root, repo, state, env = self.make_pipeline_fixture()
        remote = root / "remote.git"
        self.assertEqual(self.run_command("git", "init", "--bare", "-q", str(remote)).returncode, 0)
        self.assertEqual(self.git(repo, "remote", "add", "origin", str(remote)).returncode, 0)
        self.assertEqual(self.git(repo, "push", "-qu", "origin", "main").returncode, 0)
        base_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        (repo / "local.txt").write_text("preserve me\n", encoding="utf-8")
        self.assertEqual(self.git(repo, "add", "local.txt").returncode, 0)
        self.assertEqual(self.git(repo, "commit", "-qm", "local only").returncode, 0)
        commit_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        begin = self.run_command(
            sys.executable,
            str(repo / "scripts" / "runqueue_state.py"),
            "--dir",
            str(state),
            "begin",
            "--action",
            "record",
            "--slug",
            "sample",
            "--title",
            "Sample",
            "--base-head",
            base_head,
            "--push-required",
            "true",
            "--push-remote",
            "origin",
            "--push-ref",
            "refs/heads/main",
            "--check-required",
            "false",
        )
        self.assertEqual(begin.returncode, 0, begin.stderr)
        committed = self.run_command(
            sys.executable,
            str(repo / "scripts" / "runqueue_state.py"),
            "--dir",
            str(state),
            "phase",
            "committed",
            "--commit-head",
            commit_head,
        )
        self.assertEqual(committed.returncode, 0, committed.stderr)
        sync_calls = root / "sync-calls"
        model_calls = root / "model-calls"
        fake_git = root / "git"
        fake_git.write_text(
            "#!/bin/bash\n"
            "case \" $* \" in\n"
            "  *' ls-remote '*|*' push '*) printf 'sync\\n' >> \"$SYNC_CALLS\"; exit 1 ;;\n"
            "esac\n"
            "exec /usr/bin/git \"$@\"\n",
            encoding="utf-8",
        )
        fake_git.chmod(0o755)
        fake_codex = Path(env["PATH"].split(os.pathsep)[0]) / "codex"
        fake_codex.write_text(
            "#!/bin/sh\nprintf 'model\\n' >> \"$MODEL_CALLS\"\nexit 99\n",
            encoding="utf-8",
        )
        fake_codex.chmod(0o755)
        env.update(
            {
                "PIPELINE_GIT_BIN": str(fake_git),
                "SYNC_CALLS": str(sync_calls),
                "MODEL_CALLS": str(model_calls),
            }
        )

        for _ in range(3):
            reset = self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "reset-push-attempts",
            )
            self.assertEqual(reset.returncode, 0, reset.stderr)
            failed = self.run_command(
                str(repo / "runqueue.sh"),
                "--recover-only",
                "--no-check",
                "--max-push-attempts",
                "1",
                "--push-timeout",
                "2",
                cwd=repo,
                env=env,
            )
            self.assertEqual(failed.returncode, 69, failed.stderr)

        self.assertGreaterEqual(len(sync_calls.read_text(encoding="utf-8").splitlines()), 3)
        self.assertFalse(model_calls.exists())
        transaction = json.loads((state / "transaction.json").read_text(encoding="utf-8"))
        self.assertEqual(transaction["phase"], "committed")
        self.assertEqual(transaction["commit_head"], commit_head)
        self.assertEqual(self.git(repo, "rev-parse", "HEAD").stdout.strip(), commit_head)

    def test_recover_only_commits_validated_ready_work_without_rerunning_codex(self) -> None:
        _root, repo, state, env = self.make_pipeline_fixture()
        base_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        registry_path = repo / "content" / "registry.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["chapters"][0]["status"] = "draft"
        registry_path.write_text(json.dumps(registry), encoding="utf-8")
        (repo / "src" / "chapters" / "sample.mdx").write_text("# Sample\n", encoding="utf-8")
        begin = self.run_command(
            sys.executable,
            str(repo / "scripts" / "runqueue_state.py"),
            "--dir",
            str(state),
            "begin",
            "--action",
            "build",
            "--slug",
            "sample",
            "--title",
            "Sample",
            "--base-head",
            base_head,
            "--push-required",
            "false",
            "--check-required",
            "false",
        )
        self.assertEqual(begin.returncode, 0, begin.stderr)
        ready = self.run_command(
            sys.executable,
            str(repo / "scripts" / "runqueue_state.py"),
            "--dir",
            str(state),
            "phase",
            "ready",
        )
        self.assertEqual(ready.returncode, 0, ready.stderr)

        recovered = self.run_command(
            str(repo / "runqueue.sh"),
            "--recover-only",
            "--no-check",
            "--no-push",
            cwd="/",
            env=env,
        )

        self.assertEqual(recovered.returncode, 0, recovered.stderr)
        self.assertIn("recovery complete", recovered.stdout)
        self.assertFalse((state / "transaction.json").exists())
        self.assertEqual(self.git(repo, "status", "--porcelain").stdout, "")
        self.assertTrue(self.git(repo, "log", "-1", "--format=%s").stdout.startswith("build: sample"))

    def test_recover_only_pushes_a_journaled_commit_before_clearing_it(self) -> None:
        root, repo, state, env = self.make_pipeline_fixture()
        remote = root / "remote.git"
        self.assertEqual(self.run_command("git", "init", "--bare", "-q", str(remote)).returncode, 0)
        self.assertEqual(self.git(repo, "remote", "add", "origin", str(remote)).returncode, 0)
        self.assertEqual(self.git(repo, "push", "-qu", "origin", "main").returncode, 0)
        base_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        (repo / "tracked-after-push.txt").write_text("local commit\n", encoding="utf-8")
        self.assertEqual(self.git(repo, "add", "tracked-after-push.txt").returncode, 0)
        self.assertEqual(self.git(repo, "commit", "-qm", "local only").returncode, 0)
        commit_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        begin = self.run_command(
            sys.executable,
            str(repo / "scripts" / "runqueue_state.py"),
            "--dir",
            str(state),
            "begin",
            "--action",
            "record",
            "--slug",
            "sample",
            "--title",
            "Sample",
            "--base-head",
            base_head,
            "--push-required",
            "true",
            "--check-required",
            "false",
        )
        self.assertEqual(begin.returncode, 0, begin.stderr)
        committed = self.run_command(
            sys.executable,
            str(repo / "scripts" / "runqueue_state.py"),
            "--dir",
            str(state),
            "phase",
            "committed",
            "--commit-head",
            commit_head,
        )
        self.assertEqual(committed.returncode, 0, committed.stderr)

        recovered = self.run_command(
            str(repo / "runqueue.sh"),
            "--recover-only",
            "--no-check",
            cwd="/",
            env=env,
        )

        self.assertEqual(recovered.returncode, 0, recovered.stderr)
        remote_head = self.run_command("git", "--git-dir", str(remote), "rev-parse", "refs/heads/main")
        self.assertEqual(remote_head.stdout.strip(), commit_head)
        self.assertFalse((state / "transaction.json").exists())

    def test_permanent_push_rejection_exhausts_a_persistent_budget(self) -> None:
        root, repo, state, env = self.make_pipeline_fixture()
        remote = root / "remote.git"
        self.assertEqual(self.run_command("git", "init", "--bare", "-q", str(remote)).returncode, 0)
        self.assertEqual(self.git(repo, "remote", "add", "origin", str(remote)).returncode, 0)
        self.assertEqual(self.git(repo, "push", "-qu", "origin", "main").returncode, 0)
        hook = remote / "hooks" / "pre-receive"
        hook.write_text("#!/bin/sh\nexit 1\n", encoding="utf-8")
        hook.chmod(0o755)
        base_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        (repo / "local.txt").write_text("rejected\n", encoding="utf-8")
        self.assertEqual(self.git(repo, "add", "local.txt").returncode, 0)
        self.assertEqual(self.git(repo, "commit", "-qm", "local only").returncode, 0)
        commit_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "begin",
                "--action",
                "record",
                "--slug",
                "sample",
                "--title",
                "Sample",
                "--base-head",
                base_head,
                "--push-required",
                "true",
                "--check-required",
                "false",
            ).returncode,
            0,
        )
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "phase",
                "committed",
                "--commit-head",
                commit_head,
            ).returncode,
            0,
        )

        recovered = self.run_command(
            str(repo / "runqueue.sh"),
            "--recover-only",
            "--no-check",
            "--max-push-attempts",
            "1",
            "--push-timeout",
            "2",
            cwd="/",
            env=env,
        )

        self.assertEqual(recovered.returncode, 69, recovered.stderr)
        transaction = json.loads((state / "transaction.json").read_text(encoding="utf-8"))
        self.assertEqual(transaction["push_attempt"], 1)
        self.assertEqual(transaction["phase"], "committed")

    def test_pre_push_hook_mutation_keeps_the_transaction_and_halts(self) -> None:
        root, repo, state, env = self.make_pipeline_fixture()
        remote = root / "remote.git"
        self.assertEqual(self.run_command("git", "init", "--bare", "-q", str(remote)).returncode, 0)
        self.assertEqual(self.git(repo, "remote", "add", "origin", str(remote)).returncode, 0)
        self.assertEqual(self.git(repo, "push", "-qu", "origin", "main").returncode, 0)
        git_dir = Path(self.git(repo, "rev-parse", "--git-dir").stdout.strip())
        if not git_dir.is_absolute():
            git_dir = repo / git_dir
        hook = git_dir / "hooks" / "pre-push"
        hook.write_text(
            f"#!/bin/sh\nprintf '\\n' >> \"{repo}/content/registry.json\"\n",
            encoding="utf-8",
        )
        hook.chmod(0o755)
        base_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        (repo / "local.txt").write_text("push me\n", encoding="utf-8")
        self.assertEqual(self.git(repo, "add", "local.txt").returncode, 0)
        self.assertEqual(self.git(repo, "commit", "-qm", "local only").returncode, 0)
        commit_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "begin",
                "--action",
                "record",
                "--slug",
                "sample",
                "--title",
                "Sample",
                "--base-head",
                base_head,
                "--push-required",
                "true",
                "--check-required",
                "false",
            ).returncode,
            0,
        )
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "phase",
                "committed",
                "--commit-head",
                commit_head,
            ).returncode,
            0,
        )

        recovered = self.run_command(
            str(repo / "runqueue.sh"), "--recover-only", "--no-check", cwd="/", env=env
        )

        self.assertEqual(recovered.returncode, 1, recovered.stderr)
        self.assertIn("left a dirty worktree", recovered.stderr)
        self.assertTrue((state / "transaction.json").exists())

    def test_pre_commit_hook_cannot_inject_an_unrelated_path(self) -> None:
        _root, repo, state, env = self.make_pipeline_fixture()
        base_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        registry_path = repo / "content" / "registry.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["chapters"][0]["status"] = "draft"
        registry_path.write_text(json.dumps(registry), encoding="utf-8")
        (repo / "src" / "chapters" / "sample.mdx").write_text("# Sample\n", encoding="utf-8")
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "begin",
                "--action",
                "build",
                "--slug",
                "sample",
                "--title",
                "Sample",
                "--base-head",
                base_head,
                "--push-required",
                "false",
                "--check-required",
                "false",
            ).returncode,
            0,
        )
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "phase",
                "ready",
            ).returncode,
            0,
        )
        git_dir = Path(self.git(repo, "rev-parse", "--git-dir").stdout.strip())
        if not git_dir.is_absolute():
            git_dir = repo / git_dir
        hook = git_dir / "hooks" / "pre-commit"
        hook.write_text(
            f"#!/bin/sh\nprintf 'injected\\n' > \"{repo}/unrelated.txt\"\n"
            f"git -C \"{repo}\" add -- \"{repo}/unrelated.txt\"\n",
            encoding="utf-8",
        )
        hook.chmod(0o755)

        recovered = self.run_command(
            str(repo / "runqueue.sh"),
            "--recover-only",
            "--no-check",
            "--no-push",
            cwd="/",
            env=env,
        )

        self.assertEqual(recovered.returncode, 1, recovered.stderr)
        self.assertIn("unexpected committed path", recovered.stderr)
        self.assertTrue((state / "transaction.json").exists())

    def test_pre_commit_hook_cannot_invalidate_an_allowed_path(self) -> None:
        _root, repo, state, env = self.make_pipeline_fixture()
        base_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        registry_path = repo / "content" / "registry.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["chapters"][0]["status"] = "draft"
        registry_path.write_text(json.dumps(registry), encoding="utf-8")
        (repo / "src" / "chapters" / "sample.mdx").write_text("# Sample\n", encoding="utf-8")
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "begin",
                "--action",
                "build",
                "--slug",
                "sample",
                "--title",
                "Sample",
                "--base-head",
                base_head,
                "--push-required",
                "false",
                "--check-required",
                "false",
            ).returncode,
            0,
        )
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "phase",
                "ready",
            ).returncode,
            0,
        )
        git_dir = Path(self.git(repo, "rev-parse", "--git-dir").stdout.strip())
        if not git_dir.is_absolute():
            git_dir = repo / git_dir
        hook = git_dir / "hooks" / "pre-commit"
        hook.write_text(
            f"#!/bin/sh\ncd \"{repo}\"\n"
            "python3 scripts/mark.py sample pending >/dev/null\n"
            "git add -- content/registry.json prompts/queue.md\n",
            encoding="utf-8",
        )
        hook.chmod(0o755)

        recovered = self.run_command(
            str(repo / "runqueue.sh"),
            "--recover-only",
            "--no-check",
            "--no-push",
            cwd="/",
            env=env,
        )

        self.assertEqual(recovered.returncode, 1, recovered.stderr)
        self.assertIn("no longer passes", recovered.stderr)
        self.assertTrue((state / "transaction.json").exists())

    def test_pre_push_hook_cannot_move_head_without_being_detected(self) -> None:
        root, repo, state, env = self.make_pipeline_fixture()
        remote = root / "remote.git"
        self.assertEqual(self.run_command("git", "init", "--bare", "-q", str(remote)).returncode, 0)
        self.assertEqual(self.git(repo, "remote", "add", "origin", str(remote)).returncode, 0)
        self.assertEqual(self.git(repo, "push", "-qu", "origin", "main").returncode, 0)
        base_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        registry_path = repo / "content" / "registry.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["chapters"][0]["status"] = "draft"
        registry_path.write_text(json.dumps(registry), encoding="utf-8")
        (repo / "src" / "chapters" / "sample.mdx").write_text("# Sample\n", encoding="utf-8")
        self.assertEqual(self.git(repo, "add", "-A").returncode, 0)
        self.assertEqual(self.git(repo, "commit", "-qm", "build: sample -- Sample").returncode, 0)
        commit_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "begin",
                "--action",
                "build",
                "--slug",
                "sample",
                "--title",
                "Sample",
                "--base-head",
                base_head,
                "--push-required",
                "true",
                "--check-required",
                "false",
            ).returncode,
            0,
        )
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "phase",
                "committed",
                "--commit-head",
                commit_head,
            ).returncode,
            0,
        )
        git_dir = Path(self.git(repo, "rev-parse", "--git-dir").stdout.strip())
        if not git_dir.is_absolute():
            git_dir = repo / git_dir
        hook = git_dir / "hooks" / "pre-push"
        hook.write_text(
            f"#!/bin/sh\nprintf '\\n' >> \"{repo}/content/registry.json\"\n"
            f"git -C \"{repo}\" add -- \"{repo}/content/registry.json\"\n"
            f"git -C \"{repo}\" commit -qm 'hook moved head'\n",
            encoding="utf-8",
        )
        hook.chmod(0o755)

        recovered = self.run_command(
            str(repo / "runqueue.sh"), "--recover-only", "--no-check", cwd="/", env=env
        )

        self.assertEqual(recovered.returncode, 1, recovered.stderr)
        self.assertIn("HEAD moved", recovered.stderr)
        self.assertTrue((state / "transaction.json").exists())

    def test_successful_final_push_is_reconciled_after_a_crash(self) -> None:
        root, repo, state, env = self.make_pipeline_fixture()
        remote = root / "remote.git"
        self.assertEqual(self.run_command("git", "init", "--bare", "-q", str(remote)).returncode, 0)
        self.assertEqual(self.git(repo, "remote", "add", "origin", str(remote)).returncode, 0)
        self.assertEqual(self.git(repo, "push", "-qu", "origin", "main").returncode, 0)
        base_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        registry_path = repo / "content" / "registry.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["chapters"][0]["status"] = "draft"
        registry_path.write_text(json.dumps(registry), encoding="utf-8")
        (repo / "src" / "chapters" / "sample.mdx").write_text("# Sample\n", encoding="utf-8")
        self.assertEqual(self.git(repo, "add", "-A").returncode, 0)
        self.assertEqual(self.git(repo, "commit", "-qm", "build: sample -- Sample").returncode, 0)
        commit_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "begin",
                "--action",
                "build",
                "--slug",
                "sample",
                "--title",
                "Sample",
                "--base-head",
                base_head,
                "--push-required",
                "true",
                "--check-required",
                "false",
            ).returncode,
            0,
        )
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "phase",
                "committed",
                "--commit-head",
                commit_head,
            ).returncode,
            0,
        )
        crashing_env = env.copy()
        crashing_env["RUNQUEUE_TEST_FAILPOINT"] = "after_push"
        first = self.run_command(
            str(repo / "runqueue.sh"),
            "--recover-only",
            "--no-check",
            "--max-push-attempts",
            "1",
            cwd="/",
            env=crashing_env,
        )
        self.assertEqual(first.returncode, 75, first.stderr)
        self.assertTrue((state / "transaction.json").exists())

        recovered = self.run_command(
            str(repo / "runqueue.sh"),
            "--recover-only",
            "--no-check",
            "--max-push-attempts",
            "1",
            cwd="/",
            env=env,
        )

        self.assertEqual(recovered.returncode, 0, recovered.stderr)
        self.assertFalse((state / "transaction.json").exists())
        remote_head = self.run_command("git", "--git-dir", str(remote), "rev-parse", "refs/heads/main")
        self.assertEqual(remote_head.stdout.strip(), commit_head)

    def test_failed_final_push_is_reconciled_when_remote_received_it(self) -> None:
        root, repo, state, env = self.make_pipeline_fixture()
        remote = root / "remote.git"
        self.assertEqual(self.run_command("git", "init", "--bare", "-q", str(remote)).returncode, 0)
        self.assertEqual(self.git(repo, "remote", "add", "origin", str(remote)).returncode, 0)
        self.assertEqual(self.git(repo, "push", "-qu", "origin", "main").returncode, 0)
        base_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        registry_path = repo / "content" / "registry.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["chapters"][0]["status"] = "draft"
        registry_path.write_text(json.dumps(registry), encoding="utf-8")
        (repo / "src" / "chapters" / "sample.mdx").write_text("# Sample\n", encoding="utf-8")
        self.assertEqual(self.git(repo, "add", "-A").returncode, 0)
        self.assertEqual(self.git(repo, "commit", "-qm", "build: sample -- Sample").returncode, 0)
        commit_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "begin",
                "--action",
                "build",
                "--slug",
                "sample",
                "--title",
                "Sample",
                "--base-head",
                base_head,
                "--push-required",
                "true",
                "--check-required",
                "false",
            ).returncode,
            0,
        )
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "phase",
                "committed",
                "--commit-head",
                commit_head,
            ).returncode,
            0,
        )
        git_dir = Path(self.git(repo, "rev-parse", "--git-dir").stdout.strip())
        if not git_dir.is_absolute():
            git_dir = repo / git_dir
        hook = git_dir / "hooks" / "pre-push"
        hook.write_text("#!/bin/sh\ngit push --no-verify >/dev/null 2>&1\nexit 1\n", encoding="utf-8")
        hook.chmod(0o755)

        recovered = self.run_command(
            str(repo / "runqueue.sh"),
            "--recover-only",
            "--no-check",
            "--max-push-attempts",
            "1",
            cwd="/",
            env=env,
        )

        self.assertEqual(recovered.returncode, 0, recovered.stderr)
        self.assertFalse((state / "transaction.json").exists())
        remote_head = self.run_command("git", "--git-dir", str(remote), "rev-parse", "refs/heads/main")
        self.assertEqual(remote_head.stdout.strip(), commit_head)

    def test_push_publishes_only_the_journaled_ref(self) -> None:
        root, repo, state, env = self.make_pipeline_fixture()
        remote = root / "remote.git"
        self.assertEqual(self.run_command("git", "init", "--bare", "-q", str(remote)).returncode, 0)
        self.assertEqual(self.git(repo, "remote", "add", "origin", str(remote)).returncode, 0)
        self.assertEqual(self.git(repo, "push", "-qu", "origin", "main").returncode, 0)
        self.assertEqual(self.git(repo, "switch", "-qc", "unrelated").returncode, 0)
        (repo / "unrelated.txt").write_text("must stay local\n", encoding="utf-8")
        self.assertEqual(self.git(repo, "add", "unrelated.txt").returncode, 0)
        self.assertEqual(self.git(repo, "commit", "-qm", "unrelated local work").returncode, 0)
        self.assertEqual(self.git(repo, "switch", "-q", "main").returncode, 0)
        base_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        registry_path = repo / "content" / "registry.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["chapters"][0]["status"] = "draft"
        registry_path.write_text(json.dumps(registry), encoding="utf-8")
        (repo / "src" / "chapters" / "sample.mdx").write_text("# Sample\n", encoding="utf-8")
        self.assertEqual(self.git(repo, "add", "-A").returncode, 0)
        self.assertEqual(self.git(repo, "commit", "-qm", "build: sample -- Sample").returncode, 0)
        commit_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        self.assertEqual(self.git(repo, "config", "remote.origin.push", "refs/heads/*:refs/heads/*").returncode, 0)
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "begin",
                "--action",
                "build",
                "--slug",
                "sample",
                "--title",
                "Sample",
                "--base-head",
                base_head,
                "--push-required",
                "true",
                "--check-required",
                "false",
            ).returncode,
            0,
        )
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "phase",
                "committed",
                "--commit-head",
                commit_head,
            ).returncode,
            0,
        )

        recovered = self.run_command(
            str(repo / "runqueue.sh"), "--recover-only", "--no-check", cwd="/", env=env
        )

        self.assertEqual(recovered.returncode, 0, recovered.stderr)
        remote_unrelated = self.run_command(
            "git", "--git-dir", str(remote), "show-ref", "--verify", "refs/heads/unrelated"
        )
        self.assertNotEqual(remote_unrelated.returncode, 0)
        remote_head = self.run_command("git", "--git-dir", str(remote), "rev-parse", "refs/heads/main")
        self.assertEqual(remote_head.stdout.strip(), commit_head)

    def test_push_remote_uses_the_current_branch_under_simple_mode(self) -> None:
        root, repo, state, env = self.make_pipeline_fixture()
        origin = root / "origin.git"
        publish = root / "publish.git"
        self.assertEqual(self.run_command("git", "init", "--bare", "-q", str(origin)).returncode, 0)
        self.assertEqual(self.run_command("git", "init", "--bare", "-q", str(publish)).returncode, 0)
        self.assertEqual(self.git(repo, "remote", "add", "origin", str(origin)).returncode, 0)
        self.assertEqual(self.git(repo, "remote", "add", "publish", str(publish)).returncode, 0)
        self.assertEqual(self.git(repo, "push", "-qu", "origin", "main").returncode, 0)
        self.assertEqual(self.git(repo, "config", "branch.main.merge", "refs/heads/trunk").returncode, 0)
        self.assertEqual(self.git(repo, "config", "branch.main.pushRemote", "publish").returncode, 0)
        base_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        registry_path = repo / "content" / "registry.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["chapters"][0]["status"] = "draft"
        registry_path.write_text(json.dumps(registry), encoding="utf-8")
        (repo / "src" / "chapters" / "sample.mdx").write_text("# Sample\n", encoding="utf-8")
        self.assertEqual(self.git(repo, "add", "-A").returncode, 0)
        self.assertEqual(self.git(repo, "commit", "-qm", "build: sample -- Sample").returncode, 0)
        commit_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "begin",
                "--action",
                "build",
                "--slug",
                "sample",
                "--title",
                "Sample",
                "--base-head",
                base_head,
                "--push-required",
                "true",
                "--check-required",
                "false",
            ).returncode,
            0,
        )
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "phase",
                "committed",
                "--commit-head",
                commit_head,
            ).returncode,
            0,
        )

        recovered = self.run_command(
            str(repo / "runqueue.sh"), "--recover-only", "--no-check", cwd="/", env=env
        )

        self.assertEqual(recovered.returncode, 0, recovered.stderr)
        publish_main = self.run_command(
            "git", "--git-dir", str(publish), "rev-parse", "refs/heads/main"
        )
        self.assertEqual(publish_main.stdout.strip(), commit_head)
        publish_trunk = self.run_command(
            "git", "--git-dir", str(publish), "show-ref", "--verify", "refs/heads/trunk"
        )
        self.assertNotEqual(publish_trunk.returncode, 0)

    def test_reconciliation_requires_every_push_url_to_succeed(self) -> None:
        root, repo, state, env = self.make_pipeline_fixture()
        first = root / "first.git"
        missing = root / "missing" / "second.git"
        self.assertEqual(self.run_command("git", "init", "--bare", "-q", str(first)).returncode, 0)
        self.assertEqual(self.git(repo, "remote", "add", "origin", str(first)).returncode, 0)
        self.assertEqual(self.git(repo, "push", "-qu", "origin", "main").returncode, 0)
        self.assertEqual(self.git(repo, "remote", "set-url", "--add", "--push", "origin", str(first)).returncode, 0)
        self.assertEqual(self.git(repo, "remote", "set-url", "--add", "--push", "origin", str(missing)).returncode, 0)
        base_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        registry_path = repo / "content" / "registry.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["chapters"][0]["status"] = "draft"
        registry_path.write_text(json.dumps(registry), encoding="utf-8")
        (repo / "src" / "chapters" / "sample.mdx").write_text("# Sample\n", encoding="utf-8")
        self.assertEqual(self.git(repo, "add", "-A").returncode, 0)
        self.assertEqual(self.git(repo, "commit", "-qm", "build: sample -- Sample").returncode, 0)
        commit_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "begin",
                "--action",
                "build",
                "--slug",
                "sample",
                "--title",
                "Sample",
                "--base-head",
                base_head,
                "--push-required",
                "true",
                "--check-required",
                "false",
            ).returncode,
            0,
        )
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "phase",
                "committed",
                "--commit-head",
                commit_head,
            ).returncode,
            0,
        )

        recovered = self.run_command(
            str(repo / "runqueue.sh"),
            "--recover-only",
            "--no-check",
            "--max-push-attempts",
            "1",
            cwd="/",
            env=env,
        )

        self.assertEqual(recovered.returncode, 69, recovered.stderr)
        self.assertTrue((state / "transaction.json").exists())
        first_head = self.run_command("git", "--git-dir", str(first), "rev-parse", "refs/heads/main")
        self.assertEqual(first_head.stdout.strip(), commit_head)

    def test_committed_recovery_enforces_the_critique_round_limit(self) -> None:
        _root, repo, state, env = self.make_pipeline_fixture()
        registry_path = repo / "content" / "registry.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["chapters"][0]["status"] = "draft"
        registry_path.write_text(json.dumps(registry), encoding="utf-8")
        (repo / "src" / "chapters" / "sample.mdx").write_text("# Sample\n", encoding="utf-8")
        self.assertEqual(self.git(repo, "add", "-A").returncode, 0)
        self.assertEqual(self.git(repo, "commit", "-qm", "draft setup").returncode, 0)
        base_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        critique = repo / "content" / "critiques" / "sample.md"
        critique.parent.mkdir(parents=True)
        critique.write_text(
            "verdict: revise\n\n" + "\n".join(f"## Critique round {n}" for n in range(1, 7)) + "\n",
            encoding="utf-8",
        )
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "begin",
                "--action",
                "critique",
                "--slug",
                "sample",
                "--title",
                "Sample",
                "--base-head",
                base_head,
                "--push-required",
                "false",
                "--check-required",
                "false",
            ).returncode,
            0,
        )
        self.assertEqual(self.git(repo, "add", "-A").returncode, 0)
        self.assertEqual(self.git(repo, "commit", "-qm", "critique: sample -- revise").returncode, 0)
        commit_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "phase",
                "committed",
                "--commit-head",
                commit_head,
            ).returncode,
            0,
        )

        recovered = self.run_command(
            str(repo / "runqueue.sh"),
            "--recover-only",
            "--no-check",
            "--no-push",
            "--max-review-rounds",
            "6",
            cwd="/",
            env=env,
        )

        self.assertEqual(recovered.returncode, 1, recovered.stderr)
        self.assertIn("configured limit", recovered.stderr)
        transaction = json.loads((state / "transaction.json").read_text(encoding="utf-8"))
        self.assertEqual(transaction["phase"], "halted")
        self.assertIn("configured limit", transaction["halt_reason"])
        repeated = self.run_command(
            str(repo / "runqueue.sh"),
            "--recover-only",
            "--no-check",
            "--no-push",
            "--max-review-rounds",
            "6",
            cwd="/",
            env=env,
        )
        self.assertEqual(repeated.returncode, 1, repeated.stderr)
        self.assertIn("configured limit", repeated.stderr)

    def test_recovered_completion_counts_toward_count_limit(self) -> None:
        _root, repo, state, env = self.make_pipeline_fixture()
        registry_path = repo / "content" / "registry.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["chapters"][0]["status"] = "draft"
        registry["chapters"].append(
            {"num": 2, "slug": "second", "title": "Second", "status": "pending"}
        )
        registry_path.write_text(json.dumps(registry), encoding="utf-8")
        queue_path = repo / "prompts" / "queue.md"
        queue_path.write_text(
            "| # | slug | item | status |\n"
            "|---|---|---|---|\n"
            "| 1 | sample | Sample | PENDING |\n"
            "| 2 | second | Second | PENDING |\n",
            encoding="utf-8",
        )
        (repo / "src" / "chapters" / "sample.mdx").write_text("# Sample\n", encoding="utf-8")
        self.assertEqual(self.git(repo, "add", "-A").returncode, 0)
        self.assertEqual(self.git(repo, "commit", "-qm", "draft setup").returncode, 0)
        base_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "begin",
                "--action",
                "critique",
                "--slug",
                "sample",
                "--title",
                "Sample",
                "--base-head",
                base_head,
                "--push-required",
                "false",
                "--check-required",
                "false",
            ).returncode,
            0,
        )
        registry["chapters"][0]["status"] = "done"
        registry_path.write_text(json.dumps(registry), encoding="utf-8")
        queue_path.write_text(
            "| # | slug | item | status |\n"
            "|---|---|---|---|\n"
            "| 1 | sample | Sample | DONE |\n"
            "| 2 | second | Second | PENDING |\n",
            encoding="utf-8",
        )
        critique = repo / "content" / "critiques" / "sample.md"
        critique.parent.mkdir(parents=True)
        critique.write_text("verdict: approve\n\n## Critique round 1\n", encoding="utf-8")
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "phase",
                "ready",
            ).returncode,
            0,
        )

        recovered = self.run_command(
            str(repo / "runqueue.sh"),
            "--count",
            "1",
            "--no-check",
            "--no-push",
            "--yes",
            cwd="/",
            env=env,
        )

        self.assertEqual(recovered.returncode, 0, recovered.stderr)
        self.assertIn("reached limit of 1", recovered.stdout)
        final_registry = json.loads(registry_path.read_text(encoding="utf-8"))
        self.assertEqual(final_registry["chapters"][1]["status"], "pending")

    def test_recovery_adopts_the_exact_commit_created_before_journal_update(self) -> None:
        _root, repo, state, env = self.make_pipeline_fixture()
        base_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        registry_path = repo / "content" / "registry.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["chapters"][0]["status"] = "draft"
        registry_path.write_text(json.dumps(registry), encoding="utf-8")
        (repo / "src" / "chapters" / "sample.mdx").write_text("# Sample\n", encoding="utf-8")
        begin = self.run_command(
            sys.executable,
            str(repo / "scripts" / "runqueue_state.py"),
            "--dir",
            str(state),
            "begin",
            "--action",
            "build",
            "--slug",
            "sample",
            "--title",
            "Sample",
            "--base-head",
            base_head,
            "--push-required",
            "false",
            "--check-required",
            "false",
        )
        self.assertEqual(begin.returncode, 0, begin.stderr)
        ready = self.run_command(
            sys.executable,
            str(repo / "scripts" / "runqueue_state.py"),
            "--dir",
            str(state),
            "phase",
            "ready",
        )
        self.assertEqual(ready.returncode, 0, ready.stderr)
        self.assertEqual(self.git(repo, "add", "-A").returncode, 0)
        self.assertEqual(
            self.git(repo, "commit", "-qm", "build: sample -- Sample").returncode,
            0,
        )
        commit_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()

        recovered = self.run_command(
            str(repo / "runqueue.sh"),
            "--recover-only",
            "--no-check",
            "--no-push",
            cwd="/",
            env=env,
        )

        self.assertEqual(recovered.returncode, 0, recovered.stderr)
        self.assertEqual(self.git(repo, "rev-parse", "HEAD").stdout.strip(), commit_head)
        self.assertFalse((state / "transaction.json").exists())

    def test_recovery_rejects_a_matching_commit_that_contains_an_unrelated_path(self) -> None:
        _root, repo, state, env = self.make_pipeline_fixture()
        base_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        registry_path = repo / "content" / "registry.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["chapters"][0]["status"] = "draft"
        registry_path.write_text(json.dumps(registry), encoding="utf-8")
        (repo / "src" / "chapters" / "sample.mdx").write_text("# Sample\n", encoding="utf-8")
        (repo / "unrelated.txt").write_text("must not be adopted\n", encoding="utf-8")
        begin = self.run_command(
            sys.executable,
            str(repo / "scripts" / "runqueue_state.py"),
            "--dir",
            str(state),
            "begin",
            "--action",
            "build",
            "--slug",
            "sample",
            "--title",
            "Sample",
            "--base-head",
            base_head,
            "--push-required",
            "false",
            "--check-required",
            "false",
        )
        self.assertEqual(begin.returncode, 0, begin.stderr)
        self.assertEqual(
            self.run_command(
                sys.executable,
                str(repo / "scripts" / "runqueue_state.py"),
                "--dir",
                str(state),
                "phase",
                "ready",
            ).returncode,
            0,
        )
        self.assertEqual(self.git(repo, "add", "-A").returncode, 0)
        self.assertEqual(self.git(repo, "commit", "-qm", "build: sample -- Sample").returncode, 0)

        recovered = self.run_command(
            str(repo / "runqueue.sh"),
            "--recover-only",
            "--no-check",
            "--no-push",
            cwd="/",
            env=env,
        )

        self.assertEqual(recovered.returncode, 1, recovered.stderr)
        self.assertIn("unexpected committed path", recovered.stderr)
        self.assertTrue((state / "transaction.json").exists())

    def test_resumed_transaction_with_exhausted_attempts_halts_instead_of_spinning(self) -> None:
        _root, repo, state, env = self.make_pipeline_fixture()
        base_head = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        begin = self.run_command(
            sys.executable,
            str(repo / "scripts" / "runqueue_state.py"),
            "--dir",
            str(state),
            "begin",
            "--action",
            "build",
            "--slug",
            "sample",
            "--title",
            "Sample",
            "--base-head",
            base_head,
            "--push-required",
            "false",
            "--check-required",
            "false",
        )
        self.assertEqual(begin.returncode, 0, begin.stderr)
        attempted = self.run_command(
            sys.executable,
            str(repo / "scripts" / "runqueue_state.py"),
            "--dir",
            str(state),
            "phase",
            "agent",
            "--attempt",
            "1",
        )
        self.assertEqual(attempted.returncode, 0, attempted.stderr)

        resumed = self.run_command(
            str(repo / "runqueue.sh"),
            "--no-check",
            "--no-push",
            "--yes",
            "--max-agent-attempts",
            "1",
            cwd="/",
            env=env,
            timeout=3,
        )

        self.assertEqual(resumed.returncode, 1, resumed.stderr)
        self.assertIn("already exhausted", resumed.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
