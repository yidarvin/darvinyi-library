verdict: approve

## Critique round 1 — 2026-07-16

### Required

1. **Compress `The thesis` to the fixed one-or-two-sentence anatomy.** The section
   currently uses five sentences to move from unwitnessed history through scientific
   method to the ordinary morning (`src/chapters/short-history-nearly-everything.mdx:11-17`).
   The Hero line does not replace the required Thesis block. Preserve the useful
   scale-and-method synthesis, but make this section the one or two sentences a reader
   can carry away.

2. **Complete the registry record and make it agree with the rendered chapter.** The
   draft entry contains only identity, shelf, route, and status fields
   (`content/registry.json:717-725`). The definition of done also requires `tier`,
   `thesis`, `framework`, and the diagram inventory. Record the deliberate absence of
   a signature framework, as required by the brief, and list the six rendered forms in
   page order.

3. **Recompute the Hero reading-time badge from the rendered page.** A direct MDX
   render contains 1,437 reader-visible words, including the Hero and cover metadata,
   headings, captions, SVG labels, exercise titles, prose, and nearby-book footer. At
   the authoring spec's approximately 200 words per minute, rounded up, this is an
   eight-minute distillation, not `minutes={9}`
   (`src/chapters/short-history-nearly-everything.mdx:5-9`). Recompute after the other
   revisions and set the final badge from that rendered count.

4. **Preserve meaning-bearing label sizes for all six figures at a 360 px viewport.**
   Every SVG is explicitly `block w-full` with no chapter-local minimum width
   (`src/chapters/short-history-nearly-everything.mdx:38-160`). At a 360 px viewport,
   Layout and Figure padding leave roughly 278 px for the SVG. The 558-unit four-step
   Flow therefore reduces its 11.5-unit labels to about 5.7 CSS px and its 9-unit
   sequence numbers to about 4.5 px. The 416-unit Timeline and 380-unit remaining
   forms reduce their smallest labels to roughly 6.3 to 8.8 px. Figure's horizontal
   overflow cannot engage while each child is forced to fit the available width.
   Give the chapter-local compositions sufficient minimum rendered widths, or use
   compact in-vocabulary layouts, so their authored text remains phone-legible without
   changing shared components.

5. **Make Figure 36.1's geometry encode the scale contrast it is meant to teach.**
   The prose distinguishes 13.8 billion, 4.6 billion, and 300,000 years, but the
   Timeline assigns all three milestones equal horizontal spacing
   (`src/chapters/short-history-nearly-everything.mdx:29-48`; `src/components/diagrams/Timeline.tsx:17-31`).
   That geometry turns an orders-of-magnitude contrast into three equal intervals and
   leaves the central “arrived very late” idea in labels alone. Use an in-vocabulary
   magnitude or time composition that visibly preserves the contrast, or explicitly
   separate ordered milestones from a second visual encoding of relative duration.

6. **Remove Figure 36.3's unsupported compounding semantics.** The rock-cycle prose
   describes formation, exposure, weathering, burial, and remaking, but does not claim
   that the return from burial to formation compounds or reinforces the system. Passing
   `compoundingEdge={3}` assigns exactly that vocabulary meaning to the final edge
   (`src/chapters/short-history-nearly-everything.mdx:73-89`; `src/components/diagrams/ProcessLoop.tsx:8-14,62-83`).
   Render the ordinary cycle without a compounding edge, or state and label a supported
   feedback mechanism rather than using unexplained accent as decoration.

7. **Remove or justify Figure 36.4's positive-reinforcement signs.** The prose and
   caption say that life and planetary conditions alter one another. The graph instead
   marks `living communities → atmosphere` and `conditions for later life → living
   communities` as `kind="reinforcing"`, which the imported component draws as accent
   plus signs (`src/chapters/short-history-nearly-everything.mdx:91-117`;
   `src/components/diagrams/NodeGraph.tsx:12-16,70-103`). Those broad nodes are not
   signed scalar variables, so “more life increases atmosphere” and “more habitat
   increases life” are not coherent general causal claims. Use unsigned alteration
   edges, or define narrower variables and a genuinely supported reinforcing loop.

8. **Eliminate Figure 36.6's intrinsic label collision and match its form to its
   claim.** The shared Spectrum places both pole labels at `y=74` and the marker label
   at `y=78`. With `right="testable question"`, `marker={0.78}`, and
   `markerLabel="a claim with evidence"`, the right pole and marker occupy overlapping
   horizontal ranges on nearly the same baseline, so they collide at every rendered
   size (`src/chapters/short-history-nearly-everything.mdx:140-160`;
   `src/components/diagrams/Spectrum.tsx:92-110`). Shorten or remove the colliding
   labels, or use a directed Flow if the intended idea is progression from surprise to
   a testable claim rather than degree along one continuum.

### Advisory

1. Within the repository's bounded evidence, the copyright posture is sound. The
   chapter uses original thematic organization, no quotation or real cover art, and
   shared diagram primitives rather than a reproduced source figure. The brief
   supports the sweep from cosmic history to human origins, the curious-amateur frame,
   and deliberate omission of a signature Model. The repository contains no source
   excerpts for a close-paraphrase comparison, and this review began no new external
   web search.

2. The caveat attributes the approximately 13.8-billion-year age to NASA but provides
   no NASA link, while the nearby Smithsonian claim does have a recorded direct URL
   (`src/chapters/short-history-nearly-everything.mdx:193-203`). The number is not a
   misleading change to the chapter's argument, so this does not block approval by
   itself, but a direct recorded source would make the attribution auditable and
   parallel the human-origins citation.

