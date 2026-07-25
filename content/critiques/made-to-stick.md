verdict: resolved

## Critique round 1 — 2026-07-25

### Required

1. `src/chapters/made-to-stick.mdx:13-19` opens the thesis with a comparative causal
   claim that the brief and the repository's recorded evidence do not support:
   messages disappear less often because they are false or badly delivered than because
   they ask listeners to retain an expert's whole mental model. The brief supports the
   SUCCESs traits and deliberate message design, but it does not establish the relative
   prevalence of these causes of communication failure. This changes the reader's
   understanding by presenting the curse-of-knowledge diagnosis as more common than
   falsity or poor delivery. Recast it as the book's design problem without the unsupported
   frequency comparison, or support the comparison with existing recorded evidence.

2. Figure 74.4 contradicts its own prose. Lines 89-93 say that the strongest credibility
   mechanism depends on the decision and allow recognized expertise to be the right
   choice, while `favor="right"` at line 98 uses the comparison primitive's accent to
   explicitly favor "inspectable proof" over "borrowed trust." The diagram therefore
   teaches a hierarchy the explanation rejects. Make the visual neutral or revise the
   claim and evidence so the preference is actually warranted.

3. Figure 74.7 adds an unsupported distinction to the SUCCESs model. Lines 173, 176, and
   178 mark only simple, credible, and story-based as `reinforcing`; the shared
   `NodeGraph` renders those edges in accent with a plus sign. Neither the brief nor the
   surrounding explanation says those three qualities reinforce a message while
   unexpected, concrete, and emotional do not. The caption and accessible label instead
   present six parallel qualities. Remove the selective reinforcing semantics or explain
   and support them so the diagram matches the framework.

4. The Hero's `minutes={9}` does not follow the authoring spec's reading-time rule.
   Rendering the chapter through its MDX components produces 1,465 visible words, which
   is 8 minutes at approximately 200 words per minute when rounded up. Set the badge from
   the rendered count.

### Advisory

None.

## Builder resolution — 2026-07-25

- Recast the thesis as the book's message-design problem, removing the unsupported comparison with false or poorly delivered messages.
- Set Figure 74.4 to neutral emphasis (`favor="none"`) so authority and inspectable evidence remain parallel choices.
- Removed the selective `reinforcing` edge kinds from Figure 74.7; all six SUCCESs qualities now connect neutrally to the central message.
- Corrected the Hero reading-time badge from 9 to 8 minutes to match the recorded rendered-word count and the specified rounding rule.
