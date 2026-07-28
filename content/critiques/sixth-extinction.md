verdict: revise

## Critique round 1 — 2026-07-28

### Required

1. **The registry entry is not complete enough for `done`.** The entry at
   `content/registry.json:2526-2534` contains only `num`, `slug`, `title`,
   `subtitle`, `part`, `routes`, and `status`. It omits the brief's tier, the page
   thesis, the explicit reason the Model section is absent, and the five diagram
   forms. Neighboring completed entries carry those fields, and definition of done
   item 7 requires them. Populate the chapter metadata before approval.

2. **Figure 128.1 does not encode the key idea or its caption.** The section argues
   that mass extinction is a change in the pace and breadth of loss, and the caption
   calls the present a rapid shift in that pace. The equal-width timeline at
   `src/chapters/sixth-extinction.mdx:43-54` shows a sequence of labels but no rate,
   magnitude, breadth, or contrast between background turnover and extinction
   pulses. It therefore cannot teach the stated idea and may read as five successive
   stages, including the five deep-time events as one stage. Revise the visual so it
   structurally conveys the contrast without presenting invented quantitative data,
   or narrow the key idea and caption to what the timeline actually shows.

3. **Two consequential factual claims outrun the recorded evidence.** First,
   `src/chapters/sixth-extinction.mdx:113` says human transport operates at a speed
   "no animal migration could match." The invasive-species assessment recorded in
   `content/evidence/sixth-extinction.md` supports human-mediated introductions and
   their consequences, not that absolute comparison. Second,
   `src/chapters/sixth-extinction.mdx:195-197` asserts a scientific debate over
   whether a strict geological mass-extinction threshold has already been crossed,
   but none of the evidence notes is recorded as support for that threshold claim.
   Rephrase both claims to the narrower propositions supported by the recorded
   sources, or record direct support for the claims as written.

### Advisory

1. The Shelved Nearby clause says *The Selfish Gene* explains why "small population
   changes matter over generations." That is looser than the linked page's actual
   gene-centered selection thesis. A relationship framed around differential
   reproduction or selection would make the cross-link more precise.

2. `npm run check` passed in full on 2026-07-28: validation, prose lint, 40 pipeline
   tests, 274 application tests, typecheck, production build, and lint all passed.

## Builder resolution — 2026-07-28

- Completed the registry metadata with tier, page thesis, the explicit reason The Model is
  absent, and the five in-vocabulary diagram forms. The chapter remains `draft`.
- Replaced Figure 128.1's equal-width timeline with an in-vocabulary comparison that contrasts
  dispersed background turnover with the concentrated time span and breadth of a mass
  extinction. Its caption now states that contrast directly without numerical claims.
- Narrowed the human-transport claim to human-mediated connections between previously separate
  places, removed the unsupported geological-threshold debate claim, and retained the IUCN
  measurement caveat supported by the recorded evidence.
- Tightened the *The Selfish Gene* cross-link to differential reproduction changing population
  composition over generations.

## Critique round 2 — 2026-07-28

### Required

1. **The Thesis does not follow the fixed one-to-two-sentence contract.** The block at
   `src/chapters/sixth-extinction.mdx:13-18` is four sentences: a framing sentence,
   the central claim, a qualification, and a second formulation of the claim. The
   authoring spec requires this section to compress the entire argument into one or
   two sentences. Reduce it to that form while preserving the causal claim and the
   useful qualification that mass extinction does not mean every species disappears.

2. **Figure 128.4 puts prevention after the event it must prevent.** The shared
   `Flow` component attaches its branch after the last step, so the sequence at
   `src/chapters/sixth-extinction.mdx:125-131` reads: human transport, new arrival,
   novel interaction, local vulnerability, then “prevention or removal.” That
   conflicts with the surrounding prose and Exercise 03, which correctly distinguish
   prevention before introduction from response after an arrival. Move prevention
   to the appropriate point in the sequence, or relabel the post-arrival branch as
   containment/removal so the diagram teaches the intervention chronology accurately.

### Advisory

1. Figure 128.1's third comparison row is not structurally parallel:
   “ecological roles can be refilled” and “ecological roles are abruptly reordered”
   can both occur on different timescales, and the recorded evidence does not establish
   this as a defining binary. The first two rows already carry the supported contrast
   in pace and breadth; removing or tightening the third would make the figure cleaner.

2. The three required findings from round 1 are resolved. The registry metadata is
   complete, Figure 128.1 now encodes pace and breadth, the unsupported transport and
   threshold claims are gone, and the *Selfish Gene* cross-link is precise.
   `npm run check` passed in full on 2026-07-28: validation, prose lint, 40 pipeline
   tests, 274 application tests, typecheck, production build, and lint all passed.
