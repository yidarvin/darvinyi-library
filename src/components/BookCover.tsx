import { hash } from "./diagrams/_util";

export interface BookCoverMeta {
  slug: string;
  title: string;
  /** Usually "Author · Year". */
  subtitle?: string;
  /** The shelf. */
  part?: string;
}

interface BookCoverProps {
  meta: BookCoverMeta;
  /** "tile" for the library grid, "hero" for the top of a book page. */
  size?: "tile" | "hero";
  className?: string;
}

// A bounded set of code-comment glyphs. Which one a book gets is derived from its
// slug, so every cover is deterministic (the same book always renders the same
// cover) while the grid stays varied. All variation stays inside the palette.
const GLYPHS = ["{ }", "//", "< >", "[ ]", "::", "=>", "*", "~", "#", "&&", "()", "|>"];

/**
 * A generated, typographic book cover: teal-on-near-black, JetBrains Mono, no image
 * and no real cover art, ever. Deterministic from the book's registry meta. The teal
 * stays the one loud thing (a spine and a single glyph); the title is quiet so a full
 * shelf of covers does not shout. Works at grid-tile size and at hero size.
 */
export function BookCover({ meta, size = "tile", className }: BookCoverProps) {
  const h = hash(meta.slug);
  const glyph = GLYPHS[h % GLYPHS.length];
  // Two teal shades, both in-palette; picked deterministically per slug.
  const accent = (h >> 5) % 2 === 0 ? "var(--accent)" : "var(--accent-dim)";
  const hero = size === "hero";

  return (
    <div
      className={`relative flex aspect-[3/4] flex-col justify-between overflow-hidden rounded-md border border-border bg-surface ${hero ? "p-5" : "p-3"} ${className ?? ""}`}
      style={{ borderLeft: `${hero ? 3 : 2}px solid ${accent}` }}
    >
      <div className="flex items-start justify-between gap-2">
        {meta.part && (
          <span className={`truncate font-mono ${hero ? "text-[0.7rem]" : "text-[0.6rem]"} text-comment`}>
            {`// ${meta.part}`}
          </span>
        )}
        <span
          aria-hidden="true"
          className={`shrink-0 font-mono ${hero ? "text-base" : "text-sm"}`}
          style={{ color: accent, opacity: 0.7 }}
        >
          {glyph}
        </span>
      </div>

      <div>
        <div
          className={`font-mono font-semibold leading-tight text-fg ${hero ? "text-xl" : "text-[0.9rem]"}`}
          style={{
            display: "-webkit-box",
            WebkitBoxOrient: "vertical",
            WebkitLineClamp: hero ? 5 : 4,
            overflow: "hidden",
          }}
        >
          {meta.title}
        </div>
        {meta.subtitle && (
          <div className={`mt-1.5 truncate font-mono ${hero ? "text-xs" : "text-[0.62rem]"} text-muted`}>
            {meta.subtitle}
          </div>
        )}
      </div>
    </div>
  );
}
