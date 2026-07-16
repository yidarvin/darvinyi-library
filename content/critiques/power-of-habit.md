verdict: approve

## Critique round 1 — 2026-07-15

### Required

1. **Make all six figures legible at a 360 px viewport.** Every diagram is rendered
   as `block w-full` with no chapter-local minimum width. At a 360 px viewport, the
   page and `Figure` padding leave roughly 278 px for each SVG. The 380-to-384-unit
   Iceberg, Compare, Spectrum, NodeGraph, and ProcessLoop therefore reduce their
   meaning-bearing 9.5-to-12-unit labels to roughly 7-to-9 CSS px. The 558-unit
   four-step Flow reduces its 11.5-unit step labels to about 5.7 px. This fails the
   explicit phone-legibility requirement and the approximately 11 px floor
   established by completed chapters. Preserve chapter-local rendered widths that
   keep the labels readable inside the existing horizontal-overflow wrapper, or
   provide equally legible compact layouts. Do not change the shared diagram or
   `Figure` components for this finding.

2. **Make Figure 11.2 encode the cue-selection idea stated by its heading and
   caption.** The prose and caption say that one specific situation selects a
   learned response from many possible actions, but the `Flow` labels show a
   diagnostic procedure: notice the situation, name the cue, spot the response,
   and choose a test. That procedure is useful practice, but it does not show the
   structural claim the figure says it shows. Use an in-vocabulary structure and
   labels that visibly connect a cue to the selected routine among alternatives,
   or revise this key idea's visual claim so caption, prose, and diagram teach the
   same relationship.

3. **Keep Figure 11.3's left panel heading inside its panel.** `Compare` renders
   titles as a single unwrapped 13-unit monospace line inside a 168-unit panel. The
   22-character title “watch only the routine” exceeds the roughly 140 units
   available after padding and can run into the center gap or right panel. A larger
   rendered minimum width scales the overflow with the rest of the SVG, so it does
   not repair the internal collision. Shorten the chapter-local title or otherwise
   provide a compact label that remains inside the panel without changing the
   shared `Compare` component.

### Advisory

1. Within the repository's bounded evidence, the factual and copyright posture is
   sound. The chapter brief, seed metadata, and registry support the simple
   cue-routine-reward loop as the thesis and signature model. The draft consistently
   treats the loop as a working model, uses original thematic prose, contains no
   quotation or real cover art, and composes original labels through the shared
   diagram vocabulary rather than reproducing a source figure. The repository has
   no chapter-specific source excerpts or separate evidence dossier for closer
   attribution or close-paraphrase comparison, and this review began no external
   web search.

2. Apart from the required visual findings, the anatomy and practice design are
   sound. Five key ideas each have a captioned vocabulary figure; the Model section
   renders the required three-part habit loop; the four exercises form a concrete
   observation, reward-testing, replacement, and feedback sequence; and the caveat
   appropriately limits the loop around addiction, trauma, disability, material
   constraints, coercive systems, and overconfident “keystone” claims. Both related
   slugs are complete, their relationships are stated in prose, the publisher link
   is direct, and the registry record is complete.

3. `npm run check` passed on 2026-07-15: queue/registry/content validation, prose
   lint, pipeline tests, 26 Vitest tests, TypeScript and Vite production build, and
   ESLint all completed successfully. The jsdom run emitted only the existing
   non-failing `Window.scrollTo()` notices.

## Builder resolution — 2026-07-15

- Added chapter-local `min-w-[440px]` sizing to all six Power of Habit SVGs. Figure's
  existing horizontal-overflow wrapper now preserves the authored label scale at a 360px
  viewport without changing shared Figure or diagram components. At 440px, the 9.5-unit
  labels in the 380-to-384-unit figures render at about 11 CSS pixels or larger.
- Rebuilt Figure 11.2 as an in-vocabulary branching Flow: a specific cue now visibly
  forks toward the learned routine and away from other possible actions, matching its
  prose and caption's cue-selection claim rather than depicting the observation exercise.
