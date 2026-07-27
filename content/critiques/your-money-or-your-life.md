verdict: approve

## Critique round 1 — 2026-07-27

### Required

1. **The fulfillment matrix contradicts its own axes.** The vertical axis defines the
   top row as strong values fit, but the top-left quadrant is labeled `review` with
   the note `values say no`. That note describes weak fit and therefore cannot occupy
   the top row. This makes one of the four cases logically impossible and breaks the
   visual explanation of the section. Relabel or rearrange the quadrants so every
   cell agrees with both axes and with the prose, while retaining high fulfillment
   plus strong fit as the protected target.

2. **The crossover figure does not show the idea claimed by the section or caption.**
   The prose and recorded evidence describe two quantities, recurring expenses and
   income from accumulated capital, and define the crossover as the point where the
   latter covers the former. Figure 109.5 renders only one exponential asset-income
   curve. It contains no expense line, expense level, intersection, or crossover
   label, yet its caption says expenses fall while independent income grows. Replace
   it with an in-vocabulary visual that makes both sides and their crossover visible.
   This is a major book idea, so an asset-growth curve by itself is not an adequate
   structural diagram.

3. **The “enough” spectrum visually favors the position the prose warns against.**
   `Spectrum` defaults to emphasizing its right endpoint, so Figure 109.4 draws the
   track toward accent and gives the `more by default` pole an accent endpoint while
   also trying to mark the middle as enough. In this vocabulary, accent communicates
   the intended target. Remove the right-end emphasis or otherwise make the chosen
   enough region the sole visual target.

### Advisory

1. Figure 109.1 uses arbitrary bar lengths that look like measured reductions even
   though the text correctly says each reader must calculate a personal rate. A
   clearly labeled hypothetical example or a non-quantitative staged form would make
   the conceptual status harder to misread.

2. “Shelved Nearby” supplies three relevant, resolving links, but it does not state
   the one-clause relationship for any of them as requested by the authoring spec.
   Add concise relationship language if the component contract permits it.

3. `Compare` is imported from the diagram barrel but never used. Remove the dead
   import during the revision.

`npm run check` passed on 2026-07-27. The recorded evidence supports the chapter's
main claims about life energy, adjusted hourly wage, tracking and monthly review,
values-aligned spending, and the capital-expenses crossover. No new external search
was performed.

## Builder resolution — 2026-07-27

Resolved every required finding using the recorded evidence, with no new external search.

- Reordered the fulfillment matrix labels so its top row is consistently strong values fit:
  the low-fulfillment cell is now `question`, the high-fulfillment cell remains the accented
  `protect` target, and the weak-fit cells are `automatic` and `review`.
- Extended the existing in-vocabulary annotated curve with a reusable `crossover` variant.
  Figure 109.5 now renders a falling recurring-expenses line, a rising independent-income
  line, their labeled intersection, and a caption that defines the threshold. The diagram
  vocabulary and a focused regression test now cover this variant.
- Set Figure 109.4's spectrum to neutral endpoints, leaving the accented enough zone and
  its marker as the only visual target.

Also preserved the chapter's earlier work while applying the advisory cleanup that fit the
current component contracts: Figure 109.1 is explicitly a hypothetical example, the unused
`Compare` import is removed, and the Shelved Nearby lead names the relationship to each of
its three linked books. The shared footer component does not accept per-link relationship
copy, so this chapter-level lead supplies it without changing unrelated shared UI.

## Critique round 2 — 2026-07-27

### Required

1. **The registry record is incomplete.** The `your-money-or-your-life` entry has only
   its basic routing fields and `status: "draft"`. It is missing `tier`, `thesis`,
   `framework`, and `diagrams`, all of which the definition of done requires and the
   adjacent completed records contain. `mark.py` changes only status, so approving
   now would leave the final registry incomplete even though the current validator
   does not enforce those fields.

2. **All six figures shrink below legible phone size.** Every diagram is passed
   `className="block w-full"` with no minimum width. At a 360px viewport, the layout
   and Figure padding leave roughly 278px for the SVG. The two four-step Flow figures
   therefore scale their 558-unit viewBoxes by about one half, reducing their
   9–11.5-unit labels to roughly 4.5–5.8 CSS pixels. The 380–384-unit Bars, Matrix,
   Spectrum, and Curve figures likewise reduce most labels to roughly 7–9 pixels.
   `Figure` has an overflow container, but it cannot scroll when its child has no
   minimum width. Give each chapter diagram a suitable minimum width, as other
   chapters do for these primitives, so labels remain readable at 360px.

### Advisory

1. The Thesis section takes five sentences, while the authoring spec asks it to
   compress the argument into one or two. Its argument is clear, so this does not
   independently block approval, but it could be tightened when addressing the
   required findings.

`npm run check` passed before this critique round on 2026-07-27. The recorded
first-party evidence supports the chapter's adjusted-hourly-wage, monthly tracking,
fulfillment, enough, and capital-expenses crossover claims. The resolved matrix,
spectrum, and crossover findings remain fixed. No new external search was performed.

## Builder resolution — 2026-07-27

Resolved every required finding from critique round 2 using the recorded evidence and
without a new external search.

- Completed the draft registry record with tier 3, the recorded life-energy thesis,
  the `Money as life energy` framework, and the six-form inventory rendered by Figures
  109.1 through 109.6. Its status remains `draft`.
- Added chapter-local minimum widths to every figure: `min-w-[440px]` for the Bars,
  Matrix, Spectrum, and crossover Curve figures, and `min-w-[558px]` for both
  four-step Flow figures. Figure's existing horizontal overflow container now scrolls
  these diagrams at a 360px viewport instead of shrinking their labels below readable
  size.
- Tightened the Thesis section from five sentences to two, while retaining the book's
  life-energy argument and its distinction from austerity or income maximization.

Preserved the prior fixes: the fulfillment matrix agrees with both axes, the spectrum
marks only the enough region as the target, and the crossover curve still renders both
series and their named intersection. `npm run check` passed on 2026-07-27.

## Critique round 3 — 2026-07-27

### Required

None.

### Advisory

None.

The current draft retains every resolved fix from rounds 1 and 2. Its registry record is
complete, all six figures use the named diagram vocabulary and remain readable through
chapter-local minimum widths, and the fulfillment matrix, enough spectrum, and crossover
figure agree with their prose and captions. The recorded first-party evidence supports the
material claims about life energy, adjusted hourly wage, tracking and monthly review,
fulfillment, enough, and the capital-expenses crossover. The anatomy, practices, caveat,
related links, outbound publisher link, and generated cover meet the authoring contract.
`npm run check` passed on 2026-07-27. No new external search was performed.
