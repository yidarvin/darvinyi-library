verdict: revise

## Critique round 1 — 2026-07-26

### Required

1. **Complete the registry record and make its diagram inventory agree with the
   rendered page.** The `tao-te-ching` entry stops after the generated identity,
   shelf, route, and draft status fields (`content/registry.json:1818-1826`). The
   definition of done also requires tier, thesis, framework, and diagram list
   (`docs/authoring-spec.md:76-85`). Add the brief-supported tier 2, the final
   thesis, the *wu wei* framework, and all six vocabulary forms in figure order.
   The current validator does not enforce these metadata fields, so the passing
   mechanical gate does not resolve this contract failure.

2. **Remove the unsupported causal loop and reinforcing polarity from the
   leadership figure.** The prose says restrained leadership clarifies purpose,
   removes obstacles, and gives capable people room to act
   (`src/chapters/tao-te-ching.mdx:94-104`). Figure 92.4 adds a directed cycle from
   clear purpose through leadership, room, and shared work back to clear purpose,
   labels the invented return edge “what reality teaches,” and marks the
   room-to-work edge as reinforcing (`src/chapters/tao-te-ching.mdx:106-121`).
   Neither the neighboring prose nor the bounded evidence establishes that feedback
   path or a positive causal sign. Recompose the figure as a neutral relationship
   map or another in-vocabulary structure that shows leadership creating room for
   others without attributing an unsupported management flywheel to the text.

3. **Correct the translator attribution on the outbound edition.** The linked
   Penguin Random House edition is translated by D. C. Lau, but the chapter expands
   that name as “Darrell D. Lau” in the reader-facing buy label
   (`src/chapters/tao-te-ching.mdx:220-224`), and the evidence record repeats the
   same incorrect expansion (`content/evidence/tao-te-ching.md:10`). Use the
   translator's published name, D. C. Lau, in both places so the page does not
   misattribute the edition it recommends.

4. **Support or narrow the textual-history claim in the caveat.** The page says
   that “manuscript discoveries and scholarship show a layered transmission” and
   that no settled single author stands behind the received eighty-one chapters
   (`src/chapters/tao-te-ching.mdx:195-205`). The recorded primary-text links
   support the work's ideas and variant wording, while the publisher record supports
   traditional attribution and a fourth-century BCE compilation date
   (`content/evidence/tao-te-ching.md:8-10`). None of the recorded evidence
   establishes the stronger manuscript-discovery and layered-transmission claim.
   Add an appropriate scholarly source to the bounded evidence and state only what
   it supports, or narrow the caveat to the attribution and compilation facts
   already recorded.

### Advisory

1. Figure 92.3 uses a directed `Flow` for what the prose and caption describe as a
   complementary relationship between structure and empty capacity
   (`src/chapters/tao-te-ching.mdx:74-92`). The sequence still conveys that leaving
   room enables use, so it does not block approval, but a future polish pass could
   make the solid/empty relationship itself visible instead of implying four
   successive stages.

2. Apart from the required findings, the anatomy and practical treatment are
   strong. Five key ideas each have a captioned vocabulary figure, the separate
   Model section renders *wu wei* as an explicitly practical synthesis, four
   exercises ask for observable actions, and the caveat rejects passivity before
   harm. The seven-minute badge is consistent with the reader-facing length at
   approximately 200 words per minute.

3. Within the repository's bounded evidence, the main conceptual claims about
   naming, yielding, useful emptiness, restrained leadership, contentment, and
   non-forcing are supported. The page uses no quotation, real cover art, or
   apparent reproduction of a source figure, and its organization is original
   thematic synthesis. All three nearby slugs resolve to done chapters, and their
   relationships are stated in prose. This review began no external web search.

4. `npm run check` completed with `CHECK OK` on 2026-07-26. Validation and prose
   lint passed; all 40 pipeline and runner tests and all 191 Vitest tests passed;
   TypeScript, the Vite production build, and ESLint passed. Vitest emitted only
   the existing non-failing jsdom `Window.scrollTo()` notices.
