verdict: approve

## Critique round 1 — 2026-07-16

### Required

1. **Compress "The thesis" to the required one or two sentences.** The paragraph at
   `src/chapters/thinking-in-bets.mdx:13` contains three sentences. The authoring
   spec reserves this section for the single compact argument a reader can carry
   away. Preserve uncertainty, explicit belief, revision, and process-over-result,
   but combine them into no more than two sentences.

2. **Make Figure 48.6 depict both directions claimed by its key idea and caption.**
   The prose at `src/chapters/thinking-in-bets.mdx:138` teaches both a premortem and
   working backward from success, and the caption says the figure exposes
   assumptions from failure and success. The rendered flow only shows `imagine
   failure`, `name weak assumptions`, and two risk-response branches. It contains no
   successful future, required condition, or positive early sign. Recompose the
   chapter-local visual with an in-vocabulary form that visibly includes both
   backward-looking paths, or narrow the idea, prose, and caption to the one path
   actually shown.

3. **Complete the `thinking-in-bets` registry record.** The draft entry at
   `content/registry.json:952` has display metadata and `status: "draft"` but omits
   the authoring spec's required `tier`, `thesis`, `framework`, and `diagrams`
   fields. Record tier 2 and the brief-supported thesis, identify Resulting as the
   signature framework, and inventory the seven rendered figures in page order:
   two-by-two matrix, spectrum, iceberg, process loop, node graph, flow, and the
   Model's flow/comparison composition.

4. **Recompute the Hero reading-time badge from the rendered page.** A direct static
   render of this exact draft contains approximately 1,413 reader-visible words,
   including the Hero, headings, captions, SVG labels, exercises, generated cover
   metadata, and nearby-book footer. At approximately 200 words per minute, rounded
   up as the authoring spec requires, the page is an eight-minute distillation, not
   `minutes={7}` at `src/chapters/thinking-in-bets.mdx:8`.

### Advisory

1. Within the repository's bounded evidence, the central factual and copyright
   posture is sound. The chapter brief and seed metadata support the distinction
   between decision quality and outcome quality and identify Resulting as the
   signature model. The draft develops those ideas in original thematic prose,
   uses no quotation or real cover art, and composes documented shared-vocabulary
   figures rather than a chapter-specific reproduction of a source figure. No
   separate chapter evidence dossier or source excerpts exist for closer
   attribution or close-paraphrase comparison, and this review began no external
   web search.

2. Apart from the required findings, the anatomy and teaching progression are
   strong. Six key ideas each have a captioned structural visual; the Model renders
   the brief's signature concept; the four exercises prescribe observable actions;
   the caveat keeps uncertainty distinct from irresponsibility; and the final
   takeaway is concise. The three related slugs resolve to done chapters, their
   relationships are stated in the preceding sentence, and the outbound link is a
   direct Penguin Random House page.

3. The direct imports and their rendering helpers are technically coherent. The
   chapter's minimum widths sit inside `Figure`'s horizontal scroller, preserving
   authored SVG label sizes on a phone. `npm run check` passed on 2026-07-16:
   repository validation, prose lint, both pipeline tests, all 100 Vitest tests,
   TypeScript, the Vite production build, and ESLint. Vitest emitted only the
   existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-16

- Reduced the Thesis to two sentences while retaining uncertainty, explicit belief,
  revision, and process-over-result.
- Rebuilt Figure 48.6 as two backward-looking flow paths: future failure leads to a
  weak assumption and a safeguard today; future success leads to a required condition
  and a positive early sign today.
- Completed the registry entry with tier 2, the brief-supported thesis, Resulting as
  the framework, and the ordered inventory of all seven rendered figures.
- Corrected the Hero badge to an eight-minute distillation.
- Ran `npm run check` successfully; validation, prose lint, pipeline tests, 100
  Vitest tests, TypeScript, Vite build, and ESLint passed. The existing jsdom
  `Window.scrollTo()` notices remained non-failing.

## Critique round 2 — 2026-07-16

### Required

None.

### Advisory

1. All four round-one findings are resolved. The Thesis is now two sentences;
   Figure 48.6 visibly teaches both backward-looking paths described by its prose
   and caption; the registry records tier, thesis, Resulting, and all seven figures;
   and the Hero shows the recomputed eight-minute badge.

2. The bounded factual and copyright review remains sound. The brief and seed
   metadata support the process-over-outcome thesis and identify Resulting as the
   signature model. The surrounding material develops compatible decision-journal,
   calibrated-belief, dissent, and premortem practices in original thematic prose,
   with no quotation, close-paraphrase evidence, real cover art, or reproduction of
   a source figure found in the repository. No chapter-specific evidence dossier is
   recorded, and this review began no external web search.

3. The six key ideas, seven captioned figures, signature Model, four concrete
   exercises, caveat, takeaway, and nearby links satisfy the page anatomy. The
   imported Hero, ShelvedNearby, Matrix, Spectrum, Iceberg, ProcessLoop, NodeGraph,
   Flow, and Compare components render coherently; minimum-width compositions sit
   inside Figure's horizontal scroller for phone layouts. `npm run check` passed on
   2026-07-16, including validation, prose lint, pipeline tests, all 100 Vitest
   tests, TypeScript, the Vite production build, and ESLint. The jsdom
   `Window.scrollTo()` notices were non-failing.
