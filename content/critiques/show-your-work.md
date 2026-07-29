verdict: resolved

## Critique round 1 — 2026-07-28

### Required

1. **Compress “The thesis” to the required one or two sentences.** The section at
   `src/chapters/show-your-work.mdx:16-21` contains four sentences. The authoring spec
   defines this paragraph as the one- or two-sentence compression a reader can carry
   away. Preserve the useful core claim about selected process traces becoming a
   findable archive, but move implementation detail into the later sections so the
   fixed anatomy is respected.

2. **Make Figure 143.3's feedback label fully legible.** The chapter places “questions
   you keep” and “experiments you make” at the same height, leaving approximately 112
   viewBox units between their 94-unit node cards, while the 17-character
   `sharper attention` label at `src/chapters/show-your-work.mdx:98` is rendered by
   `NodeGraph` as centered 12-unit monospace text. The label is wider than that gap.
   Because `NodeGraph` paints edge labels before it paints node cards
   (`src/components/diagrams/NodeGraph.tsx:75-135`), the two cards obscure the label's
   ends. Shorten or reposition the chapter-local label, or recompose the node
   positions, so the feedback relationship reads intact at the component's rendered
   sizes.

### Advisory

1. **Clarify the nearby-book relationship mapping.** The sentence at
   `src/chapters/show-your-work.mdx:211-212` gives three thematic relationships for
   four linked covers, so it is not clear which phrase describes which title. The
   links themselves resolve, so this does not block the draft, but a direct mapping
   would better satisfy the cross-link guidance.

The bounded review found no other defect worth requesting. The brief and recorded
evidence support the chapter's selective process-sharing, useful teaching, attribution,
persistence, and privacy-boundary arc. The caveat properly avoids treating visibility as
a guarantee of discovery or income. No apparent close paraphrase, reproduced source
figure, quotation, real cover art, or unsupported factual claim that changes the
reader's understanding was found. The deliberate absence of a Model section is recorded
in both the brief and registry. Six key ideas each have a captioned shared-vocabulary
diagram, the four exercises are concrete, the registry's diagram inventory matches the
page, all four related slugs are done, and the publisher link matches the evidence
record. No new external web search was begun.

`npm run check` completed with `CHECK OK` on 2026-07-28: validation, prose lint, all
42 pipeline and runner tests, all 308 Vitest tests, TypeScript, the Vite production
build, and ESLint passed. Vitest emitted only the existing non-failing jsdom
`Window.scrollTo()` notices.

## Builder resolution — 2026-07-28

Resolved every required finding from critique round 1:

1. Compressed **The thesis** to two sentences. It now carries only the core claim that
   selected, useful process traces make work findable and accumulate into an archive for
   people who share the problem; the operational detail remains in the later sections.
2. Replaced Figure 143.3's reinforcing-edge label, `sharper attention`, with the short
   label `refine`. The feedback relationship remains intact and the label now fits in the
   available clearance between the cards at the primitive's rendered sizes.

Also addressed the advisory cross-link note: the nearby-shelf sentence now maps each of the
four linked books to its specific relationship. Existing privacy, attribution, persistence,
and discoverability caveats and their supporting evidence were preserved. `npm run check`
passes on 2026-07-28.
