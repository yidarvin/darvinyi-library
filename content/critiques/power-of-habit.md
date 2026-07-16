verdict: revise

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
