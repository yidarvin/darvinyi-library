verdict: resolved

## Critique round 1 — 2026-07-17

### REQUIRED

1. **Compress The thesis to the required one or two sentences.** The fixed anatomy
   defines this section as the compact argument a reader can carry away, but the
   current paragraph uses four sentences (`src/chapters/good-strategy.mdx:11-17`).
   Its content agrees with the brief and registry, but the extra setup and test turn
   the thesis into a short explanation rather than the specified one- or two-sentence
   compression. Retain the consequential-difficulty contrast and the three-part
   kernel in no more than two sentences.

2. **Do not define every proximate objective as a constraint to remove.** The section
   first describes the concept accurately as a demanding nearer target within reach
   of current knowledge and resources, then categorically says, "It is the constraint
   whose removal opens the next move" (`src/chapters/good-strategy.mdx:109-120`). A
   proximate objective makes a strategically useful target feasible amid uncertainty;
   removing a bottleneck can be one instance, but it is not the definition. The
   figure repeats the narrowing with `names the next constraint`
   (`src/chapters/good-strategy.mdx:122-133`). Preserve the onboarding example if
   useful, but make constraint removal an example rather than a universal condition,
   and keep the prose, comparison, caption, and exercise consistent.

3. **Separate Figure 65.2's overlapping pole and marker labels.** The chapter gives
   the Spectrum a long right pole, `one chosen approach`, and a `guiding policy`
   marker at 0.76 (`src/chapters/good-strategy.mdx:60-71`). The primitive renders the
   right pole at `(340, 74)` with end anchoring and the marker label at approximately
   `(268, 78)` with center anchoring, so the two mono labels occupy the same horizontal
   and vertical region (`src/components/diagrams/Spectrum.tsx:92-110`). The 440px
   chapter-local minimum width preserves font size but scales both labels together,
   so it cannot remove the collision. Recompose or relabel this in-vocabulary figure
   so every meaning-bearing label is independently legible, and avoid implying that
   a guiding policy must be a single tactic rather than a chosen approach that can
   coordinate several actions.

4. **Correct the Hero reading-time badge from the direct render.** A direct static
   render of the chapter body contains 1,459 reader-visible alphanumeric word tokens,
   including the Hero, headings, captions, diagram labels, exercise titles, and
   generated component text. At the authoring spec's approximately 200 words per
   minute, rounded up, this is an eight-minute distillation, not `minutes={7}`
   (`src/chapters/good-strategy.mdx:5-9`). Recount after the required content edits
   and set the final badge from that render.

The chapter brief, seed metadata, registry record, and draft were the only local
chapter evidence found; there is no separate recorded evidence dossier, and this
review began no external web search. Against those records, the central thesis and
signature kernel are correct. The page otherwise has five key ideas with captioned
in-vocabulary diagrams, the required Model, concrete practice cards, an honest
caveat, a generated typographic cover, two completed related chapters, and a direct
publisher link. Registry metadata and the six-form diagram inventory match the
current draft.

`npm run check` passed on 2026-07-17: queue/registry/content validation, prose lint,
2 pipeline tests, 37 runner tests, 134 application tests, typecheck, production build,
and ESLint all completed successfully. Vitest emitted only the existing non-failing
jsdom `Window.scrollTo()` notices. The gate does not enforce the thesis sentence
limit, test conceptual scope, detect SVG label collisions, or recompute reading time.

### ADVISORY

1. `ShelvedNearby` renders two relevant completed books, but the page gives neither
   link the one-clause relationship requested by the cross-linking guidance
   (`src/chapters/good-strategy.mdx:224-228`). A short chapter-local sentence can
   explain how `good-to-great` and `zero-to-one` connect to this framework; the links
   themselves resolve, so this remains optional enrichment.

## Builder resolution — 2026-07-17

- Compressed **The thesis** to two sentences while retaining the consequential-
  difficulty contrast and the diagnosis, guiding-policy, coherent-action kernel.
- Reframed the proximate objective as a feasible, strategically useful nearer target
  amid uncertainty. Constraint removal is now one possible target, and the Figure
  65.4 comparison and exercise use the same broader framing.
- Added the reusable `Spectrum` `markerLabelPlacement` option and used its top
  placement in Figure 65.2. The `guiding policy` marker now has its own vertical
  space above the pole labels; the right pole now reads `chosen approach`, and the
  caption makes clear that this approach coordinates multiple actions.
- Changed the Hero from `minutes={7}` to `minutes={8}`. The critique's recorded
  1,459 visible-word direct render already rounds up to eight minutes at the house
  rate, and the required edits reduce that total rather than crossing the 1,600-word
  threshold for nine minutes.
