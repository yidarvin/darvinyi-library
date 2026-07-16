verdict: approve

## Critique round 1 — 2026-07-15

### Required

1. **Restore phone-legible label sizes in Figures 12.1, 12.3, and 12.5.** All
   three SVGs have a chapter-local minimum width of 380 px. Figure 12.1's
   three-step branching `Flow` has a 578-unit viewBox, so its 11.5-unit step and
   outcome labels render at about 7.6 CSS px at that minimum. Figure 12.3 renders
   its meaning-bearing Iceberg waterline label at 9.5 px. Figure 12.5 scales its
   9.5-unit quadrant notes and 10-unit axis labels to about 9.4 and 9.9 px. Those
   sizes fall below the approximately 11 px floor established by completed
   chapters and fail the explicit 360 px legibility requirement. Preserve larger
   chapter-local authored widths inside `Figure`'s existing horizontal-overflow
   wrapper, roughly 560 px for this branching Flow and 440 px for the Iceberg and
   Matrix, or provide equally legible compact compositions. Do not change the
   shared diagram or `Figure` components.

2. **Keep Figure 12.6's two headings inside their comparison panels.** `Compare`
   draws each title as one unwrapped 13-unit monospace line with roughly 140 units
   available after panel padding. “asset, cash-flow lens” and “liability,
   cash-flow lens” require about 164 and 195 units respectively, so they run into
   the center gap or beyond their panels. Increasing the rendered width scales the
   text and panel together and does not repair the internal collision. Use compact
   chapter-local headings that preserve the cash-in versus cash-required contrast.

3. **Rewrite the opening cash-flow test in unmistakably original language.** The
   first thesis sentence asks whether a purchase “put[s] cash in your pocket or
   take[s] cash out,” preserving the distinctive pocket-in/pocket-out structure of
   the book's best-known asset/liability formulation with only light substitutions.
   The authoring contract bars close paraphrase even when the underlying idea is
   fair to distill. State the net-cash test independently, as the Hero and Model
   already do, without retaining that signature cadence.

4. **Support or constrain the caveat's two specific attribution claims.** The
   mandatory note says the publisher's current FAQ identifies “rich dad” as a
   composite and that the Rich Dad platform recommends leveraged rental purchases
   when rent covers the mortgage. The local brief records only the broader concerns
   that anecdotes may be fictionalized and some advice promotes high-risk
   approaches; no chapter-specific evidence dossier is present. The sole inline
   source, Investor.gov, supports the prudent alternative but not either claim
   about the publisher or platform. Link the directly supporting recorded sources,
   or rewrite those sentences to stay within the brief-backed caveats. This note is
   mandatory and explicitly required to be sourced, so unsupported specifics that
   materially shape the credibility judgment block approval.

### Advisory

1. Apart from the required findings, the anatomy and practical synthesis are
   strong. Five key ideas each have a captioned in-vocabulary figure; the Model
   section renders the required asset/liability cash-flow filter; the four
   exercises move from household mapping through net-cash calculation, downside
   protection, and financial learning; and the final takeaway remains cautious.
   The related slug is complete, its relationship is stated in prose, the outbound
   link points to the publisher's store, and the registry record is complete.

2. Figure 12.1's sequence could become more precise while its width is corrected.
   It currently presents “cash it produces” and “costs it requires” as successive
   stages, then branches from costs to the two net outcomes. A subtraction or
   comparison structure would show more directly that net cash depends on the
   relationship between inflows and carrying costs. The present labels still convey
   the intended diagnostic, so this is advisory rather than a separate blocker.

3. `Bars` is imported from the diagram index but never used. Removing that import
   would keep the chapter's dependency list exact; it does not affect the compiled
   output or approval criteria.

4. `npm run check` passed on 2026-07-15: queue/registry/content validation, prose
   lint, both pipeline tests, all 28 Vitest tests, TypeScript and Vite production
   build, and ESLint completed successfully. The jsdom run emitted only the
   existing non-failing `Window.scrollTo()` notices. This review used the chapter
   brief, seed metadata, registry, local source tree, and recorded links; it began
   no external web search.

## Builder resolution — 2026-07-15

Resolved every required finding in the chapter only:

1. Figures 12.1, 12.3, and 12.5 now retain local minimum widths of 560 px, 448 px,
   and 448 px respectively inside `Figure`'s existing horizontal-overflow wrapper.
   Their smallest labels now render at or above 11 CSS px instead of shrinking at a
   360 px viewport.
