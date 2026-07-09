import { C, MONO, SANS, wrapLabel, type DiagramBase } from "./_util";
import { Svg } from "./_shared";

export interface ComparePanel {
  title: string;
  points: string[];
}

export interface CompareProps extends DiagramBase {
  left: ComparePanel;
  right: ComparePanel;
  /** Which panel to favor with the accent. Defaults to the right. */
  favor?: "left" | "right" | "none";
}

/**
 * Two side-by-side panels contrasting two states or approaches: System 1 versus
 * System 2, before and after, positions versus interests. The panels are kept
 * visually parallel so the contrast reads at a glance.
 */
export function Compare({
  left = { title: "", points: [] },
  right = { title: "", points: [] },
  favor = "right",
  ariaLabel,
  className,
}: CompareProps) {
  const panelW = 168;
  const gapX = 20;
  const x0 = 8;
  const x1 = x0 + panelW + gapX;
  const top = 12;
  const rows = Math.max(left.points.length, right.points.length);
  const headerH = 40;
  const rowH = 34;
  const height = top * 2 + headerH + rows * rowH + 6;

  const panel = (p: ComparePanel, x: number, accent: boolean) => (
    <g>
      <rect
        x={x}
        y={top}
        width={panelW}
        height={headerH + rows * rowH + 6}
        rx="8"
        fill={accent ? C.accent : C.surface2}
        fillOpacity={accent ? 0.1 : 1}
        stroke={accent ? C.accent : C.border}
        strokeOpacity={accent ? 0.5 : 1}
      />
      <text x={x + 14} y={top + 25} fontFamily={MONO} fontSize="13" fontWeight={600} fill={accent ? C.accent : C.fg}>
        {p.title}
      </text>
      <line x1={x + 12} y1={top + headerH} x2={x + panelW - 12} y2={top + headerH} stroke={C.border} />
      {p.points.map((pt, i) => {
        const lines = wrapLabel(pt, 24);
        return (
          <g key={i}>
            <circle cx={x + 18} cy={top + headerH + i * rowH + 15} r="2.5" fill={accent ? C.accent : C.comment} />
            <text x={x + 28} y={top + headerH + i * rowH + 19} fontFamily={SANS} fontSize="11" fill={accent ? C.fg : C.muted}>
              {lines.map((ln, li) => (
                <tspan key={li} x={x + 28} dy={li === 0 ? 0 : 12}>
                  {ln}
                </tspan>
              ))}
            </text>
          </g>
        );
      })}
    </g>
  );

  return (
    <Svg
      viewBox={`0 0 384 ${Math.round(height)}`}
      ariaLabel={ariaLabel ?? `A comparison of ${left.title} versus ${right.title}.`}
      className={className}
    >
      {panel(left, x0, favor === "left")}
      {panel(right, x1, favor === "right")}
      <text x={x0 + panelW + gapX / 2} y={top + headerH / 2 + 4} textAnchor="middle" fontFamily={MONO} fontSize="11" fill={C.comment}>
        vs
      </text>
    </Svg>
  );
}
