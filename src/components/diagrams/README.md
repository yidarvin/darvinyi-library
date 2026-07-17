# Diagram primitives

The fixed vocabulary of diagram forms for the library, one reusable component per
form. Every key-idea figure and every hero Model diagram picks a form from this list
(see `docs/diagram-vocabulary.md` for when to use each). These are hand-authored
inline SVG: no diagramming or charting library, no raster images. Colors and fonts
resolve to the house tokens in `src/styles/tokens.css`, so they match automatically
and stay crisp at any width. Each is data-driven through props, gives a sensible
default render, is legible at 360px, and carries `role="img"` with a derived
`aria-label` (override with the `ariaLabel` prop).

Import from the barrel:

```tsx
import { ProcessLoop, Matrix } from "../components/diagrams";
```

Compose inside a `<Figure>` so it gets the framed card and caption:

```tsx
<Figure id="1.1" caption="The habit loop feeds back on itself.">
  <ProcessLoop stages={["cue", "craving", "response", "reward"]} compoundingEdge={3} />
</Figure>
```

## The forms and their props

Every form also takes `ariaLabel?` and `className?` (from `DiagramBase`).

| Form | Component | Key props |
|------|-----------|-----------|
| Process loop | `ProcessLoop` | `stages: string[]`, `direction?: "cw"\|"ccw"`, `compoundingEdge?: number`, `centerLabel?: string` |
| Two-by-two matrix | `Matrix` | `xAxis: {left,right,label?}`, `yAxis: {low,high,label?}`, `quadrants: [q,q,q,q]` (tl,tr,bl,br; each `{title,note?}`), `highlight?: number` |
| Pyramid / hierarchy | `Pyramid` | `tiers: {label,note?}[]` (base first), `highlight?: number` |
| Spectrum / gradient | `Spectrum` | `left`, `right`, `marker?: 0..1`, `markerLabel?`, `zones?: {from,to,label,accent?}[]` |
| Concentric circles | `Concentric` | `rings: {label}[]` (core first), `highlight?: number` |
| Core / context | `CoreContext` | `coreTitle`, `coreItems: string[]`, `contextItems: string[]`, `contextTitle?: string` |
| Flow / sequence | `Flow` | `steps: string[]`, `highlight?: number`, `branch?: {up,down}` |
| Annotated curve | `Curve` | `shape: "exp"\|"log"\|"s"\|"u"\|"bell"\|"channel"`, `axes?: {x?,y?}`, `annotations?: {x,y,text}[]` |
| Comparison / split | `Compare` | `left: {title,points[]}`, `right: {title,points[]}`, `favor?: "left"\|"right"\|"none"` |
| Iceberg | `Iceberg` | `above: string`, `below: string[]`, `waterlineLabel?` |
| Venn / overlap | `Venn` | `sets: {label}[]` (2 or 3), `intersectionLabel: string` |
| Node graph | `NodeGraph` | `nodes: {id,label,x?,y?}[]`, `edges: {from,to,kind?}[]` (`kind: "reinforcing"\|"balancing"`) |
| Timeline | `Timeline` | `segments: {label,sub?}[]`, `highlight?: number` |
| Bars | `Bars` | `items: {label,value:0..1,accent?,valueLabel?}[]` |

## House rules for these

- One accent. The teal is the single loud thing; secondary strokes stay muted. To
  single out an element, use the form's `highlight` / `compoundingEdge` / `accent`
  prop rather than adding a second color.
- Labels in the mono face (`--font-mono`); prose-y labels may use `--font-sans`.
  Keep labels short; the wrap helper breaks long ones across lines.
- Structure, not decoration. If a figure does not encode something true about the
  idea, cut it. One good figure beats three pretty ones.
- Vary the forms across a single book page so its key-idea diagrams are not all the
  same shape.
- Need a form that is not here? Add it to `docs/diagram-vocabulary.md` first (name,
  when-to-use, component), then build the component here, then use it.
