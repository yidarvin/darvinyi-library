verdict: resolved

## Critique round 1 — 2026-07-15

### Required

1. **Make Figure 3.3's meaning-bearing labels legible at a 360 px viewport.** The
   Matrix has a 384-unit-wide viewBox and the chapter renders it at a 384 px minimum,
   leaving its quadrant notes at 9.5 CSS px and its axis labels at 10 CSS px. Labels
   such as "protect time," "handle now," and "delegate or limit" carry the practical
   distinction the figure is meant to teach, so this misses the phone-legibility
   requirement and the roughly 11 px floor established by the completed chapters.
   Increase the chapter-local rendered width or revise this chapter-local figure layout
   so its smallest meaning-bearing text remains readable inside the existing horizontal
   overflow wrapper. Do not change the shared Matrix component for this finding.

2. **Rebuild Figure 3.7 so the seven-habit signature model does not overlap itself.**
   `ProcessLoop` documents that two to six stages read well, but this instance supplies
   seven. With the component's fixed 108-unit node width, the two bottom nodes have
   centers only about 97 units apart at the same vertical position, so their boxes
   overlap by about 11 viewBox units; the two nodes beside the top node also touch.
   Scaling the SVG cannot remove that internal collision. Use an in-vocabulary,
   chapter-local composition that keeps all seven habit labels distinct and preserves
   the prose's central relationship: self-direction supports cooperation, and renewal
   restores capacity for the cycle to continue.

### Advisory

1. The copyright posture is sound in this bounded review. The chapter uses no quotation
   or real cover art, organizes the ideas thematically, gives the habits original headings
   and labels, and uses shared diagram forms rather than tracing the book's figures.

2. Apart from the two diagram findings, the page satisfies the required anatomy: a clear
   thesis and significance section, six key ideas with captioned structural figures, a
   distinct seven-habit Model section, four concrete practice cards, an honest caveat, a
   concise final takeaway, and a direct publisher link. The seven-minute badge is
   consistent with the rendered amount of text. The registry record has the title,
   author/year subtitle, shelf, tier, thesis, framework, seven-item diagram inventory,
   and draft status; the queue's `PENDING` state is the valid companion to registry
   `draft`.

3. The brief supplies the core thesis and identifies the seven habits as the signature
   model, but it includes no attached primary-source evidence for checking the chapter's
   more detailed attributions. This bounded pass used no external search. The habit
   progression and caveat are cautious and consistent with the brief, and no unsupported
   empirical claim was found that changes the reader's understanding, but a future
   evidence pass would benefit from a local primary-source excerpt or official framework
   reference.

4. Both related slugs resolve to completed chapters, but the footer presents only their
   covers and does not state the one-clause relationship requested by the cross-linking
   guidance. A short chapter-local relationship note would make those edges more useful;
   this remains advisory under the critique rubric.

5. `npm run check` passed on 2026-07-15: queue, registry, critique, and content
   validation; prose lint; pipeline tests; ten Vitest tests; TypeScript and Vite
   production build; and ESLint all completed successfully. The jsdom run emitted only
   the existing non-failing `Window.scrollTo()` notices.

## Builder resolution — 2026-07-15

1. Figure 3.3 now renders its existing 384-unit Matrix at a chapter-local minimum width
   of 448 px inside the unchanged Figure overflow wrapper. The 9.5-unit notes therefore
   render at about 11.1 CSS px, and the 10-unit axis labels at about 11.7 CSS px, at a
   360 px viewport.

2. Figure 3.7 now uses the in-vocabulary NodeGraph composition rather than a seven-stage
   ProcessLoop. Its seven separate nodes form a self-direction chain that feeds the
   cooperation chain; renewal links the end of that work back to choosing a response.
   The two reinforcing edges make the support and restoration relationships explicit
   without exceeding ProcessLoop's documented six-stage capacity.
