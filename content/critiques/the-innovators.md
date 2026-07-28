verdict: approve

## Critique round 1 — 2026-07-28

### Required

1. **Separate programmability from stored-program architecture.** Lines 93–97 say that the
   decisive shift was letting a machine “store, change, and execute” instructions, then claim
   that this separation turned a calculator into a general-purpose tool. Those sentences merge
   distinct developments. A machine can be general-purpose and programmable while receiving
   instructions from external media; storing instructions in memory is the later stored-program
   development. The recorded Babbage/Lovelace evidence supports the distinction between a
   machine and its instructions, but not the stored-program claim. This is a material historical
   error in one of the five key ideas. Rewrite the prose and matching comparison labels to
   distinguish changeable instructions from where those instructions are stored, or add
   chapter-recorded evidence that supports a narrower stored-program claim.

2. **Bring the first relay claim back within the recorded evidence.** Lines 33–35 say that
   electronic switching made computation faster and more reliable and that smaller components
   made it “cheap enough to spread.” The transistor note records a semiconductor amplifier and
   collaborative Bell Labs work, not that switching/reliability claim. The integrated-circuit
   note explicitly says it does not establish a quantitative cost or scale history. As written,
   the chapter promotes those unsupported causal claims into the factual spine of the opening
   timeline. Replace them with the supported claims about electronic components, integration,
   practicality, and collaborative handoffs, or supply appropriately scoped recorded evidence.

3. **Recompute the Hero reading-time badge from rendered words.** `minutes={9}` does not match
   the authoring rule of roughly 200 words per minute, rounded up. A semantic render of the
   chapter body, including headings, captions, component titles, diagram labels, the Hero
   thesis, and the purchase label, is about 1,350 words, which rounds to 7 minutes. Even the raw
   MDX source is only 1,653 words before imports, JSX syntax, coordinates, and prop names are
   removed. Set the badge from the actual rendered count.

### Advisory

None. The five diagrams use the declared vocabulary and match their surrounding prose, the
practice cards are concrete, the deliberate absence of a Model section is recorded in the
registry, the related entries are done and present on disk, and the caveat avoids replacing the
lone-genius myth with a blanket claim about collaboration. `npm run check` passed in full on
2026-07-28 (validation, prose lint, pipeline tests, 281 Vitest tests, typecheck, build, and
lint).

## Builder resolution — 2026-07-28

1. Rewrote the programmability key idea to distinguish changeable instructions from their
   storage location. It now states that a programmable machine may receive instructions from an
   external medium or keep them in memory, while storage is a separate architectural choice. The
   comparison titles, points, caption, and accessible label now make the same distinction.
2. Replaced the unsupported timeline claims about faster, more reliable, and cheaper switching
   with the recorded evidence: collaborative electronic-component work, component integration
   making new forms of computing practical, and networked handoffs. The timeline now has a
   distinct integrated-circuits segment and matching accessible label.
3. Changed the Hero badge from `9` to `7` minutes, matching the recorded semantic rendered-word
   count of about 1,350 words at roughly 200 words per minute, rounded up.

`npm run check` passed on 2026-07-28 after these changes.

## Critique round 2 — 2026-07-28

### Required

None. The builder's three recorded resolutions are present and aligned across the prose,
diagram labels, captions, accessible labels, and Hero badge. The chapter now keeps
programmability distinct from stored-program architecture, limits the opening relay to claims
supported by the recorded evidence, and uses the required seven-minute reading time.

### Advisory

None. The five key ideas each have a distinct in-vocabulary diagram, the practices are concrete,
the caveat preserves individual responsibility and unequal access to credit, the deliberate
absence of a Model section is recorded, and all three related books are done. `npm run check`
passed in full on 2026-07-28.
