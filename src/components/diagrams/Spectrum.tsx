import { useId } from "react";
import { C, MONO, wrapLabel, type DiagramBase } from "./_util";
import { Svg, CenteredText } from "./_shared";

export interface SpectrumZone {
  /** Start and end along the axis, each 0 (left pole) to 1 (right pole). */
  from: number;
  to: number;
  label: string;
  /** Draw this zone in accent rather than muted. */
  accent?: boolean;
}

export interface SpectrumProps extends DiagramBase {
  left: string;
  right: string;
  /** Optional marker position, 0 (left) to 1 (right). */
  marker?: number;
  /** Optional marker caption. */
  markerLabel?: string;
  /** Put a marker caption above the pole labels when the two would otherwise collide. */
  markerLabelPlacement?: "near-marker" | "top";
  /** Optional labeled bands along the axis. */
  zones?: SpectrumZone[];
}

/**
 * A single labeled axis between two poles, for matters of degree: fixed to growth,
 * fragile to antifragile, any continuum. An optional marker places a point on it and
 * optional zones name regions of the range.
 */
export function Spectrum({
  left = "less",
  right = "more",
  marker,
  markerLabel,
  markerLabelPlacement = "near-marker",
  zones = [],
  ariaLabel,
  className,
}: SpectrumProps) {
  const uid = useId();
  const x0 = 40;
  const x1 = 340;
  const span = x1 - x0;
  const trackY = 108;
  const at = (t: number) => x0 + span * Math.min(1, Math.max(0, t));

  return (
    <Svg
      viewBox="0 0 380 176"
      ariaLabel={ariaLabel ?? `A spectrum from ${left} to ${right}.`}
      className={className}
    >
      <defs>
        <linearGradient id={`sp-grad-${uid}`} x1="0" y1="0" x2="1" y2="0">
          <stop offset="0" stopColor={C.comment} />
          <stop offset="1" stopColor={C.accent} />
        </linearGradient>
      </defs>

      {/* zones */}
      {zones.map((z, i) => {
        const zx = at(z.from);
        const zw = at(z.to) - zx;
        return (
          <g key={`zone-${i}`}>
            <rect
              x={zx}
              y={trackY - 26}
              width={zw}
              height={52}
              rx="4"
              fill={z.accent ? C.accent : C.surface2}
              fillOpacity={z.accent ? 0.12 : 0.6}
              stroke={z.accent ? C.accent : C.border}
              strokeOpacity={z.accent ? 0.5 : 1}
            />
            <CenteredText
              x={zx + zw / 2}
              y={trackY + 44}
              lines={wrapLabel(z.label, Math.max(8, Math.floor(zw / 7)))}
              fill={z.accent ? C.accent : C.muted}
              size={9.5}
            />
          </g>
        );
      })}

      {/* the axis track */}
      <line x1={x0} y1={trackY} x2={x1} y2={trackY} stroke={`url(#sp-grad-${uid})`} strokeWidth="3" strokeLinecap="round" />
      <circle cx={x0} cy={trackY} r="4" fill={C.comment} />
      <circle cx={x1} cy={trackY} r="4" fill={C.accent} />

      {/* pole labels */}
      <text x={x0} y={trackY - 34} textAnchor="start" fontFamily={MONO} fontSize="12" fill={C.fg}>
        {left}
      </text>
      <text x={x1} y={trackY - 34} textAnchor="end" fontFamily={MONO} fontSize="12" fill={C.fg}>
        {right}
      </text>

      {/* marker */}
      {typeof marker === "number" && (
        <g>
          <path
            d={`M${at(marker)},${trackY - 12} l6,-11 l-12,0 z`}
            fill={C.accent}
          />
          <line x1={at(marker)} y1={trackY - 12} x2={at(marker)} y2={trackY + 12} stroke={C.accent} strokeWidth="2" />
          {markerLabel && (
            <text
              x={at(marker)}
              y={markerLabelPlacement === "top" ? 24 : trackY - 30}
              textAnchor="middle"
              fontFamily={MONO}
              fontSize="10"
              fill={C.accent}
            >
              {markerLabel}
            </text>
          )}
        </g>
      )}
    </Svg>
  );
}
