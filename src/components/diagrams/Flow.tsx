import { useId } from "react";
import { C, MONO, wrapLabel, type DiagramBase } from "./_util";
import { Svg, CenteredText } from "./_shared";

export interface FlowProps extends DiagramBase {
  /** Ordered steps, left to right. Three or four fit a phone without scrolling. */
  steps: string[];
  /** Index of a step to emphasize in accent. */
  highlight?: number;
  /** Optional fork from the last step into two labeled outcomes. */
  branch?: { up: string; down: string };
}

/**
 * Directed left-to-right stages with a start and an end, for staged methods,
 * decision procedures, and cause-to-effect chains. An optional branch forks the last
 * step into two outcomes.
 */
export function Flow({ steps = [], highlight, branch, ariaLabel, className }: FlowProps) {
  const uid = useId();
  const boxW = 104;
  const gap = 34;
  const boxH = 58;
  const y = branch ? 60 : 90;
  const n = steps.length;
  const width = 20 + n * boxW + (n - 1) * gap + (branch ? boxW + gap + 40 : 20);
  const height = branch ? 200 : 180;
  const xOf = (i: number) => 20 + i * (boxW + gap);
  const lastX = xOf(n - 1);

  return (
    <Svg
      viewBox={`0 0 ${Math.round(width)} ${height}`}
      ariaLabel={ariaLabel ?? `A sequence of steps: ${steps.join(", then ")}.`}
      className={className}
    >
      <defs>
        <marker id={`fl-arw-${uid}`} viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
          <path d="M0,0 L10,5 L0,10 z" fill={C.comment} />
        </marker>
      </defs>

      {steps.map((step, i) => {
        const on = highlight === i;
        const x = xOf(i);
        return (
          <g key={`step-${i}`}>
            {i > 0 && (
              <line
                x1={xOf(i - 1) + boxW}
                y1={y + boxH / 2}
                x2={x}
                y2={y + boxH / 2}
                stroke={C.comment}
                strokeWidth="1.5"
                markerEnd={`url(#fl-arw-${uid})`}
              />
            )}
            <rect
              x={x}
              y={y}
              width={boxW}
              height={boxH}
              rx="7"
              fill={on ? C.accent : C.surface2}
              fillOpacity={on ? 0.14 : 1}
              stroke={on ? C.accent : C.border}
              strokeOpacity={on ? 0.6 : 1}
            />
            <text x={x + 10} y={y + 16} fontFamily={MONO} fontSize="9" fill={C.comment}>
              {String(i + 1).padStart(2, "0")}
            </text>
            <CenteredText
              x={x + boxW / 2}
              y={y + boxH / 2 + 6}
              lines={wrapLabel(step, 13)}
              fill={on ? C.accent : C.fg}
              size={11.5}
              font={MONO}
            />
          </g>
        );
      })}

      {branch && (
        <g>
          {/* fork from the last step */}
          {[
            { label: branch.up, dy: -52, sign: -1 },
            { label: branch.down, dy: 52, sign: 1 },
          ].map((b, i) => {
            const bx = lastX + boxW + gap;
            const by = y + b.dy;
            return (
              <g key={`branch-${i}`}>
                <path
                  d={`M${lastX + boxW},${y + boxH / 2} C${lastX + boxW + gap / 2},${y + boxH / 2} ${lastX + boxW + gap / 2},${by + boxH / 2} ${bx},${by + boxH / 2}`}
                  stroke={C.comment}
                  strokeWidth="1.5"
                  markerEnd={`url(#fl-arw-${uid})`}
                />
                <rect x={bx} y={by} width={boxW} height={boxH} rx="7" fill={C.surface2} stroke={C.border} />
                <CenteredText x={bx + boxW / 2} y={by + boxH / 2 + 4} lines={wrapLabel(b.label, 13)} fill={C.fg} size={11.5} font={MONO} />
              </g>
            );
          })}
        </g>
      )}
    </Svg>
  );
}
