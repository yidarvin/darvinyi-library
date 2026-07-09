# The Body Keeps the Score

- **Author:** Bessel van der Kolk
- **Year:** 2014
- **Shelf:** Meaning, Psychology & the Mind
- **Tier:** 1
- **Slug / route:** `body-keeps-the-score`  ->  `/body-keeps-the-score`

## Thesis to convey

Trauma lives in the body and rewires the brain, so healing has to reach past talk into the nervous system.

## Signature model

This book has no single signature framework. Skip the Model section rather than inventing one, and let the Key Ideas diagrams carry the visual load.

## Build brief

Distill this book into one long scroll following the fixed anatomy in
`docs/authoring-spec.md`: Hero, Thesis, Key Ideas (4 to 7, each with
its own diagram), Put It To Work, If You Remember One
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
passes; then flip `body-keeps-the-score` to done in the registry and DONE in the queue.
