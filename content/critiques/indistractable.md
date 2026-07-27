verdict: resolved

## Critique round 1 — 2026-07-27

### Required

1. **Restore the recorded contributor credit in the rendered book metadata.** The
   publisher evidence describes the 2019 book as “by Nir Eyal with Julie Li,” but the
   registry subtitle rendered by `<Hero>` says only `Nir Eyal · 2019`, and the outbound
   `buyLabel` likewise names only Nir Eyal. The mandatory author line and reader-facing
   book link therefore give incomplete attribution. Reconcile the registry/Hero byline
   and outbound label with the publisher record so Julie Li's credit is visible.

### Advisory

1. **State the relationship behind the nearby-book choices.** `make-time`,
   `deep-work`, and `atomic-habits` are valid built links, but the page supplies only
   cover tiles. The authoring spec asks each nearby link to be motivated in one clause;
   one short sentence before the footer could explain the three connections.

`npm run check` passed in full: validation, prose lint, pipeline tests, 228 chapter
tests, typecheck, production build, and lint.

## Builder resolution — 2026-07-27

- Restored the publisher-recorded contributor credit as `Nir Eyal with Julie Li` in the
  registry subtitle that `<Hero>` renders, the source metadata that regenerates it, the
  chapter brief, and the outbound bookseller label.
- Added a concise relationship sentence for Make Time, Deep Work, and Atomic Habits
  immediately before the Shelved Nearby footer.
