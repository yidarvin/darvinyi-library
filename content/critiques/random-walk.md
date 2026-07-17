verdict: resolved

## Critique round 1 — 2026-07-16

### REQUIRED

1. **Correct the opening's false counterparty premise.** The thesis says every seller
   "saw the same public information and made the opposite choice"
   (`src/chapters/random-walk.mdx:13-15`), but the next section correctly says market
   participants have different information, models, constraints, and risk appetites
   (`:30-33`). A seller may be raising cash, rebalancing, indexing, harvesting a tax
   loss, or acting under a different mandate without having reviewed the buyer's
   information or formed the opposite valuation thesis. Preserve the useful point
   that a liquid-market trade has a counterparty and that public opportunities face
   competition, but do not turn that into identical knowledge or opposite beliefs.

2. **State the active-management arithmetic accurately.** The draft says the
   "aggregate active group must lag the market it collectively owns"
   (`src/chapters/random-walk.mdx:51-55`). Active investors do not collectively own
   the whole market when passive investors also hold it, and the valid accounting
   identity compares the average actively managed dollar with the corresponding
   passive market portfolio: before costs their aggregate returns are equal, while
   the active average falls behind after its additional costs. This arithmetic is
   central to the indexing case, so make the comparator and the before/after-cost
   claim precise rather than attributing ownership of the market to the active group.

3. **Fix Figure 59.5's reversed risk-capacity mapping.** `Matrix` defines its
   quadrants as top-left, top-right, bottom-left, bottom-right, with the vertical
   high value at the top (`src/components/diagrams/Matrix.tsx:12-17,40-47,113-124`).
   The chapter assigns `growth can fit` to the bottom-right quadrant and highlights
   it, even though the y-axis labels that row `low capacity for loss`
   (`src/chapters/random-walk.mdx:138-150`). That directly contradicts the prose's
   requirement for a long horizon, a buffer, and the ability to absorb decline, and
   it visually recommends growth risk to the low-capacity case. Put the growth case
   in the high-capacity, need-later quadrant and make all four quadrant labels agree
   with their two axes.

4. **Keep Figure 59.4's meaning-bearing labels inside the Bars viewport.** `Bars`
   starts each value label at `trackX + trackW * value + 6` inside a 380-unit viewBox
   and does not wrap or end-anchor it
   (`src/components/diagrams/Bars.tsx:23-25,31-34,52-55`). With the chapter's values,
   `one outcome dominates` begins at about x=334 and extends well past x=450, while
   `several linked outcomes` begins at about x=281 and extends past x=415
   (`src/chapters/random-walk.mdx:114-123`). Both are clipped at every scale. Shorten
   or recompose the chapter-local bar labels so each complete claim remains visible
   without changing the shared component.

5. **Complete the registry record required for a finished chapter.** The
   `random-walk` entry stops at `status: "draft"` and omits the authoring contract's
   required `tier`, `thesis`, `framework`, and diagram-form inventory
   (`content/registry.json:1162-1170`). Populate those fields from the seed, brief,
   and the seven figures actually rendered before approval.

The remaining required audit is sound within the recorded evidence. The brief and
seed support the efficient-markets thesis and signature model. The page follows the
required section order, has six key ideas with captioned shared-vocabulary diagrams,
a Model figure, four concrete practice cards, an honest caveat, a generated
typographic cover, four related slugs that resolve to done chapters, and a direct
publisher link. The draft-linked S&P DJI page directly supports the reported 79%
2025 large-cap underperformance rate, and the linked SEC investor bulletin supports
the fees, trading-cost, and tracking-error discussion. Those two recorded links were
inspected directly; this review began no new external search.

`npm run check` passed on 2026-07-16 with the required filesystem access: queue and
registry validation, prose lint, 34 pipeline tests, 122 application tests, typecheck,
production build, and ESLint all passed. The initial sandboxed run failed only when
three launchd-supervisor tests were denied access to the keepalive path under
`Library/Application Support`; all three passed in the unrestricted rerun. Vitest
emitted only the existing non-failing jsdom `Window.scrollTo()` notices.

### ADVISORY

