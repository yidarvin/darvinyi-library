verdict: approve

## Critique round 1 — 2026-07-28

### Required

1. The signature Model turns negative visualization into a four-step procedure whose required
   endpoint is "take the prudent next act" (`src/chapters/guide-to-good-life.mdx`, lines 160–176),
   and the prose insists that this last step matters. The brief identifies negative visualization
   as the signature model, while the recorded publisher evidence supports its presence as a topic,
   but neither source records prudent risk-reduction as an intrinsic final stage. This addition
   changes the reader's understanding of the book's central exercise from briefly imagining loss
   to renew appreciation into a preparation workflow. Either record direct support for attributing
   that step to Irvine, or distinguish an optional practical consequence from the exercise itself
   in both the prose and diagram.

2. The control section attributes a practical three-ring model to Irvine and carries that model
   into Exercise 02 (`src/chapters/guide-to-good-life.mdx`, lines 53–76 and 188–192), but the
   recorded evidence does not establish that attribution. The Epictetus note supports the ancient
   sharper distinction and calls the rings a "modern, action-oriented three-ring heuristic"; the
   publisher note only records control as a topic. Because the three rings materially determine
   what the reader is told to do, record support tying this exact trichotomy and its internalized
   effort guidance to Irvine, or present it clearly as this page's application rather than as the
   book's own working model.

3. The Hero declares a 10-minute distillation (`src/chapters/guide-to-good-life.mdx`, line 8),
   contrary to the required calculation at roughly 200 words per minute, rounded up. The MDX
   prose extraction is about 1,339 words; even after adding headings, captions, exercise titles,
   diagram labels, and generated book metadata, the rendered page remains well below the more
   than 1,800 words needed to round to 10 minutes. Recompute the badge from the final rendered
   word count.

4. The registry entry is incomplete (`content/registry.json`, lines 2665–2673). It has no `tier`,
   `thesis`, `framework`, or `diagrams`, although the authoring spec's definition of done requires
   those descriptive fields and the completed chapter supplies enough information to populate
   them. Add the correct values, including all six diagram forms, before approval.

### Advisory

1. The first key idea makes a psychological claim that attention "quickly normalizes" an
   acquisition and reaches for a new standard, but the evidence note records no support for
   hedonic adaptation. This is directionally compatible with the brief's dissatisfaction theme,
   yet recording the support would make the causal framing independently auditable.

2. `Compare` is imported but unused. Removing it would keep the chapter's declared component
   surface accurate, though the current toolchain accepts it.

### Verification

`npm run check` passed on 2026-07-28: validation, prose lint, pipeline tests, 290 Vitest
tests, typecheck, production build, and lint all completed successfully. No interactive
`npm run dev` visual review was run because the repository reserves that step for an operator
decision.

## Builder resolution — 2026-07-28

- Recast the Model as the three-part negative-visualization exercise supported by the recorded
  evidence: name something valued, picture a plausible absence, and return attention to what is
  present. The diagram and caption no longer make a prudent act its endpoint. The prose and
  Exercise 01 now place any protective action after the exercise as optional follow-through.
- Recast the concentric figure and Exercise 02 as this page's modern three-ring planning map.
  The control section now distinguishes it from the sharper ancient control distinction and does
  not attribute the trichotomy to Irvine. Added the same attribution boundary to the recorded
  evidence.
- Removed the unused `Compare` import and softened the unsupported rapid-normalization claim in
  the first key idea.
- Recomputed the final rendered reading-time band and changed the Hero badge from 10 to 8
  minutes, which is the rounded-up value at approximately 200 words per minute.
- Completed the `guide-to-good-life` registry record with tier 3, the brief thesis, the
  negative-visualization framework, and all six rendered diagram forms. Its status remains
  `draft`; this resolution does not mark the chapter done.
- Ran the mandatory `npm run check` gate after these changes; validation, prose lint, pipeline
  tests, Vitest, typecheck, production build, and advisory lint passed.

## Critique round 2 — 2026-07-28

### Required

None.

### Advisory

1. Figure 135.1's caption says that attention can bring an ordinary good back into view, but the
   curve itself encodes only novelty fading from "new" to "familiar"
   (`src/chapters/guide-to-good-life.mdx`, lines 41–50). A future polish pass could either narrow
   the caption to the decay the figure actually shows or add an annotation that makes the return
   of attention visible.

### Verification

`npm run check` passed on 2026-07-28: queue and registry validation, prose lint, 42 pipeline
tests, 290 Vitest tests, typecheck, production build, and lint all completed successfully. The
three prior required corrections remain present: the negative-visualization flow ends with
renewed attention rather than a mandatory planning step, the three-ring control map is explicitly
this page's application rather than an attribution to Irvine, and the reading-time and registry
metadata are complete.
