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
next: "[[Week - 14|Week - 14]]"
---
# Chapter - 24 Maximum Flow
## 24.1 Flow Networks
A **flow network** is a directed graph $G = (V, E)$ with a **source** $s$ and **sink** $t$, where each edge $(u, v) \in E$ has a nonnegative **capacity** $c(u, v) \geq 0$. If $(u, v) \notin E$, then $c(u, v) = 0$.

A **flow** is a function $f: V \times V \to \mathbb{R}$ satisfying:
- **Capacity constraint**: $0 \leq f(u, v) \leq c(u, v)$ for all $u, v \in V$.
- **Flow conservation**: for all $u \in V \setminus \{s, t\}$, $\sum_{v \in V} f(v, u) = \sum_{v \in V} f(u, v)$.

The **value** of a flow is $|f| = \sum_{v \in V} f(s, v) - \sum_{v \in V} f(v, s)$.

> [!INFO] The textbook assumes no antiparallel edges (if $(u,v) \in E$ then $(v,u) \notin E$) and that $s$ has no incoming edges and $t$ has no outgoing edges. Networks with multiple sources/sinks can be reduced to single-source single-sink by adding a supersource and supersink.

### Residual Networks
Given a flow $f$ in $G$, the **residual network** $G_f = (V, E_f)$ has edges with **residual capacity**:
$$c_f(u, v) = \begin{cases} c(u,v) - f(u,v) & \text{if } (u,v) \in E \\ f(v,u) & \text{if } (v,u) \in E \\ 0 & \text{otherwise} \end{cases}$$

An edge $(u,v)$ is in $E_f$ if $c_f(u,v) > 0$. Forward edges represent remaining capacity; backward edges represent flow that can be "undone."

### Augmenting Paths
An **augmenting path** $p$ is a simple $s \to t$ path in $G_f$. The **residual capacity** of $p$ is $c_f(p) = \min\{c_f(u,v) : (u,v) \text{ is on } p\}$. Pushing $c_f(p)$ units of flow along $p$ increases $|f|$ by $c_f(p)$.

### Cuts
A **cut** $(S, T)$ of a flow network is a partition of $V$ into $S$ and $T = V \setminus S$ with $s \in S$ and $t \in T$. The **capacity** of the cut is $c(S, T) = \sum_{u \in S} \sum_{v \in T} c(u, v)$. A **minimum cut** has the smallest capacity among all cuts.

> [!summary] Max-flow min-cut theorem (Theorem 24.11)
> The following are equivalent:
> 1. $f$ is a maximum flow in $G$.
> 2. The residual network $G_f$ contains no augmenting path.
> 3. $|f| = c(S, T)$ for some cut $(S, T)$.

## 24.2 The Ford-Fulkerson Method
The Ford-Fulkerson method iteratively finds augmenting paths in $G_f$ and pushes flow along them.

```text
FORD-FULKERSON-METHOD(G, s, t)
  initialize flow f to 0
  while there exists an augmenting path p in G_f
      augment flow f along p
  return f
```

- **Termination**: with integer capacities, each augmentation increases $|f|$ by at least 1, so the method terminates in at most $|f^*|$ iterations where $f^*$ is the max flow.
- **Edmonds-Karp**: using BFS to find the shortest augmenting path guarantees at most $O(VE)$ augmentations, giving $O(VE^2)$ total time.

### Complexity

| Variant | Path Selection | Augmentations | Total |
|---|---|---|---|
| Generic Ford-Fulkerson | arbitrary | $O(\|f^*\|)$ | $O(E \cdot \|f^*\|)$ |
| Edmonds-Karp | BFS (shortest) | $O(VE)$ | $O(VE^2)$ |

## 24.3 Maximum Bipartite Matching
A **bipartite graph** $G = (L \cup R, E)$ has edges only between $L$ and $R$. A **matching** is a subset of edges with no shared endpoints. The **maximum matching** can be found by reducing to max flow:
1. Add source $s$ with edges to all vertices in $L$ (capacity 1).
2. Add sink $t$ with edges from all vertices in $R$ (capacity 1).
3. Direct all edges from $L$ to $R$ with capacity 1.
4. Run Ford-Fulkerson. The max flow equals the maximum matching size.

## Overview
- Chapter 24 studies maximum flow in directed capacity networks.
- In CSCI 4041, the main emphasis is on residual networks, augmenting paths, Ford-Fulkerson, and the max-flow min-cut theorem.
- The Network Flow final-project option directly applies this chapter's model to distribution-network optimization.

## Core Definitions
- **Flow network:** directed graph with source `s`, sink `t`, and nonnegative capacities.
- **Capacity constraint:** `0 <= f(u,v) <= c(u,v)`.
- **Flow conservation:** all non-source/non-sink vertices have equal incoming and outgoing flow.
- **Residual capacity:** remaining ability to increase or undo flow on an edge.
- **Residual network `G_f`:** graph of all positive-residual-capacity moves.
- **Augmenting path:** path from `s` to `t` in `G_f`.
- **Cut:** partition `(S,T)` with `s in S` and `t in T`.

