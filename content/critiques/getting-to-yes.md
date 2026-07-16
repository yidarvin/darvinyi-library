verdict: approve

## Critique round 1 — 2026-07-15

### Required

1. **Make Figure 29.3 show trades across different interests, not only an overlap of
   interests.** The section explains that one side may value speed while the other
   values certainty, or that one may value present cash while the other can offer a
   longer commitment. Those differences create the exchange material. The figure
   instead passes `your interests` and `their interests` as the two sets of a `Venn`
   and places `options worth testing` in their intersection
   (`src/chapters/getting-to-yes.mdx:71-86`). In the documented vocabulary, a Venn
   says that the overlap itself is the point, so the visible structure narrows this
   major idea to shared interests and contradicts the prose's account of gains from
   differences. Recompose the chapter-local figure with an in-vocabulary form that
   visibly encodes differently valued terms being traded, or revise its claim only if
   the recorded concept genuinely supports an overlap model.

2. **Separate Figure 29.5's colliding pole and marker labels.** The shared `Spectrum`
   renders the left and right pole labels on the same baseline at y=74 and the marker
   caption at y=78. Here, `worse than the alternative` extends rightward from x=40,
   `better than the alternative` extends leftward from x=340, and `BATNA threshold`
   is centered at x=190 (`src/chapters/getting-to-yes.mdx:128-140`). All three occupy
   the middle of the SVG, so they overlap at every rendered scale. The chapter's
   minimum width and `Figure`'s horizontal-overflow wrapper preserve that intrinsic
   collision rather than repairing it. Shorten, move, or remove chapter-local labels,
   or use another in-vocabulary composition, so each concept remains independently
   legible on a phone without changing the shared component.

3. **Complete the `getting-to-yes` registry record required by the content contract.**
   The current draft entry contains display metadata and `draft` status but omits
   `tier`, `thesis`, `framework`, and the rendered diagram inventory
   (`content/registry.json:578-585`). Add the brief-supported tier 1, thesis, and
   principled-negotiation/BATNA framework, then record all six figure forms in page
   order after Figures 29.3 and 29.5 are corrected. The validator permits this
   scaffold record while it is a draft, but definition-of-done item 7 does not.

### Advisory

1. Within the repository's bounded evidence, the central claims and copyright posture
   are otherwise sound. The chapter brief and `_books.py` independently record the
   people/problem, interests/positions thesis and the principled negotiation/BATNA
   signature model. The draft develops those ideas in original thematic prose, uses
   no source quotation or material empirical claim beyond that evidence, uses a
   generated typographic cover, and composes documented shared diagram primitives
   rather than reproducing a book figure. No separate chapter-specific evidence
   dossier was found, and this review began no external web search.

2. Apart from the two required figure findings, the page's anatomy is strong. Five
   key ideas have captioned structural diagrams, the Model figure presents the full
   decision sequence and BATNA branch, four practice cards specify observable
   preparation and decision actions, and the caveat directly addresses unequal power,
   bad faith, coercion, selective standards, legal rights, and safety. The eight-minute
   badge is consistent with the reader-facing material at approximately 200 words per
   minute rounded up.

3. All three nearby slugs resolve to done chapters, the prose states the relationship
   of each title to this one, and the outbound link is a direct publisher page. The
   Compare, Iceberg, NodeGraph, and Flow figures match their prose and imported
   components; their chapter-local minimum widths are preserved by `Figure`'s
   horizontal-overflow wrapper on a phone.

4. `npm run check` completed with `CHECK OK` on 2026-07-15: queue, registry,
   critique, and content validation; prose lint; both pipeline tests; all 62 Vitest
   tests; TypeScript and Vite production build; and ESLint passed. Vitest emitted only
   the existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-15

1. Replaced Figure 29.3's Venn with an in-vocabulary comparison. The two panels now
   show an explicit asymmetric exchange: one side values speed and can offer a longer
   commitment, while the other values certainty and can offer a faster decision. The
   revised caption identifies the trade rather than an overlap of interests.

2. Kept the shared `Spectrum` unchanged and made Figure 29.5's chapter-local labels
   independently legible: its poles are now `walk away` and `accept`, and its centered
   marker is `BATNA`. The zone labels still explain the comparison, without competing
   with the pole and marker labels above the axis.

3. Completed the draft registry record with the brief-supported tier, thesis,
   principled-negotiation/BATNA framework, and six rendered diagram forms in page
   order: comparison, iceberg, comparison, node graph, spectrum, and flow.

## Critique round 2 — 2026-07-15

### Required

None.

### Advisory

1. All three round 1 requirements are resolved in the current draft. Figure 29.3 now
   uses a parallel comparison to encode an asymmetric exchange across differently
   valued terms. Figure 29.5 gives `walk away`, `accept`, and `BATNA` separate label
   positions while its zones preserve the decision rule. The registry now records the
   brief-supported tier, thesis, framework, and all six figure forms in page order.

2. The bounded factual record remains consistent with the page. The chapter brief and
   `_books.py` support the people/problem and interests/positions thesis plus the
   principled-negotiation/BATNA signature model. No chapter-specific evidence dossier
   exists in the repository, and this review began no external web search. The draft
   makes no source quotation or material empirical claim requiring further support.

3. The full page and imported renderers meet the content contract. Five key ideas each
   have a captioned, in-vocabulary structural figure; the Model composes the method and
   BATNA decision branch; the practice cards specify concrete preparation and choice
   actions; and the caveat covers power, bad faith, coercion, selective criteria,
   rights, and safety. The related slugs resolve to done chapters, and the outbound
   link points to the publisher.

4. `npm run check` completed with `CHECK OK` on 2026-07-15. Validation, prose lint,
   both pipeline tests, all 62 Vitest tests, TypeScript and Vite production build, and
   ESLint passed. Vitest emitted only the existing non-failing jsdom
   `Window.scrollTo()` notices.
