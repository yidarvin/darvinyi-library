verdict: resolved

## Critique round 1 — 2026-07-28

### Required

1. **Complete the registry record before this chapter can be done.** The
   `superintelligence` entry ends after `status` and omits the required `tier`,
   `thesis`, `framework`, and `diagrams` fields
   (`content/registry.json:2604-2612`). Populate those fields from the brief and
   the finished chapter, naming the control problem as the signature framework
   and listing the forms actually rendered. The authoring spec requires this
   metadata even though the validator permits an incomplete draft entry.

2. **Compress The thesis to the fixed one-or-two-sentence anatomy.** The carry-away
   block is five sentences (`src/chapters/superintelligence.mdx:11-18`), including
   a separate setup, capability claim, negative formulation, positive formulation,
   and timing claim. Preserve the distinction between capability and objective,
   but express the whole argument in the one or two sentences required by
   `docs/authoring-spec.md`.

3. **Keep the treatment of technical paths and governance within the recorded
   evidence.** The heading claims that the path to advanced AI “matters less” than
   control, and the prose calls attention to system form a “common distraction”
   (`src/chapters/superintelligence.mdx:117-127`). The brief requires the control
   problem, but the recorded Oxford Martin evidence says the book examines several
   paths, and the chapter itself says those paths differ in speed, ownership, and
   technical details. Nothing in the evidence record supports the relative ranking
   that paths matter less, which understates a subject important enough to appear
   in the book's subtitle. State the supported synthesis that different paths can
   share control burdens without dismissing path-dependent differences. Also,
   lines 153-156 attribute incident reporting, dangerous-capability security, and
   pause agreements to the book, while the recorded racing evidence supports only
   the narrower claim that competition can reduce safety investment. Either narrow
   that attribution to what is recorded, clearly label the specific measures as
   the chapter's practical synthesis, or record evidence that supports them.

4. **Move Figure 132.3's branch to the decision point it can actually change.**
   `Flow` forks from its final step, so the current figure completes “risk of
   conflict” and only then branches to “limits and review” or “unchecked pursuit”
   (`src/chapters/superintelligence.mdx:107-114`;
   `src/components/diagrams/Flow.tsx:19-34,82-107`). The prose says limits, access
   controls, and intervention determine whether useful intermediate moves become
   conflict. The figure instead makes both control and unchecked pursuit outcomes
   of conflict after it has already occurred. Recompose the sequence so the branch
   precedes the risk outcome, or make the two branch outcomes accurately express
   bounded pursuit versus conflict.

5. **Correct every quadrant in Figure 132.4.** `Matrix` consumes quadrants in
   `[top-left, top-right, bottom-left, bottom-right]` order, with broad reach at the
   top and narrow reach at the bottom
   (`src/components/diagrams/Matrix.tsx:13-17,46-56`). The supplied labels do not
   match those coordinates (`src/chapters/superintelligence.mdx:129-142`):
   “ordinary oversight / local and limited” is placed at distributed plus broad
   reach; “shared safeguards / many actors, wide effects” is placed at concentrated
   plus broad reach; “local controls / one owner” is placed at distributed plus
   narrow reach; and the highlighted “control problem / concentrated power, wide
   effects” is placed at concentrated plus narrow reach. Reorder and, where needed,
   rename the quadrants so every label follows the axes and the highlighted cell is
   actually concentrated power with broad reach.

6. **Make the signature control model encode the feedback its prose and caption
   promise.** The prose says operational evidence should revise the specification
   and deployment limits, and the caption says feedback must revise both
   (`src/chapters/superintelligence.mdx:183-189`). The graph has no edge from
   effects or evaluation to either node. It instead draws a balancing edge from
   world effects to human purpose, which the imported `NodeGraph` renders as a
   dashed connection with an explicit minus sign
   (`src/chapters/superintelligence.mdx:193-209`;
   `src/components/diagrams/NodeGraph.tsx:12-17,94-120`). That teaches that effects
   suppress purpose, not that evidence updates the specification and limits.
   Recompose the graph with defensible feedback targets and use reinforcing or
   balancing signs only where their polarity has a clear meaning.

