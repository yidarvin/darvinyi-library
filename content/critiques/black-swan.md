verdict: approve

## Critique round 1 — 2026-07-15

### Required

1. **The risk matrix assigns all four responses to the wrong coordinates.** The `Matrix` contract consumes quadrants as top-left, top-right, bottom-left, bottom-right. With the chapter's axes, those cells mean visible/severe, outside-the-model/severe, visible/limited, and outside-the-model/limited. The draft instead places `routine check`, `preserve optionality`, `repair the exposure`, and `build resilience` in that order and highlights the last cell. This contradicts both the caption and the prose: repair belongs with visible/severe risk, resilience belongs with outside-the-model/severe risk, routine monitoring belongs with visible/limited risk, and optionality belongs with outside-the-model/limited risk. Reorder the entries and move the highlight so the figure teaches the stated distinction.

2. **Figure 18.1 clips the label on its decisive bar.** `Bars` places a value label at `trackX + w + 6` inside a 380-unit viewBox. For the `0.96` bar, `can dominate` begins at about x=346, leaving only about 34 units for text that needs substantially more width. The SVG viewport therefore cuts off the phrase, including at the chapter's 380px mobile minimum. Shorten or reposition the value label so the complete claim is legible.

3. **The Hero reading-time badge is not computed from the final rendered page.** A render of this chapter contains 1,380 visible words. At the specified approximately 200 words per minute, rounded up, the badge must read 7 minutes, not `minutes={6}`.

4. **The `black-swan` registry record is incomplete for a finished book.** It currently stops at `status: "draft"` and omits the authoring spec's required `tier`, `thesis`, `framework`, and `diagrams` fields. Populate those fields from the recorded book seed, brief, and the six forms actually used by the chapter before approval.

### Advisory

- In the signature Flow, the upper branch leaves `retrospective explanation` and then says `reduce ruin before it arrives`. The advice is sound, but its placement after the event reverses its timing. Removing the branch or reframing the visual so advance exposure control sits outside the event sequence would make the central model cleaner.

## Builder resolution — 2026-07-15

- Reordered Figure 18.5 to the Matrix contract's top-left, top-right, bottom-left, bottom-right sequence: repair the exposure, build resilience, routine check, preserve optionality. The severe, outside-the-model cell is now highlighted.
- Shortened Figure 18.1's decisive-bar label to `sets result` and reduced its conceptual bar to 0.75, leaving the complete label inside the 380-unit viewport while preserving the comparison with the two ordinary magnitudes.
- Updated the Hero badge from 6 to 7 minutes, matching the recorded final-rendered word-count calculation.
- Completed the draft registry record with tier, seed thesis, framework, and the six diagram forms rendered by the chapter.

## Critique round 2 — 2026-07-15

### Required

None.

### Advisory

1. The current draft resolves every required finding from round 1. Figure 18.5 now
   assigns all four responses to the coordinates defined by its axes and highlights
   the severe, outside-the-model case. Figure 18.1's decisive value label fits its
   SVG viewport. The seven-minute Hero badge matches the recorded rendered-word
   calculation, and the registry now contains the brief-supported tier, thesis,
   framework, and diagram inventory.

2. Within the bounded local record, the chapter accurately carries through the
   brief's core claim and three-part signature model. Its treatment of concentrated
   outcomes, retrospective explanation, and silent evidence is framed conceptually
   rather than as unrecorded study-level proof. The known-risk distinction and the
   forecasting caveat also prevent the term from swallowing ordinary negligence or
   every useful forecast. No new external web search was begun for this review.

3. The upper branch in Figure 18.6 still places `reduce ruin before it arrives`
   after the retrospective-explanation step. The advice is sound, but moving advance
   exposure control outside the event sequence would make its timing clearer. This
   remains the round 1 advisory and does not make the central three-part model
   misleading.

4. The three nearby slugs resolve to built chapters, but the footer still presents
   covers without the one-clause relationship notes requested by the cross-linking
   guidance. Adding those relationships later would improve the graph without
   blocking this chapter.

5. `npm run check` passed on 2026-07-15: queue, registry, critique, and content
   validation; prose lint; both pipeline tests; all 40 Vitest tests; TypeScript and
   Vite production build; and ESLint. Vitest emitted only the existing non-failing
   jsdom `Window.scrollTo()` notices.
