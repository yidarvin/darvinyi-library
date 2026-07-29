verdict: resolved

## Critique round 1 — 2026-07-28

### Required

1. **Complete the chapter's registry metadata.** The `when-breath-becomes-air` entry in
   `content/registry.json` stops at the base fields and `status: "draft"`. It has no
   thesis, framework rationale, or diagram inventory. Definition-of-done item 7 in
   `docs/authoring-spec.md` requires those fields. Record the chapter's thesis, state
   that the Model section is deliberately absent because the book has no single
   signature framework, and inventory the five forms actually used: comparison,
   core/context, timeline, flow, and assembly/contribution. `npm run check` currently
   passes, but that does not make this incomplete registry record approvable.

### Advisory

None.

## Builder resolution — 2026-07-28

- Completed the `when-breath-becomes-air` registry record with tier 3, the
  brief-supported thesis, and an explicit note that no single signature framework
  exists, so the Model section is deliberately absent and the five key ideas carry
  the argument.
- Recorded the five rendered diagram forms in page order: comparison / split, core
  / context, timeline / bar, flow / sequence, and assembly / contribution. The
  chapter remains `draft`; no queue or status transition was made.
- Preserved the existing chapter prose, evidence record, diagrams, and cross-links.
  No external search was begun. `npm run check` passed on 2026-07-28: validation,
  prose lint, pipeline tests, 314 Vitest tests, TypeScript, the Vite build, and
  ESLint all completed successfully. Vitest emitted only the existing non-failing
  jsdom `Window.scrollTo()` notices.

## Critique round 2 — 2026-07-28

### Required

1. **Make figure 146.1 encode the meeting it claims to show.** The prose says the
   medical and human questions are linked, and the caption says they “meet in a
   decision” (`src/chapters/when-breath-becomes-air.mdx:23-30`). The rendered
   `<Compare>` primitive instead places the two questions on opposing sides of a
   literal `vs` label and contains no decision node or convergence
   (`src/components/diagrams/Compare.tsx`). That changes a complementary,
   two-input relationship into an opposition and leaves the key idea's central
   structure absent from its diagram. Use an in-vocabulary form or composition
   that visibly brings both kinds of knowledge into a decision, with labels and
   caption aligned to what the figure actually renders.

### Advisory

None.

## Builder resolution — 2026-07-28

- Replaced figure 146.1's opposing comparison panels with the in-vocabulary
  assembly / contribution diagram. It now visibly routes `medical knowledge` and
  `personal priorities` into `a decision`, matching both the surrounding prose and
  the revised caption that says the inputs converge.
- Updated the complete registry diagram inventory to replace the removed comparison
  entry with `assembly / contribution (decision)` and distinguish the final legacy
  figure as `assembly / contribution (legacy)`. The Model rationale, draft status,
  prior metadata repair, prose, evidence record, and cross-links remain intact.
- `npm run check` passed on 2026-07-28 after the diagram and registry corrections.
  No external search was performed, no status transition was made, and the chapter
  remains `draft` pending independent re-review.
