verdict: approve

## Critique round 1 — 2026-07-16

### Required

1. **The practice matrix highlights the wrong feedback condition.** In `src/chapters/range.mdx`, Figure 1.3 defines the top row as clear feedback and the bottom row as weak feedback, then places and highlights “adaptive practice” at index 3, the bottom-right cell. That makes the diagram say adaptive practice combines varied cases with weak feedback, contrary to the surrounding prose, the caption’s “realistic feedback,” and the cell’s own “select, test, revise” label. Put adaptive practice in the top-right cell and highlight that cell, then make the remaining quadrant labels and notes consistent with their axes.

2. **The outbound book link does not meet the page contract.** `ShelvedNearby` points to `https://davidepstein.com/range/`, an author site rather than the publisher or a bookseller required by `docs/authoring-spec.md` and the chapter brief. Replace it with a direct publisher or bookseller page for the book.

### Advisory

None.

## Builder resolution — 2026-07-16

- Moved “adaptive practice” to the matrix’s top-right quadrant, where varied cases meet clear feedback, and changed the highlight to quadrant `1`. Reworked the other three quadrant labels and notes so each now matches its feedback and variety conditions.
- Replaced the author-site outbound URL with the direct Penguin Random House product page for *Range*.

## Critique round 2 — 2026-07-16

### Required

The two findings from round 1 are resolved. The matrix now places and highlights adaptive practice in the top-right quadrant, and the outbound link is a direct Penguin Random House product page.

1. **Recompute the Hero reading-time badge from the rendered page.** A direct server render contains approximately 1,505 visible words, including the Hero, headings, captions, diagram labels, exercise titles, and generated component text. At the authoring spec's approximately 200 words per minute, rounded up, this is an eight-minute distillation, not `minutes={9}`.

2. **Figure 1.5 encodes unsupported causal signs and draws a return edge through the bridge it is supposed to explain.** The prose and caption describe specialists contributing evidence through a bridge to a shared problem. The graph instead marks `bridge -> problem` as reinforcing (`+`) and `problem -> field` as balancing (`−`), which says the bridge increases the problem and the problem suppresses field insight without any support in the text. Because `field`, `bridge`, and `problem` are vertically aligned, the long dashed return edge also overlaps the two shorter evidence paths and passes through the central bridge node. Redraw the graph with neutral, non-overlapping paths that represent the movement of evidence and questions described in the prose, or provide labels and geometry that make a different intended relationship explicit.

### Advisory

None.

## Builder resolution — 2026-07-16

- Changed the Hero badge from `9-min` to `8-min`, using the critique's recorded approximately 1,505 visible-word server render and the specified 200-words-per-minute rounding rule.
- Redrew Figure 1.5 with neutral, labeled arrows for evidence, constraints, conditions, framing, and questions. Repositioned the bridge and shared-problem nodes so the question path is diagonal and does not overlap the evidence paths or pass through the bridge. Removed the unsupported reinforcing and balancing signs.

## Critique round 3 — 2026-07-16

### Required

None. Both round 2 findings are resolved. The eight-minute badge matches the recorded rendered-word evidence, and Figure 1.5 now uses neutral, labeled, non-overlapping paths that match the prose. The round 1 matrix and publisher-link fixes also remain intact. The chapter follows the required anatomy, keeps the deliberately absent Model section consistent with the brief and registry, and passes `npm run check`.

### Advisory

None.
