verdict: resolved

## Critique round 1 — 2026-07-25

### REQUIRED

1. **The signature Model substitutes an unsupported taxonomy for cognitive
   distortions, then contradicts its own axes.** The brief records cognitive
   distortions as the signature framework, but the Model recasts them as a new
   scope-by-certainty matrix (`src/chapters/feeling-good.mdx:96-113`). That matrix
   cannot account for several distortions the chapter itself names, including
   emotional reasoning and rule-like “should” thoughts, and the recorded brief
   supplies no basis for claiming that these two dimensions are “the most useful
   version” of the model. The visible placement is also internally wrong. `Matrix`
   orders its cells top-left, top-right, bottom-left, bottom-right and defines the
   top as high confidence (`src/components/diagrams/Matrix.tsx:11-19,42-47`), so the
   high-certainty, wide-scope corner described in the prose is top-right. The draft
   instead highlights bottom-right, puts the certain global verdict there, and puts
   the tentative question in top-left. Render the recorded cognitive-distortions
   framework as the hero model without inventing an unsupported typology, and make
   every label, highlight, axis, caption, and accessible description agree.

2. **Figure 80.5 omits the action that the key idea says interrupts the downward
   loop.** The heading, prose, and caption teach that one scheduled action can give
   the cycle a different input, but the figure contains only `low mood → withdraw →
   fewer rewarding moments → bleaker conclusion → low mood`
   (`src/chapters/feeling-good.mdx:83-94`). The accented return edge shows how the
   harmful cycle reinforces itself; no node, branch, or alternate path shows a
   planned action, new contact or accomplishment, or an interruption. Recompose the
   in-vocabulary figure so its structure teaches the stated intervention rather
   than only the problem.

3. **Figure 80.4 is not legible as authored and does not show what its caption
   claims.** `Compare` draws each 168-unit panel header as one unwrapped 13-unit
   monospace line, with only 140 units between the intended side insets
   (`src/components/diagrams/Compare.tsx:21-44`). Both supplied titles exceed that
   space, and “the careful investigator” extends beyond its panel and the 384-unit
   viewBox, so the right header is clipped at every rendered scale
   (`src/chapters/feeling-good.mdx:68-81`). The caption also promises evidence for
   and against one claim, while the panels contrast two styles of reasoning and
   never display the two bodies of evidence. Shorten or structurally wrap the
   headings and align the figure, caption, and key-idea explanation around the same
   thought-testing operation.

4. **The clinical treatment and crisis directions have no chapter-specific
   recorded support.** The caveat makes consequential claims about common
   depression treatment and gives a current U.S. crisis-contact instruction
   (`src/chapters/feeling-good.mdx:133-137`). The chapter brief and seed metadata
   contain neither claim, and the repository has no evidence dossier or source
   excerpt for this chapter. Because this guidance can change what a distressed
   reader does, it cannot rest on unrecorded general knowledge. Preserve the safety
   boundary, but record and attribute authoritative support for the treatment and
   escalation guidance, and verify that any current contact instruction is accurate.
   This review began no new external web search.

5. **The registry record is incomplete for a chapter seeking approval.**
   `content/registry.json:1583-1591` records only the identifying fields and draft
   status; it omits the required tier, thesis, framework, and diagram inventory.
   Populate those fields from the brief and the final rendered page, with all figure
   forms listed in page order, so the registry agrees with the chapter and satisfies
   the authoring spec's definition of done.

### ADVISORY

None.

The remaining anatomy is sound within the bounded recorded evidence: the page has
five key ideas, concrete practice cards, an honest safety boundary, the final
takeaway, completed related-book links, a publisher link, a generated typographic
cover, captions, and mobile overflow widths. No quotation, real cover art, apparent
close paraphrase, or apparent reproduction of a source figure was found in the
materials available here.

`npm run check` passed on 2026-07-25: queue/registry/content validation, prose lint,
2 pipeline tests, 38 runner tests, 165 Vitest tests, TypeScript and the Vite
production build, and ESLint all completed successfully. Vitest emitted only the
existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-25

Resolved every required finding while leaving `feeling-good` at `draft`.

1. Replaced Figure 80.6's unsupported scope-by-certainty matrix with an in-vocabulary `NodeGraph` that renders cognitive distortions directly: all-or-nothing thinking, overgeneralizing, mind reading, emotional reasoning, should statements, and labeling. The revised prose, caption, and explicit accessible description all present these as thought patterns to notice and test, not as a new taxonomy or diagnosis.
2. Extended the reusable `ProcessLoop` primitive with an optional accent alternate-action branch. Figure 80.5 now branches from low mood to a scheduled contact or task, and its caption and accessible description explain that this supplies an alternate input to the withdrawal loop.
3. Made the reusable `Compare` primitive calculate wrapped header and body heights. Figure 80.4 now puts evidence for and evidence against one concrete claim in its two panels, matching the key idea and caption without clipping its headings.
4. Replaced the unsupported treatment and crisis wording with linked, attributable guidance from the National Institute of Mental Health and the official 988 Suicide & Crisis Lifeline. Recorded the verified source claims in `content/evidence/feeling-good.md`.
5. Completed the `feeling-good` registry record with its tier, brief-supported thesis and framework, and the six final figure forms in page order. Its status remains `draft`.
6. `npm run check` completed with `CHECK OK` on 2026-07-25: queue/registry/content validation, prose lint, 2 pipeline tests, 38 runner tests, 165 Vitest tests, TypeScript, the Vite production build, and ESLint all passed. Vitest emitted only the existing non-failing jsdom `Window.scrollTo()` notices.
