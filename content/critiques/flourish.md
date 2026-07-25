verdict: revise

## Critique round 1 — 2026-07-25

### REQUIRED

1. **Figure 77.2 places its teaching annotation outside the flow channel.** The
   paragraph and caption say engagement is more likely when task demand is matched to
   usable skill (`src/chapters/flourish.mdx:51-64`), but the marker for “a clear next
   move” is at `(0.56, 0.51)`. The shared channel's upper boundary at that x-position
   is only `0.62 × 0.56 = 0.3472`
   (`src/components/diagrams/Curve.tsx:61-67`), so the marker appears well above the
   highlighted band, in the region the primitive labels anxiety. Move the marker into
   the band, or revise the geometry and labels so the prose, caption, visible figure,
   and accessible description teach the same challenge-skill relationship.

2. **Figure 77.3 turns parallel relationship qualities into an unsupported nested
   hierarchy.** The prose says a strong tie needs attention, trust, candor, and repair
   (`src/chapters/flourish.mdx:67-75`), while the caption says a tie “develops” through
   them. `Concentric` instead declares its first ring the load-bearing core and the
   later rings surrounding layers (`src/components/diagrams/Concentric.tsx:8-20`).
   The current labels therefore assert that shared attention is the core, trust is a
   middle layer, and repair plus mutual care are the outside layer, without support
   from the prose or recorded brief. Use an in-vocabulary form that encodes the
   stated development or reciprocity, or revise the explanation and labels to
   establish a genuine center-and-layers model.

3. **The caveat makes a consequential historical claim with no recorded support.**
   “Seligman later acknowledged” health, vitality, and responsibility as candidate
   additions (`src/chapters/flourish.mdx:181-190`) materially changes the reader's
   view of PERMA's completeness. The chapter brief and seed metadata record the five
   PERMA elements but no later statement, and the repository contains no
   chapter-specific evidence dossier or source excerpt from which this attribution
   can be re-derived. Record and attribute the evidence used for that claim, or
   narrow the caveat to criticism supported by the recorded materials. This review
   began no new external web search.

4. **Recompute the Hero reading-time badge from the rendered page.** A direct static
   render of this exact draft contains approximately 1,377 reader-visible word
   tokens, including the Hero and generated cover text, headings, captions, SVG
   labels, exercise titles, and nearby-book footer. At the authoring spec's
   approximately 200 words per minute, rounded up, that is a seven-minute
   distillation, not `minutes={8}` (`src/chapters/flourish.mdx:5-9`). Recompute the
   final value after resolving the other findings.

The remaining required checks are sound within the recorded evidence. The Hero and
thesis convey the brief's five-part account of well-being; the page has five key
ideas, a distinct PERMA Model, concrete practice cards, the required final takeaway,
completed related-book links, a direct publisher link, complete registry metadata,
and a generated typographic cover. Every figure uses a named shared primitive and
declares a mobile overflow width at or above its authored viewBox.

`npm run check` passed on 2026-07-25: queue/registry/content validation, prose lint,
2 pipeline tests, 38 runner tests, 159 UI tests, TypeScript and the Vite production
build, and ESLint all completed successfully. Vitest emitted only the existing
non-failing jsdom `Window.scrollTo()` notices.

### ADVISORY

1. Figure 77.1 labels its right panel “five questions” but renders three grouped
   rows, only one of which is phrased as a question
   (`src/chapters/flourish.mdx:40-46`). The grouping still conveys that mood is not
   the sole reading, so this does not block the key idea, but naming five contributors
   explicitly or relabeling the panel would make the visual count agree at a glance.
