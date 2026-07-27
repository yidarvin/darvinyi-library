verdict: resolved

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

## Builder resolution — 2026-07-27

- Corrected Figure 113.1 to pass `Bars` fractional magnitudes (`0.92`, `0.71`,
  `0.58`, `0.28`, and `0.20`), so the visible bar lengths now encode the stated
  priority tradeoff.
- Rebuilt Figure 113.2's four labels around its declared axes: clear activity is
  purposeful activity, clear evidence is a useful key result, unclear activity is
  busy but detached, and unclear evidence is an orphan metric.
- Repositioned Figure 113.3 into a sparse, non-overlapping goal network. Every
  directed edge now has positive clearance from its source and target cards, and
  the company-direction-to-support connection no longer crosses the customer card.
- Completed the registry record with tier, thesis, framework, and the six diagram
  forms used on the finished page. The chapter remains `draft`; this resolution does
  not mark it done.
- Ran the mandatory full `npm run check` gate after the corrections; it passes.

## Critique round 2 — 2026-07-27

### Required

1. Figure 113.5 gives the committed-versus-aspirational distinction the wrong
   structure. The chapter prose describes two explicitly labeled goal types, and the
   recorded evidence likewise distinguishes goals requiring dependable delivery from
   goals intended to stretch a team. `Spectrum` is reserved for matters of degree,
   but this figure places the two types at opposite ends of one scale and adds an
   unsupported `0.72` marker. That presentation tells the reader an OKR occupies a
   position between committed and aspirational, rather than requiring an honest
   choice of type. Use an in-vocabulary categorical form, such as `Compare`, that
   preserves the distinction, and keep the registry diagram list in agreement.

### Advisory

- None.

## Builder resolution — 2026-07-27

- Replaced Figure 113.5's `Spectrum` with the in-vocabulary `Compare` form. The
  figure now presents committed and aspirational results as two explicitly labeled
  goal types, with no continuum or unsupported numerical marker.
- Updated the registry diagram list from `spectrum` to `comparison` so it matches
  the six forms rendered by the chapter. The chapter remains `draft`; this
  resolution does not mark it done.
