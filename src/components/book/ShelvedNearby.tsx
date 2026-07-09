import { Link } from "react-router";
import { BookCover } from "../BookCover";
import { chapterBySlug } from "../../lib/registry";

interface ShelvedNearbyProps {
  /** Slugs of related books. Only ones already built (draft or done) are linked. */
  related?: string[];
  /** Where to buy the real book (a bookseller). The library links out; it never hosts. */
  buyUrl?: string;
  /** Link text for the outbound link, e.g. "Atomic Habits by James Clear". */
  buyLabel?: string;
}

/**
 * The cross-link footer for a book page: a few related books that are already built,
 * and the outbound link to buy the real book. A reader who wants the book buys it;
 * this library distills ideas and points out.
 */
export function ShelvedNearby({ related = [], buyUrl, buyLabel }: ShelvedNearbyProps) {
  const built = related
    .map((slug) => chapterBySlug(slug))
    .filter((m): m is NonNullable<typeof m> => !!m && m.status !== "pending");

  if (built.length === 0 && !buyUrl) return null;

  return (
    <section className="mt-16 border-t border-border pt-8">
      <p className="eyebrow mb-4">shelved_nearby</p>

      {built.length > 0 && (
        <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
          {built.map((m) => (
            <Link key={m.slug} to={`/${m.slug}`} className="block no-underline hover:opacity-80">
              <BookCover meta={m} size="tile" />
            </Link>
          ))}
        </div>
      )}

      {buyUrl && (
        <p className="mt-6 font-mono text-sm text-muted">
          {"/* want the whole book? */ "}
          <a
            href={buyUrl}
            target="_blank"
            rel="noopener noreferrer"
            aria-label={`${buyLabel ?? "buy it"} (opens in a new tab)`}
          >
            {buyLabel ?? "buy it"}
          </a>
        </p>
      )}
    </section>
  );
}
