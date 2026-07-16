verdict: approve

## Critique round 1 — 2026-07-15

### Required

1. **Complete the `lean-startup` registry metadata required by the content contract.** The registry entry has the display metadata and `draft` status, but it omits `tier`, `thesis`, `framework`, and the diagram list required by definition-of-done item 7. Add those fields for this chapter without changing unrelated entries or shared tooling.

2. **Recompute the Hero reading-time badge from rendered words.** The draft declares `minutes={9}`, but the rendered textual content is approximately 1,310 words, including headings, captions, exercise titles, and the Hero thesis. At the authoring spec's roughly 200 words per minute, rounded up, that is about 7 minutes, not 9. Set the badge from the final rendered count after any other revision.

3. **Make the pivot figure encode the pivot described in its prose and caption.** Figure 22.5 says that a pivot edits one strategic assumption while preserving the larger purpose, but the `NodeGraph` shows only a static set of nodes. No node or relationship is presented as the changed assumption, and the accented `channel` to `business model` edge is marked `reinforcing` even though neither the paragraph nor caption claims that relationship is reinforcing. The result does not teach the stated distinction between a stable purpose and a deliberately changed strategy. Revise the chapter-local composition so the visual clearly identifies what stays fixed and what changes, and remove any unexplained semantic edge styling. Keep the figure within the shared diagram vocabulary.

### Advisory

1. The prose before `ShelvedNearby` gives a relationship clause for *Good to Great* and *Start With Why*, but the component also links *Thinking, Fast and Slow* without explaining that connection. Add a short relationship clause for the third link or omit it.

2. The Model prose correctly describes pivot-or-persevere as the decision produced by learning, while Figure 22.6 draws it as a fourth peer stage in Build-Measure-Learn. Consider visually distinguishing that decision from the three named stages so the original extension does not look like a redefinition of the signature framework.

### Evidence checked

- The chapter brief supports the central thesis and names Build-Measure-Learn / MVP as the signature model. No separate chapter research or evidence record exists in the repository, and this review did not begin an external search.
- All six figures use existing vocabulary primitives. Their chapter-local minimum widths preserve readable SVG label sizes through the existing horizontal overflow behavior at a 360px viewport.
- The three related slugs resolve to chapters with `done` status, and the outbound link is a direct Penguin Random House book page.
- `npm run check` passed on 2026-07-15: queue/registry/content validation, prose lint, pipeline tests, 48 Vitest tests, TypeScript/Vite production build, and ESLint all completed successfully. The jsdom `Window.scrollTo()` messages were non-failing notices.

## Builder resolution — 2026-07-15

- Completed the `lean-startup` registry record with tier 1, the brief's thesis and Build-measure-learn / MVP framework, and the six rendered diagram forms. The chapter remains `draft` and its queue row remains `PENDING`.
- Recomputed the final rendered reading estimate at roughly 200 words per minute and changed the Hero badge from 9 to 7 minutes.
- Replaced the static pivot node graph with an in-vocabulary comparison that holds the purpose and customer constant while changing the channel from direct sales to a self-serve trial. This removes the unexplained reinforcing edge and makes the changed assumption explicit.
- Kept Build-Measure-Learn as a three-stage loop, so pivot or persevere remains the decision produced by learning rather than a peer stage. Added the missing relationship clause for Thinking, Fast and Slow in Shelved Nearby.

## Critique round 2 — 2026-07-15

### Required

None.

### Advisory

None.

### Evidence checked

- Rechecked all three round 1 REQUIRED findings against the revised chapter and registry. The registry now contains the required metadata, the 7-minute badge matches the recorded rendered-word estimate at roughly 200 words per minute, and Figure 22.5 now presents a parallel before-and-after comparison that holds purpose and customer constant while changing only the channel.
- Rechecked both round 1 ADVISORY findings. The prose now explains the relationship to all three related books, and Figure 22.6 keeps Build-Measure-Learn as the three-stage signature loop while leaving pivot-or-persevere in the explanatory prose as the decision produced by learning.
- Re-derived the central claims from the chapter brief and the repository's recorded evidence where practical. The brief supports the experiment-driven thesis and identifies Build-Measure-Learn / MVP as the signature model. No separate chapter research or evidence record exists, and this review did not begin an external search.
- Re-read every imported chapter component and the shared wrappers used by the MDX. All six figures use registered vocabulary forms, their labels match the surrounding prose, and the minimum-width SVG compositions remain accessible through the Figure wrapper's horizontal overflow behavior on narrow screens.
- `npm run check` passed on 2026-07-15: queue/registry/content validation, prose lint, pipeline tests, 48 Vitest tests, TypeScript/Vite production build, and ESLint all completed successfully. The jsdom `Window.scrollTo()` messages were non-failing notices.
