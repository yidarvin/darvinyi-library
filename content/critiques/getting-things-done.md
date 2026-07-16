verdict: approve

## Critique round 1 — 2026-07-16

### Required

1. **Compress "The thesis" to the required one or two sentences.** The paragraph at
   `src/chapters/getting-things-done.mdx:13-17` contains three sentences. The
   authoring spec reserves this section for the compact argument a reader can carry
   away. Preserve the trusted external system, clarification into a next action, and
   recurring review, but express the argument in no more than two sentences.

2. **Correct Figure 52.4 so its quadrants agree with its axes and prose.** `Matrix`
   receives quadrants in top-left, top-right, bottom-left, bottom-right order. With
   time increasing left to right and energy increasing bottom to top, the current
   top-left cell is the little-time/high-energy cell, yet it is labeled `deep task`
   with the note `longer, alert stretch` (`src/chapters/getting-things-done.mdx:107-119`).
   The highlighted bottom-right cell likewise gives unexplained target status to the
   more-time/low-energy case. Relabel or rearrange the cells so every example fits its
   coordinates, and highlight a cell only if the prose identifies it as a target.

3. **Replace Figure 52.5's false nesting with a structure that depicts the review
   described in the section.** `Concentric` means core-to-outer nested layers, so the
   current rings assert that next actions sit inside projects, which sit inside
   calendar and waiting items, which sit inside future choices
   (`src/chapters/getting-things-done.mdx:122-142`). Those are not the containment
   relationships taught by the paragraph, which describes a maintenance pass across
   capture points, projects, the calendar, and stale items. Recompose this key-idea
   figure with an in-vocabulary form that shows review touching parallel system
   elements or a maintenance sequence, then align its caption and labels.

4. **Remove the unsupported reinforcing relationship from Figure 52.3.** The edge
   from `clarified item` to `next actions` uses `kind="reinforcing"`
   (`src/chapters/getting-things-done.mdx:77-96`). In the imported `NodeGraph`, that
   prop draws an accent edge with a visible plus sign and specifically denotes a
   reinforcing feedback relationship. The prose describes simple routing to a
   destination, not a feedback loop. Render this as a neutral edge, or use another
   in-vocabulary structure whose visible semantics match the classification idea.

### Advisory

1. The signature workflow uses `compoundingEdge={3}` on the reflect-to-engage edge
   (`src/chapters/getting-things-done.mdx:152-158`), even though neither the brief nor
   the Model prose identifies that transition as compounding or uniquely reinforcing.
   Removing that special edge treatment would keep the original five-stage loop while
   avoiding unexplained emphasis.

2. Within the repository's bounded evidence, the factual and copyright posture is
   otherwise sound. The chapter brief and seed metadata support the trusted-system
   thesis and identify Capture, clarify, organize, reflect, engage as the signature
   framework. The surrounding next-action, retrieval, contextual-choice, and review
   explanations are compatible with that framework and are presented in original
   thematic prose. No quotation attributable to the book, close-paraphrase evidence,
   reproduced source figure, or real cover art was identified. No separate
   chapter-specific evidence dossier exists, and this review began no external web
   search.

3. Apart from the required findings, the anatomy and implementation are strong. Five
   key ideas each have a captioned vocabulary figure; the Model renders the required
   five stages; the four exercises prescribe observable actions; the caveat usefully
   separates commitment management from priority choice; and the takeaway is concise.
   All three related slugs resolve to completed chapters, their relationships are
   stated in prose, and the outbound link targets the publisher. A direct static
   render contains approximately 1,289 reader-visible words, supporting the existing
   seven-minute badge at roughly 200 words per minute, rounded up.

4. `npm run check` passed on 2026-07-16: queue, registry, critique, and content
   validation; prose lint; both pipeline tests; all 108 Vitest tests; TypeScript and
   the Vite production build; and ESLint. Vitest emitted only the existing non-failing
   jsdom `Window.scrollTo()` notices. The directly imported Hero, ShelvedNearby,
   Concentric, Iceberg, Matrix, NodeGraph, ProcessLoop, and Spectrum components, plus
   their transitive cover, registry, SVG, and MDX helpers, render without build errors.

## Builder resolution — 2026-07-16

- Compressed **The thesis** to two sentences while retaining the trusted system,
  clarified next action, and recurring review.
- Corrected Figure 52.4 to the Matrix component's top-left, top-right, bottom-left,
  bottom-right order. Its low-energy, little-time **small admin action** cell is now
  the only highlighted target, matching the surrounding prose.
- Replaced Figure 52.5's concentric containment claim with a Flow-based review pass:
  empty capture points, scan projects, look ahead at the calendar, and remove stale
  items. Updated its caption and the registry's diagram metadata to `flow`.
- Changed Figure 52.3's intake-to-next-actions connection to a neutral edge, removing
  the unsupported reinforcing-feedback mark.
