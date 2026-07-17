# Diagram Vocabulary — darvinyi-library

A fixed set of diagram forms. Every key-idea visual and every hero "Model" diagram picks a form from this list. This is deliberate: a bounded vocabulary keeps the whole shelf visually coherent and keeps the pipeline from reinventing a diagram grammar per book. Pick the form that fits the concept. If a concept genuinely needs a form not here, add the form to this file (name, when-to-use, and a reusable component) before using it.

All forms share the house rendering: background `#0a0e0f`, primary accent `#2dd4bf`, secondary strokes in muted gray (`#3a4145` to `#6b7280`), structural labels in JetBrains Mono, prose labels in Inter. Hand-authored inline SVG returned from a React component. No diagramming or charting library. Legible at 360px. One-line caption in house voice.

Each form below is a reusable primitive in `src/components/diagrams/`. A book page composes and labels these; it does not author raw SVG from zero each time.

## The forms

### 1. Process loop
A cycle of stages connected by arrows returning to the start. For anything iterative or self-reinforcing.
- Use for: the habit loop (cue → routine → reward), build-measure-learn, the flywheel, feedback cycles, virtuous/vicious circles.
- Component: `<ProcessLoop stages={[...]} direction="cw" />`
- Variant: mark one edge as the reinforcing "compounding" arrow in accent.

### 2. Two-by-two matrix
Two axes, four quadrants. For anything that sorts on two independent dimensions.
- Use for: the Eisenhower urgent/important matrix, radical candor, effort vs. impact, any typology.
- Component: `<Matrix xAxis={...} yAxis={...} quadrants={[...]} highlight={...} />`
- Highlight the "target" quadrant in accent; leave the rest muted.

### 3. Pyramid / hierarchy
Stacked tiers, foundational at the base. For layered or prerequisite structures.
- Use for: Maslow's hierarchy, layered models where lower levels support higher ones.
- Component: `<Pyramid tiers={[...]} ascending />`
- Note: recreate the *concept* of a needs hierarchy; do not trace Maslow's specific figure.

### 4. Spectrum / gradient
A single labeled axis between two poles, optionally with a marker. For matters of degree.
- Use for: fixed↔growth mindset, fragile↔antifragile, introvert↔extrovert, any continuum.
- Component: `<Spectrum left={...} right={...} marker={...} zones={[...]} />`

### 5. Concentric circles
Nested rings, core outward. For center-and-layers ideas.
- Use for: the Golden Circle (why/how/what), circle of control vs. concern, core-values models.
- Component: `<Concentric rings={[...]} labelFrom="inside" />`

### 5a. Core / context
A grouped enduring center with two or more peer elements, surrounded by changeable context.
For models where the core's parts are parallel, not successive rings or prerequisite tiers.
- Use for: core values plus purpose, constitutional principles plus evolving policy, or any stable identity with revisable practices around it.
- Component: `<CoreContext coreTitle="..." coreItems={[...]} contextItems={[...]} />`

### 6. Flow / sequence
Directed left-to-right (or top-down) stages, non-cyclic. For processes with a start and an end.
- Use for: pipelines, decision procedures, staged methods, cause→effect chains.
- Component: `<Flow steps={[...]} branch={optional} />`
- Variant: a branch node for fork-in-the-path decisions.

### 7. Annotated curve
A plotted line making a conceptual (not data-precise) point, with annotations on regions.
- Use for: the flow channel (challenge vs. skill), the forgetting curve, compounding/exponential growth, the hype cycle, diminishing returns.
- Component: `<Curve shape="exp|log|s|u|bell|channel" annotations={[...]} axes={{x,y}} />`
- These are illustrative. Label axes conceptually; never present as reproduced data from the book.

### 8. Comparison / split
Two side-by-side panels contrasting two states or approaches.
- Use for: System 1 vs. System 2, red ocean vs. blue ocean, positions vs. interests, before/after.
- Component: `<Compare left={{title,points}} right={{title,points}} />`
- Keep the two panels visually parallel so the contrast reads instantly.

### 9. Iceberg
Small visible tip above a waterline, large mass below. For surface-vs-underlying ideas.
- Use for: what's visible vs. what drives it, conscious vs. unconscious, stated vs. real.
- Component: `<Iceberg above={...} below={[...]} />`

### 10. Venn / overlap
Two or three overlapping sets with a labeled intersection. For sweet-spot and combination ideas.
- Use for: the Hedgehog Concept (three circles), ikigai-style intersections, overlap-is-the-point models.
- Component: `<Venn sets={[...]} intersectionLabel={...} />`

### 11. Node graph
Nodes connected by edges, non-hierarchical. For networks and system maps.
- Use for: stocks-and-flows sketches, network effects, systems with feedback between parts.
- Component: `<NodeGraph nodes={[...]} edges={[...]} />`
- Keep sparse and legible; this is a concept sketch, not a full systems model.

### 12. Timeline / bar
A horizontal axis of ordered segments or magnitudes. For sequence-in-time or simple magnitude contrasts.
- Use for: historical arcs (e.g., Sapiens' revolutions), stage theories over time, simple relative comparisons.
- Component: `<Timeline segments={[...]} />` / `<Bars items={[...]} />`
- For magnitude bars, keep it conceptual and clearly labeled; not a data chart.

## Matching guidance

Rough defaults from concept shape to form:

- Something that feeds back on itself → **process loop** or **node graph**.
- Sorting on two dimensions → **two-by-two matrix**.
- Levels that build on each other → **pyramid**.
- A matter of degree → **spectrum**; a matter of degree with a curve → **annotated curve**.
- Center and layers → **concentric circles**.
- Parallel elements inside a stable center, with changeable elements outside → **core / context**.
- A start-to-end procedure → **flow**.
- Two contrasting things → **comparison** (or **spectrum** if they are two poles of one axis).
- Surface vs. depth → **iceberg**.
- A sweet spot where things overlap → **venn**.
- A change or relationship over time → **timeline** or **annotated curve**.

When two forms fit, choose the simpler one, and vary forms across a single page so one book's key-idea diagrams are not all the same shape.
