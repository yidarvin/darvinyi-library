verdict: revise

## Critique round 1 — 2026-07-28

### Required

1. **Correct the Hero reading-time badge from the rendered page.** A direct server
   render of this exact MDX through its real shared components contains approximately
   1,395 reader-visible alphanumeric word tokens, including the Hero, headings,
   captions, diagram labels, exercise titles, callout, and generated component text.
   At the authoring spec's approximately 200 words per minute, rounded up, this is a
   seven-minute distillation, not `minutes={8}` at
   `src/chapters/mind-for-numbers.mdx:11`. Recompute after the other revisions and set
   the final badge from that count.

2. **Preserve the Model Flow's label sizes at a 360px viewport.** Figure 141.6 puts
   both primitives inside a `min-w-[440px]` wrapper
   (`src/chapters/mind-for-numbers.mdx:149-168`). The four-step `Flow` has a
   558-unit-wide viewBox by its width calculation
   (`src/components/diagrams/Flow.tsx:21-33`), so constraining it to 440px reduces
   its 11.5-unit step labels to about 9.1 CSS pixels and its 9-unit sequence numbers
   to about 7.1 pixels. The surrounding `Figure` can scroll, but only at that
   undersized width. Give the composition at least the Flow's native 558px minimum
   width, or provide an equally legible in-vocabulary composition.

3. **Make Figure 141.3's directed relations encode the chunk described in the
   prose.** The paragraph and caption define a chunk as a structure joining a cue,
   linked procedure, meaning, and checking
   (`src/chapters/mind-for-numbers.mdx:64-73`). The `NodeGraph` keeps its default
   `directed={true}` and instead renders a causal cycle
   (`src/chapters/mind-for-numbers.mdx:74-90`). Most clearly, the arrow from “why it
   works” to “answer check” labeled “tests” states that the explanation tests the
   check, the reverse of the intelligible relation. The accented return from “answer
   check” to “problem cue” also asserts a reinforcing feedback loop that the prose
   does not teach. Recompose this as a neutral relationship map or correct the
   directions and labels so the required key-idea diagram matches its explanation.

4. **Support or narrow the chunk-formation account within the recorded evidence.**
   “Build chunks that can travel” and exercise 03 attribute a specific learning
   structure and recipe to the book: combine several moves into a reusable pattern,
   follow a worked example, reproduce it without looking, vary a nearby problem, and
   connect the procedure to a cue and purpose
   (`src/chapters/mind-for-numbers.mdx:64-71,186-190`). The chapter brief records
   focused versus diffuse thinking, while the evidence file directly records
   incubation, retrieval, spacing, and interleaving. It does not record support for
   chunking or this formation recipe. Because this is one of only five major ideas,
   add book-specific support to the bounded record or narrow/replace the section with
   a claim that can be re-derived from the existing brief and evidence.

5. **Complete the draft registry record before approval.** The
   `mind-for-numbers` entry contains only scaffold metadata and `status: "draft"`
   (`content/registry.json:2781-2789`). It omits the authoring spec's required
   `tier`, `thesis`, `framework`, and `diagrams` fields. Record tier 3, a
   brief-consistent thesis, focused versus diffuse thinking as the signature
   framework, and the six rendered diagram forms in page order after the diagram
   revisions. `npm run check` does not currently enforce those metadata fields, so
   its passing result does not satisfy definition-of-done item 7.

### Advisory

1. Apart from the required findings, the fixed anatomy is intact. Five key ideas
   each have a captioned shared-vocabulary figure, the signature Model is present,
   the four practice cards specify observable actions, the caveat avoids treating
   focused and diffuse thinking as discrete neural switches, and all three nearby
   slugs resolve to chapters with `done` status.

2. The bounded evidence supports the chapter's restrained claims about incubation,
   retrieval, spacing, and interleaving, including the caveat that their effects
   depend on task and timing. No quotation, apparent close paraphrase, reproduced
   source figure, real cover art, or new external web search was found.

3. `npm run check` completed with `CHECK OK` on 2026-07-28. Queue, registry,
   critique, and content validation; prose lint; all 42 pipeline and runner tests;
   all 303 Vitest tests; TypeScript and the Vite production build; and ESLint
   passed. Vitest emitted only the existing non-failing jsdom
   `Window.scrollTo()` notices.
