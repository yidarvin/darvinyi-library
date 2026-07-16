verdict: approve

## Critique round 1 — 2026-07-15

### Required

1. **Make Figure 27.1 encode all three conditions it claims to explain.** The
   section defines a crucial conversation by consequential stakes, differing
   views, and rising emotion, and the caption says those three conditions rise
   together. The shared `Matrix` receives only consequence and heat as axes, so
   disagreement is absent from the visible figure and from its generated
   accessible description. Recompose the chapter-local visual with an
   in-vocabulary form that represents all three conditions, or narrow the prose
   and caption only if the recorded concept genuinely supports a two-condition
   account. The current diagram does not structurally show the major idea it
   accompanies.

2. **Separate Figure 27.2's marker caption from its right pole label.** The shared
   `Spectrum` renders both pole labels at y=74 and the marker caption at y=78. At
   `marker={0.62}`, the centered `enough safety` label occupies the same horizontal
   region as the right-aligned `candid contribution` label, so they overlap inside
   the SVG at every scale. Figure's horizontal overflow preserves the geometry but
   cannot repair an intrinsic collision. Revise the chapter-local labels or
   composition so both concepts remain independently legible without changing the
   shared component.

3. **Complete the `crucial-conversations` registry metadata required by the
   content contract.** The draft record contains display metadata and `draft`
   status but omits `tier`, `thesis`, `framework`, and the rendered diagram
   inventory (`content/registry.json:538-545`). Add the brief-supported tier 1,
   high-stakes-dialogue thesis, and pool-of-shared-meaning framework, then record
   the six forms used in order after Figure 27.1 is corrected. The validator
   permits the scaffold record while it remains a draft, but definition-of-done
   item 7 does not.

4. **Recompute the Hero reading-time badge from the rendered page.** The draft
   declares `minutes={8}`, but a direct server render contains 1,380
   reader-visible words, including headings, prose, diagram labels, captions,
   exercise titles, and component chrome. At the authoring spec's roughly 200
   words per minute, rounded up, the current page is a 7-minute distillation.
   Recompute after the other revisions and set the final badge accordingly.

### Advisory

1. Within the repository's bounded evidence, the central claim and copyright
   posture are otherwise sound. The chapter brief and seed record support making
   high-stakes dialogue safe enough for people to contribute to a shared pool of
   meaning. The five key ideas develop that claim in an original thematic order,
   the prose contains no quotation or empirical claim stronger than the local
   record can support, the generated cover uses no real artwork, and the diagrams
   compose shared vocabulary primitives rather than tracing a source figure. No
   separate chapter-specific evidence dossier exists, and this review began no
   external web search.

2. Apart from the two required figure findings, the diagrams agree with their
   prose and fit their imported components. The iceberg separates event from
   interpretation and response, the flow makes a view testable, the comparison
   shows withdrawal and force as parallel losses of information, and the node
   graph renders the brief's pool-of-shared-meaning model. Their chapter-local
   minimum widths are preserved by Figure's horizontal-overflow wrapper on a
   phone.

3. The full anatomy is present and ordered correctly. Four practice cards specify
   observable preparation, opening, and follow-through actions; the caveat
   explicitly rejects coercive use and directs readers toward boundaries, formal
   process, or outside support under intimidation or severe power imbalance. Both
   nearby slugs resolve to `done` chapters, the prose states each relationship,
   and the outbound URL is a bookseller link.

4. `npm run check` completed with `CHECK OK` on 2026-07-15: queue, registry,
   critique, and content validation; prose lint; both pipeline tests; all 58 Vitest
   tests; TypeScript and Vite production build; and ESLint passed. Vitest emitted
   only the existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-15

- Replaced Figure 27.1's two-axis matrix with a three-set Venn. Its visible labels
  and generated accessible description now name high stakes, differing views, and
  rising emotion, which meet at a crucial conversation.
- Kept Figure 27.2's `enough safety` marker and moved it from 0.62 to 0.40 on the
  spectrum. The marker caption now ends before the right-aligned `candid
  contribution` pole label begins, so the two labels remain independently legible.
- Completed the `crucial-conversations` registry record with tier 1, the
  brief-supported high-stakes-dialogue thesis, the Pool of shared meaning framework,
  and the six rendered forms in page order: venn, spectrum, iceberg, flow,
  comparison, and node graph. Status remains `draft`.
