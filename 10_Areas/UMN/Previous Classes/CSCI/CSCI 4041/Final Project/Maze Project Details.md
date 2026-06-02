---
type: class
input_kind: project
status: reference
created: 2026-05-04
updated: 2026-05-04
area:
  - "[[Final Project|Final Project]]"
  - "[[Final Project Report|Final Project Report]]"
tags:
  - "#class"
  - "#Project"
---
# Maze Project Details

This is the technical companion for [[Final Project Report|Final Project Report]]. Use the report note for the overall approach. Use this note while coding, validating, citing sources, and writing detailed correctness or experiment sections.

## Navigation
- Main approach: [[Final Project Report|Final Project Report]]
- Compact project index: [[Maze Project|Maze Project]]
- Graph traversal: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11|Week - 11]], [[Chapter - 20|Chapter - 20]]
- Spanning trees / Prim: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12|Week - 12]], [[Chapter - 21|Chapter - 21]]
- Dijkstra / shortest paths: [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 13|Week - 13]], [[Chapter - 22|Chapter - 22]]

## Source Files
- `Final Project/Maze/Ch20(Graphs-CodeBase)-MAZE.ipynb` - professor graph code base and maze utilities.
- `Final Project/Maze/Maze-Template.ipynb` - project scaffold and required implementation slots.
- Local graph traversal notes from [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11|Week - 11]].
- Local MST notes from [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12|Week - 12]].
- Local shortest-path notes from [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 13|Week - 13]].

## Citation Set
Use these when writing the final report or explaining implementation choices.

- Jamis Buck maze algorithm index: https://www.jamisbuck.org/mazes/
- Recursive backtracking: https://weblog.jamisbuck.org/2010/12/27/maze-generation-recursive-backtracking
- Prim's maze algorithm: https://weblog.jamisbuck.org/2011/1/10/maze-generation-prim-s-algorithm
- Recursive division: https://weblog.jamisbuck.org/2011/1/12/maze-generation-recursive-division-algorithm
- Lee 1961 metadata: https://www.semanticscholar.org/paper/An-Algorithm-for-Path-Connections-and-Its-Lee/6b9cbd70349aac279cb69ffb6017ee6504a729b9
- Hadlock overview: https://sites.lafayette.edu/cadapps/main-page/maze-router-app/hadlocks-algorithm/
- Shannon/Theseus context: https://cir.nii.ac.jp/crid/1390009224839265920

Local papers already in the project folder:
- `An_Algorithm_for_Path_Connections_and_Its_Applications-1961.pdf` - Lee path connections.
- `Fast_Maze_Router-Soukup1978.pdf` - Soukup fast maze routing.
- `Networks - Winter 1977 - Hadlock - A shortest path algorithm for grid graphs.pdf` - Hadlock grid shortest paths.
- `Presentation_of_a_MazeSolving_MachineTransactions_8th_Cybernetics_Conference_Josiah_Macy_Jr._Foundation_1952..pdf` - Shannon maze-solving machine context.

## Graph Model
Use one consistent graph model:

- `V`: all cells in the grid.
- `E_grid`: all possible edges between adjacent cells.
- `E_maze`: open passages after generation.
- Wall between cells `u` and `v`: the candidate edge `(u, v)` is not in `E_maze`.
- Open passage between cells `u` and `v`: `(u, v)` is in `E_maze`.

For an `n x m` grid:

- $|V| = nm$
- $|E_grid| = n(m-1) + m(n-1)$
- $|E_grid| = O(nm) = O(V)$

The passage graph is sparse because each cell has degree at most 4. That is why adjacency lists fit the assignment better than adjacency matrices.

## Maze Validity Invariant
For a perfect maze:

- every cell is reachable,
- the passage graph is connected,
- the passage graph is acyclic,
- the number of undirected passage edges is $|V|-1$.

The validator should do this:

1. Run BFS or DFS from the entrance over open passages.
2. Count reachable cells.
3. Count undirected passage edges once.
4. Check `reachable_count == rows * cols`.
5. Check `passage_edge_count == rows * cols - 1` for generators intended to create perfect mazes.

