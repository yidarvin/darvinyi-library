verdict: resolved

## Critique round 1 — 2026-07-27

### Required

1. Figure 119.4 has a label collision that makes the diagram illegible. In
   `src/chapters/supercommunicators.mdx:99`, the `Spectrum` places the inline right
   endpoint label, "building a shared account," at `y=74` across much of the right
   half of the SVG, while the marker label, "reflect, then ask," is centered at
   roughly the same horizontal position at `y=78`. Scaling or horizontal scrolling
   preserves the overlap because both labels share the same viewBox coordinates.
   Use the primitive's existing collision-avoidance layout props, or otherwise
   separate those two labels, and verify that both remain readable at phone width.

### Advisory

None.

## Builder resolution — 2026-07-27

- Set Figure 119.4's `markerLabelPlacement="top"`. The marker label `reflect, then
  ask` now renders at the separate upper baseline, while `building a shared account`
  remains on the inline endpoint baseline, so their SVG text boxes do not overlap at
  phone width.
- Added a Spectrum regression test using Figure 119.4's labels. It asserts the top
  marker baseline (`y=24`) remains separate from the inline endpoint baseline (`y=74`).
