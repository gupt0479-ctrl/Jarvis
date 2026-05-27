---
type: class
input_kind: project
status: tree
created: 2026-05-04
updated: 2026-05-04
area:
  - "[[Final Project|Final Project]]"
  - "[[Maze Project|Maze Project]]"
tags:
  - "#class"
  - "#Project"
---
# Maze Generation and Solving with Graph Algorithms
## 1. Project Objective
This project implements and analyzes graph algorithms for maze generation and maze solving. The central model is a square grid graph. Each maze cell is represented as a vertex, and each possible movement between horizontally or vertically adjacent cells is represented as an undirected edge. A wall is the absence of such an edge; an open passage is the presence of the edge in the maze graph.
The implementation follows the professor's graph code base from `Ch20(Graphs-CodeBase)-MAZE.ipynb` and the maze scaffold in `Maze-Template.ipynb`. The code uses the professor's `graph`, `matrixgraph`, and `PrintGraph` utilities so that the algorithmic work remains connected to the course's graph representation rather than becoming a separate maze-only program.
The final implementation has three goals:
1. Generate valid mazes as graph structures.
2. Solve generated mazes using BFS, DFS, and Dijkstra's algorithm.
3. Validate and visualize the results using the course graph tools and maze-specific wall drawings.
## 2. Graph Model
Let the maze have side length `n`. The vertex set is

$$
V = \{0,1,\ldots,n^2-1\},
$$

where vertex `i*n + j` corresponds to the cell in row `i` and column `j`. The full grid graph contains an edge between two vertices exactly when the corresponding cells are adjacent in the grid. Since each cell has at most four neighbors, the grid graph is sparse. This is why the adjacency-list `graph` class is the natural representation for the passage graph.

The implementation uses two related graphs:

- `Grid`: the full graph of all possible adjacent cell moves.
- `M`: the generated maze graph containing only carved passages.

For visualizing the walls, the notebook converts the passage graph into a wall graph using the professor's `matrixgraph` representation. This mirrors the method in `Maze-Template.ipynb`: the algorithmic maze is stored as passages between cells, while the displayed maze is drawn as the dual wall structure.

A perfect maze is a spanning tree of the grid graph. Therefore, a valid perfect maze with `|V| = n^2` cells must satisfy two structural checks:

$$
\text{reachable vertices} = |V|
$$

and

$$
\text{undirected passage edges} = |V|-1.
$$

These checks are implemented in `validate_maze` and are used after generation.

## 3. Maze Generation Algorithms

### 3.1 Recursive Backtracking

The recursive-backtracking generator is an iterative version of depth-first search. It starts from the entrance cell, keeps a stack of the current search path, and repeatedly carves a passage to a randomly chosen unvisited neighbor. When a cell has no unvisited neighbors, the algorithm backtracks by popping the stack.

The main invariant is that every carved edge connects the already visited region to exactly one new cell. This preserves connectedness and prevents cycles. Initially, the maze contains one visited cell and no edges, so the invariant is true. Each accepted carve adds one new vertex and one edge. When all vertices have been visited, the resulting graph is connected and has `|V|-1` undirected edges, so it is a spanning tree.

This generator is useful as the first implementation test because it exercises the core helper methods: neighbor lookup, edge insertion, predecessor storage, and path reconstruction.

### 3.2 Prim-Based Maze Generation

The Prim-based generator builds a random weighted grid graph and then runs the professor-style Prim procedure from the MST section. Each full-grid edge is assigned a random positive weight. Prim's algorithm chooses a minimum spanning tree of this weighted grid, and the selected predecessor edges are copied into the maze graph as open passages.

This approach follows the structure of the course MST material: initialize all keys to infinity, set the root key to zero, maintain a min-priority queue, and relax incident edges by updating `key` and `prev`. Because all edge weights are random, the resulting spanning tree behaves as a randomized maze generator even though the algorithm is formally an MST algorithm.

The correctness argument follows directly from the MST property used in class. Prim returns a spanning tree over the connected full grid. Copying the selected tree edges into the passage graph produces a connected acyclic maze with exactly `|V|-1` passages.

### 3.3 Kruskal-Based Maze Generation

The Kruskal-based generator also starts with a randomly weighted full grid graph. It sorts all edges by increasing weight and accepts an edge when its endpoints are currently in different components. In the professor's implementation, components are represented by sets stored in a dictionary. When an edge is accepted, the two sets are unioned.

The accepted edge set is copied into the maze graph. Since Kruskal accepts only edges that join distinct components, it never introduces a cycle. Since the full grid is connected, the process continues until all cells are in one component. The result is again a spanning tree and therefore a perfect maze.

