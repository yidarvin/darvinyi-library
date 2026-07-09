import { C, MONO, wrapLabel, type DiagramBase } from "./_util";
import { Svg, CenteredText } from "./_shared";

export interface IcebergProps extends DiagramBase {
  /** The small visible tip above the waterline. */
  above: string;
  /** The larger mass below: the underlying drivers, top to bottom. */
  below: string[];
  /** Caption on the waterline itself. */
  waterlineLabel?: string;
}

/**
 * A small visible tip above a waterline over a large mass below, for surface-versus-
 * underlying ideas: what is visible against what drives it, stated against real.
 */
export function Iceberg({
  above = "what you see",
  below = ["what drives it"],
  waterlineLabel = "waterline",
  ariaLabel,
  className,
}: IcebergProps) {
  const waterY = 104;
  const cx = 190;

  return (
    <Svg
      viewBox="0 0 380 300"
      ariaLabel={ariaLabel ?? `An iceberg. Above the water: ${above}. Below: ${below.join(", ")}.`}
      className={className}
    >
      {/* water */}
      <rect x="0" y={waterY} width="380" height={300 - waterY} fill={C.accent} fillOpacity="0.05" />

      {/* mass below the waterline */}
      <polygon
        points={`150,${waterY} 230,${waterY} 286,168 262,236 190,280 118,246 94,166`}
        fill={C.surface2}
        stroke={C.border}
      />

      {/* tip above the waterline */}
      <polygon points={`190,44 232,${waterY} 148,${waterY}`} fill={C.surface} stroke={C.accent} strokeOpacity="0.6" />

      {/* waterline */}
      <line x1="0" y1={waterY} x2="380" y2={waterY} stroke={C.comment} strokeWidth="1.2" strokeDasharray="5 4" />
      <text x="372" y={waterY - 7} textAnchor="end" fontFamily={MONO} fontSize="9.5" fill={C.comment}>
        {`// ${waterlineLabel}`}
      </text>

      {/* labels */}
      <CenteredText x={cx} y={82} lines={wrapLabel(above, 16)} fill={C.accent} size={11.5} font={MONO} weight={600} />
      {below.map((b, i) => (
        <CenteredText
          key={i}
          x={cx}
          y={waterY + 40 + i * 34}
          lines={wrapLabel(b, 22)}
          fill={C.fg}
          size={11.5}
          font={MONO}
        />
      ))}
    </Svg>
  );
}
