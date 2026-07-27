verdict: revise

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
