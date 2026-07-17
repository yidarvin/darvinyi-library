verdict: revise

## Critique round 1 — 2026-07-17

### REQUIRED

1. **Compress The thesis to the required one or two sentences.** The fixed anatomy
   defines this block as the compact argument a reader can carry away, but the draft
   uses six sentences (`src/chapters/extreme-ownership.mdx:14-21`). The section is
   directionally consistent with the brief, yet it expands into boundaries and
   organizational propagation rather than meeting the specified thesis form. Retain
   the core chain from responsibility, through influence, to coordinated action in no
   more than two sentences.

2. **Replace Figure 69.4 with a diagram that actually encodes mutual support across
   teams.** `Concentric` is the shared vocabulary form for a center with successive
   layers. Here it renders one `team priorities` ring and one `local tasks` ring around
   a `shared outcome` (`src/chapters/extreme-ownership.mdx:123-145`), so it shows nested
   alignment. The section and caption instead teach multiple teams, visible
   dependencies, handoffs, conflict resolution, and lending capacity. No separate
   teams, dependency, handoff, or movement toward the shared outcome appears in the
   figure. Use an in-vocabulary form and chapter-local labels/connections that make the
   stated coordination structure visible, then keep the caption aligned with what the
   figure shows.

3. **Recompute the Hero reading-time badge from the rendered page.** A direct static
   render of this exact draft contains 2,006 reader-visible alphanumeric tokens,
   including the Hero and cover metadata, headings, prose, captions, SVG labels,
   exercise titles, callout, and nearby-book footer. At approximately 200 words per
   minute, rounded up, the current page is an 11-minute distillation, not
   `minutes={9}` (`src/chapters/extreme-ownership.mdx:8-12`). Recount after the required
   prose and figure revisions and set the final badge from that render.

4. **Replace the outbound URL with a qualifying publisher or bookseller page.** The
   current `buyUrl` points to Echelon Front's `what-is-extreme-ownership` explainer
   (`src/chapters/extreme-ownership.mdx:264-268`). Echelon Front is the authors'
   leadership company, and this URL is not a direct publisher or bookseller page for
   the book. The fixed anatomy and chapter brief require the footer link itself to
   send a reader to a publisher or bookseller.

The chapter brief and seed record support the core total-responsibility thesis and the
presence of an Extreme Ownership signature model. No separate chapter-specific
evidence dossier or source excerpt exists in the repository, so factual and
close-paraphrase review was bounded to those records and internal agreement among the
prose, captions, and figures; this review began no external web search. Within that
boundary, the draft otherwise uses original thematic prose, no quotation or real cover
art, six key ideas with captioned shared-vocabulary figures, a captioned signature
model, four concrete exercises, and an honest caveat. The registry metadata is
complete, and all three related slugs resolve to done chapters with relationship
clauses.

`npm run check` passed on 2026-07-17: queue/registry/content validation, prose lint, 2
pipeline tests, 37 runner tests, 142 application tests, TypeScript, the production
build, and ESLint all completed successfully. Vitest emitted only the existing
non-failing jsdom `Window.scrollTo()` notices. The gate does not enforce the thesis
sentence limit, judge diagram-to-prose semantics, recompute reading time, or classify
an outbound vendor.

### ADVISORY

None.

## Builder resolution — 2026-07-17

1. Rewrote **The thesis** as two sentences that retain the responsibility → influence →
   coordinated-action chain, without expanding into the section's supporting boundaries.
2. Replaced Figure 69.4's nested `Concentric` rings with a `NodeGraph` showing separate sales,
   delivery, and support teams, labeled feasible-promise and handoff dependencies, and a
   customer-result connection to the shared outcome. The caption now describes that visible
   sequence.
3. Rendered the revised chapter and counted 1,968 reader-visible alphanumeric tokens, including
   Hero and footer content, headings, figure labels and captions, exercises, and the callout.
   At 200 words per minute, rounded up, the Hero badge is now `10-min distillation`.
4. Replaced the Echelon Front explainer URL with Macmillan's publisher page for the book:
   `https://us.macmillan.com/books/9781250067050/extremeownership`.

`npm run check` was invoked on 2026-07-17. The terminal ended its foreground run during the
unrelated runner regression test `test_interrupted_validation_keeps_the_transaction_restartable`,
before the suite could report a final result. The individual chapter-relevant gates passed:
queue/registry validation, prose lint, the direct `extreme-ownership` MDX render test, production
build, and ESLint.

## Critique round 2 — 2026-07-17

### REQUIRED

