verdict: approve

## Critique round 1 — 2026-07-15

### Required

1. **Make Figure 15.3's examples agree with its axes.** The shared `Matrix` reads its
   quadrants as top-left, top-right, bottom-left, bottom-right. With the chapter's
   vertical axis running from `fragile measure` at the bottom to `durable measure`
   at the top, `chosen conduct` is currently placed and highlighted in the
   bottom-right fragile quadrant even though the prose and caption present it as
   the durable, within-your-control target. `approval` is likewise placed in the
   top-left durable quadrant, contrary to the prose's description of approval as a
   fragile outside score. Recompose the chapter-local examples and highlight so
   every label occupies the quadrant its two axis values describe, or use a simpler
   vocabulary form if the examples do not support a genuine two-axis taxonomy.

2. **Separate Figure 15.5's marker caption from its right pole label.** The shared
   `Spectrum` puts pole labels at y=74 and the marker caption at y=78. At
   `marker={0.69}`, the centered `room to revise` label occupies the same region as
   the right-aligned `test the belief` label, so the two strings collide inside the
   SVG. The chapter's 440 px minimum width preserves that authored geometry, which
   means scrolling or scaling cannot repair it. Move the chapter-local marker or
   shorten/recompose the labels so both remain independently readable without
   changing the shared component.

3. **Complete the `subtle-art` registry record required by the content contract.**
   The draft record has the display title, author/year subtitle, shelf, routes, and
   status, but omits `tier`, `thesis`, `framework`, and the diagram-form inventory.
   Add the brief-supported tier 1 and thesis, record that there is no single
   signature framework and therefore no Model section, and inventory the five forms
   used by the key ideas. This is also the required registry explanation for the
   deliberate absence of a Model section.

4. **Recompute the Hero reading-time badge from rendered words.** The draft sets
   `minutes={9}`, but the entire 1,543-word MDX source already includes non-rendered
   imports, component names, prop syntax, and class names. The visible page is
   therefore below the 1,601 words needed to round up to nine minutes at the
   specified 200 words per minute. Count the final rendered text and set the badge
   to the resulting rounded-up value.

### Advisory

1. Within the repository's bounded evidence, the factual and copyright posture is
   sound. The chapter brief and seed metadata support selective caring, acceptance
   of struggle, and release from constant positive feeling as the central thesis,
   with no signature model. The draft develops those ideas in an original thematic
   order and original prose, uses shared diagram forms rather than reproducing a
   source figure, contains no quotation or real cover art, and carefully separates
   responsibility for a response from blame for a cause. The repository contains
   no chapter-specific source excerpts or separate evidence dossier for closer
   attribution or close-paraphrase comparison. This review began no external web
   search.

2. Apart from the required findings, the anatomy and teaching progression are
   strong. Five key ideas each receive a captioned structural diagram; omitting the
   Model section follows the brief; the four exercises prescribe observable actions;
   the caveat keeps personal agency in proportion to trauma, illness, discrimination,
   and institutional constraints; and the final takeaway is concise.

3. The three related slugs resolve to done chapters, and the prose states a useful
   one-clause relationship for each before the cover links. The outbound Apple Books
   URL is a direct bookseller link. The chapter-local minimum widths also work with
   `Figure`'s horizontal-overflow wrapper to preserve diagram type size on a phone;
   the required Figure 15.5 problem is an internal label collision, not a scaling
   problem.

4. `npm run check` passed on 2026-07-15: queue/registry/content validation, prose
   lint, both pipeline tests, all 34 Vitest tests, TypeScript and Vite production
   build, and ESLint completed successfully. The jsdom run emitted only its existing
   non-failing `Window.scrollTo()` notices.

## Builder resolution — 2026-07-15

1. Reassigned Figure 15.3 in the shared matrix's documented reading order. Durable,
   outside-control `shared result` is top-left; durable, within-control `chosen
   conduct` is top-right and highlighted; fragile, outside-control `approval` is
   bottom-left; and fragile, within-control `short-term comfort` is bottom-right.
   The figure now agrees with both axes and the surrounding prose.

2. Moved Figure 15.5's marker to 0.55 and shortened its caption to `revise`.
   Its centered label now occupies the open space between `protect the identity` and
   `test the belief`, so it does not overlap either pole label at the authored width.

3. Completed the `subtle-art` registry record with tier 1, the brief-supported
   thesis, an explicit no-signature-framework explanation for omitting the Model
   section, and the five key-idea diagram forms: comparison, process loop,
   two-by-two matrix, flow with branch, and spectrum.

4. Rendered the completed MDX with its normal providers and counted 1,410 visible
   words. At 200 words per minute rounded up, the Hero badge is now 8 minutes.

5. Ran `npm run check` after these changes.

## Critique round 2 — 2026-07-15

### Required

None.

### Advisory

1. The four round 1 findings are resolved in the rendered inputs. Figure 15.3 now
   places and highlights `chosen conduct` in the durable, within-control quadrant;
   Figure 15.5's shortened `revise` marker is clear of both pole labels; the registry
   records the brief-supported tier, thesis, absent signature framework, and five
   diagram forms; and the 8-minute Hero badge agrees with the recorded 1,410 visible
   words at 200 words per minute, rounded up.

2. The chapter remains faithful to the bounded evidence available in the repository.
   Its thesis matches the chapter brief and seed metadata, its five ideas develop that
   thesis in original prose and a thematic order, and its diagrams instantiate shared
   vocabulary forms rather than reproducing an author figure. There is no quotation or
   real cover art. No new external web search was begun for this review.

3. The anatomy and teaching function meet the contract: five key ideas each have a
   captioned structural diagram, the Model section is deliberately absent as directed
   by the brief, all four exercises specify observable actions, the caveat distinguishes
   agency from blame under material and institutional constraints, and all three nearby
   slugs resolve to done chapters before the direct bookseller link.

4. `npm run check` passed on 2026-07-15. Validation, prose lint, both pipeline tests,
   all 34 Vitest tests, TypeScript, the Vite production build, and ESLint succeeded.
   The Vitest run emitted only the existing non-failing jsdom `Window.scrollTo()`
   notices.
