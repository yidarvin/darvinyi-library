verdict: resolved

## Critique round 1 — 2026-07-28

### Required

1. The Model figure does not encode the model described by its prose and caption. The prose says the action happens now inside conditions that extend outward across timescales, and the caption likewise places behavior inside those conditions. The `Concentric` instance instead passes `externalLabel="a behavior happens now"`, whose component explicitly renders that label outside the rings, while the core is labeled “neural activity, seconds.” As rendered and exposed to assistive technology, the figure says the behavior is outside the causal layers. Revise the hero diagram so the behavior and nested timescales have the same spatial relationship in the visual, caption, and explanation.

2. The `behave` registry entry is incomplete for a done chapter. It contains the identity fields and `status`, but omits the brief's tier plus the authoring spec's required `thesis`, `framework`, and `diagrams` metadata. Populate those fields with values that agree with the finished page before approval.

### Advisory

None. `npm run check` passed on 2026-07-28.

## Builder resolution — 2026-07-28

- Revised the Model figure so “a behavior, now” is the innermost ring, surrounded in order by neural activity, body and recent state, development and culture, and evolutionary history. The visual, caption, prose, and accessible ring order now all place behavior inside its causal conditions.
- Completed the `behave` registry entry with tier 3, the brief-aligned thesis, the nested-timescales framework description, and the six diagram forms used on the finished page. The chapter remains `draft` and is not marked done.
