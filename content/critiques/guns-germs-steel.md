verdict: approve

## Critique round 1 — 2026-07-16

### Required

1. **Compress `The thesis` to the fixed one-or-two-sentence anatomy.** The section
   currently takes five sentences to move from Diamond's question through food
   production, density, technology, disease, and the framework's limits
   (`src/chapters/guns-germs-steel.mdx:11-19`). The Hero already supplies the
   one-line claim, but the required Thesis block must itself be the one or two
   sentences a reader can carry away. Preserve the rejection of innate group
   differences and the non-inevitability boundary while making this block conform
   to the specified anatomy.

2. **Recompute the Hero badge from the final rendered page.** A direct render of
   the exact chapter contains 1,352 visible words, including headings, Hero and
   footer text, captions, SVG labels, exercise titles, and prose. At approximately
   200 words per minute, rounded up, this is a seven-minute distillation, not
   `minutes={6}` (`src/chapters/guns-germs-steel.mdx:5-9`). Recompute again after
   the thesis revision and set the final rounded value.

3. **Replace Figure 33.2's inverted hierarchy with geometry that shows the stated
   foundation.** The prose and caption say that food production is the base,
   denser settlement builds on it, and specialized roles sit above. The imported
   `Pyramid` places tier index 0 at the bottom but computes it at only 128 units
   wide, while tier index 2 appears at the top at 300 units wide
   (`src/components/diagrams/Pyramid.tsx:23-45`). The chapter therefore renders
   the food foundation as the narrowest tier and specialized institutions as the
   widest, the reverse of the vocabulary's foundational-pyramid semantics
   (`src/chapters/guns-germs-steel.mdx:53-72`). Recompose this chapter-local figure
   with an existing vocabulary form whose visible structure matches the causal
   stack. Do not change the shared component. Also preserve a rendered size that
   keeps every meaning-bearing label readable on a phone; the present 380 px
   minimum renders the component's 9-unit tier notes at only 9 CSS px.

4. **Remove Figure 33.3's unsupported return edge.** `ProcessLoop` always connects
   the final stage back to the first, so the diagram asserts that `repeated
   exposure changes vulnerability` leads back to `close human-animal contact`
   (`src/components/diagrams/ProcessLoop.tsx:28-31,68-83`; `src/chapters/guns-germs-steel.mdx:84-96`). Neither the prose nor the caption supplies that causal return, and changing population vulnerability does not by itself create renewed animal contact. Use a directed sequence or sparse system map, or label a genuinely supported feedback mechanism, so the figure encodes the disease ecology described rather than a false cycle.

5. **Make Figure 33.4's labels intrinsically legible.** The shared `Spectrum`
   places both pole labels on the same baseline and its marker caption four units
   lower (`src/components/diagrams/Spectrum.tsx:92-110`). In this figure, the long
   `large climate shift` and `similar growing conditions` poles reach into the
   same central region, while the `lower friction` marker at 0.72 overlaps the
   right pole (`src/chapters/guns-germs-steel.mdx:107-119`). Those collisions exist
   inside the SVG at every scale, so horizontal scrolling cannot repair them.
   Shorten or remove the colliding chapter-local labels, or use another vocabulary
   form. If the Spectrum remains, also increase its authored minimum width enough
   to keep the 9.5-unit zone labels at the established phone-readable scale.

6. **Make the Model figure and its caption claim the same thing.** Figure 33.6 is
   an unbranched five-step Flow from ecology to unequal power, but its caption says
   the diagram shows “room for change at every link”
   (`src/chapters/guns-germs-steel.mdx:153-174`). No branch, modifier, or alternate
   path encodes that qualification. Either show the stated contingency through the
   shared vocabulary or narrow the caption to the causal sequence actually drawn;
   keep the surrounding prose's important warning that the framework is not a
   finished historical script.

### Advisory

1. Within the repository's bounded evidence, the chapter otherwise carries the
   brief's geography-and-biology thesis and mandatory determinism critique in
   original thematic prose. It uses no quotation, real cover art, source-order
   imitation, or bespoke reproduction of a source figure. The caveat records two
   scholarly DOI links, including the plant-domestication paper used for the
   multiple-pathways point. Those endpoints did not return inspectable text through
   the bounded source access in this pass, and no new external web search was
   begun, so closer source-to-sentence verification was not practical here.

