verdict: approve

## Critique round 1 — 2026-07-15

### Required

1. The three figures do not keep their labels legible at the required 360 px viewport. The page gives `Flow` five stages (`src/chapters/about.mdx:69`) even though that primitive documents only three or four as phone-safe. At 360 px, the layout and figure padding leave about 278 px for the SVG. `Flow` then scales its 696-unit viewBox into that width, reducing its 11.5-unit stage labels to roughly 4.6 CSS pixels and its 9-unit sequence numbers to roughly 3.6 pixels. `Compare` and `Iceberg` similarly reduce most labels to roughly 8 to 9 pixels. The horizontal-overflow wrapper does not prevent this because the shared SVG root is `w-full` with no minimum width, so it shrinks instead of scrolling. This violates the authoring spec and critique rubric's phone-legibility requirement. Make these figures responsive or give them a genuinely scrollable phone-safe minimum width, and verify all three at 360 px.

### Advisory

1. Reframe the claim that readers can reconstruct examples once they hold a book's structure (`src/chapters/about.mdx:39-42`) as an editorial aim rather than a general fact. Evidence and worked examples often carry the basis for judging whether a framework is credible, not merely extra mass. The later "map, not the territory" paragraph partly supplies this caveat, but the earlier wording is more categorical than the library's evidence-minded posture warrants.

2. The copyright premise is sound. [17 U.S.C. § 102(b)](https://uscode.house.gov/view.xhtml?req=%28title%3A17+section%3A102+edition%3Aprelim%29) excludes ideas, procedures, processes, systems, methods, concepts, principles, and discoveries from copyright protection while preserving protection for original expression. The page states that distinction accurately and makes no source-dependent book claims.

3. `npm run check` passes: queue/registry/content validation, prose lint, pipeline tests, Vitest, TypeScript, Vite build, and ESLint all completed successfully.

## Builder resolution — 2026-07-15

Resolved every required finding from critique round 1. The three about-page figures now
keep a phone-safe minimum SVG width inside Figure's existing horizontal-scroll wrapper:
Compare and Iceberg use 384 px, and Flow uses its native 568 px width. The queue Flow
also now has four stages, within the primitive's documented phone-safe limit, while its
"distilled" stage still represents the writing and drawing work described in the prose.
At a 360 px viewport, the figures scroll horizontally instead of scaling their labels
below their authored sizes. I also reframed the supporting-material passage as an
editorial aim and made clear that readers should use the original to judge examples and
evidence.

## Critique round 2 — 2026-07-15

### Required

None.

### Advisory

1. The round 1 phone-legibility finding is resolved. `Figure` provides an
   `overflow-x-auto` wrapper, the revised `Compare` and `Iceberg` instances retain a
   24 rem minimum width, and `Flow` retains its 568 px native width through a 35.5 rem
   minimum. The production CSS contains both minimum-width rules, so these SVGs scroll
   at a 360 px viewport instead of shrinking their labels. The queue flow now contains
   four stages, within the primitive's documented phone-safe count.

2. The earlier evidence caveat is resolved. The page now describes preservation of the
   book's conceptual shape as the distillation's aim and explicitly leaves readers with
   the original examples and evidence to judge.

3. The copyright premise remains accurate. 17 U.S.C. § 102(b) excludes ideas,
   procedures, processes, systems, methods, concepts, principles, and discoveries from
   copyright protection, while the U.S. Copyright Office's Circular 33 confirms that
   protection can attach to the original literary or graphic expression of those ideas.
   The page draws that distinction without making source-dependent claims about a book.

4. `npm run check` passes all six stages: queue/registry/content validation, prose lint,
   pipeline tests, Vitest, TypeScript and Vite production build, and ESLint.
