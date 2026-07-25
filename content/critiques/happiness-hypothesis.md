verdict: revise

## Critique round 1 — 2026-07-25

### Required

1. **The page does not convey the thesis recorded in the chapter brief.** The brief
   says the book tests ancient wisdom about the good life against modern psychology
   and finds that much of it holds up. The draft says only that Haidt tests "old
   advice" (`src/chapters/happiness-hypothesis.mdx:13-17`); it never identifies a
   representative piece of that wisdom, the psychological result brought to bear on
   it, or the qualification that follows. The Hero and the rest of the scroll instead
   substitute a general fit among mind, conditions, relationships, and commitments.
   That is a useful synthesis, but it leaves the book's stated hypothesis untested and
   changes the core argument a reader carries away. Make the ancient-wisdom-versus-
   evidence comparison concrete enough to deliver the brief's thesis without mirroring
   the book's chapter order or adding unsupported claims.

2. **The signature Model diagram contradicts the coordination model it is meant to
   teach.** The brief explicitly requires the elephant and rider as the hero model,
   and the prose says they must cooperate (`src/chapters/happiness-hypothesis.mdx:
   154-161`). Figure 76.7 uses `Compare`, whose component places a literal "vs"
   between two parallel panels (`src/components/diagrams/Compare.tsx:86-88`). It
   therefore depicts alternatives or opponents, not a rider steering and training
   the source of momentum described by the caption. Recompose the figure with an
   in-vocabulary form that visibly encodes direction, force, feedback, or cooperation
   between the two roles. Keep it an original abstraction rather than reproducing the
   book's figure.

3. **Figure 76.6 invents a prerequisite hierarchy that neither its prose nor the
   recorded brief supports.** The paragraph at
   `src/chapters/happiness-hypothesis.mdx:131-139` argues that sustained commitments
   create depth across craft, friendship, and citizenship. The Pyramid at lines
   141-151 instead asserts a fixed ascent from safety, to trusted people, to a project,
   to participation beyond the self. Because `Pyramid` explicitly represents lower
   tiers as prerequisites for higher ones, the figure adds both a universal sequence
   and an apex that the explanation never establishes. Use a form and labels that show
   durable engagement without turning these parallel sources of meaning into an
   unsupported needs hierarchy.

4. **Figure 76.4 does not match its own reciprocity claim.** Its caption says
   contribution, response, and repair reinforce one another, and the prose makes repair
   part of the practical rule, but the graph has no repair node
   (`src/chapters/happiness-hypothesis.mdx:95-109`). It also marks only
   `response → trust` and `trust → cooperate` as reinforcing, which the shared
   component renders in accent with plus signs, while leaving the other two links
   neutral. Nothing in the explanation supports that selective edge semantics. Include
   the stated repair mechanism and make the loop's edge meanings consistent, or narrow
   the caption and prose to the relationship the graph actually encodes.

5. **The registry record is incomplete for a chapter seeking approval.**
   `content/registry.json` records the slug, title, subtitle, shelf, routes, and draft
   status, but omits the required tier, thesis, framework, and diagram list. The
   authoring spec's definition of done requires complete metadata, and nearby completed
   entries demonstrate the expected shape. Populate those fields consistently with the
   final chapter before the next critique pass.

### Advisory

1. Within the repository's bounded evidence, no separate research dossier, source
   excerpt, or prior critique exists for this chapter; this review began no external
   web search. The draft contains no quotation or real cover art and shows no evident
   source-figure reproduction from the materials available here. Its six-idea anatomy,
   concrete exercises, caveat, related-book links, publisher link, generated cover, and
   mobile minimum widths otherwise satisfy the content contract.

2. `npm run check` passed on 2026-07-25: validation, prose lint, 2 pipeline tests, 38
   runner tests, 157 app tests, TypeScript and Vite production build, and ESLint all
   completed successfully. The app tests emitted only the existing non-failing jsdom
   `Window.scrollTo()` notices.
