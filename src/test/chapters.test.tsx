import type { ComponentType } from "react";
import { afterEach, describe, it, expect } from "vitest";
import { cleanup, render, screen, waitFor } from "@testing-library/react";
import { MemoryRouter } from "react-router";
import { MDXProvider } from "@mdx-js/react";
import { mdxComponents } from "../components/mdxComponents";
import { AppRoutes } from "../App";
import { Bars, CoreContext, Curve, Matrix, NodeGraph, Pyramid, Spectrum } from "../components/diagrams";
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

describe("Bars", () => {
  it("keeps long value annotations inside the fixed viewport", () => {
    const { container } = render(
      <Bars
        items={[
          { label: "one broad impression", value: 0.92, valueLabel: "more room for drift" },
          { label: "separate criteria", value: 0.62, valueLabel: "make reasons visible" },
          { label: "independent judgments", value: 0.42, valueLabel: "avoid a shared anchor" },
        ]}
      />,
    );

    const annotations = Array.from(container.querySelectorAll<SVGTSpanElement>("[data-bar-annotation] tspan"));
    expect(annotations).toHaveLength(3);
    for (const annotation of annotations) {
      expect(Number(annotation.getAttribute("x"))).toBe(136);
      expect(annotation.textContent!.length).toBeLessThanOrEqual(30);
    }
  });
});

describe("Noise audit flow", () => {
  it("keeps the four-step audit at its readable width instead of shrinking on a phone", async () => {
    const mod = await mdxModules["../chapters/noise.mdx"]();
    const Noise = mod.default;
    render(
      <MemoryRouter>
        <MDXProvider components={mdxComponents}>
          <Noise />
        </MDXProvider>
      </MemoryRouter>,
    );

    const caption = screen.getByText(/A noise audit turns an impression of inconsistency/i);
    const figure = caption.closest("figure");
    const flow = figure?.querySelector("svg");

    expect(flow).not.toBeNull();
    expect(flow?.getAttribute("viewBox")).toBe("0 0 558 180");
    expect(flow?.getAttribute("class")).toContain("min-w-[558px]");
  });
});

describe("The Tao of Pooh mobile flow", () => {
  it("keeps its four-step fitting-action flow at its readable native width", async () => {
    const mod = await mdxModules["../chapters/tao-of-pooh.mdx"]();
    const TaoOfPooh = mod.default;
    render(
      <MemoryRouter>
        <MDXProvider components={mdxComponents}>
          <TaoOfPooh />
        </MDXProvider>
      </MemoryRouter>,
    );

    const caption = screen.getByText(/A fitting action begins with conditions/i);
    const flow = caption.closest("figure")?.querySelector("svg");

    expect(flow).not.toBeNull();
    expect(flow?.getAttribute("viewBox")).toBe("0 0 558 180");
    expect(flow?.getAttribute("class")).toContain("min-w-[558px]");
  });
});

describe("The Demon-Haunted World figure regressions", () => {
  it("keeps its confidence, inquiry, and detection-kit diagrams semantically and visually distinct", async () => {
    const compactText = (value: string | null | undefined) => (value ?? "").replace(/\s+/g, "");
    const mod = await mdxModules["../chapters/demon-haunted-world.mdx"]();
    const DemonHauntedWorld = mod.default;
    render(
      <MemoryRouter>
        <MDXProvider components={mdxComponents}>
          <DemonHauntedWorld />
        </MDXProvider>
      </MemoryRouter>,
    );

    const confidenceFigure = screen.getByText(/Confidence should rise with checked support/i).closest("figure");
    expect(confidenceFigure?.textContent).toContain("very tentative");
    expect(compactText(confidenceFigure?.textContent)).toContain(compactText("well supported, still revisable"));
    expect(confidenceFigure?.textContent).not.toContain("cost of being wrong");

    const independentCheckFigure = screen.getByText(/Independent checks can confirm a prediction/i).closest("figure");
    expect(compactText(independentCheckFigure?.textContent)).toContain(compactText("prediction agrees"));
    expect(compactText(independentCheckFigure?.textContent)).toContain(compactText("conflict found"));
    expect(independentCheckFigure?.textContent).not.toMatch(/[+−]/);

    const inquiryFigure = screen.getByText(/Inquiry stays open to possibilities/i).closest("figure");
    expect(inquiryFigure?.querySelector('[data-spectrum-endpoints="stacked"]')).not.toBeNull();
    expect(screen.getByText("curious, testable inquiry").getAttribute("y")).toBe("24");

    const kitFigure = screen.getByText(/The kit turns an appealing claim/i).closest("figure");
    const kit = kitFigure?.querySelector("svg");
    expect(kit?.getAttribute("viewBox")).toBe("0 0 992 200");
    expect(kit?.getAttribute("class")).toContain("min-w-[992px]");
    expect(compactText(kitFigure?.textContent)).toContain(compactText("name the losing result"));
    expect(compactText(kitFigure?.textContent)).toContain(compactText("seek an independent test"));
  });
});

