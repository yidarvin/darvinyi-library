verdict: revise

## Critique round 1 — 2026-07-15

### Required

1. The three figures do not keep their labels legible at the required 360 px viewport. The page gives `Flow` five stages (`src/chapters/about.mdx:69`) even though that primitive documents only three or four as phone-safe. At 360 px, the layout and figure padding leave about 278 px for the SVG. `Flow` then scales its 696-unit viewBox into that width, reducing its 11.5-unit stage labels to roughly 4.6 CSS pixels and its 9-unit sequence numbers to roughly 3.6 pixels. `Compare` and `Iceberg` similarly reduce most labels to roughly 8 to 9 pixels. The horizontal-overflow wrapper does not prevent this because the shared SVG root is `w-full` with no minimum width, so it shrinks instead of scrolling. This violates the authoring spec and critique rubric's phone-legibility requirement. Make these figures responsive or give them a genuinely scrollable phone-safe minimum width, and verify all three at 360 px.

### Advisory

1. Reframe the claim that readers can reconstruct examples once they hold a book's structure (`src/chapters/about.mdx:39-42`) as an editorial aim rather than a general fact. Evidence and worked examples often carry the basis for judging whether a framework is credible, not merely extra mass. The later "map, not the territory" paragraph partly supplies this caveat, but the earlier wording is more categorical than the library's evidence-minded posture warrants.

2. The copyright premise is sound. [17 U.S.C. § 102(b)](https://uscode.house.gov/view.xhtml?req=%28title%3A17+section%3A102+edition%3Aprelim%29) excludes ideas, procedures, processes, systems, methods, concepts, principles, and discoveries from copyright protection while preserving protection for original expression. The page states that distinction accurately and makes no source-dependent book claims.

3. `npm run check` passes: queue/registry/content validation, prose lint, pipeline tests, Vitest, TypeScript, Vite build, and ESLint all completed successfully.
