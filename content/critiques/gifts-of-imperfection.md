verdict: revise

## Critique round 1 — 2026-07-27

### Required

1. **Do not model courage, compassion, and connection as constituents of inherent
   worth in Figure 124.1.** The prose at
   `src/chapters/gifts-of-imperfection.mdx:33-40` distinguishes stable worthiness
   from variable performance measures. The figure instead places `courage`,
   `compassion`, and `connection` inside a core titled `inherent worth`, and the
   shared primitive's generated accessibility text explicitly says that inherent
   worth “contains” those elements. The brief and recorded evidence support those
   three as practices or qualities of wholehearted living, not as ingredients a
   person must possess for worth to remain inherent. This changes the model at the
   exact point where the chapter argues that worth is not earned. Recompose the
   figure so stable worth is not visually or accessibly conditional on three
   practice capacities, and make its labels encode the prose's actual
   stable-worth/changeable-performance distinction.

2. **Correct the reversed visual emphasis in Figure 124.3.** At
   `src/chapters/gifts-of-imperfection.mdx:79-92`, the comparison passes
   `favor="right"` while the right panel is `perfectionism`. The shared
   `Compare` component defines `favor` as the panel favored with the accent, so the
   figure highlights the defensive pattern the prose warns against and leaves
   careful striving muted. The structural cue therefore contradicts the teaching.
   Favor the careful-striving panel, or remove the favored-panel cue if neither
   side should be presented as the target.

3. **Make Figure 124.4 show the gratitude interruption its caption says it
   shows.** The paragraph and caption at
   `src/chapters/gifts-of-imperfection.mdx:94-103` teach that gratitude redirects
   attention from scarcity toward what is present. The `ProcessLoop` at lines
   104-109 renders only the four-stage scarcity cycle and accents its reinforcing
   return edge. Nothing in the SVG represents gratitude or a return to the present.
   This leaves the key idea's practical causal move out of its structural diagram
   and makes the caption false as a description of the rendered figure. Encode a
   visible interruption from the scarcity loop into gratitude/present attention,
   using the vocabulary primitive's supported interruption where appropriate.

4. **Recompute the Hero reading-time badge from the rendered page.** A direct
   render of this exact MDX through its imported components contains 1,326
   reader-visible words before the small outer page header and navigation are
   added. Those additions do not take the page above 1,400 words. At the authoring
   spec's approximately 200 words per minute, rounded up, this is a seven-minute
   distillation, not `minutes={8}` at
   `src/chapters/gifts-of-imperfection.mdx:9-13`.

### Advisory

None.

The brief and recorded evidence support the chapter's treatment of worthiness,
shame and connection, perfectionism, gratitude and joy, creativity, and rest and
play. The caveat properly limits the reflective practices and does not turn them
into clinical treatment or an answer to material and structural hardship. The
draft uses original prose and vocabulary-based conceptual diagrams, reproduces no
source figure or cover art, deliberately omits a Model section as the brief
requires, and links to three completed related chapters and a bookseller. This
review began no new external web search.

`npm run check` completed with `CHECK OK` on 2026-07-27. Repository validation,
prose lint, all 40 pipeline and runner tests, all 264 Vitest tests, TypeScript, the
Vite production build, and ESLint passed. Vitest emitted only the existing
non-failing jsdom `Window.scrollTo()` notices.
