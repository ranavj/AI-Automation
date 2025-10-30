export type Edge = { id?: string; source: string; target: string };
export type Node = { id: string; [k: string]: unknown };
export type Pipeline = { nodes: Node[]; edges: Edge[] };
export type ParseResult = { num_nodes: number; num_edges: number; is_dag: boolean };