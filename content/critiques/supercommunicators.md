verdict: revise

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
