verdict: revise

## Critique round 1 — 2026-07-17

### Required

1. The Thesis section is four sentences long (`src/chapters/e-myth.mdx:16-21`), but the fixed anatomy requires this section to compress the entire argument into one or two sentences. Reduce it to one or two sentences while preserving both halves of the diagnosis: technical competence is not business-building competence, and durability comes from a teachable system that does not depend on the founder.

2. Figure 68.3 has a deterministic label collision. The chapter places `markerLabel="documented handoffs"` at `marker={0.76}` without changing `markerLabelPlacement` (`src/chapters/e-myth.mdx:92-101`). `Spectrum` therefore draws that label on the near-marker baseline at roughly `(268, 78)`, while the right pole label `system-supported` is drawn right-aligned at `(340, 74)`. With the component's mono font sizes, the two strings occupy the same horizontal and vertical area, so the structural labels overwrite each other. Move the marker label to the component's top placement or otherwise revise this chapter's labels/placement so both labels are legible.

3. The hero Model prose and caption describe an improvement loop, but Figure 68.6 renders the operational part as the vocabulary's non-cyclic `Flow`: `choose the customer promise → design roles and routines → train and run the work → review the experience`, with no return path from review to redesign (`src/chapters/e-myth.mdx:142-171`). The comparison below it distinguishes working in the business from working on it, but it does not supply that missing feedback edge. Make the hero visual encode the stated review-and-revision loop, or remove the loop claim and align the caption and explanation with the one-way sequence actually shown.

### Advisory

1. The Shelved Nearby prose explains the relationship to `good-to-great` and `lean-startup`, but `built-to-last` is also passed to `related` without the one-clause relationship called for by the cross-linking contract (`src/chapters/e-myth.mdx:218-224`). Either add its relationship or omit that third link.

2. `npm run check` passed on 2026-07-17: validation, prose lint, pipeline tests, 140 Vitest tests, typecheck, production build, and ESLint all completed successfully. The repeated jsdom `Window.scrollTo()` notices were non-failing test-environment messages.

## Builder resolution — 2026-07-17

- Condensed **The thesis** to two sentences while retaining the distinction between technical skill and business-building skill, plus the need for a teachable system independent of the founder.
- Set Figure 68.3's `markerLabelPlacement="top"`, separating `documented handoffs` from the right pole label.
- Replaced Figure 68.6's one-way `Flow` with a `ProcessLoop` whose final stage is `review and revise the system`; its returning edge now makes the stated improvement loop explicit. Updated the e-myth registry diagram record to `process loop and comparison`.
- Added the missing one-clause relationship for the existing `built-to-last` Shelved Nearby link.

## Critique round 2 — 2026-07-17

### Required

1. Figure 68.1 has a deterministic label collision (`src/chapters/e-myth.mdx:41-47`). `Iceberg` wraps `above="the craft the customer receives"` at 16 characters into three centered lines whose final baseline is approximately `y=96.4`, while it draws `// what the owner is trained to notice` right-aligned on the waterline at `y=97` (`src/components/diagrams/Iceberg.tsx:46-53`). The final tip line, `receives`, therefore overlaps the long waterline label on essentially the same baseline. Shorten or reposition this chapter's labels, or otherwise revise the figure usage so both structural labels are legible.

### Advisory

1. All three required fixes from round 1 remain satisfied: the Thesis is two sentences, Figure 68.3 uses the top marker-label placement, and Figure 68.6 now encodes the stated review-and-revision loop. The `built-to-last` relationship is also now stated in the Shelved Nearby prose.

2. `npm run check` passed on 2026-07-17: validation, prose lint, pipeline tests, 140 Vitest tests, typecheck, production build, and ESLint all completed successfully. The repeated jsdom `Window.scrollTo()` notices were non-failing test-environment messages.
