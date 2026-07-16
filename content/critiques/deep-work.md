verdict: approve

## Critique round 1 — 2026-07-15

### Required

1. **Make all six figures legible at a 360 px viewport.** Every diagram is rendered
   as `block w-full` with no chapter-local minimum width. At a 360 px viewport, the
   page and `Figure` padding leave roughly 280 px for each SVG. The 380-to-384-unit
   Curve, Iceberg, Pyramid, ProcessLoop, and Compare therefore reduce their
   meaning-bearing 9-to-13-unit labels to roughly 6.6-to-9.5 CSS px. The 558-unit
   four-step Flow reduces its 11.5-unit step labels to about 5.8 px. This fails the
   explicit phone-legibility requirement and the approximately 11 px floor used by
   completed chapters. Preserve chapter-local rendered widths inside `Figure`'s
   existing horizontal-overflow wrapper, sized for each primitive's smallest
   meaning-bearing type, or provide equally legible compact layouts. Do not change
   the shared diagram or `Figure` components.

2. **Keep Figure 13.1's right annotation visible and make its visual claim match its
   caption.** `Curve` places the `more work becomes possible` annotation to the
   right of the point at `x: 0.7`; because its anchor switches only when `x > 0.7`,
   that roughly 26-character, 10-unit monospace label extends past the 380-unit
   viewBox and is clipped. A larger rendered width scales the clipping with the
   figure, so it does not repair the internal layout. The figure also draws only
   capability across repeated hard sessions, while the caption claims growth
   faster than a stream of easy completions without drawing an easy-work baseline.
   Reposition or shorten the annotation and either encode the comparison or narrow
   the caption to what the curve actually shows.

3. **Keep Figure 13.4's apex note inside its tier.** The shared `Pyramid` gives the
   apex a 128-unit width and does not wrap tier notes. The 30-character note `one
   thing worth full attention`, rendered in 9-unit monospace type, is approximately
   162 units wide and spills beyond the highlighted `demanding task` tier at every
   rendered size. Use a compact chapter-local note that fits the tier while
   preserving the demanding-target idea.

4. **Make Figure 13.5 and its caption teach the same attention-training loop.** The
   ProcessLoop draws only `friction or boredom` through `brief relief` and back to
   the practiced escape. Its caption additionally says that returning teaches a
   different loop, but no return-to-work path or alternate loop appears in the
   figure. Either show the contrasting practiced return with an in-vocabulary
   composition or limit the caption to the escape loop the figure actually encodes.

5. **Complete the `deep-work` registry record required by the content contract.**
   The record contains the display title, author/year subtitle, shelf, routes, and
   draft status, but it omits `tier`, `thesis`, `framework`, and the diagram-form
   inventory required by definition-of-done item 7. Add the brief-supported tier,
   thesis, deep-versus-shallow framework, and six diagram forms without changing
   unrelated registry entries or shared tooling.

### Advisory

1. The bounded factual and copyright posture is suitable for revision. The brief
   and seed metadata support the rare, valuable, trainable attention thesis and the
   deep-versus-shallow signature model. The chapter's thematic prose uses no quote,
   real cover art, source-order imitation, or bespoke reproduction of a book
   figure. Its claims about visible busyness, task-switching residue, rituals, and
   rehearsed escape are stated cautiously and cohere with the recorded thesis, but
   the repository contains no chapter-specific source excerpts or separate evidence
   dossier for closer attribution or close-paraphrase comparison. This review began
   no external web search.

2. Apart from the required visual and registry findings, the anatomy and practice
   design are sound. Five key ideas each have a captioned vocabulary figure; the
   Model section renders the required deep-versus-shallow distinction; the four
   exercises specify concrete calendar, communication, shallow-work, and restart
   actions; the caveat responsibly covers role constraints and team-level design;
   and the final takeaway is concise. The publisher link is direct, and all three
   related slugs are done.

3. The footer shows three related covers but does not state the one-clause
   relationship requested by the cross-linking guidance. A short chapter-local note
   could explain that *Atomic Habits* and *The Power of Habit* supply the behavior-
   training counterparts, while *The 7 Habits of Highly Effective People* supplies
   the priority-setting counterpart. This remains advisory because the critique
   rubric treats optional cross-link improvement as non-blocking.

4. The `minutes={7}` badge is consistent with approximately 1,300 rendered words at
   200 words per minute, rounded up. `npm run check` passed on 2026-07-15:
   queue/registry/content validation, prose lint, both pipeline tests, all 30 Vitest
   tests, TypeScript and Vite production build, and ESLint completed successfully.
   The jsdom run emitted only the existing non-failing `Window.scrollTo()` notices.

## Builder resolution — 2026-07-15

- Set chapter-local minimum SVG widths inside `Figure`'s existing horizontal-overflow
  wrapper: 440 px for the curve, iceberg, process loop, and comparison; 480 px for
  the pyramid; and 560 px for the four-step flow. This preserves the primitives while
  keeping every meaning-bearing label at or above the phone-legibility floor.
- Shortened and moved Figure 13.1's high-end annotation to `more becomes possible`
  at `x: 0.65`, where it remains inside the curve viewBox. Its caption now describes
  only the depicted hard-session capability curve, rather than an undrawn easy-work
  baseline.
- Replaced Figure 13.4's highlighted apex note with `one hard target`, which fits
  within the 128-unit demanding-task tier at every rendered size.
- Revised Figure 13.5's caption to describe only the escape loop that the ProcessLoop
  renders; the paragraph continues to explain the separate return practice in prose.
- Completed the `deep-work` registry record with tier 1, the brief-supported thesis,
  the deep-work-versus-shallow-work framework, and its six diagram forms. Status
  remains `draft`.

## Critique round 2 — 2026-07-15

### Required

None.

### Advisory

1. All five prior required findings are resolved. The six chapter-local minimum
   widths preserve meaning-bearing type inside `Figure`'s horizontal-overflow
   wrapper at a 360 px viewport. Figure 13.1's revised annotation remains within
   the Curve viewBox and its caption now states only the relationship drawn. Figure
   13.4's apex note fits its tier. Figure 13.5's caption now describes the rendered
   escape loop. The registry record contains the brief-supported tier, thesis,
   framework, and six-form diagram inventory.

2. The independent content judgment remains favorable. The thesis and signature
   comparison agree with the chapter brief and seed metadata. The page uses an
   original thematic structure, original wording, and vocabulary diagrams rather
   than quotations, cover art, source-order imitation, or a reproduced book figure.
   Its claims about demanding practice, visible busyness, interruption costs,
   focus rituals, and rehearsed escape are bounded and consistent with the recorded
   thesis. No chapter-specific source excerpts or separate evidence dossier exist
   for closer attribution or close-paraphrase comparison, and this round began no
   external web search.

3. The required anatomy is complete and useful: five key ideas each have a
   captioned structural figure, the Model renders deep work versus shallow work,
   the four exercises specify concrete actions, the caveat addresses role and
   organizational constraints, and the final takeaway is concise. The related
   slugs resolve to done chapters, and the outbound publisher link is direct.

4. `npm run check` passed on 2026-07-15: queue/registry/content validation, prose
   lint, both pipeline tests, all 30 Vitest tests, TypeScript and Vite production
   build, and ESLint completed successfully. The jsdom run emitted only the
   existing non-failing `Window.scrollTo()` notices.
