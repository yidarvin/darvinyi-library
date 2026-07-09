# Authoring Spec — darvinyi-library

The quality contract for every book page. The refsite-runner skill owns the *mechanics* (how to run the queue, wire nav, validate, commit). This file owns the *standard*: what a finished distillation is, how it reads, how it looks, and how it stays on the right side of copyright. If this file and the skill ever disagree on mechanics, the skill wins; on voice and anatomy, this file wins.

## What this site is

darvinyi-library is a distillation shelf. Each page takes one work of educational non-fiction and compresses its ideas — not its text — into original prose and original diagrams. The reader should leave understanding the book's core argument, its central framework, and how to use it, without ever having read a sentence of the original. This is a synthesis, not a substitute-by-summary and never a reproduction.

The landing page is a library: shelves of books, browsable by category, each cover a generated typographic treatment in house style.

## The copyright line (non-negotiable)

Ideas are free; expression is not. We distill concepts and lessons. We never reproduce.

- **Everything is written from scratch.** No verbatim quoting beyond the rare, short, attributed epigraph (see below). More importantly, no *close paraphrase*: do not take the author's sentence and swap in synonyms. If you could not explain the idea with the book closed, you have not distilled it yet.
- **Diagrams recreate the concept, never the author's figure.** If the book has a diagram, build an original visual of the underlying idea in our vocabulary and house style. Never reproduce the book's specific layout, labels, or chart.
- **Organize by our own logic**, not the book's chapter order. A thematic distillation reads as synthesis. Mirroring the table of contents reads as a replacement.
- **Epigraphs:** at most one short attributed quote per page (well under 25 words), in quotation marks, with author attribution, and only when it genuinely earns its place. The value of every page must come from our explanation, not from lifted passages. When in doubt, cut it.
- **Never reproduce cover art.** Covers are copyrighted. We use a generated typographic cover.

## Voice

The house voice, consistent with every darvinyi.com property.

- Direct, confident, unhurried. Explaining to a smart peer, not selling to a stranger.
- No hype, no self-help breathlessness, no "life-changing." The ideas carry the weight; the prose stays calm.
- **No em dashes.** Use commas, colons, periods, or restructure. (The prose gate at `prose-lint.config.json` fails the build on them, along with a list of AI tells.)
- **No AI-tell phrasing.** None of "in today's fast-paced world," "it's important to note," "delve," "tapestry," "navigate the complexities," "unlock," "leverage" (as a verb applied to abstractions), "game-changer," or the "it's not just X, it's Y" cadence. If a sentence sounds like it came from a model, rewrite it.
- Second person is fine for the practice sections. Elsewhere prefer the idea as subject.
- American spelling. Oxford comma.
- Prose is prose. In-page explanation runs in real paragraphs, not bullet lists. Bullets are reserved for the practice checklist and the "shelved nearby" links, where they are structurally correct.

## Page anatomy

Every book page is one long scroll, assembled from a fixed spine of sections plus two optional blocks. Sections render in this order. The spine is mandatory; optional blocks appear only when the book warrants them.

