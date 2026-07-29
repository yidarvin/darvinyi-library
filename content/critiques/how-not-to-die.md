verdict: approve

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

## Builder resolution — 2026-07-28

- Compressed **The thesis** to two sentences and retained the distinction between Greger's
  ambitious preventive case and the chapter's bounded interpretation.
- Replaced Figure 144.1's invalid food-group Venn with the new reusable **Assembly /
  contribution** diagram. Its three distinct food groups now converge on a whole-food
  pattern rather than falsely overlap as sets. Added the primitive to the diagram index and
  vocabulary.
- Reduced Figure 144.3 to the supported relationships: food pattern → lower blood lipids
  on average in the recorded randomized evidence, and care and context → food pattern. The
  three cards are now spaced so every arrow segment and label stays outside the cards.
- Replaced Figure 144.4's sequential Flow with a neutral side-by-side comparison of short
  randomized trials and long observational cohorts. It now shows distinct evidence paths and
  preserves the primitive's 380-unit mobile width.
- Supplied Figure 144.5's Pyramid tiers from base to apex: whole-food staples, planned
  nutrients and fortification, variety and adequate energy, then personal goals and
  preferences. Removed the unsupported `ascending` prop.
- Narrowed the clinical claim to recorded randomized lipid evidence, removed unsupported
  blood-pressure, glycemic-control, and weight claims, and aligned the planning list with the
  evidence record by naming B12, vitamin D, iodine, zinc, calcium, and selenium.
- Completed the draft registry record with tier 3, a chapter-aligned thesis, the deliberate
  absence of a signature model, and the five rendered diagram forms in order. The registry
  status remains `draft`; the queue was not changed.
- Made the caveat self-contained by removing the inaccessible pointer to internal evidence
  notes while retaining its concrete randomized-trial qualification.

## Critique round 2 — 2026-07-28

### Required

1. **Restore the book's central preventive argument instead of reducing the
   distillation to dietary prudence and one lipid outcome.** The brief says the
   thesis to convey is that Greger treats diet as the biggest lever against the
   diseases most likely to kill people, with the evidence pointing toward whole
   plant foods (`prompts/notes/how-not-to-die.md:10-12`). The Hero never states that
   claim, and “The thesis” calls the case ambitious but replaces it with the much
   narrower conclusion that plant-centered patterns can lower blood lipids
   (`src/chapters/how-not-to-die.mdx:5-16`). Of the five Key Ideas, three are mainly
   qualifications about medical care, evidence design, and nutritional planning;
   none explains the book's claimed connection between the ordinary food pattern
   and its broad chronic-disease or mortality focus. A reader therefore leaves with
   sensible guidance for eating more plants, but not with the core argument of *How
   Not to Die*, which fails the site's defining distillation standard and the
   rubric's thesis requirement.

   Reintroduce the broad claim explicitly as **Greger's argument**, then give the
   library's bounded synthesis without presenting it as settled fact. The recorded
   evidence already provides a practical way to do this without reviving round 1's
   unsupported multi-risk-factor claims: two long-running cohorts support adjusted
   associations between healthier plant-centered patterns and cardiovascular or
   all-cause outcomes, while the randomized meta-analysis supports lower blood
   lipids and the caveat explains the causal limit
   (`content/evidence/how-not-to-die.md:6-11`). Make that preventive logic visible in
   the Hero/Thesis and at least one structural Key Idea and diagram. Keep the
   mandatory criticism prominent, preserve medical care, and do not state
   “biggest lever” as an independently established fact.

### Advisory

None.

Round 1's seven required findings are resolved. Figure 144.1 now encodes assembly,
Figure 144.3's narrowed arrows render with clearance, Figure 144.4 keeps the study
designs parallel, Figure 144.5 renders the hierarchy from the intended base, the
clinical and nutrient claims match the recorded evidence, and the registry record
is complete. The outbound link and all three related slugs resolve, the Model
section remains correctly absent under the brief, and no apparent close paraphrase,
source-figure reproduction, quotation, or real cover art was found. No new external
web search was begun.

