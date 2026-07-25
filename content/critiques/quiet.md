verdict: resolved

## Critique round 1 — 2026-07-25

### Required

1. **Figure 75.1 renders its marker caption on top of the pole labels.** In
   `src/chapters/quiet.mdx:43-46`, the long marker label is placed at `0.34` without
   overriding `Spectrum`'s default `near-marker` placement. The component draws that
   caption at y=78 and both pole labels at y=74, so "a preference, not a label"
   collides with "lower stimulation" and reaches the higher-stimulation label as well.
   Scaling the SVG or horizontally scrolling it preserves the collision. Move the
   marker caption to the component's non-colliding top placement or otherwise give
   these labels distinct space so the first key-idea diagram is legible.

2. **Figure 75.5 adds an unsupported feedback claim and draws it through the central
   node.** The prose establishes that purpose and preparation support a chosen stretch,
   followed by recovery and sustainable contribution. It does not establish that
   contribution reinforces purpose, yet `src/chapters/quiet.mdx:137-138` marks both
   closing edges as reinforcing and closes that loop. With the supplied coordinates,
   the diagonal `contribute → purpose` edge also passes directly through the "a chosen
   stretch" card, where the later-painted node obscures the connection. Revise the
   graph so its directions match the stated free-trait lesson and every edge has a
   clear, unambiguous route.

### Advisory

None.

## Builder resolution — 2026-07-25

- Figure 75.1 now sets `markerLabelPlacement="top"`, placing the marker caption at
  the top of the Spectrum graphic and leaving the two pole labels unobstructed.
- Figure 75.5 now shows only the supported one-way sequence: purpose and preparation
  support a chosen stretch, which leads to recovery and then sustainable contribution.
  Removed the unsupported contribution-to-purpose feedback edge and its reinforcing
  markers; no remaining edge passes through the central stretch node.
