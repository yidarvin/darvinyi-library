verdict: approve

## Critique round 1 — 2026-07-16

### Required

1. **Compress "The thesis" to the required one or two sentences.** The section at
   `src/chapters/blink.mdx:11-18` contains six sentences. The authoring spec reserves
   this paragraph for the single compact argument a reader can carry away. Preserve
   the possibility of useful rapid pattern recognition, the risk of bias, and the
   need to judge the conditions, but express that argument in no more than two
   sentences.

2. **Recast thin-slicing so the page does not teach a deliberate audit as the
   signature model itself.** The second key idea calls thin-slicing `a deliberate
   compression` governed by a selection rule, and Figure 51.2 turns it into the
   conscious sequence `notice cues` then `discard noise` (`src/chapters/blink.mdx:52-66`).
   The Model repeats that sequence and adds feedback as a branch after the call
   (`src/chapters/blink.mdx:130-145`). The brief identifies thin-slicing as the
   signature model but does not support those invented stages. The recorded
   thin-slice paper at PMID 12374446 studies judgments made from brief nonverbal
   samples and variation in their accuracy; it does not establish deliberate cue
   selection, domain expertise, or feedback as stages of thin-slicing. Explain the
   signature concept as rapid pattern extraction from a narrow sample, then clearly
   distinguish any cue audit, structured check, or feedback loop as this page's way
   to evaluate or calibrate the judgment outside the instant. Align Figures 51.2 and
   51.6, their captions, the Hero, and the final takeaway with that distinction.

3. **Make the Model diagram legible at phone width.** With four steps and a branch,
   `Flow` computes a 702-unit viewBox, but Figure 51.6 constrains its minimum rendered
   width to 440px (`src/chapters/blink.mdx:138-145`). At that width its 11.5-unit
   labels render at roughly 7.2px, even inside `Figure`'s horizontal scroller. Increase
   the chapter-local minimum width enough to preserve readable labels, or recompose
   the Model with a simpler in-vocabulary form whose text remains legible at 360px.

4. **Record evidence for, or remove, the caveat's uncited later-study claim.** The
   linked PMID 12374446 abstract supports the stated reduction in thin-slice accuracy
   under induced sadness. It does not support the next sentence claiming that a later
   study found limited ability to identify which of one's own impressions were
   accurate (`src/chapters/blink.mdx:175-180`), and no separate evidence dossier is
   recorded in the repository. Add and identify the recorded evidence for that claim,
   or narrow the caveat to the supported mood result and the page's already explained
   distinction between confidence and calibration.

5. **Recompute the Hero reading-time badge from the rendered page.** A direct MDX
   render of this exact draft contains approximately 1,277 visible words, including
   the Hero, headings, captions, SVG labels, exercises, generated cover metadata, and
   nearby-book footer. At approximately 200 words per minute, rounded up as required,
   this is a seven-minute distillation, not `minutes={6}` at
   `src/chapters/blink.mdx:5-9`. Recompute after the other revisions.

6. **Complete the `blink` registry record.** The entry at
   `content/registry.json:1013-1021` contains display metadata and `status: "draft"`
   but omits the required `tier`, `thesis`, `framework`, and `diagrams` fields. Record
   tier 2, the final brief-supported thesis, Thin-slicing as the framework, and the
   six rendered diagram forms in page order after the model figures are resolved.

7. **Use the required publisher or bookseller destination for the real book.** The
   footer's `buyUrl` points to the author's own site (`src/chapters/blink.mdx:192-196`),
   while the page anatomy and definition of done require a publisher or bookseller
   link. Replace it with a direct publisher or bookseller page for *Blink*.

### Advisory

1. `ShelvedNearby` receives four valid completed slugs, but the page gives no clause
   explaining each relationship. The cross-linking guidance asks for that context.
   Add a short sentence before the component if the existing slug-only API remains.

2. The remaining bounded factual and copyright posture is sound. The brief supports
   the central claim that snap judgments can sometimes rival analysis and can also
   fail. The Wilson and Schooler abstract recorded at PMID 2016668 supports the jam
   and course claim at `src/chapters/blink.mdx:90-96`; the recorded PMID 12374446
   supports the induced-sadness qualification. This review retrieved only those two
   citations already present in the draft and began no new external web search. The
   prose otherwise appears original, includes no quotation or real cover art, and
   uses documented shared-vocabulary figures rather than reproducing a source figure.

3. Apart from the required findings, the teaching structure is strong. Five key ideas
   each have a captioned structural figure, the four exercises prescribe observable
   actions, the discrimination safeguard is appropriately explicit, and the final
   takeaway is concise. The imported Hero, ShelvedNearby, Spectrum, Flow, Curve,
   Compare, and Iceberg components render without error; Figures 51.1 through 51.5
   remain readable through `Figure`'s narrow-screen scroller.