- Recomputed the Hero badge from the rendered-page evidence at roughly 200 words per
  minute and set it to `7-min distillation`; the small figure-label substitutions do
  not change that rounded result.
- Ran `npm run check` after the changes. It finished with `CHECK OK`, including
  validation, prose lint, pipeline tests, all 58 Vitest tests, TypeScript, Vite
  build, and ESLint.

## Critique round 2 — 2026-07-15

### Required

1. **Finish resolving Figure 27.2's intrinsic label collision.** Moving the
   `enough safety` marker from 0.62 to 0.40 clears the right pole, but it moves the
   marker caption into the left pole label instead. In the shared `Spectrum`, the
   left label starts at x=40 with a 12px mono font, while the centered marker label
   sits at x=160 with a 10px mono font; `self-protection` and `enough safety`
   therefore overlap horizontally. Their baselines are y=74 and y=78, only four
   pixels apart, so the text also collides vertically at every rendered scale.
   Revise the chapter-local labels or composition so the left pole, marker caption,
   and right pole are all independently legible without changing the shared
   component. Horizontal overflow cannot repair a collision inside the SVG.

### Advisory

1. The other round 1 findings are settled. Figure 27.1 now visibly and accessibly
   encodes high stakes, differing views, and rising emotion in a three-set Venn.
   The registry contains the brief-supported tier, thesis, framework, and six-form
   diagram inventory, and the Hero now reports a 7-minute distillation.

2. The bounded factual and copyright review remains sound. The brief and seed
   record support the chapter's central claim and pool-of-shared-meaning model; no
   separate evidence dossier was found, and this review began no external search.
   The page uses original thematic organization and wording, makes no quotation or
   material empirical claim beyond the recorded evidence, and uses the shared
   diagram vocabulary rather than reproducing a source figure.

3. The remaining anatomy and implementation satisfy the rubric. Five key ideas
   each have a structural figure, the signature model is present, the four practice
   cards are concrete, the caveat rejects coercive use under unsafe conditions, and
   both related slugs resolve to done pages with a bookseller link out.

4. `npm run check` completed with `CHECK OK` on 2026-07-15: validation, prose lint,
   both pipeline tests, all 58 Vitest tests, TypeScript and Vite production build,
   and ESLint passed. Vitest emitted only the existing non-failing jsdom
   `Window.scrollTo()` notices.

## Builder resolution — 2026-07-15

- Resolved Figure 27.2's remaining intrinsic label collision by changing its left
  pole from `self-protection` to the shorter, equivalent `guarded`. At the existing
  0.40 marker, `guarded`, `enough safety`, and `candid contribution` now occupy
  separate horizontal ranges despite their nearby baselines. The caption and prose
  retain the fuller explanation that safety moves people beyond self-protection.

## Critique round 3 — 2026-07-15

### Required

None.

### Advisory

1. The remaining round 2 finding is settled. In the shared `Spectrum`, the left
   pole begins at x=40, the 0.40 marker is centered at x=160, and the right pole
   ends at x=340. At the component's declared mono font sizes, `guarded`, `enough
   safety`, and `candid contribution` occupy separate horizontal ranges. Their
   nearby baselines therefore do not produce an intrinsic collision. Figure's
   horizontal-overflow wrapper and the chapter's minimum width preserve those
   ranges on a 360px viewport.

2. The bounded factual and copyright review remains sound. The chapter brief and
   `_books.py` seed independently record the high-stakes-dialogue thesis and pool
   of shared meaning model used here. The chapter develops those ideas in original
   wording and thematic order, contains no quotation or material empirical claim,
   uses generated typographic cover treatment, and composes only the documented
   shared diagram forms. No separate chapter evidence dossier exists, and this
   review began no external web search.

3. The finished anatomy satisfies the content contract. Five key ideas each have
   a captioned structural diagram, the signature model has its own node graph, the
   four exercises are concrete, and the caveat rejects coercive use where dialogue
   is not actually safe. Registry metadata matches the brief and rendered diagram
   order; both nearby slugs are done pages, their relationships are stated in the
   prose, and the outbound link points to a bookseller.

4. `npm run check` completed with `CHECK OK` on 2026-07-15: validation, prose lint,
   both pipeline tests, all 58 Vitest tests, TypeScript and Vite production build,
   and ESLint passed. Vitest emitted only the existing non-failing jsdom
   `Window.scrollTo()` notices.
