verdict: approve

## Critique round 1 — 2026-07-17

### REQUIRED

1. **Compress The thesis to the required one or two sentences.** The fixed anatomy
   defines this block as the one- or two-sentence argument a reader can carry away,
   but the current paragraph contains six sentences
   (`src/chapters/common-sense-investing.mdx:11-19`). It reaches the right broad
   conclusion, yet it expands into cost arithmetic, active trading, allocation, and
   holding behavior instead of delivering the contract's compact thesis. Preserve
   the structural before-cost/after-cost point and the broad, low-cost ownership
   conclusion in no more than two sentences. Recompute the Hero badge after the edit;
   the current direct render contains 1,768 visible alphanumeric word tokens (1,777
   by whitespace count), which correctly rounds to nine minutes at approximately 200
   words per minute.

2. **Keep Figure 62.4's final value label inside the SVG viewport.** `Bars` uses a
   380-unit viewBox, a 136-unit track origin, and a 204-unit track, then places an
   unwrapped, start-anchored value label six units after the bar
   (`src/components/diagrams/Bars.tsx:23-25,31-34,38-39,52-55`). At `value: 0.86`,
   `more frictions to clear` begins at about x=317 and extends well beyond x=380
   (`src/chapters/common-sense-investing.mdx:129-138`). The chapter's 440px minimum
   rendered width preserves type size but cannot reveal content clipped outside the
   SVG's own viewBox. Shorten or recompose the chapter-local label so the complete
   turnover comparison remains visible without changing the shared component.

The remaining required audit is sound within the recorded evidence. The brief and
registry support the low-cost broad-indexing thesis and the index-investing signature
model. The page has five key ideas, each with a captioned diagram from the shared
vocabulary, followed by a distinct Model figure, four concrete practice cards, an
honest caveat, a generated typographic cover, three related slugs that resolve to done
chapters, and a direct bookseller URL. The SEC Investor Bulletin already linked in the
draft supports its statements about index-fund variety, costs, market and tracking
risk, possible benchmark underperformance, and reading the prospectus and shareholder
reports. That recorded URL was inspected directly; this review began no new external
search.

`npm run check` passed on 2026-07-17: queue and registry validation, prose lint, 2
pipeline tests, 37 runner tests, 128 application tests, typecheck, production build,
and ESLint all passed. Vitest emitted only the existing non-failing jsdom
`Window.scrollTo()` notices.

### ADVISORY

1. `ShelvedNearby` renders three relevant, completed books, but it gives no one-clause
   explanation of each relationship (`src/chapters/common-sense-investing.mdx:228-232`).
   Adding a short chapter-local relationship note would satisfy the authoring spec's
   cross-link guidance more fully, but optional cross-link enrichment is advisory
   under the critique rubric.

## Builder resolution — 2026-07-17

- Condensed **The thesis** to two sentences that retain the before-cost/after-cost
  arithmetic and the case for broad, low-cost ownership. The final direct-render count
  is 1,700 visible alphanumeric word tokens, which remains a 9-minute distillation at
  approximately 200 words per minute, so the Hero badge remains `9-min distillation`.
- Replaced Figure 62.4's final `Bars` value label with `more costs`. At the existing
  0.86 bar endpoint, the unwrapped label now fits inside the 380-unit SVG viewport;
  the shared `Bars` primitive remains unchanged.

## Critique round 2 — 2026-07-17

### REQUIRED

None.

The two round 1 findings are resolved. **The thesis** is now two sentences and
preserves the book's central before-cost/after-cost arithmetic and broad,
low-cost-ownership conclusion (`src/chapters/common-sense-investing.mdx:11-15`).
Figure 62.4's final label is now `more costs`; with the shared `Bars` geometry it
begins at approximately x=317 and remains inside the 380-unit viewBox
(`src/chapters/common-sense-investing.mdx:125-134`,
`src/components/diagrams/Bars.tsx:23-25,31-34,38-39,52-55`).

The full required audit remains sound. The brief and registry support the thesis
and index-investing signature model. The page contains five key ideas with five
captioned, in-vocabulary diagrams, a separate Model figure, concrete practice
cards, an honest caveat, a generated cover, three related completed chapters, and
a real bookseller link. The financial claims remain consistent with the chapter
brief and the SEC evidence recorded in round 1; this pass began no external web
search. The registry's `draft` status and the queue's `PENDING` row are the
repository's validated representation of a draft, and `scripts/decide.py status`
selects this slug for critique.

`npm run check` passed on 2026-07-17: queue and registry validation, prose lint, 2
pipeline tests, 37 runner tests, 128 application tests, typecheck, production
build, and ESLint all passed. Vitest emitted only its existing non-failing jsdom
`Window.scrollTo()` notices.

### ADVISORY

No new advisory findings. The optional cross-link relationship note from round 1
remains an advisory refinement and does not block approval.
