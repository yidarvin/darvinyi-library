verdict: approve

## Critique round 1 — 2026-07-15

### Required

1. **Complete the `innovators-dilemma` registry metadata required by the content
   contract.** The registry entry has display metadata and `draft` status, but it
   omits `tier`, `thesis`, `framework`, and the rendered diagram list required by
   definition-of-done item 7 (`content/registry.json:497-505`). Add the brief-aligned
   metadata and record the six forms actually rendered without changing unrelated
   entries or shared tooling.

2. **Recompute the Hero reading-time badge from all reader-visible text.** The draft
   declares `minutes={7}` (`src/chapters/innovators-dilemma.mdx:5-9`), but the page
   contains approximately 1,494 visible words when its prose and headings, Hero,
   captions, diagram labels, exercise titles, component chrome, and Shelved Nearby
   text are counted. At the authoring spec's roughly 200 words per minute, rounded
   up, that is an 8-minute distillation. Set the badge from the final rendered count
   after the other revisions.

3. **Make Figure 25.2 encode performance outrunning practical demand.** The prose and
   caption claim that product performance can rise beyond what a customer group can
   use, but the figure draws only one exponential product-performance curve and puts
   `good enough for one job` and `premium demand` on that same line
   (`src/chapters/innovators-dilemma.mdx:49-67`). With no demand threshold,
   customer-need trajectory, or second structure to compare against performance,
   the visual cannot show the gap that makes a simpler offer viable. Recompose the
   chapter-local figure from the existing vocabulary so supply performance and a
   group's usable need are visibly distinct, without reproducing the book's figure
   or changing the shared diagram components.

4. **Support or narrow the caveat's claim about later assessments.** The sentence
   saying that later assessments of the book's cases found mixed fit for the
   theory's proposed mechanisms is a substantive empirical claim that changes how
   much confidence the reader should place in the framework
   (`src/chapters/innovators-dilemma.mdx:190-199`). Neither the chapter brief, seed
   metadata, registry, nor any chapter-specific evidence record supports it. Record
   and identify the evidence behind that assessment, or rewrite the caveat to make
   only the internally supported limits already stated around it.

### Advisory

1. Figure 25.3 explains both low-end and new-market footholds, but accents only the
   new-market quadrant even though the prose gives the two paths equal weight
   (`src/chapters/innovators-dilemma.mdx:70-96`). Consider removing the single
   highlight or recomposing the visual so both overlooked footholds read as the
   relevant contrast to premium competition.

2. Within the repository's bounded evidence, the draft otherwise preserves the
   brief's incumbent-incentive thesis in original thematic prose. It has five key
   ideas with captioned shared-vocabulary figures, a distinct Model figure, four
   concrete exercises, a generated typographic cover, no quotation or real cover
   art, and relationship clauses for all three nearby books. The related slugs are
   built, and the outbound URL is a direct HBR Store page. No separate chapter
   evidence dossier exists, and this review began no external web search.

3. `npm run check` passed on 2026-07-15: queue, registry, critique, and content
   validation; prose lint; both pipeline tests; all 54 Vitest tests; TypeScript and
   Vite production build; and ESLint. Vitest emitted only the existing non-failing
   jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-15

- Completed the `innovators-dilemma` registry entry with its brief-aligned tier,
  thesis, framework, and the six rendered vocabulary forms: iceberg, annotated curve,
  two-by-two matrix, spectrum, comparison, and flow. Its status remains `draft`.
- Recomputed the Hero badge after the revisions and set it to an 8-minute
  distillation.
- Rebuilt Figure 25.2 as two distinct annotated curves: supplier performance rises
  across generations while a single job's practical need levels off. The figure now
  makes the surplus that creates room for a simpler offer visible without changing a
  shared diagram component.
- Removed the unsupported claim about later assessments finding mixed case fit. The
  caveat now stays within the recorded, internally supported limits: disruption is
  not a generic label, neither incumbent failure nor entrant success is inevitable,
  and real industries do not follow one clean path.

## Critique round 2 — 2026-07-15

### Required

1. **Finish Figure 25.2 so it visibly shows performance exceeding practical need.**
   The revision now gives supplier performance and practical need separate curves,
   but the side-by-side panels never compare them on one shared structure
   (`src/chapters/innovators-dilemma.mdx:47-76`). If their normalized axes are read
   as comparable, the exponential supplier curve remains below the logarithmic need
   curve at every interior point and they meet only at the endpoint. The `more than
   this job needs` marker is also plotted at `(0.78, 0.76)`, well above the supplier
   curve's value of about `0.49` there, so the label asserts the surplus rather than
   the line encoding it. Recompose this chapter-local figure from the existing
   vocabulary so a reader can see performance move from below to above a stated
   need threshold, or can otherwise see the before-and-after surplus directly,
   without changing a shared component or reproducing the book's figure.

### Advisory

1. The other round 1 required findings are resolved. The registry metadata matches
   the brief and rendered forms, the 8-minute badge remains consistent with the
   prior rendered-text count, and the caveat no longer makes the unsupported claim
   about later assessments. The review remained within the chapter brief, seed
   metadata, registry, prior critique record, and current implementation; no
   chapter-specific evidence dossier exists, and no external web search was begun.

2. The round 1 note about Figure 25.3 accenting only the new-market foothold remains
   advisory. It does not block this verdict.

3. `npm run check` passed on 2026-07-15: validation and prose lint; both pipeline
   tests; all 54 Vitest tests; TypeScript and Vite production build; and ESLint.
   Vitest emitted only the existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-15

- Rebuilt Figure 25.2 as one product-performance curve paired with two equal-scale
  spectra. The practical-need boundary remains at the same point in both spectra;
  the early-product marker is below it, while the later-product marker sits beyond it
  in an explicitly labeled surplus zone. This makes the before-and-after relationship
  visible without altering a shared diagram component or reproducing the book's figure.
- Updated the chapter's registry diagram inventory to identify the composed annotated
  curve and before-and-after spectrum form. The existing metadata, 8-minute badge,
  caveat, and `draft` status are preserved.

## Critique round 3 — 2026-07-15

### Required

None.

### Advisory

1. The round 2 required finding is resolved. Figure 25.2 now pairs the supplier-
   performance curve with two equal-scale spectra that keep the practical-need
   boundary fixed. The early marker is visibly below that boundary, and the later
   marker is visibly beyond it in the labeled surplus zone, so the composition now
   encodes the before-and-after relationship claimed by the prose and caption.

2. The earlier metadata, reading-time, and sourcing findings remain resolved. The
   registry records the brief-aligned thesis, framework, tier, and six rendered
   forms; the Hero remains an 8-minute distillation; and the caveat stays within the
   internally supported limits of the theory. Within the repository's bounded
   evidence, the draft remains an original thematic distillation of the recorded
   incumbent-incentive thesis. No separate chapter evidence dossier exists, and this
   round began no external web search.

3. The round 1 advisory about Figure 25.3 still applies: the prose treats low-end and
   new-market footholds as parallel paths, while the matrix accents only the new-
   market quadrant. The labels still encode both paths accurately, so this visual
   emphasis does not block approval.

4. `npm run check` passed on 2026-07-15: queue, registry, critique, and content
   validation; prose lint; both pipeline tests; all 54 Vitest tests; TypeScript and
   Vite production build; and ESLint. Vitest emitted only the existing non-failing
   jsdom `Window.scrollTo()` notices.
