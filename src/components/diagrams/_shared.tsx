// _shared.tsx --- the SVG helper components shared by the diagram primitives.
//
// Constants, tokens, and pure helpers live in _util.ts; this file exports only
// components so React Fast Refresh stays happy. Every primitive is hand-authored
// inline SVG returned from a React component: no diagramming or charting library, no
// D3. Diagrams are built to read at 360px wide, so keep viewBoxes modest and labels
// in the mono face at a legible size.
import type { ReactNode } from "react";
import { C, MONO } from "./_util";

/**
 * The root <svg> for a primitive: sets the viewBox, the accessible role/label, and
 * the default full-width sizing so a figure scrolls (never shrinks illegibly) on a
 * phone. Children are the diagram body.
 */
export function Svg({
  viewBox,
  ariaLabel,
  className,
  children,
}: {
  viewBox: string;
  ariaLabel: string;
  className?: string;
  children: ReactNode;
}) {
  return (
    <svg
      viewBox={viewBox}
      className={className ?? "block w-full"}
      role="img"
      aria-label={ariaLabel}
      fill="none"
    >
      {children}
    </svg>
  );
}

/**
 * Centered, optionally multi-line text block. Lines stack around `y` so the whole
 * block stays vertically centered on it.
 */
export function CenteredText({
  x,
  y,
  lines,
  fill = C.fg,
  size = 12,
  font = MONO,
  weight,
  lineHeight = 1.25,
}: {
  x: number;
  y: number;
  lines: string[];
  fill?: string;
  size?: number;
  font?: string;
  weight?: number | string;
  lineHeight?: number;
}) {
  const step = size * lineHeight;
  const start = y - ((lines.length - 1) * step) / 2;
  return (
    <text
      x={x}
      textAnchor="middle"
      fontFamily={font}
      fontSize={size}
      fontWeight={weight}
      fill={fill}
    >
      {lines.map((ln, i) => (
        <tspan key={i} x={x} y={start + i * step}>
          {ln}
        </tspan>
      ))}
    </text>
  );
}
