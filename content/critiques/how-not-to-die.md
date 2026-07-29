verdict: revise

## Critique round 1 — 2026-07-28

### Required

1. **Compress “The thesis” to the required one or two sentences.** The paragraph at
   `src/chapters/how-not-to-die.mdx:13-17` contains three sentences. The authoring
   spec defines this section as the one- or two-sentence argument a reader can carry
   away. Preserve the useful distinction between Greger's ambitious case and the
   draft's bounded interpretation, but make that compression conform to the fixed
   anatomy.

2. **Replace Figure 144.1 with a form that encodes combination rather than set
   intersection.** The chapter passes vegetables and fruit, beans and whole grains,
   and nuts and seeds as the three sets of a `Venn` and labels their intersection “a
   repeatable whole-food pattern” at
   `src/chapters/how-not-to-die.mdx:36-45`. Those food-group categories do not
   overlap to produce a member that belongs to all three; a dietary pattern combines
   foods drawn from the groups. The diagram vocabulary reserves Venn for a sweet
   spot where sets actually overlap (`docs/diagram-vocabulary.md:100`). As rendered,
   the first key idea's visual teaches the wrong structural relationship.

3. **Recompose Figure 144.3 so its directed relationships render intact.** The
   chapter places `food pattern` at x 0.50, `glycemic control` at x 0.86, and `body
   weight` at x 0.14 (`src/chapters/how-not-to-die.mdx:84-95`). With `NodeGraph`'s
   380-unit viewBox, 94-unit cards, and 7-unit arrow clearance
   (`src/components/diagrams/NodeGraph.tsx:43-58,90-97`), each horizontal pair has
   only about 9 units between cards but needs 14 units of clearance. Both edge
   segments therefore reverse direction. Their offset `can affect` labels land
   inside the destination cards and are subsequently obscured because nodes paint
   after edges (`NodeGraph.tsx:75-135`). The `blood lipids` and `care and context`
   cards also overlap slightly at the authored coordinates. Increase the clearances
   through chapter-local node placement or otherwise simplify the map so every
   stated relationship is visible and correctly directed.

4. **Do not present different study designs as successive stages of one process in
   Figure 144.4.** The prose correctly distinguishes short randomized trials from
   long observational cohorts, but the `Flow` at
   `src/chapters/how-not-to-die.mdx:103-115` draws `food change → short trial: risk
   factor → long cohort: outcomes → careful conclusion`. `Flow` explicitly means a
   start-to-end procedure or cause-to-effect chain
   (`src/components/diagrams/Flow.tsx:14-17`); a cohort is not the next stage of a
   short trial. Use a vocabulary form that preserves the designs as distinct
   evidence paths or comparisons. Also preserve the primitive's authored mobile
   label size: four steps generate a 558-unit viewBox
   (`Flow.tsx:21-26`), while the chapter supplies only `min-w-[520px]`, shrinking its
   11.5-unit labels at the 360px scroll layout.

5. **Correct the reversed hierarchy in Figure 144.5.** The caption says adequacy is
   the foundation, but the chapter supplies `personal goals and preferences` first
   and `whole-food staples` last, then passes an `ascending` prop
   (`src/chapters/how-not-to-die.mdx:127-137`). `Pyramid` has no `ascending` prop and
   ignores it; index 0 is always the base and the last index is the apex
   (`src/components/diagrams/Pyramid.tsx:9-14,22,41-45`). The rendered pyramid
   therefore puts preferences at the foundation and staples at the apex, opposite
   the intended prerequisite structure and caption. Supply the tiers in the order
   the actual component renders.

6. **Bring the central multi-risk-factor claim within the recorded evidence.** The
   prose and Figure 144.3 say a plant-centered food pattern can affect blood pressure,
   glycemic control, body weight, and blood lipids
   (`src/chapters/how-not-to-die.mdx:73-95`). The recorded randomized evidence
   supports lower blood lipids, while the only recorded weight trial found no
   between-group weight or lipid difference; the notes record no blood-pressure or
   glycemic-control evidence (`content/evidence/how-not-to-die.md:11-12`). This claim
   is central to the explanation that one pattern matters across conditions, not a
   peripheral aside. Narrow the prose and diagram to what the current record
   supports, or record suitable supporting evidence. Apply the same reconciliation
   to the actionable nutrient list: the notes support B12, vitamin D, iodine, zinc,
   calcium, and selenium, but the page substitutes iron and omega-3 fats for selenium
   without recorded support (`src/chapters/how-not-to-die.mdx:120-125`;
   `content/evidence/how-not-to-die.md:13-14`).

7. **Complete the registry record required for done status.** The
   `how-not-to-die` entry at `content/registry.json:2841-2847` stops after routes and
   draft status. Definition-of-done item 7 requires tier, thesis, framework, and the
   diagram inventory as well as the display metadata. Record tier 3, a
   chapter-aligned thesis, the brief's deliberate absence of a signature model, and
   the actual diagram forms in rendered order.

### Advisory

1. **Do not direct readers to an internal evidence file they cannot reach.** The
   caveat ends with “See the evidence notes” at
   `src/chapters/how-not-to-die.mdx:170-178`, but the chapter supplies no link to
   those notes. The underlying evidence record exists and the preceding randomized
   trial is identified well enough to keep this non-blocking; if the sentence
   remains, make the destination available to the reader or replace the internal
   pointer with a self-contained attribution.

The bounded review found no apparent close paraphrase, reproduced source figure,
quotation, or real cover art. The draft presents Greger's position as a
well-supported option rather than settled proof, preserves medical care, states the
observational limitations plainly, and gives concrete practices with appropriate
clinical cautions. Five key ideas are present, the Model section is correctly absent
under the brief, all three related slugs are done, and the Macmillan outbound link
matches the evidence record. No new external web search was begun.

`npm run check` completed with `CHECK OK` on 2026-07-28: queue, registry, content,
critique-state, and prose validation passed; all 42 pipeline and runner tests and all
310 Vitest tests passed; TypeScript, the Vite production build, and ESLint passed.
Vitest emitted only the existing non-failing jsdom `Window.scrollTo()` notices.
