---
type: class
input_kind: project
status: sprout
created: 2026-04-27
updated: 2026-04-27
area:
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Concepts/Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Project"
related:
  - "[[Final Project|Final Project]]"
  - "[[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 14|Week - 14]]"
  - "[[Chapter - 24|Chapter - 24]]"
---
# Network Flow Project
## Overview
This project option implements a distribution network flow solver. The problem models a directed graph where edges have capacities and the goal is to maximize the total flow from a source to a sink without exceeding any edge capacity. The implementation uses the Ford-Fulkerson method with augmenting paths, built on the course graph code base.
## Source Files
- `Final Project/Network Flow/Ch20(Graphs-CodeBase)-NETWORK.ipynb` — network flow implementation on the course graph code base
- `Final Project/Network Flow/Distribution-Network-Template.ipynb` — project template with scaffolding
## Reference Papers
- `MaximalFlowThroughANetwork-FordFulkerson-1954.pdf` — Ford and Fulkerson's original max-flow paper (1956)
- `NetworkFlowTheory_Ford(1956).pdf` — Ford's network flow theory
- `OntheMaxFLowMinCutTheoremofNetworks.pdf` — max-flow min-cut theorem
- `A Primal-dual Algorithm for the capacitated Hitchcock Problem.pdf` — primal-dual approach to capacitated transport
- `a-simple-algorithm-for-finding-maximal-network-flows-and-an-application-to-the-hitchcock-problem.pdf` — simple max-flow algorithm and Hitchcock application
## Key Algorithms and Data Structures
- **Ford-Fulkerson method**: repeatedly find augmenting paths from source to sink in the residual graph and push flow along them
- **Residual graph**: for each edge with capacity $c$ and flow $f$, the residual graph has forward capacity $c - f$ and backward capacity $f$
- **Augmenting path**: a path from source to sink in the residual graph with positive capacity on every edge
- **Max-flow min-cut theorem**: the maximum flow equals the minimum cut capacity, connecting flow optimization to graph structure
- **BFS for augmenting paths (Edmonds-Karp)**: using BFS to find shortest augmenting paths gives $O(VE^2)$ time
## Concept Links
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 14|Week - 14]] — maximum flow lecture
- [[Chapter - 24|Chapter - 24]] — maximum flow (CLRS)
- [[Graph Algorithms|Graph Algorithms]] — graph representations, BFS, DFS
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 13|Week - 13]] — shortest paths (related: augmenting paths use BFS/DFS)
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11|Week - 11]] — BFS and DFS foundations
## Complexity
| Algorithm | Time | Space |
|---|---|---|
| Ford-Fulkerson (DFS) | $O(E \cdot f^*)$ | $O(V + E)$ |
| Edmonds-Karp (BFS) | $O(VE^2)$ | $O(V + E)$ |

$f^*$ is the maximum flow value. Edmonds-Karp's BFS-based approach removes the dependence on flow magnitude, making it polynomial regardless of edge capacities.