verdict: approve

## Critique round 1 — 2026-07-27

### Required

1. The signature matrix assigns every attachment pattern to the wrong combination of its stated axes. `Matrix` consumes quadrants in `[top-left, top-right, bottom-left, bottom-right]` order, while this figure defines anxiety as high at the top and avoidance as high at the right. The resulting positions should therefore be anxious at top-left, mixed/fearful at top-right, secure at bottom-left, and avoidant at bottom-right. Lines 147–150 instead place secure, anxious, avoidant, and mixed alarm in those positions, respectively, and line 152 highlights the erroneous secure cell. This reverses the chapter's central framework and changes the reader's understanding. Reorder the labels and highlight the actual secure quadrant. Also rename or reverse the horizontal dimension label: a left-to-right increase in avoidance is not a left-to-right increase in “comfort with closeness and dependence.”

2. The `attached` registry record is incomplete against the authoring spec's definition of done. It contains only the basic route metadata and `status`, but omits the brief's tier, the chapter thesis, the signature framework, and the diagram-form list. Populate those fields so the database describes the finished page rather than relying on the MDX and brief as separate sources of truth.

### Advisory

1. The prose before `ShelvedNearby` explains the relationship to `nonviolent-communication` and `seven-principles-marriage`, but the component also links `supercommunicators` without the relationship clause required by the cross-linking guidance. Add a short clause explaining that edge or omit the third link.

2. `npm run check` passes. The repeated jsdom `Window.scrollTo()` notices during Vitest are non-failing environment output, not a defect in this chapter.

## Builder resolution — 2026-07-27

- Reordered the attachment matrix into its documented `[top-left, top-right, bottom-left, bottom-right]` order: anxious, mixed alarm, secure, and avoidant. The secure cell is now highlighted, and the horizontal dimension now reads “avoidance of closeness and dependence,” which matches its low-to-high pole labels.
- Completed the `attached` registry record with tier 3, the brief thesis, the Attachment styles framework, and the six rendered diagram forms; its lifecycle status remains `draft`.
- Added the missing relationship clause for the existing `supercommunicators` shelf link.

## Critique round 2 — 2026-07-27

### Required

None.

### Advisory

1. All round 1 requirements are resolved in the current draft. The Model matrix now
   places anxious at high anxiety and low avoidance, mixed alarm at high anxiety and
   high avoidance, secure at low anxiety and low avoidance, and avoidant at low
   anxiety and high avoidance. Its secure highlight and both axis labels agree with
   that geometry. The registry records the brief-supported tier, thesis, framework,
   and all six figure forms in page order.

2. The bounded factual record remains consistent with the page. The brief supports
   the secure, anxious, and avoidant signature model; the recorded adult-attachment
   research supports the romantic-bond framing, accessibility and responsiveness,
   the later anxiety/avoidance dimensions, and a combination of stability and
   change. The page presents these as patterns rather than diagnoses, avoids a
   childhood-destiny claim, and clearly separates communication practice from
   coercive or unsafe relationships. It uses no quotation, close source-shaped
   paraphrase, reproduced figure, or real cover art. This review began no new
   external web search.

3. The fixed anatomy and imported renderers are internally consistent. Five key
   ideas each have a captioned structural figure, the signature Model has its own
   matrix, and the four practice cards specify observable actions and return times.
   `Hero`, `ShelvedNearby`, `Iceberg`, `Compare`, `Flow`, `ProcessLoop`,
   `NodeGraph`, and `Matrix` all render the supplied labels without an intrinsic
   collision or semantic reversal. The chapter-local minimum widths remain legible
   through `Figure`'s horizontal scroller on a phone. All three nearby slugs resolve
   to done chapters, the prose explains every relationship, and the outbound link
   is the recorded publisher page.

4. `npm run check` completed with `CHECK OK` on 2026-07-27. Repository validation,
   prose lint, the pipeline and runner suites, all 256 Vitest tests, TypeScript, the
   Vite production build, and ESLint passed. Vitest emitted only the existing
   non-failing jsdom `Window.scrollTo()` notices.
