verdict: revise

## Critique round 1 — 2026-07-16

### REQUIRED

1. **Compress "The thesis" to the required one or two sentences.** The block is a
   five-sentence paragraph (`src/chapters/think-and-grow-rich.mdx:13-17`), while the
   fixed anatomy defines this section as the one- or two-sentence compression a
   reader can carry away (`docs/authoring-spec.md:37-40`). Preserve both sides of
   the current synthesis, Hill's claim that desire, faith, planning, and persistence
   organize effort toward wealth, and the page's bounded refusal to treat thought as
   a wealth-producing mechanism, but make the block conform to the contract.
   Recompute the Hero reading-time badge from the final rendered text after the
   edit.

2. **Separate Figure 58.2's marker label from its right-pole label.** The chapter
   places `repeatable action` at marker `0.72` while the right pole reads
   `commitment` (`src/chapters/think-and-grow-rich.mdx:59-69`). In the shared
   `Spectrum`, the pole labels sit at y=74 in 12-unit monospace and the marker label
   sits at y=78 in 10-unit monospace; marker 0.72 centers the latter at x=256 while
   `commitment` is end-anchored at x=340
   (`src/components/diagrams/Spectrum.tsx:31-35,86-91,103-105`). Their horizontal
   spans overlap by roughly 35 to 40 viewBox units on nearly the same baseline, so
   the meaning-bearing labels overwrite one another at every rendered width. Change
   this chapter's marker position or label composition so both labels are distinct
   and fully legible without editing the shared component.

The other required checks hold within the repository's bounded evidence. The brief
supports the desire, faith, organized-planning, and persistence thesis and explicitly
requires no Model section. The page has six key ideas, each with a captioned diagram
from the shared vocabulary; the other five figures retain legible authored widths
inside `Figure`'s horizontal-overflow wrapper. The four practice cards specify
observable actions and review rules. The mandatory caveat plainly limits the book's
research and causal claims; the recorded historical account supports the Nasaw
attribution, while the brief independently records the disputed Carnegie and
interview story. Both nearby slugs are done, their relationships are stated, the
outbound link points to the foundation's book shop, the generated cover uses no real
cover art, and the registry record is complete. No separate chapter-specific source
excerpt or evidence dossier is recorded, and this review began no new external web
search.

`npm run check` passed on 2026-07-16 with normal filesystem access, including queue
and registry validation, prose lint, 34 pipeline tests, 120 application tests,
typecheck, production build, and ESLint. The initial sandboxed run failed only
because two launchd tests were denied access to the keepalive path under
`Library/Application Support`; both passed in the required unrestricted rerun.
Vitest emitted only the existing non-failing jsdom `Window.scrollTo()` notices.

### ADVISORY

None.