7. **Recompute the Hero reading-time badge from rendered words.** `minutes={7}`
   cannot satisfy the roughly 200-wpm, rounded-up rule
   (`src/chapters/superintelligence.mdx:5-9`). The visible prose and headings alone
   are about 1,275 words after Markdown markers are excluded. Adding the Hero
   thesis, six captions, and four exercise titles already pushes the rendered
   total above 1,400 words before any diagram labels or footer text are counted.
   The badge therefore rounds to at least eight minutes.

### Advisory

1. `ShelvedNearby` resolves four done chapters, but it renders only cover tiles and
   supplies none of the one-clause relationship notes required by the cross-linking
   guidance (`src/chapters/superintelligence.mdx:271-275`;
   `src/components/book/ShelvedNearby.tsx:22-54`). Adding the conceptual relation
   for each link would make this footer an actual graph rather than an unlabeled
   shelf. This is advisory because the links themselves resolve and the critique
   rubric treats optional cross-link improvements as non-blocking.

2. Within the bounded record, the chapter's orthogonality, instrumental-convergence,
   broad-capability, and competitive-pressure claims agree with the brief and
   evidence summaries. The organization, wording, and diagrams appear to be
   original synthesis, with no quotation or real cover art. Because the evidence
   file records source summaries rather than source text, this review could not
   perform sentence-level close-paraphrase comparison and began no new external
   web search.

3. The remaining page wiring is sound: five key ideas each have a captioned
   vocabulary diagram, the practice cards are concrete, the caveat correctly
   presents the argument as conditional rather than a timetable, the related
   slugs are done, and the publisher purchase link is present. `npm run check`
   completed with `CHECK OK` on 2026-07-28: validation, prose lint, 42
   pipeline/runner tests, 283 Vitest tests, TypeScript, the Vite production build,
   and ESLint all passed. Vitest emitted only the existing non-failing jsdom
   `Window.scrollTo()` notices.

## Builder resolution — 2026-07-28

- Completed the `superintelligence` registry record with tier 3, the brief-supported thesis, the control problem as its signature framework, and the seven rendered diagram forms in page order. Its status remains `draft`.
- Compressed “The thesis” to two sentences while retaining the distinction between broad capability and a safe objective under meaningful human direction.
- Rewrote the technical-path section to retain path-dependent differences while identifying the shared control burden. Narrowed the race claim to the recorded evidence that competition can reduce safety investment, and explicitly labeled the listed institutional measures as this chapter’s practical synthesis.
- Rebuilt Figure 132.3 so its access-and-review decision branches to bounded pursuit or risk of conflict, before the conflict outcome. Reordered Figure 132.4 into Matrix’s documented coordinate order and highlighted concentrated decision power with broad reach.
- Rewired Figure 132.6 with labeled feedback from world effects to evaluation and deployment limits, an evaluation-to-objective revision edge, and a deployment-limit-to-system access boundary. The graph now uses neutral labeled arrows rather than unsupported polarity signs.
- Recomputed the Hero badge to `8-min distillation` from the rendered chapter length.

## Critique round 2 — 2026-07-28

### Required

1. **Give Figure 132.6 enough space to render its two core forward arrows.** The
   revised graph places `human purpose` and `specified objective` at normalized
   x-coordinates 0.12 and 0.45, and places `capable system` and `world effects` at
   0.45 and 0.78 (`src/chapters/superintelligence.mdx:193-203`). In `NodeGraph`,
   those positions resolve to centers only 94.38 SVG units apart. Each card is 94
   units wide, and the component adds seven units of clearance at both ends of an
   edge (`src/components/diagrams/NodeGraph.tsx:42-46,54-58,87-93`). Both horizontal
   links therefore have a drawable length of 94.38 - 94 - 14 = -13.62 units:
   their computed start lies beyond their computed end, inside the cards that are
   painted over the edges. The signature model consequently does not visibly
   communicate either purpose → specification or system → effects, two links
   essential to the chain described by the prose and accessibility label. Recompose
   the chapter-local node positions so each linked pair has real clearance and the
   arrowheads remain visible; do not change the shared component for this page-only
   defect.

### Advisory

1. The `Compare` under the control graph omits `favor`, so the shared component's
   default accents capability control over motivation control
   (`src/chapters/superintelligence.mdx:211-222`;
   `src/components/diagrams/Compare.tsx:22-24,36-42`). `favor="none"` would better
   match the prose's claim that neither requirement substitutes for the other.

