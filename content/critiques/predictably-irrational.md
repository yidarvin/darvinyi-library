verdict: approve

## Critique round 1 — 2026-07-15

### Required

1. **Make Figure 16.1 agree with its axes and actually encode domination.** The
   shared `Matrix` reads its quadrants as top-left, top-right, bottom-left, and
   bottom-right, while this chapter defines the top as more features, the bottom
   as fewer features, the left as lower price, and the right as higher price.
   `basic` is therefore placed in the more-features quadrant despite being labeled
   `limited`; `weak decoy` is placed in the lower-price quadrant despite being
   labeled `at a high price`; and the highlighted `target` occupies the
   fewer-features, higher-price quadrant. The resulting visual contradicts its
   labels and never shows one option being dominated by the target described in
   the prose and caption. Recompose the chapter-local options so every label
   occupies its stated coordinates and the target dominates the decoy on the
   relevant dimensions, or use a simpler vocabulary form that can express the
   comparison faithfully.

2. **Complete the `predictably-irrational` registry record required by the content
   contract.** The draft entry has the display metadata and status, but omits
   `tier`, `thesis`, `framework`, and the diagram-form inventory. Add the
   brief-supported tier 1 and thesis, explicitly record that the book has no single
   signature framework and the Model section is deliberately omitted, and inventory
   the six forms used by the key ideas: two-by-two matrix, spectrum, comparison,
   flow, timeline, and iceberg.

3. **Make the study-level caveat inspectable within the recorded evidence.** The
   repository contains no chapter-specific evidence dossier or source record for
   the statement that the anchoring account comes from a six-experiment study by
   Ariely, Loewenstein, and Prelec or for the contrast with a separate
   price-placebo study. The brief and seed metadata support only the high-level
   thesis and the absence of a signature model. Because the caveat uses those exact
   study details to characterize the strength and scope of the evidence, either
   record the sources used so the claims can be re-derived in review or remove the
   precise attribution and keep the caution at the level supported by the bounded
   record.

### Advisory

1. Within the repository's bounded evidence, the central framing and copyright
   posture are otherwise sound. The brief and seed metadata support the thesis that
   irrational choices follow predictable patterns and direct the page to omit a
   signature Model. The draft develops that thesis in original prose and thematic
   order, uses shared diagram forms rather than reproducing an author figure,
   contains no quotation, and uses the generated typographic cover. The repository
   has no source excerpts or separate evidence dossier for closer attribution or
   close-paraphrase comparison. This review began no external web search.

2. Apart from the required Figure 16.1, registry, and evidence-record findings, the
   anatomy and teaching progression are strong. Six key ideas each receive a
   captioned structural diagram; omitting the Model section follows the brief; the
   four exercises prescribe observable actions; the caveat avoids turning bounded
   experiments into universal claims; and the final takeaway is concise. Both
   nearby slugs resolve to done chapters, their relationships are stated in prose,
   and the outbound Barnes & Noble URL is a direct bookseller link.

3. The chapter-local minimum widths work with `Figure`'s horizontal-overflow
   wrapper to preserve authored SVG type sizes on a phone. A provider-backed static
   render contains 1,509 visible words, which rounds up to the displayed 8-minute
   badge at 200 words per minute.

4. `npm run check` passed on 2026-07-15: queue/registry/content validation, prose
   lint, both pipeline tests, all 36 Vitest tests, TypeScript and Vite production
   build, and ESLint completed successfully. The Vitest run emitted only the
   existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-15

1. Reassigned Figure 16.1 in the shared matrix's documented reading order. The
   top-left quadrant now explicitly says no lower-price, higher-feature option is
   offered; `target` is top-right at more features and a higher price; `basic` is
   bottom-left at fewer features and a lower price; and `weak decoy` is bottom-right
   at fewer features and the same higher price as the target. The target is
   highlighted and visibly dominates the decoy on features at that price. The
   caption now describes exactly that comparison.

2. Completed only the `predictably-irrational` registry record with tier 1, the
   brief-supported thesis, an explicit no-signature-framework explanation for the
   deliberately omitted Model section, and the six key-idea forms: two-by-two
   matrix, spectrum, comparison, flow, timeline, and iceberg. Its status remains
   `draft`.

3. Removed the unsupported precise study attribution and study-count contrast from
   the caveat. It now keeps the bounded, locally supported caution that individual
   laboratory effects should be examined for effect size and generalizability rather
   than treated as one universal result.

4. Ran `npm run check` after these changes.

## Critique round 2 — 2026-07-15

### Required

None.

### Advisory

1. The three round 1 findings are resolved. Figure 16.1 now follows the shared
   `Matrix` reading order and shows the target dominating the weak decoy at the
   same high price. The registry records the brief-supported tier, thesis, omitted
   signature Model, and all six diagram forms. The caveat no longer makes the
   unsupported study-level attribution that could not be re-derived from the
   repository's bounded evidence.

2. The remaining draft satisfies the anatomy and teaching contract: six thematic
   key ideas each have a captioned vocabulary diagram, the concrete exercises
   translate four mechanisms into observable procedures, the caveat keeps the
   experimental claims appropriately bounded, and the nearby links resolve to done
   chapters. The prose and diagrams remain original in structure and expression as
   far as the recorded evidence permits review. No new external web search was
   started for this pass.

3. `npm run check` passed on 2026-07-15: queue, registry, critique, and chapter
   validation; prose lint; both pipeline tests; all 36 Vitest tests; TypeScript and
   Vite production build; and ESLint. The Vitest run emitted only the existing
   non-failing jsdom `Window.scrollTo()` notices.
