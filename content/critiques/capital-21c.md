verdict: approve

## Critique round 1 — 2026-07-27

### Required

1. The two carry-away statements replace the brief's `r > g` condition with a
   different claim. The Hero says that "private assets grow faster than the economy"
   (`src/chapters/capital-21c.mdx:7`), and the final takeaway repeats that assets grow
   faster than the economy (`src/chapters/capital-21c.mdx:224-226`). A return on
   capital is not itself growth of the asset stock: returns may be consumed, taxed,
   lost, or reinvested, a distinction the chapter correctly makes elsewhere. The
   brief requires the thesis that returns on capital can outrun economic growth, and
   the recorded evidence treats saving and unequal returns as separate interacting
   drivers. Restore that distinction in both summary statements so a reader who sees
   only the Hero or final takeaway receives the actual model rather than a
   consequence that holds only after additional conditions.

2. Figures 111.2 and 111.6 misuse magnitude bars by placing unlike concepts on one
   quantitative-looking scale. Figure 111.2 assigns arbitrary lengths to one year's
   national income, a private wealth stock, and "ownership distribution"
   (`src/chapters/capital-21c.mdx:69-77`), although distribution is not a magnitude
   comparable to either stock or flow. Figure 111.6 similarly places economic
   growth, return to capital, and "result when ownership is unequal" on the same
   scale (`src/chapters/capital-21c.mdx:171-179`); the result is not a rate, and its
   intermediate bar length has no defined meaning. The vocabulary permits Bars for
   simple, clearly labeled magnitude contrasts, not for categorical annotations.
   Rework both figures so every encoded length has a coherent common basis and move
   conditions or consequences into a structural form that represents their role.

3. Exercise 02 tells the reader to pick an asset and includes "a student loan" in
   the examples (`src/chapters/capital-21c.mdx:191-195`). A student loan is an asset
   to the lender but a liability to the student, and the exercise gives no
   perspective that would make the classification valid. That directly undercuts
   the page's stock, flow, and debt distinction. Either identify the lender's claim
   explicitly or frame the exercise around an asset-or-liability compounding loop.

4. The Shelved Nearby block supplies three bare related slugs but no explanation of
   any relationship (`src/chapters/capital-21c.mdx:229-233`). The authoring contract
   requires each graph edge to note the relationship in one clause. Add a
   reader-visible relationship for each related book while retaining only links to
   built chapters.

### Advisory

1. The wealth-to-income discussion switches from "national income" to "one year's
   output" at `src/chapters/capital-21c.mdx:60-63`. Those are not strictly the same
   denominator. Use the recorded term consistently unless the distinction is
   intentionally explained.

2. Figure 111.5 marks the links from "tax and property rules" to both returns and
   assets as balancing, while one is labeled only "inheritance." Tax and property
   rules can reinforce or reduce concentration depending on their design, and
   inheritance itself transfers ownership rather than necessarily balancing it.
   More precise node and edge labels would make the visual agree with the nuanced
   prose.

### Verification

`npm run check` passed on 2026-07-27: queue/registry/content validation, prose lint,
2 pipeline tests, 40 runner tests, 236 application tests, typecheck, production
build, and ESLint all completed successfully. Vitest emitted only the existing
non-failing jsdom `Window.scrollTo()` notices.

The thesis, stock/flow distinction, conditional treatment of `r > g`, interacting
drivers of concentration, measurement caveat, and publisher link were re-derived
against `prompts/notes/capital-21c.md` and `content/evidence/capital-21c.md`. The
chapter, all of its imports, and the relevant shared SVG helpers were inspected. The
three related slugs resolve to completed chapters, the generated cover uses no book
art, and the recorded evidence supports the caveat's caution about measurement and
single-cause readings. Because the evidence dossier records source summaries rather
than source excerpts, close-paraphrase review was limited to the local material. No
new external web search was begun.

## Builder resolution — 2026-07-27

Resolved every required finding using the existing dossier, without a new external search.

1. Rewrote the Hero, Thesis, and final takeaway to name the actual condition: returns on
   capital persistently exceeding economic growth. Each now makes retention and reinvestment
   by an unequally owning group an additional condition, rather than calling a return the
   growth of an asset stock.
2. Replaced Figure 111.2's unlike magnitude bars with a comparison that separates the
   wealth-to-income ratio from the ownership-distribution question. Replaced Figure 111.6's
   bars with a flow that shows `r > g`, retained returns, unequal ownership, and the
   conditional concentration pressure as distinct roles. Updated the registry diagram forms
   to match.
3. Reframed Exercise 02 around a claim or obligation and explicitly identifies a student
   loan as the borrower's liability and the lender's asset.
4. Added reader-visible, linked relationship clauses for *The Psychology of Money*,
   *Thinking in Systems*, and *Why Nations Fail*. Each target is already a built chapter.
5. Preserved and tightened prior caveats: the wealth-to-income discussion now consistently
   uses national income, the institutional-rules node has neutral, precise edges for net
   returns and transfers, and the evidence scope note now distinguishes a return rate from
   asset-stock growth.

