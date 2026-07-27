import { C, MONO, SANS, type DiagramBase } from "./_util";
import { Svg } from "./_shared";

export type CurveShape = "exp" | "log" | "s" | "u" | "bell" | "peak" | "decay" | "channel" | "crossover";

export interface CurveAnnotation {
  /** Position along the plot, each 0 to 1. */
  x: number;
  y: number;
  text: string;
  /** Put the label below its marker when the annotation describes a lower region. */
  labelPosition?: "above" | "below";
}

export interface CurveProps extends DiagramBase {
  shape: CurveShape;
  axes?: { x?: string; y?: string };
  annotations?: CurveAnnotation[];
}

const value = (shape: Exclude<CurveShape, "channel" | "crossover">, t: number): number => {
  switch (shape) {
    case "exp":
      return (Math.exp(3 * t) - 1) / (Math.exp(3) - 1);
    case "log":
      return Math.log(1 + 9 * t) / Math.log(10);
    case "s":
      return 1 / (1 + Math.exp(-11 * (t - 0.5)));
    case "u":
      return 4 * (t - 0.5) * (t - 0.5);
    case "bell":
      return Math.exp(-((t - 0.5) / 0.17) * ((t - 0.5) / 0.17) * 0.5);
    case "peak":
      // A conceptual rise to a maximum followed by a modest decline. This is useful
      // when the direction of change after a peak matters, without implying data values.
      return t <= 0.72
        ? 0.08 + 0.84 * (1 - (1 - t / 0.72) * (1 - t / 0.72))
        : 0.92 - 0.1 * Math.pow((t - 0.72) / 0.28, 1.2);
    case "decay":
      // A conceptual reaction that is strongest at the event and then loses force.
      // The floor keeps the line illustrative rather than implying that impact vanishes.
      return 0.18 + 0.74 * Math.exp(-2.8 * t);
  }
};

/**
 * A plotted line making a conceptual (not data-precise) point, with region
 * annotations: compounding growth, diminishing returns, an adoption S-curve, the
 * flow channel, or a crossover between two conceptual series. Axes are labeled
 * conceptually and never present reproduced data.
 */
