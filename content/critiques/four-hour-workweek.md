verdict: revise

## Critique round 1 — 2026-07-23

### REQUIRED

1. **Compress The thesis to the required one or two sentences.** The fixed anatomy
   defines this section as the compact argument a reader can carry away, but the
   draft uses five sentences (`src/chapters/four-hour-workweek.mdx:14-21`). Preserve
   the deferred-life diagnosis and the progression from definition through removal
   and systems to nearer-term freedom, but express that argument in no more than two
   sentences.

2. **Replace Figure 70.1 with a diagram that actually shows experiments happening
   before the deferred finish line.** The prose and caption teach trying parts of the
   imagined future now, in smaller and more frequent stretches. The timeline instead
   orders `defer → save → retire → try now`
   (`src/chapters/four-hour-workweek.mdx:33-53`), placing the highlighted experiment
   after retirement and visually preserving the exact deferred-life sequence the
   section rejects. Use an in-vocabulary form whose structure makes the alternative
   visible rather than appending it to the old path.

3. **Make Figure 70.2 encode the cost-of-inaction comparison stated by its prose and
   caption.** The section says to compare a feared outcome and its repair with the
   cost of staying put, and the caption says those costs are weighed. The rendered
   `Flow` contains only `name the desired change → describe the feared outcome →
   plan a repair → run a bounded test`
   (`src/chapters/four-hour-workweek.mdx:55-71`). It has no cost of inaction and no
   comparison, so the key idea's structural diagram omits the decision the text says
   it teaches. Add that comparison using the shared vocabulary and keep the caption
   aligned with the resulting figure.

4. **Separate Figure 70.4's marker label from both pole labels.** The chapter leaves
   `Spectrum` at its default near-marker placement while using the long strings
   `always interruptible`, `clear response windows`, and `never reachable`
   (`src/chapters/four-hour-workweek.mdx:102-115`). The component draws the pole
   labels at `y=74` and the marker label at `y=78`; at `marker={0.55}` their
   horizontal spans overlap on both sides
   (`src/components/diagrams/Spectrum.tsx:43-47,95-121`). The result is three labels
   overwriting one another. Use the component's top placement or otherwise revise
   this chapter's labels and placement so all structural text is legible.

5. **Keep Figure 70.3's final value label inside the SVG viewport.** `Bars` gives the
   plot a 380-unit viewBox and starts a value label at `trackX + value × trackW + 6`
   (`src/components/diagrams/Bars.tsx:23-25,31-34,38-55`). With this chapter's
   `value={0.91}`, `protect it` begins at approximately x=327.6 and its ten
   10-pixel mono glyphs extend beyond x=380
   (`src/chapters/four-hour-workweek.mdx:82-91`). The right end is clipped rather
   than legible. Shorten or reposition the chapter-local label, or otherwise leave
   enough right-side room without changing the idea.

6. **Recompute the Hero reading-time badge from the rendered page.** A direct server
   render of this exact draft contains 1,606 reader-visible alphanumeric word tokens,
   including Hero and cover metadata, headings, captions, SVG labels, exercises,
   callout text, and the nearby-book footer. At approximately 200 words per minute,
   rounded up, this is a nine-minute distillation, not `minutes={8}`
   (`src/chapters/four-hour-workweek.mdx:8-12`). Recount after the required revisions
   and set the final badge from that render.

The chapter brief and seed record support the deferred-life thesis and DEAL signature
model. No chapter-specific evidence dossier or source excerpt exists in the repository,
so factual and close-paraphrase review was bounded to those records and internal
agreement among the prose, captions, diagrams, and metadata; this review began no new
external web search. Within that boundary, the draft otherwise uses original thematic
prose, no quotation or real cover art, six key ideas with captioned shared-vocabulary
figures, a DEAL model figure, four concrete exercises, and a substantive caveat. The
registry inventory matches the rendered diagram forms, all three related slugs are done
and have relationship clauses, and the outbound link is a direct publisher page.

`npm run check` passed on 2026-07-23: queue/registry/content validation, prose lint, 2
pipeline tests, 38 runner tests, 145 application tests, TypeScript, production build,
and ESLint all completed successfully. Vitest emitted only the existing non-failing
jsdom `Window.scrollTo()` notices. The gate does not enforce thesis length, judge
diagram-to-prose semantics, detect SVG text collisions or clipping, or recompute the
reading-time badge.

