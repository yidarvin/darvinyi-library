verdict: approve

## Critique round 1 — 2026-07-15

### Required

1. **Render the five-part signature framework in the Model figure.** The brief names
   the five love languages as the signature model, and the Model prose calls it a
   five-part vocabulary. Figure 28.6 instead shows a two-set overlap between what one
   person offers and another receives, followed by a four-step feedback procedure. It
   never names or visually distinguishes affirming words, attentive time, thoughtful
   gifts, practical help, and welcome touch. Those five forms appear in Figure 28.5,
   but a preceding key-idea figure does not make Figure 28.6 the required hero rendering
   of the signature model. Recompose the Model figure so the five alternatives are the
   visible structure, while preserving the draft's useful warning that they are routes
   to test rather than permanent boxes.

2. **Separate Figure 28.3's colliding labels.** The shared `Spectrum` places both pole
   labels at y=74 and the marker caption at y=78. Here, `marker={0.76}` centers `chosen
   attention` at x=268, directly inside the horizontal range occupied by the
   right-aligned `present together` label ending at x=340. The two strings therefore
   overlap at every rendered scale. The chapter's minimum width and `Figure`'s overflow
   wrapper preserve that collision rather than fixing it. Shorten, move, or remove the
   chapter-local marker label, or use another in-vocabulary composition, so the figure
   remains independently legible on a phone without changing the shared component.

3. **Complete the `five-love-languages` registry record required by the content
   contract.** The draft entry has display metadata and `draft` status but omits `tier`,
   `thesis`, `framework`, and the rendered diagram inventory
   (`content/registry.json:557-565`). Add the brief-supported tier 1, thesis, and five
   love languages framework, then record the figure forms in page order, including the
   final Model composition after it is corrected. The validator permits the scaffold
   record while it is a draft, but definition-of-done item 7 does not.

### Advisory

1. Within the repository's bounded evidence, the central claim and copyright posture
   are otherwise sound. The chapter brief and `_books.py` independently record the
   mismatch thesis and five-language framework. The draft develops them in original
   thematic prose, contains no source quotation or material empirical claim beyond the
   recorded evidence, uses a generated typographic cover, and composes documented shared
   diagram forms rather than reproducing a book figure. No separate chapter-specific
   evidence dossier exists, and this review began no external web search.

2. The remaining anatomy is strong. Five key ideas each have a captioned structural
   figure, the four practice cards specify observable questions and actions, the caveat
   rejects rigid typing, coercion, and using the framework as a substitute for consent or
   safety, and the final takeaway is concise. The seven-minute badge is consistent with
   the reader-facing material at approximately 200 words per minute rounded up.

3. All three related slugs resolve to done chapters, and the outbound URL is a direct
   publisher link. The prose explains how Nonviolent Communication and Crucial
   Conversations relate to this chapter but gives no relationship clause for How to Win
   Friends, even though the cross-linking guidance asks for one per nearby book. Adding
   that clause would make the third edge useful, but it does not block approval.

4. `npm run check` completed with `CHECK OK` on 2026-07-15: queue, registry, and
   content validation; prose lint; both pipeline tests; all 60 Vitest tests; TypeScript
   and Vite production build; and ESLint passed. Vitest emitted only the existing
   non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-15

- Replaced Figure 28.6's Venn-and-procedure composition with a `NodeGraph` that visibly
  names affirming words, attentive time, thoughtful gifts, practical help, and welcome
  touch as five routes into "care that lands." The existing prose and caption retain the
  warning that these are routes to test, not permanent boxes.
- Removed Figure 28.3's `markerLabel`, leaving its marker and pole labels in separate
  vertical positions so `chosen attention` no longer collides with `present together`.
- Completed the `five-love-languages` registry entry with tier 1, the brief-supported
  thesis and framework, and the six rendered diagram forms in page order, including the
  corrected Model node graph.
- Ran `npm run check` after the changes: `CHECK OK` (validation, prose lint, pipeline
  tests, 60 Vitest tests, TypeScript/Vite build, and ESLint). The existing non-failing
  jsdom `Window.scrollTo()` notices remain.

## Critique round 2 — 2026-07-15

### Required

None. All three round 1 findings are resolved in the current draft. Figure 28.6 now
renders the five named languages as distinct routes into care that lands; Figure 28.3
retains its marker without the colliding marker caption; and the registry records the
brief-supported tier, thesis, framework, and six diagram forms. The five key ideas,
signature Model, four concrete practice cards, caveat, takeaway, related links, and
publisher link satisfy the required anatomy and technical contract.

The factual and copyright review remains bounded to the recorded local evidence as
requested. The brief, `_books.py`, and registry agree on the mismatch thesis and the
five-part framework. The chapter makes no empirical efficacy claim, uses original
thematic prose, quotes no source text, and builds its figures from the documented shared
vocabulary rather than reproducing a source figure. `npm run check` completed with
`CHECK OK` on 2026-07-15: validation, prose lint, both pipeline tests, all 60 Vitest
tests, TypeScript/Vite production build, and ESLint passed. The jsdom
`Window.scrollTo()` notices remain non-failing test-environment output.

### Advisory

1. Figures 28.5 and 28.6 now both use nearly the same six-node, five-arrow structure:
   the five forms converge on `felt care` in the key idea and on `care that lands` in
   the Model. Each figure is accurate and legible, so this does not block approval, but
   a later polish pass could give Figure 28.5 a different in-vocabulary form or a more
   distinct relation so the Model has a stronger visual reveal.

2. The round 1 cross-link advisory remains optional: the prose explains the relation
   to Nonviolent Communication and Crucial Conversations but not to the third related
   title, How to Win Friends. The link resolves and is not misleading.
