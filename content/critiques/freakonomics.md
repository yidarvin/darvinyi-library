verdict: approve

## Critique round 1 — 2026-07-15

### Required

1. **Compute the Hero badge from the rendered page.** A direct render of the exact
   chapter contains 1,276 visible words, including headings, captions, SVG labels,
   generated Hero text, exercise labels, and footer text. At the specified roughly
   200 words per minute, rounded up, the badge must read 7 minutes, not
   `minutes={5}` (`src/chapters/freakonomics.mdx:5-9`).

2. **Keep Figure 20.2's branched Flow legible on a phone.** With three steps and a
   branch, the shared `Flow` computes a 578-unit-wide viewBox and draws its step and
   outcome labels at 11.5 units (`src/components/diagrams/Flow.tsx:19-29,75-82,109-110`).
   The chapter gives it only a 440 px minimum width
   (`src/chapters/freakonomics.mdx:57-64`), which renders those labels at about
   8.8 CSS px when the figure scrolls at its minimum. Increase the chapter-local
   authored width to roughly 560 px, or use a form whose complete labels remain
   readable at the current width.

3. **Remove the false negative-causal semantics from Figure 20.4.** The two
   `kind="balancing"` edges make the shared `NodeGraph` draw dashed lines with minus
   signs, whose documented meaning is a balancing causal edge
   (`src/components/diagrams/NodeGraph.tsx:15-18,78-103`). The figure therefore
   depicts `observed pattern` as negatively affecting `rival explanations` and
   `rival explanations` as negatively affecting `specific question`, while the
   prose and caption say that alternatives are tests applied to a pattern
   (`src/chapters/freakonomics.mdx:83-107`). Use plain edges or recompose the graph
   so its direction and polarity encode the stated evidence-testing process.

4. **Complete the registry record required for a finished chapter.** The
   `freakonomics` entry currently stops at `status: "draft"` and omits the authoring
   contract's required `tier`, `thesis`, `framework`, and diagram-form inventory
   (`content/registry.json:397-405`). Populate those fields from the seed, brief,
   and the six figures actually rendered before approval.

### Advisory

1. Within the repository's bounded evidence, the draft carries through the brief's
   incentives thesis and signature model in original thematic prose. It has five key
   ideas with captioned shared-vocabulary figures, four concrete exercises, a useful
   caveat, a generated typographic cover, and no quotation or real cover art. The
   repository contains no chapter-specific evidence dossier beyond the brief and seed
   metadata, and this review began no external web search.

2. The caveat's repeated phrase `the authors` blurs three different possible
   referents: the book's coauthors, the original abortion-and-crime paper's authors,
   and the test-score-manipulation study's authors
   (`src/chapters/freakonomics.mdx:182-189`). Naming the relevant research team or
   using neutral wording would make the evidence provenance clearer without changing
   the caution the paragraph correctly communicates.

3. The signature loop marks the `measured outcome → reward or penalty` edge as
   `compounding`, although the prose describes institutional feedback and rule
   revision, not necessarily amplification (`src/chapters/freakonomics.mdx:133-149`;
   `src/components/diagrams/ProcessLoop.tsx:8-15,76-88`). A neutral feedback edge
   would match the claim more precisely.

4. Both nearby slugs resolve to done chapters, the preceding sentence supplies the
   requested relationship clauses, and the outbound URL is a direct publisher link.

5. `npm run check` passed on 2026-07-15: queue, registry, critique, and content
   validation; prose lint; both pipeline tests; all 44 Vitest tests; TypeScript and
   Vite production build; and ESLint. Vitest emitted only the existing non-failing
   jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-15

1. Updated the Hero badge to `minutes={7}`, matching the recorded 1,276 rendered-word
   count at roughly 200 words per minute, rounded up.
2. Increased Figure 20.2's chapter-local Flow minimum width from 440 px to 560 px so
   its branched step and outcome labels retain readable rendered size.
3. Replaced Figure 20.4's two `balancing` edges with plain directed edges. The graph
   now depicts evidence moving from the observed pattern to rival explanations and
   back to the specific question, without false negative-causal markers.
4. Completed the `freakonomics` registry record while keeping its status `draft`:
   added tier, brief-derived thesis, `Incentives` framework, and the inventory of all
   six rendered diagram forms.

## Critique round 2 — 2026-07-15

### Required

None. All four required findings from round 1 are resolved in the exact draft reviewed:
the Hero badge reads 7 minutes, Figure 20.2 retains readable scale through its 560 px
minimum width and scrolling Figure wrapper, Figure 20.4 uses semantically neutral
directed edges, and the registry contains the required chapter metadata and six-form
diagram inventory.

### Advisory

No new advisory findings. The repository still contains no chapter-specific evidence
dossier beyond the brief, seed metadata, and recorded critique history, so this pass did
not expand the claim trail or begin an external search. The earlier advisory observations
remain non-blocking and are not reopened.

`npm run check` passed on 2026-07-15: queue, registry, critique, and content validation;
prose lint; both pipeline tests; all 44 Vitest tests; TypeScript and Vite production
build; and ESLint. Vitest emitted only the existing non-failing jsdom
`Window.scrollTo()` notices.
