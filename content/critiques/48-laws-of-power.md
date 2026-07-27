verdict: approve

## Critique round 1 — 2026-07-27

### Required

1. The page does not yet preserve the book's central argument as stated in the brief.
   The brief calls this an often ruthless catalog of observable laws that operate
   whether or not the reader chooses to use them. The Hero instead leads with agency
   and recognizing manipulation (`src/chapters/48-laws-of-power.mdx:5-8`), while much
   of the core turns the material into ordinary, consent-respecting workplace advice.
   Most clearly, “Influence lasts when the other person can still choose” supplies a
   “better test” and concludes that durable power comes from competence,
   contribution, and consent (`:170-182`). That is the library's ethical alternative,
   not one of Greene's key ideas, and it duplicates work that belongs in the mandatory
   caveat. Replace it with a supported central pattern from the book, and revise the
   Hero/takeaway as needed so a reader first understands Greene's descriptive,
   ruthless framework and then encounters the ethical rejection in “Where people get
   it wrong.” The recorded evidence currently supports only the book-level framing,
   not the specific claims that Greene emphasizes reputation, dependence, timing, and
   emotional control. Extend the evidence record enough to re-derive the final
   chapter-specific attributions.

2. Figure 114.6 contradicts its own axes. `Matrix` consumes quadrants in top-left,
   top-right, bottom-left, bottom-right order. With concealed terms on the left and
   real room to choose at the top, the top-left cell cannot be “informed agreement”
   or “a durable basis for cooperation” (`src/chapters/48-laws-of-power.mdx:184-196`).
   Its terms are concealed by definition. Relabel or restructure the four cases so
   every cell follows from both axes and the figure agrees with its caption.

3. The registry entry is incomplete
   (`content/registry.json:2254-2262`). It has no `tier`, `thesis`, `framework`, or
   `diagrams` fields. The authoring contract requires that inventory, and this title
   specifically requires the reason for omitting the Model section to be recorded.
   Add the missing metadata, state that no single signature model exists, and list
   the final rendered diagram forms in order.

4. The caveat reproduces the publisher's phrase “amoral, cunning, ruthless” inside
   ordinary body prose (`src/chapters/48-laws-of-power.mdx:232-241`). The
   non-negotiable copyright rule permits verbatim source language only as the rare
   short attributed epigraph, not as an inline evidentiary quotation. Paraphrase the
   publisher's characterization in original language while retaining the source and
   the force of the criticism.

### Advisory

- Remove the unused `Compare` import from
  `src/chapters/48-laws-of-power.mdx:3` when revising the chapter.

- `npm run check` passed in full on 2026-07-27: validation, prose lint, 40 pipeline
  tests, 243 application tests, TypeScript, production build, and ESLint. Vitest
  emitted only the existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-27

- Recast the Hero, thesis, sixth key idea, and takeaway around Greene's descriptive,
  often ruthless catalog of recurring power patterns. Replaced the consent-based
  "Influence lasts" section with an information-asymmetry pattern grounded in the
  book's treatment of concealed intention and private knowledge; the ethical rejection
  remains in the mandatory caveat.
- Extended `content/evidence/48-laws-of-power.md` with the book's searchable table of
  contents. It records support for the chapter's attributions about hidden intention,
  reputation, dependence, timing, emotional disturbance, and information asymmetry.
- Rebuilt Figure 114.6 as an information matrix. Its four cells now align with both
  axes: concealed or declared aim, and little or more private knowledge.
- Completed the registry inventory with tier, thesis, the deliberate Model-section
  omission, and the six rendered diagram forms in page order.
- Paraphrased the publisher's characterization in the caveat, removed the inline
  verbatim phrase, and removed the unused `Compare` import.

## Critique round 2 — 2026-07-27

### Required

None. The round-one findings are resolved. The revised chapter now preserves
Greene's descriptive, often ruthless account before separating out the library's
defensive applications; Figure 114.6 follows both of its axes; the registry records
the deliberate Model-section omission and all six rendered forms; and the caveat
uses original wording supported by the recorded evidence.

`npm run check` passed in full on 2026-07-27: queue and registry validation, prose
lint, 40 pipeline tests, 243 application tests, TypeScript, production build, and
ESLint. The jsdom `Window.scrollTo()` notices remained non-failing.

### Advisory

None.
