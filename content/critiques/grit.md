verdict: approve

## Critique round 1 — 2026-07-16

### Required

1. **The thesis does not convey the thesis in the chapter brief.** The Hero and `The thesis` section (`src/chapters/grit.mdx:5-17`) recast the book as a sensible system for choosing and revising long-range goals, but they never state Duckworth's central predictive claim that sustained passion and perseverance can explain achievement beyond talent. The required thesis block is also three sentences rather than the specified one or two. State the book's actual claim explicitly and compactly, while retaining the later qualifications so it is not presented as a universal causal law.

2. **The empirical caveat contains consequential claims with no recorded support.** The statements about the original studies' explained variation and relationship to conscientiousness, the later meta-analysis, and Duckworth's restrictions on use of the self-report scale (`src/chapters/grit.mdx:200-207`) materially change how much confidence a reader should place in the model. None can be re-derived from `prompts/notes/grit.md`, and no chapter-specific evidence is recorded in the repository. Record and attribute the evidence used for these claims, or narrow the passage to claims supported by the available brief. This review did not begin a new external search.

3. **Figure 31.5 encodes the branch in the wrong place.** `Flow` branches only after its final step, so the current labels read: obstacle → name what changed → find a controllable move → either revise the route or abandon the aim (`src/chapters/grit.mdx:120-126`). That contradicts the caption and prose, which present abandoning the aim as the alternative to searching for a revised route. Restructure the steps/branch so the two outcomes actually diverge at the decision the prose describes.

4. **The `grit` registry entry is incomplete.** `content/registry.json:617-625` has only the base fields and `status: draft`; it lacks the required `tier`, `thesis`, `framework`, and `diagrams` metadata. Add values that agree with the final page before approval. The present `npm run check` passes because the validator does not enforce these definition-of-done fields for a draft.

### Advisory

1. Remove the unused `Compare` import at `src/chapters/grit.mdx:3` when revising the chapter.

2. Consider softening "Interest usually develops in stages" (`src/chapters/grit.mdx:32-33`). The sentence compresses encounter, practice, and contribution into a single developmental sequence without recorded support, while the rest of the section makes the safer and more useful point that durable interest often grows through repeated contact with real work.

`npm run check` passed on 2026-07-16: validation, prose lint, pipeline tests, 66 UI tests, typecheck/build, and lint all completed successfully.

## Builder resolution — 2026-07-16

- Rewrote the Hero and two-sentence thesis to state the recorded predictive claim explicitly, while retaining the non-causal qualification.
- Replaced the uncited empirical and measurement assertions in the caveat with a bounded use note grounded in the chapter brief's stated thesis and the page's route-revision model.
- Moved Figure 31.5's fork to the decision about whether the aim remains worth pursuing; its branches now lead to a search for a revised route or abandonment of the aim.
- Added the `tier`, `thesis`, `framework`, and full diagram list to the `grit` registry entry, and removed the unused `Compare` import. The interest-development wording now uses qualified language.

## Critique round 2 — 2026-07-16

### Required

None. The revised Hero and thesis now state the brief's predictive claim while preserving its non-causal boundary. The caveat no longer relies on the unsupported empirical and measurement assertions from round 1. Figure 31.5 now forks from the decision about whether the aim remains worth pursuing, and the registry metadata agrees with the seven rendered diagram forms. The remaining conceptual claims track the brief and the chapter's recorded framework where they can be re-derived locally; this review did not begin a new external search.

`npm run check` passed on 2026-07-16: validation, prose lint, pipeline tests, 66 UI tests, typecheck/build, and lint all completed successfully. The rendered page contains approximately 1,470 words, which supports the 8-minute badge at the specified 200 words per minute, rounded up.

### Advisory

None.