3. The page's scale-and-method synthesis is coherent, but it leans more heavily toward
   a general lesson in scientific epistemology than the brief's grand tour from the Big
   Bang to human origins. One concrete connection among cosmic material, planetary
   change, life's history, and the late human arrival would make the chapter feel more
   unmistakably specific to Bryson without recreating his chapter order.

4. Apart from the required findings, the page anatomy and wiring are sound. Six key
   ideas each have a captioned vocabulary figure; omission of a Model follows the
   brief; four exercises are concrete; the caveat is appropriately skeptical of an
   aging popular synthesis; `sapiens` and `selfish-gene` both resolve to done chapters;
   and the outbound Penguin Random House URL points directly to the publisher's page.

5. `npm run check` completed with `CHECK OK` on 2026-07-16: queue, registry,
   critique, and content validation; prose lint; both pipeline tests; all 76 Vitest
   tests; TypeScript and Vite production build; and ESLint passed. Vitest emitted only
   the existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-16

Resolved every required finding in the current critique while preserving the existing
chapter structure and caveat.

1. Compressed **The thesis** to two sentences that retain the scale-and-method
   synthesis.
2. Completed the registry entry with tier, rendered thesis, the deliberate absence of
   a single signature framework, and the six diagram forms in page order.
3. Recomputed the chapter after the revisions and changed the Hero badge to an
   eight-minute distillation.
4. Added chapter-local SVG minimum widths, inside Figure's existing horizontal scroll
   container: 380 px for Bars, ProcessLoop, NodeGraph, and Iceberg; 558 px for the
   four-step Flow; and 420 px for the three-step Flow. This retains authored label
   sizes at a 360 px viewport instead of shrinking them to fit.
5. Replaced the equal-interval Timeline with relative-scale Bars. The universe, Earth,
   and modern-human durations now use a common linear scale, making the late human
   arrival geometrically visible.
6. Removed the ProcessLoop `compoundingEdge`, leaving an ordinary rock cycle.
7. Changed both NodeGraph feedback edges to unsigned alteration edges, removing the
   unsupported positive-reinforcement signs.
8. Replaced the overloaded Spectrum with a directed three-step Flow from surprise to
   a testable question to evidence for a claim, eliminating the label collision and
   matching the chapter's progression claim.

## Critique round 2 — 2026-07-16

### Required

1. **Keep the universe value label inside Figure 36.1's SVG viewBox.** The replacement
   Bars composition fixes the earlier equal-spacing problem, but the full-length
   universe bar sets `value={1}`, which makes its value label begin at x=346 in a
   380-unit viewBox (`src/chapters/short-history-nearly-everything.mdx:36-44`;
   `src/components/diagrams/Bars.tsx:23-25,32,38-39,50-55`). Only 34 units remain for
   the 10-unit mono label `13.8 billion years`, so most of that meaning-bearing label
   is clipped at the right edge. Use a chapter-local Bars composition that leaves room
   for the longest value label, places the value inside the full bar, or otherwise
   keeps every displayed age legible without changing the shared component.

### Advisory

1. All eight round-1 findings otherwise verify as resolved in the current draft. The
   thesis now fits the two-sentence anatomy; the registry records the missing Model
   deliberately and inventories all six forms; the eight-minute badge is consistent
   with the recorded rendered count; minimum widths engage Figure's horizontal scroll;
   and Figures 36.3, 36.4, and 36.6 no longer encode the unsupported or colliding
   semantics identified earlier.

2. Within the repository's recorded evidence, the factual and copyright posture
   remains acceptable. The brief supports the grand-tour framing and lack of a
   signature model; the draft uses original thematic organization and shared diagram
   forms; the Smithsonian URL directly supports the approximately 300,000-year human
   date; and no new external search was started for this review. The uncited NASA
   attribution remains advisory for the reason recorded in round 1.

3. `npm run check` completed with `CHECK OK` on 2026-07-16: validation and prose lint
passed; both pipeline tests and all 76 Vitest tests passed; TypeScript, the Vite
production build, and ESLint passed. Vitest emitted only the existing non-failing
jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-16

Resolved the remaining required finding from critique round 2. Figure 36.1 now puts
each full age in its wrapped, left-hand row label and removes the trailing value labels.
The universe's full-length bar can therefore remain a true maximum on the common linear
scale without clipping its `13.8 billion years` label at the SVG's right edge. The
composition keeps its existing 380 px chapter-local minimum width, so all three age
labels remain legible on a 360 px viewport through Figure's horizontal scroll container.

## Critique round 3 — 2026-07-16

### Required

None. The remaining round-2 figure defect is resolved: Figure 36.1 retains a common
linear scale, keeps each complete age in the wrapped row label, and no longer places a
meaning-bearing value label beyond the SVG viewBox. The chapter now satisfies the
copyright, anatomy, diagram, interaction, and technical-integrity requirements in the
critique rubric.

### Advisory

1. No new advisory findings. Within the repository's recorded evidence, the factual
   posture remains acceptable: the brief supports the grand-tour framing and deliberate
   absence of a signature model, while the recorded Smithsonian link supports the
   approximately 300,000-year age used for *Homo sapiens*. This review began no new
   external web search.

2. `npm run check` completed with `CHECK OK` on 2026-07-16. Validation and prose lint
   passed; both pipeline tests and all 76 Vitest tests passed; TypeScript, the Vite
   production build, and ESLint passed. Vitest emitted only the existing non-failing
   jsdom `Window.scrollTo()` notices.
