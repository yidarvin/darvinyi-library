import { useId } from "react";
import { C, MONO, wrapLabel, type DiagramBase } from "./_util";
import { Svg, CenteredText } from "./_shared";

export interface GraphNode {
  id: string;
  label: string;
  /** Optional placement in a 0-to-1 box; omit to auto-arrange on a ring. */
  x?: number;
  y?: number;
}

export interface GraphEdge {
  from: string;
  to: string;
  /** Reinforcing edges draw in accent with a plus; balancing edges dash with a minus. */
  kind?: "reinforcing" | "balancing";
}

export interface NodeGraphProps extends DiagramBase {
  nodes: GraphNode[];
  edges: GraphEdge[];
}

/**
 * Nodes connected by edges, non-hierarchical: for network effects and system maps
 * where parts feed back on each other. Kept sparse on purpose; this is a concept
 * sketch, not a full stocks-and-flows model.
 */
export function NodeGraph({ nodes = [], edges = [], ariaLabel, className }: NodeGraphProps) {
  const uid = useId();
  const cx = 190;
  const cy = 162;
  const R = 116;
  const n = Math.max(nodes.length, 1);

  const pos = (node: GraphNode, i: number): [number, number] => {
    if (typeof node.x === "number" && typeof node.y === "number") {
      return [47 + node.x * 286, 34 + node.y * 256];
    }
    const a = (-90 + (i * 360) / n) * (Math.PI / 180);
    return [cx + R * Math.cos(a), cy + R * Math.sin(a)];
  };

  const points = new Map<string, [number, number]>();
  nodes.forEach((node, i) => points.set(node.id, pos(node, i)));

  const nodeW = 94;
  const nodeH = 40;

  return (
    <Svg
      viewBox="0 0 380 324"
      ariaLabel={ariaLabel ?? `A network of ${n} nodes: ${nodes.map((x) => x.label).join(", ")}.`}
      className={className}
    >
      <defs>
        <marker id={`ng-arw-${uid}`} viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
          <path d="M0,0 L10,5 L0,10 z" fill={C.comment} />
        </marker>
        <marker id={`ng-arwA-${uid}`} viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
          <path d="M0,0 L10,5 L0,10 z" fill={C.accent} />
        </marker>
      </defs>

      {/* edges */}
      {edges.map((e, i) => {
        const a = points.get(e.from);
        const b = points.get(e.to);
        if (!a || !b) return null;
        const dx = b[0] - a[0];
        const dy = b[1] - a[1];
        const len = Math.hypot(dx, dy) || 1;
        const ux = dx / len;
        const uy = dy / len;
        // shorten both ends so the line meets node edges, not centers
        const sx = a[0] + ux * 50;
        const sy = a[1] + uy * 26;
        const ex = b[0] - ux * 50;
        const ey = b[1] - uy * 26;
        const rein = e.kind === "reinforcing";
        const bal = e.kind === "balancing";
        return (
          <g key={`edge-${i}`}>
            <line
              x1={sx}
              y1={sy}
              x2={ex}
              y2={ey}
              stroke={rein ? C.accent : C.comment}
              strokeWidth={rein ? 1.8 : 1.4}
              strokeDasharray={bal ? "5 3" : undefined}
              markerEnd={`url(#${rein ? `ng-arwA-${uid}` : `ng-arw-${uid}`})`}
            />
            {(rein || bal) && (
              <text
                x={(sx + ex) / 2}
                y={(sy + ey) / 2 - 4}
                textAnchor="middle"
                fontFamily={MONO}
                fontSize="12"
                fill={rein ? C.accent : C.comment}
              >
                {rein ? "+" : "−"}
              </text>
            )}
          </g>
        );
      })}

      {/* nodes */}
      {nodes.map((node, i) => {
        const [x, y] = pos(node, i);
        return (
          <g key={node.id}>
            <rect x={x - nodeW / 2} y={y - nodeH / 2} width={nodeW} height={nodeH} rx="7" fill={C.surface2} stroke={C.accent} strokeOpacity="0.5" />
            <CenteredText x={x} y={y} lines={wrapLabel(node.label, 13)} fill={C.fg} size={11} font={MONO} />
          </g>
        );
      })}
    </Svg>
  );
}
