verdict: approve

## Critique round 1 — 2026-07-16

### Required

1. **Compress "The thesis" to the required one or two sentences.** The section currently contains four sentences, while `docs/authoring-spec.md` defines this paragraph as the one- or two-sentence compression a reader can carry away. Preserve the brief's core chain of reading, regular writing, and unsparing revision, but make the section conform to the fixed anatomy.

2. **Make Figure 45.3's labels non-overlapping.** `Spectrum` renders both pole labels at `y=74` and the marker label at `y=78`. With the marker at `x=262`, "a modest daily target" occupies the same horizontal region as the right-anchored "keep a writing appointment," so the two labels collide at every scale, including inside the chapter's 440 px minimum-width SVG. Adjust the chapter-local labels or composition so the routine continuum remains readable on a phone without changing the shared component.

3. **Replace the outbound book URL with a direct publisher or bookseller page.** The current `buyUrl` points to `stephenking.com`, an author site. The authoring spec and chapter brief require the footer link itself to target a publisher or bookseller.

### Advisory

None. The brief supports the central craft claims, no separate recorded evidence artifact exists for this chapter, and the prose presents the ideas in original wording without reproducing a book figure. The six key ideas have distinct, captioned vocabulary diagrams; the absent Model section agrees with the brief and registry; the practices and caveat are concrete; related slugs resolve to completed chapters; and the generated cover/metadata path is intact. A direct server render contains approximately 1,294 visible words, which supports `minutes={7}` at 200 words per minute rounded up. `npm run check` passed on 2026-07-16, including validation, prose lint, pipeline tests, 94 Vitest tests, TypeScript, the production build, and ESLint; Vitest emitted only the existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-16

1. Compressed **The thesis** to two sentences. It now retains the recorded chain of attentive reading, regular writing, and revision for the reader, while framing the craft as repeated return to the desk.

2. Reworked Figure 45.3's chapter-local labels within the unchanged `Spectrum` component. The pole labels are now `mood` and `routine`, with the marker labeled `target`; each occupies a separate horizontal region, while the zones and caption retain the diagram's fuller routine-versus-inspiration meaning.

3. Replaced the author-site outbound URL with Simon & Schuster's direct *On Writing* book page.

## Critique round 2 — 2026-07-16

### Required

None. The three round 1 findings are resolved: The thesis is now two sentences, the
Spectrum pole and marker labels occupy separate regions, and the outbound link targets
the publisher. The brief and registry support the central reading, regular-writing, and
revision thesis, the deliberate absence of a signature Model, and the six-diagram
structure. No chapter-specific evidence artifact exists beyond the brief, and this pass
did not initiate external research. The remaining craft claims are presented as King's
working preferences or as practical synthesis, not as unsupported empirical claims.

The required anatomy is complete and ordered; all six key ideas have distinct,
captioned diagrams from the shared vocabulary; the exercises are concrete; the caveat
appropriately limits the method; related slugs resolve to completed chapters; and the
publisher link, generated-cover path, metadata, and imports are intact. `npm run check`
passed on 2026-07-16, including validation, prose lint, pipeline tests, 94 Vitest tests,
TypeScript, the production build, and ESLint. Vitest emitted only the existing
non-failing jsdom `Window.scrollTo()` notices.

### Advisory

None.
