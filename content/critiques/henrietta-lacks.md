verdict: revise

## Critique round 1 — 2026-07-26

### Required

1. **The core synthesis omits the racial and family power structure that the brief
   names as central.** The brief's thesis is that Henrietta Lacks's story exposes
   "the ethics and race at the heart of science," but the Hero, thesis, and takeaway
   reduce that argument to general duties of consent, privacy, recognition, and
   respect (lines 5-26 and 207-211). Race appears only once, as the unexamined phrase
   "racial inequality" (lines 105-110). The page never even tells the reader that
   Lacks was a Black woman, nor does a key idea explain how racialized institutional
   power shaped what happened to her and her family. As a result, the five-idea spine
   reads as a capable modern biospecimen-ethics primer, but not as a distillation of
   the argument assigned in the brief. Rework the thesis and key-idea spine so the
   racial and family dimension receives structural treatment, including an original
   diagram, and extend the evidence record with direct support for the history used.

2. **A post-publication development is presented as one of the book's five core
   ideas without a clear chronology or provenance boundary.** The book is from 2010,
   while the agreement at the center of "Governance can turn gratitude into
   responsibility" occurred in 2013 (lines 138-164). The evidence correctly dates
   the NIH-Lacks Family Agreement, but the page does not identify this section as a
   later update, so a reader can reasonably take it as part of Skloot's account.
   The later agreement is useful context, but it cannot silently substitute for one
   fifth of the book's conceptual spine. Label and position it explicitly as a
   post-book development, and restore the displaced core material from the book, or
   otherwise make the boundary between distillation and subsequent history
   unmistakable.

3. **The trust feedback loop is not supported by the recorded evidence.** Lines
   112-116 and Figure 88.4 make a substantive causal claim that respectful choice
   increases participation, participation broadens evidence, broader evidence makes
   research more relevant, and resulting benefit earns trust. The evidence note
   records sources for HeLa's origin and uses, genome privacy, consent rules, and the
   2013 governance agreement, but none for this participation-to-evidence-to-trust
   chain. Because the claim occupies a full key idea and structural diagram, it
   materially changes the reader's understanding rather than serving as incidental
   commentary. Add recorded support for the causal relationships, qualify the model
   explicitly as a proposed inference, or replace it with a key idea that can be
   re-derived from the book brief and evidence.

### Advisory

None.

Mechanical verification: `npm run check` passed on 2026-07-26.

## Builder resolution — 2026-07-26

Resolved every required finding.

1. Rewrote the Hero, thesis, Why It Matters, and takeaway to identify Henrietta Lacks as a Black woman and make race, family, and institutional power part of the chapter's central argument. Replaced the unsupported trust-loop key idea with "Race and family are part of the power question," including an original Venn diagram that maps racialized access to care, institutional control of tissue, and family exposure and exclusion. Added direct institutional evidence for the historical context, including the important qualification that the collection practice was not race-specific.
2. Reclassified the NIH-Lacks Family Agreement as the subordinate section "A later development: the 2013 agreement." It now states that the book was published in 2010, identifies the agreement as subsequent history rather than a core idea, and preserves its limited value as a governance example.
3. Removed the unsupported participation-to-evidence-to-trust causal loop and its NodeGraph. The replacement makes no unrecorded causal claim; it is a structural account grounded in the expanded evidence record.

Mechanical verification: `npm run check` passed on 2026-07-26 after this resolution.

## Critique round 2 — 2026-07-26

### Required

1. **A second post-publication development still appears inside the book's core
   idea spine without a chronology boundary.** The privacy section says that the
   stakes sharpened when the HeLa genome was sequenced, then attributes the
   section's lesson to the book (lines 84-95). The recorded evidence supports the
   later genome-data privacy issue and ties its governance response to 2013, while
   the brief and the page identify the book as a 2010 publication. Unlike the
   agreement section, this core section does not tell the reader that the genomic
   development is subsequent history. The result preserves the provenance problem
   from round 1 in a different key idea: a reader can reasonably take later
   genomic history as part of Skloot's original account. Mark the sequencing and
   descendant-privacy discussion explicitly as post-book context, or re-anchor the
   core privacy idea in material that the recorded evidence and brief support as
   part of the book, while keeping later history clearly separated.

2. **The rewritten thesis block violates the required thesis anatomy.** The
   authoring spec defines "The Thesis" as one or two sentences, the single
   carry-away paragraph for a reader who reads nothing else. Lines 13-19 now use
   six sentences to move through achievement, chronology, race, scientific value,
   and obligation. The argument is present, but it is no longer the required
   compressed thesis. Reduce this block to one or two sentences that retain the
   book's scientific, racial, family, and consent dimensions.

### Advisory

None.

Mechanical verification: `npm run check` passed on 2026-07-26.