- Shortened Figure 11.3's left panel heading to `watch the routine`, which fits within
  the Compare panel without colliding with its center gap or the opposing panel.
- Preserved the existing chapter prose, model, exercises, caveat, links, and earlier
  critique evidence. `npm run check` passes after these changes.

## Critique round 2 — 2026-07-15

### Required

1. **Restore a passing full mechanical gate before approval.** Two consecutive
   `npm run check` runs reached Vitest and failed because `home lists every chapter
   title` exceeded its 15-second timeout, at 15.124 seconds and 15.048 seconds. In
   both runs, the other 25 Vitest tests passed; validation, prose lint, and the two
   pipeline tests also passed before the timeout. Running that exact integration
   test by itself passed in 5.58 seconds, with 3.30 seconds spent in the test, so
   this does not presently identify a Power of Habit rendering assertion failure.
   It still blocks approval because the rubric and definition of done explicitly
   require `npm run check` to pass. Re-run or otherwise resolve the gate through the
   repository's authorized workflow, then record a passing full check.

### Advisory

1. The three required visual findings from round 1 remain resolved. All six figures
   preserve a 440 px authored width inside `Figure`'s horizontal-overflow wrapper;
   Figure 11.2 now branches from the specific cue to the learned routine and other
   possible actions; and Figure 11.3's `watch the routine` title fits the shared
   comparison panel.

2. No new chapter-content blocker emerged from this pass. Within the brief and
   recorded repository evidence, the thesis and three-part model remain supported,
   the five key ideas and practices are coherent, the caveat is appropriately
   bounded, the related slugs resolve to completed chapters, and the publisher link
   and registry metadata remain consistent. No external web search was begun.

## Builder resolution — 2026-07-15

- Preserved the three round-1 chapter fixes: all six Power of Habit figures retain
  their 440 px chapter-local width, Figure 11.2 shows cue-based routine selection,
  and Figure 11.3 uses the compact `watch the routine` heading.
- Restored the full mechanical gate by adding explicit Testing Library cleanup after
  every Vitest case in `src/test/chapters.test.tsx`. Vitest's configuration did not
  expose a global `afterEach` hook for automatic cleanup, so earlier chapter renders
  accumulated in the DOM and made the whole-library home-title query exceed its
  15-second budget. The assertion and its 15-second budget are unchanged; each test
  now starts from a clean rendered document.
- Verified the isolated home-title integration test in 3.155 seconds and the full
  Vitest suite in 10.20 seconds, with all 26 tests passing. `npm run check` then
  passed validation, prose lint, both pipeline tests, Vitest, the TypeScript and Vite
  production build, and ESLint. The existing non-failing `Window.scrollTo()` jsdom
  notices remain unchanged.

## Critique round 3 — 2026-07-15

### Required

None.

### Advisory

1. The round-1 visual blockers remain resolved. Each figure preserves a 440 px
   authored width inside the existing horizontal-overflow wrapper, Figure 11.2
   visibly branches from the cue to the learned routine and other possible actions,
   and Figure 11.3's compact heading stays within its comparison panel. The other
   figures' structures, labels, and captions continue to agree with their prose.

2. Within the chapter brief, seed metadata, registry, and existing critique record,
   the factual and copyright posture remains suitable for approval. The thesis and
   signature diagram center the recorded cue-routine-reward loop, broader claims are
   framed as practical interpretations rather than guarantees, and the caveat limits
   the model around individual and systemic constraints. The prose and diagrams are
   original in form, with no quotation or real cover art. No external web search was
   begun for this review.

3. `npm run check` passed on 2026-07-15. Validation, prose lint, both pipeline tests,
   all 26 Vitest tests, the TypeScript and Vite production build, and ESLint
   completed successfully. The jsdom run emitted only the existing non-failing
   `Window.scrollTo()` notices.
