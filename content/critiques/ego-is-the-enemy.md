verdict: resolved

## Critique round 1 — 2026-07-26

### Required

- `src/chapters/ego-is-the-enemy.mdx:163-164` uses “Humility is not thinking less
  of yourself” as unattributed ordinary prose. That closely reproduces the
  recognizable opening of the aphorism commonly circulated as “humility is not
  thinking less of yourself, but thinking of yourself less.” The authoring contract
  requires wording written from scratch and permits borrowed wording only as a
  short, attributed epigraph. Rewrite this takeaway in original language rather than
  retaining the borrowed construction.

### Advisory

- Figure 94.3's caption says the diagram shows either a maintenance cycle or a
  self-protective story that cuts off feedback, but the `ProcessLoop` renders only
  the constructive cycle. Tighten the caption to describe the cycle actually shown,
  or encode the alternative path if the contrast is important.

- `npm run check` passed in full on 2026-07-26: validation, prose lint, pipeline
  tests, application tests (195), TypeScript and production build, and ESLint.

## Builder resolution — 2026-07-26

- Rewrote the “If You Remember One Thing” takeaway in original language. It now asks
  the reader to see themselves accurately and let the task, facts, and next action
  outweigh the urge to appear exceptional, removing the recognizable aphorism cited
  in the required finding.
- Tightened Figure 94.3's caption to describe only the constructive maintenance cycle
  that the rendered `ProcessLoop` shows.
