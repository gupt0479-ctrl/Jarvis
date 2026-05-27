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
# Chapter - 23 All-Pairs Shortest Paths
The goal is to find the shortest-path weight $\delta(u, v)$ for every pair of vertices $u, v \in V$ in a weighted, directed graph $G = (V, E)$. The output is an $n \times n$ matrix $D = (d_{ij})$ where $d_{ij} = \delta(i, j)$.

> [!NOTE] Running single-source algorithms $|V|$ times solves APSP but is not always efficient. Dijkstra $|V|$ times gives $O(V^2 \lg V + VE)$; Bellman-Ford $|V|$ times gives $O(V^2 E)$. This chapter provides better solutions for dense graphs or graphs with negative weights.

## 23.1 Shortest Paths and Matrix Multiplication
This section uses dynamic programming where the subproblem structure is based on the number of edges in a path.

Let $l_{ij}^{(r)}$ be the minimum weight of any path from $i$ to $j$ using at most $r$ edges.
- **Base case**: $l_{ij}^{(0)} = 0$ if $i = j$, and $\infty$ otherwise.
- **Recurrence**: $l_{ij}^{(r)} = \min_{1 \leq k \leq n}\{l_{ik}^{(r-1)} + w_{kj}\}$

The computation of $L^{(r)}$ from $L^{(r-1)}$ is identical to matrix multiplication with $(\min, +)$ replacing $(+, \times)$. This is the **tropical semiring**.

```text
EXTEND-SHORTEST-PATHS(L, W)
  let L' be a new n x n matrix
  for i = 1 to n
      for j = 1 to n
          l'_ij = infinity
          for k = 1 to n
              l'_ij = min(l'_ij, l_ik + w_kj)
  return L'
```

**Slow APSP**: compute $L^{(1)}, L^{(2)}, \ldots, L^{(n-1)}$ by calling `EXTEND-SHORTEST-PATHS` $n - 2$ times. Complexity: $\Theta(n^4)$.

**Faster APSP (repeated squaring)**: since the extension operation is associative, compute $L^{(1)}, L^{(2)}, L^{(4)}, \ldots$ by squaring. Only $\lceil \lg(n-1) \rceil$ matrix products needed. Complexity: $\Theta(n^3 \lg n)$.

## 23.2 The Floyd-Warshall Algorithm
Floyd-Warshall uses a different DP formulation based on intermediate vertices rather than edge count.

$d_{ij}^{(k)}$ is the weight of a shortest path from $i$ to $j$ with all intermediate vertices in $\{1, 2, \ldots, k\}$.
- **Base case**: $d_{ij}^{(0)} = w_{ij}$.
- **Recurrence**: $d_{ij}^{(k)} = \min(d_{ij}^{(k-1)},\; d_{ik}^{(k-1)} + d_{kj}^{(k-1)})$

```text
FLOYD-WARSHALL(W)
  n = W.rows
  D(0) = W
  for k = 1 to n
      let D(k) be a new n x n matrix
      for i = 1 to n
          for j = 1 to n
              d_ij(k) = min(d_ij(k-1), d_ik(k-1) + d_kj(k-1))
  return D(n)
```

- **Complexity**: $\Theta(n^3)$ time, $\Theta(n^2)$ space (can reuse matrices).
- **Path reconstruction**: maintain a predecessor matrix $\Pi$ where $\pi_{ij}^{(k)}$ records the predecessor of $j$ on the shortest $i \to j$ path using intermediates $\{1, \ldots, k\}$. Update $\pi_{ij}$ when the path through $k$ is shorter.

### Transitive Closure
To determine reachability ($\delta(u,v) < \infty$) for all pairs, use the same Floyd-Warshall structure with boolean logic:
$$t_{ij}^{(k)} = t_{ij}^{(k-1)} \lor (t_{ik}^{(k-1)} \land t_{kj}^{(k-1)})$$
Logical operations are often faster than arithmetic on modern hardware.

## 23.3 Johnson's Algorithm for Sparse Graphs
Johnson's algorithm handles sparse graphs with negative weights (but no negative cycles) by reweighting edges to make them nonnegative, then running Dijkstra from each vertex.

1. Add a source vertex $s$ with $0$-weight edges to all other vertices.
2. Run Bellman-Ford from $s$ to compute $h(v) = \delta(s, v)$.
3. Reweight: $\hat{w}(u, v) = w(u, v) + h(u) - h(v) \geq 0$.
4. Run Dijkstra from each vertex $u$ using $\hat{w}$.
5. Recover original distances: $d_{uv} = \hat{\delta}(u, v) + h(v) - h(u)$.

- **Complexity with Fibonacci heaps**: $O(V^2 \lg V + VE)$.
- **Complexity with binary min-heaps**: $O(VE \lg V)$.

