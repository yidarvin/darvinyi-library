verdict: resolved

## Critique round 1 — 2026-07-27

### Required

1. **Compress The thesis to the required one or two sentences.** The paragraph at
   `src/chapters/outlive.mdx:13` is four sentences. The authoring spec defines this
   section as the one- or two-sentence compression a reader can carry away. Preserve
   the useful distinction between earlier prevention, physical capacity, and
   healthspan, but make the section conform to the fixed anatomy.

2. **Preserve the two Flow diagrams' authored label size on a phone.** Each four-step
   `Flow` generates a 558-unit-wide viewBox, but Figure 103.5 has only
   `min-w-[380px]` at `src/chapters/outlive.mdx:132`, and the Flow in Figure 103.6 is
   constrained by the same 380px minimum at `src/chapters/outlive.mdx:148`. At that
   rendered width, the primitive's 11.5-unit labels shrink to about 7.8 CSS pixels.
   This fails the explicit mobile-legibility requirement even though the surrounding
   Figure can scroll horizontally. Raise the chapter-local minimum rendered width to
   the generated Flow width, or reduce or recompose the steps so both figures remain
   readable at a 360px viewport.

3. **Replace the outbound book URL with a qualifying publisher or bookseller link.**
   `buyUrl` at `src/chapters/outlive.mdx:228` points to Peter Attia's author site. Both
   the fixed anatomy and this chapter's brief require the footer to link to the real
   book at a publisher or bookseller. Use a stable direct book page from one of those
   sources.

4. **Complete the Outlive registry record required by the content contract.** The
   record at `content/registry.json:2034` contains the display metadata and draft
   status but omits `tier`, `thesis`, `framework`, and `diagrams`. Definition-of-done
   item 7 requires all four. Add values that agree with the chapter, including
   Medicine 3.0 as the signature framework and the actual diagram forms used.

### Advisory

1. Figure 103.3's caption says that shared risks and care choices connect the four
   fronts, but the diagram contains only a `shared risks` node, and each directed edge
   is labeled `informs`. Consider either narrowing the caption to the shared-risk map
   actually shown or revising the labels and direction so the visual states the
   prose's relationship more precisely.

2. Within the chapter brief and recorded evidence available for this review, the
   health claims are otherwise appropriately bounded. The draft distinguishes
   association from personal prediction, does not turn earlier testing into a blanket
   recommendation, presents Medicine 3.0 as a framing device rather than a validated
   protocol, and matches the recorded 2025 rapamycin review. No new external web
   search was begun.

3. The remaining structure is intact. Five key ideas each have a captioned,
   in-vocabulary diagram; the Medicine 3.0 Model is present; the practice cards are
   concrete and include appropriate clinical cautions; related slugs resolve to
   completed chapters; and the generated cover preserves the copyright line.
   `npm run check` passed on 2026-07-27, including validation, prose lint, all 40
   pipeline tests, all 216 Vitest tests, TypeScript, the production build, and ESLint.
   Vitest emitted only the existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-27

- Compressed **The thesis** to two sentences while retaining the healthspan, earlier
  prevention, physical-capacity, and evidence-revision argument.
- Set Figure 103.5's four-step `Flow` to its generated 558px width and set Figure
  103.6's shared wrapper to 558px, so both flows preserve their authored 11.5-unit
  labels at a 360px viewport through the Figure's horizontal scroll container.
- Replaced the author-site outbound link with Harmony/Penguin Random House's direct
  Outlive purchase page and recorded that publisher source in the chapter evidence.
- Completed the Outlive registry record with tier 2, a chapter-aligned thesis,
  Medicine 3.0 as the framework, and all seven diagram forms in rendered order.
- `npm run check` passed on 2026-07-27.