2. The round-one prose, evidence, registry, branching-flow, matrix-order, and
   reading-time findings are resolved. Within the recorded evidence, the chapter's
   broad-capability, orthogonality, instrumental-convergence, technical-path, and
   competitive-pressure claims remain supportable and appropriately conditional.
   The page uses original synthesis and diagrams, with no quotation or real cover
   art. No new external web search was performed.

3. `npm run check` completed with `CHECK OK` on 2026-07-28: validation, prose lint,
   42 pipeline/runner tests, 283 Vitest tests, TypeScript, the Vite production
   build, and ESLint all passed. Vitest emitted only non-failing jsdom
   `Window.scrollTo()` notices.

## Builder resolution — 2026-07-28

- Repositioned Figure 132.6’s chapter-local nodes so `human purpose` → `specified objective` and `capable system` → `world effects` each span 134.42 SVG units between centers, leaving 26.42 units of visible edge after the cards and the component’s seven-unit clearances. The evaluation and deployment-limit nodes were moved with the new layout so the feedback links remain distinct and inside the canvas.
- Set the model’s comparison to `favor="none"`, matching the text’s point that motivation and capability control are complementary rather than competing priorities.
- Ran `npm run check` successfully on 2026-07-28 (`exit 0`). The chapter remains `draft`; no done status, commit, or push was performed.

## Critique round 3 — 2026-07-28

### Required

1. **Keep Figure 132.6's `revises limits` label inside the SVG canvas.** The
   `effects` and `limits` nodes share x-coordinate `0.97`, which resolves to
   `324.42` in `NodeGraph`'s 380-unit viewBox
   (`src/chapters/superintelligence.mdx:196-198`;
   `src/components/diagrams/NodeGraph.tsx:43-45,60-64`). The vertical edge label
   would be centered there, but its chapter-local `labelOffset.x` moves the
   14-character `revises limits` text to x `342.42`
   (`src/chapters/superintelligence.mdx:206`;
   `src/components/diagrams/NodeGraph.tsx:96-97,110-120`). At the component's
   12-unit JetBrains Mono size, the text extends beyond x `380` and is clipped by
   the root SVG. Scaling the figure does not recover content outside the viewBox,
   so the signature control diagram loses part of a feedback label at desktop and
   phone widths. Reposition the label or the chapter-local nodes so the full text
   remains inside the canvas without colliding with a card or another edge.

### Advisory

1. The round-two forward-arrow spacing defect is resolved: both horizontal links
   now have 26.42 SVG units of drawable shaft after card intersection and the
   component's clearances. The comparison also correctly uses `favor="none"`.
   The earlier prose, evidence, registry, flow, matrix, and reading-time fixes
   remain intact. No settled finding was reopened, and no new external web search
   was performed.

2. `npm run check` completed with `CHECK OK` on 2026-07-28: validation, prose lint,
   42 pipeline/runner tests, 283 Vitest tests, TypeScript, the Vite production
   build, and ESLint all passed. Vitest emitted only the known non-failing jsdom
   `Window.scrollTo()` notices.

## Builder resolution — 2026-07-28

- Rebalanced Figure 132.6's chapter-local layout: `capable system` now sits left of the specification and `world effects` plus `deployment limits` occupy a shared, inset right column. This preserves both 134.42-unit horizontal forward links while giving the feedback label a separate lane.
- Moved the `revises limits` label to x=308.36 in the 380-unit viewBox. Its roughly 101-unit text span now remains within x=258 to x=359, clear of the right-side cards and the diagonal deployment-limit edge.
- The chapter remains `draft`; no done status, commit, or push was performed.

## Critique round 4 — 2026-07-28

### Required

1. **Separate Figure 132.5's marker label from its right endpoint label.** The
   chapter uses the `Spectrum` defaults for both label layouts while supplying
   `right="coordinate for safety"` and `markerLabel="shared standards"` at
   `marker={0.7}` (`src/chapters/superintelligence.mdx:157-168`). The component
   renders the 21-character endpoint at x=340, y=74 in 12-unit monospace type and
   the 16-character marker label at x=250, y=78 in 10-unit monospace type
   (`src/components/diagrams/Spectrum.tsx:49-53,129-158`). Their horizontal spans
   overlap almost completely and their baselines are only four SVG units apart,
   so the labels paint over each other at every display size. Use the component's
   chapter-local `markerLabelPlacement` and/or `endpointLabelLayout` options, or
   otherwise recompose this figure so all three structural labels are readable.

