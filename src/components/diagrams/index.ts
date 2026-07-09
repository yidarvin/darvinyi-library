// The diagram primitive library. A fixed vocabulary of hand-authored inline-SVG
// forms (see docs/diagram-vocabulary.md). A book page composes and labels these; it
// never authors raw SVG from zero. All forms theme to the house tokens and read at
// 360px wide. See ./README.md for the form-to-props cheatsheet.
export { ProcessLoop, type ProcessLoopProps } from "./ProcessLoop";
export { Matrix, type MatrixProps, type MatrixQuadrant } from "./Matrix";
export { Pyramid, type PyramidProps, type PyramidTier } from "./Pyramid";
export { Spectrum, type SpectrumProps, type SpectrumZone } from "./Spectrum";
export { Concentric, type ConcentricProps, type ConcentricRing } from "./Concentric";
export { Flow, type FlowProps } from "./Flow";
export { Curve, type CurveProps, type CurveShape, type CurveAnnotation } from "./Curve";
export { Compare, type CompareProps, type ComparePanel } from "./Compare";
export { Iceberg, type IcebergProps } from "./Iceberg";
export { Venn, type VennProps, type VennSet } from "./Venn";
export { NodeGraph, type NodeGraphProps, type GraphNode, type GraphEdge } from "./NodeGraph";
export { Timeline, type TimelineProps, type TimelineSegment } from "./Timeline";
export { Bars, type BarsProps, type BarItem } from "./Bars";