### ADVISORY

1. **Avoid the unsupported reception claim in Why it matters.** “The book landed
   because it makes that mismatch visible” asserts a cause for the book's reception
   (`src/chapters/four-hour-workweek.mdx:23-29`), but neither the chapter brief nor
   another recorded evidence artifact supports that causal claim. This does not
   change the framework being taught, so it is not independently blocking, but a
   future revision should either state the significance without claiming why readers
   received it as they did or record suitable evidence.

## Builder resolution — 2026-07-23

- Compressed **The thesis** to two sentences while retaining the deferred-life
  diagnosis, near-term definition, elimination, systems, and usable freedom.
- Replaced Figure 70.1's deferred timeline with a split comparison between deferring
  life and testing a valued piece now, so experiments occur before retirement rather
  than after it.
- Replaced Figure 70.2's one-way flow with a balanced comparison of fear-and-repair
  and the cost of inaction; its caption now names that comparison.
- Set Figure 70.4's `markerLabelPlacement="top"`, separating the marker label from
  both spectrum poles, and shortened Figure 70.3's final value label to `focus` so
  it remains inside the Bars viewport.
- Rendered the exact `/four-hour-workweek` route and counted 1,550 reader-visible
  alphanumeric tokens. At 200 words per minute, rounded up, this confirms the
  existing eight-minute Hero badge.

## Critique round 2 — 2026-07-23

### REQUIRED

1. **Update the registry's diagram inventory to match the resolved draft.** The
   builder replaced Figure 70.1's `Timeline` and Figure 70.2's `Flow` with
   `Compare` figures, but the registry still lists `timeline, flow, bars, spectrum,
   node graph, comparison, flow`
   (`content/registry.json:1393-1400`). The chapter now renders `comparison,
   comparison, bars, spectrum, node graph, comparison, flow`
   (`src/chapters/four-hour-workweek.mdx:40-191`). Correct the inventory so the
   registry agrees with the page on disk. `npm run check` currently does not
   validate these form names, so its passing result does not clear this mismatch.

2. **Untangle Figure 70.5's crossing connections and overlapping edge labels.**
   The chapter places `owner` and `record` on one horizontal row, then draws
   `owner → record` across the center and `review → outcome` vertically through
   that same connection (`src/chapters/four-hour-workweek.mdx:134-150`). Under
   `NodeGraph`'s placement and midpoint-label formulas
   (`src/components/diagrams/NodeGraph.tsx:41-56,74-120`), the two lines intersect
   near `(187, 170)`, while `update` and `improve` are centered at approximately
   `(184, 166)` and `(187, 158)` in 12-pixel type. Their horizontal spans nearly
   coincide and their baselines are less than one font height apart, so the labels
   overwrite each other and the paths are ambiguous at every display width. Move a
   node or connection path and use the available chapter-local label offsets so the
   loop and all four handoffs remain separately legible.

The six required findings from round 1 are otherwise resolved in the current source.
The thesis is two sentences; Figures 70.1 and 70.2 now encode the comparisons stated
by their prose; Figure 70.4 uses the top marker-label placement; Figure 70.3's `focus`
label stays within the 380-unit viewport; and the builder's recorded 1,550-token
render supports the retained eight-minute badge. The brief and seed record still
support the deferred-life thesis and DEAL model. No separate chapter-specific
evidence dossier or source excerpt exists, and this review began no new external web
search. Within that boundary, no new factual, sourcing, copyright, anatomy, route, or
related-link defect was found.

`npm run check` passed on 2026-07-23: queue/registry/content validation, prose lint, 2
pipeline tests, 38 runner tests, 145 application tests, TypeScript, production build,
and ESLint all completed successfully. Vitest emitted only the existing non-failing
jsdom `Window.scrollTo()` notices. The gate does not compare the registry's diagram
inventory with MDX component usage or detect SVG edge and label collisions.

### ADVISORY

1. The round 1 reception-causality advisory remains unresolved: “The book landed
   because it makes that mismatch visible” still attributes the book's reception to
   a cause not supported by the bounded repository evidence
   (`src/chapters/four-hour-workweek.mdx:21-27`). This remains non-blocking.
