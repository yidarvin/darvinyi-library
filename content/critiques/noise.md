verdict: revise

## Critique round 1 — 2026-07-27

### Required

1. Figure 106.3 mis-encodes the source taxonomy it is meant to teach. In
   `src/chapters/noise.mdx:79`, the caption says that a case "pick[s] up variability,"
   and the three directed edges at lines 89–91 all terminate at the node labeled
   `same case`. Level, pattern, and occasion noise are sources of variation in the
   judgments or outcomes produced for the same case; they do not act on or alter the
   case itself. Redraw the relationship so the stable case is an input and the
   variable judgment is the affected output, or otherwise make the causal target
   unambiguous.

2. Figure 106.5 is not legible as authored because its value labels overflow the SVG
   viewport. The chapter supplies long labels such as `more room for drift` and
   `make reasons visible` at `src/chapters/noise.mdx:127-128`. `Bars` places each
   label at `trackX + w + 6` without wrapping or reserving horizontal space, inside a
   fixed 380-unit viewBox (`src/components/diagrams/Bars.tsx:23-25,32,53-55`). The
   first label begins at roughly x=330 and is clipped well before its text ends; the
   second also reaches beyond the right boundary. Make every label fit within the
   figure at 360px, whether by changing this figure's labeling/form or by fixing the
   primitive with regression coverage.

3. The `noise` registry record is incomplete for a finished chapter.
   `content/registry.json:2095-2103` contains only the scaffold metadata and status;
   it omits the chapter thesis, the explicit explanation that the Model section is
   deliberately absent, and the five diagram forms. Definition of done item 7 in
   `docs/authoring-spec.md` requires the registry entry to include its thesis,
   framework, and diagram list. Add metadata that agrees with the draft and brief
   before approval.

### Advisory

- None.

## Builder resolution — 2026-07-27

- Redrew Figure 106.3 so `stable case` is an input to `variable judgment`, with
  baseline, attention, and occasion noise all directed to the judgment rather than
  the case. Its caption now names that causal target directly.
- Reworked the shared `Bars` primitive so value annotations wrap below the track
  within the SVG viewport instead of extending past each bar endpoint. Added a
  shared regression test covering the long Noise annotations.
- Completed the Noise registry record with its tier, thesis, deliberate absence of
  a Model section, and the five diagram forms used by the chapter.
- Verified the targeted diagram and chapter test. Full `npm run check` passes.

## Critique round 2 — 2026-07-27

### Required

1. Figure 106.4 is not legible at the required 360px phone width. The four supplied
   steps at `src/chapters/noise.mdx:107-112` make `Flow` calculate a 558-unit-wide
   viewBox (`src/components/diagrams/Flow.tsx:21-27`), but the chapter passes
   `className="block w-full"` and `Svg` applies that class directly
   (`src/components/diagrams/_shared.tsx:28-33`). The SVG therefore compresses to
   the figure's content width instead of using the horizontal overflow wrapper. Even
   before accounting for the figure's 40px horizontal padding, the 11.5-unit step
   labels render below 7.5px in a 360px viewport; inside the padded figure they are
   smaller still. Make this four-step figure readable at 360px, either by giving the
   flow a real scrollable minimum width or by using a mobile layout that preserves
   legible label size, and add regression coverage for the sizing behavior.

### Advisory

- None.
