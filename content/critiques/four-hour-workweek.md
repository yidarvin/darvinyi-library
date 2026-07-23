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
