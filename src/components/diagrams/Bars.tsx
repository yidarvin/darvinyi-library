import { C, MONO, type DiagramBase } from "./_util";
import { Svg } from "./_shared";

export interface BarItem {
  label: string;
  /** Magnitude, 0 to 1. Conceptual, not a precise data value. */
  value: number;
  /** Draw this bar in accent to single it out. */
  accent?: boolean;
  /** Optional short value caption at the end of the bar, e.g. "80%". */
  valueLabel?: string;
}

export interface BarsProps extends DiagramBase {
  items: BarItem[];
}

/**
 * Horizontal bars for a simple magnitude contrast: relative sizes, conceptual
 * proportions. Kept clearly conceptual and labeled, not a precise data chart.
 */
export function Bars({ items = [], ariaLabel, className }: BarsProps) {
  const gutter = 128;
  const trackX = gutter + 8;
  const trackW = 380 - trackX - 40;
  const rowH = 38;
  const top = 14;
  const height = top * 2 + items.length * rowH;

  return (
    <Svg
      viewBox={`0 0 380 ${Math.round(height)}`}
      ariaLabel={ariaLabel ?? `A bar comparison of ${items.map((i) => i.label).join(", ")}.`}
      className={className}
    >
      {items.map((item, i) => {
        const y = top + i * rowH + rowH / 2;
        const v = Math.min(1, Math.max(0, item.value));
        const w = Math.max(2, trackW * v);
        return (
          <g key={i}>
            <text x={gutter} y={y + 4} textAnchor="end" fontFamily={MONO} fontSize="11" fill={item.accent ? C.accent : C.fg}>
              {item.label}
            </text>
            <rect x={trackX} y={y - 9} width={trackW} height={18} rx="4" fill={C.surface2} stroke={C.border} />
            <rect x={trackX} y={y - 9} width={w} height={18} rx="4" fill={item.accent ? C.accent : C.comment} fillOpacity={item.accent ? 0.85 : 0.6} />
            {item.valueLabel && (
              <text x={trackX + w + 6} y={y + 4} fontFamily={MONO} fontSize="10" fill={C.muted}>
                {item.valueLabel}
              </text>
            )}
          </g>
        );
      })}
    </Svg>
  );
}