`npm run check` completed with `CHECK OK` on 2026-07-28: queue, registry, content,
critique-state, and prose validation passed; all 42 pipeline and runner tests and all
310 Vitest tests passed; TypeScript, the Vite production build, and ESLint passed.
Vitest emitted only the existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-28

- Restored the book's central preventive claim in the Hero and two-sentence Thesis as
  **Greger's argument**, rather than an independently established fact. Both now pair it with
  the chapter's bounded synthesis: adjusted cohort associations with cardiovascular and
  all-cause outcomes, randomized evidence of lower blood lipids on average, and no claim that
  diet is the biggest lever, proves causation, or replaces care.
- Reworked Key Idea 2 and Figure 144.2 into a neutral evidence map. The map keeps long cohorts
  and randomized trials as separate paths: cohorts connect a healthful plant pattern with
  adjusted cardiovascular and mortality associations, while trials test the shorter-term lipid
  result. This makes the broad preventive logic visible without turning either study design into
  proof of universal disease prevention.
- Updated the registry thesis to match the restored attributed argument and its evidence-bounded
  interpretation. The record remains `draft`; the queue and done state were not changed.

## Critique round 3 — 2026-07-28

### Required

1. **Make the registry diagram inventory agree with the revised page.** Figure 144.2
   now renders a `NodeGraph` (`src/chapters/how-not-to-die.mdx:50-68`), but the
   registry still declares the second diagram as `comparison`
   (`content/registry.json:2851-2856`). The page's rendered sequence is assembly,
   node graph, node graph, comparison, pyramid. The registry currently records
   assembly, comparison, node graph, comparison, pyramid. This mismatch was
   introduced when round 2 changed the preventive-evidence figure without making
   the corresponding diagram-inventory update, and it violates the technical
   integrity requirement that the registry agree with the files on disk.

### Advisory

None.

Round 2's substantive finding is resolved. The Hero and Thesis now distinguish
Greger's broad preventive argument from the library's bounded conclusion, and Key
Idea 2 connects the recorded cohort associations and randomized lipid evidence
without claiming that either proves universal prevention. The five key ideas each
have an in-vocabulary structural figure; the deliberate absence of a Model section
matches the brief; the practice and mandatory caveat sections are concrete; the
nutrient guidance and clinical qualifications remain within the recorded evidence;
the three related slugs are done; and the Macmillan outbound link matches the
evidence record. No apparent close paraphrase, reproduced source figure, quotation,
or real cover art was found. No new external web search was begun.

`npm run check` completed with `CHECK OK` on 2026-07-28: queue, registry, content,
critique-state, and prose validation passed; all 42 pipeline and runner tests and all
310 Vitest tests passed; TypeScript, the Vite production build, and ESLint passed.
Vitest emitted only the existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-28

- Updated the `how-not-to-die` registry diagram inventory so its second entry is
  `node graph`, matching Figure 144.2 and the rendered order: assembly, node graph,
  node graph, comparison, pyramid. The chapter remains `draft`; no done status, commit,
  or push was made.

## Critique round 4 — 2026-07-28

### Required

None.

### Advisory

None.

Round 3's registry finding is resolved. The registry now records the rendered
diagram sequence as assembly / contribution, node graph, node graph, comparison,
and pyramid. The chapter and registry otherwise remain aligned: the Hero and Thesis
attribute Greger's broad preventive claim while bounding it with the recorded cohort
associations and randomized lipid evidence; the mandatory caveat keeps causation,
variable trial results, nutritional planning, and medical care explicit; all five
key ideas have captioned in-vocabulary diagrams; the deliberate absence of a Model
section matches the brief; and the related slugs and publisher link resolve. The
review found no apparent close paraphrase, reproduced source figure, quotation, real
cover art, or unsupported factual claim that changes the reader's understanding. No
new external web search was begun.

`npm run check` completed with `CHECK OK` on 2026-07-28: queue, registry, content,
critique-state, and prose validation passed; all 42 pipeline and runner tests and all
310 Vitest tests passed; TypeScript, the Vite production build, and ESLint passed.
Vitest emitted only the existing non-failing jsdom `Window.scrollTo()` notices.
