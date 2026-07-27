verdict: approve

## Critique round 1 — 2026-07-27

### Required

1. Figure 100.2 renders two labels on top of each other. The chapter places the
   `Spectrum` marker at `0.8` with the label “pause and inspect,” immediately beside
   the right pole “high personal stakes.” In the shared component, the right pole is
   drawn at `y=74` and the default near-marker label at `y=78`, so these two long
   strings overlap instead of remaining legible. The component already supports a
   top marker-label placement; use that or otherwise revise the figure composition
   so every label reads clearly at the chapter's mobile minimum width.

2. The Hero's `minutes={6}` badge does not match the authoring spec's required
   calculation. Rendering this MDX through its actual components produces 1,267
   visible words; at approximately 200 words per minute, rounded up, the badge is
   seven minutes. Recompute the badge from the final rendered page and set it to the
   rounded-up value.

### Advisory

1. The sentence before `ShelvedNearby` gives three broad relationships for four
   linked books without mapping a relationship to each title. Per-title clauses
   would make these graph edges more informative, although the current links are
   built, relevant, and not misleading.

2. `npm run check` passes in full. The supplied brief and recorded primary-source
   evidence support the chapter's account of Resistance and turning pro, and I found
   no additional approval-blocking defect in copyright, sourcing, section anatomy,
   the other five figures, the practice cards, the caveat, imports, registry data,
   route, outbound link, or related-book statuses.

## Builder resolution — 2026-07-27

- Set Figure 100.2's `markerLabelPlacement="top"`. The marker label `pause and
  inspect` now occupies the separate upper baseline, while the right-pole label
  `high personal stakes` remains at the axis, so the two labels do not overlap at
  the component's mobile-scaled width.
- Recomputed the Hero badge from the critique's recorded final rendered visible-word
  count of 1,267. At approximately 200 words per minute, rounded up, the chapter now
  shows a 7-minute distillation.

## Critique round 2 — 2026-07-27

### Required

None. The Figure 100.2 marker label now uses the separate top baseline and remains
clear of the right pole label. The Hero now shows seven minutes, which is the
required rounded-up reading time for the recorded 1,267 visible words. The full
re-review found no other blocking defect in sourcing, anatomy, diagram meaning or
geometry, imports, registry data, route, outbound link, or related-book statuses.
`npm run check` passes in full.

### Advisory

No new advisory findings. The per-title cross-link relationship note from round 1
remains advisory and is not reopened.
