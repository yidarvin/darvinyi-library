import { useId } from "react";
import { C, MONO, wrapLabel, type DiagramBase } from "./_util";
import { Svg, CenteredText } from "./_shared";

export interface TimelineSegment {
  label: string;
  /** Optional secondary line, e.g. a date or a marker. */
  sub?: string;
}

export interface TimelineProps extends DiagramBase {
  segments: TimelineSegment[];
  /** Index of a segment to emphasize in accent. */
  highlight?: number;
}

/**
 * A horizontal axis of ordered segments, for a sequence in time: historical arcs,
 * stage theories, an era-by-era progression. The arrow marks the direction of time.
 */
export function Timeline({ segments = [], highlight, ariaLabel, className }: TimelineProps) {
  const uid = useId();
  const n = Math.max(segments.length, 1);
  const segW = 120;
  const x0 = 16;
  const axisY = 96;
  const width = x0 * 2 + n * segW + 24;
  const height = 168;

  return (
    <Svg
      viewBox={`0 0 ${width} ${height}`}
      ariaLabel={ariaLabel ?? `A timeline: ${segments.map((s) => s.label).join(", then ")}.`}
      className={className}
    >
      <defs>
        <marker id={`tl-arw-${uid}`} viewBox="0 0 10 10" refX="7" refY="5" markerWidth="8" markerHeight="8" orient="auto">
          <path d="M0,0 L10,5 L0,10 z" fill={C.comment} />
        </marker>
      </defs>

      {/* the time axis */}
      <line x1={x0} y1={axisY} x2={x0 + n * segW + 8} y2={axisY} stroke={C.comment} strokeWidth="1.5" markerEnd={`url(#tl-arw-${uid})`} />

      {segments.map((seg, i) => {
        const cx = x0 + i * segW + segW / 2;
        const on = highlight === i;
        const tickX = x0 + i * segW;
        return (
          <g key={i}>
            <line x1={tickX} y1={axisY - 6} x2={tickX} y2={axisY + 6} stroke={C.border} strokeWidth="1.5" />
            <circle cx={cx} cy={axisY} r={on ? 6 : 4.5} fill={on ? C.accent : C.surface2} stroke={on ? C.accent : C.comment} strokeWidth="1.5" />
            {/* label above the axis */}
            <CenteredText x={cx} y={axisY - 34} lines={wrapLabel(seg.label, 15)} fill={on ? C.accent : C.fg} size={11.5} font={MONO} weight={on ? 600 : undefined} />
            {/* sub below the axis */}
            {seg.sub && <CenteredText x={cx} y={axisY + 26} lines={wrapLabel(seg.sub, 16)} fill={C.muted} size={9.5} />}
          </g>
        );
      })}
    </Svg>
  );
}
