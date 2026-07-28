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
