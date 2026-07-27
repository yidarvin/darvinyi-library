verdict: resolved

## Critique round 1 — 2026-07-26

### Required

1. **Remove the unsupported reinforcing signal from the fear-and-preparation
   loop.** The prose supports a recurring practice: name a fear, test a bounded
   hardship, learn what remains possible, and use that preparation when another
   threat arrives (`src/chapters/letters-from-a-stoic.mdx:82-101`). Figure 93.3
   nevertheless passes `compoundingEdge={3}`, which the shared `ProcessLoop` API
   defines and renders as a reinforcing edge
   (`src/components/diagrams/ProcessLoop.tsx:8-11,71-85`). Neither the surrounding
   explanation nor Letters 18 and 24 in the recorded evidence establishes that
   meeting a threat compounds or positively reinforces the return to naming the
   next fear. Remove the compounding prop so the return is neutral, or replace the
   encoding with another relationship that the prose and bounded evidence support.

2. **Make Figure 93.2's pole and marker labels legible.** The chapter supplies
   `comfort as a requirement` and `comfort as a preference` as unwrapped pole
   labels and places the `enough` marker at 0.78
   (`src/chapters/letters-from-a-stoic.mdx:68-80`). The shared `Spectrum` places
   both pole labels on the same baseline from x=40 to x=340, then places the
   near-marker label only four SVG units lower
   (`src/components/diagrams/Spectrum.tsx:43-47,95-121`). At the component's
   monospaced font sizes, the two long pole labels overlap each other, and
   `enough` also overlaps the right pole label. The 440px minimum width scales the
   collision rather than separating the fixed viewBox coordinates, so the figure
   does not meet the phone-legibility contract. Shorten or otherwise recompose
   the chapter-local labels, and use the existing top marker-label placement if
   useful; do not change the shared component.

3. **Recompute the Hero reading-time badge from the rendered page.** A direct MDX
   render of this exact draft contains 1,477 reader-visible alphanumeric tokens,
   including generated Hero and cover metadata, headings, captions, diagram
   labels, exercise titles, prose, and the nearby-book footer. At the authoring
   contract's approximately 200 words per minute, rounded up, that is an
   eight-minute distillation, not `minutes={9}`
   (`src/chapters/letters-from-a-stoic.mdx:5-9`;
   `docs/authoring-spec.md:35-37`). Recompute after resolving the other findings
   and set the badge from the final rendered count.

### Advisory

1. Within the brief and bounded evidence, the central treatments of time,
   voluntary simplicity, examined fear, mortality, and humane conduct across rank
   are supportable. The thematic organization and diagrams are original
   synthesis; no quotation, source-figure reproduction, or close paraphrase that
   changes the copyright judgment is apparent. This review followed the recorded
   evidence links and began no new external web search.

2. Apart from the required diagram defects, the page follows the intended
   anatomy. Five key ideas each have a captioned vocabulary figure, the Model
   section is correctly absent and that reason is recorded in the registry, four
   practice cards specify observable actions, and the caveat addresses both
   harmful Stoic misreadings and Seneca's historical contradictions. All three
   nearby slugs resolve to done chapters, and the outbound publisher link matches
   the evidence record.

3. `npm run check` completed with `CHECK OK` on 2026-07-26. Validation and prose
   lint passed; the two pipeline tests, all 40 runner tests, all 193 Vitest tests,
   TypeScript, the Vite production build, and ESLint passed. Vitest emitted only
   the existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-26

- Removed `compoundingEdge={3}` from Figure 93.3. The Process Loop now encodes the
  evidence-supported recurring practice with neutral return arrows, without claiming
  that meeting a threat reinforces the next cycle.
- Re-composed Figure 93.2's poles as `comfort required` and `comfort preferred`, and
  set `markerLabelPlacement="top"`. The shorter endpoint labels no longer collide,
  and `enough` occupies its own line above the axis labels at phone width.
- Recomputed the final rendered reader-visible count from the critique's recorded
  1,477-token render: the two shortened labels remove four alphanumeric tokens,
  leaving 1,473. At approximately 200 words per minute, rounded up, the Hero now
  shows an 8-minute distillation.
