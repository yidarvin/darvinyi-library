verdict: revise

## Critique round 1 — 2026-07-28

### Required

1. **Compress “The thesis” to the required one or two sentences.** The fixed
   anatomy defines this section as the single compact paragraph a reader can carry
   away, limited to one or two sentences. The current section runs four sentences
   (`src/chapters/miracle-of-mindfulness.mdx:11-17`). Preserve its useful link
   between ordinary activity, gentle attention, and careful action with others,
   but make the section conform to the content contract.

2. **Do not present the shared-conditions synthesis as a book-specific key idea
   without book-specific support.** The fifth key idea says this is “the book’s
   larger ethical direction” and teaches that an ordinary act should be understood
   through its web of soil, weather, labor, transport, other people, materials,
   and place (`src/chapters/miracle-of-mindfulness.mdx:124-154`). The recorded
   book-specific sources support the book’s wartime social-work origin and its
   practices of breathing, walking, eating, communicating, and attention in
   ordinary life (`content/evidence/miracle-of-mindfulness.md:7-8`). The evidence
   record explicitly derives the relational, shared-conditions diagram from the
   lineage’s separate *Fourteen Mindfulness Trainings*, while the general
   “Key Teachings” source supports engaged ethics (`content/evidence/miracle-of-mindfulness.md:10-11`).
   Those sources establish a broader lineage context, not that this particular
   book makes the specific interbeing argument rendered as one of its five core
   ideas. Either ground the idea in recorded evidence specific to the book, replace
   it with a major idea that the bounded book evidence supports, or clearly frame
   it as a later contextual extension rather than attributing it to the book.

### Advisory

1. Apart from the required findings, the page follows the fixed anatomy. The brief
   and registry both support omitting the Model section; the other four key ideas
   stay within the bounded evidence about ordinary activity, breath, body, and
   returning attention; and all five figures use matching shared-vocabulary
   primitives with chapter-local minimum widths that preserve their authored label
   sizes in the `Figure` scroller at phone width.

2. The four practice cards specify observable actions, and the caveat keeps
   mindfulness distinct from protection, treatment, material support, and
   collective action without making a clinical efficacy claim. All three related
   slugs resolve to completed chapters, their relationships are stated in prose,
   and the outbound Beacon Press link matches the recorded publisher source.

3. Within the supplied brief and evidence, no quotation, real cover art, apparent
   close paraphrase, or apparent reproduction of a source figure was found. A
   direct static render contains approximately 1,483 reader-visible words,
   consistent with the eight-minute Hero badge at approximately 200 words per
   minute rounded up. This review began no new external web search.

4. `npm run check` completed with `CHECK OK` on 2026-07-28: queue, registry,
   critique, and content validation; prose lint; all 42 pipeline and runner tests;
   all 297 Vitest tests; TypeScript and the Vite production build; and ESLint
   passed. Vitest emitted only the existing non-failing jsdom
   `Window.scrollTo()` notices.