export function Curve({ shape, axes, annotations = [], ariaLabel, className }: CurveProps) {
  const x0 = 46;
  const x1 = 344;
  const y0 = 30; // top of plot
  const y1 = 188; // bottom of plot (axis)
  const pw = x1 - x0;
  const ph = y1 - y0;
  const px = (t: number) => x0 + pw * t;
  const py = (v: number) => y1 - ph * Math.min(1, Math.max(0, v));

  return (
    <Svg
      viewBox="0 0 380 220"
      ariaLabel={ariaLabel ?? `A conceptual ${shape} curve.`}
      className={className}
    >
      {/* axes */}
      <line x1={x0} y1={y0} x2={x0} y2={y1} stroke={C.border} strokeWidth="1" />
      <line x1={x0} y1={y1} x2={x1} y2={y1} stroke={C.border} strokeWidth="1" />

      {shape === "channel" ? (
        <>
          {/* the flow channel: a widening diagonal band between over- and under-challenge */}
          <polygon points={`${x0},${y1} ${x1},${py(0.62)} ${x1},${py(0.38)} ${x0},${y1}`} fill={C.accent} fillOpacity="0.14" />
          <line x1={x0} y1={y1} x2={x1} y2={py(0.62)} stroke={C.accent} strokeWidth="1.4" strokeDasharray="4 3" />
          <line x1={x0} y1={y1} x2={x1} y2={py(0.38)} stroke={C.accent} strokeWidth="1.4" strokeDasharray="4 3" />
          <line x1={x0} y1={y1} x2={x1} y2={py(0.5)} stroke={C.accent} strokeWidth="2" />
          <text x={x0 + 26} y={y0 + 22} fontFamily={SANS} fontSize="11" fill={C.muted}>
            anxiety
          </text>
          <text x={x1 - 8} y={y1 - 12} textAnchor="end" fontFamily={SANS} fontSize="11" fill={C.muted}>
            boredom
          </text>
          <text
            x={px(0.62)}
            y={py(0.5) - 6}
            fontFamily={MONO}
            fontSize="11"
            fill={C.accent}
            transform={`rotate(-15 ${px(0.62)} ${py(0.5) - 6})`}
          >
            flow
          </text>
        </>
      ) : shape === "crossover" ? (
        <>
          {/* Two conceptual series meet when independent income covers recurring expenses. */}
          <path
            data-curve-series="independent-income"
            d={Array.from({ length: 49 }, (_, i) => {
              const t = i / 48;
              const income = 0.06 + 0.82 * t * t;
              return `${i === 0 ? "M" : "L"}${px(t).toFixed(1)},${py(income).toFixed(1)}`;
            }).join(" ")}
            stroke={C.accent}
            strokeWidth="2.4"
            strokeLinecap="round"
            strokeLinejoin="round"
          />
          <path
            data-curve-series="recurring-expenses"
            d={Array.from({ length: 49 }, (_, i) => {
              const t = i / 48;
              const expenses = 0.72 - 0.36 * t;
              return `${i === 0 ? "M" : "L"}${px(t).toFixed(1)},${py(expenses).toFixed(1)}`;
            }).join(" ")}
            stroke={C.muted}
            strokeWidth="2"
            strokeDasharray="5 4"
            strokeLinecap="round"
          />
          {(() => {
            const crossoverT = (-0.36 + Math.sqrt(0.36 * 0.36 + 4 * 0.82 * 0.66)) / (2 * 0.82);
            const crossoverValue = 0.72 - 0.36 * crossoverT;
            const crossoverX = px(crossoverT);
            const crossoverY = py(crossoverValue);
            return (
              <g>
                <line
                  data-crossover-guide="true"
                  x1={crossoverX}
                  y1={crossoverY}
                  x2={crossoverX}
                  y2={y1}
                  stroke={C.accent}
                  strokeWidth="1"
                  strokeDasharray="3 3"
                  opacity="0.7"
                />
                <circle data-crossover-point="true" cx={crossoverX} cy={crossoverY} r="4.5" fill={C.accent} />
                <text x={crossoverX + 8} y={crossoverY - 8} fontFamily={MONO} fontSize="10" fill={C.accent}>
                  crossover
                </text>
              </g>
            );
          })()}
          <g aria-hidden="true">
            <line x1={x0} y1="15" x2={x0 + 18} y2="15" stroke={C.accent} strokeWidth="2.4" />
            <text x={x0 + 24} y="19" fontFamily={MONO} fontSize="9.5" fill={C.accent}>
              independent income
            </text>
            <line x1="194" y1="15" x2="212" y2="15" stroke={C.muted} strokeWidth="2" strokeDasharray="5 4" />
            <text x="218" y="19" fontFamily={MONO} fontSize="9.5" fill={C.muted}>
              recurring expenses
            </text>
          </g>
        </>
      ) : (
        <path
          d={Array.from({ length: 49 }, (_, i) => {
            const t = i / 48;
            return `${i === 0 ? "M" : "L"}${px(t).toFixed(1)},${py(value(shape, t)).toFixed(1)}`;
          }).join(" ")}
          stroke={C.accent}
          strokeWidth="2.4"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      )}

      {/* annotations */}
      {annotations.map((a, i) => (
        <g key={`ann-${i}`}>
          <circle cx={px(a.x)} cy={py(a.y)} r="3.5" fill={C.accent} />
          <text
            x={px(a.x) + (a.x > 0.7 ? -8 : 8)}
            y={py(a.y) + (a.labelPosition === "below" ? 18 : -8)}
            textAnchor={a.x > 0.7 ? "end" : "start"}
            fontFamily={MONO}
            fontSize="10"
            fill={C.fg}
          >
            {a.text}
          </text>
        </g>
      ))}

      {/* axis labels */}
      {axes?.x && (
        <text x={(x0 + x1) / 2} y={214} textAnchor="middle" fontFamily={MONO} fontSize="10" fill={C.comment}>
          {`${axes.x} ->`}
        </text>
      )}
      {axes?.y && (
        <text
          x={16}
          y={(y0 + y1) / 2}
          textAnchor="middle"
          fontFamily={MONO}
          fontSize="10"
          fill={C.comment}
          transform={`rotate(-90 16 ${(y0 + y1) / 2})`}
        >
          {`${axes.y} ->`}
        </text>
      )}
    </Svg>
  );
}
