verdict: approve

## Critique round 1 — 2026-07-16

### Required

1. **Compress `The thesis` to the fixed one-or-two-sentence anatomy.** The section
   currently uses six sentences to move from recurring outcomes through the system
   definition to leverage (`src/chapters/thinking-in-systems.mdx:11-18`). The Hero
   line does not replace the required Thesis block. Preserve the stocks, flows,
   feedback, and structural-intervention synthesis, but make this section the one or
   two sentences a reader can carry away.

2. **Make Figure 37.1 encode the key idea stated by its prose and caption.** The
   section says the same elements can produce different behavior when their
   connections or purpose change, but the figure shows only one static arrangement
   and contains no purpose or aim (`src/chapters/thinking-in-systems.mdx:29-56`). It
   therefore cannot display the comparison it claims. It also marks `result →
   signal` as reinforcing, which the component renders as a positive causal sign,
   although neither the prose nor the broad node labels establish that polarity
   (`src/components/diagrams/NodeGraph.tsx:13-17,81-105`). Use an in-vocabulary
   comparison of two arrangements, or otherwise make changed connections and purpose
   structurally visible; remove the unsupported polarity unless narrower variables
   justify it.

3. **Correct the emissions example so it teaches the stock-and-flow rule without a
   false implication.** “A lower emissions rate does not immediately lower
   atmospheric carbon” can imply that the lower rate will eventually lower the stock
   (`src/chapters/thinking-in-systems.mdx:58-65`). A stock falls only when total
   outflow exceeds total inflow; reducing a still-positive inflow may merely slow its
   rise. State that condition directly so this central example does not blur the
   distinction the section is meant to teach.

4. **Replace Figure 37.4 with a structural account of delayed correction and
   oscillation, or change the key idea to match what is actually drawn.** The prose
   teaches a delayed signal followed by an overcorrection and a swing, but the figure
   is a monotonic S-curve whose geometry contains no corrective action, overshoot,
   reversal, or oscillation (`src/chapters/thinking-in-systems.mdx:112-136`). The
   shared `Curve` implements `shape="s"` as a logistic rise
   (`src/components/diagrams/Curve.tsx:19-31,84-94`), so the annotations alone do not
   encode the section's central mechanism. Use a fitting vocabulary composition that
   shows the delayed feedback path and resulting correction, rather than a generic
   visibility curve.

5. **Complete the registry record and make it agree with the rendered chapter.** The
   draft entry contains only identity, shelf, route, and status fields
   (`content/registry.json:737-745`). The definition of done also requires `tier`,
   `thesis`, `framework`, and the diagram inventory. Record the brief-supported tier
   1, the final thesis, stocks/flows/feedback/leverage-points framework, and all six
   rendered figure forms in page order after resolving the figure changes above.

### Advisory

1. Within the repository's bounded evidence, the core factual and copyright posture
   is otherwise sound. The brief supports stocks, flows, feedback, and leverage
   points as the signature model; the page uses original thematic organization, no
   quotation or real cover art, and shared diagram primitives rather than a reproduced
   source figure. The repository contains no chapter-specific evidence dossier or
   source excerpts for closer factual or paraphrase comparison, and this review began
   no new external web search.

2. The remaining anatomy is strong: five key ideas each have a captioned vocabulary
   figure; the separate Model composes the signature framework; four exercises ask for
   observable work products; and the caveat treats system boundaries, responsibility,
   and model revision honestly. The seven-minute badge is plausible for the current
   reader-visible content and should be recomputed after revision.

3. `black-swan`, `thinking-fast-and-slow`, and `nudge` resolve to built chapters, and
   the outbound Chelsea Green URL points to the publisher's book page. The footer does
   not state the requested one-clause relationship for each nearby title, but this is
   advisory because the links themselves resolve and the shared footer currently
   exposes no relationship-label prop.

4. `npm run check` completed with `CHECK OK` on 2026-07-16: queue, registry, critique,
   and content validation; prose lint; both pipeline tests; all 78 Vitest tests;
   TypeScript and the Vite production build; and ESLint passed. Vitest emitted only
   the existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-16

