verdict: approve

## Critique round 1 — 2026-07-16

### Required

1. **Compress "The thesis" to the required one or two sentences.** The section at
   `src/chapters/why-we-sleep.mdx:13` currently runs four sentences. The authoring
   spec defines this paragraph as the one- or two-sentence compression a reader can
   carry away. Preserve the useful balance between protecting sleep, avoiding
   perfectionism, and investigating persistent problems, but make the section
   conform to the fixed anatomy.

2. **Replace Figure 46.4's U-curve with a form that matches the stated decline.** The
   prose and caption say reliable daytime performance keeps declining across
   successive restricted nights, but `shape="u"` at
   `src/chapters/why-we-sleep.mdx:117` falls and then rises back to its starting
   height. Its `debt accumulates` annotation also sits away from that plotted line.
   The figure therefore reverses the key idea over the latter half of the x-axis.
   Use an in-vocabulary composition whose actual geometry shows the claimed
   cumulative decline, and keep the registry's diagram record in agreement.

3. **Preserve Figure 46.5's authored label size on a phone.** Five steps give the
   shared `Flow` a computed 696-unit viewBox, while the chapter sets only
   `min-w-[560px]` at `src/chapters/why-we-sleep.mdx:137`. Even inside `Figure`'s
   horizontal scroller, that scales the component's 11.5-unit labels down to about
   9.3 CSS pixels. Raise the chapter-local minimum width to the generated viewBox
   width, or reduce/recompose the steps so the labels remain legible at 360px.

4. **Correct the reading-time badge from eight minutes to seven.** A direct test
   render through the repository's MDX provider and chapter components produced
   1,324 visible words. At the specified 200 words per minute, rounded up, the Hero
   value at `src/chapters/why-we-sleep.mdx:8` is seven minutes.

5. **Support or remove the specific 42-study mortality assertion.** The mandatory
   caveat is required to be sourced, but the sentence at
   `src/chapters/why-we-sleep.mdx:183` names a precise evidence base and conclusion
   without linking or identifying the review. The chapter brief and repository do
   not contain a separate evidence record that substantiates it. Cite the review
   directly and make the wording match its conclusion, or retain the surrounding
   observational caveat without this unsupported numerical claim.

### Advisory

1. Figure 46.1 uses `favor="right"`, which accents circadian timing as if it were
   preferable to sleep pressure even though the prose presents two complementary
   forces. Consider `favor="none"` when revising so the visual hierarchy matches the
   explanation.

2. Within the bounded evidence available for this review, the remaining factual
   claims are careful and plausible: the draft distinguishes sleep pressure from
   circadian timing, qualifies stage-specific functions, treats memory reactivation
   as a modest contribution rather than a learning shortcut, and avoids turning one
   poor night into a health diagnosis. The recorded audit and PDF links could not be
   independently reopened in this environment, and no new external search was
   begun.

3. The rest of the required structure is intact. Five key ideas each have a
   captioned diagram from the shared vocabulary; the absent Model section matches
   the brief and registry; the practices are concrete and appropriately direct
   persistent symptoms toward qualified care; the mandatory criticism is prominent;
   related slugs resolve to completed chapters; and the outbound link points to the
   publisher's book page. `npm run check` passed on 2026-07-16, including validation,
   prose lint, pipeline tests, all 96 Vitest tests, TypeScript, the production build,
   and ESLint. Vitest emitted only the existing non-failing jsdom
   `Window.scrollTo()` notices.

## Builder resolution — 2026-07-16

- Compressed **The thesis** to two sentences while retaining protected sleep, avoiding
  perfectionism, and investigating persistent problems.
- Replaced Figure 46.4's U-curve with the existing conceptual `Bars` form, whose four
  successive-night bars visibly decline; updated the matching registry diagram record
  from `annotated curve` to `bars`.
- Raised Figure 46.5's local minimum width to its generated 696-unit `Flow` viewBox
  width, preserving the authored label size in the figure's horizontal scroller.
- Corrected the Hero badge to a seven-minute distillation and set the complementary
  sleep-pressure comparison to neutral emphasis.
- Removed the unsupported 42-study mortality assertion while preserving the sourced,
  observational caveat and the recorded audit links.
- Ran `npm run check`: validation, prose lint, pipeline tests, all 96 Vitest tests,
  TypeScript, and the production build passed. Vitest retained only the existing
  non-failing jsdom `Window.scrollTo()` notices.

## Critique round 2 — 2026-07-16

### Required

None.

### Advisory

1. The five round-one blockers are resolved without introducing a new mismatch. The
   thesis is two sentences; Figure 46.4 now uses descending conceptual bars; Figure
   46.5 preserves the shared Flow component's authored label size in the horizontal
   scroller; the seven-minute badge agrees with the recorded rendered word count;
   and the unsupported 42-study assertion has been removed.

2. Within the chapter brief and recorded evidence available for this review, the
   factual framing remains appropriately qualified. The page distinguishes the two
   forces governing sleep, avoids assigning exclusive benefits to individual sleep
   stages, describes memory reactivation effects as modest, and treats chronic sleep
   restriction as a safety concern without turning an isolated poor night into a
   diagnosis. The mandatory caveat names the documented criticism plainly and keeps
   observational mortality associations separate from causal claims. No new external
   web search was begun.

3. The fixed anatomy and visual contract are satisfied. Five key ideas each have a
   captioned, in-vocabulary diagram whose labels agree with the prose; omitting the
   Model section matches both the brief and registry; the practice cards are concrete
   and include appropriate clinical escalation; related slugs resolve to completed
   chapters; and the generated typographic cover and publisher link preserve the
   copyright line. `npm run check` passed on 2026-07-16, including validation, prose
   lint, pipeline tests, all 96 Vitest tests, TypeScript, the production build, and
   ESLint. The only test output beyond passes was the existing non-failing jsdom
   `Window.scrollTo()` notice.
