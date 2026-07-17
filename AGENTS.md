# AGENTS.md --- the library

This repo is a **queue-built reference site**: a Vite + React + TypeScript + MDX
site on Vercel, built from the `darvinyi-refsite-template`. Each item in the queue
is one non-fiction book, distilled one at a time. This file is thin. The build loop
and queue verbs live in a skill; the content contract lives in `docs/`.

## What this site is

A library of distilled non-fiction. Each page takes one educational non-fiction book
and compresses its **ideas** into original prose and original diagrams. It never
reproduces the book's text or the author's figures. A reader should leave
understanding the core argument, the central framework, and how to use it, without
having read a line of the original. The landing page is a library of shelves; a book
that wants reading is bought at the link out.

The copyright line is non-negotiable and is stated in full in `docs/authoring-spec.md`:
distill ideas, never reproduce expression, no close paraphrase, at most one short
attributed epigraph, no real cover art.

## Use the library-runner skill

The build loop, queue verbs, and definition of done live in the checked-in
**`library-runner`** skill. When I say
**"run the next one"**, **"run the next N"**, **"queue status"**, **"add X"**,
**"reprioritize"**, or **"rerun <slug>"**, follow that skill. If it is not
installed, tell me before improvising.

## What "run the next one" means in this repo

The next item is the first `PENDING` row in `prompts/queue.md`.

- **The first item is `about` (num 0). It is the bootstrap, not a book.** Building it
  stands up the whole library shell: the diagram primitive components, the generated
  typographic cover, the library landing page, and the shared book-page layout. Its
  full instructions are in `prompts/notes/about.md`. Run it first. Visual review with
  `npm run dev` is an operator decision, never an unattended agent step.
- **Every item after `about` is one book.** For a book, read its brief at
  `prompts/notes/<slug>.md` (thesis, signature model, any credibility caveat), then
  build the page following `docs/authoring-spec.md` for the anatomy and
  `docs/diagram-vocabulary.md` for the diagram forms. Treat the first book,
  `atomic-habits`, as the content reference to review before batch-running the rest.

A Terra builder may mark an item `draft` only after `npm run check` passes. A separate
Sol critic grants `done` through an approving critique and `scripts/mark.py`. The
headless runner owns per-stage commits and pushes the accumulated commits only when the
chapter is approved as done; interactive work does not push unless explicitly asked.

## The content contract (project-specific, in docs/)

- `docs/authoring-spec.md` --- the quality contract: the fixed 9-section page anatomy
  (Hero, Thesis, optional Why It Matters, Key Ideas with a diagram each, The Model,
  Put It To Work, optional Where People Get It Wrong, If You Remember One Thing,
  Shelved Nearby), the house voice, the copyright line, the section-to-component
  mapping, and the definition of done.
- `docs/diagram-vocabulary.md` --- the fixed set of diagram forms. Every key-idea
  visual and every hero Model diagram picks a form from this list. Add a form here
  (with a component) before using one that is not listed.

Diagrams are the point of this site. Every key idea gets an original in-vocabulary
diagram in house style, hand-authored inline SVG, no diagramming or charting
library.

## Where things live in this repo

- `prompts/queue.md` --- the ordered run list. Next item is the first PENDING row.
- `prompts/notes/<slug>.md` --- the per-item brief a run reads (`about.md` is the
  bootstrap brief; one file per book).
- `content/registry.json` --- the database: which books exist, their order, shelf
  (`part`), and status.
- `prompts/_books.py` --- the seed source of truth (title, author, year, shelf, tier,
  thesis, model, caveat) for every book.
- `prompts/_generate.py` --- regenerates `registry.json`, `queue.md`, and any missing
  note briefs from `_books.py`. Re-running preserves existing statuses and does not
  overwrite edited briefs. Use it after adding books to `_books.py`.
- `src/chapters/<slug>.mdx` --- book prose. A book is one "chapter" slot.
- `src/components/diagrams/` --- the diagram primitive library (built by the scaffold).
- `src/components/book/` --- book-page section helpers: `Hero`, `ShelvedNearby`.
- `src/components/` --- shared template primitives: `Figure`, `Widget`,
  `ExerciseCard`, `Callout`.
- `src/styles/tokens.css` --- the house style, source of truth. Do not restyle it.
- `scripts/` --- repo-owned tooling: `validate.py`, `decide.py`, `prose_lint.py`,
  `new_chapter.py`, `mark.py`, `check.sh`, `sitemap.mjs`.
- `.codex/agents/` --- project role definitions: Terra builder/resolver and Sol critic,
  all with high reasoning effort.

## House rules

- Match `src/styles/tokens.css` exactly. Prose has no em dashes and none of the AI
  tells in `prose-lint.config.json` (the gate fails the build on them).
- `npm run check` is the mechanical gate. A done item also needs `verdict: approve` in
  `content/critiques/<slug>.md`.
- Builders and resolvers use `gpt-5.6-terra` at high effort. Critics use
  `gpt-5.6-sol` at high effort. Agents never commit or push; `runqueue.sh` does.

## Adding to the queue later

Add the book to `prompts/_books.py` (and to `STAGE_1` if it belongs in the launch
shelf), then run `python3 prompts/_generate.py`. Or use the skill's "add X" verb,
which appends a PENDING row and a matching registry entry. Either way, `validate.py`
must stay green (queue and registry list the same slugs in the same order).
