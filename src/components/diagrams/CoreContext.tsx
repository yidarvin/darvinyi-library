import { C, MONO, wrapLabel, type DiagramBase } from "./_util";
import { CenteredText, Svg } from "./_shared";

export interface CoreContextProps extends DiagramBase {
  /** The name of the small, enduring center. */
  coreTitle: string;
  /** Optional peer elements that belong together inside the core. */
  coreItems: string[];
  /** Elements outside the core that can change independently. */
  contextItems: string[];
  /** Label for the changeable area that surrounds the core. */
  contextTitle?: string;
}

/**
 * An enduring center, optionally with peer elements, inside a wider changeable
 * context. Use when the core must stay distinct from revisable surrounding measures
 * or practices, without rendering either as nested layers or prerequisites.
 */
export function CoreContext({
  coreTitle,
  coreItems,
  contextItems,
  contextTitle = "changeable context",
  ariaLabel,
  className,
}: CoreContextProps) {
  const hasCoreItems = coreItems.length > 0;
  const itemCount = Math.max(coreItems.length, 1);
  const grid = itemCount > 3;
  const gridColumns = 2;
  const gridRows = grid ? Math.ceil(itemCount / gridColumns) : 1;
  const itemW = grid
    ? 122
    : Math.min(132, Math.max(82, (270 - (itemCount - 1) * 12) / itemCount));
  const itemH = grid ? 44 : 58;
  const itemGapY = grid ? 10 : 0;
  const itemsStart = grid ? 92 : 220 - (itemCount * itemW + (itemCount - 1) * 12) / 2;
  const coreHeight = grid ? 48 + gridRows * itemH + (gridRows - 1) * itemGapY + 16 : 130;
  const coreBottom = 72 + coreHeight;
  const diagramHeight = grid ? coreBottom + 54 : 264;

  return (
    <Svg
      viewBox={`0 0 440 ${diagramHeight}`}
      ariaLabel={
        ariaLabel ??
        (hasCoreItems
          ? `${coreTitle} contains the parallel elements ${coreItems.join(", ")}.`
          : `${coreTitle} remains stable.`) +
          ` Outside it, ${contextTitle} includes ${contextItems.join(", ")}.`
      }
      className={className}
    >
      <rect x="18" y="18" width="404" height={diagramHeight - 36} rx="12" fill={C.surface} stroke={C.border} />
      <text x="38" y="47" fontFamily={MONO} fontSize="11" fill={C.comment}>
        {`// ${contextTitle}`}
      </text>

      <rect x="74" y="72" width="292" height={coreHeight} rx="10" fill={C.surface2} stroke={C.accent} strokeOpacity="0.7" strokeWidth="1.5" />
      <text x="220" y={hasCoreItems ? 99 : 146} textAnchor="middle" fontFamily={MONO} fontSize="12" fontWeight="600" fill={C.accent}>
        {coreTitle}
      </text>

      {coreItems.map((item, i) => {
        const col = grid ? i % gridColumns : i;
        const row = grid ? Math.floor(i / gridColumns) : 0;
        const x = itemsStart + col * (itemW + 12);
        const y = grid ? 118 + row * (itemH + itemGapY) : 120;
        return (
          <g key={item}>
            <rect data-core-item="true" x={x} y={y} width={itemW} height={itemH} rx="7" fill={C.surface} stroke={C.border} />
            <CenteredText x={x + itemW / 2} y={y + itemH / 2} lines={wrapLabel(item, 16)} fill={C.fg} size={11.5} font={MONO} />
          </g>
        );
      })}

      {contextItems.map((item, i) => {
        const positions = [
          { x: 46, y: 64 },
          { x: 272, y: 64 },
          { x: 46, y: diagramHeight - 36 },
          { x: 272, y: diagramHeight - 36 },
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
