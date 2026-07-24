verdict: revise

## Critique round 1 — 2026-07-23

### Required

1. **Compress `The thesis` to the fixed one-or-two-sentence anatomy.** The dedicated
   thesis block at `src/chapters/seven-principles-marriage.mdx:13-17` contains five
   sentences. The authoring spec reserves this section for the compact argument a
   reader could carry away after reading nothing else. Preserve the ordinary-moments,
   friendship, conflict, influence, and repair synthesis, but express it in no more
   than two sentences.

2. **Correct figure 73.4's quadrant-to-axis mapping.** `Matrix` explicitly consumes
   quadrants in `[top-left, top-right, bottom-left, bottom-right]` order, with the
   vertical high pole at the top. The draft declares `meaning-laden` as high and
   `logistical` as low at
   `src/chapters/seven-principles-marriage.mdx:104-111`, but places `solve / make a
   plan` and `returning task / revise the system` in the high, meaning-laden row while
   placing `name the value / hear the wish` and `live with difference / seek a
   workable rhythm` in the low, logistical row. This reverses the prose's lesson, and
   `highlight={3}` consequently emphasizes recurring logistical conflict as the place
   to live with an enduring difference. Reorder the labels, and move the highlight if
   needed, so the visible matrix agrees with its axes, caption, and explanation.

3. **Complete and correct the book metadata before approval.** The registry entry at
   `content/registry.json:1443-1449` has none of the required `tier`, `thesis`,
   `framework`, or `diagrams` fields, even though definition-of-done item 7 requires
   them. It also supplies `John Gottman · 1999` to `Hero`, while the draft's own
   purchase label at `src/chapters/seven-principles-marriage.mdx:223` identifies the
   book as by John Gottman and Nan Silver. Correct the durable seed/registry metadata
   so the rendered byline credits both authors, then add the completion fields with
   diagram names that match the forms actually rendered.

4. **Develop the accepting-influence claim that the thesis makes load-bearing.** The
   thesis says the difference between manageable and damaging conflict includes
   whether each person can hear influence
   (`src/chapters/seven-principles-marriage.mdx:15-17`), but the page never explains
   what accepting a partner's influence means and none of the four exercises lets a
   reader practice it. The phrase is therefore undefined at the point where the page
   presents it as a causal hinge. Add it to an existing key idea and its structural
   diagram or give it its own key idea, then include a concrete practice; alternatively,
   remove it from the compact thesis if the page will not teach it.

### Advisory

1. Figure 73.1 draws every arrow toward `partner today` while labeling those arrows
   with the partner's actions, `ask`, `notice`, and `remember`
   (`src/chapters/seven-principles-marriage.mdx:46-51`). The picture can reasonably
   show pressures, hopes, people, and history informing a current map, but directional
   action labels imply that those surrounding nodes perform the actions. Neutral
   relationship labels or outward action arrows would remove the ambiguity.

2. The prose before `ShelvedNearby` states why *Nonviolent Communication* and
   *Difficult Conversations* are related, but the component also links
   `five-love-languages` without the relationship clause required by the cross-linking
   contract (`src/chapters/seven-principles-marriage.mdx:216-223`). Add a short,
   discriminating clause for that third link rather than leaving the reader to infer
   the connection.

3. Re-derivation against the bounded repository evidence supports the brief's central
   synthesis: friendship, respect, repair, measurable warning patterns, and the Four
   Horsemen signature model are all represented without quotation, real cover art, or
   an apparent recreation of a source figure. The love-map, bids, fondness, recurring
   conflict, flooding, repair, and Four Horsemen claims are internally coherent, and
   the caveat appropriately rejects personal prediction scores and communication
   advice for abusive situations. No chapter evidence dossier or source excerpts are
   recorded, so close-paraphrase comparison and stronger source-level verification
   were not possible; this review began no external web search.

4. Apart from the required defects, the page has the mandatory sections in order,
   five key ideas with captioned vocabulary diagrams, a signature Model, four concrete
   exercises, a safety-aware caveat, and a valid outbound publisher link. All three
   related slugs resolve to `done` chapters. The seven-minute badge agrees with a rough
   1,284-visible-word count at 200 words per minute.

5. The direct imports and their SVG helpers build successfully. The explicit minimum
   widths keep the smallest labels at approximately 9.5 CSS pixels or larger inside
   `Figure`'s horizontal scroller at phone width. `npm run check` completed with
   `CHECK OK` on 2026-07-23: validation, prose lint, all pipeline tests, all 151
   Vitest tests, TypeScript, the Vite production build, and ESLint passed. Vitest
   emitted only the existing non-failing jsdom `Window.scrollTo()` notices.
