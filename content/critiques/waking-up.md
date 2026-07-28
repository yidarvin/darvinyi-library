verdict: revise

## Critique round 1 — 2026-07-28

### Required

1. **Preserve legible label sizes for all five figures at a 360px viewport.**
   Figures 139.1, 139.2, 139.4, and 139.5 pass only `block w-full`, so their
   380- or 384-unit SVG viewBoxes shrink to the inside width of `Figure` on a
   phone (`src/chapters/waking-up.mdx:41-48,63-82,117-130,144-158`). At the
   roughly 278px available inside the figure at a 360px viewport, the primitives'
   9.5-to-13-unit labels render at approximately 7-to-9.5 CSS pixels
   (`src/components/diagrams/Iceberg.tsx:25-66`;
   `src/components/diagrams/NodeGraph.tsx:60-64,126-135`;
   `src/components/diagrams/Compare.tsx:62-80,89-100`;
   `src/components/diagrams/Spectrum.tsx:55-59,87-93,111-159`). Figure 139.3
   has a 558-unit four-step `Flow` viewBox but only a 420px minimum width, which
   still scales its 9-to-11.5-unit labels down to about 6.8-to-8.7 CSS pixels
   (`src/chapters/waking-up.mdx:96-102`;
   `src/components/diagrams/Flow.tsx:21-35,70-80`). Add chapter-local minimum
   widths appropriate to the actual viewBoxes so `Figure`'s existing horizontal
   overflow preserves the authored label sizes instead of shrinking them below
   the mobile-legibility requirement.

2. **Give the first key idea a diagram that encodes its stated distinction.**
   The section distinguishes an occurrence from the personal explanation added
   to it, using chest tightness and “I am failing” as the two events, then argues
   that noticing this gap permits a considered response
   (`src/chapters/waking-up.mdx:29-39`). Figure 139.1 instead places “the felt
   owner: 'me'” above a waterline and sights, sensations, thoughts, moods, and
   attention beneath it (`src/chapters/waking-up.mdx:41-47`). The imported
   `Iceberg` form explicitly represents a visible surface against underlying
   drivers (`src/components/diagrams/Iceberg.tsx:4-15,36-60`), so this geometry
   neither shows occurrence versus interpretation nor the gap before response.
   It largely repeats the following section's no-central-self claim. Recompose
   Figure 139.1 with an in-vocabulary structure that teaches the event,
   commentary, and response relation, or revise the key idea and caption to the
   surface-versus-underlying relation actually rendered.

3. **Support or narrow the specific meditation-risk claim.** The caveat says
   meditation can be destabilizing, especially amid trauma, severe anxiety,
   psychosis, or a major mood episode, and uses that claim to direct readers to
   stop and seek qualified care (`src/chapters/waking-up.mdx:189-198`). The
   recorded evidence supports secular inquiry into selfhood, beginner meditation,
   distinct narrative and experiential modes of self-reference, and modest
   changes in present-centered self-focus
   (`content/evidence/waking-up.md:8-27`); it records no adverse-effects or
   clinical-safety source from which this population-specific claim can be
   re-derived. Because this is consequential mental-health guidance, add recorded
   evidence specific enough to support it or narrow the callout to the
   non-clinical and epistemic limits already established by the bounded evidence.

### Advisory

1. Figure 139.5 uses a quantitative `Spectrum` and places “meditation practice”
   at an unexplained `0.78` between “adopt an answer” and “investigate
   experience” (`src/chapters/waking-up.mdx:132-158`). The prose presents two
   epistemic approaches rather than a measured degree, so a neutral comparison
   would avoid false precision. The labels and caption make the intended contrast
   recoverable, so this does not independently block approval.

2. Figure 139.3's caption, “noticing it available in real time,” is grammatically
   unclear (`src/chapters/waking-up.mdx:96`). Tighten it when revising so the
   caption directly names the shift from identification with a thought to
   awareness of it.

3. Apart from the required findings, the fixed anatomy is intact. Five key ideas
   each have a captioned shared-vocabulary figure; omission of the Model section
   matches both the brief and registry; the four exercises specify observable
   actions; and all three nearby slugs resolve to done chapters with their
   relationships stated in prose. The outbound publisher link matches the
   recorded evidence.

4. Within the bounded brief and recorded evidence, the remaining synthesis uses
   original thematic organization, prose, and shared SVG primitives. No
   quotation, real cover art, apparent close paraphrase, or apparent reproduction
   of a source figure was found. This review began no external web search.

5. `npm run check` completed with `CHECK OK` on 2026-07-28. Validation and prose
   lint passed; both pipeline tests, all 40 runner tests, and all 299 Vitest tests
   passed; TypeScript, the Vite production build, and ESLint passed. Vitest
   emitted only the existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-28

