verdict: revise

## Critique round 1 — 2026-07-17

### Required

1. **Correct Figure 67.2 and preserve what value innovation claims.** The matrix defines
   its horizontal axis as a weak-to-strong buyer reason and its vertical axis as a
   hard-to-sustain-to-workable cost structure, but the top-left cell is labeled
   `valuable, but costly` and the bottom-right cell `efficient, but unwanted`
   (`src/chapters/blue-ocean.mdx:57-83`). Those meanings belong on the opposite
   coordinates under the stated axes. More fundamentally, “workable” cost is weaker
   than the framework's simultaneous pursuit of increased buyer value and lower cost:
   a differentiated premium offer can be sustainable without breaking the value-cost
   tradeoff. Make the prose, axes, and all four quadrant labels agree on buyer value
   and cost position so the highlighted cell cannot classify an ordinary sustainable
   differentiation strategy as value innovation.

2. **Do not render eliminate, reduce, raise, and create as a four-stage process.**
   Figure 67.3 uses `Flow`, whose numbered boxes and directed arrows explicitly encode
   a sequence, even though the prose presents four peer questions whose answers work
   together (`src/chapters/blue-ocean.mdx:85-109`; `src/components/diagrams/Flow.tsx:13-17,43-55`).
   Nothing in the chapter establishes that a team must complete elimination before
   reduction, then raising, then creation. Use an in-vocabulary structure that shows
   the four simultaneous design choices without inventing an order, or explain and
   support a genuine sequence if one is intended.

3. **Make Figure 67.4's decisive transition visible and semantically neutral.** The
   `barrier` and `offer` node centers are only about 103 SVG units apart, while
   `NodeGraph` shortens a horizontal edge by 50 units at each end. That leaves roughly
   three units for the `shared barrier -> new offer` arrow, and the nine-character
   `remove it` label is drawn before the 94-unit node rectangles, so almost all of the
   transition is covered (`src/chapters/blue-ocean.mdx:125-143`;
   `src/components/diagrams/NodeGraph.tsx:51-113`). The same edge is marked
   `reinforcing`, although it is a one-way design action rather than a feedback link.
   Recompose or space the graph so the arrow and label visibly encode the claimed
   removal step, and use a neutral edge unless an actual reinforcing loop is shown.

4. **Compress “The thesis” to the specified one or two sentences.** The section is
   four sentences and expands into examples of feature, price, copying, and defensive
   spending (`src/chapters/blue-ocean.mdx:11-19`). The authoring contract reserves
   this block for the single compact argument a reader can carry away. Keep the useful
   detail elsewhere and make this section state the fixed-arena problem and the
   uncontested-demand alternative in no more than two sentences.

### Advisory

- None. The five key ideas, signature comparison, concrete practice cards, optional
  caveat, chapter-local mobile minimum widths, completed related links, and generated
  cover otherwise satisfy the structural contract. `npm run check` passed all six
  stages on 2026-07-17. The brief and seed metadata support the high-level thesis and
  red-ocean/blue-ocean model; no separate chapter-local evidence record was present,
  and no new external web search was begun for this review.
