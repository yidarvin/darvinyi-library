verdict: resolved

## Critique round 1 — 2026-07-28

### Required

1. **Complete the registry record before this chapter can be done.** The
   `demon-haunted-world` entry ends after `status` and omits the required `tier`,
   `thesis`, `framework`, and `diagrams` fields
   (`content/registry.json:2565-2573`). Populate those fields from the brief and
   the chapter, identifying the baloney detection kit as the signature framework
   and listing the six forms actually rendered after the diagram findings below
   are resolved. The authoring spec's definition of done requires this metadata
   even though the current validator accepts an incomplete draft entry.

2. **Compress The thesis to the fixed one-or-two-sentence anatomy.** The current
   block is three sentences: the need for more than scientific products, the
   required habits of mind, and science as a method of reducing self-deception
   (`src/chapters/demon-haunted-world.mdx:11-17`). Preserve the useful synthesis,
   but make it the one- or two-sentence carry-away paragraph required by
   `docs/authoring-spec.md`.

3. **Correct Figure 130.2's quadrant placement and separate confidence from action
   policy.** `Matrix` consumes quadrants in `[top-left, top-right, bottom-left,
   bottom-right]` order, with the high end of the vertical axis at the top
   (`src/components/diagrams/Matrix.tsx:13-17,46-51`). The chapter instead places
   “hold lightly / low stakes, low support” in the top-left, which its own axes
   define as large consequence plus thin evidence, and “pause and test / large
   stakes, weak support” in the bottom-right, which the axes define as small
   consequence plus checked evidence
   (`src/chapters/demon-haunted-world.mdx:60-71`). The figure therefore contradicts
   itself. More fundamentally, the section is about confidence tracking evidence
   and a claim's burden relative to established knowledge, while the vertical axis
   switches to the cost of acting wrongly. High consequences can sometimes warrant
   precautionary action under weak evidence, so “pause” is not a safe general rule.
   Recompose the figure so its labels occupy the quadrants the axes actually define
   and so it does not conflate epistemic confidence with a separate decision
   threshold.

4. **Make Figure 130.4 encode independent checking without unsupported
   reinforcing/balancing signs.** The prose says an independent check may expose a
   missing variable or fail to reproduce a result, and that agreement matters
   because the work had a real chance to disagree
   (`src/chapters/demon-haunted-world.mdx:96-105`). The graph instead marks
   `independent check → revised confidence` as reinforcing and
   `revised confidence → claim` as balancing (`:107-125`). The imported component
   renders those kinds as an explicit plus and minus, respectively
   (`src/components/diagrams/NodeGraph.tsx:13-17,94-120`). That teaches that an
   independent check inherently raises confidence and that increased confidence
   suppresses the claim, neither of which follows from the prose. Use neutral
   result-flow edges, show confirming and disconfirming outcomes, or otherwise
   recompose the graph so the signs have defensible meanings.

5. **Repair Figure 130.5's colliding labels.** The chapter supplies the long pole
   labels “automatic belief” and “automatic disbelief” plus the centered marker
   label “curious, testable inquiry,” while leaving the `Spectrum` defaults in
   place (`src/chapters/demon-haunted-world.mdx:141-153`). Those defaults put the
   pole-label baselines at `trackY - 34` and the marker-label baseline at
   `trackY - 30`, only four SVG units apart
   (`src/components/diagrams/Spectrum.tsx:41-43,49-53,129-158`). The centered
   marker text spans into both long endpoint labels, so the meaning-bearing text
   overlaps at every scale, including in the phone scroller. Use the component's
   top marker placement and/or stacked endpoint layout, or shorten and recompose
   the labels so all three remain distinct.

6. **Make the signature baloney-detection model match its prose, its branch, and a
   legible authored width.** The prose names five checks, ending with the result
   that would change the conclusion, but the figure renders only four steps and
   branches directly from “seek an independent check” into “prediction holds” or
   “check fails” (`src/chapters/demon-haunted-world.mdx:156-170`). No prediction
   step precedes that branch, and the stated losing condition is absent as a
   visible check. This reduces the required signature framework to an incoherent
   generic sequence. Recompose it so the visible model contains the core checks
   the paragraph teaches and the branch follows a step that can actually produce
   those outcomes. Also preserve its readable label size: with four steps and a
   branch, `Flow` computes a 716-unit-wide viewBox
   (`src/components/diagrams/Flow.tsx:19-34`), but the chapter permits it to shrink
   to 584 CSS px. That reduces the 11.5-unit step and outcome labels to roughly
   9.4 px at the authored minimum. The shared `Figure` already scrolls
   horizontally, so retain the primitive's native width or recompose it into a
   phone-legible form.

### Advisory

1. Within the bounded record, the chapter's central claims agree with the brief and
   recorded evidence: skeptical inquiry uses clear claims, source and evidence
   checks, alternatives, independent scrutiny, and revision; peer review and
   institutions are not truth machines. The organization, prose, and diagrams
   appear original, with no quotation or real cover art. Because the evidence file
   records source summaries rather than source text, this review could not perform
   sentence-level close-paraphrase comparison and began no new external web search.

2. The remaining anatomy and wiring are sound. There are five key ideas with
   captioned vocabulary diagrams, four concrete exercises, an honest caveat, two
   related slugs that resolve to done chapters, and a publisher purchase link.
   `minutes={8}` is plausible for the draft's rendered length.

3. `npm run check` completed with `CHECK OK` on 2026-07-28. Validation, prose lint,
   40 pipeline tests, 278 Vitest tests, TypeScript, the Vite production build, and
   ESLint all passed. Vitest emitted only the existing non-failing jsdom
   `Window.scrollTo()` notices.

## Builder resolution — 2026-07-28

Resolved every required finding without changing the chapter's status.

1. Completed the draft registry record with tier 3, the distilled thesis, the baloney
   detection kit framework, and the six rendered diagram forms.
2. Compressed “The thesis” to two sentences while retaining the argument that science is
   a method for reducing self-deception.
3. Rebuilt Figure 130.2 around evidence support and the scope of revision a claim would
   require. Its quadrant order now matches `Matrix`'s top-left, top-right, bottom-left,
   bottom-right contract, and it no longer prescribes action from a confidence judgment.
4. Rebuilt Figure 130.4 as neutral result flow from a testable expectation through an
   independent check and competing account to visible agreement or conflict outcomes.
   It has no reinforcing or balancing signs.
5. Set Figure 130.5 to use the Spectrum top marker and stacked endpoint layouts, with
   no endpoint emphasis, so the three labels remain distinct at mobile width.
6. Expanded Figure 130.6 to six visible checks, including the losing result, prediction,
   and independent test before its branch. It now keeps the primitive's 992-unit native
   width through the existing horizontal scroller, preserving its authored label size.
7. Ran `npm run check`: validation, prose lint, pipeline tests, Vitest, TypeScript,
   the production build, and ESLint all passed.
