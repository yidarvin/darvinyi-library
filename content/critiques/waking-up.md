verdict: revise

## Critique round 1 — 2026-07-28

### Required

1. **Preserve legible label sizes for all five figures at a 360px viewport.**
   Figures 139.1, 139.2, 139.4, and 139.5 pass only `block w-full`, so their
   380- or 384-unit SVG viewBoxes shrink to the inside width of `Figure` on a
   phone (`src/chapters/waking-up.mdx:41-48,63-82,117-130,144-158`). At the
   roughly 278px available inside the figure at a 360px viewport, the primitives'
   9.5-to-13-unit labels render at approximately 7-to-9.5 CSS pixels
   (`src/components/diagrams/Iceberg.tsx:25-66`;
   `src/components/diagrams/NodeGraph.tsx:60-64,126-135`;
   `src/components/diagrams/Compare.tsx:62-80,89-100`;
   `src/components/diagrams/Spectrum.tsx:55-59,87-93,111-159`). Figure 139.3
   has a 558-unit four-step `Flow` viewBox but only a 420px minimum width, which
   still scales its 9-to-11.5-unit labels down to about 6.8-to-8.7 CSS pixels
   (`src/chapters/waking-up.mdx:96-102`;
   `src/components/diagrams/Flow.tsx:21-35,70-80`). Add chapter-local minimum
   widths appropriate to the actual viewBoxes so `Figure`'s existing horizontal
   overflow preserves the authored label sizes instead of shrinking them below
   the mobile-legibility requirement.

2. **Give the first key idea a diagram that encodes its stated distinction.**
   The section distinguishes an occurrence from the personal explanation added
   to it, using chest tightness and “I am failing” as the two events, then argues
   that noticing this gap permits a considered response
   (`src/chapters/waking-up.mdx:29-39`). Figure 139.1 instead places “the felt
   owner: 'me'” above a waterline and sights, sensations, thoughts, moods, and
   attention beneath it (`src/chapters/waking-up.mdx:41-47`). The imported
   `Iceberg` form explicitly represents a visible surface against underlying
   drivers (`src/components/diagrams/Iceberg.tsx:4-15,36-60`), so this geometry
   neither shows occurrence versus interpretation nor the gap before response.
   It largely repeats the following section's no-central-self claim. Recompose
   Figure 139.1 with an in-vocabulary structure that teaches the event,
   commentary, and response relation, or revise the key idea and caption to the
   surface-versus-underlying relation actually rendered.

3. **Support or narrow the specific meditation-risk claim.** The caveat says
   meditation can be destabilizing, especially amid trauma, severe anxiety,
   psychosis, or a major mood episode, and uses that claim to direct readers to
   stop and seek qualified care (`src/chapters/waking-up.mdx:189-198`). The
   recorded evidence supports secular inquiry into selfhood, beginner meditation,
   distinct narrative and experiential modes of self-reference, and modest
   changes in present-centered self-focus
   (`content/evidence/waking-up.md:8-27`); it records no adverse-effects or
   clinical-safety source from which this population-specific claim can be
   re-derived. Because this is consequential mental-health guidance, add recorded
   evidence specific enough to support it or narrow the callout to the
   non-clinical and epistemic limits already established by the bounded evidence.

### Advisory

1. Figure 139.5 uses a quantitative `Spectrum` and places “meditation practice”
   at an unexplained `0.78` between “adopt an answer” and “investigate
   experience” (`src/chapters/waking-up.mdx:132-158`). The prose presents two
   epistemic approaches rather than a measured degree, so a neutral comparison
   would avoid false precision. The labels and caption make the intended contrast
   recoverable, so this does not independently block approval.

2. Figure 139.3's caption, “noticing it available in real time,” is grammatically
   unclear (`src/chapters/waking-up.mdx:96`). Tighten it when revising so the
   caption directly names the shift from identification with a thought to
   awareness of it.

3. Apart from the required findings, the fixed anatomy is intact. Five key ideas
   each have a captioned shared-vocabulary figure; omission of the Model section
   matches both the brief and registry; the four exercises specify observable
   actions; and all three nearby slugs resolve to done chapters with their
   relationships stated in prose. The outbound publisher link matches the
   recorded evidence.

4. Within the bounded brief and recorded evidence, the remaining synthesis uses
   original thematic organization, prose, and shared SVG primitives. No
   quotation, real cover art, apparent close paraphrase, or apparent reproduction
   of a source figure was found. This review began no external web search.

5. `npm run check` completed with `CHECK OK` on 2026-07-28. Validation and prose
   lint passed; both pipeline tests, all 40 runner tests, and all 299 Vitest tests
   passed; TypeScript, the Vite production build, and ESLint passed. Vitest
   emitted only the existing non-failing jsdom `Window.scrollTo()` notices.