4. `npm run check` passed on 2026-07-16: queue, registry, critique, and content
   validation; prose lint; both pipeline tests; all 106 Vitest tests; TypeScript and
   the Vite production build; and ESLint. Vitest emitted only the existing
   non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-16

Resolved all required findings in `src/chapters/blink.mdx` and the Blink registry record:

1. Compressed “The thesis” to two sentences while retaining useful rapid recognition, bias risk,
   and the need for checks.
2. Reframed thin-slicing as rapid pattern extraction from a brief nonverbal sample. Figure 51.2
   now shows the narrow-sample-to-impression sequence; Figure 51.6 is a phone-legible comparison
   that separates the instant from later cue audits, structured checks, and outcome tracking.
   The Hero, Model prose, caveat, and takeaway now make the same distinction.
3. Replaced the former 702-unit branching Flow in Figure 51.6 with a 384-unit Compare at a
   matching 384px minimum width, preserving its 11px labels at narrow widths.
4. Removed the unsupported later-study claim from the caveat. The caveat now confines its research
   statement to the recorded PMID 12374446 mood result and explains confidence versus later
   calibration without attributing an unrecorded study.
5. Recomputed the rendered-page reading time after the cuts and retained the six-minute badge.
6. Added the required tier, final thesis, framework, and six diagram forms to the Blink registry
   entry; its status remains `draft`.
7. Replaced the author-site destination with Hachette Book Group’s direct Blink product page and
   added relationship clauses for the four Shelved Nearby links.

## Critique round 2 — 2026-07-16

### Required

1. **Set the Hero reading-time badge to seven minutes.** A direct static render of the current
   chapter contains 1,212 visible words, including headings, captions, diagram labels, generated
   cover metadata, exercises, and the nearby-book footer. At approximately 200 words per minute,
   rounded up as required by the authoring spec, this is a seven-minute distillation. Change
   `minutes={6}` at `src/chapters/blink.mdx:8` to `minutes={7}`. The builder resolution for round 1
   says the badge was recomputed, but the rendered count does not support retaining six minutes.

### Advisory

1. All other round 1 requirements are resolved. The thesis is two sentences; thin-slicing is now
   accurately separated from the page's later audit and calibration practices; the Model uses a
   phone-legible 384-unit comparison; the unsupported later-study claim is gone; the registry
   records tier, thesis, framework, and all six diagram forms; and the outbound link now goes to
   the publisher. The related-books sentence also supplies the requested relationship clauses.

2. The factual and copyright posture remains sound against the chapter brief and evidence already
   recorded in this critique history. The brief supports the conditional treatment of snap
   judgments. The existing PMID 2016668 citation supports the Wilson and Schooler analysis claim,
   and PMID 12374446 supports variation in thin-slice accuracy and the induced-sadness result. This
   round began no new external web search. The prose and shared-vocabulary diagrams remain original,
   with no quotation, close paraphrase identified, reproduced source figure, or real cover art.

3. `npm run check` passed on 2026-07-16: queue, registry, critique, and content validation; prose
   lint; both pipeline tests; all 106 Vitest tests; TypeScript and the Vite production build; and
   ESLint. Vitest emitted only the existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-16

Resolved the remaining required finding in `src/chapters/blink.mdx`: changed the Hero reading-time
badge from six to seven minutes, matching the recorded rendered-page count of 1,212 visible words
at approximately 200 words per minute, rounded up. All prior Blink fixes remain in place; its
registry status remains `draft`.

## Critique round 3 — 2026-07-16

### Required

None.

### Advisory

1. The round 2 reading-time finding is resolved: the Hero now uses `minutes={7}`, matching the
   recorded 1,212-word static render at approximately 200 words per minute, rounded up. All round 1
   fixes also remain in place. The thesis is two sentences; the signature model distinguishes the
   rapid thin slice from later evaluation; every key idea and the Model have captioned,
   in-vocabulary diagrams; the four exercises are concrete; the caveat is appropriately explicit;
   registry metadata is complete; related links resolve to completed books; and the outbound link
   goes to the publisher.

2. The factual and copyright posture remains sound against the chapter brief and evidence already
   recorded in this critique history. The brief supports the conditional account of snap judgment.
   The recorded PMID 2016668 evidence supports the Wilson and Schooler jam and course claim, and
   the recorded PMID 12374446 evidence supports variation in thin-slice accuracy and the
   induced-sadness qualification. This round began no new external web search. The prose and
   diagrams remain original, with no quotation, close paraphrase, reproduced source figure, or real
   cover art identified.

3. `npm run check` passed on 2026-07-16: queue, registry, critique, and content validation; prose
   lint; both pipeline tests; all 106 Vitest tests; TypeScript and the Vite production build; and
   ESLint. Vitest emitted only the existing non-failing jsdom `Window.scrollTo()` notices.
