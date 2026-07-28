verdict: approve

## Critique round 1 — 2026-07-28

### Required

1. The Model figure does not encode the model described by its prose and caption. The prose says the action happens now inside conditions that extend outward across timescales, and the caption likewise places behavior inside those conditions. The `Concentric` instance instead passes `externalLabel="a behavior happens now"`, whose component explicitly renders that label outside the rings, while the core is labeled “neural activity, seconds.” As rendered and exposed to assistive technology, the figure says the behavior is outside the causal layers. Revise the hero diagram so the behavior and nested timescales have the same spatial relationship in the visual, caption, and explanation.

2. The `behave` registry entry is incomplete for a done chapter. It contains the identity fields and `status`, but omits the brief's tier plus the authoring spec's required `thesis`, `framework`, and `diagrams` metadata. Populate those fields with values that agree with the finished page before approval.

### Advisory

None. `npm run check` passed on 2026-07-28.

## Builder resolution — 2026-07-28

- Revised the Model figure so “a behavior, now” is the innermost ring, surrounded in order by neural activity, body and recent state, development and culture, and evolutionary history. The visual, caption, prose, and accessible ring order now all place behavior inside its causal conditions.
- Completed the `behave` registry entry with tier 3, the brief-aligned thesis, the nested-timescales framework description, and the six diagram forms used on the finished page. The chapter remains `draft` and is not marked done.

## Critique round 2 — 2026-07-28

### Required

1. The Hero's `minutes={9}` badge does not follow the authoring spec's reading-time calculation. Rendering the actual MDX with its real shared and chapter components produces 1,518 visible words. At approximately 200 words per minute, rounded up, that is an 8-minute distillation. Recompute the badge from the rendered page and set it to 8.

2. The acute-stress example overstates the recorded evidence. The evidence note says the study associated acute psychosocial stress with larger task-switching costs during measured post-stress intervals. The Callout instead says it found “impaired flexible goal switching,” which turns a narrow measured task-switching result into a broader claim about goal switching. Describe the recorded outcome and its limited scope directly.

### Advisory

None. The two round-one findings remain resolved, and `npm run check` passed on 2026-07-28.

## Builder resolution — 2026-07-28

- Recomputed the Hero badge from the recorded rendered-page count of 1,518 visible words: at approximately 200 words per minute, rounded up, *Behave* is now an 8-minute distillation.
- Replaced the broad claim about “flexible goal switching” with the evidence note's limited finding: acute psychosocial stress was associated with larger task-switching costs during measured post-stress intervals in one sample.
- Rechecked the prior round's Model and registry fixes. The behavior remains the innermost causal layer in the hero diagram, and the draft registry entry retains its tier, thesis, framework, and diagram metadata.

## Critique round 3 — 2026-07-28

### Required

1. The two mandatory carry-away sections exceed the authoring spec's explicit length
   limits. “The thesis” contains four sentences, while “If you remember one thing”
   contains three; each must be one or two sentences. Compress both sections without
   losing the distinction between explaining behavior and excusing it.

2. The “Yesterday is still in the room” timeline does not present a coherent temporal
   order. It runs from “last night” to the broader interval “this week,” then to “this
   hour” and “this moment.” Because last night falls within this week, the first two
   segments reverse the move from broader recent history toward the present and do
   not encode the accumulation described by the prose and caption. Reorder or relabel
   the segments so the axis advances consistently toward the current response.

### Advisory

None. The four findings from rounds 1 and 2 remain resolved. `npm run check` passed
on 2026-07-28, including 269 Vitest tests, TypeScript, the production build, and
ESLint; the repeated jsdom `Window.scrollTo()` notices were non-failing test output.

## Builder resolution — 2026-07-28

- Compressed “The thesis” to two sentences, retaining the distinction between explaining behavior and treating it as harmless or unavoidable.
- Compressed “If you remember one thing” to two sentences and made its final clause explicit: wider explanation supports prevention and fairer responsibility without excusing harm.
- Reordered the “Yesterday is still in the room” timeline as earlier this week, last night, this hour, and this moment, so it moves consistently toward the response without overlapping time labels.
- Rechecked the earlier Model, registry, reading-time, and acute-stress scope fixes; they remain present. The chapter remains `draft` and is not marked done.

## Critique round 4 — 2026-07-28

### Required

None. The round-three length and timeline findings are resolved in the draft, and
the required fixes from rounds one and two remain intact.

### Advisory

None. `npm run check` passed on 2026-07-28, including validation, prose lint, 42
pipeline and runner tests, 269 Vitest tests, TypeScript, the production build, and
ESLint. The repeated jsdom `Window.scrollTo()` notices were non-failing test output.
