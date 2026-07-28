verdict: approve

## Critique round 1 — 2026-07-28

### Required

1. **Recompute the Hero reading-time badge from the rendered page.** A direct server
   render contains approximately 1,445 visible words, including the Hero, headings,
   captions, diagram labels, exercise titles, and generated component text. At the
   authoring spec's approximately 200 words per minute, rounded up, this is an
   eight-minute distillation, not `minutes={7}` at
   `src/chapters/art-of-war.mdx:8`.

2. **Figure 136.2 asserts unsupported exponential cost growth.** The recorded
   “Waging War” evidence supports the burden of a prolonged campaign, retained
   capacity, and avoiding destructive victory. It does not establish that
   `capacity consumed` grows exponentially with `time in the contest`. Yet
   `shape="exp"` at `src/chapters/art-of-war.mdx:63` makes that quantitative shape
   the figure's central claim, while the surrounding prose only says that costs
   accumulate and options can shrink. Replace the exponential curve with an
   in-vocabulary visual that shows cumulative depletion or rising burden without an
   unsupported growth law, or record evidence and prose that genuinely support the
   stronger shape.

3. **The historical explanation for the book's survival is unsupported.**
   `src/chapters/art-of-war.mdx:19` says the book survives because it identifies
   people's tendency to substitute intensity for strategy. The recorded evidence
   establishes the received text, the relevant strategic passages, and a current
   edition, but it does not establish why the work persisted or became canonical.
   Recast this as a present-day relevance claim, or support the historical causal
   claim with recorded evidence.

### Advisory

None.

## Builder resolution — 2026-07-28

- Changed the Hero badge to `minutes={8}`, using the critique's recorded direct-render count of approximately 1,445 visible words and the specified 200 words per minute, rounded up.
- Replaced Figure 136.2's exponential `Curve` with the in-vocabulary `Flow` "enter the contest → spend time and resources → lose room for other needs." The revised figure has no quantitative axes or growth law and states the recorded evidence's supported burden and capacity tradeoff.
- Recast "Why it matters" as a present-day relevance claim. It no longer attributes the book's survival or canonical status to a historical cause.
- Updated the evidence attribution boundary and registry diagram inventory from annotated curve to flow so the chapter artifacts describe the rendered figure consistently.

## Critique round 2 — 2026-07-28

### Required

None.

### Advisory

None.
