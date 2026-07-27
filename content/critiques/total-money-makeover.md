verdict: approve

## Critique round 1 — 2026-07-27

### Required

1. The thesis section does not meet the fixed anatomy. `src/chapters/total-money-makeover.mdx:13-19` expands the thesis to six sentences that walk through the whole Baby Steps sequence, while `docs/authoring-spec.md` requires this section to compress the entire argument into one or two sentences. Reduce this section to the governing claim; the later sections already explain the sequence.

2. Figure 112.1 contradicts its accompanying explanation at a consequential point. The prose at lines 31-33 says essentials, every minimum debt payment, and the current priority are funded before discretionary spending, but the flow at lines 42-48 jumps from “cover essentials” to “fund the current priority.” That diagram can be read as sending money to the target before keeping the other required payments current. Make the structural diagram explicitly preserve minimum payments before the extra target payment.

3. The phone-width diagram requirement is not met. Both four-step `Flow` uses, figures 112.1 and 112.6, render a 558-unit viewBox as `w-full`; inside a padded figure on a 360px viewport, their 11.5-unit labels shrink to roughly 6px instead of scrolling or reflowing. Figure 112.2 also places the long, unwrapped endpoint labels “one surprise means borrowing” and “an interruption has a cash buffer” at the same vertical level, with the default “starter reserve” marker label only four units below them, so the three labels collide. Give these chapter diagrams a genuinely phone-legible layout and verify the labels without changing their meaning.

### Advisory

None.

## Builder resolution — 2026-07-27

- Reduced **The thesis** to two sentences that state the governing sequence and its
  behavior-first tradeoff, leaving the Baby Steps detail to the later sections.
- Corrected figure 112.1 to show `cover essentials → pay every minimum → fund the current
  priority`; its five-step flow now keeps the extra target payment structurally after every
  required debt payment.
- Made figures 112.1, 112.2, and 112.6 phone-legible by preserving their 696px, 380px, and
  558px diagram widths inside the figure's horizontal scroll container, rather than shrinking
  their labels.
- Added Spectrum's reusable stacked-endpoint layout and applied it to figure 112.2 with the
  starter-reserve marker placed above the endpoint labels. Added a regression test that checks
  the wrapped endpoint rows remain below the top marker label.

## Critique round 2 — 2026-07-27

### Required

None.

### Advisory

None.
