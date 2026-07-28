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