## Overview
- Chapter 23 studies all-pairs shortest paths: compute shortest-path weights between every ordered pair of vertices.
- In CSCI 4041, this chapter is the dynamic-programming continuation of Chapter 22, moving from one source to a full distance matrix.
- The lecture focuses on matrix-extension APSP, repeated squaring, Floyd-Warshall, and path reconstruction.

## Core Definitions
- **Weight matrix `W`:** `w_ij` is edge weight from `i` to `j`, `0` on the diagonal, infinity when no edge exists.
- **Distance matrix `D`:** final matrix where `d_ij = delta(i,j)`.
- **Predecessor matrix `PI`:** stores path-reconstruction information.
- **Min-plus product:** matrix multiplication with `min` replacing sum and `+` replacing multiplication.
- **Intermediate-vertex DP:** Floyd-Warshall subproblem indexed by which vertices are allowed as internal path vertices.

## Main Algorithms
- `EXTEND-SHORTEST-PATHS`: one min-plus matrix extension step.
- `SLOW-APSP`: repeat extension `n-1` times for `O(n^4)`.
- `FASTER-APSP`: repeated squaring for `O(n^3 lg n)`.
- `FLOYD-WARSHALL`: `Theta(n^3)` DP over intermediate vertices.
- Path reconstruction with a predecessor matrix.
- Johnson's algorithm is textbook-covered for sparse graphs, but the Week 13 lecture skipped it.

## Correctness Ideas
- Matrix APSP correctness follows from allowing paths with at most `r` edges and extending by one final edge.
- Faster APSP uses repeated squaring: after each extension, the maximum allowed path length roughly doubles.
- Floyd-Warshall invariant: after iteration `k`, `D[i][j]` is shortest among paths whose intermediate vertices come from the first `k` vertices.
- Path reconstruction is correct only if predecessor/intermediate information is updated exactly when the distance improves.

## Complexity
- Slow APSP is `O(n^4)` time and `O(n^2)` space.
- Faster APSP is `O(n^3 lg n)` time and `O(n^2)` space.
- Floyd-Warshall is `Theta(n^3)` time and `Theta(n^2)` space.
- Johnson's algorithm is better for sparse graphs with negative edges but no negative cycles; lecture coverage is a TODO/source gap here.

## Examples
- Floyd-Warshall checks whether `i -> k -> j` improves the previous best `i -> j`.
- A disconnected pair keeps infinity unless an allowed intermediate path connects it.
- Path reconstruction needs the matrix entry to remember the split/intermediate that caused the improvement.

## Connections
- [[Week - 13|Week - 13]]
- [[Shortest Paths|Shortest Paths]]
- [[Chapter - 22|Chapter - 22]]
- [[Heuristic Pathfinding Project|Heuristic Pathfinding Project]] is related through weighted pathfinding but focuses on single-source/single-target A*.
- Source homework read: `Homework/Coding/CodingHW_9(chapter20-23-CLRS).ipynb`.
- TODO: source gap - Johnson's algorithm appears in the textbook outline but was not present in the Week 13 lecture emphasis.

## Common Pitfalls
- Confusing APSP with running BFS from every vertex; BFS only handles unweighted graphs.
- Forgetting to initialize diagonal entries to 0.
- Updating Floyd-Warshall in a way that loses the intended `k`-iteration invariant.
- Treating the predecessor matrix as optional when the task asks for actual paths.
- Assuming Johnson was lecture-emphasized; this note marks it as textbook-covered but lecture-light.

## Review Checklist
- [ ] Define APSP, weight matrix, distance matrix, and predecessor matrix.
- [ ] Trace one min-plus extension step.
- [ ] Compare slow APSP, faster APSP, and Floyd-Warshall.
- [ ] Write the Floyd-Warshall recurrence.
- [ ] Explain how path reconstruction is stored.

## Lecture Emphasis
The professor's lecture ([[Week - 13|Week - 13]]) covers Sections 23.1 and 23.2 but skips Johnson's algorithm (Section 23.3). The key code artifacts are in `Ch23_All-Pairs_Shortest_Path.ipynb`:
- `extend_shortest_paths(L_prev,W,L,n)` — the (min, +) matrix multiplication step.
- `slow_apsp(W,L0,n)` — $O(n^4)$ variant calling `extend_shortest_paths` $n-1$ times.
- `faster_apsp(W,n)` — $O(n^3 \lg n)$ variant using repeated squaring.
- `floyd_warshall(W,n)` — $\Theta(n^3)$ implementation with the intermediate-vertex recurrence.
- `floyd_warshall_path(W,n)` — adds predecessor matrix $\Pi$ for path reconstruction.

The professor uses a `matrixgraph` class (from `Ch20(Graphs-CodeBase)-1.ipynb`) that stores the weight matrix directly, since all APSP algorithms operate on $n \times n$ matrices. The lecture emphasizes the progression from $O(n^4)$ to $O(n^3 \lg n)$ to $\Theta(n^3)$ as increasingly clever DP formulations.