2. **Give Figure 132.6's `evidence` and `bounds access` edge labels distinct
   lanes.** With the current node positions and offsets, `NodeGraph` centers
   `evidence` at approximately (170.84, 217.92) and `bounds access` at
   approximately (209.15, 222.16)
   (`src/chapters/superintelligence.mdx:192-207`;
   `src/components/diagrams/NodeGraph.tsx:43-58,75-120`). Both labels render in
   12-unit JetBrains Mono. Their text spans overlap by roughly 34 SVG units while
   their baselines differ by only 4.24 units, making both connection meanings
   unreadable where the two diagonal feedback edges cross. Reposition the
   chapter-local nodes or label offsets so each feedback label is visibly tied to
   one edge without colliding with another label, edge, or card.

### Advisory

1. The round-three clipping defect is resolved: `revises limits` now remains
   inside the 380-unit viewBox, and the round-two forward arrows retain visible
   clearance. The two findings above concern distinct collisions in the current
   rendered geometry, so they do not reopen either settled issue.

2. The earlier thesis, evidence, registry, flow, matrix, comparison, and
   reading-time fixes remain intact. Within the recorded evidence, the factual
   synthesis remains supportable and appropriately conditional. The page uses
   original prose and original vocabulary diagrams, with no quotation or real
   cover art. No new external web search was performed.

3. `npm run check` completed with `CHECK OK` on 2026-07-28: validation, prose
   lint, 42 pipeline/runner tests, 283 Vitest tests, TypeScript, the Vite
   production build, and ESLint all passed. Vitest emitted only the repository's
   known non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-28

- Reconfigured Figure 132.5's chapter-local `Spectrum` labels: `shared standards` now occupies the top marker lane, while the two long endpoint labels use the stacked layout above their respective ends. The marker and the right endpoint no longer share the same horizontal band.
- Moved Figure 132.6's `evidence` label to its lower-left feedback lane at approximately `(127.84, 217.92)` in the 380-unit viewBox, adjacent to the effects-to-evaluation arrow and clear of the crossing. Moved `bounds access` to a separate lower-middle lane at approximately `(187.15, 233.16)`, leaving clear vertical separation from `evidence` and clearance from the evaluation and deployment-limit cards.
- Preserved the prior forward-arrow spacing, `revises limits` in-canvas placement, neutral comparison, evidence-bound prose, registry metadata, and all earlier corrections.
- Ran `npm run check` successfully on 2026-07-28 (`exit 0`): validation, prose lint, pipeline tests, Vitest, TypeScript, production build, and ESLint passed. The chapter remains `draft`; no done status, commit, or push was performed.

## Critique round 5 — 2026-07-28

### Required

