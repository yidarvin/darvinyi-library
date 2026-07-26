verdict: revise

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
