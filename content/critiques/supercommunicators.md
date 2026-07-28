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

## Critique round 2 — 2026-07-27

### Required

1. **Correct the Hero reading-time badge from the rendered page.** A direct render
   of this exact chapter body contains 1,210 reader-visible words, including the
   Hero, headings, captions, diagram labels, exercise titles, callout, and generated
   component text. At the authoring spec's approximately 200 words per minute,
   rounded up, this is a seven-minute distillation, not `minutes={5}`
   (`src/chapters/supercommunicators.mdx:8-12`).

2. **Remove the unsupported reinforcing polarity from Figure 119.5 and make its
   connections match the prose.** The shared `NodeGraph` reserves
   `kind="reinforcing"` for an accent edge with a plus sign
   (`src/components/diagrams/NodeGraph.tsx:13-19,92-119`). The draft applies that
   meaning to `genuine shared ground -> the disputed claim`
   (`src/chapters/supercommunicators.mdx:123-138`), which visually says shared
   ground increases or reinforces the disputed claim. The prose instead says genuine
   shared ground, identity, values, and experience should receive room while the
   claim remains open to factual discussion. Use neutral associations, or recompose
   and label the graph around the actual movement toward understanding, without an
   unsupported positive causal sign.

The round 1 collision is resolved: Figure 119.4 now puts `reflect, then ask` at
`y=24`, clear of the inline endpoint baseline at `y=74`, and the regression test
checks that separation. The brief and recorded evidence support the three-mode
thesis, practical exercises, and scope caveat; no external search was started.
The remaining anatomy, five in-vocabulary figures, generated cover, related links,
publisher link, registry inventory, and deliberate absence of a Model section agree.
`npm run check` passed on 2026-07-27, including validation, prose lint, pipeline
tests, 254 application tests, typecheck, production build, and ESLint. The repeated
jsdom `Window.scrollTo()` notices were non-failing environment messages.

### Advisory

None.

## Builder resolution — 2026-07-27

- Changed the Hero badge from `5-min distillation` to `7-min distillation`, matching
  the recorded rendered-word count of 1,210 at the specified approximately 200 words
  per minute, rounded up.
- Recast Figure 119.5 as a neutral relationship map with `directed={false}`. All four
  links, including genuine shared ground to the disputed claim, now render without
  arrowheads, accent treatment, or a plus sign. Its aria label now states the intended
  reading: identity, values, experience, and genuine shared ground can be acknowledged
  while the claim remains open to discussion.
- Preserved the round 1 Spectrum correction and its regression test: `reflect, then
  ask` remains on the upper baseline at `y=24`, separate from the inline endpoint at
  `y=74`.
