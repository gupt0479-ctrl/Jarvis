---
type: concept
status: seed
created: 2026-04-27
updated: 2026-04-27
tags:
  - concept
notes:
  - "[[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Graphs/Graph Algorithms]]"
  - "[[Minimum Spanning Trees]]"
track:
  - algorithms
prerequisites:
  - "[[Time Complexity]]"
  - "[[Elementary Data Structures]]"
used_in: []
evidence: []
difficulty: 4
mastery_level: novice
drill_interval: 7
last_drilled: 2026-04-25
next_drill: 2026-05-02
---

# Graph Algorithms

> Distilled from [[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Graphs/Graph Algorithms|CSCI 4041 — Graph Algorithms]]

## Deep Dive

### One-Sentence Version

BFS explores by layers to find shortest paths in unweighted graphs; DFS explores by recursive descent to reveal structure like topological order and strongly connected components.

### What It Is

Graph algorithms operate on `G = (V, E)` using two core representations:
- **Adjacency list**: `Θ(V+E)` space, standard for sparse graphs
- **Adjacency matrix**: `Θ(V²)` space, constant-time edge lookup

Four fundamental algorithms:
- **BFS**: layer-by-layer exploration using a FIFO queue, computes shortest-path distance in edges
- **DFS**: recursive descent with discovery/finish timestamps
- **Topological sort**: reverse DFS finish order on a DAG
- **SCC**: two DFS passes (on G then G^T) to find maximal mutually reachable vertex sets

### Why It Matters

Graph problems appear everywhere: dependency resolution (topological sort), network routing (BFS/shortest paths), social network analysis (SCC), build systems (DAG ordering). The BFS/DFS distinction is a fundamental algorithmic choice that determines what structural information you can extract.

### Real Example

Course prerequisite scheduling is topological sort: run DFS on the prerequisite DAG, reverse the finish order, and every directed edge points forward in the result. If DFS encounters a Gray vertex (back edge), the graph has a cycle and no valid schedule exists.

### Contrast With

- **BFS vs DFS**: BFS finds shortest paths in unweighted graphs. DFS reveals deeper structure (timestamps, back edges, topological order). BFS uses a queue; DFS uses a stack (recursion).
- **Adjacency list vs matrix**: Lists are better for traversals (`O(V+E)`). Matrices are better for constant-time edge queries but waste space on sparse graphs.
- **Topological sort vs SCC**: Topological sort works only on DAGs and produces a linear order. SCC works on any directed graph and partitions vertices into mutually reachable groups.

### Source Anchors

- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Graphs/Graph Algorithms]] — full lecture notes with BFS/DFS/topo/SCC code
- [[Chapter - 20]] — CLRS graph representations and algorithms
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Week - 11]], [[10_Areas/Degree/UMN/Classes/CSCI 4041/Week - 12]] — lecture coverage

## Complexity

| Algorithm | Time | Key constraint |
|---|---|---|
| BFS | `O(V+E)` | shortest path only in unweighted graphs |
| DFS | `O(V+E)` | timestamps expose nested structure |
| Topological sort | `O(V+E)` | valid only on DAGs |
| SCC (Kosaraju) | `O(V+E)` | needs two DFS passes plus transpose |

## Diagnostic Questions

- Why does BFS compute shortest-path distance only in unweighted graphs?
- What extra information does DFS provide that BFS does not?
- Why does topological sort rely on finishing times rather than discovery times?
- Why does SCC require two DFS passes instead of one?
