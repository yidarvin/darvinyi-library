# Zero to One

- **Author:** Peter Thiel
- **Year:** 2014
- **Shelf:** Leadership & Business
- **Tier:** 1
- **Slug / route:** `zero-to-one`  ->  `/zero-to-one`

## Thesis to convey

Real progress comes from building something genuinely new rather than copying what works, and monopolies, not competition, fund it.

## Signature model

**0 to 1 vs. 1 to n.** Render this as the hero diagram in the Model section, in house style, as an original recreation of the idea (never a trace of the book's own figure).

## Build brief

Distill this book into one long scroll following the fixed anatomy in
`docs/authoring-spec.md`: Hero, Thesis, Key Ideas (4 to 7, each with
its own diagram), The Model (hero diagram of the framework), Put It To Work, If You Remember One
Thing, Shelved Nearby.

Diagrams are the point. Give every key idea a diagram drawn from
`docs/diagram-vocabulary.md`, in house style, as an inline-SVG React component
under `src/components/diagrams/` (compose the primitives the scaffold built; add a
new primitive to the vocabulary first if a concept truly needs one). Vary the forms
across the page. Wrap each diagram in the existing `<Figure>` component with a
one-line caption. "Put It To Work" suits `<ExerciseCard>`.

Copyright line: distill ideas, never reproduce text or the author's figures. No
close paraphrase. At most one short attributed epigraph, and only if it earns its
place. No real cover art; the scaffold's generated typographic cover is used.

"Shelved Nearby": link only to books already built (status done in the registry),
noting the relationship in a clause. Link out to the real book at a bookseller.

## Where People Get It Wrong (optional)

Include an honest caveats-and-misreadings section if the book has well-known ones; otherwise omit it.

## Done when

Every spine section present and in order; 4 to 7 key ideas each with an in-vocabulary
diagram; the signature model rendered as the hero Model diagram (or Model section
deliberately absent, noted in the registry); house voice with no em dashes and no AI
tells; diagrams legible at 360px and captioned; cross-links resolve; `npm run check`
passes; then flip `zero-to-one` to done in the registry and DONE in the queue.