- Compressed **The thesis** to two sentences that retain the stocks, flows, feedback,
  delays, and structural-intervention synthesis.
- Replaced Figure 37.1 with a comparison of two arrangements using the same signals and
  people, while making the changed connection, rule, and aim explicit. This removes the
  unsupported reinforcing polarity.
- Corrected the emissions example: a lower emissions rate can slow atmospheric-carbon
  growth, while the stock falls only when removals exceed emissions.
- Replaced the monotonic S-curve in Figure 37.4 with a delayed-feedback process loop that
  shows a stale report, a large correction, an overshoot, and the next corrective swing.
- Completed the draft registry record with tier 1, the final thesis, the
  stocks/flows/feedback/leverage-points framework, and the six figures in page order.

## Critique round 2 — 2026-07-16

### Required

1. **Make the revised comparison's panel titles fit inside the diagram.** Figure 37.1
   now encodes the intended change in connections, rules, and aims, but both titles are
   23-character strings (`src/chapters/thinking-in-systems.mdx:39-44`). `Compare`
   gives each panel 168 viewBox units and renders its title from 14 units inside the
   panel as one unwrapped 13px monospace line
   (`src/components/diagrams/Compare.tsx:28-35,38-54`). The left title therefore
   spills into the 20-unit gap and collides with the centered `vs` label, while the
   right title runs past its panel edge (`src/components/diagrams/Compare.tsx:73-84`).
   Shorten the two chapter labels or otherwise make them fit without collision, then
   confirm the comparison remains legible in its 420px mobile scroll width.

### Advisory

1. The other five round-1 requirements are resolved. The thesis is two sentences; the
   emissions example states the necessary stock-and-flow condition; the delayed loop
   now shows stale information, correction, overshoot, and recurrence; and the registry
   records the brief-supported tier, thesis, framework, and six diagram forms. The
   available brief and seed record support the central factual synthesis, and the repo
   contains no separate evidence dossier or source excerpts for this chapter. This
   review began no external web search.

2. `npm run check` completed with `CHECK OK` on 2026-07-16: validation, prose lint,
   both pipeline tests, all 78 Vitest tests, TypeScript, the Vite production build,
   and ESLint passed. Vitest emitted only the existing non-failing jsdom
   `Window.scrollTo()` notices.

## Builder resolution — 2026-07-16

- Shortened Figure 37.1's comparison titles to **"speed first"** and
  **"reliability first"**. Both titles now fit within the 140-unit usable title
  width of their 168-unit panels, preserving the visible connection, rule, and aim
  contrast without reaching the centered `vs` label or panel edge at the 420px
  mobile scroll width.

## Critique round 3 — 2026-07-16

### Required

None.

### Advisory

1. The round-2 diagram finding is resolved. `speed first` and `reliability first`
   fit the comparison headers without reaching the centered `vs` label or either
   panel edge. The parallel connection, rule, and aim rows still encode the section's
   stated contrast. The figure's 420px minimum width remains usable in the shared
   horizontal-overflow wrapper at phone width.

2. Re-derivation against the bounded repository evidence supports the draft's central
   claims. The chapter brief and seed record identify stocks, flows, feedback, and
   leverage points as the signature model, and the draft explains and diagrams those
   ideas without quotation, source-figure reproduction, or a real cover. No separate
   chapter evidence dossier or source excerpts are recorded, and this round began no
   external web search.

3. The fixed anatomy is complete and in order: five key ideas each have a captioned
   vocabulary figure, the Model composes the signature framework, the four exercises
   specify concrete work products, and the caveat treats boundaries, responsibility,
   counterintuitive intervention, and model revision honestly. Registry metadata lists
   the six rendered figure forms in order; all three related slugs are `done`.

4. `npm run check` completed with `CHECK OK` on 2026-07-16. Validation, prose lint,
   both pipeline tests, all 78 Vitest tests, TypeScript, the Vite production build,
   and ESLint passed. Vitest emitted only the existing non-failing jsdom
   `Window.scrollTo()` notices.
