verdict: resolved

## Critique round 1 — 2026-07-26

### Required

1. Compress **The thesis** to the fixed one-or-two-sentence anatomy. The current
   block uses three sentences, including a separate “not solved” sentence and its
   “It is” correction (`src/chapters/brief-history-time.mdx:13-17`). Preserve the
   useful synthesis of large cosmological questions, observable consequences, and
   acknowledged limits, but make the section the one or two sentences the authoring
   spec requires.

2. Recompute the Hero reading-time badge from the rendered page. A direct MDX render
   contains 1,329 reader-visible word tokens, including cover and Hero metadata,
   headings, captions, SVG labels, exercise titles, prose, and the nearby-book
   footer. At approximately 200 words per minute, rounded up, this is a seven-minute
   distillation, not `minutes={6}` (`src/chapters/brief-history-time.mdx:5-9`).
   Recompute after the other revisions and set the final badge from that render.

3. Complete the `brief-history-time` registry record. It currently ends after
   `status` and omits the required `tier`, `thesis`, `framework`, and `diagrams`
   fields (`content/registry.json:1642-1650`). Record the deliberate absence of a
   signature framework, as the brief requires, and inventory the five forms actually
   rendered after the diagram revision below. The authoring spec makes this metadata
   part of done even though the current validator accepts the draft.

4. Remove Figure 83.5's unsupported reinforcing-edge semantics. The edge from
   `black holes` to `quantum gravity open question` is passed as
   `kind="reinforcing"` (`src/chapters/brief-history-time.mdx:142-157`), but the
   prose claims only that black holes test the overlap between two theories. There is
   no feedback loop or signed variable by which more black holes reinforce more open
   question. The imported `NodeGraph` reserves this kind for reinforcing edges and
   renders it in the accent. Use an unsigned relationship edge, or define and support
   a genuine reinforcing mechanism rather than applying the semantic accent as
   decoration.

5. Bring the chapter's corrective scientific claims inside the recorded evidence.
   The evidence note supports the broad accounts of spacetime, the cosmic microwave
   background, event horizons, Hawking radiation as a theoretical proposal, and the
   missing quantum foundation. It does not record support for the information-paradox
   formulation or the categorical correction that the particle-pair cartoon is not
   the mechanism (`src/chapters/brief-history-time.mdx:113-116`). It also does not
   support the evaluative claim that Hawking treated speculative possibilities with
   excess confidence or the present-status claim about inflation
   (`src/chapters/brief-history-time.mdx:187-193`;
   `content/evidence/brief-history-time.md:6-10`). These claims materially teach the
   reader what the physics means and what to distrust in the book. Record evidence
   that directly supports them, or narrow/remove them so the page does not present
   unverified corrections as settled synthesis.

### Advisory

1. Figure 83.3 uses an Iceberg to place observable surroundings above the event
   horizon and three unlike statements below it: a causal constraint, a knowledge
   limit, and a misconception (`src/chapters/brief-history-time.mdx:92-103`). The
   visible-versus-hidden structure makes the broad point recoverable, so this does
   not block the round, but an outside/inside comparison or boundary flow would encode
   escape versus non-return more directly than an iceberg mass.

2. Within the repository's bounded record, the copyright posture is otherwise sound.
   The chapter uses original thematic organization, no quotation or real cover art,
   and shared vocabulary primitives rather than a reproduced source figure. The
   evidence file contains summaries rather than source excerpts, so this review could
   not perform a sentence-level close-paraphrase comparison and began no new external
   web search.

3. The remaining anatomy and wiring are sound. Five key ideas each have a captioned,
   phone-scrollable vocabulary figure; omission of a Model follows the brief; the
   three exercises are concrete; both related slugs resolve to done chapters; and the
   outbound link points to the publisher's page.

4. `npm run check` completed with `CHECK OK` on 2026-07-26. Queue and registry
   validation, prose lint, 42 pipeline tests, 171 Vitest tests, TypeScript, the Vite
   production build, and ESLint all passed. Vitest emitted only the existing
   non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-26

- Compressed **The thesis** to two sentences while retaining the large cosmological
  questions, observable consequences, and explicit limits.
- Re-rendered the completed MDX page and counted 1,336 reader-visible word tokens;
  at roughly 200 words per minute, rounded up, the Hero badge is now `minutes={7}`.
- Completed the registry record with tier 2, the Hero thesis, the deliberately absent
  signature framework, and the five rendered forms: comparison, timeline, iceberg,
  flow, and node graph.
- Changed Figure 83.5's black-hole-to-open-question connection to an unsigned
  relationship edge. Its label now describes the supported testing relationship
  without implying a feedback loop.
- Removed the unsupported information-paradox and particle-pair-mechanism corrections.
  The Hawking-radiation explanation and its figure now stay with the recorded account
  of a theoretical proposal for black holes to lose energy. The caveat no longer makes
  unsupported judgments about Hawking's confidence, observed evaporation, or the
  present status of inflation; it retains only the recorded later observations and the
  missing quantum foundation.
