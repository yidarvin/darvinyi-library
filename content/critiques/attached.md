verdict: resolved

## Critique round 1 — 2026-07-27

### Required

1. The signature matrix assigns every attachment pattern to the wrong combination of its stated axes. `Matrix` consumes quadrants in `[top-left, top-right, bottom-left, bottom-right]` order, while this figure defines anxiety as high at the top and avoidance as high at the right. The resulting positions should therefore be anxious at top-left, mixed/fearful at top-right, secure at bottom-left, and avoidant at bottom-right. Lines 147–150 instead place secure, anxious, avoidant, and mixed alarm in those positions, respectively, and line 152 highlights the erroneous secure cell. This reverses the chapter's central framework and changes the reader's understanding. Reorder the labels and highlight the actual secure quadrant. Also rename or reverse the horizontal dimension label: a left-to-right increase in avoidance is not a left-to-right increase in “comfort with closeness and dependence.”

2. The `attached` registry record is incomplete against the authoring spec's definition of done. It contains only the basic route metadata and `status`, but omits the brief's tier, the chapter thesis, the signature framework, and the diagram-form list. Populate those fields so the database describes the finished page rather than relying on the MDX and brief as separate sources of truth.

### Advisory

1. The prose before `ShelvedNearby` explains the relationship to `nonviolent-communication` and `seven-principles-marriage`, but the component also links `supercommunicators` without the relationship clause required by the cross-linking guidance. Add a short clause explaining that edge or omit the third link.

2. `npm run check` passes. The repeated jsdom `Window.scrollTo()` notices during Vitest are non-failing environment output, not a defect in this chapter.

## Builder resolution — 2026-07-27

- Reordered the attachment matrix into its documented `[top-left, top-right, bottom-left, bottom-right]` order: anxious, mixed alarm, secure, and avoidant. The secure cell is now highlighted, and the horizontal dimension now reads “avoidance of closeness and dependence,” which matches its low-to-high pole labels.
- Completed the `attached` registry record with tier 3, the brief thesis, the Attachment styles framework, and the six rendered diagram forms; its lifecycle status remains `draft`.
- Added the missing relationship clause for the existing `supercommunicators` shelf link.
