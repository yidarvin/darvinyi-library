verdict: approve

## Critique round 1 — 2026-07-16

### Required

1. **Compress "The thesis" to the required one or two sentences.** The paragraph at
   `src/chapters/paradox-of-choice.mdx:13-20` contains four sentences. The authoring
   spec reserves this section for the compact argument a reader can carry away.
   Preserve abundance, comparison work, doubt, and a bounded stopping standard, but
   express the thesis in no more than two sentences.

2. **Recompose Figure 50.1 so its arrows encode the relationship described in the
   prose.** The current `Flow` reaches `action or delay` and only then branches to `a
   clearly better fit` or `another close call` (`src/chapters/paradox-of-choice.mdx:35-42`).
   In the section's explanation, finding a better fit is the benefit an added option
   may supply, while another close call adds comparison work and can produce delay.
   Those are inputs or intermediate consequences, not outcomes that follow action or
   delay. Use an in-vocabulary structure whose direction makes the useful-fit path and
   comparison-burden path legible, and keep the caption aligned with that structure.

3. **Correct the opportunity-cost terminology in the third key idea.** The paragraph
   calls the continued salience of rejected alternatives `the opportunity cost of
   attention` (`src/chapters/paradox-of-choice.mdx:76-83`). Opportunity cost is the
   value of the best foregone alternative; attention returning to several imagined
   outcomes is a related psychological burden, but it is not that definition. Either
   explain the foregone value accurately and then describe how salient alternatives
   reduce satisfaction, or rename the attentional/counterfactual effect so the page
   does not teach a different concept under the opportunity-cost label.

4. **Record evidence for, or narrow, the caveat's named empirical claims.** The
   statements about the 2000 Iyengar and Lepper jam study and later reviews and
   meta-analyses are substantive claims that shape how broadly the reader should
   trust choice overload (`src/chapters/paradox-of-choice.mdx:188-199`). Neither the
   chapter brief, seed metadata, registry, nor a chapter-specific evidence record
   supports them. Add and identify the recorded evidence behind those claims, or
   rewrite the caveat to stay within the internally supported limits already stated
   in the Model: effects depend on context, organization, expertise, time, and
   meaningful differences, with no universal option threshold.

5. **Complete the `paradox-of-choice` registry record.** The draft entry at
   `content/registry.json:994-1001` has display metadata and `status: "draft"`, but
   omits the authoring spec's required `tier`, `thesis`, `framework`, and `diagrams`
   fields. Record tier 2, the brief-supported thesis and Choice overload framework,
   and the six rendered forms in page order after Figure 50.1 is resolved.

### Advisory

1. `ShelvedNearby` receives four valid completed slugs, but the page gives no clause
   explaining why each title is related. The cross-linking guidance asks for that
   relationship context. Add a short preceding sentence if the existing component
   remains slug-only.

2. The rest of the bounded factual and copyright posture is sound. The brief and
   seed metadata support the abundance, paralysis, dissatisfaction, and choice
   overload spine; the draft uses original thematic prose, documented shared
   diagram forms, a generated typographic cover, no quotation, and no apparent
   reproduction of a source figure. No separate chapter evidence dossier exists,
   and this review began no external web search.

3. The remaining anatomy and implementation are coherent. Five key ideas each have
   a captioned structural figure, the Model presents a conceptual rather than
   numerical curve, the four exercises prescribe observable actions, the final
   takeaway is concise, all four related slugs resolve to done chapters, and the
   outbound link targets the publisher. The directly imported Hero, ShelvedNearby,
   Flow, Compare, Iceberg, NodeGraph, Timeline, and Curve components render without
   error; their declared minimum widths remain readable through Figure's horizontal
   scroller on narrow screens. A direct static render contains approximately 1,328
   reader-visible words, supporting the existing seven-minute badge at roughly 200
   words per minute, rounded up.

4. `npm run check` passed on 2026-07-16: queue, registry, critique, and content
   validation; prose lint; both pipeline tests; all 104 Vitest tests; TypeScript and
   the Vite production build; and ESLint. Vitest emitted only the existing
   non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-16

- Compressed “The thesis” to two sentences while retaining the benefit of more options,
  comparison work, doubt, and a bounded stopping standard.
- Replaced Figure 50.1’s misleading terminal branch with a directed node graph: added
  options now lead either toward a possible better fit and useful choice, or toward
  comparison work and another close call. The caption now states those two paths.
- Corrected the third key idea: opportunity cost now means the value of the best
  foregone alternative, while the lingering attention to unselected options is named
  as a related psychological burden.
- Narrowed the caveat to the internally recorded Model limits, removing the unsupported
  named study, review, and meta-analysis claims. It now states only that organization,
  expertise, time, stakes, and meaningful differences make any overload point contextual.
- Completed the registry record with tier 2, the brief-supported thesis, the Choice
  overload framework, and the six rendered diagram forms in page order.

## Critique round 2 — 2026-07-16

### Required

None. All five round 1 findings are resolved. The thesis is now two sentences;
Figure 50.1 directs added options toward either a possible better fit and useful
choice or comparison work and another close call; opportunity cost is defined as the
value of the best foregone alternative; the caveat stays within the contextual limits
supported by the recorded brief and Model; and the registry now records the required
tier, thesis, framework, and six diagram forms.

### Advisory

None. The earlier cross-link advisory is also addressed by the relationship sentence
before `ShelvedNearby`. Within the repository's bounded evidence, the draft remains
consistent with the brief and seed metadata, uses original prose and documented shared
diagram forms, includes no quotation or real cover art, and makes no material empirical
claim beyond what the recorded evidence permits. No separate chapter-specific evidence
dossier exists, and this round began no external web search.

The complete anatomy is present in order. Five key ideas each have a captioned,
in-vocabulary figure; the signature Choice overload Model is a clearly conceptual
curve; the practices are concrete; all four related slugs resolve to completed
chapters; and the outbound link targets the publisher. The direct imports and their
transitive cover, registry, SVG, and figure helpers render coherently at their declared
minimum widths. `npm run check` passed on 2026-07-16, including validation, prose lint,
both pipeline tests, all 104 Vitest tests, TypeScript, the Vite production build, and
ESLint; Vitest emitted only the existing non-failing jsdom `Window.scrollTo()` notices.
