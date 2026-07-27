verdict: resolved

## Critique round 1 — 2026-07-27

### Required

1. **Reverse Figure 110.2's tier order so the stated prerequisites actually support
   guilt-free spending.** The prose and caption say that fixed costs, savings, debt,
   and investing receive their claims before discretionary spending
   (`src/chapters/i-will-teach-you.mdx:55-68`). The chapter passes
   `guilt-free spending` as index 0 and `fixed costs` as the last item
   (`src/chapters/i-will-teach-you.mdx:69-76`), but `Pyramid` defines index 0 as
   the widest base and the last item as the apex
   (`src/components/diagrams/Pyramid.tsx:9-18,41-45`). The rendered hierarchy
   therefore says guilt-free spending supports every prior claim, exactly the
   opposite of the section's argument. Put the prerequisites at the base and the
   remainder at the apex, or choose another in-vocabulary structure that preserves
   the stated order.

2. **Make every Figure 110.6 quadrant agree with the cost and value axes.** `Matrix`
   consumes labels in top-left, top-right, bottom-left, bottom-right order, with
   high vertical values at the top (`src/components/diagrams/Matrix.tsx:11-17,45-50`).
   The chapter instead places “small and unimportant” and “cheap pleasure” in the
   high-cost row, then places “costly and forgettable” and the highlighted
   deliberate-funding target in the low-cost row
   (`src/chapters/i-will-teach-you.mdx:167-179`). All four cases contradict their
   plotted cost. Reorder or relabel the quadrants and move the highlight so the
   visual teaches the value-versus-cost decision described by the prose.

3. **Remove the label collision in Figure 110.1 and clarify what its scale
   measures.** The marker at `0.8` places “start here” near x=280, while the long
   right-pole label “a few recurring choices” ends at x=340. `Spectrum` renders
   both as unwrapped text on nearly the same baseline by default
   (`src/chapters/i-will-teach-you.mdx:41-50`;
   `src/components/diagrams/Spectrum.tsx:108-134`), so the two labels occupy the
   same region regardless of horizontal scrolling. The unexplained numeric marker
   and zone boundaries also turn a priority between types of expense into an
   undefined quantitative continuum. Use the component's non-colliding marker
   placement and name the dimension, or use a simpler registered form that
   structurally contrasts small one-off cuts with high-impact recurring choices.

4. **Do not use reinforcing-edge semantics merely to accent preferred money
   routes.** Figure 110.3 marks the edge from `remainder available` back to
   `payday` as `compoundingEdge={3}`, even though neither the prose nor the evidence
   says the remainder causes or reinforces the next payday
   (`src/chapters/i-will-teach-you.mdx:80-100`). `ProcessLoop` reserves that prop
   for the reinforcing, compounding edge of a self-reinforcing cycle
   (`src/components/diagrams/ProcessLoop.tsx:5-11,30-34,71-85`). Figure 110.7
   likewise marks the one-way income-to-savings and income-to-investing routes as
   `kind="reinforcing"` (`src/chapters/i-will-teach-you.mdx:191-206`), while
   `NodeGraph` defines that kind as a reinforcing system relation, not a neutral
   transfer that happens to be desirable
   (`src/components/diagrams/NodeGraph.tsx:13-19,31-35,94-119`). Keep the recurring
   payday routine and automated fan-out, but render their edges with semantics that
   the chapter actually establishes.

5. **Complete the registry record before this chapter can be done.** The
   `i-will-teach-you` entry contains only routing/display fields and `status:
   "draft"` (`content/registry.json:2173-2180`). It is missing the required `tier`,
   `thesis`, `framework`, and `diagrams` inventory, even though the brief supplies
   the first three and the chapter renders seven named forms. `mark.py` changes
   status only, so approval would leave definition-of-done item 7 unsatisfied even
   though the current validator does not reject the omission.

### Advisory

1. The Thesis section takes five sentences
   (`src/chapters/i-will-teach-you.mdx:11-18`), while the authoring contract asks
   this section to compress the whole argument into one or two. Its argument is
   clear, so this does not independently block approval, but it can be tightened
   while preserving the one-line Hero thesis.

2. “Shelved Nearby” supplies four relevant links to completed chapters, but the
   page gives no one-clause explanation of any relationship
   (`src/chapters/i-will-teach-you.mdx:258-262`). Add a short lead naming why each
   book is nearby if that can be done without changing the shared footer.

3. Within the bounded brief and recorded evidence, the remaining factual synthesis
   is appropriately qualified. The page uses original thematic organization,
   prose, and shared SVG primitives, with no quotation, real cover art, apparent
   close paraphrase, or apparent reproduction of a source figure. The automation,
   conscious-spending, recurring-investment, diversification, overdraft, and
   changing-rule claims are traceable to `content/evidence/i-will-teach-you.md`.
   This review began no new external web search.

4. The remaining anatomy and technical wiring are intact. Six key ideas each have a
   captioned vocabulary figure, the signature automated-finance model is present,
   the four exercises specify observable actions, related slugs resolve to done
   chapters, and the outbound publisher link matches the recorded evidence. Every
   SVG has a chapter-local 440px minimum width inside the shared horizontal
   scroller. A direct render contains 1,783 reader-visible alphanumeric word tokens,
   consistent with the nine-minute Hero badge at approximately 200 words per minute
   rounded up.

5. `npm run check` completed with `CHECK OK` on 2026-07-27. Validation and prose
   lint passed; all 40 runner tests and 233 Vitest tests passed; TypeScript, the Vite
   production build, and ESLint passed. Vitest emitted only the existing non-failing
   jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-27

- Figure 110.1 now uses the registered comparison / split form to contrast small
  one-off cuts with recurring choices. This removes the undefined numeric spectrum,
  zones, and colliding marker label while preserving the chapter's priority claim.
- Figure 110.2 now passes `Pyramid` tiers from fixed costs at the base through
  savings and debt, then investing, to guilt-free spending at the apex.
- Figure 110.3 no longer marks the payday-return edge as compounding. Figure 110.7
  now renders all income transfers as neutral directed routes, without unsupported
  reinforcing semantics.
- Figure 110.6 now places costly, low-value spending in the top-left; deliberate
  funding in the top-right and highlighted target quadrant; small, low-value spending
  in the bottom-left; and cheap pleasure in the bottom-right, matching the axes.
- The `i-will-teach-you` draft registry record now includes tier 3, the brief's
  thesis and automated-personal-finance framework, and the seven rendered diagram
  forms. Its status remains `draft`.
- `npm run check` passed on 2026-07-27.
