verdict: approve

## Critique round 1 — 2026-07-15

### Required

1. **Do not define all speculation as a forecast about the next buyer.** The
   opening correctly describes an investment through analysis, protection of
   principal, and a reasonable return (`src/chapters/intelligent-investor.mdx:13-18`),
   but the first key idea then says a speculator necessarily begins with an
   expectation about a later buyer, and Figure 19.1 reduces speculation to a price
   forecast that depends on future buyers (`:29-50`). That is materially narrower
   than Graham's boundary. An operation can be speculative because its analysis or
   protection against loss is inadequate even when its thesis is not a greater-buyer
   forecast. Keep price forecasting as one example, and make the prose and comparison
   define speculation as the residual category outside the stated investment test.

2. **Keep Figure 19.2's value labels inside the Bars viewport.** `Bars` places each
   value label at `trackX + trackW * value + 6` in a 380-unit viewBox
   (`src/components/diagrams/Bars.tsx:23-25,31-34,52-55`). With the chapter's values,
   `estimated from evidence` begins at about x=260 and extends past x=398, while
   `expectations added` begins at about x=326 and extends past x=433
   (`src/chapters/intelligent-investor.mdx:68-75`). Both meaning-bearing labels are
   clipped at every rendered width. Shorten or recompose the chapter-local bars so
   every complete label remains visible without changing the shared component.

3. **Remove Figure 19.3's internal label collision.** The shared `Spectrum` draws
   the right pole at y=74 and the marker caption at y=78. At `marker={0.74}`, the
   chapter's `room for error` caption occupies the same horizontal region as the
   long `price well below estimate` pole, so the two labels overlap at every scale
   (`src/chapters/intelligent-investor.mdx:93-103`; `Spectrum.tsx:92-110`). Shorten,
   move, or remove the chapter-local marker caption so the safety spectrum is
   separately legible.

4. **Recompose Figure 19.4 so its fork matches the idea and its labels remain
   phone-legible.** The shared branching `Flow` always forks from the final step,
   so this figure currently runs `choose your role` through `follow the policy` and
   only then branches into the defensive and enterprising roles
   (`src/chapters/intelligent-investor.mdx:120-126`; `Flow.tsx:24-29`). The prose
   says the role choice determines the program, not that the role is an outcome of
   following one. The same three-step branching Flow has a 578-unit viewBox; at the
   chapter's 520 px minimum, its 11.5-unit step and outcome labels render at about
   10.3 CSS px, below the phone-legibility floor used by completed chapters. Use a
   structurally accurate form or sequence and preserve a chapter-local authored
   width of roughly 560 px if the branching Flow remains.

5. **Compute the Hero badge from the rendered page.** A local render of the exact
   chapter contains about 1,691 visible words, including headings, captions, and
   diagram labels. At the specified approximately 200 words per minute, rounded up,
   the badge should read 9 minutes, not `minutes={10}`
   (`src/chapters/intelligent-investor.mdx:5-9`).

6. **Complete the registry record required for a finished chapter.** The
   `intelligent-investor` entry currently stops at `status: "draft"` and omits the
   authoring contract's required `tier`, `thesis`, `framework`, and diagram-form
   inventory (`content/registry.json:376-384`). Populate those fields from the seed,
   brief, and the six figures actually rendered before approval.

### Advisory

1. Within the repository's bounded evidence, the draft otherwise carries through
   the brief's core thesis and combined Mr. Market / margin-of-safety model. It uses
   original thematic prose, no quotation or real cover art, five key ideas with
   captioned shared-vocabulary figures, four concrete exercises, and a useful
   caveat that separates enduring principles from dated numerical screens. The
   repository contains no chapter-specific evidence dossier beyond the brief and
   seed metadata, and this review began no external web search.

2. Figure 19.5 marks the `evidence → policy` and `policy → action` edges as
   `reinforcing`, which makes the shared `NodeGraph` draw plus signs that conventionally
   indicate amplifying feedback. The prose describes a decision loop, not positive
   amplification. Plain edges would make the visual grammar more precise.

3. Figure 19.6 sends every `thin buffer or premium` case to `wait`, while the prose
   correctly allows a sufficiently high price to prompt selling or trimming as well
   as inaction. Framing the figure explicitly as a purchase screen, or broadening
   that branch label, would align the signature diagram more closely with the text.

4. The three nearby slugs resolve to done chapters, and the outbound URL is a direct
   publisher link recorded in the draft. The footer still shows covers without the
   one-clause relationship notes requested by the cross-linking guidance. Adding
   those relationships later would improve the library graph without blocking this
   chapter.

5. `npm run check` passed on 2026-07-15: queue, registry, critique, and content
   validation; prose lint; both pipeline tests; all 42 Vitest tests; TypeScript and
   Vite production build; and ESLint. Vitest emitted only the existing non-failing
   jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-15

1. Rewrote the investment/speculation distinction so the three-part investment test
   defines investment, and speculation is the residual category outside it. The
   comparison now identifies price forecasting as one speculative case rather than
   its definition.
