verdict: resolved

## Critique round 1 — 2026-07-23

### REQUIRED

1. **Correct Figure 71.4's reversed low-contribution quadrants.** `Matrix` consumes
   quadrant entries in top-left, top-right, bottom-left, bottom-right order, with
   the vertical axis high at the top and low at the bottom
   (`src/components/diagrams/Matrix.tsx:11-19,42-47`). This chapter defines deadline
   pressure as the high pole and little time pressure as the low pole, but assigns
   `defer / neither signal is strong` to the top-left cell and
   `trim or delegate / available work` to the bottom-left cell
   (`src/chapters/effective-executive.mdx:100-113`). The rendered top-left therefore
   says that work under deadline pressure has neither signal, while the genuinely
   low-contribution, low-pressure cell receives the trim-or-delegate action. Swap
   those two chapter-local entries so the matrix agrees with its axes, prose, and
   caption. This blocks approval because a key idea's structural diagram currently
   teaches the wrong action for two of its four cases.

The chapter otherwise follows the required anatomy. The brief explicitly says there
is no single signature model, and the registry records why the Model section is
absent. The draft presents five key ideas with five captioned forms from the shared
vocabulary, four concrete exercises, a substantive optional caveat, a generated
typographic cover, two relationship clauses for done related books, and a direct
publisher link. The registry's diagram inventory matches the chapter's rendered
sequence.

The chapter brief and registry record support the effectiveness-as-practice thesis,
the emphasis on time, contribution, strengths, priorities, and decisions, and the
deliberate absence of a signature framework. No separate chapter-specific evidence
dossier or source excerpt exists in the repository, so factual and close-paraphrase
review was bounded to those records and internal agreement among the prose, captions,
diagrams, and metadata. This review began no external web search. Within that
boundary, no unsupported claim that changes the reader's understanding, quotation,
close-paraphrase signal, reproduced figure, or real cover art was found.

`npm run check` passed on 2026-07-23: queue/registry/content validation, prose lint,
2 pipeline tests, 38 runner tests, 147 application tests, TypeScript, production
build, and ESLint all completed successfully. Vitest emitted only the existing
non-failing jsdom `Window.scrollTo()` notices. The gate does not judge whether
quadrant labels agree with their axes.

### ADVISORY

None.

## Builder resolution — 2026-07-23

Resolved REQUIRED finding 1 in `src/chapters/effective-executive.mdx`: Figure 71.4 now
passes the low-contribution, deadline-pressure case (`trim or delegate / available work`)
as the top-left quadrant and the low-contribution, little-time-pressure case (`defer /
neither signal is strong`) as the bottom-left quadrant. The right-hand actions, axis labels,
caption, highlight, five-diagram inventory, deliberately absent Model section, and existing
cross-links remain unchanged. No reusable diagram primitive or diagram-vocabulary change was
needed.
