import { Link } from "react-router";
import { registry, type ChapterMeta } from "../lib/registry";
import { useHead } from "../lib/useHead";
import { Layout } from "../components/Layout";
import { BookCover } from "../components/BookCover";

// Home --- the library. A shelf per `part`, each a grid of generated covers, driven
// entirely from content/registry.json. A built book links to its page; a book still
// in the queue shows as a dimmed, unlinked cover ("in the stacks"), so the whole
// shape of the library is visible from day one and fills in as the queue runs.
export function Home() {
  useHead(registry.title, registry.subtitle);
  const about = registry.chapters.find((c) => c.slug === "about");
  const books = registry.chapters.filter((c) => c.slug !== "about");
  const shelves = groupByPart(books);

  return (
    <Layout>
      <div className="flex items-start justify-between gap-4">
        <div>
          <p className="eyebrow mb-3">library</p>
          <h1 className="font-mono text-3xl font-bold tracking-tight text-fg">{registry.title}</h1>
          <p className="mt-2 max-w-xl text-muted">{registry.subtitle}</p>
        </div>
        {about && (
          <Link to={`/${about.slug}`} className="mt-1 shrink-0 font-mono text-xs text-muted hover:text-accent">
            {about.title}
          </Link>
        )}
      </div>

      <div className="mt-14 space-y-12">
        {shelves.map(({ part, chapters }) => (
          <section key={part ?? "_"}>
            {part && (
              <h2 className="mb-4 font-mono text-xs uppercase tracking-wider text-comment">{`// ${part}`}</h2>
            )}
            <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 md:grid-cols-4">
              {chapters.map((c) => (
                <Shelf key={c.slug} chapter={c} />
              ))}
            </div>
          </section>
        ))}
      </div>
    </Layout>
  );
}

function Shelf({ chapter }: { chapter: ChapterMeta }) {
  const published = chapter.status !== "pending";
  if (published) {
    return (
      <Link to={`/${chapter.slug}`} className="block no-underline transition-opacity hover:opacity-80">
        <BookCover meta={chapter} size="tile" />
      </Link>
    );
  }
  return (
    <div className="cursor-default opacity-45" title="in the stacks">
      <BookCover meta={chapter} size="tile" />
    </div>
  );
}

// Group every book onto its shelf. The registry is ordered by tier then shelf, so a
// shelf recurs across tiers; a real library shows each shelf once with all its books.
// Shelves keep first-appearance order, and books keep registry order within a shelf.
function groupByPart(items: ChapterMeta[]): { part?: string; chapters: ChapterMeta[] }[] {
  const out: { part?: string; chapters: ChapterMeta[] }[] = [];
  const byPart = new Map<string, ChapterMeta[]>();
  for (const item of items) {
    const key = item.part ?? "_";
    let bucket = byPart.get(key);
    if (!bucket) {
      bucket = [];
      byPart.set(key, bucket);
      out.push({ part: item.part, chapters: bucket });
    }
    bucket.push(item);
  }
  return out;
}
