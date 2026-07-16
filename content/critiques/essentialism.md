verdict: approve

## Critique round 1 — 2026-07-16

### REQUIRED

1. **Recompute the Hero reading-time badge from the final rendered page.** A direct
   render contains 1,246 reader-visible words, including the Hero, headings,
   captions, SVG labels, exercise titles, generated cover metadata, and the nearby
   footer. At the authoring spec's approximately 200 words per minute, rounded up,
   this is a seven-minute distillation, not `minutes={8}`
   (`src/chapters/essentialism.mdx:5-9`). Set the badge to seven minutes and
   recompute it if the rendered text changes during resolution.

### ADVISORY

None. Within the repository's bounded evidence, the brief supports the central
fewer-but-better thesis and the deliberate absence of a Model section. The draft
uses original thematic prose and six distinct shared-vocabulary figures rather than
quotation, real cover art, close source-order imitation, or reproduction of a book
figure. Its thesis is clear, its practice cards are concrete, its optional caveat is
responsible without adding an unsupported empirical claim, and all related slugs
resolve to completed chapters. No separate chapter-specific evidence dossier or
source excerpts are recorded, and this review began no new external web search.
`npm run check` passed on 2026-07-16, including validation, prose lint, pipeline
tests, 110 application tests, typecheck, production build, and lint.

## Builder resolution — 2026-07-16

- Changed the Essentialism Hero badge from `minutes={8}` to `minutes={7}`. The
  critique's recorded final rendered count is 1,246 reader-visible words, which rounds
  up to seven minutes at the house rate of approximately 200 words per minute.
- This correction changes only the badge value. No reader-visible prose, diagrams,
  links, or prior content decisions were changed.

## Critique round 2 — 2026-07-16

### REQUIRED

None. The round 1 reading-time finding is resolved: the unchanged recorded render of
1,246 reader-visible words rounds up to seven minutes at the house rate of roughly 200
words per minute, and the Hero now declares `minutes={7}`.

### ADVISORY

None. The brief and seed record support the fewer-but-better thesis and the deliberate
absence of a signature Model section. The six key ideas each have a captioned,
in-vocabulary structural diagram whose labels agree with the prose, the practice cards
are concrete, the optional caveat is appropriately bounded, and all three nearby links
resolve to done chapters. The draft contains no quotation or real cover art and uses
shared diagram primitives with original labels rather than a bespoke reproduction of a
book figure. No separate chapter-specific evidence dossier or source excerpts are
recorded, and this review began no external web search. `npm run check` passed on
2026-07-16, including validation, prose lint, pipeline tests, 110 application tests,
typecheck, production build, and lint.
