verdict: revise

## Critique round 1 — 2026-07-26

### Required

1. **Make Figure 91.2 visibly preserve the full field of choice stated in the prose.**
   The section places preparation, judgment, speech, and the next act on the
   actionable side of the Stoic boundary, while treating results, other people, the
   past, and chance as conditions (`src/chapters/daily-stoic.mdx:50-60`). The figure
   instead accents only the innermost `judgment` ring and renders `preparation and
   conduct` with the same muted treatment as `the result`
   (`src/chapters/daily-stoic.mdx:62-72`). Because the shared `Concentric` component
   uses its single highlight to identify the emphasized core
   (`src/components/diagrams/Concentric.tsx:48-60,65-77`), the visible encoding
   contradicts both the prose and caption by separating chosen conduct from
   judgment. Recompose the chapter-local figure with an in-vocabulary form or labels
   that clearly group judgment, preparation, and conduct as available choices while
   keeping results and external conditions distinct. Do not edit the shared
   component.

2. **Replace Figure 91.4's unsupported hierarchy with a form that treats the named
   qualities as parallel standards.** The prose presents clear judgment, restraint,
   courage, and fairness as qualities brought to a situation, with no claim that one
   is a prerequisite, foundation, or higher achievement than another
   (`src/chapters/daily-stoic.mdx:95-106`). The `Pyramid` renders `clear judgment` as
   the widest base, `self-command` as a middle tier, and accented `courage and
   fairness` as the apex (`src/chapters/daily-stoic.mdx:108-118`). The documented
   vocabulary reserves this form for layered or prerequisite structures, and the
   component's accessible label explicitly calls the result a hierarchy from the
   base up (`src/components/diagrams/Pyramid.tsx:9-20,32-45`). Use an in-vocabulary
   composition that shows mutually relevant qualities without inventing a ranking,
   or add prose and evidence only if this particular hierarchy is genuinely part of
   the book's argument.

### Advisory

1. Within the repository's bounded evidence, the factual and copyright posture is
   otherwise sound. The brief and evidence record support the 2016 authorship, the
   366-day daily-reader format, the use of translated ancient Stoic material with
   commentary, and the deliberate absence of one signature model. The draft uses no
   quotation, real cover art, empirical result, or apparent reproduction of a source
   figure. Its thematic organization and wording are original synthesis. This review
   began no external web search.

2. Apart from the two required visual mappings, the anatomy is strong. Five key
   ideas each have a captioned shared-vocabulary diagram, the Model section is
   correctly absent under the brief, four practice cards specify observable actions,
   and the caveat rejects emotional numbness, passive tolerance of harm, victim
   blaming, and replacement of professional or community support. The eight-minute
   badge is consistent with the reader-facing length at approximately 200 words per
   minute rounded up.

3. All three nearby slugs resolve to done chapters, their relationships are stated in
   prose, and the outbound link is the publisher page recorded in the evidence file.
   The ProcessLoop, Flow, and NodeGraph figures otherwise match their neighboring
   explanations. Their chapter-local minimum widths remain readable through
   `Figure`'s horizontal-overflow wrapper rather than shrinking their labels below
   the shared components' intended phone treatment.

4. `npm run check` completed with `CHECK OK` on 2026-07-26. Queue, registry,
   critique, and content validation; prose lint; all pipeline tests; all 188 Vitest
   tests; TypeScript and Vite production build; and ESLint passed. Vitest emitted
   only the existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-26

1. Replaced Figure 91.2's concentric-circle encoding with the in-vocabulary
   `Compare` form. Its accented "available choices" panel now lists preparation,
   judgment, speech, and the next act together, while its peer panel lists other
   people, the past, chance, and results as conditions to meet. The revised
   caption states the same full boundary.

2. Replaced Figure 91.4's `Pyramid` with `CoreContext`, so clear judgment,
   restraint, courage, and fairness appear as four peer standards inside changing
   conditions rather than as a ranked structure. Extended `CoreContext` with a
   bounded two-by-two layout for four or more core items and added a regression
   test that verifies the four peer cards remain within the core.

3. Preserved the prior chapter prose, evidence posture, caveats, linked books, and
   all other diagrams. `npm run test -- src/test/chapters.test.tsx` passed before
   the full gate, and `npm run check` completed with `CHECK OK` afterward.

## Critique round 2 — 2026-07-26

### Required

1. **Update the registry's diagram inventory to match the resolved chapter.**
   Figures 91.2 and 91.4 now use the imported `Compare` and `CoreContext` forms
   (`src/chapters/daily-stoic.mdx:3,62-75,110-118`), but the registry still lists
   their superseded forms, `concentric circles` and `pyramid`
   (`content/registry.json:1810-1815`). The authoring definition of done requires a
   complete registry entry, and the critique rubric requires registry and content
   agreement. Replace those two stale inventory values with the vocabulary names
   for the forms the page actually renders, preserving the diagram order. The
   current validator does not compare this metadata with MDX imports, so
   `npm run check` passing does not resolve the inconsistency.

### Advisory

1. The two findings from round 1 are otherwise resolved. Figure 91.2 now groups
   preparation, judgment, speech, and the next act together as available choices,
   and Figure 91.4 renders clear judgment, restraint, courage, and fairness as peer
   items rather than a hierarchy. The revised components' visible and accessible
   encodings agree with the prose and captions.

2. No new factual, copyright, anatomy, practice, caveat, related-link, or
   phone-legibility defect was found in this pass. The chapter remains an original
   thematic synthesis within the brief and recorded evidence, deliberately omits a
   signature Model section, and uses five captioned vocabulary diagrams. This
   review began no external web search.

3. `npm run check` completed with `CHECK OK` on 2026-07-26. Queue, registry,
   critique, and content validation; prose lint; all pipeline tests; all 189
   Vitest tests; TypeScript and Vite production build; and ESLint passed. Vitest
   emitted only the existing non-failing jsdom `Window.scrollTo()` notices.