- Removed the unexplained compounding treatment from the Model loop's reflect-to-engage
  edge.

## Critique round 2 — 2026-07-16

### Required

1. **Separate the colliding labels in Figure 52.2.** The chapter places
   `markerLabel="begin here"` at `marker={0.82}` while the Spectrum component draws
   the long right-pole label `next physical action` on nearly the same baseline
   (`src/chapters/getting-things-done.mdx:52-63`). In the imported component, those
   labels land at approximately `(286, 78)` and `(340, 74)` in the same 380-unit
   viewBox (`src/components/diagrams/Spectrum.tsx:84-110`). Their text spans overlap,
   and uniform SVG scaling preserves the collision on a phone. Remove or move the
   marker label, shorten the competing labels, or choose another in-vocabulary
   composition so each label can be read independently.

2. **Make Figure 52.5 readable at 360px.** Four Flow steps produce a 558-unit-wide
   viewBox, but the chapter passes `className="block w-full"`
   (`src/chapters/getting-things-done.mdx:128-138`). That forces the whole sequence
   into the Figure's padded mobile width instead of giving the existing
   `overflow-x-auto` wrapper a wider child to scroll. At a 360px viewport, the
   component's 11.5-unit labels shrink to roughly 6px, before accounting for their
   multi-line wrapping, so the maintenance sequence fails the spec's phone-legibility
   requirement. Give this chapter-local diagram a suitable minimum width so it can
   scroll, or use an in-vocabulary composition that remains legible without changing
   the shared component.

### Advisory

1. All four required findings from round 1 are resolved in the current draft. The
   thesis is two sentences; Figure 52.4's examples now match the Matrix coordinate
   order; Figure 52.5 now represents review as a sequence rather than false nesting;
   Figure 52.3 uses neutral routing edges; and the unexplained compounding edge is gone
   from the Model.

2. The bounded repository evidence supports the core factual structure. The chapter
   brief and seed metadata identify a trusted external system as the thesis and
   Capture, clarify, organize, reflect, engage as the signature framework. No separate
   evidence dossier for this chapter was found. The surrounding operational guidance
   is presented as original synthesis, with no source quotation, close-paraphrase
   evidence, reproduced book figure, or real cover art identified. This review began
   no external web search.

3. Apart from the two figure defects, the required anatomy is complete and coherent:
   five key ideas have captioned vocabulary diagrams, the signature model is present,
   the four exercises prescribe observable actions, the caveat distinguishes managing
   commitments from choosing them, and the final takeaway is concise. The three
   related slugs resolve to completed chapters, and the outbound link targets the
   publisher.

4. `npm run check` passed on 2026-07-16. Validation, prose lint, both pipeline tests,
   all 108 Vitest tests, TypeScript, the Vite production build, and ESLint completed
   successfully. Vitest emitted only its existing non-failing jsdom
   `Window.scrollTo()` notices.

## Builder resolution — 2026-07-16

- Removed Figure 52.2's `begin here` marker caption while retaining the marker and
  its two poles, so the marker no longer competes with the right-pole label.
- Set Figure 52.5's four-step Flow to `min-w-[558px]`, its native viewBox width.
  The existing Figure overflow wrapper now preserves its 11.5-unit step labels at
  phone width and provides horizontal scrolling rather than shrinking the sequence.

## Critique round 3 — 2026-07-16

### Required

None.

### Advisory

1. Both required findings from round 2 are resolved. Figure 52.2 retains the useful
   spectrum marker without rendering the competing marker caption, so its pole and
   zone labels remain distinct. Figure 52.5 now has `min-w-[558px]`, matching the
   Flow component's native four-step viewBox width; the surrounding Figure component
   supplies horizontal scrolling at phone width instead of shrinking the labels.

2. The earlier factual and copyright assessment still holds within the repository's
   bounded evidence. The brief and seed metadata support the trusted-system thesis
   and the five-stage Capture, clarify, organize, reflect, engage framework. No
   separate evidence dossier exists, and this review began no external web search.
   The draft uses original thematic prose and original vocabulary diagrams; no source
   quotation, close paraphrase evidence, reproduced book figure, unsupported claim
   that changes the reader's understanding, or real cover art was identified.

3. The finished anatomy is complete and coherent. Five key ideas each have a
   captioned structural diagram, the signature workflow appears in the Model section,
   the four exercises prescribe observable actions, the caveat distinguishes managing
   commitments from choosing them, and the final takeaway is concise. All three
   related slugs resolve to completed chapters, and the outbound link targets the
   publisher.

4. `npm run check` passed on 2026-07-16. Queue, registry, critique, and content
   validation; prose lint; both pipeline tests; all 108 Vitest tests; TypeScript; the
   Vite production build; and ESLint completed successfully. Vitest emitted only the
   existing non-failing jsdom `Window.scrollTo()` notices.
