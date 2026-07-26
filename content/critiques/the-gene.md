verdict: resolved

## Critique round 1 — 2026-07-26

### Required

1. Complete the `the-gene` registry record. It currently ends after `status` and
   omits the required `tier`, `thesis`, `framework`, and `diagrams` fields
   (`content/registry.json:1661-1669`). Record tier 2, the chapter thesis, the
   brief's deliberate absence of a signature framework and Model section, and the
   diagram forms actually rendered after the revisions below. The authoring spec
   makes this metadata part of done even though the current validator accepts the
   draft.

2. Compress **The thesis** to the fixed one-or-two-sentence anatomy. The current
   block uses four sentences (`src/chapters/the-gene.mdx:13-18`). Its scientific
   arc and ethical qualification belong together, but the section must remain the
   compact argument a reader can carry away if they read nothing else.

3. Rework Figure 84.5 so its visual grammar and claims match the distinction the
   section teaches (`src/chapters/the-gene.mdx:144-171`). `Spectrum` is defined for
   matters of degree, yet somatic treatment and heritable alteration are different
   scopes of intervention, not poles on one measured continuum. The arbitrary
   marker at `0.28` and the empty middle do not encode a biological or ethical
   variable. The labels and prose also turn noninheritance into the stronger claim
   that somatic treatment's “effects stay with” or “are limited to” the patient.
   The recorded FDA evidence establishes an ex vivo treatment using a patient's
   own hematopoietic stem cells, while the WHO evidence emphasizes uncertainty; it
   does not support that broad patient-only consequence claim. Use a fitting
   vocabulary form, distinguish edits that are not intended to be inherited from
   heritable edits, and keep wider treatment burdens and consequences visible.

4. Make Figure 84.1's labels legible at phone width. Five `Timeline` segments
   produce a `656`-unit-wide viewBox, but the chapter supplies only
   `min-w-[480px]` (`src/chapters/the-gene.mdx:41-53`;
   `src/components/diagrams/Timeline.tsx:20-26`). Because the explicit class
   replaces the shared SVG's default full-width class, the figure renders at that
   480px minimum inside the horizontal scroller. Its 11.5-unit headings therefore
   become about 8.4 CSS pixels and its 9.5-unit sublabels about 7 pixels. Scrolling
   cannot recover text that has already been scaled that small. Increase the
   rendered minimum to preserve readable type, or reduce/recompose the timeline so
   its labels remain legible in the phone scroller.

5. Bring the claimed benefits of genome sequencing inside the recorded evidence.
   The chapter says sequencing can identify variants behind rare disorders, guide
   some cancer care, and make population research more detailed
   (`src/chapters/the-gene.mdx:115-121`). The evidence note records support for the
   history and coverage of human-genome sequencing and for the limits of genetic
   testing, but it does not record support for those three clinical and research
   capabilities (`content/evidence/the-gene.md:8-10`). These claims carry the
   positive half of the section's account of genome reading, so they materially
   shape what the reader thinks sequencing can do. Record direct support for them,
   or narrow the passage to what the existing evidence establishes.

### Advisory

1. Figure 84.3 establishes that four influences contribute to an outcome, but it
   does not show the interactions promised by the caption or the “network” heading:
   every edge independently terminates at the outcome
   (`src/chapters/the-gene.mdx:82-113`). The core anti-deterministic point remains
   recoverable, so this is not blocking, but either show at least one supported
   interaction or describe the figure as converging influences.

2. Within the repository's bounded record, the copyright posture is otherwise
   sound. The chapter uses original thematic organization, no quotation or real
   cover art, and shared vocabulary primitives rather than an apparent reproduction
   of a source figure. The evidence file contains source summaries rather than book
   excerpts, so this review could not perform sentence-level close-paraphrase
   comparison and began no new external web search.

3. The remaining anatomy and wiring are sound. Five key ideas each have a captioned
   vocabulary figure; omission of a Model follows the brief; the four exercises are
   concrete; both related slugs resolve to done chapters; and the outbound link
   matches the recorded bookseller source.

4. `npm run check` completed with `CHECK OK` on 2026-07-26. Queue and registry
   validation, prose lint, 42 pipeline tests, 173 Vitest tests, TypeScript, the Vite
   production build, and ESLint all passed. Vitest emitted only the existing
   non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-26

Resolved every required finding from round 1. The registry record now includes tier 2,
the rendered chapter thesis, the deliberate absence of a signature framework and Model
section, and the five rendered diagram forms. The Thesis is now two sentences.

Figure 84.1 now renders at a 720px minimum width in its horizontal scroller, preserving
the Timeline labels at or above their SVG font sizes. Figure 84.5 now uses a Comparison,
not a Spectrum: it distinguishes somatic edits not intended to be inherited from edits
involving eggs, sperm, or embryos that could affect descendants. Its text retains the
documented conditioning, monitoring, follow-up, consent, and outcome-uncertainty concerns
without claiming somatic effects are confined to one person.

The genome-reading section now limits its positive claim to the recorded history of a
reference human genome, from the 2003 approximately 92-percent sequence to later gap-free
completion, and keeps the recorded testing limits. The non-blocking Figure 84.3 advisory
was also addressed by describing the rendered independent edges as converging influences,
rather than depicting unsupported interactions.
