import { C, MONO, wrapLabel, type DiagramBase } from "./_util";
import { CenteredText, Svg } from "./_shared";

export interface CoreContextProps extends DiagramBase {
  /** The name of the small, enduring center. */
  coreTitle: string;
  /** Peer elements that belong together inside the core. */
  coreItems: string[];
  /** Elements outside the core that can change independently. */
  contextItems: string[];
  /** Label for the changeable area that surrounds the core. */
  contextTitle?: string;
}

/**
 * A grouped core with peer elements inside a wider, changeable context. Use when
 * a concept has several equally fundamental parts that should not be rendered as
 * nested layers, while the surrounding practices remain open to revision.
 */
export function CoreContext({
  coreTitle,
  coreItems,
  contextItems,
  contextTitle = "changeable context",
  ariaLabel,
  className,
}: CoreContextProps) {
  const itemCount = Math.max(coreItems.length, 1);
  const itemW = Math.min(132, Math.max(94, (270 - (itemCount - 1) * 12) / itemCount));
  const itemsStart = 220 - (itemCount * itemW + (itemCount - 1) * 12) / 2;

  return (
    <Svg
      viewBox="0 0 440 264"
      ariaLabel={
        ariaLabel ??
        `${coreTitle} contains the parallel elements ${coreItems.join(", ")}. Outside it, ${contextTitle} includes ${contextItems.join(", ")}.`
      }
      className={className}
    >
      <rect x="18" y="18" width="404" height="228" rx="12" fill={C.surface} stroke={C.border} />
      <text x="38" y="47" fontFamily={MONO} fontSize="11" fill={C.comment}>
        {`// ${contextTitle}`}
      </text>

      <rect x="74" y="72" width="292" height="130" rx="10" fill={C.surface2} stroke={C.accent} strokeOpacity="0.7" strokeWidth="1.5" />
      <text x="220" y="99" textAnchor="middle" fontFamily={MONO} fontSize="12" fontWeight="600" fill={C.accent}>
        {coreTitle}
      </text>

      {coreItems.map((item, i) => {
        const x = itemsStart + i * (itemW + 12);
        return (
          <g key={item}>
            <rect x={x} y="120" width={itemW} height="58" rx="7" fill={C.surface} stroke={C.border} />
            <CenteredText x={x + itemW / 2} y={149} lines={wrapLabel(item, 16)} fill={C.fg} size={11.5} font={MONO} />
          </g>
        );
      })}

      {contextItems.map((item, i) => {
        const positions = [
          { x: 46, y: 64 },
          { x: 272, y: 64 },
          { x: 46, y: 228 },
          { x: 272, y: 228 },
        ];
        const position = positions[i % positions.length];
        return (
          <text key={item} x={position.x} y={position.y} fontFamily={MONO} fontSize="10" fill={C.muted}>
            {item}
          </text>
        );
      })}
    </Svg>
  );
}
