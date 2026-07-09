import { C, MONO, wrapLabel, type DiagramBase } from "./_util";
import { Svg, CenteredText } from "./_shared";

export interface ConcentricRing {
  label: string;
}

export interface ConcentricProps extends DiagramBase {
  /** Rings from the core outward: index 0 is the innermost, the last is outermost. */
  rings: ConcentricRing[];
  /** Index of a ring to emphasize in accent (defaults to the core). */
  highlight?: number;
}

/**
 * Nested rings, core outward: for center-and-layers ideas like the Golden Circle
 * (why, how, what) or circles of control. The core is the load-bearing center; each
 * ring is a layer around it.
 */
export function Concentric({ rings = [], highlight = 0, ariaLabel, className }: ConcentricProps) {
  const cx = 190;
  const cy = 160;
  const outerR = 138;
  const n = Math.max(rings.length, 1);
  const boundary = (k: number) => (outerR * k) / n;

  // Draw outer rings first so inner discs paint on top.
  const order = rings.map((_, i) => i).reverse();

  return (
    <Svg
      viewBox="0 0 380 320"
      ariaLabel={
        ariaLabel ??
        `Concentric rings from the core outward: ${rings.map((r) => r.label).join(", ")}.`
      }
      className={className}
    >
      {order.map((i) => {
        const on = highlight === i;
        return (
          <circle
            key={`ring-${i}`}
            cx={cx}
            cy={cy}
            r={boundary(i + 1)}
            fill={i === 0 ? (on ? C.accent : C.surface2) : C.surface}
            fillOpacity={i === 0 && on ? 0.16 : i % 2 === 0 ? 1 : 0.55}
            stroke={on ? C.accent : C.border}
            strokeOpacity={on ? 0.7 : 1}
            strokeWidth={on ? 1.6 : 1}
          />
        );
      })}

      {rings.map((ring, i) => {
        const on = highlight === i;
        const y = i === 0 ? cy : cy - (boundary(i) + boundary(i + 1)) / 2;
        return (
          <CenteredText
            key={`label-${i}`}
            x={cx}
            y={y}
            lines={wrapLabel(ring.label, 16)}
            fill={on ? C.accent : i === 0 ? C.fg : C.muted}
            size={i === 0 ? 13 : 11}
            font={MONO}
            weight={i === 0 ? 600 : undefined}
          />
        );
      })}
    </Svg>
  );
}
