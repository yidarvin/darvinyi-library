verdict: resolved

## Critique round 1 — 2026-07-17

### REQUIRED

1. **Compress The thesis to the required one or two sentences.** The fixed anatomy
   defines this block as the single compact argument a reader can carry away, but the
   draft uses five sentences (`src/chapters/dare-to-lead.mdx:14-20`). The ideas agree
   with the chapter brief, yet the section expands into a contrast between compliance
   and trust rather than meeting the specified thesis form. Preserve the claim that
   courageous leadership makes uncertainty discussable through visible, repeatable
   behaviors, in no more than two sentences.

2. **Make the trust diagram match the seven behaviors stated in the prose.** The
   paragraph gives a complete seven-part paraphrase of BRAVING: clear limits, follow
   through, own an error, protect confidences, act by a stated standard, ask for help
   without shame, and assume decent intent (`src/chapters/dare-to-lead.mdx:81-86`).
   Figure 63.3 shows only five contributing behaviors, omitting the stated-standard
   and nonjudgment/help behaviors, and changes `protect confidences` to the materially
   different singular label `protect confidence`
   (`src/chapters/dare-to-lead.mdx:93-110`). Because the caption says the figure lets
   a team locate the behavior needing repair, those omissions make the structural
   diagram incomplete. Include all seven prose concepts with labels that retain their
   meaning, while keeping the figure sparse and phone-legible.

3. **Recompose Figure 63.5 so it teaches the causal culture mechanism in its prose and
   caption.** The section says a leader's response to candor changes the perceived
   cost of speaking, which changes whether useful information arrives next time
   (`src/chapters/dare-to-lead.mdx:135-148`). The current spectrum only places
   `visible repair` at an unexplained numeric position between `self-protection` and
   `shared courage`, with outcome zones at either end
   (`src/chapters/dare-to-lead.mdx:149-159`). It does not show a leader response, the
   team's learned inference, repetition, or the claimed effect on future candor. Use
   an in-vocabulary form that encodes that relationship, such as a flow from response
   to learned safety to earlier information, or a parallel comparison of punitive
   and constructive responses. Do not imply a measured 0.72 position for a
   qualitative claim.

4. **Recompute the Hero reading-time badge from the final direct render.** The badge
   says eight minutes (`src/chapters/dare-to-lead.mdx:8-12`), which would require more
   than 1,400 visible words at the specified approximately 200 words per minute. The
   entire MDX source currently contains only 1,167 alphanumeric word tokens even when
   imports, component and prop names, slugs, URLs, and other non-rendered syntax are
   counted; the shared components add only short metadata and repeated cover labels.
   The visible reading count therefore cannot support eight minutes and will shrink
   again when the thesis is compressed. Record a direct-render count after resolving
   the content findings and round it up at approximately 200 words per minute.

The broad thesis and the deliberate absence of a Model section agree with the chapter
brief and registry. The page otherwise has five key ideas, five captioned figures from
the shared vocabulary, four concrete practice cards, a careful power-aware caveat, a
generated typographic cover, four related slugs that resolve to done chapters, and a
direct publisher URL. No chapter-specific evidence record exists beyond the brief and
registry, so factual re-derivation was limited to those local records and internal
agreement among the prose, captions, and diagrams. This review began no external web
search.

`npm run check` passed on 2026-07-17: queue/registry/content validation, prose lint, 2
pipeline tests, 37 runner tests, 130 application tests, typecheck, production build,
and ESLint all passed. Vitest emitted only the existing non-failing jsdom
`Window.scrollTo()` notices.

### ADVISORY

1. Figure 63.1 introduces Brown's term `a rumble` only inside the diagram, without
   defining it in the surrounding explanation (`src/chapters/dare-to-lead.mdx:42-53`).
   A plain label such as `curious conversation`, or one short definition in the prose,
   would make the contrast self-contained for a reader who does not know the book's
   vocabulary.

2. `ShelvedNearby` renders four relevant completed books, but the page gives no
   one-clause explanation of each relationship
   (`src/chapters/dare-to-lead.mdx:205-209`). Adding a short chapter-local relationship
   note would satisfy the authoring spec's cross-link guidance more fully; cross-link
   enrichment remains advisory under the critique rubric.

## Builder resolution — 2026-07-17

- Compressed **The thesis** to two sentences while retaining the claim that visible,
  repeatable practices make uncertainty discussable and create the candor difficult
  work needs.
- Expanded Figure 63.3's trust graph to all seven behaviors named in its prose:
  clear limits, follow-through, owning an error, protecting confidences, acting by a
  stated standard, asking for help without shame, and assuming decent intent.
- Replaced Figure 63.5's qualitative spectrum and arbitrary numeric marker with a
  three-stage Flow: leader response to candor, the team's learned cost of speaking,
  and future candor bringing information earlier.
- Directly rendered the final chapter body and counted 1,331 visible word tokens.
  At approximately 200 words per minute, rounded up, the Hero badge is now
  `7-min distillation`.
- Ran `npm run check` before recording this resolution. It passed validation, prose
  lint, pipeline tests, application tests, typecheck, production build, and ESLint.
