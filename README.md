# darvinyi-library

A Codex-built library of non-fiction ideas. Each page distills a book into original
prose, diagrams, caveats, and practice. It never reproduces book text, cover art, or
author figures.

## Local development

```bash
npm install
npm run dev
npm run check
```

`npm run check` validates the queue and critique state, lints prose, renders every
chapter, builds the site, and runs advisory ESLint.

## The Codex workflow

The repository owns a three-stage lifecycle:

1. **Terra** (`gpt-5.6-terra`, high effort) researches and builds one pending book,
   then marks it `draft`.
2. **Sol** (`gpt-5.6-sol`, high effort) independently critiques the draft. Only Sol
   can approve a book and mark it `done`.
3. **Terra** resolves any required findings, after which Sol re-reviews.

The project defaults and role definitions live in `.codex/`. The reusable queue
workflow is `.agents/skills/library-runner/`. Read [AGENTS.md](AGENTS.md) for the
durable repository contract and [docs/authoring-spec.md](docs/authoring-spec.md) for
the content contract.

Run one completed lifecycle locally:

```bash
./runqueue.sh --count 1 --no-push
```

Run the unattended queue with automatic commits and pushes:

```bash
./runqueue.sh --all --yes
```

The driver journals each action before model work, retries incomplete model attempts,
and recovers interrupted validated or committed work before starting anything new.
Every model attempt has a two-hour hard timeout. Git, scope, project checks, commit,
and push are mandatory gates. Push attempts and repeated critique cycles are bounded;
the default critique ceiling is six revise rounds. Use `--dry-run` to inspect the
active models and next action, and `--no-push` to retain commits locally.

## Keep the queue running on macOS

Install the per-user LaunchAgent once to run until the queue drains. A persistent marker
keeps transient failures alive across restarts, while deterministic validation or scope
failures halt with a durable status instead of looping. Crashes also restart. A clean
queue drain removes the marker and stays stopped.

```bash
bash scripts/install-runqueue-launchd.sh
```

Check the service, transaction, queue, and worktree in one command:

```bash
bash scripts/runqueue-status.sh
```

Agent transcripts and the durable transaction journal live under
`~/Library/Application Support/darvinyi-library/runqueue/`. Launch logs live under
`~/Library/Logs/` and are rotated whenever the service is reinstalled.

Remove the service when you want the queue to stop:

```bash
bash scripts/uninstall-runqueue-launchd.sh
```

## State and tooling

- `content/registry.json` and `prompts/queue.md` are the ordered source of truth.
- `content/critiques/<slug>.md` is append-only review history. A `done` chapter needs
  `verdict: approve` on its first line.
- `scripts/decide.py status` reports the next build, critique, or resolution action.
- `scripts/mark.py` atomically changes registry and queue status.
- `src/chapters/` holds book pages; `src/components/diagrams/` holds reusable SVG
  primitives.

## Deploy

Push `main` to GitHub and import the repository in Vercel with the Vite preset and
`dist` output directory. `vercel.json` includes the SPA rewrite for book routes.
