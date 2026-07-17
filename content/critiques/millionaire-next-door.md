verdict: revise

## Critique round 1 — 2026-07-16

### Required

1. **Figure 60.4 turns a conceptual allocation into unsupported quantities.** The prose and caption describe current needs, future costs, and saving as parts of one income, but `Bars` renders the supplied values `0.72`, `0.40`, and `0.58` as relative magnitudes. Those invented proportions sum to 170 percent, have no support in the brief or recorded evidence, and visually imply a data claim the text does not make. The longest end label also runs beyond the component's 380-unit viewBox at this value. Replace this with an in-vocabulary diagram that shows roles or a valid allocation without fabricated magnitudes, with every label contained at phone width.

2. **Figure 60.6 does not encode the key idea stated by its caption or prose.** The caption promises a contrast between capability-building support and a recurring obligation, but the `ProcessLoop` shows only the positive sequence. Its highlighted closing edge specifically sends “more family latitude” back to “defined help,” which implies another cycle of aid and undercuts the section's warning about recurring rescue. Use an existing form such as comparison or branched flow to show both outcomes, or otherwise make the visual faithfully distinguish bounded help from dependency.

3. **The exact research description in the caveat is not independently supportable from the repository's evidence.** Lines 202–205 assert a 1995–1996 survey of “about 1,000 people” and attribute it to a contemporaneous University at Albany account, but the brief contains no survey details and there is no recorded evidence or source record for this chapter. The respondent population also matters: “people” is too vague to establish what sample the stated associations came from. Record a source that supports the dates, count, and population and state the population precisely, or remove the exact historical claim. This evidence cannot be supplied by a new critic search under the review constraint.

### Advisory

None.

### Verification

`npm run check` passed on 2026-07-16: queue/registry validation, prose lint, pipeline tests, app tests, typecheck and production build, and ESLint all completed successfully. The first sandboxed attempt could not access the launchd keepalive path; the required rerun with that filesystem access passed.
