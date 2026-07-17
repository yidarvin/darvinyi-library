verdict: approve

## Critique round 1 — 2026-07-17

### REQUIRED

1. **Rebuild the Model figure around the book's actual BHAG structure.** Figure 64.6
   turns core purpose, core values, learning mechanisms, and BHAG into prerequisite
   pyramid tiers, then makes the BHAG flow into a vivid picture
   (`src/chapters/built-to-last.mdx:151-178`). That hierarchy is not established by
   the prose or the chapter brief, and it splits the two parallel parts of core
   ideology into successive levels. In the book's framework, an envisioned future
   pairs a 10-to-30-year BHAG with a vivid description; the vivid picture is not a
   downstream result of the BHAG. The practice card compounds the error by asking for
   a three-to-ten-year goal (`src/chapters/built-to-last.mdx:200-203`). Render the
   signature model without inventing a dependency hierarchy, keep core values and
   purpose structurally parallel if they appear, show the BHAG and vivid description
   in their correct relationship, and correct the operating horizon.

2. **Correct Figure 64.2's structural claim about core ideology.** The text correctly
   says core ideology has two parts, core values and core purpose, but the imported
   `Concentric` primitive explicitly interprets its array as nested rings from the
   core outward. The current labels therefore place purpose around values as a
   separate layer (`src/chapters/built-to-last.mdx:54-76`;
   `src/components/diagrams/Concentric.tsx:8-20,48-78`). The caption instead says
   both belong at the center. Make the visual encode values and purpose together as
   parallel parts of the enduring core, with strategies and practices outside it.

3. **Restore phone legibility for Figures 64.1 through 64.4.** At a 360px viewport,
   the article and Figure padding leave approximately 278px for each SVG. These four
   diagrams have 380-to-384-unit viewBoxes but use `className="block w-full"`, so the
   shared overflow wrapper shrinks them instead of scrolling them
   (`src/chapters/built-to-last.mdx:39-127`; `src/components/Figure.tsx:17-19`). That
   reduces meaning-bearing text to roughly 8px in the Compare and Concentric figures,
   about 7px for Matrix notes and axes, and 8-to-9px in the ProcessLoop. Preserve
   suitable chapter-local minimum widths, or provide equally legible compact mobile
   compositions. Figures 64.5 and 64.6 already activate horizontal scrolling through
   their minimum-width constraints; do not edit the shared primitives to fix the
   four undersized figures.

4. **Complete the registry record before approval.** The `built-to-last` entry has
   only its identity, shelf, route, and draft status; it omits the required `tier`,
   `thesis`, `framework`, and `diagrams` fields
   (`content/registry.json:1262-1271`). Add the seed-supported tier and thesis, record
   BHAG as the framework, and inventory every rendered diagram form after the Model
   figure is corrected. The authoring spec's definition of done requires these
   fields even though the current draft-state validator permits the partial entry.

5. **Compress The Thesis to the specified one or two sentences.** The section is
   currently three sentences (`src/chapters/built-to-last.mdx:14-20`). It conveys the
   right core argument, but it does not meet the fixed anatomy's requirement for a
   one- or two-sentence carry-away paragraph.

6. **Recompute the Hero badge from the final rendered page.** A direct static render
   of the current draft contains 1,656 visible alphanumeric word tokens, including
   headings, component text, captions, and SVG labels. At approximately 200 words
   per minute, rounded up, that is a nine-minute distillation, not the declared eight
   minutes (`src/chapters/built-to-last.mdx:8-12`). Recount after the required edits
   and set the badge from that final render.

### ADVISORY

1. The four nearby covers resolve to completed chapters, but the page gives none of
   them the relationship clause requested by the cross-linking guidance
   (`src/chapters/built-to-last.mdx:224-228`). A short sentence before
   `ShelvedNearby` could explain why each selected title belongs here, or the list
   could be narrowed to links whose relationship is worth stating.

2. The brief, seed metadata, registry record, and draft are the only local evidence
   found for this chapter; there is no separate chapter-specific evidence dossier,
   and this review began no external web search. The central thesis, core-ideology
   distinction, clock-building idea, and BHAG model can be checked against those
   records and the framework itself. The claim that several celebrated comparison
   companies later suffered serious setbacks (`src/chapters/built-to-last.mdx:209-216`)
   is plausible but not locally recorded. If it remains, naming the relevant cases
   in a recorded evidence note would make the caveat auditable.

3. Apart from the findings above, the page has five key ideas with captioned
   vocabulary diagrams, concrete practice cards, a useful causal and ethical caveat,
   a generated typographic cover, original thematic prose, and a direct publisher
   link. The draft imports no chapter-specific component; all directly imported
   shared components and the six used diagram primitives were inspected.

4. `npm run check` passed on 2026-07-17: queue/registry/content validation, prose
lint, 2 pipeline tests, 37 runner tests, 132 application tests, typecheck and
production build, and ESLint all completed successfully. Vitest emitted only the
existing non-failing jsdom `Window.scrollTo()` notices. The gate does not measure
SVG label size at the required mobile viewport or enforce complete draft metadata.

## Builder resolution — 2026-07-17

- Replaced the Model pyramid and BHAG-to-picture flow with a comparison that keeps
  core ideology distinct from an envisioned future, and shows the envisioned future
  as the paired 10-to-30-year BHAG and vivid description. Updated the corresponding
  key-idea flow and practice card to use the 10-to-30-year horizon.
- Added the reusable `CoreContext` diagram form and vocabulary entry. Figure 64.2
  now places core values and core purpose as peer elements in one enduring core,
  with strategies, practices, and markets and technology outside it.
- Added chapter-local SVG minimum widths of 384px, 440px, 384px, and 380px to
  Figures 64.1 through 64.4 so the existing Figure overflow wrapper scrolls rather
  than reducing their labels at a 360px viewport.
- Completed the `built-to-last` registry entry with tier 2, the seed thesis, BHAG
  framework, and the final six rendered diagram forms.
- Reduced The Thesis to two sentences. A final static render counted 1,500 visible
  alphanumeric word tokens, which rounds to the retained 8-minute Hero badge at
  approximately 200 words per minute.
- `npm run check` passed after these changes.

## Critique round 2 — 2026-07-17

### REQUIRED

None.

The current draft resolves every required finding from round 1. The Model preserves
the parallel structure of core ideology and the paired structure of the envisioned
future; the goal horizon is consistently 10 to 30 years; the core/context figure
keeps values and purpose as peers; all six diagrams have chapter-local minimum
widths suitable for the shared overflow treatment; the registry metadata is
complete; The Thesis is two sentences; and the eight-minute badge agrees with the
builder's recorded 1,500-token static-render count.

### ADVISORY

1. The page still does not state the relationship between each nearby title and
   this one. The four links resolve to completed chapters, so this remains optional
   cross-link context rather than a blocker.

2. No chapter-specific evidence dossier exists locally. The brief, seed metadata,
   draft, and recorded round-1 review support the central framework, but the claim
   that several comparison companies later suffered serious setbacks remains less
   auditable than the rest of the page. No external search was started for this
   review.

3. `npm run check` passed on 2026-07-17: queue/registry/content validation, prose
   lint, 2 pipeline tests, 37 runner tests, 132 application tests, typecheck,
   production build, and ESLint all completed successfully. Vitest emitted only
   non-failing jsdom `Window.scrollTo()` notices.
