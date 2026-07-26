verdict: resolved

## Critique round 1 — 2026-07-26

### Required

1. **The Hero omits two credited authors.** `Hero` derives its byline from the
   registry, which currently renders `Hans Rosling · 2018`, while the chapter's own
   publisher-backed purchase label credits Hans Rosling, Ola Rosling, and Anna
   Rosling Rönnlund. The recorded evidence says the publisher page confirms that
   author credit. Credit the work consistently in the Hero and registry, including
   Ola Rosling and Anna Rosling Rönnlund.

2. **Figure 86.3 does not match the population claim it illustrates.** The prose
   reports the UN projection that global population will peak around the middle of
   the 2080s, but the plotted `shape="s"` curve labeled `total population` only
   rises and approaches a plateau. It never peaks or reverses, even though the
   caption explicitly includes reversal. This changes the visual meaning of the
   sourced projection. Either make the plot a clearly generic illustration without
   a total-population axis, or use an original in-vocabulary visual that actually
   represents a peak and subsequent change.

3. **Figure 86.4 encodes unsupported magnitudes and does not show the stated
   operation.** The four arbitrary bar values compare a raw count, a per-person
   rate, a share, and a trend as though those unlike quantities had meaningful
   relative sizes. No evidence supports the 0.90, 0.52, 0.31, and 0.68
   relationships. The caption says one count becomes interpretable as context is
   added, but the figure neither preserves one count nor shows that transformation.
   Replace it with a structural in-vocabulary diagram that shows how comparison,
   division, and trend contextualize a number, or use one sourced example with
   commensurable magnitudes.

4. **The `factfulness` registry entry is incomplete under definition-of-done item
   7.** It has no `tier`, `thesis`, `framework`, or `diagrams` fields, unlike the
   completed chapter records. Populate the tier from the brief, record the chapter's
   thesis and ten-instinct framework, and inventory all six diagram forms. The
   current validator does not enforce these metadata fields, so `npm run check`
   passing does not satisfy this contract item.

### Advisory

None.

## Builder resolution — 2026-07-26

1. Corrected the credited author line everywhere this book's metadata is maintained:
   the registry subtitle now supplies the Hero byline as Hans Rosling, Ola Rosling, and
   Anna Rosling Rönnlund; the brief and `_books.py` source metadata match it; and the
   existing publisher evidence now records the full credit explicitly.

2. Replaced Figure 86.3's S-curve with the reusable annotated-curve `peak` variant.
   Its labels show slowing growth, the recorded UN projection of a mid-2080s peak, and
   the subsequent modest decline. The caption identifies it as an illustrative
   trajectory rather than a data plot. The vocabulary now documents the new variant.

3. Replaced Figure 86.4's arbitrary magnitude bars with an in-vocabulary flow. It
   keeps one reported count intact and shows the actual contextualizing operations:
   compare another case, divide by the relevant denominator, then check the trend and
   largest contributors. The wide intrinsic flow is preserved by the figure's mobile
   overflow wrapper rather than shrinking its labels.

4. Completed the draft registry entry with the brief-supported tier, thesis, ten-
   instincts framework, and the six rendered diagram forms in page order: spectrum,
   iceberg, annotated curve, flow, node graph, and comparison. The chapter remains
   `draft`; it has not been marked done.