## Main Algorithms
- Ford-Fulkerson method: repeatedly find an augmenting path, compute bottleneck, and augment flow.
- Edmonds-Karp: Ford-Fulkerson with BFS shortest augmenting paths.
- Residual-network construction with forward and backward edges.
- Max-flow min-cut extraction: after termination, reachable vertices from `s` in `G_f` form the source side of a minimum cut.
- Bipartite matching reduction is textbook-covered, but not lecture-emphasized in the read Week 14 materials.

## Correctness Ideas
- Augmenting along a residual path preserves capacity constraints and flow conservation.
- If an augmenting path exists, the current flow is not maximum.
- If no augmenting path exists, reachable vertices from `s` in the residual graph define a cut whose capacity equals the current flow value.
- Max-flow min-cut theorem ties these together: maximum flow value equals minimum cut capacity.
- Integer capacities make generic Ford-Fulkerson terminate because each augmentation increases flow by at least 1.

## Complexity
- Generic Ford-Fulkerson with integer capacities is `O(E * |f*|)` using a simple path-search implementation.
- Edmonds-Karp is `O(VE^2)` because BFS path choice bounds the number of augmentations.
- Space is `O(V+E)` for adjacency-list network and residual network representations.

## Examples
- A forward residual edge has capacity `c(u,v)-f(u,v)`.
- A backward residual edge has capacity `f(u,v)`, allowing the algorithm to undo part of a previous decision.
- In Edmonds-Karp, BFS chooses an augmenting path with fewest edges in the residual network.

## Connections
- [[Week - 14|Week - 14]]
- [[Maximum Flow|Maximum Flow]]
- [[Graph Algorithms|Graph Algorithms]]
- [[Network Flow Project|Network Flow Project]]
- [[Chapter - 20|Chapter - 20]] for BFS and adjacency-list foundations.
- TODO: source gap - Section 24.3 bipartite matching is textbook-covered but was not supported by the read Week 14 lecture notebook emphasis.

## Common Pitfalls
- Confusing original capacity with residual capacity.
- Forgetting backward edges in the residual network.
- Violating flow conservation while augmenting.
- Thinking Ford-Fulkerson specifies one path rule; path choice determines the variant and bound.
- Computing cut capacity using residual edges instead of original network edges from `S` to `T`.

## Review Checklist
- [ ] Define flow network, capacity constraint, conservation, residual network, and augmenting path.
- [ ] Construct a residual network from a given flow.
- [ ] Trace one Ford-Fulkerson augmentation and bottleneck update.
- [ ] State max-flow min-cut and identify the final cut.
- [ ] Explain Edmonds-Karp's BFS path choice and complexity.

## Lecture Emphasis
The professor's lecture ([[Week - 14|Week - 14]]) focuses on Sections 24.1 and 24.2, with emphasis on residual network construction and the Ford-Fulkerson iteration. Section 24.3 (bipartite matching) is not covered in lecture. The key code artifacts are in `Ch20(Graphs-CodeBase)-NETWORK.ipynb` and `Ch24_Maximum_Flow.ipynb`:
- `network` class — extends the adjacency-list `graph` class with `capacity` and `flow` on each edge.
- `residual_network(G)` — constructs $G_f$ with forward edges (residual capacity $c - f$) and backward edges (residual capacity $f$).
- BFS-based augmenting-path search — implements the Edmonds-Karp variant.

The professor demonstrates the algorithm step by step on the CLRS textbook example (Figure 24.6), showing the residual network and augmenting path at each iteration. The `network` class reuses the same adjacency-list linked-list structure as the base `graph` class from [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11|Week - 11]], with the `edge` inner class extended to store `capacity` and `flow`. The final project (`Final Project/Network Flow/`) applies this to distribution network optimization.

The Ford-Fulkerson/Edmonds-Karp augmenting-path loop is the actual algorithm that uses the residual network. The professor's implementation uses BFS to find shortest augmenting paths (Edmonds-Karp variant):

```python
def ford_fulkerson(G, s, t):
    """Ford-Fulkerson method using BFS (Edmonds-Karp) for augmenting paths"""
    Gf = residual_network(G)
    while True:
        # BFS to find augmenting path in residual network
        path = bfs_path(Gf, s, t)
        if path is None:
            break
        # Find bottleneck (minimum residual capacity along path)
        bottleneck = min(Gf.get_edge(path[i], path[i+1]).flow 
                        for i in range(len(path)-1))
        # Augment flow along path
        for i in range(len(path)-1):
            u, v = path[i], path[i+1]
            edge = G.get_edge(u, v)
            if edge:  # forward edge in original
                edge.flow += bottleneck
            else:     # backward edge — reduce flow on reverse
                rev_edge = G.get_edge(v, u)
                rev_edge.flow -= bottleneck
        # Rebuild residual network
        Gf = residual_network(G)
    return G
```

This loop is the core of the algorithm: find a path, compute the bottleneck, push flow, rebuild the residual network, and repeat until no augmenting path exists.