1. **Hero.** Title, author, year, category tag, one-line thesis, and an "N-min distillation" badge (compute N from final rendered word count at ~200 wpm, rounded up). Generated typographic cover treatment, teal-on-near-black. No real cover art.
2. **The Thesis.** One or two sentences compressing the entire argument. The single paragraph a reader could carry away if they read nothing else on the page.
3. **Why It Matters** *(optional)*. The problem the book tackles and why it stuck. Include when the book's significance is not self-evident from the thesis. Skip for books whose importance is obvious.
4. **Key Ideas.** The core of the scroll. Four to seven ideas. Each is one heading, prose explanation, and its own diagram from the vocabulary. This is where most of the visuals live. Every key idea gets a diagram unless the idea is genuinely non-visual, in which case note why in the registry and prefer a different idea.
5. **The Model.** One hero diagram of the book's central framework, when it has a signature one (the habit loop, the Golden Circle, System 1/2, the flow channel, BATNA). Books without a single signature model skip this section rather than inventing one.
6. **Put It To Work.** Concrete practices as a checklist or practice cards. What the reader actually does differently on Monday. Grounded and specific, never generic affirmation.
7. **Where People Get It Wrong** *(optional)*. Misreadings, caveats, honest criticism. This is what separates a real distillation from a shallow summary and reinforces that we are synthesizing, not selling. **Mandatory** for any title flagged in the queue with a credibility caveat (see the flagged-titles list): render a brief, sourced "what to question" note.
8. **If You Remember One Thing.** The single takeaway, one or two sentences.
9. **Shelved Nearby.** Cross-links to related books in the library plus a link out to the real book (publisher or a bookseller, so a reader who wants the original goes and buys it). The library becomes a light web, not a flat list, the same citation-graph instinct as litsearch.

## Section components

Book pages are MDX under `src/chapters/<slug>.mdx` (a book occupies one "chapter"
slot). Reuse the template's existing components rather than inventing markup: wrap
every diagram in `<Figure>` with a one-line caption, render "Put It To Work" as
`<ExerciseCard>` items, and render the "Where People Get It Wrong" note as a
`<Callout>`. The scaffold step adds a small set of book-specific section components
under `src/components/book/` (at least a `Hero` that renders the generated
typographic cover, and a `ShelvedNearby` for the cross-link footer). Use those for
the Hero and Shelved Nearby sections; the remaining sections are plain MDX headings
and prose. Diagram primitives live under `src/components/diagrams/`.

## Diagrams

Diagrams are the point of this site, not decoration. Every page should be visually dense. See `diagram-vocabulary.md` for the fixed set of forms and when to use each. Rules that hold across all of them:

- **Inline SVG, hand-authored. No diagramming library, no chart library, no D3.** A diagram is a React component returning SVG.
- House style: near-black background `#0a0e0f`, teal accent `#2dd4bf`, structural labels in JetBrains Mono, any prose labels in Inter. Muted grays for secondary strokes. One accent, used with restraint.
- Every diagram matches a named form in the vocabulary. Do not improvise a new form per book; pick the form that fits the concept. If a concept truly needs a form the vocabulary lacks, add it to the vocabulary first (with a component), then use it.
- Diagrams are original recreations of *ideas*, never traced from the book's own figures.
- Legible at mobile width. Test at 360px. SVG scales; layout and label sizing must not break.
- Each diagram is self-contained and captioned. The caption is one line, in our voice, stating what the diagram shows.

## Cross-linking

"Shelved Nearby" links are the graph edges. When building a page, link to books already in the registry that share a shelf or a concept, and note the relationship in one clause ("also on anchoring," "the productivity counterpart," "argues the opposite"). Do not link to books not yet built; the skill's validator flags dangling links. As the shelf grows, earlier pages can be revisited to add edges, but never block a build on a link that does not exist yet.

## Definition of done

A book page is done when:

1. Every spine section is present and in order; optional blocks are present iff warranted (and "Where People Get It Wrong" is present for any flagged title).
2. Four to seven key ideas, each with its own in-vocabulary diagram in house style.
3. The Model section renders the signature framework as a hero diagram, or is deliberately absent with reason noted.
4. Prose is in house voice: no em dashes, no AI-tell phrasing, no close paraphrase of the source, at most one short attributed epigraph.
5. All diagrams are legible at 360px and captioned.
6. Cross-links resolve to built pages; the book links out to a real bookseller.
7. The registry entry is complete (see queue-schema in the skill): id, shelf, tier, title, author, year, thesis, framework, diagram list, status.
8. `npm run check` passes (validate.py for queue/registry agreement, prose_lint.py for the em-dash and AI-tell gate, typecheck, and build).
9. The generated cover renders and no real cover art is used anywhere.

Only when all nine hold does the item flip to DONE and the run stop.
