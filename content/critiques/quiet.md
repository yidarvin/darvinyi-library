verdict: approve

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

## Critique round 2 — 2026-07-25

### Required

1. **Recompute the Hero reading-time badge from the rendered page.** A direct render
   of this exact draft contains 1,229 reader-visible words, including the Hero,
   headings, captions, diagram labels, exercise titles, and generated component text.
   At the authoring spec's approximately 200 words per minute, rounded up, this is a
   seven-minute distillation, not `minutes={6}` (`src/chapters/quiet.mdx:8`). Set the
   badge from the final rendered count.

### Advisory

None. The two round 1 diagram findings remain resolved. Within the repository's
bounded evidence, the brief, seed metadata, registry record, draft, and critique
history support the chapter's central framing; no separate chapter evidence dossier
or source excerpt is recorded, and this review began no external web search. The
draft uses no quotation or real cover art and shows no evident close paraphrase or
source-figure reproduction. Its anatomy, exercises, related links, publisher link,
and deliberately absent Model section otherwise satisfy the content contract.
`npm run check` passed on 2026-07-25, including validation, prose lint, 2 pipeline
tests, 38 runner tests, 155 app tests, typecheck, production build, and ESLint; the
app tests emitted only the existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-25

- Recomputed the Hero badge from the recorded 1,229 reader-visible words. At roughly
  200 words per minute, rounded up, the page is a seven-minute distillation; changed
  `src/chapters/quiet.mdx` from `minutes={6}` to `minutes={7}`.
- Preserved the round 1 diagram corrections: Figure 75.1 keeps its marker caption in
  the top position, and Figure 75.5 remains a supported one-way sequence with clear
  connections.

## Critique round 3 — 2026-07-25

### Required

None. The round 1 diagram findings remain resolved: Figure 75.1 uses the
non-colliding top marker-caption placement, and Figure 75.5 contains only the
supported one-way connections with clear routes between node cards. The round 2
reading-time finding also remains resolved: `minutes={7}` agrees with the recorded
1,229 reader-visible words at approximately 200 words per minute, rounded up.

The chapter follows the required anatomy, with five key ideas and five distinct
in-vocabulary diagrams, concrete practice cards, an appropriately bounded caveat,
and the Model section deliberately absent as required by the brief and registry.
The related slugs are all `done`, the publisher link is present, and the generated
cover uses registry metadata rather than real cover art. Against the repository's
recorded brief, seed metadata, registry entry, and prior critique evidence, the
chapter's factual framing is supported; no separate source dossier is recorded, and
this review began no new external search.

`npm run check` passed on 2026-07-25: validation, prose lint, 2 pipeline tests, 38
runner tests, 155 app tests, typecheck, production build, and ESLint all completed
successfully. The app tests emitted only the existing non-failing jsdom
`Window.scrollTo()` notices.

### Advisory

None.
