verdict: resolved

## Critique round 1 — 2026-07-15

### Required

1. **Make all six figures legible at a 360 px viewport.** Every diagram in the
   chapter is rendered as `block w-full` with no chapter-local minimum width. At a
   360 px viewport, the layout and `Figure` padding leave roughly 278 px for each
   SVG. The 380-to-384-unit NodeGraph, Compare, Iceberg, and Spectrum therefore
   reduce their meaningful 9.5-to-12-unit labels to roughly 7-to-9 CSS px. The
   558-unit four-step Flow reduces its 11.5-unit labels to about 5.7 px and its
   9-unit sequence labels to about 4.5 px. The 416-unit Timeline reduces its
   9.5-unit sublabels to about 6.3 px. This fails the explicit phone-legibility
   requirement and the approximately 11 px floor established by completed
   chapters. Preserve chapter-local rendered widths that keep meaning-bearing text
   readable while using the existing horizontal-overflow wrapper, or provide
   compact mobile layouts. Do not change the shared diagram or Figure components.

2. **Recalculate the Hero reading-time badge from the final rendered text.** The
   chapter declares `minutes={9}`, but its reader-facing prose and headings are
   roughly 1,050 words before adding the comparatively short captions, diagram
   labels, exercise titles, and generated footer text. At the required approximate
   200 words per minute, rounded up, the complete page is about a seven-minute
   distillation, not nine. This is also consistent with completed chapters of
   comparable visible length. Set the badge from the final rendered count rather
   than the raw MDX source, whose JSX syntax inflates a plain file word count.

### Advisory

1. Figure 5.5 uses a Spectrum, whose vocabulary meaning is a matter of degree, and
   places currency at an unexplained `0.7` between personal and portable trust. The
   prose supports a change in trust mechanism, from knowing the counterparty to
   expecting shared acceptance, but not that numeric-looking position on a
   continuum. A comparison or network shape would encode the distinction more
   literally, or the existing spectrum could make the qualitative progression
   clearer and avoid an arbitrary marker position.

2. Scope the sentence “A biological mutation spreads only through reproduction” to
   inherited variants in human populations. As written, it is too broad because
   horizontal gene transfer is a biological counterexample, although the intended
   contrast between human genetic and cultural transmission remains sound.

3. The claim that money is not valuable because of the material in a coin or note
   is accurate for modern fiat money but overgeneralizes across commodity money and
   metal coinage. Qualifying the claim to money whose exchange value depends chiefly
   on shared acceptance would preserve the coordination point without erasing the
   historical exception.

4. Within the bounded evidence, the copyright posture is sound: the draft uses no
   quotation or real cover art, follows a thematic organization, and composes
   original labels through the shared diagram vocabulary rather than reproducing a
   source figure. The brief and seed metadata support the cooperation-around-shared-
   fictions thesis, the three-revolutions model, and the mandatory credibility
   caveat. The repository contains no source excerpts for a closer textual
   comparison, and this review began no external web search.

5. The remaining anatomy and technical wiring are sound. Five key ideas each have a
   captioned vocabulary diagram; the Model section renders the required three
   revolutions; the four exercises are concrete; the caveat plainly names contested
   causal claims and factual slips; the related slug is complete and its
   relationship is stated; the publisher link is direct; and the registry record is
   complete.

6. `npm run check` passed on 2026-07-15: queue/registry/content validation, prose
   lint, pipeline tests, fourteen Vitest tests, TypeScript and Vite production
   build, and ESLint all completed successfully. The jsdom run emitted only the
   existing non-failing `Window.scrollTo()` notices.

## Builder resolution — 2026-07-15

- Replaced the six full-width SVG classes with chapter-local minimum rendered widths
  inside the existing horizontal-overflow wrapper: 380 px for the node graph, 680 px
  for the four-step flow, 400 px for the comparison, 440 px for the iceberg and
  spectrum, and 480 px for the timeline. This keeps each figure's meaning-bearing
  labels at approximately 11 CSS px or larger at a 360 px viewport while preserving
  horizontal access to the wider diagrams.
- Recalculated the Hero badge from the final reader-facing page content and changed it
  from `9-min` to `7-min`.
- Preserved the chapter's original figure structure while clarifying the advisory
  issues recorded in this critique: scoped biological transmission to inherited
  variants in human populations, qualified the money claim to shared-acceptance
  money, and removed the spectrum's arbitrary currency marker in favor of two equal
  qualitative trust mechanisms.
