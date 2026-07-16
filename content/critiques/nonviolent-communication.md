verdict: approve

## Critique round 1 — 2026-07-15

### Required

1. **Complete the `nonviolent-communication` registry metadata required by the
   content contract.** The draft record contains display metadata and `draft`
   status, but it omits `tier`, `thesis`, `framework`, and the rendered diagram
   inventory (`content/registry.json:517-525`). Add the brief-supported tier 1,
   thesis, and observation-feeling-need-request framework, then record the six
   rendered forms in order: comparison, iceberg, concentric circles, flow,
   spectrum, and flow. The validator currently permits the scaffold record while
   it remains a draft, but definition-of-done item 7 does not.

2. **Recompute the Hero reading-time badge from the rendered page.** The draft
   declares `minutes={8}` (`src/chapters/nonviolent-communication.mdx:5-9`), but a
   direct render of the MDX body contains 1,352 reader-visible words, including the
   Hero, headings, prose, diagram labels, captions, exercise titles, component
   chrome, and Shelved Nearby content. At the authoring spec's roughly 200 words
   per minute, rounded up, that is a 7-minute distillation. Recompute after the
   other revisions and set the final badge accordingly.

3. **Remove the intrinsic label collision in Figure 26.5.** The chapter places the
   `a clear ask` marker at 0.78 while the shared Spectrum renders its marker caption
   only four SVG units below the pole-label baseline
   (`src/chapters/nonviolent-communication.mdx:119-131`; `src/components/diagrams/Spectrum.tsx:92-112`).
   At that position, the centered marker caption overlaps the right-anchored
   `a request` pole label. The collision exists inside the SVG at every rendered
   scale, so the Figure wrapper's horizontal overflow cannot fix it. Revise the
   chapter-local labels or composition so both concepts remain separately legible,
   without changing the shared Spectrum component.

### Advisory

None.

### Evidence checked

- Re-derived the central claim from `prompts/notes/nonviolent-communication.md`,
  `prompts/_books.py`, and the current registry record. The available record
  supports the observation, feeling, need, request sequence and the distinction
  between requests and demands. No separate chapter-specific evidence dossier
  exists, and this review began no external web search.
- Read the chapter and every directly imported component, plus their shared SVG,
  cover, registry, and MDX wrapper dependencies. Apart from Figure 26.5's collision,
  the five key ideas each have a captioned registered-vocabulary diagram, the Model
  uses the brief's signature sequence, and the declared minimum widths are preserved
  by Figure's horizontal overflow on a phone.
- The prose is an original thematic synthesis within the bounded repository
  evidence. It contains no epigraph or real cover art, and no reproduced passage,
  close paraphrase, or traced author figure is evident. The four exercises are
  concrete, and the caveat appropriately warns against coercive use and against
  treating conversation as a substitute for safety.
- Both related slugs resolve to `done` chapters, and the prose explains each
  relationship before the footer. `npm run check` completed successfully on
  2026-07-15 with `CHECK OK`, including validation, prose lint, pipeline tests, all
  56 Vitest tests, typecheck, production build, and ESLint. Vitest emitted only the
  existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-15

- Completed the `nonviolent-communication` draft registry record with tier 1, the
  brief-supported thesis, the observation-feeling-need-request framework, and the
  six rendered forms in page order: comparison, iceberg, concentric circles, flow,
  spectrum, and flow.
- Recomputed the final rendered-page reading time from the recorded 1,352
  reader-visible words at roughly 200 words per minute, rounded up, and changed the
  Hero badge from 8 to 7 minutes.
- Moved Figure 26.5's `a clear ask` marker from 0.78 to 0.64. Its centered caption
  now remains distinct from the `a request` pole label without changing the shared
  `Spectrum` component.
- Ran `npm run check` successfully. The chapter remains `draft`; no queue or status
  transition was made.

## Critique round 2 — 2026-07-15

### Required

None.

### Advisory

None.

### Evidence checked

- Re-read the brief, seed record, registry metadata, full chapter, and every directly
  imported book and diagram component, including their SVG, cover, registry, route,
  and MDX-loading dependencies. No new external web search was begun.
- Re-derived the chapter's central claim from the recorded repository evidence. The
  thesis, five key ideas, signature observation-feeling-need-request sequence, and
  request-versus-demand distinction agree with the brief and seed record. The safety
  caveat is framed as a bounded application warning rather than a claim that changes
  the book's framework.
- Verified the round 1 resolutions in the current files. The registry now contains
  the required tier, thesis, framework, and six-diagram inventory; the Hero shows the
  recorded 7-minute calculation; and Figure 26.5's marker is at 0.64, leaving its
  caption distinct from the right pole label.
- Checked all six figures against their prose and the registered vocabulary. Every
  key idea has a captioned structural diagram, the Model renders the four-part
  signature sequence, labels fit their SVG geometry, and the chapter preserves each
  diagram's readable intrinsic width inside Figure's horizontal overflow at phone
  width.
- Confirmed both related slugs exist as `done` chapters, the prose states each
  relationship, the outbound link targets the publisher's product page, the generated
  typographic cover uses registry metadata, and no real cover art is present.
- `npm run check` completed with `CHECK OK` on 2026-07-15: validation, prose lint,
  pipeline tests, all 56 Vitest tests, typecheck, production build, and ESLint passed.
  Vitest emitted only the existing non-failing jsdom `Window.scrollTo()` notices.
