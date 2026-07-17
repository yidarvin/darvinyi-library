verdict: revise

## Critique round 1 — 2026-07-17

### REQUIRED

1. **Compress The thesis to the required one or two sentences.** The fixed anatomy
   defines this block as the single compact argument a reader can carry away, but the
   draft uses five sentences (`src/chapters/hard-thing.mdx:14-20`). The paragraph is
   directionally consistent with the brief, yet it expands into a description of the
   decision terrain and an operating stance instead of meeting the specified thesis
   form. Preserve the claim that hard calls have no painless formula and demand clear
   facts, timely judgment, and humane execution, in no more than two sentences.

2. **Remove the unsupported positive polarity from Figure 66.5's feedback path.**
   `NodeGraph` defines a `reinforcing` edge as an accent edge labeled with a plus sign
   (`src/components/diagrams/NodeGraph.tsx:16-19,83-107`). The draft assigns that
   meaning to both `customer evidence -> revised plan` and `revised plan -> explicit
   problem` (`src/chapters/hard-thing.mdx:151-170`). The prose says evidence can
   change a plan and that a revised plan closes the communication loop; it does not
   say that evidence increases the plan or that a plan amplifies the problem. The two
   plus signs therefore encode causal claims the section neither states nor supports.
   Use neutral, visibly directed connections, or short edge labels that name what
   travels along them, so the graph represents revision and feedback without false
   system polarity.

3. **Correct the Hero reading-time badge from the direct render.** A direct static
   render of this exact draft contains 1,623 reader-visible alphanumeric word tokens,
   including the Hero, headings, captions, SVG labels, exercise titles, callout, and
   nearby-book footer. At approximately 200 words per minute, rounded up, that is a
   nine-minute distillation, not `minutes={10}`
   (`src/chapters/hard-thing.mdx:8-12`). Recount after the required content edits and
   set the final badge from that render.

4. **Complete the registry record before approval.** The `hard-thing` entry contains
   identity, shelf, route, and draft status only (`content/registry.json:1302-1310`).
   It omits the definition-of-done fields `tier`, `thesis`, `framework`, and
   `diagrams`. Add the brief-supported tier and thesis, explicitly record that there
   is no single signature framework, and inventory the five rendered forms after the
   figure revision. The current validator permits partial draft metadata, so the
   green gate does not establish this requirement.

5. **Replace the outbound link with a qualifying publisher or bookseller page.**
   `ShelvedNearby` points to an Andreessen Horowitz promotional book page
   (`src/chapters/hard-thing.mdx:226-230`). A venture-capital firm's reading page is
   neither the book's publisher nor a bookseller, while the fixed anatomy requires
   the outbound book link itself to be one of those two. Use a stable direct publisher
   or retailer URL for this edition.

The chapter brief and seed metadata support the central no-formula thesis and the
deliberate absence of a Model section. No separate chapter-specific evidence dossier
or source excerpt exists in the repository, so factual and close-paraphrase checking
was bounded to those records and internal agreement among the prose, captions, and
figures; this review began no external web search. Within that boundary, the draft
otherwise uses original thematic prose, no quotation or real cover art, five key ideas
with captioned shared-vocabulary diagrams, four concrete practice cards, and three
related links that resolve to completed chapters. All direct imports and their relevant
transitive cover, registry, and SVG helpers were inspected.

`npm run check` passed on 2026-07-17: queue/registry/content validation, prose lint, 2
pipeline tests, 37 runner tests, 136 application tests, typecheck, production build,
and ESLint all completed successfully. Vitest emitted only the existing non-failing
jsdom `Window.scrollTo()` notices. The gate does not enforce the thesis sentence
limit, interpret graph polarity, recompute reading time, require complete draft
metadata, or classify an outbound vendor.

### ADVISORY

1. The caveat says the advice is rooted in a venture-backed technology founder's
   experience and contrasts that setting with public institutions, mature companies,
   and teams with less capacity to absorb risk
   (`src/chapters/hard-thing.mdx:203-212`). This is a useful scope warning, but neither
   the brief nor another recorded local source supports the biographical and
   institutional comparison. A future evidence pass should record the source used or
   recast the passage explicitly as this page's applicability judgment rather than an
   evidenced characterization of the book.
