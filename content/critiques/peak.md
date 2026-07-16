verdict: approve

## Critique round 1 — 2026-07-16

### Required

1. **The page collapses purposeful practice into deliberate practice.** The thesis and Model sections define deliberate practice as a narrow stretch task performed with attention, feedback, and correction, while the coaching section says rubrics, answer keys, recordings, peer review, and tests can borrow the coach's function. In *Peak*, those broadly transferable features describe purposeful practice. Deliberate practice is the narrower case: work in a well-developed field, informed by established effective training methods and ordinarily designed by a teacher or coach who knows how expert performance develops. The caveat says the model is strongest where standards and repeatable components exist, but it never names this distinction, so the page teaches a broader signature framework than the book does. Distinguish the two forms explicitly, limit “deliberate practice” to its domain and instructional conditions, and present purposeful practice as the fallback when those conditions do not exist.

2. **Figure 42.2 contradicts its prose and axes.** The chapter labels the horizontal axis “difficulty of the task” and the vertical axis “attention available for learning,” but `Curve shape="channel"` is a flow-channel graphic that hard-codes “anxiety” at the upper left, “boredom” at the lower right, and “flow” on a rising diagonal band. With this chapter's axes, that places anxiety at low difficulty with high available attention and boredom at high difficulty with low available attention. It also implies that the useful amount of attention rises continuously with difficulty instead of showing the prose's easy, demanding-but-reachable, and overloaded regions. Replace this with an in-vocabulary composition whose geometry and labels actually encode the stated moving edge, or use the channel only with the challenge-versus-skill semantics it implements.

3. **The `peak` registry entry is incomplete for a done page.** `content/registry.json` currently stops at `num`, `slug`, `title`, `subtitle`, `part`, `routes`, and `status`; it has no `tier`, `thesis`, `framework`, or `diagrams`. Definition-of-done item 7 requires all of that metadata, including the diagram forms actually used by the chapter. `npm run check` currently passes despite the omission, so the green mechanical gate does not resolve this contract failure. Complete the entry before approval.

### Advisory

1. Figure 42.6 uses a `NodeGraph` as a four-step cycle, but the return edge crosses the attempt-to-feedback edge and places “more precise next target” on the crossing. Three edges are also marked `reinforcing`, which renders unexplained plus signs even though the prose does not describe signed causal polarity. A non-crossing loop or a cleaner node arrangement would make the signature model read faster and reserve the plus notation for a relationship the prose explains.

2. Add explicit `ariaLabel` text to figures 42.2 and 42.6. The curve's default label is only “A conceptual channel curve,” and the node graph's default names the nodes without communicating their directed loop, so neither alternative description carries the lesson available visually.

3. The caveat makes a specific interpretive claim about the 1993 Ericsson, Krampe, and Tesch-Römer account but gives the reader no source link. Linking the already recorded paper, as the Outliers chapter does, would make this otherwise useful note easier to verify.

## Builder resolution — 2026-07-16

Resolved all required findings in `src/chapters/peak.mdx` and `content/registry.json`.

1. The Thesis, coaching key idea, Model, and caveat now distinguish purposeful practice from deliberate practice. Purposeful practice names the transferable cycle of a specific target, attention, feedback, and revision. Deliberate practice is limited to its narrower conditions: a well-developed field, established effective training methods, and ordinarily a teacher or coach who can adapt them. The page presents purposeful practice as the accurate fallback where those conditions are absent.
2. Figure 42.2 now uses the in-vocabulary `Spectrum` form rather than the flow-channel curve. Its ordered zones show easy repetition, the demanding-but-reachable moving edge, and overload, with an explicit alternative description that states the learning consequence of each region.
3. The `peak` registry entry now includes tier, a chapter-consistent thesis, framework description, and the five diagram forms used on the page. Its status remains `draft`.
4. Figure 42.6 now uses a non-crossing `ProcessLoop` for the directed deliberate-practice cycle, removes unexplained signed edges, and has an explicit alternative description. The caveat now links the already recorded 1993 Ericsson, Krampe, and Tesch-Römer paper.
5. `npm run check` passed after the changes: queue and registry validation, prose lint, pipeline tests, Vitest, typecheck, and production build.

## Critique round 2 — 2026-07-16

### Required

None. The draft now distinguishes purposeful practice from the narrower conditions of deliberate practice, and that distinction is consistent across the thesis, coaching discussion, Model, caveat, and registry metadata. Figure 42.2 accurately encodes the moving difficulty edge as a spectrum, figure 42.6 presents a legible directed loop with an explicit alternative description, all six figures use shared vocabulary components inside captioned `Figure` wrappers, the practice cards are concrete, related links resolve, and the full mechanical gate passes.

### Advisory

None.
