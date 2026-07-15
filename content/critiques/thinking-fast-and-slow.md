verdict: revise

## Critique round 1 — 2026-07-15

### Required

1. **Complete the `thinking-fast-and-slow` registry record required by the content contract.** The record supplies the slug, display title, author/year subtitle, shelf, and draft status, but it omits `tier`, `thesis`, `framework`, and the diagram-form inventory required by definition-of-done item 7. Add the chapter metadata without changing shared registry tooling or unrelated entries.

2. **Make the meaning-bearing labels in the Spectrum, Flow, and Timeline figures legible at a 360 px viewport.** The chapter-local minimum widths prevent those SVGs from collapsing to the Figure container's roughly 278 px content width, but the chosen minima are still smaller than the components' viewBoxes or leave their smallest type below the repository's established phone-safe scale. Figure 2.2 keeps its 9.5-unit zone labels at about 9.5 CSS px. Figure 2.3 renders a 578-unit-wide Flow at 480 px, reducing its 11.5-unit step and branch labels to about 9.6 CSS px and its 9-unit sequence labels to about 7.5 px. Figure 2.5 renders a 536-unit-wide Timeline at 500 px, reducing its meaningful 9.5-unit sublabels to about 8.9 CSS px. Increase the chapter-local rendered widths or revise those layouts so the labels remain readable while the existing Figure wrapper scrolls horizontally. The Iceberg and both Compare instances clear this specific sizing check.

### Advisory

1. The page's copyright posture is sound in this bounded review. It uses no quotation or cover art, organizes the material thematically rather than by the book's chapter sequence, and composes original labels through the shared diagram vocabulary rather than recreating a source figure.

2. The chapter otherwise satisfies the required anatomy: a clear thesis, optional significance section, five key ideas with structural figures, a distinct System 1/System 2 Model section, four concrete practice cards, an appropriately cautious caveat, a concise final takeaway, and a direct publisher link. The seven-minute badge is consistent with the rendered word count once headings, captions, SVG labels, and generated page text are included.

3. The social-priming replication sentence is cautious and directionally consistent with the caveat it serves, but the chapter brief contains no primary-source evidence for that post-publication claim. This bounded pass did not use external search, so the claim was not independently source-checked here. A future evidence pass should attach a specific primary replication source locally or narrow the sentence to evidence that can be checked from the bounded source set.

4. `ShelvedNearby` links to the completed `atomic-habits` page, but it does not state the relationship in the one-clause form requested by the cross-linking guidance. A short chapter-local note such as the shared interest in automatic judgment and behavior would make the edge informative. This remains advisory because cross-links are optional under the critique rubric.

5. `npm run check` passed on 2026-07-15: queue/registry/content validation, prose lint, pipeline tests, eight Vitest tests, TypeScript and Vite production build, and ESLint all completed successfully. The jsdom run emitted only the existing non-failing `Window.scrollTo()` notices.
