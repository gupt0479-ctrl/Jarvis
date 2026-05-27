---
type: class
input_kind: book
status: sprout
created: 2026-04-27
updated: 2026-04-28
area:
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Textbook"
next: "[[Week - 13|Week - 13]]"
---
# Chapter - 22 Single-Source Shortest Paths
In a shortest-paths problem, we are given a weighted, directed graph $G = (V, E)$ and a weight function $w: E \to \mathbb{R}$. The weight of a path $p = \langle v_0, v_1, \ldots, v_k \rangle$ is $w(p) = \sum_{i=1}^{k} w(v_{i-1}, v_i)$. The shortest-path weight from $u$ to $v$ is $\delta(u, v) = \min\{w(p) : u \leadsto v\}$ if a path exists, and $\infty$ otherwise.

**Negative-weight edges** are allowed in some algorithms. A **negative-weight cycle** reachable from the source makes shortest-path weights undefined for vertices on or reachable from that cycle. We assume shortest paths are simple (no repeated vertices), containing at most $|V| - 1$ edges.

**Relaxation** is the core operation. Each vertex $v$ maintains a shortest-path estimate $v.d$ (upper bound on $\delta(s, v)$) and a predecessor $v.\pi$. `INITIALIZE-SINGLE-SOURCE(G, s)` sets $v.d = \infty$ and $v.\pi = \text{NIL}$ for all $v$, then $s.d = 0$. `RELAX(u, v, w)` tests whether $v.d > u.d + w(u, v)$ and updates if so.

> [!summary] Key relaxation properties (Section 22.5)
> - **Triangle inequality**: $\delta(s, v) \leq \delta(s, u) + w(u, v)$ for any edge $(u, v)$.
> - **Upper-bound property**: $v.d \geq \delta(s, v)$ always, and once $v.d = \delta(s, v)$ it never changes.
> - **Convergence property**: if $u.d = \delta(s, u)$ and we relax $(u, v)$, then $v.d = \delta(s, v)$ afterward.
> - **Path-relaxation property**: relaxing edges in shortest-path order guarantees correct distances.

## 22.1 The Bellman-Ford Algorithm
Bellman-Ford solves SSSP for graphs with negative-weight edges. It performs $|V| - 1$ passes, each relaxing every edge. After all passes, it checks for negative-weight cycles.

```text
BELLMAN-FORD(G, w, s)
  INITIALIZE-SINGLE-SOURCE(G, s)
  for i = 1 to |G.V| - 1
      for each edge (u, v) in G.E
          RELAX(u, v, w)
  for each edge (u, v) in G.E
      if v.d > u.d + w(u, v)
          return FALSE
  return TRUE
```

- **Correctness**: after $i$ passes, any vertex reachable from $s$ via a shortest path of at most $i$ edges has its correct distance. Since shortest paths have at most $|V| - 1$ edges, $|V| - 1$ passes suffice.
- **Negative-cycle detection**: if any edge can still be relaxed after $|V| - 1$ passes, a negative-weight cycle is reachable.
- **Complexity**: $O(VE)$.

## 22.2 Single-Source Shortest Paths in DAGs
In a DAG, shortest paths can be computed in $\Theta(V + E)$ time even with negative edges.

```text
DAG-SHORTEST-PATHS(G, w, s)
  topologically sort G
  INITIALIZE-SINGLE-SOURCE(G, s)
  for each vertex u in topological order
      for each vertex v in G.Adj[u]
          RELAX(u, v, w)
```

- **Correctness**: topological order ensures that when we process $u$, all predecessors of $u$ on any shortest path have already been processed.
- **Critical paths**: negating edge weights and running this algorithm finds the longest path in a DAG.
- **Complexity**: $\Theta(V + E)$.

## 22.3 Dijkstra's Algorithm
Dijkstra's algorithm is a greedy algorithm for graphs with nonnegative edge weights. It maintains a set $S$ of vertices with finalized distances and a min-priority queue $Q$ of remaining vertices.

```text
DIJKSTRA(G, w, s)
  INITIALIZE-SINGLE-SOURCE(G, s)
  S = empty set
  Q = G.V
  while Q is not empty
      u = EXTRACT-MIN(Q)
      S = S union {u}
      for each vertex v in G.Adj[u]
          RELAX(u, v, w)
```

- **Correctness**: when $u$ is extracted, $u.d = \delta(s, u)$. This relies on nonnegative weights — no future path through an unextracted vertex can improve $u.d$.
- **Complexity** depends on the priority queue:

| Priority Queue | EXTRACT-MIN | DECREASE-KEY | Total |
|---|---|---|---|
| Linear array | $O(V)$ | $O(1)$ | $O(V^2)$ |
| Binary min-heap | $O(\lg V)$ | $O(\lg V)$ | $O((V+E) \lg V)$ |
| Fibonacci heap | $O(\lg V)$ amortized | $O(1)$ amortized | $O(V \lg V + E)$ |

## 22.4 Difference Constraints and Shortest Paths
A system of $m$ difference constraints has the form $x_j - x_i \leq b_k$. This maps to a constraint graph where each inequality becomes an edge $(v_i, v_j)$ with weight $b_k$. Adding a source vertex $v_0$ with $0$-weight edges to all others, then running Bellman-Ford from $v_0$, yields a feasible solution $x_i = \delta(v_0, v_i)$ if no negative-weight cycle exists.

