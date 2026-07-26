verdict: approve

## Critique round 1 — 2026-07-26

### Required

1. Figure 81.5 does not encode the feedback loop its section teaches. The prose says
   that changed behavior produces the next round of data, and the caption says the
   process acts repeatedly, but `src/chapters/homo-deus.mdx:127-131` uses the
   one-way `Flow` form and stops at "change conditions." Replace it with an
   in-vocabulary loop form, or otherwise make the return from changed conditions to
   collected signals explicit. Until then, the major-idea diagram contradicts the
   prose and fails the diagram rubric.

2. The `homo-deus` registry record is incomplete. At
   `content/registry.json:1603-1611` it ends after `status` and omits the required
   `tier`, `thesis`, `framework`, and `diagrams` fields. Populate them, including an
   accurate list of the forms actually rendered after the feedback-loop correction.
   The authoring spec's definition of done requires this metadata even though the
   current mechanical validator accepts the draft without it.

3. The outbound "want the whole book?" target is the author's informational book
   page, not a publisher or bookseller purchase page
   (`src/chapters/homo-deus.mdx:211-215`). The page anatomy and definition of done
   require the real book link to point to a publisher or bookseller. Use a direct,
   stable edition or product page.

### Advisory

- The WHO mortality claim is backed by `content/evidence/homo-deus.md`, but unlike
  the adjacent FAO and errata claims it has no inline source link. Linking the
  recorded WHO report at that sentence would make the caveat easier for a reader to
  verify.

- `npm run check` passed on 2026-07-26: queue/registry validation, prose lint,
  pipeline tests, 167 Vitest tests, typecheck and production build, and ESLint all
  completed successfully.

## Builder resolution — 2026-07-26

- Replaced Figure 81.5's one-way `Flow` with a `ProcessLoop` that returns from
  `change conditions` to `collect signals`; its highlighted closing edge and revised
  caption now make the next-pass feedback explicit.
- Completed the `homo-deus` registry record with tier 2, the book thesis, the
  `Dataism` framework, and the six rendered vocabulary forms: timeline, comparison,
  iceberg, pyramid, process loop, and node graph. The status remains `draft`.
- Changed the "want the whole book?" link to HarperCollins's `Homo Deus` product
  page.
- Linked the existing WHO evidence directly from the caveat's mortality claim.

## Critique round 2 — 2026-07-26

### Required

None.

### Advisory

None. The round 1 fixes are present and coherent: Figure 81.5 closes the feedback
loop, the registry metadata matches the six rendered diagram forms, the outbound
book link targets HarperCollins, and the WHO claim links the recorded evidence.
`npm run check` passed on 2026-07-26, including queue/registry validation, prose
lint, 42 pipeline tests, 167 Vitest tests, typecheck, production build, and ESLint.
