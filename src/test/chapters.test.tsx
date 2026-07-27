import type { ComponentType } from "react";
import { afterEach, describe, it, expect } from "vitest";
import { cleanup, render, screen, waitFor } from "@testing-library/react";
import { MemoryRouter } from "react-router";
import { MDXProvider } from "@mdx-js/react";
import { mdxComponents } from "../components/mdxComponents";
import { AppRoutes } from "../App";
import { CoreContext, Matrix, NodeGraph, Spectrum } from "../components/diagrams";
import { registry } from "../lib/registry";

// Every MDX module on disk, regardless of registry status. The chapter being built
// is still `pending` at verify time, so scoping by status would skip exactly the
// one that matters. The build already compiles all on-disk MDX; this asserts they
// also render, which is the gap `vite build` cannot cover.
const mdxModules = import.meta.glob("../chapters/*.mdx") as Record<
  string,
  () => Promise<{ default: ComponentType<Record<string, unknown>> }>
>;

const published = registry.chapters.filter((c) => c.status !== "pending");

// Vitest does not expose a global afterEach hook to Testing Library's automatic
// cleanup in this configuration. Remove each rendered chapter before the next
// integration test so the home-page query sees only the page it renders.
afterEach(cleanup);

describe("every MDX module renders directly", () => {
  for (const [path, load] of Object.entries(mdxModules)) {
    it(`renders ${path}`, async () => {
      const mod = await load();
      const Body = mod.default;
      // No ErrorBoundary here, so a widget or figure that throws at render fails loud.
      expect(() =>
        render(
          <MemoryRouter>
            <MDXProvider components={mdxComponents}>
              <Body />
            </MDXProvider>
          </MemoryRouter>,
        ),
      ).not.toThrow();
    });
  }
});

describe("every published chapter renders at its route", () => {
  for (const chapter of published) {
    it(`route /${chapter.slug}`, async () => {
      render(
        <MDXProvider components={mdxComponents}>
          <MemoryRouter initialEntries={[`/${chapter.slug}`]}>
            <AppRoutes />
          </MemoryRouter>
        </MDXProvider>,
      );
      // Wait until the lazy body has resolved: the Suspense fallback is gone whether
      // the body rendered or threw into the ErrorBoundary. Asserting before this (the
      // title alone lives in the always-present header) would let a swallowed widget
      // crash slip through.
      await waitFor(() => expect(screen.queryByText("// loading...")).toBeNull());
      // The title renders.
      expect(screen.getAllByText(chapter.title).length).toBeGreaterThan(0);
      // The ErrorBoundary fallback must be absent, or a crash was swallowed.
      expect(screen.queryByText(/chapter failed to render/i)).toBeNull();
    });
  }
});

describe("registry and modules line up", () => {
  it("every published chapter has an mdx module", () => {
    const slugs = new Set(
      Object.keys(mdxModules).map((p) => p.split("/").pop()!.replace(/\.mdx$/, "")),
    );
    for (const chapter of published) {
      expect(slugs.has(chapter.slug)).toBe(true);
    }
  });

  // This is intentionally a whole-library integration test. Give its async route
  // rendering a budget that scales beyond Vitest's 5-second unit-test default.
  it("home lists every chapter title", async () => {
    render(
      <MDXProvider components={mdxComponents}>
        <MemoryRouter initialEntries={["/"]}>
          <AppRoutes />
        </MemoryRouter>
      </MDXProvider>,
    );
    for (const chapter of registry.chapters) {
      expect(await screen.findAllByText(chapter.title)).not.toHaveLength(0);
    }
  }, 15_000);
});

describe("NodeGraph", () => {
  it("keeps arrow endpoints clear of the cards they connect", () => {
    const { container } = render(
      <NodeGraph
        ariaLabel="A directional handoff."
        nodes={[
          { id: "from", label: "from", x: 0, y: 0.5 },
          { id: "to", label: "to", x: 1, y: 0.5 },
        ]}
        edges={[{ from: "from", to: "to", label: "handoff" }]}
      />,
    );

    const edge = container.querySelector("line");
    expect(edge).not.toBeNull();
    expect(Number(edge!.getAttribute("x1"))).toBeGreaterThan(94);
    expect(Number(edge!.getAttribute("x2"))).toBeLessThan(286);
  });

  it("can show neutral connections without implying direction", () => {
    const { container } = render(
      <NodeGraph
        ariaLabel="A neutral relationship map."
        directed={false}
        nodes={[
          { id: "center", label: "center", x: 0.5, y: 0.5 },
          { id: "peer", label: "peer", x: 0.5, y: 0.1 },
        ]}
        edges={[{ from: "center", to: "peer" }]}
      />,
    );

    expect(container.querySelector("line")?.getAttribute("marker-end")).toBeNull();
  });
});

describe("CoreContext", () => {
  it("keeps three peer core items inside the inner frame", () => {
    const { container } = render(
      <CoreContext
        coreTitle="three moves"
        coreItems={["retrieval", "spacing", "interleaving"]}
        contextItems={["feedback"]}
      />,
    );

    const cards = Array.from(container.querySelectorAll<SVGRectElement>("[data-core-item]"));
    expect(cards).toHaveLength(3);
    for (const card of cards) {
      const x = Number(card.getAttribute("x"));
      const width = Number(card.getAttribute("width"));
      expect(x).toBeGreaterThanOrEqual(74);
      expect(x + width).toBeLessThanOrEqual(366);
    }
  });

  it("lays out four peer core items inside the core rather than as a hierarchy", () => {
    const { container } = render(
      <CoreContext
        coreTitle="four standards"
        coreItems={["judgment", "restraint", "courage", "fairness"]}
        contextItems={["conditions"]}
      />,
    );

    const cards = Array.from(container.querySelectorAll<SVGRectElement>("[data-core-item]"));
    expect(cards).toHaveLength(4);
    expect(new Set(cards.map((card) => card.getAttribute("y"))).size).toBe(2);
    for (const card of cards) {
      const x = Number(card.getAttribute("x"));
      const y = Number(card.getAttribute("y"));
      const width = Number(card.getAttribute("width"));
      const height = Number(card.getAttribute("height"));
      expect(x).toBeGreaterThanOrEqual(74);
      expect(x + width).toBeLessThanOrEqual(366);
      expect(y).toBeGreaterThanOrEqual(72);
      expect(y + height).toBeLessThanOrEqual(216);
    }
  });
});

describe("Spectrum", () => {
  it("can keep both endpoints neutral when a middle zone is the target", () => {
    const { container } = render(
      <Spectrum left="blocked" right="unrelated" emphasizeEndpoint="none" />,
    );

    expect(container.querySelector("linearGradient")).toBeNull();
    for (const endpoint of container.querySelectorAll("circle")) {
      expect(endpoint.getAttribute("fill")).toBe("var(--comment)");
    }
  });
});

describe("Matrix", () => {
  it("can emphasize peer quadrants when the target is not one pace or endpoint", () => {
    const { container } = render(
      <Matrix
        xAxis={{ left: "slower", right: "faster" }}
        yAxis={{ low: "more strain", high: "less strain" }}
        quadrants={[{ title: "a" }, { title: "b" }, { title: "c" }, { title: "d" }]}
        highlights={[0, 1]}
      />,
    );

    const cells = container.querySelectorAll("rect");
    expect(cells[0].getAttribute("fill")).toBe("var(--accent)");
    expect(cells[1].getAttribute("fill")).toBe("var(--accent)");
    expect(cells[2].getAttribute("fill")).toBe("var(--surface-2)");
    expect(cells[3].getAttribute("fill")).toBe("var(--surface-2)");
  });
});
