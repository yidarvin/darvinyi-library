verdict: resolved

## Critique round 1 — 2026-07-15

### Required

1. **Keep Figure 7.3's value labels inside the Bars SVG viewport.** The chapter gives
   its three bars the labels `limited effect`, `meaningful effect`, and `can reshape
   the total` (`src/chapters/psychology-of-money.mdx:88-97`). The shared Bars
   implementation places each value label at `trackX + w + 6` in a 380-unit
   viewBox (`src/components/diagrams/Bars.tsx:23-25,31-34,50-55`). With this
   chapter's values, `meaningful effect` begins around x=260 and `can reshape the
   total` begins around x=334, so substantial portions extend past x=380 and are
   clipped by the root SVG at every rendered width. Revise this chapter's figure
   composition so all three meaning-bearing labels remain visible and legible,
   without editing the shared component.

### Advisory

1. The two related slugs resolve to completed chapters, but the footer shows only
   their covers. The authoring spec asks each Shelved Nearby edge to state the
   relationship in one clause. If the existing component contract permits a
   chapter-local explanation, note that *Thinking, Fast and Slow* supplies the
   judgment counterpart and *Atomic Habits* the behavioral-practice counterpart.

2. Within the repository's bounded evidence, the factual and copyright posture is
   sound. The brief and seed metadata support the behavior, patience, and “enough”
   thesis and explicitly call for no Model section. Personal financial histories,
   continuity in compounding, tail outcomes, room for error, quiet wealth, and an
   enough boundary are presented as behavioral principles rather than universal
   guarantees. The caveat properly limits those principles against structural
   constraints and personal-advice overreach. The draft uses no quotation or real
   cover art, follows a thematic organization, and uses original prose and shared
   diagram forms. The repository contains no chapter-specific source excerpts for
   closer textual comparison, and this review began no external web search.

3. Apart from Figure 7.3, the anatomy and visual mapping are sound: six key ideas
   each have a captioned in-vocabulary diagram, the deliberately absent signature
   Model agrees with the brief and registry, four exercises are concrete, the
   caveat is honest, and the final takeaway is concise. The chapter-local minimum
   widths sit inside the shared horizontal-overflow wrapper; the remaining five
   imported diagrams keep their labels visible and aligned with the prose. The
   nine-minute badge is consistent with the full rendered page, including generated
   Hero and related-cover text, at approximately 200 words per minute rounded up.

4. `npm run check` passed on 2026-07-15: queue/registry/content validation, prose
   lint, pipeline tests, eighteen Vitest tests, TypeScript and Vite production
   build, and ESLint all completed successfully. The jsdom run emitted only the
   existing non-failing `Window.scrollTo()` notices.

## Builder resolution — 2026-07-15

- Revised only Figure 7.3's chapter-level conceptual bar proportions, from `0.24`,
  `0.58`, and `0.94` to `0.12`, `0.28`, and `0.52`. The three existing
  meaning-bearing labels remain unchanged.
- With the shared Bars component's 204-unit track, the labels now begin at roughly
  x=166, x=199, and x=248. Their approximate right edges are x=250, x=301, and
  x=374, respectively, all inside the 380-unit SVG viewport at every rendered
  width.
- Preserved the existing caption, prose, six-diagram sequence, deliberate absence
  of a Model section, exercises, caveat, and cross-links. The shared Bars component
  was not edited.