Kruskal is included because it is directly aligned with the professor's maze template, which presents minimum spanning tree generation as a natural way to create mazes.

## 4. Maze Solving Algorithms

### 4.1 Breadth-First Search

Breadth-first search is the baseline maze solver for unweighted mazes. Each open passage has unit cost, so the length of a path is the number of edges traversed. BFS explores vertices by increasing distance from the entrance. The first time the exit is discovered, the predecessor chain describes a shortest path in the maze graph.

The implementation resets all vertex colors, distances, and predecessor pointers before running. It uses a queue from `collections.deque`, matching the queue-based BFS structure from the course graph materials.

### 4.2 Depth-First Search

Depth-first search is implemented as a reachability solver. It follows one branch as far as possible before backtracking and records predecessor pointers along the first route that reaches the exit.

DFS is not a shortest-path algorithm. In a general maze graph with cycles, DFS may return a longer path than BFS. In the mazes generated by the spanning-tree methods above, however, there is exactly one simple path between the entrance and exit. For that reason, BFS, DFS, and Dijkstra return paths with the same length on these perfect mazes. The meaningful comparison is therefore not path optimality, but the order of exploration and the amount of overhead used by each solver.

### 4.3 Dijkstra's Algorithm

Dijkstra's algorithm is included because it is the standard shortest-path algorithm for graphs with nonnegative edge weights. In the unit-weight maze setting, it should agree with BFS on path length. This equality is used as a correctness check.

The implementation follows the professor's priority-queue style: vertices store `key`, `d`, and `prev`, and relaxation updates the best known distance and predecessor. Because this course-style heap implementation uses list membership and index lookup during decrease-key operations, the measured running time is higher than BFS on unit-weight mazes. The theoretical algorithm with an efficient binary heap is `O((V+E) log V)`, but this particular teaching implementation has additional linear-search overhead.

## 5. Visualization

The notebook uses two complementary visualizations.

First, `PrintGraph` displays the actual graph structure. This satisfies the project requirement to use the professor's visualization tools and is especially useful for debugging small mazes. It shows vertices, edges, and the cell-center layout used by the algorithms.

Second, `PrintMazeWithSolution` converts the passage graph into a wall graph and overlays the solution path. This gives a conventional maze picture while still using the same underlying graph representation. The wall graph is built from the absence of cell-passage edges: if two adjacent cells are connected in `M`, then the wall segment between them is removed.

A submission notebook should include executable cells that call both visualizations. A commented example is not enough for the final project, because the requirement asks that the visualization tools be used to demonstrate the implementation.

## 6. Validation

The implementation validates each generated maze using graph invariants. The key checks are:

- every cell is reachable from the entrance,
- the undirected passage edge count is `|V|-1`,
- a BFS solution exists from entrance to exit,
- BFS and Dijkstra return paths of the same length on unit-weight mazes.

The following local validation run used sizes `8`, `16`, and `32`, with visualization excluded from timing:

| Generator | n | Mean generation time (s) | Last BFS path length | Edges | Connected | Perfect |
|---|---:|---:|---:|---:|---|---|
| Recursive backtracking | 8 | 0.000539 | 47 | 63 | True | True |
| Recursive backtracking | 16 | 0.001734 | 115 | 255 | True | True |
| Recursive backtracking | 32 | 0.010666 | 251 | 1023 | True | True |
| Prim MST | 8 | 0.001658 | 15 | 63 | True | True |
| Prim MST | 16 | 0.018953 | 47 | 255 | True | True |
| Prim MST | 32 | 0.321101 | 71 | 1023 | True | True |
| Kruskal MST | 8 | 0.001158 | 15 | 63 | True | True |
| Kruskal MST | 16 | 0.004830 | 47 | 255 | True | True |
| Kruskal MST | 32 | 0.045354 | 71 | 1023 | True | True |

The edge counts match `n^2 - 1` in every case. This confirms that the generated passage graphs are spanning trees for the tested sizes.

The solver timing check below was run on already generated mazes, again excluding visualization:

| Generator | n | BFS time (s) | DFS time (s) | Dijkstra time (s) | Path length |
|---|---:|---:|---:|---:|---:|
| Recursive backtracking | 16 | 0.000168 | 0.000212 | 0.005524 | 127 |
| Recursive backtracking | 32 | 0.001231 | 0.001665 | 0.062470 | 491 |
| Prim MST | 16 | 0.000179 | 0.000188 | 0.004699 | 37 |
| Prim MST | 32 | 0.001332 | 0.001391 | 0.062504 | 119 |
| Kruskal MST | 16 | 0.000194 | 0.000148 | 0.004684 | 37 |
| Kruskal MST | 32 | 0.001217 | 0.000665 | 0.063356 | 119 |

