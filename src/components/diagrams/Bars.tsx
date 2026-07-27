import { C, MONO, wrapLabel, type DiagramBase } from "./_util";
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
  const trackW = 220;
  let cursor = 14;
  const rows = items.map((item) => {
    const labelLines = wrapLabel(item.label, 16);
    // Annotations sit under the bar rather than beyond its endpoint. This keeps
    // long explanations inside the fixed SVG viewport at narrow display widths.
    const valueLines = item.valueLabel ? wrapLabel(item.valueLabel, 30) : [];
    const mainHeight = Math.max(20, labelLines.length * 12);
    const annotationHeight = valueLines.length ? valueLines.length * 12 + 8 : 0;
    const row = {
      item,
      labelLines,
      valueLines,
      centerY: cursor + mainHeight / 2,
      annotationY: cursor + mainHeight + 12,
    };
    cursor += mainHeight + annotationHeight + 10;
    return row;
  });
  const height = Math.max(56, cursor + 4);

  return (
    <Svg
      viewBox={`0 0 380 ${Math.round(height)}`}
      ariaLabel={ariaLabel ?? `A bar comparison of ${items.map((i) => i.label).join(", ")}.`}
      className={className}
    >
      {rows.map(({ item, labelLines, valueLines, centerY, annotationY }, i) => {
        const y = centerY;
        const v = Math.min(1, Math.max(0, item.value));
        const w = Math.max(2, trackW * v);
        return (
          <g key={i}>
            <text textAnchor="end" fontFamily={MONO} fontSize="11" fill={item.accent ? C.accent : C.fg}>
              {labelLines.map((ln, li) => (
                <tspan key={li} x={gutter} y={y + 4 - (labelLines.length - 1) * 6 + li * 12}>
                  {ln}
                </tspan>
              ))}
            </text>
            <rect x={trackX} y={y - 9} width={trackW} height={18} rx="4" fill={C.surface2} stroke={C.border} />
            <rect x={trackX} y={y - 9} width={w} height={18} rx="4" fill={item.accent ? C.accent : C.comment} fillOpacity={item.accent ? 0.85 : 0.6} />
            {valueLines.length > 0 && (
              <text data-bar-annotation="true" fontFamily={MONO} fontSize="10" fill={C.muted}>
                {valueLines.map((line, lineIndex) => (
                  <tspan key={lineIndex} x={trackX} y={annotationY + lineIndex * 12}>
                    {line}
                  </tspan>
                ))}
              </text>
            )}
          </g>
        );
      })}
    </Svg>
  );
}
