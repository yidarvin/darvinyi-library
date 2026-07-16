verdict: approve

## Critique round 1 — 2026-07-16

### Required

1. **The five diagrams do not preserve legible label sizes at 360px.** Every chapter-local diagram invocation passes `className="block w-full"` (`src/chapters/body-keeps-the-score.mdx:39-137`), so the SVGs shrink to the inside width of `Figure` rather than becoming horizontally scrollable. At a 360px viewport, `Layout` leaves 320px for the page and `Figure` removes another 42px for padding and borders. Figure 32.3 therefore scales its 558-unit `Flow` viewBox into roughly 278px, reducing its 11.5-unit labels to about 5.7 CSS pixels. The nominally 380-unit figures also reduce 9.5-to-13-unit labels to roughly 7-to-9.5 pixels. Add chapter-local minimum widths appropriate to each viewBox so `Figure`'s existing overflow wrapper scrolls them instead of shrinking them below readable size. This is a required mobile-legibility failure even though the build gate cannot detect it.

2. **Figure 32.1 uses a spectrum whose endpoints are not parallel states.** `present cue` is an input, while `old alarm takes over` is one possible response to that input (`src/chapters/body-keeps-the-score.mdx:39-50`). The caption and prose describe two interpretations of the same cue, but the figure renders a degree running from the cue itself to one outcome. Recompose the visual so both poles or branches represent comparable responses, such as orienting to the present versus automatic protection, and keep the pause/orient intervention structurally distinct from those outcomes.

3. **The nine-minute reading badge is not supported by the final page length.** A static render contains 1,481 visible words, including headings, captions, SVG labels, exercises, callout text, generated cover metadata, and the nearby-book footer. At the specified 200 words per minute, rounded up, the badge should read eight minutes rather than nine (`src/chapters/body-keeps-the-score.mdx:5-9`).

### Advisory

1. Remove the unused `Curve` import at `src/chapters/body-keeps-the-score.mdx:3` when revising the chapter.

2. Within the bounded evidence available for this review, the draft otherwise carries the brief's thesis accurately and with appropriate restraint. It distinguishes trauma exposure from PTSD, avoids treating bodily reactions as proof of an event, frames grounding as optional and modest rather than curative, directs disrupted or unsafe readers toward qualified care, and preserves choice throughout the practice section. The recorded VA source directly supports the claim that PE, CPT, and EMDR are the best-supported PTSD psychotherapies under the 2023 VA/DoD guideline. The recorded PubMed page was blocked by an automated browser check during this pass, so its 64-participant trial detail could not be independently reopened here; no new external search was begun.

3. The required anatomy is otherwise complete. Five key ideas each have an original, captioned vocabulary diagram; the Model section is deliberately absent as the brief directs and the registry records why; the four exercises are concrete; the caveat is substantive; all three nearby slugs resolve to done chapters with relationship clauses; and the outbound publisher link points to the real book.

4. `npm run check` passed on 2026-07-16 both before and after this critique was written: queue, registry, and content validation; prose lint; both pipeline tests; all 68 Vitest tests; TypeScript and Vite production build; and ESLint completed successfully. Vitest emitted only the existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-16

- Replaced Figure 32.1's cue-to-outcome spectrum with a branching flow: a present cue moves through a separately highlighted pause-and-orient step, then branches to the comparable outcomes of responding to the room now or automatic protection.
- Added chapter-local native minimum widths to all five diagrams (440px, 380px, 558px, 380px, and 384px respectively), so the existing `Figure` overflow wrapper scrolls rather than scaling labels below their authored sizes on a 360px viewport.
- Corrected the Hero badge from 9 to 8 minutes, removed the unused `Curve` import, and updated this chapter's registry diagram record from spectrum to flow.
- `npm run check` passed after the chapter changes. It completed validation, prose lint, pipeline tests, 68 Vitest tests, production build, and ESLint; Vitest retained only the existing non-failing jsdom `Window.scrollTo()` notices.

## Critique round 2 — 2026-07-16

### Required

None.

### Advisory

1. All three required findings from round 1 are resolved. Figure 32.1 now represents the present cue, the pause-and-orient intervention, and two parallel response outcomes as a branching flow. Each diagram declares a minimum width equal to or greater than its viewBox width inside `Figure`'s horizontal overflow wrapper, preserving authored label sizes at a 360px viewport. The Hero badge is now eight minutes, and the unused import is gone.

2. The draft remains faithful to the chapter brief and appropriately careful within the recorded evidence. It treats the book's bodily framing as a lens rather than a literal storage claim, distinguishes trauma exposure from PTSD, avoids presenting sensation as proof of an event, and directs readers toward evidence-supported professional care. No new external search was begun for this round.

3. The required anatomy and technical contract are complete: five key ideas have captioned, in-vocabulary diagrams; the absent Model section matches the brief and registry; the exercises are concrete and safety-aware; the caveat is substantive; related links resolve to built chapters; and the outbound link points to the publisher's book page. `npm run check` passed on 2026-07-16, including validation, prose lint, pipeline tests, all 68 Vitest tests, TypeScript, the production build, and ESLint. Vitest emitted only the existing non-failing jsdom `Window.scrollTo()` notices.
