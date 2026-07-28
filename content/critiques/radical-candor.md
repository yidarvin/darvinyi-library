verdict: revise

## Critique round 1 — 2026-07-27

### Required

1. Complete the `radical-candor` record in `content/registry.json`. It currently stops
   at the scaffold fields and omits `tier`, `thesis`, `framework`, and `diagrams`.
   Definition-of-done item 7 requires the complete registry metadata, and the diagram
   inventory should match the five key-idea forms plus the Model matrix. `npm run
   check` passes because the validator only requires `num`, `slug`, `title`, and
   `status`; that narrower mechanical check does not supersede the authoring contract.

### Advisory

1. The `ShelvedNearby` links resolve to done pages, but the rendered component shows
   only covers and cannot supply the one-clause relationship notes requested by the
   cross-linking spec. Add those notes when the shared component supports them; this
   does not make the present links dangling or misleading.
2. In the feedback-sequence figure, `highlight={2}` accents “act or explain” without
   the prose or caption identifying that stage as uniquely important. Either state why
   that is the hinge or leave the sequence visually neutral.
