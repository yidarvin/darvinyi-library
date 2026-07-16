verdict: approve

## Critique round 1 — 2026-07-16

### Required

1. **Compress "The thesis" to the required one or two sentences.** The section at
   `src/chapters/superforecasting.mdx:12` currently runs five sentences. The
   authoring spec reserves this paragraph for the single compact argument a reader
   can carry away. Preserve the useful sequence of decomposition, base rates,
   explicit probabilities, and revision, but make the section conform to the fixed
   anatomy.

2. **Make Figure 47.1 show what its key idea and caption claim.** The heading and
   prose explain decomposition: one broad question is split into smaller,
   answerable drivers. The figure at `src/chapters/superforecasting.mdx:32` instead
   renders a linear workflow in which `separate key drivers` is only one box, and
   no broad question visibly divides into testable parts. The caption nevertheless
   says that the figure shows that division. Recompose the visual with an
   in-vocabulary form that actually encodes one-to-many decomposition, or revise
   the key idea and caption so the displayed procedure is the idea being taught.

3. **Complete the `superforecasting` registry record.** The draft entry at
   `content/registry.json:932` contains display metadata and `status: "draft"` but
   omits the authoring spec's required `tier`, `thesis`, `framework`, and `diagrams`
   fields. Record tier 2 and the brief-supported thesis; state that there is no
   single signature model and that the Model section is deliberately absent; and
   inventory the six forms actually used: flow, comparison, spectrum, process
   loop, timeline, and node graph.

### Advisory

1. Figure 47.3 accents the high-probability `likely, not certain` band while the
   current 62 percent estimate sits in a muted band. The prose argues for calibrated
   probabilities, not for confidence as the preferred state. Neutral treatment of
   the bands, with the current estimate carrying the accent, would align the visual
   hierarchy more closely with that lesson.

2. Within the bounded local record, the remaining factual framing is careful and
   consistent with the brief. The draft treats forecasting as a learnable practice,
   covers comparison classes, numerical probabilities, frequent revision, scoring,
   calibration, and aggregation, and confines its empirical scope to resolved
   geopolitical tournament questions. The caveat correctly separates a forecast
   from a decision and avoids claiming universal transfer or mastery of singular
   events. No new external web search was begun for this review.

3. The rest of the fixed anatomy and technical contract is intact. Six key ideas
   each have a captioned shared-vocabulary diagram; omitting the Model section
   matches the chapter brief; the four exercises are concrete; the three nearby
   slugs resolve to done chapters and their relationships are summarized in the
   preceding sentence; and the outbound link points to the publisher's book page.
   The chapter-local minimum widths preserve the SVGs in `Figure`'s horizontal
   scroller, and the seven-minute badge is consistent with the visible content at
   approximately 200 words per minute rounded up.

4. `npm run check` passed on 2026-07-16: queue, registry, critique, and content
   validation; prose lint; both pipeline tests; all 98 Vitest tests; TypeScript and
   the Vite production build; and ESLint. Vitest emitted only the existing
   non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-16

- Compressed `The thesis` to two sentences while retaining the required sequence: decompose the question, start from comparable cases, state explicit odds, revise with evidence, and learn from a scored record.
- Rebuilt Figure 47.1 as an in-vocabulary branching flow: the broad market-recovery question now visibly splits into the answerable drivers of demand strength and policy support. Its caption remains accurate, and its alternative description names the split.
- Completed the `superforecasting` registry record with tier 2, the brief-supported thesis, a note that no single signature model exists and the Model section is deliberately absent, and the six rendered forms in page order: flow, comparison, spectrum, process loop, timeline, and node graph. The chapter status remains `draft`.
- Also removed the advisory high-probability band accent from Figure 47.3, leaving the current estimate as the diagram's visual emphasis. No external search was needed.

## Critique round 2 — 2026-07-16

### Required

None.

### Advisory

1. The three round 1 requirements are resolved. The thesis is now two sentences;
   Figure 47.1 visibly branches the broad question into answerable drivers; and the
   registry records tier, thesis, the deliberate absence of a Model section, and all
   six diagram forms. The Figure 47.3 accent advisory was also addressed. No settled
   finding was reopened, and no new external web search was begun.

2. The remaining draft continues to match the bounded chapter brief and recorded
   repository evidence. Its anatomy, exercises, caveat, related links, publisher
   link, captions, component imports, and diagram labels are internally consistent.
   The shared minimum-width and horizontal-scroll treatment preserves diagram label
   size on narrow screens.

3. `npm run check` passed on 2026-07-16: repository validation, prose lint, both
   pipeline tests, all 98 Vitest tests, TypeScript, the Vite production build, and
   ESLint. Vitest emitted only the existing non-failing jsdom `Window.scrollTo()`
   notices.
