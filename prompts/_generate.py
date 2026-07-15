#!/usr/bin/env python3
"""Generate the three state files for darvinyi-library from prompts/_books.py.

Emits, matching the darvinyi-refsite-template schema exactly so the repo's own
scripts (validate.py, mark.py) work unmodified:

  content/registry.json   the database: about (num 0) + every book, in build order
  prompts/queue.md        the run list table, same order, all PENDING
  prompts/notes/<slug>.md  a per-book brief the runner reads for "run the next one"

Build order: the launch shelf (STAGE_1) first, then the rest of Tier 1, then
Tier 2, then Tier 3; within a tier, declaration order in _books.py (which is
shelf-grouped) is preserved.

Safe to re-run after editing _books.py:
  - registry.json and queue.md are rewritten, but each slug's existing status is
    carried over, so a re-run never resets progress you have already made.
  - a note file is written only if it does not already exist, so hand-edits to a
    brief survive a re-run. (about.md is bespoke and never touched here.)

Run from the repo root:  python3 prompts/_generate.py
"""
from __future__ import annotations

import json
import os

import _books as B

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
REGISTRY = os.path.join(REPO, "content", "registry.json")
QUEUE = os.path.join(REPO, "prompts", "queue.md")
NOTES_DIR = os.path.join(REPO, "prompts", "notes")

SITE_TITLE = "the library"
SITE_SUBTITLE = "big non-fiction ideas, distilled into prose and diagrams"

ABOUT = dict(id="about", title="About this library", author="", year=0,
             shelf="The system", tier=0, thesis="", model="", flag="")


def year_fmt(year: int) -> str:
    if year == 0:
        return ""
    if year < 0:
        return f"c. {abs(year)} BCE"
    if year < 1000:
        return f"c. {year} CE"
    return str(year)


def subtitle_for(book: dict) -> str:
    if book["id"] == "about":
        return "ideas, not text"
    yf = year_fmt(book["year"])
    return f"{book['author']} \u00b7 {yf}" if yf else book["author"]


def build_order(books: list[dict], stage1: list[str]) -> list[dict]:
    by_id = {b["id"]: b for b in books}
    ordered: list[dict] = []
    seen: set[str] = set()
    for sid in stage1:
        ordered.append(by_id[sid])
        seen.add(sid)
    for tier in (1, 2, 3):
        for b in books:
            if b["id"] in seen or b["tier"] != tier:
                continue
            ordered.append(b)
            seen.add(b["id"])
    return ordered


def existing_status_map() -> dict[str, str]:
    """slug -> registry status, from a prior registry.json if present."""
    if not os.path.exists(REGISTRY):
        return {}
    try:
        with open(REGISTRY, encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, json.JSONDecodeError):
        return {}
    return {c["slug"]: c.get("status", "pending") for c in data.get("chapters", [])}


