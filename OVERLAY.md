# OVERLAY --- darvinyi-library

This bundle is the project-specific overlay for a **fresh instantiation of
`darvinyi-refsite-template`**. It contains only what is specific to the library: the
queue, the registry, the per-book briefs, the content contract, and the seed
generator. Everything else (the Vite/React/TS/MDX app, `scripts/`, `package.json`,
`vercel.json`) comes from the template. Delete this file once you have applied it.

## What's in here

```
CLAUDE.md                     # replaces the template's: project-specific, thin
content/registry.json         # replaces: about (num 0) + 146 books, all pending
prompts/queue.md              # replaces: same 147 rows, in build order
prompts/_books.py             # seed source of truth for every book
prompts/_generate.py          # regenerates registry.json + queue.md + notes
prompts/notes/about.md        # the bootstrap brief (builds the library shell)
prompts/notes/<slug>.md       # 146 per-book briefs
docs/authoring-spec.md        # the quality contract: page anatomy, voice, copyright
docs/diagram-vocabulary.md    # the fixed set of diagram forms
```

146 books across 14 shelves, tiered by canonical reach. Build order is the launch
shelf first (highest-reach Tier 1), then the rest of Tier 1, then Tier 2, then Tier
3; within a tier, grouped by shelf.

## Apply it

1. Create a repo from the template (GitHub "Use this template", or
   `gh repo create darvinyi-library --template yidarvin/darvinyi-refsite-template`),
   then clone it and `cd` in. Mirror to your Gitea remote if you want it on the NAS.
2. Unzip this overlay at the repo root. It overwrites `CLAUDE.md`,
   `content/registry.json`, and `prompts/queue.md`, and adds `docs/`,
   `prompts/notes/`, `prompts/_books.py`, and `prompts/_generate.py`.
3. `npm install`. Confirm the `refsite-runner` skill is installed at
   `~/.claude/skills/refsite-runner/`.

Note: `python3 scripts/validate.py` will report the template's demo chapter
(`how-this-book-is-built.mdx`) as an orphan until you build the first item. That is
expected; the bootstrap run deletes the demo content. You do not need a clean
validate before the first run.

## Run it

In Claude Code:

1. **"run the next one"** builds `about` (num 0). This is the bootstrap: it deletes
   the demo content, builds the diagram primitive library, the generated typographic
   cover, the library landing page, and the shared book-page layout, then writes the
   about page and marks itself done. Review with `npm run dev`. This sets the
   reference aesthetic for the whole library, so look before continuing.
2. **"run the next one"** again builds `atomic-habits`, the first book. Treat it as
   the content reference. Review it before batching.
3. Batch the rest. Either say **"run the next N"**, or run the headless loop below.

## Headless batch (ultracode)

Once the aesthetic is locked, drain the queue from the command line. Adapt to your
runner; the loop just keeps invoking "run the next one" while PENDING rows remain:

```bash
while grep -q '| PENDING |' prompts/queue.md; do
  claude -p "run the next one" \
    --model 'claude-opus-4-8[1m]' \
    --settings ultracode \
    --dangerously-skip-permissions
  npm run check || { echo "check failed, stopping for review"; break; }
done
```

The per-run `npm run check` gate means a bad run stops the batch instead of
compounding. Review periodically with `npm run dev`, and commit/push/deploy on your
own terms (the runner does not push or deploy unless told).

## Adding books later

Add entries to `prompts/_books.py` (and to `STAGE_1` for the launch shelf), then
`python3 prompts/_generate.py`. It rewrites the registry and queue while preserving
the status of everything already built, and writes briefs only for new books. Keep
`validate.py` green.
