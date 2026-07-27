verdict: approve

## Critique round 1 — 2026-07-27

### Required

1. **Make the central labels in Figure 101.6 legible.** The directed edge from
   `notice` to `date` places “follow” at approximately `(190, 163)`, while the
   vertical edge from `work` to `pages` places “notice again” at approximately
   `(190, 158)`. Both use 12-unit type, so the labels overlap at the center of the
   model instead of teaching the two-tool loop clearly. Use the existing
   chapter-level `labelOffset` support, change the node/edge composition, or
   otherwise separate the labels without editing the shared diagram primitive.

2. **Recompute the Hero reading-time badge from the rendered page.** A direct static
   render of this exact draft contains approximately 1,491 visible alphanumeric
   words, including the Hero, headings, captions, diagram labels, exercise titles,
   callout, and nearby-book footer. At the authoring spec's approximately 200 words
   per minute, rounded up, the page is an eight-minute distillation, not
   `minutes={7}`.

3. **Complete the `artists-way` registry record required for a done chapter.** The
   draft entry has number, slug, title, author/year subtitle, shelf, routes, and
   status, but it omits `tier`, `thesis`, `framework`, and `diagrams`. Definition of
   done item 7 requires those fields. Record the chapter's actual thesis, the
   morning-pages-and-artist-dates framework, and the six forms used by this page.

### Advisory

None.

### Evidence checked

- The chapter brief and recorded evidence support the attribution of a twelve-week
  creative-recovery program, private longhand morning freewriting, recurring solo
  artist dates, and the framing of these as repeatable practices. The draft keeps
  the book's spiritual and clinical limits explicit and does not claim that the
  practices guarantee creative or mental-health outcomes.
- The page uses original prose and vocabulary-based conceptual diagrams rather than
  quoted text, copied organization, cover art, or a reproduced source figure. The
  five key ideas, distinct Model section, concrete practice cards, caveat, final
  takeaway, direct publisher link, route, and three related completed chapters are
  otherwise intact.
- `npm run check` passed on 2026-07-27: queue/registry/content validation, prose lint,
  42 pipeline and runner tests, 211 Vitest tests, TypeScript/Vite production build,
  and ESLint all completed successfully. Vitest emitted only the existing non-failing
  `Window.scrollTo()` notices.

## Builder resolution — 2026-07-27

1. Kept the shared `NodeGraph` primitive unchanged and separated Figure 101.6's two
   central labels with its chapter-level `labelOffset` support. `follow` now sits 16
   units above the horizontal connection, while `notice again` sits 18 units below
   its previous vertical-connection position, so each relationship remains legible.

2. Changed the Hero badge from `7-min` to `8-min`, matching the recorded rendered
   count of approximately 1,491 visible alphanumeric words at roughly 200 words per
   minute, rounded up.

3. Completed the draft `artists-way` registry entry with tier 2, the recorded thesis,
   the Morning Pages and Artist Dates framework, and the six rendered forms in page
   order: iceberg, comparison, flow, Venn overlap, spectrum, and node graph. The
   chapter remains `draft` and its queue row remains `PENDING`.

4. `npm run check` passed on 2026-07-27 after the chapter and registry fixes:
   validation, prose lint, pipeline tests, Vitest, TypeScript/Vite production build,
   and ESLint completed successfully.

## Critique round 2 — 2026-07-27

### Required

None. All three round-one findings are resolved. Figure 101.6 now separates the
central edge labels, with `follow` above the horizontal connection and
`notice again` below it. The Hero declares eight minutes, consistent with the
recorded approximately 1,491 reader-visible words at roughly 200 words per minute,
rounded up. The registry entry now records tier 2, the brief's thesis, the
Morning Pages and Artist Dates framework, and the six diagram forms used in page
order.

The independent reread found no unsupported factual claim that changes the reader's
understanding. The chapter stays within the brief and recorded evidence when it
describes private longhand morning freewriting, recurring solo artist dates, and
their use as repeatable creativity practices. Its clinical caveat appropriately
limits the promise of those practices. The prose and diagrams are original, the
five key ideas each have a captioned in-vocabulary figure, the signature model and
four concrete exercises are present, the generated cover path is intact, and all
three related slugs resolve to completed chapters.

`npm run check` passed on 2026-07-27: queue, registry, critique, and content
validation; prose lint; 42 pipeline and runner tests; 211 Vitest tests; TypeScript
and the Vite production build; and ESLint all completed successfully. Vitest emitted
only the existing non-failing jsdom `Window.scrollTo()` notices.

### Advisory

None.
