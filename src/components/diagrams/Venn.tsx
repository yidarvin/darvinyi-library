import { C, MONO, wrapLabel, type DiagramBase } from "./_util";
import { Svg, CenteredText } from "./_shared";

export interface VennSet {
  label: string;
}

export interface VennProps extends DiagramBase {
  /** Two or three sets. Two overlap in the middle; three meet in the center. */
  sets: VennSet[];
  /** Label for the shared intersection, the point of the diagram. */
  intersectionLabel: string;
}

/**
 * Two or three overlapping sets with a labeled intersection, for sweet-spot and
 * combination ideas: the Hedgehog concept, an ikigai-style overlap where the overlap
 * itself is the point.
 */
export function Venn({ sets = [], intersectionLabel = "", ariaLabel, className }: VennProps) {
  const three = sets.length >= 3;
  const r = three ? 84 : 82;
  const label = (i: number) => (sets[i] ? sets[i].label : "");

  const circles = three
    ? [
        { cx: 190, cy: 112 },
        { cx: 138, cy: 200 },
        { cx: 242, cy: 200 },
      ]
    : [
        { cx: 152, cy: 158 },
        { cx: 228, cy: 158 },
      ];

  return (
    <Svg
      viewBox="0 0 380 300"
      ariaLabel={
        ariaLabel ??
        `Overlapping sets ${sets.map((s) => s.label).join(", ")} meeting at ${intersectionLabel}.`
      }
      className={className}
    >
      {circles.map((c, i) => (
        <circle
          key={i}
          cx={c.cx}
          cy={c.cy}
          r={r}
          fill={C.accent}
          fillOpacity="0.08"
          stroke={C.accent}
          strokeOpacity="0.55"
        />
      ))}

      {/* set labels, pushed outward from the cluster */}
      {three ? (
        <>
          <CenteredText x={190} y={54} lines={wrapLabel(label(0), 16)} fill={C.fg} size={11.5} font={MONO} />
          <CenteredText x={96} y={250} lines={wrapLabel(label(1), 14)} fill={C.fg} size={11.5} font={MONO} />
          <CenteredText x={284} y={250} lines={wrapLabel(label(2), 14)} fill={C.fg} size={11.5} font={MONO} />
          <CenteredText x={190} y={178} lines={wrapLabel(intersectionLabel, 12)} fill={C.accent} size={11} font={MONO} weight={600} />
        </>
      ) : (
        <>
          <CenteredText x={112} y={110} lines={wrapLabel(label(0), 13)} fill={C.fg} size={11.5} font={MONO} />
          <CenteredText x={268} y={110} lines={wrapLabel(label(1), 13)} fill={C.fg} size={11.5} font={MONO} />
          <CenteredText x={190} y={158} lines={wrapLabel(intersectionLabel, 12)} fill={C.accent} size={11} font={MONO} weight={600} />
        </>
      )}
    </Svg>
  );
}
