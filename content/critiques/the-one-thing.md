verdict: approve

## Critique round 1 — 2026-07-16

### Required

1. Figure 55.1 assigns its quadrant labels in the wrong order for the `Matrix`
   component. That component reads the array as top-left, top-right, bottom-left,
   bottom-right, while the vertical axis places high effort at the top and low effort
   at the bottom. The current data therefore renders "quick upkeep" as high-effort,
   small-effect work, "busy effort" as low-effort, small-effect work, and the
   highlighted "lead work" as only low-effort, large-effect work. This conflicts with
   the adjacent explanation that the consequential task is not always the smallest
   and with the caption's emphasis on downstream effect. Rework the quadrant mapping
   and emphasis so the visual's labels and target agree with its axes and prose.

2. The `the-one-thing` registry record is not complete enough for the definition of
   done. It contains the base metadata and `status: "draft"`, but omits `tier`,
   `thesis`, `framework`, and the diagram inventory required by item 7 of the
   authoring spec. Record the finished page metadata, including the focusing-question
   framework and all diagram forms, before approval.

### Advisory

- The chapter imports `Compare` but does not use it. Remove the unused import when
  resolving the required findings.

## Builder resolution — 2026-07-16

Resolved all required findings for `the-one-thing`:

1. Corrected Figure 55.1 to match `Matrix` reading order and its axes. The high-effort,
   small-effect quadrant now contains “busy effort,” the high-effort, large-effect
   quadrant contains and highlights “lead work,” the low-effort, small-effect quadrant
   contains “quick upkeep,” and the low-effort, large-effect quadrant contains “useful
   repair.” The highlighted target now agrees with the prose and caption: consequential
   work has a large downstream effect and may require making room for it.
2. Completed the `the-one-thing` registry entry with tier 2, the final thesis, the
   focusing-question framework, and the six rendered diagram forms. Its status remains
   `draft`.
3. Removed the unused `Compare` import.

`npm run check` passed on 2026-07-16, including validation, prose lint, pipeline
tests, application tests, typecheck, production build, and lint.

## Critique round 2 — 2026-07-16

### Required

1. Figure 55.4 clips the first bar's value label inside the SVG viewBox. `Bars`
   starts a value label immediately after its bar, and the chapter combines a
   `0.72` bar with the long label “arrive by default.” At the component's fixed
   geometry, that text extends past the 380-unit right edge, so the final part is
   not readable. Horizontal scrolling does not help because the clipping occurs
   inside the SVG. Adjust this chapter's bar values or labels so every label fits
   without changing the intended conceptual comparison.

2. Figure 55.5 places the long marker label “protected, reachable for real needs”
   on essentially the same line as the two pole labels. At the marker's `0.6`
   position, it visibly overlaps “fully sealed off” and reaches into the left-side
   label area as well. The collision is internal to the SVG at every rendered
   width, including mobile. Shorten, remove, or otherwise reconfigure the chapter's
   labels so the selected boundary and both poles remain independently legible.

### Advisory

None.

## Builder resolution — 2026-07-16

Resolved all required findings from critique round 2:

1. Shortened Figure 55.4's first bar-end label from “arrive by default” to “by
   default.” At the existing 0.72 bar length, the label now ends inside the `Bars`
   viewBox while retaining the intended comparison: reactive requests arrive without
   being deliberately scheduled.
2. Reconfigured Figure 55.5 so the three labels are separately legible within the
   `Spectrum` viewBox. The poles now read “available” and “unavailable,” and the
   selected point is moved to 0.55 and labeled “urgent needs.” This keeps the marker
   inside the deliberate-boundary zone while leaving clear horizontal space around
   both pole labels.

The earlier matrix mapping, completed registry metadata, and removed unused import
remain intact. `npm run check` passed on 2026-07-16, including validation, prose lint,
pipeline tests, application tests, typecheck, production build, and lint. The chapter
remains `draft`; no status transition was made.

## Critique round 3 — 2026-07-16

### Required

None.

### Advisory

None.
