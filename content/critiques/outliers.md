verdict: approve

## Critique round 1 — 2026-07-16

### Required

1. **The hero model invents an unsupported four-stage learning schedule.** In figure 34.6, the bars assign "build foundations," "find weak points," and "refine with feedback" to successive exact 2,500-hour blocks. The chapter brief supports the 10,000-hour rule as the signature model, while the recorded Ericsson evidence supports deliberate practice and explicitly does not establish a universal threshold or fixed progression. These quarter-by-quarter stages are presented as if the number carries a developmental sequence, which conflicts with the prose's own warning that it is "a slogan, not a rule." Replace the fabricated hour bands with an original diagram that shows long accumulation without assigning unsupported milestones, or clearly encode task quality, feedback, and access as independent conditions rather than timed phases.

2. **The signature bars do not keep their explanatory labels inside the graphic.** `Bars` places each `valueLabel` after the bar endpoint inside a 380-unit viewBox. With the values used here, "refine with feedback" begins near the right edge and "a slogan, not a rule" begins at the full-width endpoint, so the most important caveat extends beyond the SVG's drawable width and can be clipped. Rework the composition or label placement so every model label is fully visible at the required phone width.

### Advisory

1. Figure 34.2 uses a strictly sequential timeline for a claim about overlap between formative years and the opening of a field. A future polish pass could show those windows overlapping, which would match the caption's "meets" relationship more precisely than four successive stages.

## Builder resolution — 2026-07-16

- Replaced Figure 34.6's four fabricated 2,500-hour phases and fixed 10,000-hour endpoint with an in-vocabulary Venn model. It now presents long-term practice, specific challenge and feedback, and access, recovery, and resources as independent conditions for development.
- Removed the `Bars` composition and its endpoint labels entirely. The replacement uses wrapped labels positioned within a responsive 380-unit SVG, so no model label extends beyond the drawable area at phone width.
- Updated the Outliers registry diagram inventory from `bars with flow` to `venn`; the chapter remains `draft`.
- Verified with `npm run check` on 2026-07-16: validation, prose lint, pipeline tests, 72 unit tests, production build, and lint all passed.

## Critique round 2 — 2026-07-16

### Required

None. Figure 34.6 now encodes long-term practice, specific challenge and feedback, and access, recovery, and resources as independent conditions for development. It no longer invents timed learning phases or places explanatory labels beyond the SVG bounds. The chapter states the ten-thousand-hour idea as a memorable slogan, then clearly limits it in the model prose and the sourced caveat. The full mechanical gate passes.

### Advisory

No new advisory findings.
