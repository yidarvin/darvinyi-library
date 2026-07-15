verdict: resolved

## Critique round 1 — 2026-07-15

### Required

1. **Give the signature framework its required Model section.** The brief names the Four Laws of Behavior Change as the signature model, and the authoring spec requires `The Model` after the key ideas. The draft instead makes “The four laws of behavior change” a sixth key idea and never renders a `## The Model` section. Move or rebuild this material as the hero model. The model visual also needs to encode the stated one-to-one mapping from cue, craving, response, and reward to the four laws, plus the inversions used to break a habit. The current `Flow` only sequences the four positive laws, so it implies a start-to-finish procedure and omits half of the framework described in the prose.

2. **Make the SVG labels legible at a 360px viewport.** At that viewport, the page and `Figure` padding leave roughly 278px for an SVG. The four-law `Flow` has a 558-unit-wide viewBox, so its 11.5-unit labels render at about 5.7 CSS pixels. The 380-to-384-unit figures also reduce several 9.5-to-12-unit labels to roughly 7-to-9 CSS pixels. This fails the explicit mobile requirement. Give the chapter figures a layout or minimum rendered width that preserves readable type, using the existing horizontal overflow where necessary, and verify every figure at 360px. Do not solve this by changing shared components for this critique.

3. **Correct the empirical description of habit formation.** The caveat says that a new habit took “an average of about sixty-six days to feel automatic,” with a range from eighteen days to beyond two hundred. Lally et al. operationalized the endpoint as the modeled time to reach 95% of each participant’s asymptote on a self-reported automaticity measure. The 66-day median and 18-to-254-day range apply to the 39 participants whose curves had a good fit, not to all 96 volunteers and not to a binary point at which a habit suddenly felt automatic. Preserve the useful variability point, but state the measure, endpoint, and limited subset accurately. Also remove or support the earlier claim that habits form because the loop runs “thousands of times”; the cited primary evidence shows automaticity developing over dozens of repeated opportunities for many behaviors and does not establish that threshold.

4. **Link the footer to a qualifying source for the book.** `buyUrl` currently points to James Clear’s promotional landing page. The anatomy and definition of done require the outbound book link itself to be a publisher or bookseller. Use a stable direct publisher or bookseller URL.

5. **Complete the `atomic-habits` registry record required by the content contract.** The record contains the display title, author/year in `subtitle`, shelf in `part`, and status, but it omits the explicit tier, thesis, framework, and diagram list required by definition-of-done item 7. Add the chapter metadata without changing the registry’s shared tooling or unrelated entries.

### Advisory

1. In the goals-versus-systems comparison, “yours alone” and “runs on autopilot” are too categorical. Systems can be shared, and a system is broader than an automatic habit. More parallel, precise contrasts would teach the distinction better.

2. The opening claim that “Most attempts at change fail because they aim at the wrong target” is broader than the evidence presented. Framing it explicitly as Clear’s diagnosis would preserve the force without presenting it as a measured base rate.

3. The first caption, “nothing on Tuesday and everything by December,” is memorable but overstates the illustrative math that the caveat later qualifies. A caption that says the daily difference is hard to see while the accumulated difference becomes large would better match the page’s measured voice.

### Evidence checked

- James Clear’s [official summary](https://jamesclear.com/atomic-habits-summary) supports the 1% example, systems/identity themes, four-stage loop, four laws, and their inversions. Independent calculation gives `1.01^365 = 37.783` and `0.99^365 = 0.0255`.
- Clear’s [goals and systems excerpt](https://jamesclear.com/goals-systems) and [four-stage framework excerpt](https://jamesclear.com/three-steps-habit-change) support the attribution of those ideas and show that the four laws are levers mapped to the four stages, not merely a linear sequence.
- Lally et al., [“How are habits formed: Modelling habit formation in the real world”](https://doi.org/10.1002/ejsp.674), reports 96 volunteers, 39 good-fit individual curves, a median modeled time of 66 days to 95% of the automaticity asymptote, and an 18-to-254-day range.
- `npm run check` passed on 2026-07-15: validation, prose lint, pipeline tests, six Vitest tests, TypeScript/Vite production build, and ESLint all completed successfully. The jsdom run emitted only its known `Window.scrollTo()` not-implemented notices.

## Builder resolution — 2026-07-15

- Moved the Four Laws material out of Key Ideas into the required `## The Model` section. Its single captioned hero figure now combines a cyclic cue-craving-response-reward loop with a paired build/break comparison that maps every stage to its positive law and its inverse.
- Applied chapter-local `min-w-[440px]` SVG sizing to all Atomic Habits figures, including both model sub-figures. The existing Figure overflow container now preserves at least 11px-scale diagram labels at a 360px viewport without changing shared components.
- Rewrote the habit-formation caveat to identify the Lally measure, 95-percent modeled-asymptote endpoint, 39 good-fit participants, 66-day median, 18-to-254-day range, and 96-volunteer study context. Removed the unsupported thousands-of-repetitions claim.
- Replaced the promotional outbound URL with Penguin Random House's direct Atomic Habits book page.
- Added the Atomic Habits registry tier, thesis, framework, and diagram-list metadata. Also tightened the goal/system comparison, attributed the opening diagnosis to Clear, and softened the compounding caption.
- Ran `npm run check` successfully: validation, prose lint, pipeline tests, six Vitest tests, TypeScript/Vite build, and ESLint all passed. The known jsdom `Window.scrollTo()` notices remained non-failing.
