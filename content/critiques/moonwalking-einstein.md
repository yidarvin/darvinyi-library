verdict: revise

## Critique round 1 — 2026-07-28

### Required

1. **Correct the Hero reading-time badge from the rendered page.** A direct server render of the MDX with its real components contains approximately 1,384 reader-visible alphanumeric words, including the Hero, headings, captions, diagram labels, exercise titles, and generated component text. At the authoring spec's approximately 200 words per minute, rounded up, this is a seven-minute distillation, not `minutes={8}` at `src/chapters/moonwalking-einstein.mdx:11`. Recompute after the other revisions and set the final badge accordingly.

2. **Do not define smallness as an intrinsic property of the memory-palace model.** The Model opens, “A memory palace is a deliberately small map” at `src/chapters/moonwalking-einstein.mdx:132`, and exercise 04 reinforces that characterization at lines 182–185. Neither the chapter brief nor the recorded evidence makes smallness part of the method. They support familiar locations, ordered loci, structured practice, and bounded experimental tasks. Conflating a sensible six-stop beginner exercise with the definition of the signature framework narrows the method without support and changes what the reader is taught. Define the model by its stable, familiar, ordered loci; present a short route only as a beginner-friendly implementation choice.

3. **Make the Model figure encode what its caption claims.** Figure 140.6 says the route is “ready to be walked in either direction” at `src/chapters/moonwalking-einstein.mdx:139`, but the `NodeGraph` keeps its default `directed={true}` and renders only the forward chain `gate → shoes → mirror → stove → table → window` at lines 140–157. The surrounding prose also teaches a fixed order and beginning at the first location. Either remove the unsupported bidirectional claim from the caption or change the figure and explanation so reverse traversal is actually represented without weakening the fixed-order lesson. A hero Model diagram cannot contradict its own caption.

4. **Support or narrow the fifth key idea's account of competitive-memory preparation.** “Speed is built from a reusable vocabulary” asserts that practiced memorizers prebuild images for sounds, categories, cards, and digit patterns and maintain familiar routes (`src/chapters/moonwalking-einstein.mdx:112–119`). This is one of only five major ideas and supplies the page's explanation for competitive speed, but the brief and recorded evidence support loci training, ordered-list performance, distinctive imagery, and bounded transfer, not those specific prebuilt coding systems. Record direct support for this material or narrow the section to the practice effects the evidence actually establishes.

### Advisory

None.
