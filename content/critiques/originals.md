verdict: approve

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

## Critique round 2 — 2026-07-27

### Required

1. The Hero reading-time badge is not computed from the final rendered page. A
   direct server render contains 1,655 reader-visible words, including the Hero,
   headings, captions, diagram labels, exercise titles, and generated footer text.
   At the authoring spec's approximately 200 words per minute, rounded up, this is a
   nine-minute distillation, not `minutes={8}`. Set the badge from the rendered count.

### Advisory

1. The three required findings from round 1 remain resolved. Figure 115.4 now
   progresses toward the deadline, Figure 115.5 consistently sorts initial exposure
   against reversibility, and the outbound link is a direct bookseller product page.

2. Figure 115.2 still gives the singular `first familiar answer` and `one supported
   bet` different bar lengths even though the bars otherwise encode candidate
   quantity. Equal endpoints, or labels that define another magnitude, would make
   the narrowing sequence more precise. This remains the round 1 advisory.

3. The four related slugs resolve to done chapters, but the footer still presents
   cover tiles without the one-clause relationship notes requested by the
   cross-linking guidance. This remains advisory because the links are valid and the
   missing cues do not misstate the chapter.

4. Within the recorded evidence, the chapter's claims about questioning defaults,
   generating alternatives, informed-peer review, bounded incubation, and genuine
   dissent are supported and carefully qualified. The risk and consent guidance is
   explicitly identified as the chapter's ethical synthesis. No new external web
   search was begun for this review.

5. `npm run check` passed on 2026-07-27: queue, registry, critique, and content
   validation; prose lint; all 42 pipeline tests; all 245 Vitest tests; TypeScript
   and the Vite production build; and ESLint. Vitest emitted only the existing
   non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-27

Resolved the round 2 required finding:

1. The `<Hero>` reading-time badge now uses `minutes={9}`. This matches the recorded
   server-rendered count of 1,655 reader-visible words, including headings, captions,
   diagram labels, exercise titles, and generated footer text, rounded up at
   approximately 200 words per minute.

The round 1 axis, matrix, and direct-bookseller-link fixes remain in place. The registry
remains `draft`; this resolution does not mark the chapter done.

## Critique round 3 — 2026-07-27

### Required

None. The current draft preserves all four required corrections from rounds 1 and 2:
the incubation curve's axis agrees with its sequence, the experiment matrix consistently
sorts initial exposure against reversibility, the outbound link is a direct bookseller
product page, and the Hero declares a nine-minute reading time. A fresh direct server
render contains 1,655 reader-visible words, which rounds up to nine minutes at the
authoring spec's approximately 200 words per minute.

The chapter follows the required spine and the brief's deliberate omission of a Model
section. Its six key ideas each have a captioned structural diagram from the shared
vocabulary; the practices are concrete; the caveat distinguishes originality from
contrarianism and adds clear risk, consent, and reversibility boundaries. The chapter's
claims about defaults, idea quantity, informed-peer review, bounded incubation, and
genuine dissent remain supported by the recorded evidence, while the risk guidance is
properly identified there as this library's ethical synthesis. No new external web search
was begun.

`npm run check` passed on 2026-07-27: queue, registry, critique, and content validation;
prose lint; all 42 pipeline and runner tests; all 245 Vitest tests; TypeScript and the
Vite production build; and ESLint. Vitest emitted only the existing non-failing jsdom
`Window.scrollTo()` notices.

### Advisory

1. Figure 115.2 still uses bar length as candidate quantity while giving the singular
   `first familiar answer` and `one supported bet` different lengths. Equal endpoints,
   or labels that define another magnitude, would make the narrowing sequence more
   precise. This remains the round 1 advisory and does not make the argument misleading.

2. The four related slugs resolve to completed chapters, but the shared footer still
   renders cover tiles without the one-clause relationship notes requested by the
   cross-linking guidance. This remains advisory because the links are valid and their
   lack of annotations does not misstate the chapter.