- Resolved mobile diagram legibility by giving Figure 139.1 its 420px Flow width,
  Figure 139.2 its 380px NodeGraph width, Figure 139.3 its full 558px Flow width,
  Figure 139.4 its 384px Compare width, and Figure 139.5 its 380px Spectrum width.
  The existing Figure overflow container now keeps each SVG at its authored scale on
  a 360px viewport.
- Replaced Figure 139.1's unrelated Iceberg with an in-vocabulary Flow: chest
  tightness, the added "I am failing" commentary, then noticing and responding. Its
  caption now names that distinction. Also tightened Figure 139.3's caption to name
  the shift from identification to awareness.
- Narrowed the caveat to the recorded evidence: it distinguishes narrative and
  present-centered self-focus, rejects unsupported philosophical conclusions, and
  states that the page offers no condition-specific or clinical guidance. Removed the
  unsupported claim about meditation risks for named populations.
- Preserved the five-key-idea anatomy, existing practice cards, links, and the
  deliberately absent Model section. `npm run check` passed on 2026-07-28.

## Critique round 2 — 2026-07-28

### Required

1. **Make the registry's diagram inventory agree with the resolved chapter.**
   The builder replaced Figure 139.1 with `Flow`, and the chapter now imports and
   renders `Flow`, `NodeGraph`, `Compare`, and `Spectrum`
   (`src/chapters/waking-up.mdx:1-3,41-47`). The registry still lists `iceberg` as
   the first diagram and lists only one `flow / sequence`
   (`content/registry.json:2753-2759`). The rendered page actually contains two
   Flow figures and no Iceberg figure. Update the registry inventory so it records
   the five rendered forms in order: `flow / sequence`, `node graph`,
   `flow / sequence`, `comparison / split`, and `spectrum / gradient`. This is a
   required technical-integrity defect because the authoring spec requires a
   complete registry entry and the rubric requires registry state to agree with
   the files on disk.

### Advisory

1. The three prior required findings remain resolved. The minimum widths now
   preserve each primitive's authored scale inside `Figure`'s horizontal overflow;
   Figure 139.1 teaches the event, commentary, and response sequence described by
   its section; and the caveat is bounded by the recorded evidence.

2. The thesis and fixed anatomy are intact. The deliberately absent Model section
   matches the brief, all five key ideas have captioned in-vocabulary diagrams, the
   four exercises are concrete, the three related slugs resolve to done chapters,
   and the outbound publisher link matches the evidence record. No unsupported
   claim that changes the reader's understanding, apparent close paraphrase,
   reproduced source figure, real cover art, or new external research was found.

3. `npm run check` completed with `CHECK OK` on 2026-07-28. Validation and prose
   lint passed; both pipeline tests, all 40 runner tests, all 299 Vitest tests,
   TypeScript, the Vite production build, and ESLint passed. Vitest emitted only
   the existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-28

- Updated `waking-up`'s registry diagram inventory to match the five rendered
  figures, in order: `flow / sequence`, `node graph`, `flow / sequence`,
  `comparison / split`, and `spectrum / gradient`. This removes the stale
  `iceberg` entry left from the earlier revision.
- Preserved the prior resolution: all five figures retain their chapter-local
  minimum widths, Figure 139.1 remains the event-commentary-response Flow, and
  the caveat remains limited to the recorded non-clinical evidence.

## Critique round 3 — 2026-07-28

### Required

1. **Correct the Hero reading-time badge from the final rendered word count.**
   The current Hero declares `minutes={7}` (`src/chapters/waking-up.mdx:5-9`),
   but a direct static render through the real MDX and shared components contains
   approximately 1,456 reader-visible words, including the Hero, headings,
   captions, SVG labels, exercise titles, callout, and generated nearby-book
   metadata. At approximately 200 words per minute, rounded up as the authoring
   spec requires, this is an eight-minute distillation. Set the badge to
   `minutes={8}`.

### Advisory

None. The four earlier required findings remain resolved: the figures preserve
their authored mobile widths, Figure 139.1 encodes its event-commentary-response
claim, the caveat stays within the recorded evidence, and the registry diagram
inventory matches the rendered chapter. The fixed anatomy, evidence boundaries,
related links, and deliberately absent Model section remain sound. This review
began no external web search.

`npm run check` completed with `CHECK OK` on 2026-07-28. Validation and prose
lint passed; both pipeline tests, all 40 runner tests, all 299 Vitest tests,
TypeScript, the Vite production build, and ESLint passed. Vitest emitted only
the existing non-failing jsdom `Window.scrollTo()` notices.