Verification after these changes: `npm run check` passed on 2026-07-27, including queue and
registry validation, prose lint, 42 pipeline and runner tests, 236 application tests,
typecheck, production build, and ESLint. Vitest emitted only the existing non-failing jsdom
`Window.scrollTo()` notices.

## Critique round 2 — 2026-07-27

### Required

1. The signature Model figure is not legible at the required 360px phone width. The
   chapter gives the branched `Flow` only `min-w-[380px]`
   (`src/chapters/capital-21c.mdx:175-181`), but that component computes a 578-unit
   viewBox for these three steps plus the branch
   (`src/components/diagrams/Flow.tsx:20-28`). At its 380px minimum, every 11.5-unit
   label therefore renders at about 7.6 CSS pixels, and the figure's padded mobile
   viewport makes the reader scroll even to see that undersized text. This is the
   page's signature framework, so it must meet the authoring contract's phone
   legibility requirement. Give the SVG a minimum rendered width near its intrinsic
   viewBox width, or restructure the model into a phone-legible composition without
   shrinking its labels.

2. The last sentence of the mandatory carry-away section says, "The counterweights
   are historical and political, which means they can be chosen"
   (`src/chapters/capital-21c.mdx:226-231`). The chapter has just identified war,
   depression, inflation, destruction, and other shocks as historical
   counterweights. Those events are not deliberate policy choices, and being
   historical does not imply that something can be chosen. Distinguish contingent
   historical shocks from institutions and policies that people can deliberately
   change, so the final takeaway does not collapse the chapter's own causal
   distinction.

### Advisory

1. When repairing the Model figure, add an explicit `ariaLabel` that includes both
   branch outcomes. `Flow`'s derived accessible name lists only the three `steps`
   (`src/components/diagrams/Flow.tsx:31-34`), so the current role-image name omits
   both the concentration pressure and the policy-and-shocks alternative that carry
   the figure's conclusion.

### Verification

`npm run check` passed on 2026-07-27: queue/registry/content validation, prose lint,
2 pipeline tests, 40 runner tests, 236 application tests, typecheck, production
build, and ESLint all completed successfully. Vitest emitted only the existing
non-failing jsdom `Window.scrollTo()` notices.

The prior round's four required fixes remain present: the summary statements now
separate a return rate from asset-stock growth, Figures 111.2 and 111.6 no longer
place unlike quantities on magnitude bars, Exercise 02 states the balance-sheet
perspective for a student loan, and every related link has a reader-visible
relationship clause. The brief, recorded evidence, chapter, imported components,
shared SVG helpers, registry entry, queue state, and related targets were checked
again without beginning a new external web search. The three related slugs are done,
the generated cover contains no book art, and `capital-21c` correctly remains draft
after this revise verdict.

## Builder resolution — 2026-07-27

Resolved every required finding using the existing dossier, without a new external search.

1. Set the signature Model `Flow` to its 578px intrinsic viewBox width. At a 360px phone
   viewport, the figure now scrolls horizontally rather than shrinking its 11.5-unit labels
   below their intended rendered size. Added an explicit accessible label that names both
   branch outcomes: concentration pressure and the policy-and-shocks alternative.
2. Rewrote the final carry-away sentence to separate contingent historical shocks from
   institutions and policies that people can deliberately change. The conclusion now retains
   the chapter's causal distinction rather than treating all counterweights as choices.
3. Preserved the first-round fixes: the Hero and takeaway distinguish return rates from
   asset-stock growth; Figures 111.2 and 111.6 do not use unlike concepts as magnitude bars;
   Exercise 02 states the borrower and lender perspectives for a student loan; and all three
   related, built chapters retain reader-visible relationship clauses.

Verification after these changes: `npm run check` passed on 2026-07-27, including queue and
registry validation, prose lint, pipeline and runner tests, application tests, typecheck,
production build, and ESLint. Vitest emitted only the existing non-failing jsdom
`Window.scrollTo()` notices.

## Critique round 3 — 2026-07-27

### Required

None.

### Advisory

None.

### Verification

`npm run check` passed on 2026-07-27: queue/registry/content validation, prose lint,
2 pipeline tests, 40 runner tests, 236 application tests, typecheck, production build,
and ESLint all completed successfully. Vitest emitted only the existing non-failing
jsdom `Window.scrollTo()` notices.

The brief, recorded evidence, chapter, directly imported book and diagram components,
shared SVG helpers, registry entry, queue state, generated cover path, and related targets
were checked without beginning a new external web search. The thesis and carry-away
statements preserve the conditional meaning of `r > g`; the stock/flow distinction,
retention mechanism, historical account, interacting distribution channels, and
measurement caveat agree with the local dossier. Each of the five key ideas has a
captioned, in-vocabulary structural diagram, and the signature Model figure renders at
its 578px intrinsic width so its labels remain legible in the horizontally scrolling
mobile figure. All three reader-visible related links resolve to completed chapters, and
the outbound link points to the publisher. The two earlier critique rounds' required
fixes remain present. Because the evidence dossier records source summaries rather than
source excerpts, close-paraphrase review was necessarily limited to the local material.
