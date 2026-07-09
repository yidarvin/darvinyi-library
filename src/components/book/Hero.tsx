import { BookCover } from "../BookCover";
import { chapterBySlug } from "../../lib/registry";

interface HeroProps {
  /** The book's slug; its title, author/year, and shelf come from the registry. */
  slug: string;
  /** The one-line thesis, in the house voice. */
  thesis: string;
  /** Reading time of the distillation; the book run computes it from rendered length. */
  minutes: number;
  /** Override the author/year line; defaults to the registry subtitle. */
  byline?: string;
}

/**
 * The masthead every book page opens with: the generated cover beside the shelf tag,
 * an "N-min distillation" badge, the author line, and the one-line thesis. The cover
 * carries the title typographically, so this pairs with (and does not fight) the page
 * heading. A light helper, not a framework; the anatomy in docs/authoring-spec.md
 * governs what follows it.
 */
export function Hero({ slug, thesis, minutes, byline }: HeroProps) {
  const meta = chapterBySlug(slug);
  if (!meta) return null;

  return (
    <section className="mb-12 flex flex-col gap-6 sm:flex-row sm:items-stretch">
      <div className="w-36 shrink-0 self-center sm:w-44 sm:self-start">
        <BookCover meta={meta} size="hero" />
      </div>

      <div className="flex flex-1 flex-col justify-center">
        <div className="flex flex-wrap items-center gap-2">
          {meta.part && (
            <span className="rounded border border-border px-2 py-0.5 font-mono text-[0.7rem] text-muted">
              {meta.part}
            </span>
          )}
          <span className="rounded border border-accent/40 bg-accent/10 px-2 py-0.5 font-mono text-[0.7rem] text-accent">
            {`${minutes}-min distillation`}
          </span>
        </div>

        <p className="mt-3 font-mono text-sm text-muted">{byline ?? meta.subtitle}</p>

        <p className="mt-3 text-lg leading-relaxed text-fg">{thesis}</p>
      </div>
    </section>
  );
}
