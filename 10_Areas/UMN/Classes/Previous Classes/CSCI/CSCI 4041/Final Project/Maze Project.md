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
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11|Week - 11]]"
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12|Week - 12]]"
  - "[[Chapter - 20|Chapter - 20]]"
---
# Maze Project
## Overview
This was the user's chosen final project option. The project implements maze generation and solving using graph traversal algorithms. A maze is modeled as a grid graph where cells are vertices and open passages are edges. Generation creates a spanning tree of the grid (guaranteeing exactly one path between any two cells), and solving finds a path from start to finish using BFS or DFS.
Detailed implementation notes are in [[Maze Project Details|Maze Project Details]].
## Source Files
- `Final Project/Maze/Ch20(Graphs-CodeBase)-MAZE.ipynb` — maze implementation using the course graph code base
- `Final Project/Maze/Maze-Template.ipynb` — project template with scaffolding
## Reference Papers
- `An_Algorithm_for_Path_Connections_and_Its_Applications-1961.pdf` — Lee's algorithm for path connections (1961)
- `Fast_Maze_Router-Soukup1978.pdf` — Soukup's fast maze routing algorithm (1978)
- `Networks - Winter 1977 - Hadlock - A shortest path algorithm for grid graphs.pdf` — Hadlock's shortest path on grids
- `Presentation_of_a_MazeSolving_MachineTransactions_8th_Cybernetics_Conference_Josiah_Macy_Jr._Foundation_1952..pdf` — early maze-solving machine (1952)
## Key Algorithms and Data Structures
- **Grid graph representation**: 2D grid where each cell is a vertex and edges connect adjacent open cells
- **BFS maze solving**: finds the shortest path (fewest cells) from start to finish in an unweighted grid
- **DFS maze solving**: finds a path (not necessarily shortest) by exploring as deep as possible before backtracking
- **Maze generation via spanning tree**: remove walls to create a random spanning tree of the grid, ensuring exactly one path between any two cells
- **Adjacency-list graph**: the course graph code base from [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11|Week - 11]] and [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12|Week - 12]] powers the implementation
## Concept Links
- [[Graph Algorithms|Graph Algorithms]] — BFS, DFS, graph representations
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11|Week - 11]] — BFS and DFS introduction
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12|Week - 12]] — topological sort, connected components, graph code base
- [[Chapter - 20|Chapter - 20]] — graph representations, BFS, DFS
- [[Chapter - 21|Chapter - 21]] — minimum spanning trees (related to maze generation)
### Additional Concept Links
- [[Week - 13|Week - 13]] - shortest paths and Dijkstra.
- [[Chapter - 22|Chapter - 22]] - single-source shortest paths and Dijkstra.
- [[Final Project|Final Project]] - parent final project note.
## Complexity
| Algorithm | Time | Space |
|---|---|---|
| BFS solve | $O(V + E)$ | $O(V)$ |
| DFS solve | $O(V + E)$ | $O(V)$ |
| Maze generation | $O(V + E)$ | $O(V)$ |
For an $n \times m$ grid: $V = nm$, $E = O(nm)$. Both generation and solving are linear in the grid size.
### Detailed Complexity
| Algorithm | Time | Space |
|---|---|---|
| BFS solve | $O(V + E)$ | $O(V)$ |
| DFS solve | $O(V + E)$ | $O(V)$ |
| Dijkstra solve, binary heap | $O((V + E)\log V)$ | $O(V)$ |
| Recursive backtracking generation | $O(V + E)$ | $O(V)$ |
| Randomized Prim generation | $O(V + E)$ expected with simple frontier filtering | $O(V)$ |
| Recursive division generation | Usually near $O(V \log V)$ for balanced splits; measure actual counters | $O(V)$ |
For this project, $V = nm$ and $E = O(nm)$ on an $n \times m$ grid because each cell has at most four neighbors. That is why adjacency lists match the maze better than an adjacency matrix.
## Project Readiness Addendum
The implementation choice should center the low-risk generator trio: **recursive backtracking, randomized Prim, and recursive division**. The solver comparison should include **BFS, DFS, and Dijkstra**, with BFS as the shortest-path baseline for unit-weight mazes and Dijkstra as the required nonnegative-weight shortest-path method from Week 13.
## Requirements Snapshot
- Implement multiple maze generators and compare how their structures differ.
- Solve generated mazes with BFS, DFS, and Dijkstra.
- Use the professor's graph code style and visualization utilities, especially `PrintGraph` where required.
- Include citations for outside sources used to design the algorithms.
- Provide correctness reasoning, runtime analysis, experiments as maze size grows, and visual examples.
- Keep algorithm timing separate from maze rendering so performance claims are about the algorithms.
## Chosen Algorithms
- **Recursive backtracking generation**: randomized DFS that carves to unvisited neighbors and backtracks when stuck; expected to create long corridors.
- **Randomized Prim generation**: grows a maze from a frontier of walls/cells; expected to create many short branches and dead ends.
- **Recursive division generation**: starts from open space, adds long dividing walls, and leaves a doorway per split; expected to create long straight wall segments.
- **BFS solving**: shortest path in unit-weight mazes.
- **DFS solving**: valid reachability path, not necessarily shortest.
- **Dijkstra solving**: shortest path for nonnegative edge weights; should match BFS when every passage has unit cost.
## Citation Set
- Jamis Buck maze algorithm index: https://www.jamisbuck.org/mazes/
- Recursive backtracking: https://weblog.jamisbuck.org/2010/12/27/maze-generation-recursive-backtracking
- Prim's maze algorithm: https://weblog.jamisbuck.org/2011/1/10/maze-generation-prim-s-algorithm
- Recursive division: https://weblog.jamisbuck.org/2011/1/12/maze-generation-recursive-division-algorithm
- Lee 1961 metadata: https://www.semanticscholar.org/paper/An-Algorithm-for-Path-Connections-and-Its-Lee/6b9cbd70349aac279cb69ffb6017ee6504a729b9
- Hadlock overview: https://sites.lafayette.edu/cadapps/main-page/maze-router-app/hadlocks-algorithm/
- Shannon/Theseus context: https://cir.nii.ac.jp/crid/1390009224839265920
## Correctness Hooks
- A perfect maze should have one connected passage graph and exactly $|V|-1$ undirected passage edges.
- Recursive backtracking and randomized Prim preserve acyclicity by carving only to unvisited cells.
- Recursive division preserves connectivity by leaving at least one doorway whenever a wall divides a region.
- BFS is correct for shortest paths in unit-weight mazes because it explores by increasing distance from the source.
- DFS is correct for reachability but not for shortest path optimality.
- Dijkstra is correct for nonnegative weights and should agree with BFS on unit-weight maze path length.
## Testing Checklist
- Validate generated mazes: all cells reachable, edge count correct for perfect mazes, no out-of-bounds passages.
- Validate returned paths: starts at entrance, ends at exit, uses only open adjacent cells.
- Cross-check BFS versus Dijkstra on every unit-weight test maze.
- Use repeated random seeds for each size and generator.
- Track both wall-clock time and counters such as visited cells, queue pops, stack pops, heap pops, and relaxations.
- Compare qualitative metrics: dead-end count, solution-path length, branching factor, and corridor length.
