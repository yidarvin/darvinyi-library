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

The driver stops on a model error, failed gate, unexpected edit, dirty worktree,
timeout, push failure, or three unresolved critique rounds. Use `--dry-run` to inspect
the active models and next action, and `--no-push` to retain commits locally.

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
