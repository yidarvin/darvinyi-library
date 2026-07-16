verdict: approve

## Critique round 1 — 2026-07-15

### Required

1. **Make Figure 18.6 agree with its two axes.** The shared `Matrix` reads its
   quadrants as top-left, top-right, bottom-left, and bottom-right. With refusal
   getting easier from left to right and the chooser's interest increasing from
   bottom to top, the bottom-right cell means an easy-to-refuse design led by the
   designer's gain. The chapter labels that cell `neutral convenience` with
   `little steering`, which contradicts the vertical coordinate. Recompose that
   quadrant or revise the axes so all four labels describe the positions they
   occupy. The highlighted top-right `defensible nudge` is otherwise consistent
   with the prose and caption.

2. **Repair Figure 18.4's colliding and conceptually mismatched labels.** The
   shared `Spectrum` places both pole labels at y=74 and its marker caption at
   y=78. At `marker={0.8}`, `good default` occupies the same horizontal region as
   `easy to start`, so the two labels overlap at every rendered scale. The marker
   also calls low friction a default even though this section correctly defines a
   default elsewhere as what happens when a person does nothing. Shorten, move, or
   remove the chapter-local marker caption so the labels are separately legible
   and the figure teaches friction rather than conflating it with a preset.

3. **Number the figures for this chapter.** The registry assigns `nudge` number
   17, while all seven captions are numbered 18.1 through 18.7. Change them to
   17.1 through 17.7, matching the established chapter-number convention and the
   registry record.

4. **Complete the `nudge` registry record required by the content contract.** The
   draft entry has its display metadata and `draft` status but omits `tier`,
   `thesis`, `framework`, and the diagram-form inventory. Add the brief-supported
   tier 1 and thesis, identify choice architecture / the nudge as the signature
   framework, and inventory the seven forms used: iceberg, comparison, node graph,
   spectrum, timeline, two-by-two matrix, and flow.

5. **Make the automatic-enrollment evidence inspectable within the bounded
   record.** The chapter twice presents a specific empirical account: automatic
   401(k) enrollment raised participation, while preset contribution rates and
   investments shaped where participants remained. The chapter brief supports the
   high-level choice-architecture thesis but contains none of this study-level
   evidence, and the repository has no chapter-specific evidence dossier or source
   record for `nudge`. Because the claim supplies the page's concrete evidence for
   the power and risk of defaults, either record the primary evidence used so the
   claim can be re-derived in review or narrow the passage to a book-attributed
   conceptual example that does not present unrecorded research findings as
   independently established here.

### Advisory

1. Within the repository's bounded evidence, the central thesis, anatomy, and
   copyright posture are otherwise strong. The draft follows an original thematic
   order, contains no quotation or real cover art, and uses shared vocabulary forms
   rather than reproducing an author figure. Six key ideas each have a captioned
   structural diagram, the separate Model renders the brief's signature framework,
   the four exercises prescribe observable actions, and the caveat distinguishes
   defensible help from institutional self-interest and structural remedies. No new
   external web search was begun for this review.

2. The three nearby slugs all resolve to done chapters, and the outbound Penguin
   Random House URL is a direct publisher link. The footer does not, however, state
   the one-clause relationship for any related book as requested by the
   cross-linking guidance. A short sentence connecting fast judgment, predictable
   irrationality, and influence to choice architecture would make those links more
   useful.

3. The chapter-local minimum widths work with `Figure`'s horizontal-overflow
   wrapper to preserve the authored SVG geometry on a phone. Apart from the
   internal Figure 18.4 collision above, the imported diagram labels fit their
   viewports, and the seven-minute badge is consistent with the reader-facing prose,
   headings, captions, and diagram labels at approximately 200 words per minute
   rounded up.

4. `npm run check` passed after this critique was written on 2026-07-15:
   queue/registry/content validation, prose lint, both pipeline tests, all 38
   Vitest tests, TypeScript and Vite production build, and ESLint completed
   successfully. The Vitest run emitted only the existing non-failing jsdom
   `Window.scrollTo()` notices.

## Builder resolution — 2026-07-15

1. Renumbered every `nudge` figure from 18.1–18.7 to 17.1–17.7, matching registry number 17.
2. Removed Figure 17.4's `good default` marker caption. The spectrum now labels friction only, and its pole labels remain separately legible.
3. Replaced Figure 17.6's bottom-right label with `designer convenience` and the note `easy exit, but their gain leads`, so it matches the easy-to-refuse and designer-gains axes while preserving the highlighted defensible-nudge quadrant.
4. Completed the `nudge` registry metadata with tier 1, the brief-supported thesis, `Choice architecture / the nudge`, and the seven diagram forms used on the page.
5. Narrowed both retirement-plan passages to the book-attributed conceptual example. They no longer present unrecorded 401(k) participation results or study-level conclusions as independently established evidence.

No new external search was begun. `npm run check` passed after these changes.

## Critique round 2 — 2026-07-15

### Required

None.

### Advisory

1. The current draft resolves every required finding from round 1. The matrix now
   agrees with its axes, the friction spectrum no longer conflates low effort with
   a default, figure numbering matches chapter 17, and the registry records the
   brief-supported framework and diagram inventory. The retirement passages are
   now explicitly framed as the book's conceptual example rather than as an
   independently established study result, which keeps the claims within the
   bounded evidence available for this review.

2. The footer's three related slugs resolve to built chapters, but it still does
   not explain each relationship in a clause as the cross-linking guidance asks.
   This remains a useful future refinement, not an approval blocker.

3. `npm run check` passed on 2026-07-15: queue, registry, critique, and content
   validation; prose lint; both pipeline tests; all 38 Vitest tests; TypeScript and
   Vite production build; and ESLint. Vitest emitted only the existing non-failing
   jsdom `Window.scrollTo()` notices. No new external web search was begun.
