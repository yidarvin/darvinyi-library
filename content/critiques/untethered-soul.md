verdict: approve

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

## Critique round 2 — 2026-07-26

### Required

1. **Synchronize the registry's diagram inventory with the revised Figure 95.2.**
   The builder resolved round 1 by replacing `Concentric` with `CoreContext`
   (`src/chapters/untethered-soul.mdx:3,67-75`), but the registry still records
   `"concentric circles"` as the chapter's second diagram
   (`content/registry.json:1888-1894`). The authoring spec requires a complete
   registry entry, and the critique rubric requires registry and rendered content
   to agree. Record the actual `core / context` form so the inventory describes the
   page that ships.

### Advisory

1. The three round 1 required content findings are resolved in the draft. Figure
   95.2 now visibly contains the passing-state cards within the labeled field of
   awareness; the Hero uses the recorded seven-minute reading time; and the third
   key idea now presents a modest trigger-and-old-story observation while expressly
   declining to claim a hidden stored-emotion mechanism.

2. The rest of the prior review remains settled. The fixed anatomy, five diagrammed
   key ideas, concrete practices, safety caveat, completed related-book links, and
   recorded publisher link remain intact. Within the bounded brief and evidence,
   no new unsupported consequential claim, close paraphrase, source-figure
   reproduction, or cover-art issue was found. This review began no external web
   search.

3. `npm run check` completed with `CHECK OK` on 2026-07-26. Validation, prose lint,
   both pipeline tests, all 40 runner tests, all 197 Vitest tests, TypeScript, the
   production build, and ESLint passed. Vitest emitted only the existing
   non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-26

- **Required 1:** Updated the `untethered-soul` registry diagram inventory so its
  second entry is `core / context`, matching Figure 95.2's imported
  `CoreContext` component and the named form in the diagram vocabulary. The other
  four recorded forms and all prior chapter fixes are unchanged.
- Re-ran `npm run check` after the registry edit. It completed with `CHECK OK`.

## Critique round 3 — 2026-07-26

### Required

None.

### Advisory

1. The round 2 registry mismatch is resolved. The inventory now records
   `core / context`, matching the `CoreContext` import and Figure 95.2
   (`content/registry.json:1887-1893`;
   `src/chapters/untethered-soul.mdx:3,67-75`). All three round 1 content
   findings also remain resolved.

2. The completed draft satisfies the fixed anatomy and the chapter brief: five
   key ideas each have a captioned shared-vocabulary figure, the absent Model
   section is deliberate and recorded, the practices are concrete, and the
   caveat prevents witness awareness and letting go from being presented as
   clinical explanations or substitutes for protection and care. Both nearby
   slugs resolve to done chapters, and the outbound publisher link matches the
   recorded evidence.

3. Re-derivation remained bounded to the brief and recorded evidence. Those
   sources support the chapter's central themes of mental commentary, witness
   consciousness, thoughts and emotions, inner resistance, letting go, and
   present-moment awareness. The revised trigger section is explicitly framed as
   a modest observation rather than an attributed stored-emotion mechanism. No
   unsupported consequential claim, quotation, apparent close paraphrase,
   source-figure reproduction, or real cover art remains. This review began no
   external web search.

4. `npm run check` completed with `CHECK OK` on 2026-07-26. Validation and prose
   lint passed; both pipeline tests, all 40 runner tests, and all 197 Vitest tests
   passed; TypeScript, the Vite production build, and ESLint passed. Vitest
   emitted only the existing non-failing jsdom `Window.scrollTo()` notices.

5. The shortened registry author name, `Michael Singer`, remains slightly less
   precise than the publisher's `Michael A. Singer`, but it unambiguously
   identifies the author and does not affect the distillation's accuracy.
