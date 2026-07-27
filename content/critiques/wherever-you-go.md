verdict: resolved

## Critique round 1 — 2026-07-26

### Required

1. **Make Figure 96.2 encode the body-anchor relation stated by its prose and
   caption.** The section describes bodily sensation as a concrete anchor that
   draws attention away from abstract commentary, and the caption specifically
   says attention moves from an “outer rush of thought” toward immediate
   sensation (`src/chapters/wherever-you-go.mdx:50-62`). The figure supplies no
   thought or commentary label. Instead, it nests “felt sensation” inside “breath
   and posture,” then nests both inside “sounds and surroundings”
   (`src/chapters/wherever-you-go.mdx:63-67`). The imported `Concentric`
   component defines index 0 as the innermost core and every later entry as an
   enclosing layer (`src/components/diagrams/Concentric.tsx:8-20,48-78`), so the
   rendered geometry also treats examples of felt sensation as containers around
   the broader category. Recompose the figure with an in-vocabulary form and
   labels that visibly show attention landing on a bodily anchor, or revise the
   neighboring prose and caption to the actual center-and-layers relationship the
   current geometry depicts.

2. **Replace Figure 96.3's unsupported hidden-driver model with the stated
   event-to-choice distinction.** The key idea says thoughts and feelings can be
   noticed without becoming commands, and its second paragraph separates seeing a
   reaction from deciding on a response
   (`src/chapters/wherever-you-go.mdx:70-80`). The `Iceberg` primitive is
   explicitly a surface-versus-underlying-drivers form
   (`src/components/diagrams/Iceberg.tsx:4-16,36-60`), and this usage places body
   sensation, memory, and prediction beneath a visible reaction
   (`src/chapters/wherever-you-go.mdx:82-89`). That geometry asserts a hidden
   causal account not established by the neighboring prose, chapter brief, or
   bounded evidence, while omitting the actual instructional relation between an
   event, awareness, choice, and response. Give this major idea a structural
   diagram that teaches the claimed interruption of automatic action without
   inventing an underlying mechanism.

3. **Support or narrow the clinical safety claim in the caveat.** The callout says
   that paying attention can initially make grief, trauma responses, and physical
   pain more noticeable, then directs an overwhelmed, disconnected, or unsafe
   reader toward clinical or emergency support
   (`src/chapters/wherever-you-go.mdx:173-181`). The recorded evidence supports
   present-focused, nonjudgmental practice, bodily and breath anchors, returning
   after attention wanders, and brief formal and informal exercises
   (`content/evidence/wherever-you-go.md:7-11`); it records no source for the
   more specific adverse-experience claim. Because this is consequential
   health-related guidance, record evidence specific enough to re-derive it or
   narrow the callout to the non-clinical limits already supportable from the
   chapter and brief.

### Advisory

1. Figure 96.5 uses a quantitative `Spectrum`, including an unexplained marker at
   `0.68`, for formal sitting and daily activity, which the prose treats as two
   contexts for the same practice rather than poles of a measurable degree
   (`src/chapters/wherever-you-go.mdx:118-143`;
   `src/components/diagrams/Spectrum.tsx:14-30,90-124`). The caption and zone
   labels make the intended continuity recoverable, so this does not independently
   block approval, but a neutral context range or transfer structure would avoid
   implying that walking, eating, and listening occupy a precise position on an
   undefined scale.

2. Apart from the required findings, the fixed anatomy is intact. Five key ideas
   each have a captioned shared-vocabulary figure; omitting the Model section
   matches the brief and registry; the four exercises specify observable actions;
   and all three nearby slugs resolve to done chapters with their relationships
   stated in prose. The outbound publisher link matches the recorded evidence.
   A direct render contains 1,372 reader-visible alphanumeric tokens, consistent
   with the seven-minute Hero badge at approximately 200 words per minute rounded
   up.

3. Within the bounded brief and recorded evidence, the remaining synthesis uses
   original thematic organization, prose, and shared SVG primitives. No quotation,
   real cover art, apparent close paraphrase, or apparent reproduction of a source
   figure was found. This review began no external web search.

4. `npm run check` completed with `CHECK OK` on 2026-07-26. Queue, registry,
   critique, and content validation; prose lint; all 40 pipeline and runner tests;
   all 199 Vitest tests; TypeScript and the Vite production build; and ESLint
   passed. Vitest emitted only the existing non-failing jsdom
   `Window.scrollTo()` notices.

## Builder resolution — 2026-07-26

- Replaced Figure 96.2's concentric layers with a `Flow` from thought commentary,
  through a highlighted body anchor, to immediate sensation. The diagram now shows
  the attention shift described by the neighboring prose and caption.
- Replaced Figure 96.3's iceberg with a four-step `Flow`: a thought or feeling
  appears, it is noticed, a response is chosen, then the person acts. This teaches
  the stated interruption of automatic action without claiming hidden drivers.
- Narrowed the caveat to the non-clinical practice supported by the recorded
  evidence: notice a body or breath anchor, recognize wandering attention, and
  return. Removed the unsupported adverse-experience and emergency-support claims.
- Also replaced Figure 96.5's quantified spectrum with a neutral `NodeGraph` that
  connects formal sitting, walking, eating, and listening to the shared practice of
  returning attention.
- Preserved the five key ideas, fixed page anatomy, exercises, cross-links, and
  existing evidence. `npm run check` passed before this resolution was appended.

## Critique round 2 — 2026-07-26

### Required

1. **Synchronize the registry's diagram inventory with the resolved chapter.**
   The chapter now imports and renders a process loop, two flows, a comparison,
   and a node graph (`src/chapters/wherever-you-go.mdx:1-3,41-48,62-68,82-88,102-115,129-147`).
   The registry still records the pre-resolution sequence of process loop,
   concentric circles, iceberg, comparison, and spectrum
   (`content/registry.json:1906-1912`). This leaves three of five key-idea
   diagrams falsely described and violates the authoring spec's requirement for
   complete registry metadata. Update the five entries to match the figures
   actually on the page. The repository validator does not compare these names
   with MDX usage, so its passing result does not resolve the mismatch.

### Advisory

1. The three required findings from round 1 are resolved as recorded: Figures
   96.2 and 96.3 now encode the stated relations, the caveat stays within the
   non-clinical limits supported by the recorded evidence, and Figure 96.5 now
   uses a neutral relationship map. No settled finding is reopened.

2. `npm run check` completed with `CHECK OK` on 2026-07-26. Validation and prose
   lint passed; all 40 pipeline and runner tests and all 199 Vitest tests passed;
   TypeScript, the Vite production build, and ESLint passed. Vitest emitted only
   the existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-27

- Updated the `wherever-you-go` registry inventory to match the five rendered key-idea
  figures exactly: process loop, flow, flow, comparison, and node graph. This replaces
  the obsolete concentric circles, iceberg, and spectrum entries while preserving the
  previously resolved chapter diagrams and caveat.
- `npm run check` passed after the metadata correction.
