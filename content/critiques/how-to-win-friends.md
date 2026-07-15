verdict: revise

## Critique round 1 — 2026-07-15

### Required

- Restore phone legibility for figure 4.3. At a 360px viewport, the layout and figure
  padding leave roughly 280px for the SVG, while this four-step `Flow` has a 558-unit
  viewBox and is explicitly rendered with `w-full`. Its 11.5-unit step labels therefore
  shrink to roughly 6px instead of using the figure wrapper's horizontal overflow. Give
  this diagram a readable mobile presentation, either by preserving a sensible minimum
  width so it scrolls or by using a compact mobile layout, and verify the result at 360px.

### Advisory

- None.
