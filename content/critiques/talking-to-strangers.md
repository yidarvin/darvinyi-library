verdict: revise

## Critique round 1 — 2026-07-27

### Required

1. **The Thesis section does not meet the fixed anatomy.** The authoring spec requires this section to compress the entire argument into one or two sentences. Here it runs for five sentences and mixes the thesis with explanation of ordinary social utility and consequential risk. Reduce this section to one or two sentences that carry the argument on their own; move any needed elaboration into Why It Matters or the relevant key idea.

2. **Every figure is numbered as if it belongs to the next registry item.** The registry assigns this chapter `num: 118`, and adjacent chapters use their registry number as the figure prefix, but this draft labels its figures `119.1` through `119.5`. That namespace belongs to the next queued item, `supercommunicators`. Rename these figure IDs to `118.1` through `118.5` so the rendered labels agree with the registry and surrounding chapters.

3. **Figure 119.1 does not encode the key distinction stated by its prose and caption.** The text argues for provisional trust that changes when evidence or stakes warrant verification, and the caption explicitly says higher stakes call for more checking. The graphic has no stakes, evidence, or updating dimension: it places one fixed “ordinary trust” marker on a credulity spectrum and turns the lesson into a generic middle position between hostility and unchecked acceptance. Revise the figure so a reader can see the conditional move from ordinary default trust to proportionate verification, rather than merely seeing that the midpoint is preferable.

### Advisory

1. In the conduct-and-setting graph, the `response → pressure` edge is styled as `reinforcing`, although the prose only claims that a response changes the next conditions and a response could escalate or reduce pressure. A neutral feedback edge, or a label that makes the depicted escalation case explicit, would keep the diagram from implying that every response amplifies pressure.

2. `npm run check` passed on 2026-07-27. Validation, prose lint, pipeline tests, 251 application tests, typecheck, production build, and lint were all green. The repeated `Window.scrollTo()` messages during Vitest were non-failing environment warnings.
