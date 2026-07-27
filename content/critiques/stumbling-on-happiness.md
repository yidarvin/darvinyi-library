verdict: approve

## Critique round 1 — 2026-07-27

### Required

1. Figure 105.3 encodes the opposite time course from the prose and caption. The x-axis
   is "time after the event," but `shape="peak"` rises from near zero for roughly the
   first 70 percent of the plot, labels that late maximum "initial peak," and then falls
   only slightly. The section says the reaction commands attention at first and fades as
   life resumes. Replace this with an in-vocabulary diagram whose visible curve begins
   high near the event and declines over time, with annotations placed on the curve.

2. Figure 105.5 does not match its own axes. `Matrix` orders its cells as top-left,
   top-right, bottom-left, bottom-right, while the vertical axis makes the top easy to
   try and the bottom hard to try. The draft therefore puts "run a small trial" in the
   hard-to-try/few-reports cell, "ask, then decide" in the easy-to-try/use-reports cell,
   and highlights "try and compare" as strongest in the hard-to-try cell. Reassign the
   recommendations and highlight so each quadrant teaches the decision rule stated by
   the two axes.

3. The registry entry at `content/registry.json:2075` is not complete enough for the
   authoring spec's definition of done. It has the base identity fields and `draft`
   status but omits `tier`, `thesis`, `framework`, and the six diagram-form entries.
   Populate those fields consistently with the brief and rendered chapter before this
   item can be approved.

### Advisory

- The surrogation evidence record supports another person's affective report as a
  useful corrective to event information. The stronger practice language about finding
  two or three people with matching constraints is a reasonable heuristic, but the
  recorded evidence does not establish that particular sampling rule. Present it as a
  practical check rather than an evidence-calibrated threshold, or add support during a
  future research pass.

## Builder resolution — 2026-07-27

- Replaced Figure 105.3's rising `peak` curve with the reusable `decay` annotated-curve
  variant. The visible line begins high immediately after the event, declines across
  time, and places the “initial reaction” and “life resumes” annotations on that line.
  Added `decay` to the Curve primitive's documented vocabulary options.
- Reassigned Figure 105.5 by `Matrix`'s documented reading order: small trial at
  easy-to-try/few-reports, try and compare at easy-to-try/use-reports, reversible
  commitment at hard-to-try/few-reports, and reports as a check at hard-to-try/use-reports.
  The highlighted strongest input is now the easy-to-try/use-reports quadrant.
- Completed the registry record with tier 3, the brief's thesis and affective-forecasting
  framework, and all six rendered diagram forms. Its status remains `draft`.
- Adjusted the lived-report exercise to describe seeking a few comparable people as a
  practical check, rather than presenting a two-or-three-person threshold as an
  evidence-calibrated rule.

## Critique round 2 — 2026-07-27

### Required

1. The impact-bias section still overstates the recorded result. The heading at
   `src/chapters/stumbling-on-happiness.mdx:68`, the claim that the feeling is expected
   to “remain as strong” at line 71, and the “permanent future” language at line 166
   say that people commonly forecast an unchanged or permanent reaction. The recorded
   Wilson and Gilbert evidence supports the narrower claim already stated at lines
   74–75 and 190–191: forecasts can overestimate intensity, duration, or both. It does
   not support permanence as the characteristic error. Calibrate those three passages
   to the documented overestimate so the reader learns impact bias rather than a
   stronger categorical claim.

### Advisory

None.

## Builder resolution — 2026-07-27

- Recast the impact-bias heading and explanation around the supported error: forecasts
  can overestimate a reaction's intensity, duration, or both. Removed the claim that
  people characteristically forecast an unchanged or permanent reaction.
- Rewrote the range-and-fade exercise so a single moment no longer becomes a
  “permanent future”; it now asks whether the feeling may dominate for longer than it
  will. Also softened the nearby “setback look permanent” wording for the same
  calibration.

## Critique round 3 — 2026-07-27

### Required

None. The current draft resolves the required findings from rounds 1 and 2.

### Advisory

None.
