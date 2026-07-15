verdict: revise

## Critique round 1 — 2026-07-15

### Required

1. **Keep the Model comparison headers inside their panels and SVG viewport.**
   Figure 9.6 supplies the 168-unit-wide `Compare` panels with the unbroken titles
   `when ability seems fixed` and `when ability seems developable`
   (`src/chapters/mindset.mdx:161-171`). The shared component renders panel titles
   as a single 13-unit monospace line without wrapping
   (`src/components/diagrams/Compare.tsx:28-35,51-53`) inside a 384-unit viewBox
   (`src/components/diagrams/Compare.tsx:73-77`). The 24-character left title
   crosses into the center/right region, and the 30-character right title extends
   past the viewBox and is clipped. The chapter's 440 px minimum width scales the
   same internal geometry, so it cannot repair the overflow. Shorten or otherwise
   recompose these chapter-local labels so both meaning-bearing headers remain
   distinct and fully visible. Do not edit the shared `Compare` component.

2. **Separate the Spectrum marker captions from the pole labels in Figures 9.5 and
   9.6.** The shared `Spectrum` places both pole labels at y=74 and the centered
   marker caption at y=78 (`src/components/diagrams/Spectrum.tsx:92-110`). With
   `ability is fixed` / `ability can grow` around `this domain, today`
   (`src/chapters/mindset.mdx:129-140`), the marker text overlaps the right pole and
   nearly reaches the left. The Model repeats the defect more symmetrically:
   `belief about ability` overlaps both `fixed mindset` and `growth mindset`
   (`src/chapters/mindset.mdx:152-160`). Scaling or horizontal scrolling preserves
   these coordinate collisions. Revise the chapter-local labeling or composition
   so each pole and marker caption can be read independently. Do not edit the shared
   `Spectrum` component.

### Advisory

1. Figure 9.4 marks all five `NodeGraph` edges as reinforcing, so every connection
   receives an accent plus sign (`src/chapters/mindset.mdx:99-116`). The prose
   establishes a learning cycle, but it does not establish system-dynamics polarity
   for claims such as an attempt increasing feedback/help or a revised strategy
   increasing an attempt. Plain directed edges would communicate sequence and
   feedback without adding an unexplained quantitative-looking claim.

2. Within the repository's bounded evidence, the core factual and copyright posture
   is sound. The brief, seed metadata, and registry support the fixed-versus-growth
   interpretation of challenge, effort, and failure and identify that contrast as
   the signature model. The draft uses original thematic prose, no quotation or real
   cover art, and shared diagram forms rather than a traced source figure. The 2018
   meta-analysis and later national randomized-study summaries in the caveat are
   cautious and specifically framed, but neither the brief nor a separate local
   evidence record supports independent verification of their endpoints or scope.
   This review began no external web search, so a future evidence pass should attach
   the primary records locally or narrow any detail that cannot be re-derived.

3. Apart from the required label defects, the anatomy and visual mapping are sound:
   five key ideas each have a captioned in-vocabulary diagram, the Model renders the
   required fixed/growth framework, four exercises are concrete, the caveat rejects
   effort-only and opportunity-blind readings, and the final takeaway is concise.
   All three related slugs resolve to completed chapters, their relationships are
   stated in prose, and the outbound link points to the publisher's book page. The
   seven-minute badge is consistent with the reader-facing length at approximately
   200 words per minute rounded up.

4. `npm run check` passed on 2026-07-15: queue/registry/content validation, prose
   lint, pipeline tests, twenty-two Vitest tests, TypeScript and Vite production
   build, and ESLint all completed successfully. The jsdom run emitted only the
   existing non-failing `Window.scrollTo()` notices.
