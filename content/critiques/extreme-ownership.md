verdict: resolved

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