1. **Update the registry diagram inventory to match the revised Figure 69.4.** The
   builder replaced that figure with a second `NodeGraph`, and the chapter now renders
   the forms `iceberg`, `node graph`, `comparison`, `node graph`, `flow`, `pyramid`,
   and `process loop` (`src/chapters/extreme-ownership.mdx:6,48,72,107,137,169,191,213`).
   The registry still records the fourth form as `concentric circles`
   (`content/registry.json:1376-1384`). Technical integrity requires the registry's
   diagram list to agree with the chapter on disk. Replace that stale entry with
   `node graph`; do not change the revised figure back.

The four round 1 findings are otherwise resolved. The thesis is two sentences, Figure
69.4 now encodes distinct teams and labeled handoffs, the Hero shows the builder's
recomputed 10-minute badge, and the footer links to Macmillan's page for the book. The
chapter brief and seed record remain the only recorded source evidence in the repository;
no chapter-specific evidence dossier or source excerpt was found, and this round began no
external web search. Within that evidence boundary, no new copyright, factual, anatomy,
practice, caveat, figure-semantics, mobile-legibility, import, route, or related-link defect
was found.

`npm run check` passed on 2026-07-17: queue/registry/content validation, prose lint, 2
pipeline tests, 37 runner tests, 142 application tests, TypeScript, production build, and
ESLint all completed successfully. Vitest emitted only the existing non-failing jsdom
`Window.scrollTo()` notices. The validator does not compare the registry's diagram names
with the component forms rendered by the MDX chapter, so this stale inventory survives the
mechanical gate.

### ADVISORY

None.

## Builder resolution — 2026-07-17 (round 2)

1. Updated the fourth diagram inventory entry in the `extreme-ownership` registry record from
   `concentric circles` to `node graph`. It now matches Figure 69.4's rendered `NodeGraph` and
   the chapter's complete form sequence: iceberg, node graph, comparison, node graph, flow,
   pyramid, and process loop.
2. Preserved the round 1 fixes: the two-sentence thesis, the coordination network in Figure
   69.4, the 10-minute Hero badge, and the Macmillan publisher link.
3. Ran `npm run check` on 2026-07-17. Queue/registry/content validation and prose lint passed;
   the foreground terminal was interrupted during the existing runner regression test
   `test_interrupted_validation_keeps_the_transaction_restartable` before the suite reported a
   final result. No chapter-specific gate reported a failure.

## Critique round 3 — 2026-07-17

### REQUIRED

1. **Make Figure 69.4's two team-to-team handoffs visible rather than placing them
   underneath the nodes.** The replacement graph puts sales, delivery, and support at
   normalized x positions `0.16`, `0.5`, and `0.84`
   (`src/chapters/extreme-ownership.mdx:136-150`). Under `NodeGraph`'s placement math,
   sales and delivery therefore have centers at x=92.76 and x=190; their 94-pixel
   node rectangles end and begin at x=139.76 and x=143, leaving only a 3.24-pixel
   horizontal seam. Delivery and support have the same geometry. The component then
   centers each edge label in that seam, shortens both ends of the connector, and
   renders all opaque node rectangles after the edges and labels
   (`src/components/diagrams/NodeGraph.tsx:39-51,68-122`). Consequently, the later
   rectangles cover substantial portions of `feasible promise` and `handoff`, as well
   as the connectors and arrowheads. The figure still does not visibly teach the two
   dependencies that justified replacing the original concentric diagram. Space the
   nodes far enough apart, or use another in-vocabulary layout, so both directional
   handoffs and their labels remain unobscured at phone width.

The round 2 registry correction is resolved, and the other round 1 fixes remain in
place: the thesis is two sentences, the Hero badge is 10 minutes, and the footer uses
Macmillan's publisher page. The chapter brief and seed record remain the only recorded
source evidence in the repository; no chapter-specific evidence dossier or excerpt was
found, and this review began no external web search. Factual and close-paraphrase review
was therefore bounded to those records and internal agreement among the chapter,
captions, diagrams, and metadata. A browser-backed screenshot was unavailable in this
session, so the Figure 69.4 finding is based on the component's deterministic SVG
coordinates and paint order, not a claimed screenshot observation.

`npm run check` passed in full on 2026-07-17: queue/registry/content validation, prose
lint, 2 pipeline tests, 37 runner tests, 142 application tests, TypeScript, production
build, and ESLint all completed successfully. Vitest emitted only the existing
non-failing jsdom `Window.scrollTo()` notices. The mechanical gate renders the chapter
but does not test SVG label occlusion or connector visibility.

### ADVISORY

None.
