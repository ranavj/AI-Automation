from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict, List, Set

router = APIRouter(prefix="/pipelines", tags=["pipelines"])

class Edge(BaseModel):
    id: str | None = None
    source: str
    target: str

class Pipeline(BaseModel):
    nodes: List[Dict[str, Any]]
    edges: List[Edge]

@router.post("/parse")
def parse_pipeline(p: Pipeline):
    nodes: Set[str] = {n.get('id') for n in p.nodes if n.get('id')}
    adj = {n: set() for n in nodes}
    indeg = {n: 0 for n in nodes}
    edges = 0
    for e in p.edges:
        if e.source in nodes and e.target in nodes and e.target not in adj[e.source]:
            adj[e.source].add(e.target)
            indeg[e.target] += 1
            edges += 1

    # Kahn's algorithm for DAG
    q = [n for n in nodes if indeg[n] == 0]
    visited = 0
    while q:
        u = q.pop(0)
        visited += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    return {"num_nodes": len(nodes), "num_edges": edges, "is_dag": visited == len(nodes)}