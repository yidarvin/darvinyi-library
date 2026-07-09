import { C, MONO, wrapLabel, type DiagramBase } from "./_util";
import { Svg, CenteredText } from "./_shared";

export interface PyramidTier {
  label: string;
  note?: string;
}

export interface PyramidProps extends DiagramBase {
  /** Tiers from the base (index 0, widest) up to the apex (last, narrowest). */
  tiers: PyramidTier[];
  /** Index of the tier to draw in accent. */
  highlight?: number;
}

/**
 * Stacked tiers, foundational at the base: for layered or prerequisite structures
 * where lower levels support higher ones (a needs hierarchy, a capability stack).
 * Rendered as centered, narrowing bars so each tier's label stays legible. This
 * recreates the concept of a hierarchy; it does not trace any specific figure.
 */
export function Pyramid({ tiers = [], highlight, ariaLabel, className }: PyramidProps) {
  const n = Math.max(tiers.length, 1);
  const baseW = 300;
  const apexW = 128;
  const rowH = 42;
  const gap = 7;
  const cx = 190;
  const topPad = 18;
  const height = topPad * 2 + n * rowH + (n - 1) * gap;

  return (
    <Svg
      viewBox={`0 0 380 ${Math.round(height)}`}
      ariaLabel={
        ariaLabel ??
        `A hierarchy of ${n} tiers from the base up: ${tiers.map((t) => t.label).join(", ")}.`
      }
      className={className}
    >
      {tiers.map((tier, i) => {
        // i = 0 is the base (bottom, widest); the last tier is the apex (top).
        const fromTop = n - 1 - i;
        const w = n === 1 ? baseW : baseW - ((baseW - apexW) * fromTop) / (n - 1);
        const y = topPad + fromTop * (rowH + gap);
        const on = highlight === i;
        return (
          <g key={`tier-${i}`}>
            <rect
              x={cx - w / 2}
              y={y}
              width={w}
              height={rowH}
              rx="5"
              fill={on ? C.accent : C.surface2}
              fillOpacity={on ? 0.16 : 1}
              stroke={on ? C.accent : C.border}
              strokeOpacity={on ? 0.6 : 1}
            />
            <CenteredText
              x={cx}
              y={y + rowH / 2 - (tier.note ? 7 : 0)}
              lines={wrapLabel(tier.label, Math.max(10, Math.floor(w / 8)))}
              fill={on ? C.accent : C.fg}
              size={12}
              font={MONO}
              weight={600}
            />
            {tier.note && (
              <CenteredText x={cx} y={y + rowH / 2 + 11} lines={[tier.note]} fill={C.muted} size={9} />
            )}
          </g>
        );
      })}
    </Svg>
  );
}
