import { useId } from "react";
import { C, MONO, wrapLabel, type DiagramBase } from "./_util";
import { Svg, CenteredText } from "./_shared";

export interface ProcessLoopProps extends DiagramBase {
  /** Stage labels, placed clockwise from the top. Two to six read well. */
  stages: string[];
  /** Travel direction around the loop. */
  direction?: "cw" | "ccw";
  /** Index of the edge (from stage i to the next) to mark as the reinforcing one. */
  compoundingEdge?: number;
  /** A short label for the loop's center, e.g. "the habit loop". */
  centerLabel?: string;
}

const polar = (cx: number, cy: number, r: number, deg: number): [number, number] => {
  const a = (deg * Math.PI) / 180;
  return [cx + r * Math.cos(a), cy + r * Math.sin(a)];
};

const arc = (cx: number, cy: number, r: number, a1: number, a2: number, sweep: number) => {
  const [sx, sy] = polar(cx, cy, r, a1);
  const [ex, ey] = polar(cx, cy, r, a2);
  const large = Math.abs(a2 - a1) > 180 ? 1 : 0;
  return `M${sx.toFixed(1)},${sy.toFixed(1)} A${r},${r} 0 ${large} ${sweep} ${ex.toFixed(1)},${ey.toFixed(1)}`;
};

/**
 * A cycle of stages connected around a ring, for anything iterative or
 * self-reinforcing: the habit loop, build-measure-learn, a flywheel. One edge can be
 * marked as the reinforcing "compounding" arrow in accent.
 */
export function ProcessLoop({
  stages = ["cue", "routine", "reward"],
  direction = "cw",
  compoundingEdge,
  centerLabel,
  ariaLabel,
  className,
}: ProcessLoopProps) {
  const uid = useId();
  const cx = 190;
  const cy = 160;
  const r = 112;
  const n = stages.length;
  const cw = direction === "cw";
  // Stage i sits at the top (-90) and steps around the ring in the travel direction.
  const angleOf = (i: number) => -90 + (cw ? 1 : -1) * (i * 360) / n;

  return (
    <Svg
      viewBox="0 0 380 320"
      ariaLabel={ariaLabel ?? `A loop of stages: ${stages.join(", then ")}, returning to the start.`}
      className={className}
    >
      <defs>
        <marker id={`pl-arw-${uid}`} viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M0,0 L10,5 L0,10 z" fill={C.comment} />
        </marker>
        <marker id={`pl-arwA-${uid}`} viewBox="0 0 10 10" refX="7" refY="5" markerWidth="7" markerHeight="7" orient="auto">
          <path d="M0,0 L10,5 L0,10 z" fill={C.accent} />
        </marker>
      </defs>

      {/* guide ring */}
      <circle cx={cx} cy={cy} r={r} stroke={C.border} strokeWidth="1" />

      {/* directional arcs in the gaps between stages */}
      {stages.map((_, i) => {
        const mid = angleOf(i) + (cw ? 1 : -1) * (360 / n) / 2;
        const half = Math.min(26, 360 / n / 2 - 8);
        const isCompound = compoundingEdge === i;
        const a1 = mid - (cw ? half : -half);
        const a2 = mid + (cw ? half : -half);
        return (
          <path
            key={`edge-${i}`}
            d={arc(cx, cy, r, a1, a2, cw ? 1 : 0)}
            stroke={isCompound ? C.accent : C.comment}
            strokeWidth={isCompound ? 2 : 1.4}
            markerEnd={`url(#${isCompound ? `pl-arwA-${uid}` : `pl-arw-${uid}`})`}
          />
        );
      })}

      {/* center label */}
      {centerLabel && (
        <CenteredText x={cx} y={cy} lines={wrapLabel(centerLabel, 14)} fill={C.comment} size={11} />
      )}

      {/* stage nodes */}
      {stages.map((label, i) => {
        const [x, y] = polar(cx, cy, r, angleOf(i));
        const w = 108;
        const h = 46;
        return (
          <g key={`node-${i}`}>
            <rect x={x - w / 2} y={y - h / 2} width={w} height={h} rx="7" fill={C.surface2} stroke={C.accent} strokeOpacity="0.5" />
            <CenteredText x={x} y={y} lines={wrapLabel(label, 15)} fill={C.fg} size={12} font={MONO} />
          </g>
        );
      })}
    </Svg>
  );
}
