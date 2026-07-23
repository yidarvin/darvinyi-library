verdict: revise

## Critique round 1 — 2026-07-23

### Required

1. **Compress `The thesis` to the fixed one-or-two-sentence anatomy.** The dedicated
   thesis block at `src/chapters/difficult-conversations.mdx:13-18` contains four
   sentences. The authoring spec reserves this section for the compact argument a
   reader could carry away after reading nothing else. Preserve the three simultaneous
   concerns and the move from competing certainty to joint inquiry, but express them
   in no more than two sentences.

### Advisory

1. Figure 72.3 assigns `kind="reinforcing"` to the one-way `missed expectation →
   a change to test` edge at `src/chapters/difficult-conversations.mdx:96`. The shared
   `NodeGraph` contract reserves that kind for a reinforcing causal edge, while the
   prose describes learning from an outcome and the graph contains no feedback loop.
   A neutral labeled edge would avoid importing unsupported systems polarity; this is
   advisory because the visible `learn` label and accent do not overturn the figure's
   main multi-contribution lesson.

2. Re-derivation against the bounded repository evidence supports the central factual
   synthesis. The chapter brief and seed record identify what happened, feelings, and
   identity as the three simultaneous conversations, and the draft consistently
   develops impact versus intention, contribution rather than equalized blame,
   expressed feeling, and a non-binary identity stance. No separate chapter evidence
   dossier or source excerpts are recorded, so closer attribution and paraphrase
   comparison were not possible; this review began no external web search. The draft
   uses no quotation, real cover art, or apparent recreation of a source figure.

3. Apart from the required thesis-length defect, the fixed anatomy is complete and in
   order. Five key ideas each have a captioned vocabulary figure, the Model renders the
   brief's signature framework, four exercises produce concrete preparations, and the
   caveat keeps curiosity and contribution from excusing abuse or erasing
   accountability. The six-minute badge agrees with an approximately 1,129-word
   chapter-text count at 200 words per minute. All three related slugs resolve to
   `done` chapters, their relationships are stated in the preceding prose, and the
   outbound link is a direct Penguin Random House page.

4. The direct imports and their SVG helpers render coherently. The chapter-local
   minimum widths preserve the smallest meaningful labels at approximately 11 CSS
   pixels or larger inside `Figure`'s horizontal scroller on a phone. `npm run check`
   completed with `CHECK OK` on 2026-07-23: validation, prose lint, all pipeline
   tests, all 149 Vitest tests, TypeScript, the Vite production build, and ESLint
   passed. Vitest emitted only the existing non-failing jsdom `Window.scrollTo()`
   notices.
