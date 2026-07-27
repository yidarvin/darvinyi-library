verdict: resolved

## Critique round 1 — 2026-07-26

### Required

1. **Make Figure 95.2 encode the containment relation stated by its prose and
   caption.** The section defines awareness as “the capacity in which” several
   changing states can be noticed, and the caption calls it the steady field in
   which thoughts, feelings, and events come and go
   (`src/chapters/untethered-soul.mdx:56-67`). The figure instead supplies
   `awareness` as ring 0, followed by thoughts and feelings, then events and other
   people (`src/chapters/untethered-soul.mdx:68-76`). The imported `Concentric`
   component explicitly treats index 0 as the innermost core and later entries as
   enclosing layers (`src/components/diagrams/Concentric.tsx:8-20,48-78`), so the
   rendered geometry places awareness inside the passing states rather than
   showing those states within awareness. Recompose the figure with a vocabulary
   form and labels that actually show the stated relationship, or revise the
   neighboring claim and caption to the center-and-layers relation the current
   geometry depicts.

2. **Recompute the Hero reading-time badge from the final rendered page.** A direct
   static render of this draft through the repository's MDX provider and exact
   chapter components contains approximately 1,388 reader-visible alphanumeric
   word tokens, including the generated cover and Hero metadata, headings,
   captions, diagram labels, exercise titles, prose, and nearby-book footer. At the
   authoring spec's approximately 200 words per minute, rounded up, this is a
   seven-minute distillation, not `minutes={6}`
   (`src/chapters/untethered-soul.mdx:5-9`). Recompute after the other revision and
   set the badge from the final rendered count.

3. **Support or narrow the attributed stored-emotion mechanism.** The third key
   idea says that Singer describes a present contraction as old emotional material
   held inside until life touches it, then builds the section and iceberg around
   that mechanism (`src/chapters/untethered-soul.mdx:79-99`). The bounded evidence
   record supports the broader themes of thoughts and emotions, inner resistance,
   changing circumstances, and letting go, but it does not record this more
   specific stored-material account (`content/evidence/untethered-soul.md:7-9`).
   Because the attribution supplies the causal interpretation for an entire key
   idea, record source support specific enough to re-derive it, or narrow the prose
   and diagram to the more modest trigger-and-old-story observation already
   presented as the page's synthesis.

### Advisory

1. The publisher evidence and outbound label use `Michael A. Singer`, while the
   registry-generated Hero byline and chapter brief use `Michael Singer`
   (`content/evidence/untethered-soul.md:7-9`;
   `content/registry.json:1877-1885`; `prompts/notes/untethered-soul.md:1-4`).
   The shortened name still identifies the author, so this does not block approval,
   but matching the published author name would make the metadata and reader link
   consistent.

2. Apart from the required findings, the fixed anatomy is intact. Five key ideas
   each have a captioned shared-vocabulary diagram; omitting the Model section
   matches both the brief and registry; the four exercises specify observable
   actions; and the caveat clearly separates spiritual practice from clinical
   explanation and rejects using openness to remain in danger. Both nearby slugs
   resolve to done chapters, their relationships are stated in prose, and the
   outbound link matches the recorded publisher page. The explicit diagram minimum
   widths preserve authored label sizes inside `Figure`'s phone-width horizontal
   scroller.

3. Within the bounded brief and recorded evidence, the remaining synthesis uses
   original thematic organization, prose, and shared SVG primitives. No quotation,
   real cover art, apparent close paraphrase, or apparent reproduction of a source
   figure was found. This review began no external web search.

4. `npm run check` completed with `CHECK OK` on 2026-07-26. Queue, registry,
   critique, and content validation; prose lint; all 40 pipeline and runner tests;
   all 197 Vitest tests; TypeScript and the Vite production build; and ESLint
   passed. Vitest emitted only the existing non-failing jsdom
   `Window.scrollTo()` notices.

## Builder resolution — 2026-07-26

- **Required 1:** Replaced Figure 95.2's core-first `Concentric` rings with the
  existing `CoreContext` vocabulary form. Its outer field is explicitly labeled
  “the field of awareness,” and its contained passing-state cards are thoughts,
  feelings, and events. The revised caption now describes that containment
  relation directly.
- **Required 2:** Re-rendered the final MDX page and counted 1,400
  reader-visible alphanumeric tokens, including Hero and cover metadata,
  headings, captions, diagram labels, exercise titles, and the nearby-book footer.
  At approximately 200 words per minute, rounded up, that is seven minutes; the
  Hero badge is now `minutes={7}`.
- **Required 3:** Narrowed Figure 95.3 and its section from an attributed
  stored-emotion mechanism to the page-level observation that a current trigger can
  recruit memory, expectation, or a familiar conclusion. The prose now explicitly
  says that this does not establish a hidden mechanism or explain the cause of a
  feeling, and the iceberg labels no longer assert stored emotional material.
