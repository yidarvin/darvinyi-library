verdict: revise

## Critique round 1 — 2026-07-25

### REQUIRED

1. **Compress “The thesis” to the required one or two sentences.** The section is
   currently five sentences (`src/chapters/four-agreements.mdx:14-22`), while the
   fixed anatomy defines it as a one- or two-sentence compression
   (`docs/authoring-spec.md:37-40`). Preserve the brief-supported chain from speech,
   personalization, assumptions, and variable daily effort to avoidable suffering,
   but make this section perform the single-takeaway job assigned to it.

2. **Make Figure 78.2 preserve the distinction between another person's context
   and a usable signal.** The prose treats those as alternatives to sort: a comment
   can contain a specific detail worth using, while its contempt or style belongs
   to the speaker (`src/chapters/four-agreements.mdx:56-67`). The `Iceberg`
   primitive defines every `below` item as an underlying driver of the visible tip
   (`src/components/diagrams/Iceberg.tsx:4-16,52-60`), but the chapter places “a
   possible signal for you” below the water beside the speaker's pressure and
   interpretation (`src/chapters/four-agreements.mdx:69-75`). A signal available
   to the recipient is not an underlying cause of the speaker's behavior, so the
   visual collapses the distinction the section teaches. Use an in-vocabulary form
   or chapter-local labeling that visibly separates potentially actionable content
   from the other person's context.

3. **Give the fourth agreement a diagram that encodes its moving standard.** The
   heading, prose, and caption say that today's honest best changes with present
   capacity (`src/chapters/four-agreements.mdx:106-119`). Figure 78.4 instead fixes
   one marker between the poles “self-excusing” and “self-punishing”
   (`src/chapters/four-agreements.mdx:120-131`). That spectrum shows a stance toward
   review, but it does not show capacity changing or effort being matched to
   different conditions, so the key idea's structural relationship remains
   undiagrammed. Recompose the figure within the shared vocabulary so the visible
   structure teaches variable capacity rather than only the secondary warning
   against excuse and punishment.

4. **Remove the unsupported reinforcing-system signs from the signature Model, or
   show and explain an actual reinforcing loop.** Figure 78.5 marks all four
   one-way agreement-to-response edges as `reinforcing`
   (`src/chapters/four-agreements.mdx:144-159`). The shared `NodeGraph` reserves
   that kind for accented positive causal signs and draws a “+” on every such edge
   (`src/components/diagrams/NodeGraph.tsx:13-17,92-118`), while its documented use
   is a system map whose parts feed back on one another
   (`src/components/diagrams/NodeGraph.tsx:29-32`). The chapter describes four peer
   checks converging on a chosen response, with no return edge, amplification, or
   signed causal polarity. Neutral directed edges would express that convergence
   without adding four unexplained system claims.

5. **Complete the `four-agreements` registry metadata required by the content
   contract.** The draft entry contains display metadata and status but omits
   `tier`, `thesis`, `framework`, and the diagram inventory
   (`content/registry.json:1543-1551`). Definition-of-done item 7 requires those
   fields even though the validator permits an incomplete scaffold record while it
   remains a draft (`docs/authoring-spec.md:74-86`). Record the brief-supported
   tier 2, thesis, and four-agreements framework, plus the final rendered figure
   forms in page order after the diagram revisions.

### ADVISORY

1. The four key-idea headings use `##`, making them siblings of the empty
   `## Key ideas` heading rather than children of that section
   (`src/chapters/four-agreements.mdx:33-35,56,78,106`). Using `###` for the four
   idea headings would give the page a coherent semantic outline and use the
   existing key-idea heading style.

### Evidence checked

- Re-derived the central claim from `prompts/notes/four-agreements.md` and the seed
  record in `prompts/_books.py`. Those records support four commitments concerning
  speech, personalization, assumptions, and doing one's best, with the four
  agreements as the signature framework. No separate chapter-specific evidence
  dossier exists, and this review began no external web search.
- Read the chapter and all of its direct component imports, plus the transitive
  cover, SVG helper, registry, diagram-vocabulary, and MDX rendering contracts.
  Apart from the required structural mismatches above, the comparison and flow
  figures are internally consistent, captions are present, minimum SVG widths are
  preserved by the Figure overflow wrapper, and the generated cover uses no real
  cover art.
- The practices are concrete, and the caveat appropriately rejects using the
  agreements to minimize harm, override boundaries, or substitute for safety.
  All three related slugs resolve to completed chapters, their relationships are
  stated in prose, and the outbound link targets the publisher's book page.
- A direct MDX render contains exactly 1,400 reader-visible alphanumeric word
  tokens, including Hero and cover text, headings, captions, diagram labels,
  exercise titles, callout chrome, and the nearby-book footer. That supports the
  existing seven-minute badge at approximately 200 words per minute, rounded up.
- `npm run check` passed on 2026-07-25: queue/registry/content validation, prose
  lint, 2 pipeline tests, 38 runner tests, 161 app tests, TypeScript and the Vite
  production build, and ESLint all completed successfully. Vitest emitted only the
  existing non-failing jsdom `Window.scrollTo()` notices.
