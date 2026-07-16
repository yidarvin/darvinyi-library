verdict: approve

## Critique round 1 — 2026-07-15

### Required

1. **Make the hero Model diagram encode the sequence the prose claims.** The text
   says the three signature ideas form a sequence and explicitly says that "the
   arrows matter," but Figure 21.7 renders Level 5 leadership, a focused arena, and
   disciplined action as an unarrowed pyramid beside a disconnected flywheel loop
   (`src/chapters/good-to-great.mdx:154-180`). The figure therefore shows neither a
   transition from Level 5 leadership to the Hedgehog focus nor a connection from
   that focus to the flywheel. Recompose the chapter-local figure with the shared
   vocabulary so Level 5 leadership, the Hedgehog Concept, and the flywheel are all
   recognizable and their stated relationship is visible rather than supplied only
   by the caption.

2. **Do not put strategy-defining work before the people in the "first who"
   diagram.** The prose correctly says to build the team before committing to a
   direction, while Figure 21.2 begins with `define the work` and only then reaches
   `choose for judgment and fit` (`src/chapters/good-to-great.mdx:54-69`). Read as a
   sequence, the diagram reverses the key ordering it is supposed to teach and makes
   the caption's claim ambiguous. Relabel or reorder the flow so the people precede
   the strategic direction, while preserving any role-fit distinction the prose
   needs.

3. **Keep Figure 21.2's four-stage Flow legible at its authored mobile width.** The
   shared `Flow` computes a 558-unit viewBox for four steps and draws its labels at
   11.5 units (`src/components/diagrams/Flow.tsx:19-29,57-72`). At the chapter's
   `min-w-[520px]`, those labels render at about 10.7 CSS px, including a three-line
   `choose for judgment and fit` node (`src/chapters/good-to-great.mdx:64-69`). Give
   the chapter-local figure a minimum width near its native 558 units, or recompose
   it so the complete labels remain readable in the horizontally scrolling phone
   figure.

4. **Bring the Hero and thesis block into the fixed anatomy.** The required Thesis
   section is one or two sentences, but this one contains three
   (`src/chapters/good-to-great.mdx:11-18`). The reading badge is also not computed
   from the final rendered word count: even the raw MDX, which includes non-rendered
   imports and JSX syntax, contains only 1,740 words, so the visible page cannot
   reach the more-than-1,800 words needed to round up to 10 minutes at roughly 200
   words per minute (`src/chapters/good-to-great.mdx:5-9`). Compress the thesis to
   the specified one or two sentences and set the badge from the resulting rendered
   text.

### Advisory

1. Within the repository's bounded evidence, the draft otherwise carries through
   the brief's humble-and-willful leadership, disciplined focus, and compounding
   momentum thesis in original thematic prose. It has six key ideas with captioned
   shared-vocabulary figures, four concrete exercises, a useful causal-inference
   caveat, a generated typographic cover, and no quotation or real cover art. The
   repository contains no chapter-specific evidence dossier beyond the brief, seed
   metadata, registry record, and this draft, and this review began no external web
   search.

2. The three nearby slugs all resolve to done chapters, and the outbound URL is a
   direct publisher link. The preceding sentence supplies relationship clauses for
   `seven-habits` and `start-with-why`, but not for `how-to-win-friends`
   (`src/chapters/good-to-great.mdx:232-239`). Adding the missing relationship or
   dropping that third cover would complete the cross-linking guidance.

3. `npm run check` passed on 2026-07-15: queue, registry, critique, and content
validation; prose lint; both pipeline tests; all 46 Vitest tests; TypeScript and
Vite production build; and ESLint. Vitest emitted only the existing non-failing
jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-15

- Rebuilt Figure 21.7 as an explicit `Level 5 leadership → Hedgehog Concept → flywheel
  momentum` flow. The Hedgehog Concept remains visible as a three-circle Venn and the
  flywheel as a reinforcing process loop beneath that arrowed sequence.
- Reordered Figure 21.2 to select for judgment and fit, place people in the right roles,
  test reality together, then commit to direction. Its minimum width is now the shared
  Flow component's 558-unit authored width.
- Reduced the Thesis to two sentences and changed the Hero badge to an 8-minute
  distillation: the final rendered text has 1,571 words, rounded at approximately 200 words
  per minute.

## Critique round 2 — 2026-07-15

### Required

1. **Synchronize the registry's diagram record with the revised Model figure.**
   Figure 21.7 now composes an explicit Flow, a Venn, and a ProcessLoop
   (`src/chapters/good-to-great.mdx:160-186`), but the registry still describes its
   seventh figure as `pyramid with process loop`
   (`content/registry.json:427-435`). The pyramid was removed in response to round
   1, so the metadata no longer agrees with the chapter. Replace that stale diagram
   entry with a description of the forms actually rendered; the authoring spec's
   definition of done requires a complete diagram list, and the critique rubric
   requires registry and files to agree.

### Advisory

1. The four round-1 required findings are resolved: the Model has an arrowed
   sequence and recognizable Venn and flywheel forms, the people-first flow has the
   correct order and a 558-unit minimum width, and the two-sentence thesis carries
   an 8-minute badge consistent with the recorded 1,571 rendered words.

2. The earlier cross-link advisory remains: `how-to-win-friends` is rendered as a
   nearby cover without a relationship clause in the preceding prose
   (`src/chapters/good-to-great.mdx:237-243`). This remains non-blocking.

3. `npm run check` passed on 2026-07-15: validation and prose lint; both pipeline
tests; all 46 Vitest tests; TypeScript and Vite production build; and ESLint.
Vitest emitted only the existing non-failing jsdom `Window.scrollTo()` notices.
No new external web search was used; the factual review stayed within the brief,
seed metadata, registry, prior critique evidence, and draft.

## Builder resolution — 2026-07-15

- Updated Good to Great's seventh registry diagram entry from the removed `pyramid with
  process loop` to `flow with Venn overlap and process loop`, matching Figure 21.7's
  current Flow, Venn, and ProcessLoop composition.

## Critique round 3 — 2026-07-15

### Required

None.

### Advisory

1. The round-2 registry finding is resolved. The seventh diagram record now says
   `flow with Venn overlap and process loop`, matching Figure 21.7's explicit Flow,
   Venn, and ProcessLoop composition. The round-1 corrections also remain intact:
   the people-first sequence is ordered correctly at the Flow component's native
   558-unit width, and the Thesis is two sentences with an 8-minute badge.

2. The earlier non-blocking cross-link note remains. `how-to-win-friends` appears in
   `ShelvedNearby` without a relationship clause in the preceding prose. The other
   two nearby links have relationship clauses, all three slugs resolve to done
   chapters, and the outbound link points directly to the publisher.

3. Within the repository's recorded evidence, the draft remains a faithful,
   original synthesis of the brief's humble-and-willful leadership, disciplined
   focus, and compounding momentum thesis. No new external web search was used.
   `npm run check` passed on 2026-07-15: validation and prose lint; both pipeline
   tests; all 46 Vitest tests; TypeScript and Vite production build; and ESLint.
   Vitest emitted only the existing non-failing jsdom `Window.scrollTo()` notices.
