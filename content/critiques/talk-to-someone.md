verdict: resolved

## Critique round 1 — 2026-07-27

### Required

1. **Make Figure 123.4's labels legible.** The `Spectrum` at
   `src/chapters/talk-to-someone.mdx:97-110` uses the primitive's default inline
   endpoint layout. That puts both long endpoint labels on `y=74`, with "known, even
   if painful" extending right from `x=40` and "new, not yet familiar" extending
   left from `x=340`; they meet and overlap near the center. The marker label "the
   uneasy middle" is then centered at `x=190`, `y=78`, on top of both endpoint
   labels. Scaling or horizontal scrolling preserves the collision because all
   three positions are fixed in the SVG viewBox. Use the primitive's existing
   collision-avoidance layout, such as its stacked endpoint mode, and verify that
   all three labels remain distinct at phone width.

2. **Correct the Hero reading-time badge from the rendered page.** A direct static
   render of this exact draft contains 1,290 reader-visible words, including the
   Hero and cover metadata, headings, captions, diagram labels, exercise titles,
   and nearby-book footer. At the authoring spec's approximately 200 words per
   minute, rounded up, this is a seven-minute distillation, not `minutes={6}` at
   `src/chapters/talk-to-someone.mdx:5-9`.

3. **Complete the `talk-to-someone` registry record.** The entry at
   `content/registry.json:2430-2438` stops after `status: "draft"` and omits the
   authoring contract's required tier, thesis, framework, and diagram inventory.
   Record tier 3, a chapter-aligned thesis, the brief-supported absence of a single
   signature model, and the five rendered forms in page order: iceberg, comparison,
   process loop, spectrum, and flow.

### Advisory

None. The brief and recorded evidence support the dual therapist-and-patient
perspective, narrative revision, therapeutic relationship, recurring patterns, and
loss within desired change used in the page. The draft presents these ideas as an
original synthesis, reproduces no source figure or cover art, and does not make the
reflection exercises into a diagnosis or universal treatment protocol. This review
began no new external web search.

`npm run check` completed with `CHECK OK` on 2026-07-27. Repository validation,
prose lint, all 40 pipeline and runner tests, all 262 Vitest tests, TypeScript, the
Vite production build, and ESLint passed. Vitest emitted only the existing
non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-27

Resolved every required finding from round 1:

- Figure 123.4 now uses Spectrum's `endpointLabelLayout="stacked"` and
  `markerLabelPlacement="top"`, keeping both wrapped endpoint labels below the
  top marker label and distinct within the fixed SVG at phone width.
- The Hero badge now uses `minutes={7}`, matching the recorded 1,290-word rendered
  count at approximately 200 words per minute, rounded up.
- The `talk-to-someone` registry record now includes tier 3, a chapter-aligned
  thesis, the deliberate absence of a single signature model, and the five rendered
  diagram forms in page order: iceberg, comparison, process loop, spectrum, and
  flow. Its status remains `draft` pending independent re-review.
