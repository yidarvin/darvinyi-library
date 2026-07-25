verdict: resolved

## Critique round 1 — 2026-07-25

### Required

1. **Recompute the Hero reading-time badge from the rendered page.** The draft
   declares `minutes={9}` (`src/chapters/twelve-rules.mdx:5-9`), but a direct
   render contains approximately 1,492 visible words, including the Hero, headings,
   captions, diagram labels, exercise titles, and nearby-book footer. At the
   authoring spec's approximately 200 words per minute, rounded up, this is an
   eight-minute distillation. Set the badge from the final rendered count after the
   other revisions.

2. **Figure 79.2 does not show the self-comparison the key idea promises and instead
   invents a progress trajectory.** The prose asks the reader to compare a current
   practice, responsibility, or relationship with its own recent state, but the
   figure renders a smooth sigmoid from a low starting point to a near-perfect
   endpoint (`src/chapters/twelve-rules.mdx:53-74`). Nothing in the brief or
   surrounding explanation supports monotonic improvement, an S-shaped development
   path, or a plateau. More importantly, the visual contains no paired prior/current
   reference from which the reader can inspect a local change. Replace it with an
   in-vocabulary composition that makes the repeated local comparison structural
   without fabricating a growth curve.

3. **Figure 79.3's labels and causal semantics do not match its prose or caption.**
   The caption says expectations, consequences, and repair are connected, while the
   graph contains `care`, `clear limit`, `consistent follow-through`, and
   `predictable trust`; it never depicts repair
   (`src/chapters/twelve-rules.mdx:76-102`). The graph also closes an unexplained
   `trust → care` feedback edge and marks that edge and
   `consistent follow-through → predictable trust` as reinforcing, so the shared
   component visibly assigns positive causal polarity that the explanation does not
   establish. Align the prose, caption, nodes, and edges around one supported
   structure. If the intended claim is a sequence from care through clear limits and
   follow-through to predictability, show that sequence without unsupported feedback
   polarity; if a loop is intended, explain and support every return edge.

### Advisory

1. The brief, seed metadata, and registry record are the only chapter-specific
   evidence available in the repository; there is no separate source excerpt or
   evidence dossier, and this review began no external web search. The central
   responsibility and order/chaos framing agrees with those bounded materials, and no
   quotation, real cover art, or apparent reproduction of a source figure was found.
   A future evidence pass could record the basis for the caveat's broader
   characterization of the book's movement among clinical observation, myth,
   evolutionary claims, and moral prescription.

`npm run check` passed on 2026-07-25: queue and registry validation, prose lint,
2 pipeline tests, 38 runner tests, 163 Vitest tests, TypeScript and production build,
and ESLint all completed successfully. Vitest emitted only the existing non-failing
jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-25

1. Recomputed the revised page from a static render: it has 1,500 visible word
   tokens, including the Hero, headings, captions, diagram labels, exercise titles,
   and nearby-book footer. At approximately 200 words per minute, rounded up, the
   Hero now correctly declares `minutes={8}`.
2. Replaced Figure 79.2's unsupported sigmoid with the existing comparison form.
   Its parallel `last week` and `this week` panels pair the same three domains,
   making each local self-comparison visible without implying a universal growth path.
3. Replaced Figure 79.3's feedback graph with a neutral four-step flow: care notices
   the need, a clear expectation is named, follow-through is proportionate, then
   repair restores predictability. The surrounding prose now states the same
   expectation, consequence, and repair sequence, and the diagram contains no
   unexplained feedback edge or reinforcing-polarity claim.

`npm run check` passed on 2026-07-25: queue and registry validation, prose lint,
2 pipeline tests, 38 runner tests, 163 Vitest tests, TypeScript and production build,
and ESLint all completed successfully. Vitest emitted only the existing non-failing
jsdom `Window.scrollTo()` notices.

## Critique round 2 — 2026-07-25

### Required

1. **Update the registry diagram inventory to match the resolved chapter.** The
   builder replaced Figure 79.2's annotated curve with `Compare` and Figure 79.3's
   node graph with `Flow` (`src/chapters/twelve-rules.mdx:63-95`), but the registry
   still lists `"annotated curve"` and `"node graph"` in those positions
   (`content/registry.json:1573-1580`). Record the actual page-order forms:
   comparison, comparison, flow, iceberg, concentric circles, spectrum, spectrum.
   The stale inventory violates the definition-of-done requirement that the registry
   entry be complete and the critique rubric's requirement that registry metadata
   agree with the rendered draft.

### Advisory

None.

The three round 1 findings are otherwise resolved. An independent static render of
this exact draft produced approximately 1,420 visible alphanumeric word tokens, which
still rounds up to the declared eight-minute badge at approximately 200 words per
minute. The brief, seed metadata, and registry remain the only chapter-specific
recorded evidence, so this review began no external web search and did not reopen the
settled evidence advisory.

`npm run check` passed on 2026-07-25: queue and registry validation, prose lint,
2 pipeline tests, 38 runner tests, 163 Vitest tests, TypeScript and production build,
and ESLint all completed successfully. Vitest emitted only the existing non-failing
jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-25

1. Updated the `twelve-rules` registry diagram inventory to match the rendered
   figures in page order: comparison, comparison, flow, iceberg, concentric circles,
   spectrum, spectrum. Figure 79.2 is now recorded as a comparison and Figure 79.3
   as a flow, preserving the prior substantive fixes.

`npm run check` passed on 2026-07-25.
