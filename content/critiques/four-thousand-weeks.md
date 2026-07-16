verdict: approve

## Critique round 1 — 2026-07-16

### REQUIRED

1. **Recompute the Hero reading-time badge from the final rendered page.** A direct
   render contains 1,188 reader-visible words, including the Hero, headings,
   captions, SVG labels, exercise titles, generated cover metadata, and nearby
   footer. At the authoring spec's approximately 200 words per minute, rounded up,
   this is a six-minute distillation, not `minutes={8}`
   (`src/chapters/four-thousand-weeks.mdx:5-9`). Set the badge to six minutes and
   recompute it if the rendered text changes during resolution.

### ADVISORY

None. Within the repository's bounded evidence, the brief and seed record support
the finitude thesis and the deliberate absence of a Model section. The five key
ideas each have a captioned, in-vocabulary structural diagram whose labels agree
with the prose, and the practice cards turn those ideas into concrete actions. The
optional caveat responsibly distinguishes acceptance of human limits from acceptance
of avoidable harm or unequal control over time. All three nearby links resolve to
done chapters. The draft contains no quotation or real cover art and uses shared
diagram primitives with original labels rather than a bespoke reproduction of a
book figure. No separate chapter-specific evidence dossier or source excerpts are
recorded, and this review began no external web search. `npm run check` passed on
2026-07-16, including validation, prose lint, pipeline tests, 116 application tests,
typecheck, production build, and lint.

## Builder resolution — 2026-07-16

- Changed the `Hero` reading-time prop in `src/chapters/four-thousand-weeks.mdx`
  from `minutes={8}` to `minutes={6}`. The recorded final rendered count is 1,188
  reader-visible words, which rounds up to a six-minute distillation at approximately
  200 words per minute; the one-word badge substitution leaves that count unchanged.
- Preserved the affirmed five captioned key-idea diagrams, deliberate absence of a
  Model section, caveat, and resolved nearby links. No external research was added.
- Ran `npm run check` successfully on 2026-07-16: validation, prose lint, pipeline
  tests, 116 application tests, typecheck, production build, and lint passed.

## Critique round 2 — 2026-07-16

### REQUIRED

None.

### ADVISORY

None. The round 1 reading-time finding is resolved: `minutes={6}` agrees with the
recorded 1,188-word rendered count at approximately 200 words per minute, rounded
up. The brief and seed metadata support the finitude thesis, and the registry records
the deliberate absence of a signature Model section. Five key ideas each have a
captioned diagram from the shared vocabulary, with labels that match the prose; the
practice cards are concrete, and the optional caveat distinguishes finite personal
choice from avoidable harm and unequal control over time. The related slugs resolve
to built chapters, and the page uses the generated typographic cover. No separate
chapter-specific component or evidence dossier is recorded, and this review began no
external web search. `npm run check` passed on 2026-07-16, including validation,
prose lint, pipeline tests, 116 application tests, typecheck, production build, and
lint.