1. **Route Figure 132.6's objective-revision feedback around the `capable
   system` card.** The current `evaluation` → `specified objective` connection
   runs from approximately `(97.08, 223.05)` to `(174.24, 95.83)` after
   `NodeGraph` applies its card and arrow clearances
   (`src/chapters/superintelligence.mdx:195-207`;
   `src/components/diagrams/NodeGraph.tsx:43-58,75-109`). The `capable system`
   card spans x `82.94-176.94` and y `154.8-194.8`. At those two y boundaries,
   the feedback line is at x `138.47` and `114.22`, respectively, so the entire
   middle of the connection passes behind that card. Because edges render before
   nodes (`NodeGraph.tsx:75-135`), the card paints over roughly 47 SVG units of
   the line and leaves two apparently disconnected segments. This is the
   signature model's only path by which evaluation revises the objective, so the
   occlusion breaks the feedback loop promised by the prose, caption, and
   accessibility label. Reposition the chapter-local nodes so that complete
   connection remains visible without undoing the settled edge-clearance and
   label fixes.

### Advisory

1. The round-four `Spectrum` collision is resolved: the marker label now sits at
   y `24`, while the stacked right endpoint occupies baselines `40.5` and `55.5`.
   The `evidence` and `bounds access` labels also occupy distinct lanes. The
   earlier thesis, sourcing, registry, flow, matrix, reading-time, comparison,
   clipping, and forward-arrow fixes remain intact. No settled finding was
   reopened, and no new external web search was performed.

2. Within the recorded evidence, the chapter's broad-capability,
   orthogonality, instrumental-convergence, multiple-path, control, and
   competitive-pressure claims remain supportable and appropriately
   conditional. The prose and vocabulary diagrams are original synthesis, with
   no quotation or real cover art.

3. `npm run check` completed with `CHECK OK` on 2026-07-28: validation, prose
   lint, 42 pipeline/runner tests, 283 Vitest tests, TypeScript, the Vite
   production build, and ESLint all passed. Vitest emitted only the repository's
   known non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-28

- Repositioned Figure 132.6’s purpose and objective nodes into the upper lane and moved evaluation to the upper-left feedback lane. The `evaluation` → `specified objective` arrow now runs entirely above the `capable system` card, leaving a complete visible shaft and arrowhead without changing the shared primitive.
- Moved the `revises` label into the open space between the evaluation and objective cards. The settled forward-arrow spacing, in-canvas `revises limits` label, and distinct `evidence` and `bounds access` lanes remain intact.
- Ran `npm run check` successfully on 2026-07-28 (`exit 0`). The chapter remains `draft`; no done status, commit, or push was performed.

## Critique round 6 — 2026-07-28

### Required

1. **Move Figure 132.6's `revises` and `bounds access` labels clear of their
   own connector strokes.** The round-five node move makes the full
   `evaluation` → `specified objective` arrow visible, but its label is now
   anchored at approximately `(135.66, 85.96)` while the connector runs from
   approximately `(119.95, 84.58)` to `(151.37, 65.34)`
   (`src/chapters/superintelligence.mdx:195-209`;
   `src/components/diagrams/NodeGraph.tsx:75-120`). In 12-unit JetBrains Mono,
   the diagonal crosses the visible glyph area of `revises`. The
   `deployment limits` → `capable system` connector similarly crosses the
   visible glyph area of `bounds access`: the label is anchored at
   approximately `(187.15, 233.16)`, while its connector passes through that
   text band at x-coordinates around `200-213`. Because the connector and text
   use the same muted color, both labels merge with their lines instead of
   reading as distinct feedback meanings. Adjust the chapter-local label
   offsets or node positions so each essential label is clear of its own
   connector without undoing the settled arrow, clipping, card-clearance, and
   label-lane fixes.

### Advisory

1. The round-five occlusion defect is resolved: the complete
   `evaluation` → `specified objective` connector now stays above the
   `capable system` card. The earlier thesis, sourcing, registry, flow,
   matrix, reading-time, spectrum, comparison, clipping, and label-lane fixes
   remain intact. This round identifies connector-to-label collisions, not a
   reopening of the settled card occlusion or label-to-label findings. No new
   external web search was performed.

2. Within the recorded evidence, the factual synthesis remains supportable
   and appropriately conditional. The page retains the required anatomy, five
   key ideas with vocabulary diagrams, concrete practice cards, an honest
   caveat, original prose and diagrams, resolved related links, and a
   publisher purchase link.

3. `npm run check` completed with `CHECK OK` on 2026-07-28: validation, prose
   lint, 42 pipeline/runner tests, 283 Vitest tests, TypeScript, the Vite
   production build, and ESLint all passed. Vitest emitted only the
   repository's known non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-28

- Moved Figure 132.6's `revises` label into the open top lane between the purpose and objective cards, at approximately `(120.66, 15.96)` in the 380-unit viewBox. It is now clear of the evaluation-to-objective arrow, both adjacent cards, and the canvas boundary.
- Moved `bounds access` into the lower-left feedback lane at approximately `(159.65, 258.15)`. Its text ends before the deployment-limits card begins and sits below and left of the limits-to-system connector, so neither the line nor another label crosses its glyphs.
- Preserved the settled forward-arrow clearance, visible evaluation feedback, in-canvas `revises limits` label, and separate `evidence` lane. Ran `npm run check` successfully on 2026-07-28 (`exit 0`). The chapter remains `draft`; no done status, commit, or push was performed.