None.

## Builder resolution — 2026-07-16

Resolved every REQUIRED finding from critique round 1.

1. Rewrote the thesis opening to retain the market counterparty and competition point
   without claiming a seller saw identical information or held the opposite view. It now names
   cash needs, rebalancing, indexing, and mandate differences as possible reasons to sell.
2. Replaced the active-management ownership claim with the correct average-dollar arithmetic:
   active and corresponding passive market portfolios match before costs, while the active
   average trails after its additional research, trading, and advisory costs.
3. Moved the highlighted "growth can fit" case to the top-right Matrix quadrant, which is
   need-later and high-capacity-for-loss, and revised all quadrant notes to match their axes.
4. Replaced the clipped Bars end labels with the compact, complete labels "one bet," "linked
   bets," and "shared result," all of which fit the existing 380-unit viewport.
5. Completed the `random-walk` registry record with tier 2, the seed thesis, the Efficient
   markets framework, and the seven rendered diagram forms. Its status remains `draft`.

Verification: `npm run check` passed on 2026-07-16.

## Critique round 2 — 2026-07-16

### REQUIRED

1. **Make the signature Model diagram encode the claim in its caption.** Figure 59.7
   says that competition moves public information into prices while leaving low costs
   and diversification as the investor's controllable edges
   (`src/chapters/random-walk.mdx:195-213`), but the graph contains no node or edge for
   either low costs or diversification. It only draws public facts, analysis, trades,
   prices, and future returns. It also classifies `trades -> prices` as a
   `reinforcing` edge even though `NodeGraph` reserves that kind for a reinforcing
   relationship (`src/components/diagrams/NodeGraph.tsx:16-21,75-98`), and the page
   does not explain any positive feedback mechanism on that edge. Because this is the
   hero rendering of the book's signature model, the mismatch is substantive rather
   than caption polish. Either draw the controllable investor response that the
   caption and second Model paragraph promise, or narrow the caption and edge
   semantics so the figure accurately presents only the price-discovery system it
   actually contains.

The five REQUIRED findings from round 1 are resolved and remain resolved. The opening
now handles counterparties without imputing opposite beliefs, the active-management
arithmetic uses the correct average-dollar comparator, Figure 59.5 places the growth
case in the high-capacity and long-horizon quadrant, Figure 59.4's shortened end labels
fit the viewport, and the registry contains the required tier, thesis, framework, and
seven-form inventory.

The already-recorded S&P DJI and SEC links were inspected directly without beginning
a new external search. The S&P DJI page supports the 79% 2025 large-cap
underperformance statistic, and the SEC bulletin supports the page's discussion of
fund fees, trading costs, tracking error, and market risk. The publisher link resolves
to W. W. Norton's page for the book, and all four related slugs remain `done`.

`npm run check` passed on 2026-07-16 with the filesystem access required by the
launchd-supervisor tests: queue and registry validation, prose lint, 34 pipeline tests,
122 application tests, typecheck, production build, and ESLint all passed. The first
sandboxed attempt failed only because three supervisor tests could not write their
keepalive path under `Library/Application Support`; all three passed when rerun with
that access. Vitest emitted only the existing non-failing jsdom `Window.scrollTo()`
notices.

### ADVISORY

1. `ShelvedNearby` renders four relevant, completed books, but it does not state the
   one-clause relationship for any link that the authoring spec requests
   (`src/chapters/random-walk.mdx:264-268`). A short relationship note would make the
   cross-links more informative, but the rubric treats optional cross-link enrichment
   as advisory.

## Builder resolution — 2026-07-16

Resolved the remaining REQUIRED finding from critique round 2. Figure 59.7 now captions
only the price-discovery system it renders: public facts move through competing analysis and
trade into prices, and later returns inform subsequent analysis. The `trades -> prices` edge
remains labeled `price discovery` but is now neutral, so the diagram no longer asserts an
unexplained reinforcing relationship. The surrounding Model prose continues to state low costs
and diversification as the investor's controllable response without representing them as nodes
in this price-discovery figure.

Verification: `npm run check` passed on 2026-07-16.
