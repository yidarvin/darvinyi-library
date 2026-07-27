verdict: revise

## Critique round 1 — 2026-07-27

### Required

1. **Do not present the three practices as a supported three-way intersection.**
   The brief names retrieval, spacing, and interleaving as the signature framework,
   but it does not say that durable learning exists only where all three coincide
   (`prompts/notes/make-it-stick.md:11-14`). The recorded studies support retrieval,
   distributed practice, and category discrimination separately; they record no
   interaction result showing that the three reinforce one another
   (`content/evidence/make-it-stick.md:9-12`). Figure 97.6 nevertheless uses the
   `Venn` form, whose geometry explicitly means overlapping sets meeting at a shared
   intersection, and labels that intersection “durable, usable learning”
   (`src/chapters/make-it-stick.mdx:150-169`;
   `src/components/diagrams/Venn.tsx:8-13,33-43`). Together with “work as a
   system” and “reinforce one another,” this changes a trio of complementary
   strategies into an unsupported claim of joint necessity or synergy. Recompose
   the Model so it presents three complementary moves without asserting an
   unrecorded interaction, or record evidence specific enough to support that
   stronger model.

2. **Make Figure 97.4 teach the related mix without overlapping labels or favoring
   the wrong endpoint.** The chapter places `related mix` at 0.52 while the right
   pole reads `many unrelated tasks`
   (`src/chapters/make-it-stick.mdx:107-119`). The shared `Spectrum` renders both
   pole labels at y=74 and the default marker caption at y=78; at 0.52 the marker
   is x=196, where the long right-aligned pole label also begins
   (`src/components/diagrams/Spectrum.tsx:43-47,95-121`). The two meaning-bearing
   labels therefore overlap in the SVG coordinate system, and scaling or horizontal
   scrolling cannot separate them. The same primitive also gradients toward an
   accent right endpoint even though this chapter labels that endpoint “too
   scattered to learn from,” while the prose and caveat define interleaving as a
   related mix and unrelated mixing as noise
   (`src/chapters/make-it-stick.mdx:97-105,198-206`). Recompose or relabel the
   chapter-local figure so the middle target is independently legible and the
   visual emphasis does not identify the bad endpoint as the destination.

3. **Support or narrow the causal guidance that falls outside the bounded evidence
   record.** “Elaboration gives a fact handles” is one of five major ideas and says
   that adding reasons, examples, contrasts, pictures, and prior connections gives
   a later cue more ways to find an idea
   (`src/chapters/make-it-stick.mdx:122-148`). The evidence record expressly says
   its research sources inform retrieval, spacing, interleaving, and the book's
   scope, and its author-associated summary lists retrieval, spacing,
   interleaving, errors, and metacognition, but it records no elaboration source
   (`content/evidence/make-it-stick.md:3-12`). The spacing section also prescribes
   pulling the next review closer after a difficult retrieval, while the recorded
   spacing synthesis supports only that the best interval varies with the intended
   retention interval (`src/chapters/make-it-stick.mdx:74-82`;
   `content/evidence/make-it-stick.md:10`). These are actionable causal claims, not
   decorative examples. Record support from which both can be re-derived, or narrow
   and attribute the statements to the book's recommendations rather than presenting
   them as established effects.

4. **Complete the registry metadata before approval.** The `make-it-stick` entry
   ends after `status: "draft"` and has no `tier`, `thesis`, `framework`, or
   `diagrams` fields (`content/registry.json:1914-1922`). Definition-of-done item 7
   requires those fields, including an inventory that matches the diagram forms
   actually rendered. `npm run check` does not enforce that richer metadata
   contract, and `scripts/mark.py` changes only status, so the passing gate cannot
   repair the omission.

### Advisory

1. Figure 97.3's caption compares several returns with “one long sitting,” but the
   timeline renders only the spaced sequence and no long-sitting baseline
   (`src/chapters/make-it-stick.mdx:84-95`). The surrounding prose makes the
   intended comparison recoverable, so this does not independently block approval,
   but a caption limited to what the timeline actually shows would be more precise.

2. Apart from the required findings, the fixed anatomy is intact. Five key ideas
   each have a captioned shared-vocabulary figure; the Model section is present;
   four exercise cards specify observable actions; the caveat rejects difficulty
   without instruction, feedback, and useful structure; and all three nearby slugs
   resolve to done chapters with their relationships stated in prose. The outbound
   publisher link matches the recorded evidence. A direct server render contains
   1,491 reader-visible alphanumeric tokens, consistent with the eight-minute Hero
   badge at approximately 200 words per minute rounded up.

3. The page uses original thematic prose, no quotation or real cover art, and
   shared diagram primitives rather than an apparent reproduction of a source
   figure. This review used only the chapter brief and recorded evidence and began
   no external web search.

4. `npm run check` completed with `CHECK OK` on 2026-07-27. Queue, registry,
   critique, and content validation; prose lint; all 40 pipeline and runner tests;
   all 201 Vitest tests; TypeScript and the Vite production build; and ESLint
   passed. Vitest emitted only the existing non-failing jsdom
   `Window.scrollTo()` notices.
