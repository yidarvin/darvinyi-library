verdict: revise

## Critique round 1 — 2026-07-26

### Required

1. **Rebuild the signature model so it shows systems thinking integrating the
   other disciplines rather than inventing a causal sequence.** Figure 90.6 draws
   a directed, all-reinforcing ring from personal mastery to mental models to
   shared vision to team learning to systems thinking and back to personal
   mastery (`src/chapters/fifth-discipline.mdx:145-163`). Neither the surrounding
   prose nor the brief and recorded evidence establishes that order or those five
   positive causal links. More importantly, the brief's central claim is that
   systems thinking *binds the others together*, while the figure renders it as
   one peer stage near the end of an arbitrary cycle. Use an in-vocabulary
   structure that makes the integrating relationship legible and only draws
   directional or signed connections the prose and evidence support.

2. **Give personal mastery structural treatment as one of the five disciplines.**
   The thesis names personal mastery alongside mental models, shared vision, and
   team learning (`src/chapters/fifth-discipline.mdx:13-17`), but the key-idea
   spine gives mental models, shared vision, and team learning a full explanation
   and diagram while reducing personal mastery to the single generic sentence
   “People work on their own capability and purpose” in the Model section
   (`src/chapters/fifth-discipline.mdx:138-143`). The practice section likewise
   has no personal-mastery counterpart. Because the learning organization is the
   assigned signature model and the authoring spec requires every major idea to
   receive a structural diagram, explain what this discipline contributes and
   give it comparable structural treatment. The current five-key-idea count
   leaves room for a sixth.

3. **Complete the registry record before approval.** The
   `fifth-discipline` entry contains only the base generated fields and `status`
   (`content/registry.json:1778-1786`). It is missing the required `tier`,
   `thesis`, `framework`, and `diagrams` inventory. Add the brief-aligned metadata
   and record the diagram forms actually rendered after the visual revisions.

4. **Recompute the Hero reading-time badge from the final rendered page.** A
   direct static render of this exact draft contains approximately 1,372
   reader-visible alphanumeric tokens, including generated Hero and cover
   metadata, headings, captions, diagram labels, exercise titles, prose, and the
   nearby-book footer. At the authoring spec's approximately 200 words per
   minute, rounded up, that is a seven-minute distillation, not
   `minutes={8}` (`src/chapters/fifth-discipline.mdx:5-9`). Recompute after the
   required content and model revisions and set the badge from that final count.

### Advisory

None. Within the supplied brief and recorded evidence, the remaining prose uses
original thematic organization and wording, the five existing key-idea diagrams
match their local explanations, the exercises are concrete, the caveat is honest,
the related slugs resolve to completed chapters, and the outbound link matches
the recorded publisher source. This review began no external web search.

Mechanical verification: `npm run check` completed with `CHECK OK` on
2026-07-26. Queue and registry validation, prose lint, 40 runner tests, 185
Vitest tests, TypeScript, the Vite production build, and ESLint all passed.
Vitest emitted only the existing non-failing jsdom `Window.scrollTo()` notices.