Recursive division needs one extra note: if the implementation starts from fully open space and only adds some walls, it may not produce a perfect maze unless the wall-building logic removes enough cycles. If it leaves cycles intentionally, document it as a non-perfect maze variant and do not use the $|V|-1$ test as a required invariant.

## Representation Checklist
Use this as the notebook structure:

- `cell = (r, c)`
- `in_bounds(cell)`
- `grid_neighbors(cell)`
- `open_neighbors(cell)`
- `carve(a, b)`
- `add_wall(a, b)` if the wall model needs it
- `passage_edges()`
- `count_dead_ends()`
- `reconstruct_path(prev, start, goal)`
- `validate_maze(maze)`
- `validate_path(maze, path, start, goal)`

Keep solver state separate from maze state. BFS/DFS/Dijkstra should not permanently mutate the maze. If the professor's vertex objects store color, distance, predecessor, or timestamps, call a reset helper before every algorithm run.

## Generator Details
These are the notes to use when writing pseudocode, correctness explanations, and comments in the notebook. The report should summarize these ideas; this file keeps the implementation-level details.

## Recursive Backtracking
Role: first generator and easiest correctness win.

Mechanism: randomized DFS. Start from one cell, choose random unvisited neighbors, carve passages, and backtrack when stuck.

Implementation sketch:

1. Choose a start cell.
2. Mark it visited.
3. Push it onto a stack.
4. While the stack is not empty:
   - look at the top cell,
   - collect unvisited neighboring cells,
   - if at least one exists, choose one randomly, carve to it, mark it visited, push it,
   - otherwise pop.

Correctness argument:

- Initially, the visited region is one cell, so it is connected and acyclic.
- Each accepted carve connects the current region to exactly one unvisited cell.
- Adding one new vertex by one edge preserves connectedness and does not create a cycle.
- When all cells are visited, the passage graph is connected and has $|V|-1$ edges, so it is a spanning tree.

Runtime: $O(V+E)$, which is $O(V)$ on a grid.

Expected style: long corridors, deep paths, fewer short branches than Prim.

Implementation risk: true recursion can hit Python recursion limits. Use an explicit stack.

## Randomized Prim
Role: second generator and MST/frontier comparison.

Mechanism: grow a maze from a visited region by choosing random frontier edges.

Implementation sketch:

1. Choose a start cell and mark it visited.
2. Add all candidate edges from that cell to a frontier list.
3. While the frontier is not empty:
   - choose and remove one frontier edge at random,
   - if it connects one visited cell and one unvisited cell, carve it,
   - mark the new cell visited,
   - add the new cell's candidate edges to the frontier,
   - if both endpoints are already visited, ignore it.

Correctness argument:

- The visited region starts connected.
- Every accepted edge adds exactly one new cell to the region.
- No accepted edge connects two already visited cells, so no cycle is added.
- When every cell has been visited, the result is connected and acyclic.

Runtime: $O(V+E)$ expected with a simple frontier list on a grid, assuming stale edges are filtered cheaply. If random removal from the middle of a Python list becomes expensive, mention that implementation detail in the experiment discussion.

Expected style: more branching, many short dead ends, less corridor-heavy than recursive backtracking.

Implementation risk: the condition "exactly one endpoint visited" is the whole algorithm. If that check is wrong, the maze may get cycles or disconnected regions.

## Recursive Division
Role: third generator and visual contrast.

Mechanism: starts open, adds walls recursively.

Implementation sketch:

1. Begin with an open rectangle.
2. Choose horizontal or vertical division, usually based on region shape.
3. Add one wall line across the chosen region.
4. Leave one doorway in the wall.
5. Recursively divide the two subregions.
6. Stop when a region is too small to divide.

Correctness argument:

- Before a split, assume the region is connected to the rest of the maze.
- Adding a wall with one doorway divides the space visually but preserves a route between both sides.
- Recursing preserves connectivity as long as every division leaves a doorway.

Runtime: often described near $O(V \log V)$ for balanced divisions because cells may be touched across multiple recursive levels. The exact runtime depends on how walls are represented and how splits are chosen, so record counters.

Expected style: long straight walls, rectangular regions, different visual texture from the two passage-carving generators.

