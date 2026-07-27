verdict: resolved

## Critique round 1 — 2026-07-27

### Required

1. The slower-exhale stress intervention is not supported by the recorded evidence. The
   chapter states that a longer exhale can interrupt a stress spiral, depicts that mechanism
   in figure 102.4, and instructs the reader to lengthen the exhale in exercise 02. The
   evidence file supports an acute six-breaths-per-minute condition and changes in baroreflex
   sensitivity and blood pressure. It does not establish an exhale-specific effect, an
   anxiety feedback mechanism, or the claim that this technique changes the next turn of a
   stress cycle. Because this is one of five key ideas and becomes health guidance in the
   practice section, either ground the mechanism and instruction in recorded evidence or
   narrow them to what the existing paced-breathing evidence actually supports.

2. Figure 102.3 substitutes an unsupported feedback model for the result described in its
   prose. The paragraph discusses breath timing, heart rate, blood-pressure regulation, and
   measured baroreflex sensitivity. The node graph omits blood pressure and the baroreflex,
   adds directional claims from air exchange and heart rhythm to a "felt state," and marks
   "felt state" to "breath rhythm" as a reinforcing edge. In the shared vocabulary,
   reinforcing has a specific positive-feedback meaning, while "adjusts" could reinforce or
   balance a response. Redraw the figure so it encodes the documented physiological
   relationship without inventing a positive feedback loop.

3. Figure 102.5 contradicts the key idea it is meant to explain. The prose says comfort,
   responsiveness, and repeatability are the target, explicitly noting that deliberately
   slowing down can be uncomfortable. The spectrum instead makes "rushed or forced" and
   "slow and comfortable" its poles, visually favors the slow endpoint, and places the target
   near it. This conflates speed with comfort and teaches that slower is inherently better.
   Use an axis or comparison that separates effort or strain from pace and makes comfortable,
   repeatable breathing the target.

### Advisory

None.

## Builder resolution — 2026-07-27

1. Removed the longer-exhale instruction, stress-spiral mechanism, and claim that a breath
   changes the next turn of anxiety. Key Idea 4 now presents a breathing pause only as a
   transition cue, explicitly states the limits of the recorded six-breaths-per-minute study,
   and Exercise 02 uses an unforced even rhythm without an exhale target.
2. Rebuilt figure 102.3 as a neutral, non-directional map of the recorded six-per-minute
   condition, heart rhythm, blood pressure, and baroreflex sensitivity. It no longer includes
   air exchange, felt state, or a reinforcing edge.
3. Replaced figure 102.5 with a pace-by-felt-strain matrix. Both lower-strain pace ranges are
   highlighted as potentially comfortable and repeatable, while either pace can signal that the
   reader should back off when it feels strained. Extended the shared Matrix primitive to support
   peer highlighted quadrants and added its regression test.

The registry and Breath brief now carry the same narrower framing. Chapter status remains draft;
no done mark, commit, or push was made.