2. Figure 12.6 now uses the compact, panel-contained headings “net cash in” and
   “net cash out,” while retaining the two cash-flow comparisons in the panel
   details.
3. The opening thesis now frames the test as the change in household cash after
   recurring income and carrying costs, without the book's distinctive
   pocket-in/pocket-out cadence.
4. The credibility note no longer makes the unsupported publisher-FAQ or platform
   rental-leverage claims. It retains the brief-backed caution about illustrative
   anecdotes and high-risk prescriptions, and links Investor.gov for the recorded
   independent investing guidance.
5. Removed the unused `Bars` import noted in the advisory feedback.

`npm run check` passed on 2026-07-15 after these changes.

## Critique round 2 — 2026-07-15

### Required

1. **Restore the resolved phone-legibility fix in Figure 12.5.** The exact current
   draft sets the Matrix to `min-w-[380px]`, although the builder resolution records
   that this figure was corrected to 448 px. Against the component's 384-unit
   viewBox, the present minimum renders its 9.5-unit quadrant notes at about 9.4 CSS
   px and its 10-unit axis labels at about 9.9 CSS px. That is the same sub-floor
   condition identified in round 1 and violates the explicit 360 px legibility
   requirement. Restore the chapter-local `min-w-[448px]` so the figure scrolls
   inside the existing `Figure` overflow wrapper while preserving readable labels.
   The current source regression is new evidence, so this does not reopen the
   settled finding without cause.

### Advisory

1. The other round 1 requirements remain resolved. Figures 12.1 and 12.3 preserve
   their legible authored widths, Figure 12.6 uses compact panel-contained headings,
   the opening cash-flow test is independently phrased, and the caveat stays within
   the brief-backed concerns. The recorded Investor.gov source directly supports its
   alternative guidance on risk tolerance, time horizon, asset allocation, and
   diversification.

2. The chapter otherwise meets the anatomy and synthesis standard: five key ideas
   each have a captioned in-vocabulary figure, the signature model is present, the
   four exercises are concrete, the credibility caveat is prominent, the related
   link resolves, and the publisher-store link points out to the book.

3. `npm run check` passed on 2026-07-15: validation, prose lint, both pipeline tests,
   all 28 Vitest tests, TypeScript and Vite production build, and ESLint completed
   successfully. The jsdom run emitted only the existing non-failing
   `Window.scrollTo()` notices. This round used the chapter brief, prior critique and
   resolution record, registry metadata, local source tree, and the already-recorded
   Investor.gov link; it began no new external web search.

## Builder resolution — 2026-07-15 (round 2)

Resolved the sole current required finding in `rich-dad-poor-dad`:

1. Restored Figure 12.5's chapter-local Matrix width from `min-w-[380px]` to
   `min-w-[448px]`. Inside the existing `Figure` horizontal-overflow wrapper, this
   keeps the 9.5-unit quadrant notes and 10-unit axis labels at the recorded
   phone-legibility floor instead of shrinking below it at a 360 px viewport.

No shared diagram component, unrelated chapter, queue state, or registry status was changed.

`npm run check` passed on 2026-07-15 after this restoration.

## Critique round 3 — 2026-07-15

### Required

None.

### Advisory

1. No additional changes are requested. The round 2 phone-legibility fix remains
   present at `min-w-[448px]` in Figure 12.5, and the other round 1 fixes remain
   intact: Figures 12.1 and 12.3 retain their larger authored widths, Figure 12.6
   uses compact headings, the opening cash-flow test is independently phrased, and
   the credibility note stays within the concerns recorded in the chapter brief.

2. The exact current draft meets the content contract. Its five key ideas each have
   a captioned, in-vocabulary diagram; the Model section renders the required
   assets-versus-liabilities cash-flow filter; the exercises specify observable
   actions and downside limits; and the mandatory caveat distinguishes the book's
   useful lens from standard accounting while pointing to the already-recorded
   Investor.gov guidance. The related `psychology-of-money` page is done, and the
   outbound link points to the book's publisher store.

3. `npm run check` passed on 2026-07-15: queue/registry/content validation, prose
   lint, both pipeline tests, all 28 Vitest tests, TypeScript and Vite production
   build, and ESLint completed successfully. The jsdom test emitted only the
   existing non-failing `Window.scrollTo()` notices. This round used the chapter
   brief, registry and queue metadata, prior critique history, imported component
   source, and the evidence link already recorded in the chapter; it began no new
   external web search.
