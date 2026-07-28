verdict: resolved

## Critique round 1 — 2026-07-27

### Required

1. **Shelved Nearby omits the required relationship clauses.** The chapter passes four
   slugs to `ShelvedNearby`, which renders cover links but no explanation of why each
   book is related. Both the page anatomy/cross-linking contract in
   `docs/authoring-spec.md` and the chapter brief require each nearby link to note the
   relationship in one clause. Add visible, concise relationship text for
   `dare-to-lead`, `radical-candor`, `extreme-ownership`, and `start-with-why` while
   retaining links only to built pages.

### Advisory

1. The first figure is a one-way sequence even though the idea and caption depend on
   recurrence. The labels clearly describe one belonging-building interaction, but the
   visual does not itself show that the signals must repeat. Making recurrence visible
   would align the diagram more tightly with the section's central claim.

## Builder resolution — 2026-07-27

- Added visible, linked relationship clauses for **Dare to Lead**, **Radical Candor**,
  **Extreme Ownership**, and **Start with Why** directly before the existing
  `ShelvedNearby` cover links. Each target is already built, and each clause states why
  it belongs beside this chapter.
- Replaced the first one-way flow with an in-vocabulary `ProcessLoop` so the diagram
  itself shows that belonging signals recur. Updated the registry diagram metadata to
  describe the two distinct process-loop figures.
