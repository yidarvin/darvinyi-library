verdict: approve

## Critique round 1 — 2026-07-15

### Required

1. **Separate Figure 14.4's marker caption from its right pole label.** The shared
   `Spectrum` places the pole labels at y=74 and the centered marker caption at
   y=78. With `marker={0.78}`, `useful no` sits at x=274 and overlaps the right-aligned
   `clear boundary` label ending at x=340. The chapter's 440 px minimum rendered
   width preserves the authored SVG geometry, so horizontal scrolling or scaling
   cannot remove the collision. Revise the chapter-local labels or composition so
   the marker and both poles remain independently readable without changing the
   shared `Spectrum` component.

2. **Complete the `never-split-the-difference` registry record required by the
   content contract.** The record has the display title, author/year subtitle,
   shelf, routes, and draft status, but it omits `tier`, `thesis`, `framework`, and
   the diagram-form inventory required by definition-of-done item 7. Add the
   brief-supported tier 1, thesis, mirroring-labeling-calibrated-questions framework,
   and the six diagram forms without changing unrelated registry entries or shared
   tooling.

### Advisory

1. Within the repository's bounded evidence, the factual and copyright posture is
   sound. The chapter brief and seed metadata support tactical empathy as the thesis
   and mirroring, labeling, and calibrated questions as the signature model. The
   draft uses an original thematic structure and original prose, includes no quote
   or real cover art, and composes shared vocabulary forms rather than tracing a
   source figure. Its explanations of positions, mirrors, tentative labels,
   no-oriented questions, and what/how questions are cautious and coherent with the
   recorded framework. The repository contains no chapter-specific source excerpts
   or separate evidence dossier for closer attribution or close-paraphrase
   comparison. This review began no external web search.

2. Apart from the required Spectrum and registry findings, the anatomy and practice
   design are sound. Five key ideas each have a captioned structural figure; the
   Model renders the required three-part framework; the four exercises specify
   preparation, mirroring, design questions, and implementation checks; the caveat
   rejects coercive or mechanical use; and the final takeaway is concise. The
   publisher link is direct, and all three related slugs are done.

3. The footer shows three related covers but does not state the one-clause
   relationship requested by the cross-linking guidance. A short chapter-local note
   could identify *How to Win Friends and Influence People* as the listening and
   rapport counterpart, *Thinking, Fast and Slow* as the judgment counterpart, and
   *Influence* as the persuasion counterpart. This remains advisory because the
   critique rubric treats optional cross-link improvement as non-blocking.

4. The `minutes={8}` badge is consistent with the 1,447-word MDX source at roughly
   200 words per minute, rounded up. `npm run check` passed on 2026-07-15:
   queue/registry/content validation, prose lint, both pipeline tests, all 32 Vitest
   tests, TypeScript and Vite production build, and ESLint completed successfully.
   The jsdom run emitted only the existing non-failing `Window.scrollTo()` notices.

## Builder resolution — 2026-07-15

- Moved Figure 14.4's chapter-local `useful no` marker from `0.78` to `0.48`.
  At the shared Spectrum's fixed geometry, the marker caption now ends before the
  `clear boundary` pole label begins, so both poles and the marker remain readable
  without changing the shared component.
- Completed the `never-split-the-difference` registry record with tier 1, the
  brief-supported tactical-empathy thesis, the mirroring-labeling-calibrated-questions
  framework, and its six-diagram inventory.
- Ran `npm run check` successfully: validation, prose lint, pipeline tests, 32 Vitest
  tests, TypeScript/Vite build, and ESLint passed. The chapter remains `draft`.

## Critique round 2 — 2026-07-15

### Required

None.

### Advisory

1. Both prior required findings are resolved. Figure 14.4 now places `useful no` at
   `marker={0.48}`; under the shared Spectrum geometry, its centered label remains
   separate from both pole labels. The registry now records tier 1, the brief-backed
   thesis and signature framework, and all six diagram forms.

2. The bounded factual and copyright assessment remains sound. The chapter brief and
   seed record support tactical empathy as the thesis and mirroring, labeling, and
   calibrated questions as the signature model. The draft explains those concepts in
   original prose and an original thematic order, uses only shared vocabulary diagrams,
   contains no quotation or real cover art, and avoids stronger empirical claims than
   the local evidence can establish. No chapter-specific source excerpts or separate
   evidence dossier exist for closer attribution testing, and this review began no new
   external web search.

3. The page retains the required anatomy and a usable teaching progression: five key
   ideas have captioned structural diagrams, the Model renders the signature sequence,
   four exercises specify observable actions, the caveat guards against manipulative or
   mechanical use, the related slugs resolve to done books, and the publisher link is
   direct. The earlier optional suggestion to state the relationship of each nearby book
   remains advisory and does not justify stylistic churn.

4. `npm run check` passed on 2026-07-15: queue/registry/content validation, prose lint,
   both pipeline tests, all 32 Vitest tests, TypeScript and Vite production build, and
   ESLint completed successfully. The jsdom run emitted only its existing non-failing
   `Window.scrollTo()` notices.
