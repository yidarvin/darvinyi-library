verdict: revise

## Critique round 1 — 2026-07-28

### Required

1. **Compress The thesis to the fixed one-or-two-sentence anatomy.** The current
   paragraph uses four sentences: it separately states the aim, the cosmic history,
   the point not to memorize, and the evidence-and-uncertainty takeaway
   (`src/chapters/astrophysics-hurry.mdx:11-18`). Preserve the useful synthesis, but
   make this section the single compact paragraph of one or two sentences required
   by `docs/authoring-spec.md`.

2. **Keep Figures 129.1 and 129.2 at widths that preserve their phone-legible label
   sizes.** The five-segment `Timeline` has a 656-unit viewBox, but the chapter gives
   it only `min-w-[600px]`; its 9.5-unit secondary labels therefore render at about
   8.7 CSS px at the authored minimum
   (`src/chapters/astrophysics-hurry.mdx:34-46`;
   `src/components/diagrams/Timeline.tsx:20-27,54-55`). The four-step `Flow` has a
   558-unit viewBox but only `min-w-[520px]`, shrinking its 11.5-unit meaning-bearing
   labels below their authored size
   (`src/chapters/astrophysics-hurry.mdx:61-72`;
   `src/components/diagrams/Flow.tsx:27-35,83-90`). The shared Figure scroller
   already handles overflow. Preserve the primitives' native widths, or recompose
   the chapter-local figures so their complete labels remain comfortably readable
   at 360 px.

3. **Make Figure 129.4 show the reinforcing structure-formation mechanism instead
   of applying reinforcing styling to a one-way tree.** The prose correctly says
   that an overdense region attracts more matter, which strengthens the overdensity
   (`src/chapters/astrophysics-hurry.mdx:97-103`). The figure never returns matter
   growth to the density difference. It instead draws acyclic arrows from `small
   density difference` to `gravity pulls inward` and independently to
   `dark-matter scaffold`, marking those and `gas gathers → galaxy growth` as
   reinforcing (`:110-126`). In the imported `NodeGraph`, that kind denotes a
   reinforcing edge, while the vocabulary reserves the form for systems whose
   parts feed back (`src/components/diagrams/NodeGraph.tsx:13-17,31-35,94-120`).
   Recompose the figure so the positive feedback is visible and dark matter's role
   is not presented as a separate product of the initial ripple, or use neutral
   edge semantics for a defensible non-feedback account.

4. **Repair Figure 129.4's overflowing node labels as part of that recomposition.**
   `NodeGraph` places every label in a fixed 94-by-40 card and wraps only at spaces
   with a 13-character target
   (`src/components/diagrams/NodeGraph.tsx:54-55,126-133`;
   `src/components/diagrams/_util.ts:42-54`). The chapter's single-token
   `dark-matter scaffold` label cannot wrap at the hyphen, so its roughly
   20-character first token runs well outside the 94-unit card; `small density
   difference` also becomes three lines in a 40-unit-high card
   (`src/chapters/astrophysics-hurry.mdx:113-118`). Shorten or recompose the
   chapter-local labels so every complete label stays inside its node and remains
   distinct from the connections.

### Advisory

1. Figure 129.6 uses a `Compare` that inserts “vs” and visually favors cosmic
   inquiry, although the prose says wonder and rigor are partners and the section
   heading promises a relationship between cosmic scale and care
   (`src/chapters/astrophysics-hurry.mdx:155-181`;
   `src/components/diagrams/Compare.tsx:9-19,89-99`). The caption and panel text
   keep the intended epistemic point recoverable, so this does not independently
   block the round, but a neutral or sequential composition would match the prose
   more faithfully and could also carry the stewardship half of the section.

2. Calling the Sun “one ordinary star” is acceptable shorthand for a non-exotic
   main-sequence star, but it can also imply that the Sun is representative of the
   stellar population even though lower-mass stars are much more common
   (`src/chapters/astrophysics-hurry.mdx:157-161`). “One star” or a more precise
   bounded description would avoid that ambiguity.

3. Within the repository's bounded record, the central cosmology claims agree with
   the brief and the recorded NASA and ESA evidence: hot expansion and cooling,
   primordial light nuclei, recombination and the microwave background, stellar
   chemical recycling, gravitational evidence for dark matter, approximate
   5/27/68 standard-model accounting, and continued uncertainty about the dark
   components. The organization, prose, and diagrams appear original, with no
   quotation or real cover art. Because the evidence file contains source
   summaries rather than source text, this review could not perform a
   sentence-level close-paraphrase comparison and began no new external web
   search.

4. The remaining anatomy and wiring are sound. Six key ideas have captioned
   shared-vocabulary figures; omission of a Model follows the brief and is recorded
   in the complete registry entry; the three exercises are concrete; both nearby
   slugs resolve to done chapters; and the author book page is the outward link. A
   direct static render contains 1,471 whitespace-delimited reader-visible words,
   including generated component text, so `minutes={8}` is correct at
   approximately 200 words per minute rounded up.

5. `npm run check` completed with `CHECK OK` on 2026-07-28. Queue and registry
   validation, prose lint, 42 pipeline tests, 276 Vitest tests, TypeScript, the Vite
   production build, and ESLint all passed. Vitest emitted only the existing
   non-failing jsdom `Window.scrollTo()` notices.