2. Replaced the Figure 19.2 end labels with short, complete labels that fit in the
   shared `Bars` 380-unit viewport at the chapter's existing values.
3. Removed Figure 19.3's marker caption, leaving the marker and the two pole labels
   separately legible with no collision.
4. Replaced Figure 19.4's structurally incorrect branching `Flow` with a 560 px
   chapter-local `Compare` of defensive and enterprising programs. The choice now
   directly determines the program, and the labels render above the phone-legibility
   floor.
5. Corrected the Hero badge to `minutes={9}`, using the recorded rendered-word
   evidence and the required 200-words-per-minute round-up.
6. Completed the `intelligent-investor` registry record with tier, thesis, framework,
   and its six rendered diagram forms while preserving `status: "draft"`.

Also removed the misleading reinforcing signs from Figure 19.5's decision loop and
made Figure 19.6's no-buy branch explicitly allow waiting or trimming. `npm run
check` passed on 2026-07-15: validation, prose lint, both pipeline tests, 42 Vitest
tests, TypeScript/Vite build, and ESLint. Vitest emitted only the existing non-failing
jsdom `Window.scrollTo()` notices.

## Critique round 2 — 2026-07-15

### Required

1. **Finish the Figure 19.2 label repair.** The shortened captions fix three of the
   four rows, but `priced high` still begins at x=325.6 in the 380-unit `Bars`
   viewBox (`src/chapters/intelligent-investor.mdx:68-78`;
   `src/components/diagrams/Bars.tsx:20-25,31-34,52-55`). At the component's
   10-unit monospaced label size, the eleven-character caption extends to roughly
   x=392 and is clipped. Shorten or reposition that chapter-local caption so the
   complete text stays inside the viewport.

2. **Separate Figure 19.3's two pole labels.** Removing the marker caption resolved
   its collision with the right pole, but `price above estimate` and `price well
   below estimate` still share the y=74 baseline and overlap around the center of
   the 380-unit viewBox (`src/chapters/intelligent-investor.mdx:93-104`;
   `src/components/diagrams/Spectrum.tsx:15-20,44-48,92-97`). At the specified
   12-unit JetBrains Mono size, the left label runs from about x=40 to x=184 and
   the right label from about x=160 to x=340. Shorten the chapter-local poles so
   both are separately legible.

### Advisory

1. The other first-round requirements are resolved: the investment test now defines
   the investment/speculation boundary accurately; the effort choice uses a
   structurally correct comparison; the nine-minute badge retains the recorded
   rendered-word basis; and the registry contains the required tier, thesis,
   framework, and six-form diagram inventory. The decision-loop edge signs and the
   Model's no-buy outcome were also corrected.

2. Within the repository's bounded evidence, the brief and seed support the page's
   thesis and Mr. Market / margin-of-safety model, and the remaining factual claims
   are internally consistent with that framing and the recorded first-round review.
   This round began no new external web search.

3. `npm run check` passed on 2026-07-15: queue, registry, critique, and content
validation; prose lint; both pipeline tests; all 42 Vitest tests; TypeScript and
Vite production build; and ESLint. Vitest emitted only the existing non-failing
jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-15

1. Changed Figure 19.2's final value caption from `priced high` to `premium`.
   At its x=325.6 start, the seven-character caption remains inside the 380-unit
   `Bars` viewport at the shared 10-unit mono label size.
2. Changed Figure 19.3's pole labels to `premium price` and `discount price`.
   The left label now ends well before the right-aligned label begins, so the two
   poles remain separately legible on the shared spectrum.

The prior round's resolved fixes and completed registry record are preserved. `npm
run check` passed on 2026-07-15.

## Critique round 3 — 2026-07-15

### Required

None.

### Advisory

1. Both round-two diagram repairs are complete. Figure 19.2's `premium` label stays
   inside the 380-unit `Bars` viewport at its chapter-supplied value, and Figure
   19.3's shortened `premium price` and `discount price` poles remain separated on
   the shared 380-unit spectrum. The earlier structural, factual-boundary, reading
   time, and registry repairs also remain intact.

2. Re-derivation against the chapter brief, seed metadata, draft, imported
   components, and recorded earlier critique evidence supports the page's thesis,
   investment/speculation boundary, and combined Mr. Market / margin-of-safety
   model. No chapter-specific evidence dossier exists beyond those repository
   records, and this round began no external web search. No unsupported claim was
   found that materially changes the reader's understanding.

3. The draft retains the required anatomy, five key ideas with captioned
   shared-vocabulary diagrams, a signature Model figure, four concrete practice
   cards, an honest caveat, a generated typographic cover, and three related links
   that resolve to done chapters.

4. `npm run check` passed on 2026-07-15: queue, registry, critique, and content
   validation; prose lint; both pipeline tests; all 42 Vitest tests; TypeScript and
   Vite production build; and ESLint. Vitest emitted only the existing non-failing
   jsdom `Window.scrollTo()` notices.
