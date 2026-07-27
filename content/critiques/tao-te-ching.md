verdict: resolved

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

## Builder resolution — 2026-07-26

Resolved all required findings without new external research.

1. Completed the `tao-te-ching` registry record with tier 2, the final reader-facing
   thesis, the practical *wu wei* framework, and the six rendered diagram forms in
   figure order: iceberg, spectrum, flow, node graph, comparison, and process loop.
2. Replaced the leadership figure's unsupported causal loop with an undirected node
   graph. It now maps the stated relationships among clear purpose, restrained
   leadership, room to act, and shared work, with no feedback edge or reinforcing
   polarity.
3. Corrected the linked edition's translator credit to D. C. Lau in both the outbound
   reader label and the evidence record.
4. Narrowed the caveat to the recorded publisher facts: traditional attribution to
   Lao Tzu and fourth-century BCE compilation. It retains the recorded caution that
   translation is interpretive without claiming manuscript discoveries or layered
   transmission.

## Critique round 2 — 2026-07-26

### Required

1. **Remove the unsupported compounding signal from the *wu wei* Model.** The
   Model prose supports a recurring observe-act-adjust practice, and Figure 92.6's
   caption likewise calls it recurring (`src/chapters/tao-te-ching.mdx:150-164`).
   The figure nevertheless passes `compoundingEdge={3}`, which the shared
   `ProcessLoop` API defines as the reinforcing edge and renders in accent
   (`src/components/diagrams/ProcessLoop.tsx:10-12,77-92`); the vocabulary also
   reserves that variant for a reinforcing “compounding” arrow
   (`docs/diagram-vocabulary.md:13-18`). Nothing in the bounded evidence says that
   adjusting without force compounds the next reading of conditions or makes the
   cycle self-reinforcing. Remove that prop so the return edge is neutral, or use a
   different supported encoding if the intended relation is not recurrence. The
   current accent adds a causal polarity that changes the signature framework
   beyond what the chapter establishes.

### Advisory

1. The round 1 required findings are resolved in the current files. The registry
   now carries the required metadata and six-form inventory
   (`content/registry.json:1818-1836`); Figure 92.4 no longer contains a return edge
   or polarity; the outbound edition and evidence credit D. C. Lau; and the caveat
   is limited to the attribution, compilation date, and translation caution
   recorded in the evidence.

2. Figure 92.4's new undirected lines avoid the unsupported management flywheel,
   but verb labels such as “clarifies” and “removes friction” still read as if they
   have a direction (`src/chapters/tao-te-ching.mdx:106-121`). The caption and prose
   make the intended relationships recoverable, so this does not block approval.
   Noun-phrase edge labels would make a future neutral map less ambiguous.

3. The earlier advisory about Figure 92.3 remains settled. Its directed sequence is
   a less exact fit than a solid-space relationship, but it still communicates the
   practical move from leaving room to making use possible and does not mislead
   enough to become required.

4. Apart from the required Model encoding, the draft meets the content contract.
   It has five distinct key ideas with captioned vocabulary diagrams, an explicit
   signature Model, four concrete exercises, an honest misreading and translation
   caveat, a concise takeaway, and three resolved nearby links. The conceptual
   claims remain supportable from the brief and recorded evidence; no quotation,
   source-figure reproduction, or close paraphrase is apparent. This review began
   no new external web search.

5. `npm run check` completed with `CHECK OK` on 2026-07-26. Validation and prose
   lint passed; all 40 pipeline and runner tests and all 191 Vitest tests passed;
   TypeScript, the Vite production build, and ESLint passed. Vitest emitted only
   the existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-26

Resolved the round 2 required finding. Removed `compoundingEdge={3}` from Figure
92.6's `ProcessLoop`, so all arrows now render as neutral recurrence. The Model
still expresses the supported observe-act-adjust practice without implying that
the return from adjustment reinforces or compounds the next cycle.
