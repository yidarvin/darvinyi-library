verdict: revise

## Critique round 1 — 2026-07-16

### REQUIRED

1. **Complete the registry record before this chapter can be done.** The
   `almanack-naval` entry contains only its identity, shelf, routes, and draft status
   (`content/registry.json:1122-1128`). The authoring spec requires a complete entry
   with `tier`, `thesis`, `framework`, and the rendered diagram inventory. Record the
   brief-aligned tier and thesis, the leverage-and-specific-knowledge signature
   framework, and all seven forms actually used by the page.

2. **Remove or substantiate the caveat's attribution to Ravikant.** The sentence
   "Ravikant has acknowledged that basic capacities and opportunity matter"
   (`src/chapters/almanack-naval.mdx:233-234`) is a factual attribution that is not
   supported by the chapter brief or by any chapter-specific evidence artifact in
   the repository. It changes how the reader understands the relationship between
   the author's position and the critique. Either add recorded evidence sufficient
   to support that attribution or rewrite the caveat as the distiller's own bounded
   criticism without assigning the concession to Ravikant.

3. **Make Figure 57.4's highlighted value label fit its SVG viewport.** The page
   gives `code or media` a value of `0.84` followed by the label `can reach many`
   (`src/chapters/almanack-naval.mdx:121-130`). In the shared `Bars` geometry, that
   places the label at about x=313 in a 380-unit viewBox, and the component renders
   it as unwrapped, start-anchored 10px monospace text
   (`src/components/diagrams/Bars.tsx:23-25,32,39,52-55`). The phrase extends beyond
   the right edge and is clipped in the inline SVG, so the key leverage comparison
   is not fully legible. Shorten or reposition the page's value label, or otherwise
   make the complete label visible within the authored viewport.

4. **Correct Figure 57.5's y-axis so it states the idea in the prose.** The section
   says leverage magnifies error as well as insight, while the single rising curve's
   y-axis reads `value or damage of being right`
   (`src/chapters/almanack-naval.mdx:133-155`). Damage is not an outcome of "being
   right," and the current label conflates the upside of sound judgment with the
   downside of error. Use a coherent impact or decision-quality axis, or encode the
   right-versus-wrong outcomes separately, so the diagram, caption, and prose agree.

5. **Remove the literal escape sequence from the signature Model label.** Figure
   57.7 passes `intersectionLabel="scalable value\nwith judgment"` as a quoted JSX
   attribute (`src/chapters/almanack-naval.mdx:192-198`). MDX compiles that value as
   `scalable value\\nwith judgment`, while `Venn` only splits labels on whitespace
   (`src/components/diagrams/Venn.tsx:64`; `src/components/diagrams/_util.ts:41-53`).
   The central label therefore renders a visible `\n` instead of a line break in the
   book's signature diagram. Pass an actual newline through a JSX expression or use
   ordinary whitespace so the shared wrapper can lay out the label correctly.

The remaining required checks hold within the repository's bounded evidence. The
brief supports the two-part wealth-and-happiness thesis and the signature combination
of specific knowledge with leverage. The page has six diagrammed key ideas, a distinct
Model figure, concrete practice cards, original thematic prose, a generated cover,
completed nearby slugs, and a bookseller link. No separate chapter-specific evidence
dossier or source excerpts are recorded, and this review began no external web search.
`npm run check` passed on 2026-07-16, including validation, prose lint, pipeline tests,
118 application tests, typecheck, production build, and lint; Vitest emitted only the
existing non-failing jsdom `Window.scrollTo()` notices.

### ADVISORY

None.

## Builder resolution — 2026-07-16

All required findings from critique round 1 are resolved.

1. Completed the `almanack-naval` registry record with tier 2, the brief-aligned
   wealth-and-happiness thesis, the leverage-and-specific-knowledge framework, and
   the seven rendered forms: comparison / split, flow / sequence, node graph,
   timeline / bar, annotated curve, iceberg, and venn / overlap.
2. Removed the unsupported attribution that Ravikant acknowledged differences in
   capacity and opportunity. The caveat now states the limitation as the
   distiller's criticism of the framework.
3. Shortened Figure 57.4's final bar label to `wide reach`, which fits inside the
   shared 380-unit SVG viewport.
4. Recast Figure 57.5 around `impact of decision`, with prose-aligned caption and
   annotation language that includes both sound and poor decisions.
5. Passed Figure 57.7's intersection label through a JSX expression, so the newline
   is an actual line break for the shared Venn label wrapper rather than a visible
   escape sequence.

`npm run check` passed on 2026-07-16. The chapter remains `draft`; no status,
queue, commit, or push action was taken.

## Critique round 2 — 2026-07-16

### REQUIRED

1. **Compress "The thesis" to the required one or two sentences.** The paragraph
   contains five sentences (`src/chapters/almanack-naval.mdx:13-17`), while the
   fixed anatomy defines this section as the one- or two-sentence compression a
   reader can carry away (`docs/authoring-spec.md:40`). Preserve the two-part
   financial-freedom and personal-freedom argument, including its bounded posture,
   but make this block conform to the content contract. Recompute the Hero badge
   from the final rendered text after the edit. The current direct render contains
   1,738 reader-visible words and correctly rounds to nine minutes at approximately
   200 words per minute; the final count, rather than the present value, controls.

2. **Keep wealth distinct from the capabilities used to build it.** The brief says
   to build wealth *through* leverage and specific knowledge and names those inputs
   as the signature model (`prompts/notes/almanack-naval.md:11-15`). The page instead
   defines wealth itself as a stock of "assets, capabilities, and relationships"
   and repeats `assets and durable capability` in Figure 57.1
   (`src/chapters/almanack-naval.mdx:29-34,40-51`). That collapses specific knowledge
   into the outcome before the Model later explains that specific knowledge,
   ownership, leverage, and judgment combine to create scalable value
   (`src/chapters/almanack-naval.mdx:181-198`). It also implies that an unembodied
   capability or relationship can keep producing value while its holder is absent.
   Revise the section and comparison labels so wealth means the durable assets or
   ownership that can produce beyond hours sold, while capabilities, judgment, and
   relationships remain resources used to create and steward those assets.

The five round-1 findings remain resolved. The registry now records the brief-aligned
tier, thesis, framework, and all seven rendered forms. Figure 57.4's value labels fit
the Bars viewport; Figure 57.5's axis, caption, and prose consistently describe
decision impact; Figure 57.7 receives a real newline through its JSX expression; and
the unsupported attribution in the caveat remains removed. The other required anatomy
is present: six key ideas each have a captioned vocabulary diagram, the signature Model
is distinct, the four practice cards are concrete, and the caveat and final takeaway
are appropriately bounded. No separate chapter-specific evidence dossier or source
excerpt is recorded, and this review began no external web search.

`npm run check` passed on 2026-07-16 after an unrestricted rerun, including queue and
registry validation, prose lint, both pipeline suites, 118 application tests,
typecheck, production build, and ESLint. The initial sandboxed run failed only because
two launchd tests were denied access to the keepalive path under `Library/Application
Support`; both passed when run with their normal filesystem access. Vitest emitted only
the existing non-failing jsdom `Window.scrollTo()` notices.

### ADVISORY

1. All four `ShelvedNearby` slugs resolve to `done` chapters, but the page renders
   only their covers and gives no one-clause explanation of each relationship. A
   short chapter-local sentence could connect *The Psychology of Money* to the use
   of wealth, *Zero to One* to scalable creation, *Deep Work* to rare capability,
   and *The Power of Now* to attention. This is non-blocking under the critique
   rubric's treatment of optional cross-link improvements.
