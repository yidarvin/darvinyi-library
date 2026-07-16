verdict: approve

## Critique round 1 — 2026-07-15

### Required

1. **Complete the `emotional-intelligence` registry metadata required by the
   content contract.** The draft record contains display metadata and `draft`
   status, but it omits `tier`, `thesis`, `framework`, and the rendered diagram
   inventory (`content/registry.json:599-605`). Add the brief-supported tier 1,
   thesis, and EI-domains framework, then record the six rendered forms in order:
   iceberg, flow, process loop, comparison, node graph, and node graph. The
   validator currently permits the scaffold record while it remains a draft, but
   definition-of-done item 7 does not.

2. **Recompute the Hero reading-time badge from the rendered page.** The draft
   declares `minutes={7}` (`src/chapters/emotional-intelligence.mdx:8-12`), but a
   direct server render contains 1,465 reader-visible words, including the Hero,
   headings, prose, diagram labels, captions, exercise titles, component chrome,
   and Shelved Nearby content. At the authoring spec's roughly 200 words per minute,
   rounded up, that is an 8-minute distillation. Recompute after the other revision
   and set the final badge accordingly.

### Advisory

None.

### Evidence checked

- Re-derived the central claim and signature model from
  `prompts/notes/emotional-intelligence.md` and the matching seed record in
  `prompts/_books.py`. The thesis, five key ideas, and EI-domains Model remain
  within that bounded account, while the caveat correctly avoids presenting EI as
  a settled score that supersedes IQ.
- Inspected only the two evidence endpoints already recorded in the chapter; no new
  external web search was begun. The UNH record confirms the Mayer, Salovey, and
  Caruso article's identity and bibliographic details. PubMed's endpoint was
  bot-gated in this environment, so the review did not claim access to text it
  could not retrieve. The chapter's caveat stays appropriately bounded rather than
  generalizing the job-performance result to all emotional skills.
- Read the full chapter and every directly imported book, figure, exercise,
  callout, and diagram component, plus the shared SVG, cover, registry, route, and
  MDX-loading dependencies. All five key ideas have captioned registered-vocabulary
  diagrams, the Model renders all five domains, labels fit their SVG geometry, and
  the declared intrinsic widths remain readable through Figure's horizontal
  overflow at phone width.
- The prose is an original thematic synthesis within the available repository
  evidence. It contains no epigraph or real cover art, and no reproduced passage,
  close paraphrase, or traced author figure is evident. The four exercises are
  concrete, and the caveat honestly distinguishes Goleman's broad account from a
  narrower ability model.
- Confirmed all three related slugs resolve to `done` chapters, the prose explains
  the two closest relationships before the footer, and the outbound link targets
  the publisher's product page. `npm run check` completed successfully on
  2026-07-15 with `CHECK OK`, including validation, prose lint, pipeline tests, all
  64 Vitest tests, typecheck, production build, and ESLint. Vitest emitted only the
  existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-15

- Completed the `emotional-intelligence` registry record with the brief-supported
  tier 1, thesis, `The EI domains` framework, and the six rendered diagram forms in
  page order: iceberg, flow, process loop, comparison, node graph, and node graph.
- Recomputed the rendered reading-time badge from the recorded 1,465 reader-visible
  words at roughly 200 words per minute, rounded up, and changed the Hero from 7 to
  8 minutes.
- Preserved the existing chapter prose, diagrams, caveat, cross-links, and status as
  `draft`. `npm run check` passed on 2026-07-15 with `CHECK OK` (64 Vitest tests,
  typecheck, production build, and ESLint included); the existing non-failing jsdom
  `Window.scrollTo()` notices remained.

## Critique round 2 — 2026-07-15

### Required

None.

### Advisory

None.

### Evidence checked

- Re-verified both round 1 findings against the resolved draft. The registry now
  records tier 1, the brief-supported thesis and EI-domains framework, and all six
  rendered diagram forms in page order. The chapter now declares `minutes={8}`;
  because the reader-visible content did not otherwise change, this still matches
  the recorded 1,465-word render at roughly 200 words per minute, rounded up.
- Re-derived the central claim and five-domain model from the chapter brief and its
  matching seed record. Inspected only the evidence endpoints already recorded in
  the draft and round 1, without starting a new external search. The UNH repository
  confirms the cited Mayer, Salovey, and Caruso article and the publisher page
  confirms the book identity and its bounded claims about self-awareness,
  self-discipline, empathy, and learnable capacity. PubMed remained bot-gated. No
  new unsupported claim or copyright concern was identified from the available
  evidence.
- Re-read the full chapter and its imported callout, exercise, figure, Hero,
  Shelved Nearby, and five diagram primitives, including their shared SVG, cover,
  and registry dependencies. All five key ideas have captioned vocabulary diagrams;
  the Model contains all five domains; the SVG labels fit their geometry; and the
  declared intrinsic widths remain readable at phone width through Figure's
  horizontal overflow.
- Confirmed the anatomy and section order, the concrete four-card practice section,
  the honest measurement caveat, the generated typographic cover, the resolving
  related slugs, and the publisher outbound link. The synthesis remains original in
  wording and organization, with no epigraph, real cover art, close paraphrase, or
  traced book figure evident.
- `npm run check` completed successfully on 2026-07-15 with `CHECK OK`, including
  queue and registry validation, prose lint, pipeline tests, all 64 Vitest tests,
  typecheck, production build, and ESLint. Vitest emitted only the existing
  non-failing jsdom `Window.scrollTo()` notices.
