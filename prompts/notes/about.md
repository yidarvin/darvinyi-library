# about  (num 0, the bootstrap)

This is the first item in the queue and it is not a book. Building it stands up the
whole library shell so that every book run afterward is pure content. Do all of the
following in one run, then stop for review. Do not build any book in this run.

Read first: `docs/authoring-spec.md` (the page anatomy, voice, and copyright line)
and `docs/diagram-vocabulary.md` (the fixed set of diagram forms). The running house
style is `src/styles/tokens.css`; treat it as source of truth and do not restyle it
(near-black `--bg`, teal `--accent`, JetBrains Mono structural, Inter prose).

## 1. Clear the template's demo content

This repo was instantiated from the refsite template, which ships a demo chapter.
Remove it so the registry, the queue, and the files on disk agree:

- delete `src/chapters/how-this-book-is-built.mdx`
- delete `src/chapters/_figures/Pipeline.tsx`
- delete `src/chapters/_widgets/QueueBoard.tsx`

The registry and queue in this repo already describe the library (an `about` page
plus the book queue) and do not list the demo chapter, so once the file is gone
`python3 scripts/validate.py` will be clean.

## 2. Build the diagram primitive library

Create one reusable, hand-authored inline-SVG React component per form in
`docs/diagram-vocabulary.md`, under `src/components/diagrams/`. At minimum:

`ProcessLoop`, `Matrix` (2x2), `Pyramid`, `Spectrum`, `Concentric`, `Flow`,
`Curve` (with shapes exp/log/s/u/bell/channel), `Compare`, `Iceberg`, `Venn`,
`NodeGraph`, `Timeline`, `Bars`.

Rules: no diagramming or charting library, no D3; SVG returned from a component.
Colors and fonts resolve to the tokens (`--accent` for the one accent, muted grays
for secondary strokes, JetBrains Mono for structural labels, Inter for prose
labels). Each is data-driven through props so a book page composes and labels it
without touching raw SVG. Everything must be legible at 360px wide. Give each a
minimal prop type and a sensible default render. Add a short `src/components/diagrams/README.md`
listing the forms and their props so book runs can pick from it quickly.

## 3. Build the generated typographic cover

Create a `BookCover` component that renders a deterministic, typographic cover from
a book's registry meta (title, author, shelf): teal-on-near-black, JetBrains Mono
title treatment, no image, no real cover art ever. Deterministic means the same
book always renders the same cover (derive any accent variation from a hash of the
slug, staying within the palette). It is used both on the library landing grid and
at the top of each book page. Make it work at cover size (grid tile) and at hero
size.

## 4. Rebuild the landing page as a library

Replace `src/pages/Home.tsx` so the landing page reads like a library rather than a
linear table of contents. Drive it entirely from `content/registry.json`:

- Group books by `part` (the shelf). Render each shelf as a labeled section with
  its books as a responsive grid of `BookCover` tiles.
- A book whose status is `done` links to `/<slug>`. A book still `pending` renders
  as a dimmed, unlinked tile (an "in the stacks" treatment) so the full shape of
  the library is visible from day one and fills in as the queue runs.
- Keep the site title and subtitle from the registry at the top. Exclude the
  `about` entry from the shelves; link to it from a small header or footer link.
- Preserve the existing grouping helper's behavior (books already arrive grouped by
  shelf in registry order).

Keep the existing routing: `/<slug>` already renders a chapter/book page via
`src/pages/Chapter.tsx`. If the book page needs the registry meta (it does, for the
Hero cover), read it through `src/lib/registry.ts`.

## 5. Add the book-page section scaffold

So every book page shares one anatomy, add a few small components under
`src/components/book/`:

- `Hero` — renders the `BookCover` at hero size plus title, author, year, shelf tag,
  the one-line thesis, and an "N-min distillation" badge (accept N as a prop; the
  book run computes it from rendered length).
- `ShelvedNearby` — renders the cross-link footer: related built books plus the
  outbound link to the real book at a bookseller.

The remaining sections (Thesis, Why It Matters, Key Ideas, The Model, Put It To
Work, Where People Get It Wrong, If You Remember One Thing) are plain MDX headings
and prose composed with the existing `Figure`, `ExerciseCard`, and `Callout`
components. Do not over-engineer this into a rigid framework; these are light
helpers, and the anatomy in `docs/authoring-spec.md` governs.

## 6. Write the about page

Write `src/chapters/about.mdx`: a short page explaining what the library is and how
to read it. Cover, in house voice: that each page distills a book's ideas into
original prose and original diagrams and never reproduces the text or the author's
figures; that pages are organized by our own logic, not the book's chapter order;
that the diagrams are original recreations of the concepts; that the library grows
one book at a time from a queue; and that a reader who wants a book should buy it
(the pages link out). This page doubles as proof that the pipeline works end to end:
it should use at least one `Figure` with a real diagram primitive so the primitive
library is exercised.

## 7. Verify, mark, stop

Run `npm run check` and make it pass (validate.py, prose_lint.py, typecheck, build).
Then mark `about` done: status `done` in `content/registry.json` and `DONE` in
`prompts/queue.md` (use `scripts/mark.py` if present, else edit both). Commit. Do
not push or deploy unless asked.

Then stop and hand back for review with `npm run dev`. This run establishes the
reference aesthetic for the whole library, so it is worth a careful look before any
book is built. The next queue item after `about` is `atomic-habits`; treat that
first book as the content reference to review before batch-running the rest.
