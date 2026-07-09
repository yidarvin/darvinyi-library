# Why We Sleep

- **Author:** Matthew Walker
- **Year:** 2017
- **Shelf:** Health & the Body
- **Tier:** 1
- **Slug / route:** `why-we-sleep`  ->  `/why-we-sleep`

## Thesis to convey

Sleep is not optional downtime but the foundation of health, memory, and mood, and modern life is starving us of it.

## Signature model

This book has no single signature framework. Skip the Model section rather than inventing one, and let the Key Ideas diagrams carry the visual load.

## Build brief

Distill this book into one long scroll following the fixed anatomy in
`docs/authoring-spec.md`: Hero, Thesis, Why It Matters, Key Ideas (4 to 7, each with
its own diagram), Put It To Work, Where People Get It Wrong, If You Remember One
Thing, Shelved Nearby.

Diagrams are the point. Give every key idea a diagram drawn from
`docs/diagram-vocabulary.md`, in house style, as an inline-SVG React component
under `src/components/diagrams/` (compose the primitives the scaffold built; add a
new primitive to the vocabulary first if a concept truly needs one). Vary the forms
across the page. Wrap each diagram in the existing `<Figure>` component with a
one-line caption. "Put It To Work" suits `<ExerciseCard>`. The credibility note below belongs in a `<Callout>`.

Copyright line: distill ideas, never reproduce text or the author's figures. No
close paraphrase. At most one short attributed epigraph, and only if it earns its
place. No real cover art; the scaffold's generated typographic cover is used.

"Shelved Nearby": link only to books already built (status done in the registry),
noting the relationship in a clause. Link out to the real book at a bookseller.

## Where People Get It Wrong (mandatory for this title)

Independent reviewers have documented factual errors and at least one likely misleading graph in the book. Present the core message that sleep matters while noting specific claims have been credibly challenged.

Write this as a brief, fair, sourced note in our own words. Name the criticism plainly and let the reader weigh it. Do not bury it.

## Done when

Every spine section present and in order; 4 to 7 key ideas each with an in-vocabulary
diagram; the signature model rendered as the hero Model diagram (or Model section
deliberately absent, noted in the registry); house voice with no em dashes and no AI
tells; diagrams legible at 360px and captioned; cross-links resolve; `npm run check`
passes; then flip `why-we-sleep` to done in the registry and DONE in the queue.