Implementation risk: off-by-one errors. Doorways must be placed inside the wall, wall endpoints must respect boundaries, and small regions should stop cleanly.

## Solver Interface
All solvers should have the same return shape:

- `found`
- `prev`
- `path`
- `path_length`
- `visited_count`
- `operation_counts`

Recommended counters:

- BFS: queue pushes, queue pops, visited cells.
- DFS: stack pushes, stack pops, visited cells.
- Dijkstra: heap pushes, heap pops, relaxations, stale heap entries.

## BFS
BFS solves the shortest path problem in unweighted graphs. Since a normal maze has cost 1 per move, BFS gives the fewest-edge path from entrance to exit.

Correctness claim:

- BFS explores in layers of increasing distance from the source.
- The first time a vertex is discovered, its recorded distance is shortest.
- The predecessor chain from the exit reconstructs a shortest path.

Runtime: $O(V+E)$.

## DFS
DFS solves reachability and returns a legal path if the exit is reachable. It does not guarantee the shortest path.

Correctness claim:

- DFS follows legal open edges.
- If the exit is reachable, DFS will eventually discover it.
- The predecessor chain is a valid path, but not necessarily minimum length.

Runtime: $O(V+E)$.

## Dijkstra
Dijkstra solves shortest paths with nonnegative edge weights.

Correctness claim:

- The algorithm repeatedly finalizes the unsettled vertex with minimum tentative distance.
- With nonnegative weights, a finalized distance cannot later improve.
- Relaxation updates predecessors whenever a shorter path is found.

Runtime with a binary heap: $O((V+E)\log V)$.

Important project check: on unit-weight mazes, Dijkstra and BFS should return the same path length. If they do not, check edge weights, predecessor reconstruction, and stale solver state.

## Validation Tests
Small tests:

- `1x1`: start equals goal.
- `2x2`: easy to inspect edge counts and paths.
- `3x3`: enough structure to catch wall-direction mistakes.
- A manually blocked example if the representation allows disconnected mazes.

Generator tests:

- all cells reachable,
- no passages outside the grid,
- no asymmetric passages,
- perfect mazes have $|V|-1$ undirected passage edges.

Solver tests:

- path starts at start,
- path ends at goal,
- each step is between neighboring cells,
- each step uses an open passage,
- BFS length equals Dijkstra length on unit weights,
- DFS path is legal.

## Experiments
Run each generator on several sizes and repeated seeds. Suggested size ladder:

- `5x5` for debugging,
- `10x10` for first screenshots,
- `20x20`, `40x40`, `80x80` for growth behavior if runtime allows.

For each generated maze:

- solve with BFS, DFS, and Dijkstra,
- record solver counters,
- record path length,
- record runtime without drawing,
- optionally render one example per generator and size.

Qualitative metrics:

- dead-end count,
- solution path length,
- average degree of passage graph,
- branch count,
- corridor length estimate.

Use the same maze instance when comparing solvers. Otherwise the comparison mixes solver behavior with random maze differences.

## Complexity Table
| Algorithm | Time | Space | Notes |
|---|---|---|---|
| BFS solve | $O(V + E)$ | $O(V)$ | Shortest path for unit weights |
| DFS solve | $O(V + E)$ | $O(V)$ | Valid path, not necessarily shortest |
| Dijkstra solve | $O((V + E)\log V)$ | $O(V)$ | Use for nonnegative weights |
| Recursive backtracking | $O(V + E)$ | $O(V)$ | Stack-based randomized DFS |
| Randomized Prim | $O(V + E)$ expected | $O(V)$ | Frontier filtering details matter |
| Recursive division | often near $O(V \log V)$ | $O(V)$ | Depends on wall representation |

For a grid, $E = O(V)$, so BFS, DFS, backtracking, and randomized Prim should behave close to linear in the number of cells.

## Final Writeup Prompts
- What graph representation did we use, and why?
- Which generators preserve a spanning-tree invariant?
- How is recursive division different from passage-carving methods?
- Why is BFS the unit-weight baseline?
- Why does DFS not guarantee a shortest path?
- Why should Dijkstra match BFS on unit-weight mazes?
- What did the counters show as maze size increased?
- Did the qualitative maze metrics match the screenshots?
