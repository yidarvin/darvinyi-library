verdict: resolved

## Critique round 1 — 2026-07-27

### Required

1. Figure 115.4's horizontal axis contradicts its plotted sequence. The axis reads
   `time before the deadline ->`, which means more time remaining as the reader moves
   right, but the annotations move from `first response` on the left to `rush` on the
   right. The prose and caption instead describe time progressing toward a deadline.
   Relabel the axis to that progression, or reverse the plotted sequence, so the
   structural diagram does not teach the relationship backward.

2. Figure 115.5 mixes two different vertical dimensions and therefore does not map
   its quadrant notes to its axes. The poles are `small exposure` and `large
   exposure`, while the axis label is `cost if wrong`. In the bottom-left quadrant,
   `stuck experiment` is consequently placed at small cost but described as `costly
   to unwind`; in the top-right, `guarded commitment` is placed at high cost while
   reversibility is treated as sufficient protection. Choose one vertical dimension
   and rewrite the poles and quadrant notes so each cell consistently represents the
   risk test explained in the prose.

3. The `ShelvedNearby` outbound URL points to Adam Grant's promotional book page,
   not to a publisher or bookseller product page. The authoring spec permits a
   publisher or bookseller, and the chapter brief specifically requires a bookseller
   link. Replace it with a direct qualifying page so the final spine section meets
   the outbound-book contract.

### Advisory

1. Figure 115.2 uses bar length as candidate quantity, yet `first familiar answer`
   and `one supported bet` have different lengths despite both being singular. Equal
   endpoints, or labels that make the magnitudes' meaning explicit, would make the
   narrowing sequence more precise.

2. The related-book tiles resolve to done chapters, but they do not state the
   one-clause relationship requested by the Shelved Nearby guidance. Adding those
   relationship cues would make the cross-links more useful than proximity alone.

## Builder resolution — 2026-07-27

Resolved all required findings:

1. Figure 115.4 now labels its horizontal axis `time progressing toward the deadline`,
   so the left-to-right progression agrees with `first response`, the incubation window,
   and the final rush.
2. Figure 115.5 now uses `initial exposure` consistently as its vertical dimension. Its
   four cells distinguish exposure from reversibility: avoid large, hard-to-undo moves;
   contain large exposure even where an exit exists; redesign small but sticky moves; and
   learn first through a small, easy-to-reverse test.
3. The outbound `ShelvedNearby` link now goes directly to the bookseller product listing
   for *Originals* (`amazon.com/dp/014312885X`). The evidence note retains the official
   Adam Grant page only as a source for the chapter's scope.

The related chapters remain unchanged, the registry stays `draft`, and no chapter was marked
done.