## 22.5 Proofs of Shortest-Paths Properties
This section formalizes the relaxation properties used throughout the chapter:
- **Lemma 22.10 (Triangle inequality)**: $\delta(s, v) \leq \delta(s, u) + w(u, v)$.
- **Lemma 22.11 (Upper-bound property)**: $v.d \geq \delta(s, v)$ always.
- **Lemma 22.14 (Convergence)**: if $s \leadsto u \to v$ is a shortest path and $u.d = \delta(s, u)$ before relaxing $(u, v)$, then $v.d = \delta(s, v)$ afterward.
- **Lemma 22.15 (Path relaxation)**: if edges of a shortest path $\langle v_0, v_1, \ldots, v_k \rangle$ are relaxed in order, then $v_k.d = \delta(s, v_k)$.

## Overview
- Chapter 22 studies single-source shortest paths in weighted directed graphs.
- In CSCI 4041, this chapter centers on relaxation, Bellman-Ford, Dijkstra, predecessor paths, and the exact condition under which Dijkstra is valid.
- The lecture code shares infrastructure with earlier graph and heap units, especially the graph class from Chapter 20 and the min-heap pattern from Prim.

## Core Definitions
- **Shortest-path estimate `v.d`:** current upper bound on the shortest-path weight from source `s` to `v`.
- **Predecessor `v.prev` / `v.pi`:** previous vertex on the currently best-known path.
- **Relaxation:** update `v.d` and predecessor if path through `u` is better.
- **Negative-weight cycle:** reachable cycle with total negative weight, making shortest paths undefined for affected vertices.
- **Shortest-path tree:** predecessor subgraph induced by final shortest paths from one source.

## Main Algorithms
- `INITIALIZE-SINGLE-SOURCE`: set all estimates to infinity except source distance 0.
- `RELAX`: the primitive shared by SSSP algorithms.
- Bellman-Ford: relax every edge `|V|-1` times, then check for a negative cycle.
- DAG shortest paths: topologically sort, then relax outgoing edges in topological order.
- Dijkstra: repeatedly extract the unsettled vertex with minimum estimate and relax its outgoing edges; requires nonnegative weights.

## Correctness Ideas
- Bellman-Ford invariant: after pass `i`, all shortest paths using at most `i` edges have correct estimates.
- Negative-cycle detection works because any further relaxation after `|V|-1` passes implies no simple shortest path bound.
- Dijkstra's greedy invariant is that once a vertex is extracted, its estimate is final; nonnegative edges are required.
- Relaxation properties from the textbook (upper-bound, convergence, path relaxation) are the proof toolkit.

## Complexity
- Bellman-Ford is `O(VE)` time and `O(V)` auxiliary space.
- DAG shortest paths are `Theta(V+E)` after topological sorting.
- Dijkstra with a binary heap is `O((V+E) lg V)`; with Fibonacci heap the textbook gives `O(V lg V + E)`.
- Dijkstra is not correct with negative edge weights.

## Examples
- Bellman-Ford can handle a negative edge as long as no reachable negative cycle exists.
- Dijkstra can fail if an extracted vertex later receives a better path through a negative edge.
- Path reconstruction follows predecessor pointers backward from target to source.

## Connections
- [[Week - 13|Week - 13]]
- [[Shortest Paths|Shortest Paths]]
- [[Minimum Spanning Trees|Minimum Spanning Trees]] for the Prim/Dijkstra heap contrast.
- [[Heuristic Pathfinding Project|Heuristic Pathfinding Project]]
- Source homework read: `Homework/Coding/CodingHW_9(chapter20-23-CLRS).ipynb`.
- TODO: source gap - no vault Homework/Paper Homework note exists for direct wikilinking.

## Common Pitfalls
- Running Dijkstra on graphs with negative edges.
- Forgetting the final negative-cycle check in Bellman-Ford.
- Thinking shortest paths minimize number of edges rather than total weight.
- Updating distance without updating predecessor during relaxation.
- Confusing an MST with a shortest-path tree.

## Review Checklist
- [ ] Define relaxation and shortest-path estimates.
- [ ] Implement Bellman-Ford and explain negative-cycle detection.
- [ ] Implement Dijkstra and state the nonnegative-weight assumption.
- [ ] Reconstruct a path from predecessor pointers.
- [ ] Prove correctness using the relaxation properties.

## Lecture Emphasis
The professor's lecture ([[Week - 13|Week - 13]]) focuses on Bellman-Ford and Dijkstra, skipping Section 22.2 (DAG shortest paths) and Section 22.4 (difference constraints). The key code artifacts are in `Ch22_Single-Source_Shortest_Path.ipynb`:
- `initialize_single_source(G,s)` and `relax(u,v,w_uv)` — the two foundational subroutines.
- `bellman_ford(G,s)` — direct implementation of the textbook pseudocode with negative-cycle detection.
- `print_path(G,s,v)` — recursive path reconstruction via the predecessor chain.
- `initialize_single_source_dijkstra(G,s)` and `relax_dijkstra(Q,u,v,w_uv)` — modified versions that integrate with the min-heap priority queue.
- `dijkstra(G,s)` — uses the same `minheap` class as Prim's algorithm from [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12|Week - 12]].

The professor emphasizes the structural similarity between Dijkstra and Prim: both use a min-heap with `extract_min` and `decrease_key`, but the key meaning differs (shortest-path estimate vs. lightest connecting edge). The professor also emphasizes that Dijkstra's greedy invariant breaks with negative edges — once a vertex is extracted, its distance must be final.
