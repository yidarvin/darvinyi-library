verdict: revise

## Critique round 1 — 2026-07-15

### Required

1. **Complete the `influence` registry record required by the content contract.** The
   record contains the display title, author/year subtitle, shelf, routes, and draft
   status, but it omits `tier`, `thesis`, `framework`, and the diagram-form inventory
   required by definition-of-done item 7. The brief and seed metadata supply tier 1,
   the compliance-trigger thesis, and the Six Principles of Persuasion framework; the
   chapter uses iceberg, flow, process loop, Venn, comparison, spectrum, and node graph
   forms. Add those values without changing unrelated registry entries.

2. **Make Figure 10.1's waterline label legible at a 360 px viewport.** The imported
   `Iceberg` has a 380-unit viewBox and renders the meaning-bearing waterline label at
   9.5 units. This chapter preserves only a 380 px minimum width, so “what the request
   makes salient” remains 9.5 CSS px inside the shared horizontal-overflow wrapper,
   below the approximately 11 px phone floor established by completed chapters. Give
   this figure a chapter-local minimum rendered width of roughly 440 px, or provide an
   equally legible compact presentation. Do not change the shared `Iceberg` or `Figure`
   component for this finding.

### Advisory

1. The bounded factual and copyright posture is otherwise sound. The brief and seed
   metadata support the compliance-trigger thesis and the six-principle signature
   model. The six principles named in the chapter agree with that recorded framework,
   and the page carefully treats them as context-dependent tendencies rather than
   guaranteed controls. It uses no quotation or real cover art, follows a thematic
   organization, and composes original labels through shared diagram primitives. The
   repository contains no chapter-specific source excerpts or separate evidence record
   for closer attribution or close-paraphrase comparison, and this review began no
   external web search.

2. The Hero and first key idea call all of the cues “learned shortcuts” or “learned
   social rules,” while the recorded brief describes the broader category as deep
   psychological triggers. A future precision pass could use the broader “decision
   shortcuts” or “psychological cues” throughout, since liking and scarcity are not
   clearly explained here as learned social rules. The six-part framework itself is
   still represented accurately, so this does not block approval.

3. Apart from Figure 10.1 and the registry omissions, the anatomy and visual mapping
   are sound. Six key ideas each have a captioned vocabulary diagram; the Model section
   renders all six principles as distinct cues rather than a false sequence; the four
   exercises are concrete; the caveat distinguishes tendencies from guarantees and
   notes the later addition of unity; both related slugs are complete and their
   relationships are stated in prose; and the outbound link is a direct publisher page.
   The remaining SVG minimum widths keep their meaning-bearing labels at approximately
   11 CSS px or larger on a 360 px viewport.

4. `npm run check` passed on 2026-07-15: queue/registry/content validation, prose lint,
   pipeline tests, 24 Vitest tests, TypeScript and Vite production build, and ESLint all
   completed successfully. The jsdom run emitted only the existing non-failing
   `Window.scrollTo()` notices.