def write_registry(ordered: list[dict], prior: dict[str, str]) -> None:
    chapters = []
    seq = [ABOUT] + ordered
    for num, b in enumerate(seq):
        chapters.append({
            "num": num,
            "slug": b["id"],
            "title": b["title"],
            "subtitle": subtitle_for(b),
            "part": b["shelf"],
            "routes": [],
            "status": prior.get(b["id"], "pending"),
        })
    data = {
        "title": SITE_TITLE,
        "subtitle": SITE_SUBTITLE,
        "mode": "book",
        "chapters": chapters,
    }
    os.makedirs(os.path.dirname(REGISTRY), exist_ok=True)
    with open(REGISTRY, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


QUEUE_INTRO = """# Run Queue --- the library

Run order, top to bottom. The **next** item is the first `PENDING` row. Statuses:
`PENDING`, `DONE`, `SKIPPED`. Update the status cell after each run. Reorder by
moving rows. Adding a book means adding a `PENDING` row here and a matching entry
in `content/registry.json` (or just add it to `prompts/_books.py` and re-run
`python3 prompts/_generate.py`). See `AGENTS.md` and the `library-runner` skill for
the per-item procedure. A built page becomes `DONE` only after an independent critique.

The first row, `about`, is the bootstrap: building it also builds the library
landing page, the diagram primitive components, and the shared book-page layout.
Run it first. Every row after it is one book. Each book has a brief at
`prompts/notes/<slug>.md`.
"""

QUEUE_COMMENT = """
<!--
Order is: the launch shelf first (highest-reach Tier 1), then the rest of Tier 1,
then Tier 2, then Tier 3. Within a tier, books are grouped by shelf.

A run reads prompts/notes/<slug>.md for the book's brief (thesis, signature model,
any credibility caveat), then follows docs/authoring-spec.md for the page anatomy
and docs/diagram-vocabulary.md for the diagram forms. validate.py checks that this
table and content/registry.json list the same slugs in the same order, so keep
them in sync (or regenerate both with prompts/_generate.py).
-->
"""


def render_table(seq: list[dict], prior: dict[str, str]) -> str:
    header = ["#", "slug", "item", "status"]
    rows = []
    for num, b in enumerate(seq):
        st = prior.get(b["id"], "pending").upper()
        st = "PENDING" if st == "DRAFT" else st
        rows.append([f"{num:03d}", b["id"], b["title"], st])
    widths = [len(h) for h in header]
    for r in rows:
        for c in range(4):
            widths[c] = max(widths[c], len(r[c]))

    def fmt(cells):
        return "| " + " | ".join(cells[c].ljust(widths[c]) for c in range(4)) + " |"

    out = [fmt(header), "|" + "|".join("-" * (widths[c] + 2) for c in range(4)) + "|"]
    for r in rows:
        out.append(fmt(r))
    return "\n".join(out)


def write_queue(ordered: list[dict], prior: dict[str, str]) -> None:
    seq = [ABOUT] + ordered
    table = render_table(seq, prior)
    with open(QUEUE, "w", encoding="utf-8") as fh:
        fh.write(QUEUE_INTRO + "\n" + table + "\n" + QUEUE_COMMENT)


NOTE_TMPL = """# {title}

- **Author:** {author}
- **Year:** {year_fmt}
- **Shelf:** {shelf}
- **Tier:** {tier}
- **Slug / route:** `{slug}`  ->  `/{slug}`

## Thesis to convey

{thesis}

## Signature model

{model_line}

## Build brief

Distill this book into one long scroll following the fixed anatomy in
`docs/authoring-spec.md`: Hero, Thesis, {why_matters}Key Ideas (4 to 7, each with
its own diagram), {model_section}Put It To Work, {wrong_section}If You Remember One
Thing, Shelved Nearby.

Diagrams are the point. Give every key idea a diagram drawn from
`docs/diagram-vocabulary.md`, in house style, as an inline-SVG React component
under `src/components/diagrams/` (compose the primitives the scaffold built; add a
new primitive to the vocabulary first if a concept truly needs one). Vary the forms
across the page. Wrap each diagram in the existing `<Figure>` component with a
one-line caption. "Put It To Work" suits `<ExerciseCard>`.{wrong_component}

Copyright line: distill ideas, never reproduce text or the author's figures. No
close paraphrase. At most one short attributed epigraph, and only if it earns its
place. No real cover art; the scaffold's generated typographic cover is used.

"Shelved Nearby": link only to books already built (status done in the registry),
noting the relationship in a clause. Link out to the real book at a bookseller.

{flag_block}## Done when

Every spine section present and in order; 4 to 7 key ideas each with an in-vocabulary
diagram; the signature model rendered as the hero Model diagram (or Model section
deliberately absent, noted in the registry); house voice with no em dashes and no AI
tells; diagrams legible at 360px and captioned; cross-links resolve; `npm run check`
passes; then flip `{slug}` to done in the registry and DONE in the queue.
"""


def note_for(book: dict) -> str:
    has_model = bool(book["model"])
    model_line = (
        f"**{book['model']}.** Render this as the hero diagram in the Model "
        f"section, in house style, as an original recreation of the idea (never a "
        f"trace of the book's own figure)."
        if has_model else
        "This book has no single signature framework. Skip the Model section rather "
        "than inventing one, and let the Key Ideas diagrams carry the visual load."
    )
    model_section = "The Model (hero diagram of the framework), " if has_model else ""
    flag = book["flag"]
    if flag:
        why_matters = "Why It Matters, "
        wrong_section = "Where People Get It Wrong, "
        wrong_component = " The credibility note below belongs in a `<Callout>`."
        flag_block = (
            "## Where People Get It Wrong (mandatory for this title)\n\n"
            f"{flag}\n\nWrite this as a brief, fair, sourced note in our own words. "
            "Name the criticism plainly and let the reader weigh it. Do not bury it.\n\n"
        )
    else:
        why_matters = ""
        wrong_section = ""
        wrong_component = ""
        flag_block = (
            "## Where People Get It Wrong (optional)\n\n"
            "Include an honest caveats-and-misreadings section if the book has "
            "well-known ones; otherwise omit it.\n\n"
        )
    return NOTE_TMPL.format(
        title=book["title"], author=book["author"], year_fmt=year_fmt(book["year"]),
        shelf=book["shelf"], tier=book["tier"], slug=book["id"], thesis=book["thesis"],
        model_line=model_line, model_section=model_section, why_matters=why_matters,
        wrong_section=wrong_section, wrong_component=wrong_component, flag_block=flag_block,
    )


def write_notes(ordered: list[dict]) -> tuple[int, int]:
    os.makedirs(NOTES_DIR, exist_ok=True)
    written = skipped = 0
    for b in ordered:
        path = os.path.join(NOTES_DIR, f"{b['id']}.md")
        if os.path.exists(path):
            skipped += 1
            continue
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(note_for(b))
        written += 1
    return written, skipped


def main() -> None:
    ordered = build_order(B.BOOKS, B.STAGE_1)
    prior = existing_status_map()
    write_registry(ordered, prior)
    write_queue(ordered, prior)
    w, s = write_notes(ordered)
    print(f"registry.json: 1 about + {len(ordered)} books = {len(ordered) + 1} entries")
    print(f"queue.md: {len(ordered) + 1} rows")
    print(f"notes: {w} written, {s} preserved (already existed)")
    print("launch shelf order:", ", ".join(b["id"] for b in ordered[:len(B.STAGE_1)]))


if __name__ == "__main__":
    main()
