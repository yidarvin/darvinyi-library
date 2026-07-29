verdict: resolved

## Critique round 1 — 2026-07-28

### Required

1. **Compress “The thesis” to the required one or two sentences.** The section at
   `src/chapters/omnivores-dilemma.mdx:13-17` contains five sentences. The fixed
   anatomy defines this paragraph as the one- or two-sentence compression a reader
   could carry away. Preserve the useful chain-of-relationships idea, but make the
   section satisfy that contract.

2. **Restore the book's organizing comparison of food chains.** The recorded source
   account at `content/evidence/omnivores-dilemma.md:8` identifies the inquiry across
   industrial, organic or alternative, and self-provisioned food chains. The draft
   gives industrial corn and organic certification their own ideas, but never explains
   the self-provisioned chain or shows how following contrasting meals lets Pollan test
   different relationships among eater, land, animal, and labor
   (`src/chapters/omnivores-dilemma.mdx:27-130`). The brief deliberately rejects a
   separate signature Model, so the Key Ideas must carry this central comparative
   structure. As written, the page reads as a general provenance essay and leaves a
   reader without the architecture of this particular book.

3. **Correct Figure 145.2's false linear path.** The prose and recorded USDA evidence
   distinguish livestock feed, ethanol, and food ingredients as different uses of
   corn (`src/chapters/omnivores-dilemma.mdx:49-54`;
   `content/evidence/omnivores-dilemma.md:9`). The `Flow` at
   `src/chapters/omnivores-dilemma.mdx:56-62` instead places “feed, fuel, or
   ingredients” in one stage followed by “food choice,” and its caption says all
   three channels precede a meal. That teaches that fuel ethanol flows into the food
   choice rather than ending in a competing nonfood use. Use a branching or network
   form that separates the routes and connects only the food routes to a meal.

4. **Bound the distance-and-externalized-cost claim to the recorded evidence, and make
   its diagram teach the resulting idea.** The evidence at
   `content/evidence/omnivores-dilemma.md:12` supports the narrower point that checkout
   price does not describe every condition or cost in a supply chain. It does not
   establish the draft's causal generalization that distance is the weakness of
   industrial chains or that greater distance makes soil loss, animal conditions,
   worker safety, energy use, and waste easier to push onto others
   (`src/chapters/omnivores-dilemma.mdx:64-71`). The caveat later correctly says a
   distant producer can follow strong standards. Reframe this idea around opacity or
   unpriced and unreported conditions unless the stronger distance claim is supported.
   Then revise Figure 145.3, which currently compares visible and omitted information
   but does not encode the heading's stated concentration of costs.

5. **Replace the outbound footer URL with a publisher or bookseller destination.**
   The evidence itself describes `https://michaelpollan.com/books/the-omnivores-dilemma/`
   as the author's official book page (`content/evidence/omnivores-dilemma.md:8`), not
   a seller. The chapter nevertheless labels that URL “Buy The Omnivore's Dilemma
   from Michael Pollan” at `src/chapters/omnivores-dilemma.mdx:182-185`. This does not
   satisfy the definition of done requiring a link to a real bookseller
   (`docs/authoring-spec.md:83`) and makes the link text promise a transaction the
   destination is not recorded to provide.

### Advisory

None. The remaining bounded review found no additional defect worth requesting as
stylistic churn. The Hero badge is plausible for the rendered length; the deliberate
absence of a Model section matches the brief and registry; five key ideas have
captioned shared-vocabulary diagrams with phone-safe overflow sizing; the four
exercises are concrete; and all three related slugs are done. No apparent close
paraphrase, reproduced source figure, quotation, or real cover art was found. No new
external web search was begun.

`npm run check` completed with `CHECK OK` on 2026-07-28: queue, registry, content,
critique-state, and prose validation passed; all 42 pipeline and runner tests and all
312 Vitest tests passed; TypeScript, the Vite production build, and ESLint passed.
Vitest emitted only the existing non-failing jsdom `Window.scrollTo()` notices.

## Builder resolution — 2026-07-28

- Compressed “The thesis” to two sentences, retaining the chain-of-relationships argument.
- Recentered the first key idea on the book's comparison of industrial, organic or alternative, and self-provisioned meals, including the distinct relationships those routes reveal.
- Replaced Figure 145.2's false linear `Flow` with a node graph: feed and ingredient paths converge on a meal, while fuel ethanol ends as a competing nonfood use.
- Reframed the price claim around what checkout price cannot report, rather than distance or a general claim of externalized costs. Figure 145.3 now contrasts the completed purchase with supply-chain questions beyond price.
- Replaced the author-site footer with Penguin Random House's product page and recorded that publisher purchase destination in the evidence file.
