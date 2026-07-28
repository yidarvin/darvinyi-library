verdict: resolved

## Critique round 1 — 2026-07-27

### Required

1. **The Thesis section does not meet the fixed anatomy.** The authoring spec requires this section to compress the entire argument into one or two sentences. Here it runs for five sentences and mixes the thesis with explanation of ordinary social utility and consequential risk. Reduce this section to one or two sentences that carry the argument on their own; move any needed elaboration into Why It Matters or the relevant key idea.

2. **Every figure is numbered as if it belongs to the next registry item.** The registry assigns this chapter `num: 118`, and adjacent chapters use their registry number as the figure prefix, but this draft labels its figures `119.1` through `119.5`. That namespace belongs to the next queued item, `supercommunicators`. Rename these figure IDs to `118.1` through `118.5` so the rendered labels agree with the registry and surrounding chapters.

3. **Figure 119.1 does not encode the key distinction stated by its prose and caption.** The text argues for provisional trust that changes when evidence or stakes warrant verification, and the caption explicitly says higher stakes call for more checking. The graphic has no stakes, evidence, or updating dimension: it places one fixed “ordinary trust” marker on a credulity spectrum and turns the lesson into a generic middle position between hostility and unchecked acceptance. Revise the figure so a reader can see the conditional move from ordinary default trust to proportionate verification, rather than merely seeing that the midpoint is preferable.

### Advisory

1. In the conduct-and-setting graph, the `response → pressure` edge is styled as `reinforcing`, although the prose only claims that a response changes the next conditions and a response could escalate or reduce pressure. A neutral feedback edge, or a label that makes the depicted escalation case explicit, would keep the diagram from implying that every response amplifies pressure.

2. `npm run check` passed on 2026-07-27. Validation, prose lint, pipeline tests, 251 application tests, typecheck, production build, and lint were all green. The repeated `Window.scrollTo()` messages during Vitest were non-failing environment warnings.

## Builder resolution — 2026-07-27

Resolved all required findings. The Thesis now contains two sentences that state the full argument, with the practical consequences left in the surrounding sections. Renamed the five figures from `119.1`–`119.5` to `118.1`–`118.5`, matching this chapter's registry number. Reworked Figure 118.1 so its spectrum runs from routine, reversible choices to high-consequence decisions: it starts with provisional trust, names discrepant evidence as the updating trigger, and ends with independent verification before action. Also addressed the advisory feedback in Figure 118.4 by making the response-to-pressure edge neutral and labeling it as a change to the next conditions rather than an inevitable reinforcing loop.

## Critique round 2 — 2026-07-27

### Required

1. **Figure 118.1 still does not encode the two independent triggers stated by its prose and caption.** The revised spectrum uses consequence as its axis, but places “new discrepancy or evidence” in the middle of that same axis. This makes conflicting evidence look like an intermediate level of consequence and implies that it is absent from routine and high-consequence decisions. The chapter instead says either conflicting evidence or rising stakes can trigger a move from provisional trust to verification. Revise the figure so evidence and stakes are represented as separate reasons to update the decision process.

2. **Figure 118.1's endpoint labels collide.** `Spectrum` renders inline endpoints as unwrapped text at the same height. At the component's 380-unit viewBox, “routine, reversible choice” extends rightward from `x=40` while “high-consequence decision” extends leftward from `x=340`, causing substantial overlap near the center. This makes the first key-idea diagram illegible, including in its phone-width scrolling presentation. Use the primitive's long-label layout or otherwise shorten and place the labels without collision.

### Advisory

1. `npm run check` passed on 2026-07-27. Queue and registry validation, prose lint, 42 pipeline tests, 251 application tests, typecheck, production build, and lint were all green. The repeated `Window.scrollTo()` messages during Vitest were non-failing environment warnings.

## Builder resolution — 2026-07-27

Resolved the two outstanding Figure 118.1 findings while preserving the earlier thesis,
figure-number, and neutral-feedback fixes. Replaced the one-dimensional Spectrum with the
registered two-by-two Matrix form: its horizontal axis is evidence from no conflict to
conflicting evidence, and its vertical axis is decision stakes from reversible to hard to undo.
The ordinary, reversible, no-conflict quadrant now names provisional trust; each of the other
three quadrants shows the additional checking warranted by either trigger or both together.
This removes the false implication that evidence is a middle level of consequence and avoids
the former inline endpoint-label collision. Updated the key-idea prose, caption, registry diagram
record, and evidence note to describe the same two independent triggers. `npm run check` passed;
the chapter remains draft and no status transition was made.

## Critique round 3 — 2026-07-27

### Required

1. **Figure 118.1 assigns two explanations to the wrong quadrants.** `Matrix` consumes
   its cells in top-left, top-right, bottom-left, bottom-right order. The top-left cell
   is therefore high stakes with no conflicting evidence, yet its note says “a
   discrepancy merits a check.” The bottom-right cell is reversible with conflicting
   evidence, yet its note says “high stakes need safeguards.” The prescriptions are
   consequently crossed across the two axes the prior resolution was meant to separate.
   Make each cell's title and note describe its actual evidence-and-stakes combination.

2. **Figure 118.4's feedback-edge label is not legible.** The horizontal
   `response → pressure` edge has only about 100 viewBox units between the two 94-unit
   node cards, but centers the 23-character label “changes next conditions” in that gap
   at 12px monospace. The label extends behind both endpoint cards, which render after
   the edges and cover both ends of the text. Shorten, wrap, or reposition the label so
   the full relationship remains visible at phone width.

### Advisory

1. `npm run check` passed on 2026-07-27. Queue and registry validation, prose lint,
42 pipeline tests, 251 application tests, typecheck, production build, and lint were
all green. The repeated `Window.scrollTo()` messages during Vitest were non-failing
environment warnings.

## Builder resolution — 2026-07-27

Resolved both round-3 required findings while preserving the earlier thesis, figure-number,
two-trigger matrix, and neutral-feedback fixes. Figure 118.1 now follows the Matrix reading
order: its top-left high-stakes/no-conflict cell calls for an independent check, its top-right
high-stakes/conflicting-evidence cell calls for verification before acting, its bottom-left
reversible/no-conflict cell keeps provisional trust, and its bottom-right reversible/conflicting-
evidence cell says to look again. Figure 118.4 now uses the shorter neutral relationship label
"sets next pressure" and moves it above the horizontal edge with a vertical label offset, so the
entire label clears both endpoint cards at phone width. `npm run check` passed; the chapter
remains draft and no status transition was made.
