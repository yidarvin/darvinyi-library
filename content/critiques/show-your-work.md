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

## Critique round 2 — 2026-07-28

### Required

1. **Give the Key Ideas an original organizing logic instead of retaining the source
   book's progression.** The recorded evidence at
   `content/evidence/show-your-work.md:6-10` identifies Kleon's sequence of concerns
   as process, small pieces, stories, teaching, avoiding spam, criticism, selling, and
   persistence. The draft at `src/chapters/show-your-work.mdx:29-158` selects from
   that sequence but keeps the selected ideas in the same order: process, small
   pieces and cadence, public interests, teaching, non-spammy contribution, then
   persistence. Renaming the headings and omitting several source topics does not
   supply the thematic reorganization required by the copyright line in
   `docs/authoring-spec.md`, which explicitly says not to mirror the book's chapter
   order. Recompose or reorder the six ideas under a clear original progression so
   the page reads as synthesis rather than a selected walk through the source's
   table of contents.

### Advisory

None.

The two findings from round 1 remain resolved. “The thesis” is two sentences, Figure
143.3's `refine` label fits the available clearance, and the four nearby-book
relationships are mapped individually. The brief and recorded evidence otherwise
support the draft's process-sharing, generosity, attribution, persistence, and
privacy-boundary claims. Six key ideas retain captioned shared-vocabulary diagrams;
the deliberate absence of a Model section is recorded in the brief and registry; all
four related slugs are done; and the publisher link agrees with the evidence record.
No new external web search was begun.

`npm run check` completed with `CHECK OK` on 2026-07-28: validation, prose lint, all
42 pipeline and runner tests, all 308 Vitest tests, TypeScript, the Vite production
build, and ESLint passed. Vitest emitted only the existing non-failing jsdom
`Window.scrollTo()` notices.

## Builder resolution — 2026-07-28

Resolved the required finding from critique round 2:

1. Reordered the six Key Ideas into an original reader-centered progression: make the
   practice recognizable, reveal selected working evidence, teach a bounded lesson,
   contribute without extracting attention, establish a sustainable rhythm, and stay
   with the conversation. Added a one-sentence signpost before the ideas that states
   this organizing logic. The source-concern sequence is no longer retained, while all
   six original diagrams, captions, and the round 1 `refine` label fix remain intact.

The two round 1 fixes remain preserved: **The thesis** is two sentences, and the
nearby-shelf sentence maps each linked book to its relationship. No new external research
was used. On 2026-07-28, `npm run check` cleared validation and prose lint before this
environment's foreground runner stopped it during the unchanged repository test stage;
`npm run build` and `npm run lint` then passed separately.
