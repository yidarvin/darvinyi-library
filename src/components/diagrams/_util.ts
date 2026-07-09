// _util.ts --- constants, tokens, and pure helpers for the diagram primitives.
//
// Kept separate from the SVG helper components in _shared.tsx so each file exports
// only one kind of thing (constants here, components there) and React Fast Refresh
// stays happy. Colors and fonts resolve to the house tokens in src/styles/tokens.css;
// never hard-code a hex here, so a future retune of the palette is one edit.

/** The house palette, as CSS-variable references. */
export const C = {
  bg: "var(--bg)",
  surface: "var(--surface)",
  surface2: "var(--surface-2)",
  border: "var(--border)",
  fg: "var(--fg)",
  muted: "var(--fg-muted)",
  accent: "var(--accent)",
  accentDim: "var(--accent-dim)",
  comment: "var(--comment)",
} as const;

export const MONO = "var(--font-mono)";
export const SANS = "var(--font-sans)";

/** Shared prop every primitive accepts: an accessible label and an optional class. */
export interface DiagramBase {
  /** Plain-language description for screen readers. A sensible default is derived. */
  ariaLabel?: string;
  /** Extra classes on the root <svg>. Defaults to a full-width, block SVG. */
  className?: string;
}

/** A stable, non-cryptographic string hash, for deterministic per-slug variation. */
export function hash(s: string): number {
  let h = 2166136261;
  for (let i = 0; i < s.length; i += 1) {
    h ^= s.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}

/** Greedy word wrap to a max character count, for multi-word SVG labels. */
export function wrapLabel(label: string, max = 16): string[] {
  const words = label.split(/\s+/).filter(Boolean);
  const lines: string[] = [];
  let cur = "";
  for (const w of words) {
    if (!cur) cur = w;
    else if ((cur + " " + w).length <= max) cur += " " + w;
    else {
      lines.push(cur);
      cur = w;
    }
  }
  if (cur) lines.push(cur);
  return lines.length ? lines : [label];
}
