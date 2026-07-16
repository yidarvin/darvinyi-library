verdict: approve

## Critique round 1 — 2026-07-16

### Required

1. **Recompute the Hero reading-time badge from the rendered page.** The draft
   declares `minutes={6}` (`src/chapters/selfish-gene.mdx:5-9`), but a direct MDX
   render contains 1,410 reader-visible words, including the Hero, headings,
   captions, exercise titles, diagram labels, and nearby-book footer. At the
   authoring spec's approximately 200 words per minute, rounded up, this is an
   eight-minute distillation. Recompute after the other revisions and set the final
   badge from that rendered count.

2. **Replace Figure 35.3 with a structural account of kin selection.** The prose
   correctly describes a cost to the actor being weighed against benefits to
   related recipients (`src/chapters/selfish-gene.mdx:75-82`), but the Venn at
   lines 84-93 turns “copies affected through the actor” and “copies affected
   through relatives” into overlapping sets whose intersection is “shared
   inherited variants.” Copies in different bodies are distinct copies, and
   relatedness weights the recipient effect rather than making those affected-copy
   sets literally intersect. The current form also omits the cost-versus-weighted-
   benefit relationship that makes the behavior selectable. Use an in-vocabulary
   composition whose visible labels and generated description encode the actor's
   cost, the related recipients' benefit, and the condition under which the latter
   can outweigh the former. Do not reproduce a source figure.

3. **Make Figure 35.6 trace differential copying rather than assert unconditional
   reinforcing causation.** The Model prose calls the gene's-eye view a tracing
   method and asks whether a variant's effects alter later copy count
   (`src/chapters/selfish-gene.mdx:142-149`). The NodeGraph instead marks
   `variant → development`, `body → copies`, and `copies → variant` as
   `kind="reinforcing"` (`src/chapters/selfish-gene.mdx:162-168`), so the shared
   component draws accent plus signs that mean positive reinforcement. A variant's
   developmental effects can increase or decrease its representation relative to
   alternatives, and later copies are instances of the variant, not a positive
   causal input into an earlier one. Recompose or relabel the chapter-local graph
   so the signature model visibly preserves the brief's direction: variant,
   effects through bodies and environments, and differential copies in a later
   generation.

4. **Preserve Figure 35.6's cultural-flow label sizes at a 360 px viewport.** The
   four-step `Flow` has a 558-unit viewBox, but it is rendered as `w-full` inside
   only a `min-w-[440px]` wrapper (`src/chapters/selfish-gene.mdx:151-175`). At the
   wrapper's phone width, the component's 11.5-unit step labels shrink to about
   9.1 CSS px and its 9-unit sequence numbers to about 7.1 px. Figure's horizontal
   overflow cannot prevent that internal scale-down. Give this chapter-local
   composition enough minimum rendered width, or use a compact in-vocabulary
   layout, so meaning-bearing text remains legible without changing shared
   components.

### Advisory

1. Within the repository's bounded evidence, the central thesis and copyright
   posture are sound. The chapter brief and registry support the gene's-eye view
   and the meme as a qualified cultural parallel. The draft uses original thematic
   organization, no quotation or real cover art, and shared diagram primitives
   rather than a traced source figure. The recorded Nature page confirms the 1973
   Maynard Smith and Price conflict-strategy citation. PubMed and OUP presented bot
   checks in this environment, so their recorded URLs could not be fully inspected;
   this review began no new external web search.

2. Exercise 02 applies the indirect-effects lens to help at work, at home, or in a
   group (`src/chapters/selfish-gene.mdx:187-190`). Its systems-level exercise is
   useful, but one short qualification could prevent readers from mistaking a map
   of recurring social consequences for a claim that ordinary workplace help is an
   instance of genetic kin selection.

3. Apart from the required figure findings, the anatomy and wiring are strong. Five
   key ideas each have a captioned vocabulary figure; the Model includes both parts
   named in the brief; four practice cards specify observable actions; the caveat
   rejects genetic intention, total genetic explanation, and a literal gene-like
   unit for culture; both nearby slugs resolve to `done` chapters; and the OUP link
   points to the publisher's book page. The registry metadata and rendered diagram
   inventory agree with the draft.

4. `npm run check` completed with `CHECK OK` on 2026-07-16: queue, registry,
   critique, and content validation; prose lint; both pipeline tests; all 74 Vitest
   tests; TypeScript and Vite production build; and ESLint passed. Vitest emitted
   only the existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-16

- Recomputed the final rendered-page reading estimate after the figure revisions:
  1,428 reader-visible words, including headings, figure labels, captions, Hero,
  exercises, and nearby-book footer. The Hero now declares `minutes={8}` at roughly
  200 words per minute, rounded up.
- Replaced Figure 35.3's Venn with a comparison of the actor's cost `C` and related
  recipients' benefit `B`, weighted by relatedness `r`. Its visible labels,
  caption, and accessible description now state the selection condition `rB > C`;
  the registry records the revised comparison form.
- Rebuilt Figure 35.6's gene-centered graph as a one-way trace from a gene variant
  through development, body and behavior, and into differential copies in a later
  generation. The graph has no reinforcing markers or return edge, and its
  accessible description states the directional account.
- Gave Figure 35.6's cultural Flow a chapter-local `min-w-[558px]`, equal to its
  558-unit viewBox, inside Figure's horizontal-overflow wrapper. Its authored step
  and sequence-label sizes therefore do not scale down at a 360 px viewport. The
  cultural endpoint now reads `differential copying` rather than implying an
  unconditional increase.

## Critique round 2 — 2026-07-16

### Required

None.

### Advisory

1. All four round-one required findings are resolved in the current draft. The Hero
   now reports eight minutes; Figure 35.3 visibly and accessibly compares `C` with
   `rB` and states `rB > C`; Figure 35.6 traces the gene-centered model forward to
   differential later copies without reinforcing markers or a return edge; and its
   cultural Flow preserves the authored 558 px width inside Figure's horizontal
   overflow at a phone viewport.

2. The chapter remains faithful to the local brief and bounded recorded evidence.
   Its wording and thematic organization are original, its diagrams use the shared
   vocabulary rather than source figures, and its qualifications distinguish
   differential copying from intention, kin selection from conscious calculation,
   and the meme analogy from a settled gene-like unit of culture. No new external
   web search was begun for this review.

3. `npm run check` completed with `CHECK OK` on 2026-07-16: queue, registry,
   critique, and content validation; prose lint; both pipeline tests; all 74 Vitest
   tests; TypeScript and Vite production build; and ESLint passed. Vitest emitted
   only the existing non-failing jsdom `Window.scrollTo()` notices.
