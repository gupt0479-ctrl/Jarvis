---
type: class
input_kind: project
status: sprout
created: 2026-04-27
updated: 2026-04-27
area:
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Project"
related:
  - "[[Final Project|Final Project]]"
  - "[[Week - 13|Week - 13]]"
  - "[[Chapter - 22|Chapter - 22]]"
  - "[[Chapter - 23|Chapter - 23]]"
---
# Heuristic Pathfinding Project
## Overview
This project option implements A* and related heuristic search algorithms on graphs. A* extends Dijkstra's algorithm by adding a heuristic estimate of the remaining distance to the goal, which guides the search toward the target and reduces the number of vertices explored. The project uses the course graph code base and applies heuristic search to grid-based pathfinding problems.
## Source Files
- `Final Project/Heuristic Pathfinding/Ch20(Graphs-CodeBase)-HeuristicSearch.ipynb` — heuristic search implementation on the course graph code base
- `Final Project/Heuristic Pathfinding/HeuristicPathfinding-Template.ipynb` — project template with scaffolding
## Reference Papers
- `A_Formal_Basis_for_the_Heuristic_Determination_of_Minimum_Cost_Paths(Astar)-1967-68.pdf` — Hart, Nilsson, Raphael's original A* paper (1968)
- `ExperimentswiththeGraphTraverserProgram(Astar)-1966.pdf` — early experiments with graph traverser (1966)
- `Correction_to_AFormalBasisfortheHeuristicDeterminationofmincostpaths-1971.pdf` — correction to the original A* paper (1971)
- `Generalized Best-First Search Strategies and the Optimality of Astar-1985.pdf` — optimality analysis of A* (1985)
## Key Algorithms and Data Structures
- **A* search**: best-first search using $f(n) = g(n) + h(n)$ where $g(n)$ is the cost so far and $h(n)$ is the heuristic estimate to the goal
- **Admissible heuristic**: $h(n) \leq$ actual cost to goal, which guarantees A* finds the optimal path
- **Consistent heuristic**: $h(n) \leq c(n, n') + h(n')$ for every edge, which prevents reopening closed vertices
- **Priority queue**: min-heap ordered by $f$-value drives the search frontier
- **Dijkstra's algorithm**: the special case of A* where $h(n) = 0$ for all vertices
## Concept Links
- [[Week - 13|Week - 13]] — single-source and all-pairs shortest paths
- [[Chapter - 22|Chapter - 22]] — single-source shortest paths (Dijkstra, Bellman-Ford)
- [[Chapter - 23|Chapter - 23]] — all-pairs shortest paths
- [[Graph Algorithms|Graph Algorithms]] — graph representations, BFS, DFS
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11|Week - 11]] — BFS and DFS (A* builds on BFS-style frontier expansion)
## Complexity
| Algorithm | Time | Space |
|---|---|---|
| A* (with binary heap) | $O((V + E) \log V)$ | $O(V)$ |
| Dijkstra (with binary heap) | $O((V + E) \log V)$ | $O(V)$ |

A* explores fewer vertices than Dijkstra when the heuristic is informative, but the worst-case complexity is the same. The practical speedup depends on heuristic quality.