2. Apart from the required figure findings, the structural coverage is sound: five
   key ideas each have a captioned vocabulary figure, the signature geographic
   model is present, four exercises give concrete tests and actions, and the final
   takeaway is concise. `sapiens` resolves to a done chapter and the prose states
   the relationship; the outbound Penguin URL is a direct publisher link. The
   registry's tier, thesis, framework, status, and six-form diagram inventory agree
   with the current draft.

3. `npm run check` completed with `CHECK OK` on 2026-07-16: queue/registry/content
   validation, prose lint, both pipeline tests, all 70 Vitest tests, TypeScript and
   Vite production build, and ESLint passed. Vitest emitted only the existing
   non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-16

- Compressed **The thesis** to two sentences. It retains the rejection of innate
  group differences and states that ecological conditions influence, rather than
  determine, historical outcomes.
- Recomputed the final page's reading-time badge at roughly 200 words per minute
  and set the Hero to `minutes={7}`.
- Replaced Figure 33.2's inverted `Pyramid` with a three-step `Flow` from repeatable
  food production to denser settlement and then specialized roles. Its 440 px
  minimum keeps the 11.5-unit labels at a readable rendered size.
- Replaced Figure 33.3's cyclic `ProcessLoop` with a directed `Timeline` for contact,
  spillover or adaptation, sustained transmission, and changed vulnerability. The
  new caption states that sequence without asserting a return edge; its 560 px
  minimum keeps its labels readable.
- Shortened Figure 33.4's poles to `harder match` and `closer match`, removed the
  colliding marker caption, and increased the Spectrum's minimum width to 480 px.
- Narrowed Figure 33.6's caption to the causal sequence actually rendered by the
  unbranched `Flow`. The surrounding Model prose continues to state that choices and
  local circumstances can change the path.
- Updated this chapter's registry diagram inventory to match the chapter-local Flow
  and Timeline replacements. `npm run check` passed after these changes.

## Critique round 2 — 2026-07-16

### Required

None.

### Advisory

1. All six round 1 REQUIRED findings remain resolved in the current draft. The Thesis
   is two sentences and preserves both the rejection of innate group differences and
   the limit on ecological inevitability (`src/chapters/guns-germs-steel.mdx:11-16`).
   The seven-minute badge remains consistent with the recorded rendered-word estimate
   (`src/chapters/guns-germs-steel.mdx:5-9`). Figures 33.2 and 33.3 now use directed,
   non-cyclic forms; Figure 33.4 has non-colliding pole and zone labels at a readable
   authored width; and Figure 33.6's caption claims only the causal sequence that the
   Flow draws (`src/chapters/guns-germs-steel.mdx:59-114,153-174`).

2. Against the bounded evidence, the chapter accurately carries the brief's core
   geography-and-biology argument and its mandatory specialist criticism. Its factual
   claims are framed as possibilities or proposed mechanisms rather than universal
   laws, and the prose repeatedly preserves roles for institutions, violence, local
   adaptation, political judgment, and contingency. The two scholarly DOI endpoints
   already recorded in the caveat again returned 403 responses when opened directly,
   so closer source-to-sentence inspection was not practical and no new external search
   was begun. There is no new evidence that warrants reopening the settled round 1
   sourcing assessment.

3. The page satisfies the remaining anatomy and diagram requirements. Five key ideas
   each have a captioned vocabulary figure, followed by a distinct signature-model
   Flow. The figures' minimum widths combine with `Figure`'s horizontal overflow to
   preserve meaning-bearing label sizes on a phone, and their labels agree with the
   surrounding prose. Four exercises give concrete tests and actions, the credibility
   caveat is prominent and sourced, the final takeaway is concise, `sapiens` resolves
   to a done page, and the outbound link points directly to the publisher. The registry
   metadata and six-form diagram inventory match the draft.

4. `npm run check` completed with `CHECK OK` on 2026-07-16: queue/registry/content
   validation, prose lint, both pipeline tests, all 70 Vitest tests, TypeScript and
   Vite production build, and ESLint passed. Vitest emitted only the existing
   non-failing jsdom `Window.scrollTo()` notices.
