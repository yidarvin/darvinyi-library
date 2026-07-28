verdict: revise

## Critique round 1 — 2026-07-28

### Required

1. **Compress `The thesis` to the fixed one-or-two-sentence anatomy.** The dedicated
   block at `src/chapters/tao-of-pooh.mdx:13-17` contains four sentences, while the
   authoring spec reserves this section for the single compact argument a reader can
   carry away. Preserve Hoff's use of Pooh as an entrance to Taoist ideas, the
   distinction from passivity, and the claim that capable action need not perform
   control, but state the synthesis in no more than two sentences.

2. **Keep Figure 137.2's four-step Flow legible at a 360px viewport.** Four steps give
   the shared `Flow` a 558-unit-wide viewBox, but the chapter constrains it to
   `min-w-[380px]` at `src/chapters/tao-of-pooh.mdx:62-68`. That scale reduces the
   component's 11.5-unit step labels to about 7.8 CSS pixels and its 9-unit sequence
   numbers to about 6.1 pixels. The surrounding `Figure` can scroll horizontally, but
   only at the undersized 380px width, so it does not preserve readable type. Give the
   chapter-local SVG its native 558px minimum width, or provide an equally legible
   in-vocabulary composition.

### Advisory

1. Within the bounded local record, the chapter's factual framing is careful and
   supported. The evidence record covers Hoff's Pooh-based introduction, naturalness,
   simplicity, humility, *wu wei*, sufficiency, and trained responsiveness; the page
   clearly identifies its practical labels and all five figures as original synthesis.
   It quotes no source text, reproduces no source figure or cover art, and does not
   overstate this popular interpretation as a complete account of Taoist traditions.
   No new external web search was begun for this review.

2. The remaining anatomy and technical metadata are coherent. Five key ideas each
   have a captioned registered-vocabulary diagram; omitting the Model section matches
   both the brief and registry explanation; the four exercises are concrete; the
   caveat is substantive; all three nearby slugs resolve to done chapters; and the
   outbound link matches the publisher source recorded in the evidence file.

3. `npm run check` passed on 2026-07-28: queue, registry, critique, and chapter
   validation; prose lint; 40 queue-runner tests; 294 Vitest tests; TypeScript and the
   Vite production build; and ESLint all completed successfully. Vitest emitted only
   the existing non-failing jsdom `Window.scrollTo()` notices.
