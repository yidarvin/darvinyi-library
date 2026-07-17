verdict: revise

## Critique round 1 — 2026-07-16

### Required

1. **Figure 61.1 clips two of its three value labels.** `Bars` fixes its viewBox at 380 units and starts each unanchored `valueLabel` at `trackX + w + 6`. With the chapter's `value: 1`, “the whole amount” begins at x=346 and necessarily extends past the x=380 boundary; “fit life here” also begins near the right boundary for `value: 0.82`. The 380px minimum width prevents downscaling but cannot reveal content outside the SVG viewBox, so the first structural figure is not fully legible at any viewport. Revise the figure usage or geometry so every visible label remains inside the viewBox and readable at phone width.

2. **Figure 61.5 leaves half of its stated key idea undiagrammed.** The heading and second paragraph make increasing earning capacity a parallel part of the idea, and the recorded edition presents increasing one's ability to earn as one of its seven cures. The timeline and caption show only debt inventory, repayment, and redirected cash. They contain no skill, service, responsibility, or earnings path, so the visual does not encode the complete idea that the section asks the reader to learn. Split the two ideas and give each a structural figure, or use one in-vocabulary figure that clearly shows both debt reduction and earning-capacity growth.

### Advisory

1. **Separate the book's concrete saving rule from the page's modern adaptation.** The recorded edition prescribes retaining one coin in ten, while the prose says the percentage is less important and Figure 61.1 silently uses `0.18`. The transferable principle can reasonably be generalized for households with tight cash flow, but naming Clason's one-tenth rule before adapting it would make the distillation more exact and would avoid letting an arbitrary bar length stand in for the source's prescription.

2. **Figure 61.4 names its vertical scale backward.** The axis label is “size relative to your safety margin,” but the component receives `low: "large stake"` and `high: "small stake"`. The quadrant text makes the intended target recoverable, so this is not blocking, but relabeling the scale as safety remaining after the stake, or swapping the poles and quadrants, would make the axis internally consistent.

### Verification

`npm run check` passed on 2026-07-16 after rerunning with access to the launchd keepalive fixture: queue/registry/content validation, prose lint, 2 pipeline tests, 34 runner tests, 126 app tests, typecheck and production build, and ESLint all completed successfully. The initial sandboxed run failed only because three launchd tests could not write under `~/Library/Application Support`; the unrestricted rerun passed those same tests. Factual review used the chapter brief and the edition scan already linked in the draft; no new external search was begun.

## Builder resolution — 2026-07-16

- Reworked Figure 61.1 to label its three bars directly and removed the end-of-bar value captions that could extend beyond the `Bars` viewBox. The figure now states the recorded one-in-ten rule with a 0.10 retained bar, while the surrounding prose distinguishes that rule from a cash-flow-sensitive modern adaptation.
- Replaced Figure 61.5's debt-only timeline with an in-vocabulary `NodeGraph`. Its two explicit routes, a debt payment plan producing freed cash and skill or service practice producing earning power, converge on a future claim; the caption and accessible description state that relationship.
- Corrected Figure 61.4's vertical axis to run from a small stake to a large stake relative to the safety margin, reordered the quadrants to match that axis, and moved the highlighted manageable-start quadrant accordingly.

## Critique round 2 — 2026-07-16

### Required

1. **Figure 61.5 hides and reverses the two arrows that were meant to resolve the missing earning-capacity route.** The chapter places each horizontal pair of nodes only 85.8 SVG units apart (`x: 0.36` to `x: 0.66`), while `NodeGraph` draws 94-unit-wide node boxes and shortens each end of an edge by 50 units. The paired boxes therefore overlap by 8.2 units, and the computed debt-plan-to-freed-cash and skill-to-earning-power lines run backward from x=199.96 to x=185.76. Because edges and their labels render before the node rectangles, both short reversed lines and the “reduce” / “grow” labels are covered by those rectangles. The figure consequently does not visibly encode the two central transitions it claims to teach. Space the nodes far enough apart or choose geometry whose visible arrows run from each source to its target without overlapping boxes.

2. **The registry still records the replaced Figure 61.5 as a timeline.** `src/chapters/richest-man-babylon.mdx` now imports and renders `NodeGraph`, but the fifth entry in `content/registry.json` remains `"timeline"`. The authoring spec requires a complete diagram list, and the technical-integrity rubric requires the registry to agree with the files on disk. Update that entry to the actual in-vocabulary form when the figure is repaired.

### Advisory

None.

### Verification

`npm run check` passed on 2026-07-16 after rerunning with access to the launchd keepalive fixture: queue/registry/content validation, prose lint, 2 pipeline tests, 35 runner tests, 126 app tests, typecheck and production build, and ESLint all completed successfully. The initial sandboxed run failed only because three launchd tests could not write under `~/Library/Application Support`; the unrestricted rerun passed those same tests. Factual review used the chapter brief and the edition scan already recorded in the draft, which identifies the work, author, and 1926 date; no new external search was begun.
