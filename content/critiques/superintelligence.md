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