The equal path lengths across BFS, DFS, and Dijkstra are expected for these perfect mazes. The timing difference mainly reflects algorithmic overhead: BFS and DFS use simple queue or stack traversal, while Dijkstra maintains priority-queue state and performs relaxation.

## 7. Complexity Analysis

Let `V` be the number of cells and `E` be the number of possible grid adjacencies. For an `n x n` grid, `V = n^2` and `E = O(n^2)` because each cell has at most four neighbors.

Recursive backtracking runs in `O(V+E)` time and uses `O(V)` space. On a grid this simplifies to `O(V)` time and `O(V)` space.

Kruskal's algorithm sorts the grid edges, so its theoretical running time is `O(E log E)` plus the cost of component operations. The professor-style implementation stores components as explicit sets, so the set-union bookkeeping can add overhead. Since grid graphs are sparse, `E = O(V)`, giving `O(V log V)` as the main sorting term.

Prim's algorithm with an efficient priority queue is commonly analyzed as `O((V+E) log V)`. The course-style implementation used here performs membership and index searches inside the heap array during updates, so the measured implementation is slower than the ideal heap analysis. This distinction matters because the project grades the implementation, not only the textbook pseudocode.

BFS and DFS each run in `O(V+E)` time and use `O(V)` space. Dijkstra's algorithm has theoretical time `O((V+E) log V)` with an efficient binary heap and nonnegative edge weights. In this notebook, its running time is higher because decrease-key support is implemented in a simple teaching style.

## 8. Discussion

The three generators create mazes by building spanning trees, but their mechanics differ. Recursive backtracking grows one path deeply before backtracking, so it often creates long corridors. Prim and Kruskal choose edges according to random weights and MST rules, so they tend to create different branching patterns. The validation results show that all three produce perfect mazes under the tested conditions.

For solving, BFS is the correct baseline for shortest paths in unit-weight mazes. DFS is correct for reachability, but it should not be described as a shortest-path method. Dijkstra is more general than BFS because it handles nonnegative edge weights, but on these unit-weight mazes it should not produce a shorter route. The equality of BFS and Dijkstra path lengths is therefore a strong implementation check.

The most important implementation choice is the separation between the passage graph and the wall drawing. The algorithms operate on `graph` objects whose edges are valid moves. The visualization layer converts those moves into wall segments for display. This keeps the code close to the course graph framework while still producing maze images that are easy to interpret.

## 9. Required Notebook Revisions Before Submission

The generated `Final.ipynb` is a good starting point, but it needs several cleanup steps before submission:

1. Split the large implementation cell into smaller cells: setup, helpers, generators, solvers, validation, visualization, experiments, and citations.
2. Execute at least one `PrintGraph` cell on a small generated maze so the professor can see the required visualization tool in use.
3. Use `PrintMazeWithSolution` or the template's dual-graph drawing to show the final maze and highlighted solution path.
4. Remove or clearly mark Wilson's algorithm as optional. It is not supported by the professor-provided sources listed below, so it should not be part of the main cited implementation unless an approved source is added.
5. Add an explicit `validate_path` helper that checks start, goal, adjacency, and open-passage validity.
6. If entrance and exit openings are required in the wall image, remove those boundary wall segments from the wall graph rather than only marking start and goal points.
7. Keep rendering time separate from algorithm timing.

## 10. References

Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C. *Introduction to Algorithms*. Course textbook PDF: `Textbook/Introduction to Algorithms - DSA.pdf`.

Professor course notebook: `Final Project/Maze/Ch20(Graphs-CodeBase)-MAZE.ipynb`.

Professor maze template: `Final Project/Maze/Maze-Template.ipynb`.

Lee, C. Y. "An Algorithm for Path Connections and Its Applications." Local project PDF: `Final Project/Maze/An_Algorithm_for_Path_Connections_and_Its_Applications-1961.pdf`.

Hadlock, F. O. "A shortest path algorithm for grid graphs." Local project PDF: `Final Project/Maze/Networks - Winter 1977 - Hadlock - A shortest path algorithm for grid graphs.pdf`.

Soukup, J. "Fast Maze Router." Local project PDF: `Final Project/Maze/Fast_Maze_Router-Soukup1978.pdf`.

Shannon, C. E. "Presentation of a Maze-Solving Machine." Local project PDF: `Final Project/Maze/Presentation_of_a_MazeSolving_MachineTransactions_8th_Cybernetics_Conference_Josiah_Macy_Jr._Foundation_1952..pdf`.
