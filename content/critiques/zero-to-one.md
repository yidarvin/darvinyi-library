verdict: approve

## Critique round 1 — 2026-07-15

### Required

1. **Complete the `zero-to-one` registry metadata required by the content contract.** The registry entry has display metadata, an empty `routes` array, and `draft` status, but it omits `tier`, `thesis`, `framework`, and the rendered diagram list required by definition-of-done item 7. Add those fields for this chapter without changing unrelated entries or shared tooling.

2. **Recompute the Hero reading-time badge from rendered words.** The draft declares `minutes={9}`, but a rendered-text count is approximately 1,414 words, including headings, visible component text, captions, exercise titles, the Hero, diagram labels, and Shelved Nearby. At the authoring spec's roughly 200 words per minute, rounded up, that is 8 minutes. Set the badge from the final rendered count after the other revisions.

3. **State the book's monopoly argument precisely enough to preserve the brief's central claim.** The brief says that monopolies rather than competition fund real progress, while the chapter's competition section shifts the mechanism toward rival-watching and the caveat reduces “monopoly” to a provocative name for any differentiated position. Differentiation alone is weaker than the book's claim about escaping close substitutes, retaining profits, and using that economic room to sustain innovation. Explain that argument accurately, then keep the existing ethical and legal qualification so the page neither erases the thesis nor endorses every concentrated market.

4. **Replace Figure 23.1's continuum with a structure that matches the stated distinction.** The prose and caption describe copying and creating as different paths, but `Spectrum` is the vocabulary form for matters of degree. Placing “a 0 → 1 bet” at `0.84` implies an unexplained amount of newness and turns a categorical strategic distinction into a gradient. Use an in-vocabulary composition that shows two modes or the create-then-expand relationship without inventing a numeric position.

5. **Separate the chapter's testing extension from the book's “secret” concept, and make Figure 23.4 encode the test honestly.** “For Thiel ... the important word is testable” presents the chapter's experiment-oriented interpretation as the author's definition, but neither the brief nor any recorded chapter evidence substantiates that attribution. The figure then marks customer use → evidence as reinforcing (`+`) and evidence → observation as balancing (`−`), even though its accessible label and prose say evidence can strengthen or weaken the claim. Reframe testability explicitly as a practical way to act on an overlooked insight, unless recorded evidence supports the stronger attribution, and revise the chapter-local graph so it shows genuinely two-sided feedback without unexplained system-edge semantics.

### Advisory

1. Figure 23.5's three-way Venn makes the center look like a necessary intersection of all three protections, while the prose describes a cluster of advantages and separately mentions brand. After the required revisions, consider whether a non-intersection vocabulary form would better show several possible reinforcing sources of durability. This is advisory because the caption already limits the claim to a position being stronger when the three support one another.

### Evidence checked

- The chapter brief supports the new-versus-copying thesis, explicitly identifies monopoly rather than competition as the funding mechanism, and names 0 to 1 versus 1 to n as the signature model. No separate chapter research or evidence record exists in the repository, and this review did not begin an external search.
- Re-read the chapter's direct imports (`Hero`, `ShelvedNearby`, `Compare`, `Flow`, `NodeGraph`, `Spectrum`, `Timeline`, and `Venn`), their shared SVG helpers, and the MDX wrappers used by the page. All six figures use registered vocabulary primitives. Their minimum widths preserve label size through the Figure wrapper's horizontal overflow behavior on narrow screens.
- The related slugs `lean-startup`, `good-to-great`, and `start-with-why` resolve to built chapters, the surrounding prose explains all three relationships, and the outbound URL is a direct Penguin Random House book page.
- `npm run check` passed on 2026-07-15: queue/registry/content validation, prose lint, pipeline tests, 50 Vitest tests, TypeScript/Vite production build, and ESLint all completed successfully. The jsdom `Window.scrollTo()` messages were non-failing notices.

## Builder resolution — 2026-07-15

- Added the missing `tier`, brief-aligned `thesis`, `framework`, and six rendered diagram-form entries to the `zero-to-one` registry record. Its status remains `draft`.
- Recomputed the Hero badge from the final rendered content. It remains in the 1,400-word range, so the 200-words-per-minute rule rounds up to `minutes={8}`.
- Restored the book's economic monopoly claim: escaping close substitutes preserves profits that can fund continued invention. The caveat now distinguishes that claim from competition law and keeps the ethical and regulatory qualification.
- Replaced Figure 23.1's degree-based spectrum with an in-vocabulary comparison of the categorical `0 → 1` creation mode and `1 → many` expansion mode.
- Reframed testability as this page's practical extension of an overlooked insight, not the book's definition of a secret. Figure 23.4 now shows customer evidence branching visibly to support or revise a working claim, with both outcomes feeding back into the claim and no unexplained `+` or `−` edge semantics.
- Ran `npm run check` successfully: validation, prose lint, pipeline tests, 50 Vitest tests, production build, and ESLint all passed. The jsdom `Window.scrollTo()` notices were non-failing.

## Critique round 2 — 2026-07-15

### Required

None.

### Advisory

None.

### Evidence checked

- Re-checked every round 1 requirement against the resolved draft. The registry now records the brief-aligned thesis and framework plus all six rendered diagram forms, and the 8-minute Hero badge remains consistent with the recorded rendered-text estimate of roughly 1,400 words.
- The competition section now preserves the brief's central economic claim: escaping close substitutes lets a company retain profits that can support continued invention. The caveat separately limits the claim without erasing it.
- Figure 23.1 now uses the registered comparison form for the categorical creation-versus-expansion distinction. The secrets section explicitly identifies customer testing as this page's practical extension, and Figure 23.4 presents support and revision as two visible feedback outcomes without assigning unsupported system-edge semantics.
- Re-read the full chapter, its direct imports (`Hero`, `ShelvedNearby`, `Compare`, `Flow`, `NodeGraph`, `Timeline`, and `Venn`), their transitive cover and SVG helpers, the chapter brief, the authoring contract, the diagram vocabulary, and the prior critique/resolution. No separate chapter evidence record exists, so factual checking was limited to the brief, recorded critique evidence, and internal consistency as instructed; no external search was started.
- The six figures use registered vocabulary forms, match their prose and captions, and set minimum widths inside the horizontally scrollable `Figure` wrapper so labels do not collapse at phone width. Related slugs resolve to built chapters, and the outbound link remains a direct publisher page.
- `npm run check` passed on 2026-07-15: queue/registry/content validation, prose lint, pipeline tests, 50 Vitest tests, TypeScript/Vite production build, and ESLint all completed successfully. The jsdom `Window.scrollTo()` messages were non-failing notices.
