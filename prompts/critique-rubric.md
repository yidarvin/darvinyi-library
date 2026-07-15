# Critique rubric --- the library

The critic judges a distillation, not a book report. A required finding blocks approval;
an advisory finding does not.

## Required

1. **Copyright and sourcing.** The page uses original wording and original diagrams. It
   does not closely paraphrase, reproduce a book figure, or make an unsupported factual
   claim that changes the reader's understanding.
2. **Thesis and anatomy.** The thesis is clear; the page follows the authoring spec's
   required sections; every major idea has a structural diagram; the practice section is
   concrete; the caveat section is honest where the book needs one.
3. **Diagrams and interaction.** SVG figures encode the stated idea, use the shared
   vocabulary, remain legible on a phone, and match labels to the prose. A signature
   interaction, where present, teaches the idea rather than decorating it.
4. **Technical integrity.** `npm run check` passes. Imports render. Registry, queue,
   routes, and related links agree with the files on disk.

## Advisory

- Tighter prose, a stronger example, more precise captions, optional cross-links, and
  visual polish are advisory unless their absence makes a required point misleading.
- Do not reopen a settled finding without new evidence. Do not request stylistic churn.

## Verdict format

The first line is exactly one of:

```text
verdict: approve
verdict: revise
verdict: resolved
```

Each critic pass appends `## Critique round <N> — YYYY-MM-DD`, then `### Required`
and `### Advisory`. Builder resolutions append `## Builder resolution — YYYY-MM-DD`.
Never delete earlier rounds.
