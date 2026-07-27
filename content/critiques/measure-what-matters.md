verdict: revise

## Critique round 1 — 2026-07-27

### Required

1. Figure 113.1 passes the wrong unit to `Bars`, so the rendered magnitudes are false.
   `Bars` documents `value` as a number from 0 to 1 and clamps every input above 1 to
   1, but the chapter supplies 92, 71, 58, 28, and 20. All five bars therefore render
   at full length. Use fractional values or a categorical form that does not imply a
   magnitude; the current figure does not encode the tradeoff claimed by its caption.

2. Figure 113.2 does not agree with its own axes. The top row is the "clear"
   connection-to-objective row, yet its activity cell is labeled "busy, but detached"
   and "a task without a reason." The bottom-right cell is evidence with an "unclear"
   connection, yet it is labeled "a metric with a purpose." "Vague aspiration" also
   does not occupy a coherent position on the activity-to-evidence axis. Rebuild the
   quadrants so every label is a valid combination of the two stated dimensions.

3. Figure 113.3's node placement breaks its directed connections. Product and
   marketing sit only about 103 SVG units from customer adoption while each node is
   94 units wide; after `NodeGraph` adds its endpoint clearance, both horizontal edge
   segments reverse direction. The direct company-direction-to-support edge also runs
   behind the customer-adoption card. Reposition the nodes or choose another
   in-vocabulary form so all declared links are visibly distinct and point toward
   their actual targets.

4. The `measure-what-matters` registry record is incomplete under definition-of-done
   item 7. It has no `tier`, `thesis`, `framework`, or `diagrams` fields. Add metadata
   that agrees with the finished page and its six diagram forms.

5. The mandatory full gate is not green. `npm run check` reached the Vitest stage and
   failed `src/test/chapters.test.tsx` at `route /about` because the `// loading...`
   fallback did not clear within the test timeout (240 tests passed, 1 failed).
   The two targeted `measure-what-matters` render tests pass, so its imports do render,
   but the authoring contract still requires a clean complete `npm run check` before
   approval.

### Advisory

- None.