describe("Silent Spring mobile figures", () => {
  it("keeps the two five-step flows and five-segment timeline at readable widths", async () => {
    const mod = await mdxModules["../chapters/silent-spring.mdx"]();
    const SilentSpring = mod.default;
    render(
      <MemoryRouter>
        <MDXProvider components={mdxComponents}>
          <SilentSpring />
        </MDXProvider>
      </MemoryRouter>,
    );

    const persistenceFigure = screen
      .getByText(/Persistence keeps a chemical available/i)
      .closest("figure");
    const decisionFigure = screen
      .getByText(/A sound response moves from observation/i)
      .closest("figure");
    const timelineFigure = screen
      .getByText(/Carson's warning helped connect ecological evidence/i)
      .closest("figure");

    for (const [figure, viewBox, minWidth] of [
      [persistenceFigure, "0 0 696 180", "min-w-[696px]"],
      [decisionFigure, "0 0 696 180", "min-w-[696px]"],
      [timelineFigure, "0 0 656 168", "min-w-[656px]"],
    ] as const) {
      const svg = figure?.querySelector("svg");
      expect(svg?.getAttribute("viewBox")).toBe(viewBox);
      expect(svg?.getAttribute("class")).toContain(minWidth);
      expect(figure?.querySelector(".overflow-x-auto")).not.toBeNull();
    }
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

  it("describes an empty core as stable rather than as a container", () => {
    const { container } = render(
      <CoreContext
        coreTitle="inherent worth"
        coreItems={[]}
        contextTitle="things that can change"
        contextItems={["feedback", "skill", "outcome", "approval"]}
      />,
    );

    const svg = container.querySelector("svg");
    expect(svg?.getAttribute("aria-label")).toBe(
      "inherent worth remains stable. Outside it, things that can change includes feedback, skill, outcome, approval.",
    );
    expect(container.querySelectorAll("[data-core-item]")).toHaveLength(0);
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

  it("can stack long endpoints above the track without colliding with a top marker label", () => {
    const { container } = render(
      <Spectrum
        left="one surprise means borrowing"
        right="an interruption has a cash buffer"
        marker={0.42}
        markerLabel="starter reserve"
        markerLabelPlacement="top"
        endpointLabelLayout="stacked"
      />,
    );

    const endpoints = container.querySelector('[data-spectrum-endpoints="stacked"]');
    const endpointLines = endpoints?.querySelectorAll("tspan");
    const marker = screen.getByText("starter reserve");

    expect(endpointLines).toHaveLength(4);
    for (const line of endpointLines ?? []) {
      expect(Number(line.getAttribute("y"))).toBeGreaterThan(30);
    }
    expect(Number(marker.getAttribute("y"))).toBe(24);
  });

  it("keeps a top marker label clear of inline endpoints", () => {
    const { container } = render(
      <Spectrum
        left="waiting to speak"
        right="building a shared account"
        marker={0.72}
        markerLabel="reflect, then ask"
        markerLabelPlacement="top"
      />,
    );

    const endpoints = container.querySelector('[data-spectrum-endpoints="inline"]');
    const marker = screen.getByText("reflect, then ask");

    expect(endpoints?.textContent).toContain("building a shared account");
    expect(Number(marker.getAttribute("y"))).toBe(24);
    expect(endpoints?.querySelectorAll("text")[1]?.getAttribute("y")).toBe("74");
  });
});

describe("Gödel, Escher, Bach figure regressions", () => {
  it("teaches the three-domain analogy and separates the self-reference spectrum labels", async () => {
    const mod = await mdxModules["../chapters/godel-escher-bach.mdx"]();
    const GodelEscherBach = mod.default;
    render(
      <MemoryRouter>
        <MDXProvider components={mdxComponents}>
          <GodelEscherBach />
        </MDXProvider>
      </MemoryRouter>,
    );

    const analogyFigure = screen
      .getByText(/Logic, visual art, and music each show a pattern becoming intelligible/i)
      .closest("figure");
    expect(analogyFigure?.querySelector("svg")?.getAttribute("aria-label")).toBe(
      "Logic, visual art, and music connect to a shared pattern that returns at another level.",
    );

    const spectrumFigure = screen
      .getByText(/Feedback becomes self-reference when a system can use a representation/i)
      .closest("figure");
    expect(spectrumFigure?.querySelector('[data-spectrum-endpoints="stacked"]')).not.toBeNull();
    const spectrum = spectrumFigure?.querySelector("svg");
    expect(spectrum?.getAttribute("class")).toContain("min-w-[440px]");
    expect(spectrumFigure?.querySelector(".overflow-x-auto")).not.toBeNull();
    expect(spectrum?.textContent).toContain("repetition");
    expect(spectrum?.textContent).toContain("self-reference");
    expect(screen.getByText("symbolic feedback").getAttribute("y")).toBe("24");
  });
});

describe("Curve", () => {
  it("shows both quantities and their named intersection for a crossover", () => {
    const { container } = render(
      <Curve
        shape="crossover"
        axes={{ x: "saving and time", y: "monthly cash flow" }}
      />,
    );

    expect(container.querySelector('[data-curve-series="independent-income"]')).not.toBeNull();
    expect(container.querySelector('[data-curve-series="recurring-expenses"]')).not.toBeNull();
    expect(container.querySelector("[data-crossover-point]")).not.toBeNull();
    expect(container.textContent).toContain("crossover");
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

describe("Pyramid", () => {
  it("renders the first tier as the wide base and the last tier as the narrow apex", () => {
    const { container } = render(
      <Pyramid
        tiers={[
          { label: "base" },
          { label: "middle" },
          { label: "apex" },
        ]}
      />,
    );

    const tiers = Array.from(container.querySelectorAll<SVGRectElement>("svg > g > rect"));
    expect(tiers).toHaveLength(3);
    expect(Number(tiers[0].getAttribute("y"))).toBeGreaterThan(Number(tiers[2].getAttribute("y")));
    expect(Number(tiers[0].getAttribute("width"))).toBeGreaterThan(Number(tiers[2].getAttribute("width")));
  });
});
