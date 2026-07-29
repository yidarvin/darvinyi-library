import { useId } from "react";
import { C, MONO, wrapLabel, type DiagramBase } from "./_util";
import { CenteredText, Svg } from "./_shared";

export interface AssemblyProps extends DiagramBase {
  /** Peer ingredients that combine into the result, rather than overlap as sets. */
  parts: string[];
  /** The whole created by bringing the peer ingredients together. */
  result: string;
}

/**
 * Several peer inputs converging on one assembled whole. Use when contribution and
 * combination are the idea, without implying an ordered procedure or set overlap.
 */
export function Assembly({ parts = [], result, ariaLabel, className }: AssemblyProps) {
  const uid = useId();
  const count = Math.max(parts.length, 1);
  const rowH = 44;
  const gap = 14;
  const top = 22;
  const height = top * 2 + count * rowH + (count - 1) * gap;
  const resultY = height / 2;

  return (
    <Svg
      viewBox={`0 0 400 ${height}`}
      ariaLabel={ariaLabel ?? `The peer elements ${parts.join(", ")} combine into ${result}.`}
      className={className}
    >
      <defs>
        <marker id={`as-arw-${uid}`} viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">
          <path d="M0,0 L10,5 L0,10 z" fill={C.comment} />
        </marker>
      </defs>

      {parts.map((part, i) => {
        const y = top + i * (rowH + gap);
        const cy = y + rowH / 2;
        return (
          <g key={part}>
            <rect x="20" y={y} width="140" height={rowH} rx="7" fill={C.surface2} stroke={C.border} />
            <CenteredText x={90} y={cy} lines={wrapLabel(part, 18)} fill={C.fg} size={11.5} font={MONO} />
            <path
              d={`M160,${cy} C188,${cy} 194,${resultY} 222,${resultY}`}
              stroke={C.comment}
              strokeWidth="1.5"
              markerEnd={`url(#as-arw-${uid})`}
            />
          </g>
        );
      })}

      <rect x="222" y={resultY - 34} width="158" height="68" rx="8" fill={C.accent} fillOpacity="0.12" stroke={C.accent} strokeOpacity="0.7" />
      <CenteredText x={301} y={resultY} lines={wrapLabel(result, 18)} fill={C.accent} size={12} font={MONO} weight={600} />
    </Svg>
  );
}
