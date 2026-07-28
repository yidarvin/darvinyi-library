verdict: revise

## Critique round 1 — 2026-07-27

### Required

1. **Teach the relationship foundation that the page promises.** The recorded Wharton
   outline identifies relationships alongside styles, goals, standards, interests, and
   leverage as part of Shell's approach
   (`content/evidence/bargaining-for-advantage.md:7-9`). The registry thesis likewise
   names relationships, and both the Hero and thesis present a workable relationship as
   one of the sources of negotiating strength
   (`content/registry.json:2419`; `src/chapters/bargaining-for-advantage.mdx:5-17`).
   The five key ideas then cover style, goals and alternatives, interests, standards,
   and leverage, but never explain what a negotiating relationship contributes or how
   to prepare for it. None of the four practice cards repairs that omission. This leaves
   a named part of the preparation framework as an unsupported promise rather than a
   distilled idea. Add a substantive treatment of relationships with its own structural
   diagram and a concrete practice, or revise the thesis and registry only if the
   recorded evidence supports excluding relationships from the framework.

### Advisory

1. Figure 122.2 calls itself a decision rule, but its terminal branches say only
   `better` and `worse` without naming the comparison baseline
   (`src/chapters/bargaining-for-advantage.mdx:59-65`). The prose distinguishes a
   target, a minimum, and an alternative, so the figure should say whether the offer
   is being compared with the prepared minimum, the alternative, or both. Naming that
   threshold would make the central choice auditable rather than implied.

2. Figure 122.5 marks only `authority to act → credible boundary` as a `reinforcing`
   edge (`src/chapters/bargaining-for-advantage.mdx:122-137`). In the shared
   `NodeGraph`, that kind denotes reinforcing feedback and receives the accent
   treatment (`src/components/diagrams/NodeGraph.tsx:17-23,92-126`), but this graph
   contains no return path or amplification loop. Use a plain edge unless a real
   feedback relationship is shown; otherwise the visual grammar arbitrarily privileges
   authority over options, information, and time.

The remaining bounded review checks are sound. The brief supports omitting a separate
Model section, and the draft otherwise follows the fixed anatomy with five captioned
shared-vocabulary figures, concrete exercises, a useful power-and-safety caveat,
original prose, a generated cover, three related links to done chapters, and a direct
publisher purchase link. The imported components render, preserve the authored diagram
widths through horizontal overflow on a phone, and agree with the registry inventory.
This review used only the chapter brief and recorded evidence and began no new external
web search.

`npm run check` passed on 2026-07-27: queue, registry, critique, and content validation;
prose lint; 40 runqueue tests; 260 Vitest tests; TypeScript and Vite production build;
and ESLint all passed. Vitest emitted only the existing non-failing jsdom
`Window.scrollTo()` notices.

## Builder resolution — 2026-07-27

Resolved the required relationship gap without changing the source-backed framework. The
chapter now has a sixth key idea, “Treat the relationship as working infrastructure,” explaining
what a workable negotiating relationship contributes and how to prepare for its history,
communication conditions, and repair. It includes a captioned `Venn` diagram of candid exchange,
reliable commitments, and repair after strain, plus a new concrete relationship-preparation
practice card. The registry now records six preparation-focused diagrams and includes `venn`.

Also applied both advisory diagram corrections: Figure 122.2 now states that the offer is
compared with the prepared minimum before choosing to negotiate or use the alternative, and
Figure 122.6 uses a plain authority edge rather than a feedback-only reinforcing edge. The
chapter remains `draft`; no queue status was changed.

## Critique round 2 — 2026-07-27

### Required

1. **Make the central style premise usable, and give it a diagram that encodes the
   idea.** The brief makes knowing one's own style half of the thesis
   (`prompts/notes/bargaining-for-advantage.md:10-12`), and the recorded publisher
   evidence specifically identifies a diagnostic for individual strengths and
   weaknesses (`content/evidence/bargaining-for-advantage.md:6-8`). The draft instead
   lists loose tendencies, contrasts only cooperative and competitive behavior, and
   tells the reader to notice a default without supplying a way to identify it,
   inspect its strengths and risks, or prepare the promised counterweight
   (`src/chapters/bargaining-for-advantage.mdx:25-36`). None of the five exercises
   returns to style. Figure 122.1 also treats default response, situational demand, and
   prepared adjustment as nested rings, although the shared Concentric form denotes a
   core and surrounding layers, not a conditional adjustment
   (`docs/diagram-vocabulary.md:34-38`;
   `src/components/diagrams/Concentric.tsx:16-20`). A reader therefore cannot apply
   the premise that frames the Hero, thesis, and first key idea. Add a source-grounded
   diagnostic or decision aid, a concrete practice for using it, and an
   in-vocabulary visual whose structure matches the relationship among default,
   situation, and adjustment.

2. **Correct the reading-time badge.** The Hero reports a 9-minute distillation
   (`src/chapters/bargaining-for-advantage.mdx:5-9`), but the authoring spec requires
   the badge to be computed from final rendered words at about 200 words per minute,
   rounded up (`docs/authoring-spec.md:35-38`). The MDX contains 1,252 words in
   rendered text nodes. Counting the displayed Hero thesis, captions, exercise
   titles, diagram labels, outbound label, and a generous allowance for
   registry-derived cover and related-card text still produces fewer than 1,600
   visible words, which rounds to 8 minutes, not 9. Recompute the badge from rendered
   content rather than source-code tokens.

### Advisory

1. Figure 122.5 uses a Venn diagram for three qualities rather than three sets with a
   meaningful overlap (`src/chapters/bargaining-for-advantage.mdx:116-125`). The
   caption's claim that a workable relationship “combines” candor, reliability, and
   repair is clear in prose, but a combination alone does not establish the set
   intersection that the shared Venn vocabulary is designed to show
   (`docs/diagram-vocabulary.md:66-69`). A form that presents peer elements as parts
   of one working system would be more precise.

The round-1 relationship requirement and both round-1 advisories are resolved. The
remaining anatomy, caveat, cross-links, purchase link, registry inventory, and
imported-component wiring are sound. This review used only the chapter brief and
recorded evidence and began no external web search.

`npm run check` passed on 2026-07-27 before this critique was appended: queue,
registry, critique, and content validation; prose lint; 40 runqueue tests; 260
Vitest tests; TypeScript and Vite production build; and ESLint all passed. Vitest
emitted only the existing non-failing jsdom `Window.scrollTo()` notices.
