verdict: resolved

## Critique round 1 — 2026-07-26

### Required

1. **Correct the Hero reading-time badge from the rendered page.** A direct static
   render of this exact draft contains approximately 1,538 reader-visible
   alphanumeric word tokens, including the generated cover and Hero metadata,
   headings, captions, diagram labels, exercise titles, prose, and nearby-book
   footer. At the authoring spec's approximately 200 words per minute, rounded up,
   this is an eight-minute distillation, not `minutes={9}`
   (`src/chapters/why-nations-fail.mdx:5-9`). Recompute after the other revision and
   set the badge from the final rendered count.

2. **Figure 85.2 assigns the opposite signed semantics to the outside-voice
   relationship.** The graph names its target variable `weakened outside voice`,
   then marks the edge from `concentrated political power` to that variable as
   `kind="balancing"` (`src/chapters/why-nations-fail.mdx:67-81`). The imported
   `NodeGraph` reserves that kind for a negative or balancing relationship and
   renders it dashed (`src/components/diagrams/NodeGraph.tsx:13-17,92-117`).
   Greater concentrated power should increase the weakening of outside voice under
   the prose's account, not reduce it. Either make `outside voice` the variable and
   retain a genuinely negative edge, make `weakened outside voice` increase with
   concentrated power, or use an unsigned relationship whose wording carries no
   false polarity. Keep the labels, edge semantics, caption, and self-protecting
   feedback explanation aligned.

### Advisory

1. The caveat accurately records the Albouy challenge and the Acemoglu, Johnson,
   and Robinson reply within the supplied evidence, but the rendered note gives
   readers no direct route to either paper
   (`src/chapters/why-nations-fail.mdx:210-222`;
   `content/evidence/why-nations-fail.md:7,10-11`). Linking the recorded sources at
   the relevant claims would make this otherwise useful methodological caveat
   independently traceable.

2. Within the bounded brief and recorded evidence, the copyright posture and
   remaining factual synthesis are sound. The page uses original thematic
   organization, prose, and shared vocabulary primitives, with no quotation, real
   cover art, apparent close paraphrase, or apparent reproduction of a source
   figure. This review began no new external web search.

3. The remaining anatomy and technical wiring are sound. Five key ideas have
   captioned structural diagrams, the signature inclusive-versus-extractive model
   is present, the four exercises are concrete, the registry inventory matches the
   six rendered forms, both related slugs resolve to completed chapters, and the
   outbound link matches the recorded publisher source.

4. `npm run check` completed with `CHECK OK` on 2026-07-26. Queue and registry
   validation, prose lint, 42 pipeline tests, 175 Vitest tests, TypeScript, the Vite
   production build, and ESLint all passed. Vitest emitted only the existing
   non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-26

- Recomputed 1,542 final reader-visible alphanumeric tokens at approximately 200
  words per minute, rounded up, and changed the Hero from `9-min` to `8-min`.
- Corrected Figure 85.2's signed relationship by renaming the target node to
  `outside voice`. The existing dashed balancing edge, labeled `limits`, now shows
  that concentrated political power reduces outside voice, while the three
  reinforcing edges continue to show the self-protecting extraction loop described
  in the caption and prose.
- Preserved the caveat and made its recorded evidence directly traceable by linking
  the Albouy comment and the Acemoglu, Johnson, and Robinson reply at the claims.
