import { C, MONO, wrapLabel, type DiagramBase } from "./_util";
import { Svg, CenteredText } from "./_shared";

export interface MatrixQuadrant {
  /** Short heading for the quadrant. */
  title: string;
  /** Optional one-line gloss under the heading. */
  note?: string;
}

export interface MatrixProps extends DiagramBase {
  /** The horizontal axis, low value on the left. */
  xAxis: { left: string; right: string; label?: string };
  /** The vertical axis, low value at the bottom. */
  yAxis: { low: string; high: string; label?: string };
  /** Four quadrants in reading order: [top-left, top-right, bottom-left, bottom-right]. */
  quadrants: [MatrixQuadrant, MatrixQuadrant, MatrixQuadrant, MatrixQuadrant];
  /** Index (0-3, same order) of the quadrant to highlight in accent. */
  highlight?: number;
}

/**
 * Two axes, four quadrants: for anything that sorts on two independent dimensions
 * (urgent/important, effort/impact, any typology). The target quadrant is drawn in
 * accent; the rest stay muted.
 */
export function Matrix({
  xAxis,
  yAxis,
  quadrants,
  highlight,
  ariaLabel,
  className,
}: MatrixProps) {
  // Grid geometry. The plotting square sits inside a margin that holds axis labels.
  const gx = 74;
  const gy = 40;
  const gw = 270;
  const gh = 270;
  const midX = gx + gw / 2;
  const midY = gy + gh / 2;
  const cells = [
    { x: gx, y: gy }, // top-left
    { x: midX, y: gy }, // top-right
    { x: gx, y: midY }, // bottom-left
    { x: midX, y: midY }, // bottom-right
  ];

  return (
    <Svg
      viewBox="0 0 384 372"
      ariaLabel={
        ariaLabel ??
        `A two-by-two matrix. Horizontal: ${xAxis.left} to ${xAxis.right}. Vertical: ${yAxis.low} to ${yAxis.high}.`
      }
      className={className}
    >
      {/* quadrant fills */}
      {cells.map((c, i) => {
        const on = highlight === i;
        return (
          <rect
            key={`cell-${i}`}
            x={c.x}
            y={c.y}
            width={gw / 2}
            height={gh / 2}
            fill={on ? C.accent : C.surface2}
            fillOpacity={on ? 0.14 : 1}
            stroke={C.border}
          />
        );
      })}

      {/* emphasized center axes */}
      <line x1={midX} y1={gy} x2={midX} y2={gy + gh} stroke={C.comment} strokeWidth="1.5" />
      <line x1={gx} y1={midY} x2={gx + gw} y2={midY} stroke={C.comment} strokeWidth="1.5" />

      {/* quadrant labels */}
      {cells.map((c, i) => {
        const q = quadrants[i];
        const on = highlight === i;
        const cxq = c.x + gw / 4;
        return (
          <g key={`label-${i}`}>
            <CenteredText
              x={cxq}
              y={c.y + gh / 4 - (q.note ? 8 : 0)}
              lines={wrapLabel(q.title, 15)}
              fill={on ? C.accent : C.fg}
              size={12}
              font={MONO}
              weight={600}
            />
            {q.note && (
              <CenteredText x={cxq} y={c.y + gh / 4 + 18} lines={wrapLabel(q.note, 18)} fill={C.muted} size={9.5} />
            )}
          </g>
        );
      })}

      {/* x-axis pole labels */}
      <text x={gx} y={gy + gh + 20} textAnchor="start" fontFamily={MONO} fontSize="10" fill={C.muted}>
        {xAxis.left}
      </text>
      <text x={gx + gw} y={gy + gh + 20} textAnchor="end" fontFamily={MONO} fontSize="10" fill={C.muted}>
        {xAxis.right}
      </text>
      {xAxis.label && (
        <text x={midX} y={gy + gh + 34} textAnchor="middle" fontFamily={MONO} fontSize="10" fill={C.comment}>
          {`// ${xAxis.label}`}
        </text>
      )}

      {/* y-axis pole labels (rotated) */}
      <text x={gx - 14} y={gy + gh} textAnchor="start" fontFamily={MONO} fontSize="10" fill={C.muted} transform={`rotate(-90 ${gx - 14} ${gy + gh})`}>
        {yAxis.low}
      </text>
      <text x={gx - 14} y={gy} textAnchor="end" fontFamily={MONO} fontSize="10" fill={C.muted} transform={`rotate(-90 ${gx - 14} ${gy})`}>
        {yAxis.high}
      </text>
      {yAxis.label && (
        <text x={gx - 28} y={midY} textAnchor="middle" fontFamily={MONO} fontSize="10" fill={C.comment} transform={`rotate(-90 ${gx - 28} ${midY})`}>
          {`// ${yAxis.label}`}
        </text>
      )}
    </Svg>
  );
}
