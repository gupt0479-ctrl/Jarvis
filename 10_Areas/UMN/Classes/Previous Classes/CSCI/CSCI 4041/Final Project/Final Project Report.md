---
type: class
input_kind: project
status: seed
created: 2026-05-03
updated: 2026-05-04
area:
  - "[[Final Project|Final Project]]"
  - "[[Maze Project|Maze Project]]"
tags:
  - "#class"
  - "#Project"
next:
  - "[[Maze Project Details|Maze Project Details]]"
---
# Maze

## Overview
- I am going to coding part: Implementation.
- The implementation should follow the professor's graph code style from the chapter 20-24 templates.
- The notebook must use the required visualization helpers, especially `PrintGraph` where the project asks for it.
- Any outside source used to design an algorithm needs a citation.

This is the main approach note for the maze final project. It should explain what to do, why each part matters, and how to turn the course graph material into a working notebook and report. The lower-level implementation notes, citation list, pseudocode-style breakdowns, validation checks, and experiment checklist are in [[Maze Project Details|Maze Project Details]]. The compact project index is [[Maze Project|Maze Project]].

## What the project really asks
The maze option is broader than "write one solver." It asks for a small graph-algorithm study with code, visualization, correctness reasoning, and experiments. In practical terms, the project has four deliverables:

1. **Maze generation**: generate mazes using multiple algorithms.
2. **Maze solving**: solve those mazes with BFS, DFS, and Dijkstra.
3. **Visualization**: show the maze and the path produced by the solvers.
4. **Analysis**: explain correctness, runtime, and how behavior changes as maze size grows.

The clean model is: **a maze is a sparse grid graph**. Each cell is a vertex. A possible move between neighboring cells is a candidate edge. An open passage is an edge that exists in the generated maze. A wall means the candidate edge is absent. This connects directly to [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11|Week - 11]] and [[Chapter - 20|Chapter - 20]], where graph representations, BFS, DFS, predecessor pointers, and adjacency lists are the main tools.

A perfect maze is a useful special case: every cell is reachable, and there is exactly one simple path between any two cells. In graph terms, that means the passage graph is a spanning tree of the grid cells. This is why [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12|Week - 12]] and [[Chapter - 21|Chapter - 21]] matter even though we are drawing mazes rather than computing a traditional MST.

## Big design decision
Use this implementation set:

- **Recursive backtracking** for generator 1.
- **Randomized Prim** for generator 2.
- **Recursive division** for generator 3.
- **BFS, DFS, and Dijkstra** for solvers.

This is the best low-risk set because each generator is visually and conceptually different, but none requires the more complex probability arguments behind Wilson or Aldous-Broder. Recursive backtracking is basically randomized DFS over the grid. Randomized Prim is a frontier-growth algorithm related to the spanning-tree intuition from Prim's algorithm. Recursive division is different because it starts with open space and adds walls rather than starting with walls and carving passages.

The solver story is also clear. BFS is the baseline shortest-path solver for unit-weight mazes. DFS is the reachability contrast: it can find a valid path, but not necessarily the shortest path. Dijkstra is the nonnegative-weight shortest-path method from [[Week - 13|Week - 13]] and [[Chapter - 22|Chapter - 22]]. On normal mazes where every passage has weight 1, BFS and Dijkstra should return the same path length. That equality is one of the best sanity checks in the whole project.

## What to study first
Study in the order you will implement:

1. **Graph representation**: Review adjacency lists in [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11|Week - 11]] and [[Chapter - 20|Chapter - 20]]. A grid maze is sparse because each cell has at most four neighbors, so adjacency lists fit better than adjacency matrices.
2. **BFS and DFS**: Focus on colors, distances, predecessor fields, and path reconstruction. The project needs the final path, not just a true/false answer.
3. **Spanning tree intuition**: Review [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12|Week - 12]] and [[Chapter - 21|Chapter - 21]]. Recursive backtracking and randomized Prim both grow a connected acyclic passage graph by adding one new cell at a time.
4. **Dijkstra**: Review relaxation, priority queues, and nonnegative weights in [[Week - 13|Week - 13]] and [[Chapter - 22|Chapter - 22]].
5. **Maze-specific references**: Use Jamis Buck's maze pages for generator behavior and the local Lee/Hadlock/Soukup/Shannon papers for routing context. The exact citation set is in [[Maze Project Details#Citation Set|Maze Project Details > Citation Set]].

## Representation plan
Pick one representation early and use it everywhere. The easiest mental model is:

- A cell is a coordinate like `(row, col)`.
- The full grid has all possible neighboring pairs.
- The maze stores only open passages.
- A solver reads the open-passage adjacency list.

Do not mix three different representations unless the professor's template forces it. You can keep a grid/wall structure for visualization, but solver code should still see a clean graph interface: "given a cell, return its open neighbors." That keeps BFS, DFS, and Dijkstra simple.

The core helpers should be:

- `neighbors(cell)` for legal grid neighbors.
- `carve(a, b)` for opening a wall between adjacent cells.
- `open_neighbors(cell)` for solver traversal.
- `reset_state()` for clearing colors/distances/predecessors.
- `reconstruct_path(prev, start, goal)` for all solvers.
- `validate_maze()` and `validate_path()` for testing.

This helper layer matters because most bugs in this project will not be in the high-level algorithm idea. They will be in stale state, wall direction mistakes, path reconstruction, or a solver using a wall as if it were a passage.

## Notebook organization
The notebook should read like a controlled experiment, not like a pile of unrelated cells. A good order is:

1. **Imports and constants**: random seed handling, timing helpers, and any professor-provided classes.
2. **Maze representation**: grid dimensions, wall/passages, coordinate helpers, and graph conversion.
3. **Shared graph helpers**: reset, reconstruction, validation, counters.
4. **Generators**: recursive backtracking, randomized Prim, recursive division.
5. **Solvers**: BFS, DFS, Dijkstra.
6. **Visualization**: maze drawing and path highlighting.
7. **Small tests**: hand-checkable mazes and invariants.
8. **Experiments**: size loop, repeated seeds, tables, plots.
9. **Discussion cells**: short written interpretation for the final report.

This order also makes debugging easier. If recursive backtracking fails, the problem is probably in the representation or `carve`. If BFS fails after a valid maze is generated, the problem is probably in `open_neighbors`, reset logic, or predecessor reconstruction. If Dijkstra disagrees with BFS on a unit-weight maze, the problem is probably edge weights, heap update behavior, or stale state.

## Generator plan
Implement the generators in this order.

**Recursive backtracking first.** This gives you a working maze quickly and tests your wall-carving helpers. Use an explicit stack instead of true recursion. Start at a cell, mark it visited, repeatedly carve to random unvisited neighbors, and backtrack when stuck. The key invariant is that each carved edge connects the already-built maze to one new cell. That means no cycle is created, and the visited region stays connected. When every cell is visited, the maze is a spanning tree.

**Randomized Prim second.** This tests frontier logic. Start with one visited cell and a frontier of walls or candidate edges. Randomly pick a frontier item. If it connects exactly one visited cell to one unvisited cell, carve it and add the new cell's frontier edges. If both endpoints are already visited, ignore it. The key invariant is the same tree-growth idea: every accepted edge adds exactly one new cell.

**Recursive division third.** This generator is conceptually different, so it is good for comparison. Start with open space, add a wall across a region, leave one doorway, and recursively divide the subregions. The main invariant is connectivity: every wall split must leave a doorway so the two sides are not isolated. This algorithm creates long straight walls, so it gives the report a visual contrast with the two passage-carving methods.

Detailed generator notes are in [[Maze Project Details#Generator Details|Maze Project Details > Generator Details]].

## What to implement first
The fastest path to a working submission is not to implement every algorithm before testing anything. Build one thin vertical slice first:

1. Make a small grid.
2. Generate one recursive-backtracking maze.
3. Convert it to open-neighbor adjacency.
4. Run BFS from entrance to exit.
5. Reconstruct the path.
6. Validate the path.
7. Draw the maze and path.

Once that works, the rest of the project becomes extension rather than invention. Randomized Prim can reuse the same `carve`, visited set, and validation code. DFS can reuse the same `open_neighbors` and `reconstruct_path`. Dijkstra can reuse the same path reconstruction and then add weights/relaxation. Recursive division is the one piece that may need different wall logic, so it should come after the passage-carving pipeline is already stable.

## Solver plan
Write BFS, DFS, and Dijkstra behind one shared interface. Each solver should return:

- whether a path was found,
- a predecessor map,
- the reconstructed path,
- path length,
- counters such as visited cells, queue/stack/heap pops, and relaxations.

**BFS** should be your correctness baseline. In a unit-weight maze, BFS discovers cells in increasing number of moves from the start. If the path from BFS is invalid, the representation or predecessor logic is probably wrong.

**DFS** should be explained carefully. It is not "bad BFS"; it answers a different question. It proves reachability and gives a path based on exploration order. In a maze with long corridors, DFS may look good on some examples and poor on others. That contrast is useful for the report.

**Dijkstra** should use the same reconstruction logic as BFS. If all passage weights are 1, Dijkstra should match the BFS path length. If the project allows an optional weighted extension, Dijkstra becomes more interesting, but do not overclaim it for the required unit-weight case.

## Correctness strategy
The report should make correctness concrete. Use graph invariants and validation tests.

For generators:

- Every generated maze should have all cells reachable from the entrance.
- A perfect maze should have exactly $|V|-1$ undirected passage edges.
- Recursive backtracking and randomized Prim preserve acyclicity by carving only to unvisited cells.
- Recursive division preserves connectivity by leaving a doorway in each dividing wall.

For solvers:

- The returned path starts at the entrance.
- The returned path ends at the exit.
- Consecutive path cells are adjacent grid cells.
- Consecutive path cells are connected by open passages.
- BFS and Dijkstra return the same path length on unit-weight mazes.
- DFS returns a legal path if the maze is connected, but it may be longer.

These checks should exist in code, not only in prose. The final report can then say the implementation was validated using these invariants.

## Common failure points
The project has a few predictable traps:

- **Counting each undirected edge twice.** If passages are stored in both directions, divide the total by 2 when checking $|V|-1$.
- **Forgetting to reset state.** BFS, DFS, Prim, and Dijkstra all use visited/color/predecessor fields. Reusing stale fields can make a broken algorithm look correct.
- **Mixing wall coordinates and cell coordinates.** Recursive division often needs careful distinction between a cell, a wall line, and a doorway.
- **Timing visualization.** Rendering a figure can be slower than the graph algorithm. Keep drawing out of benchmark timings.
- **Comparing solvers on different random mazes.** Use the same generated maze when comparing BFS, DFS, and Dijkstra.
- **Overclaiming DFS.** DFS finds a path if one exists, but it is not a shortest-path algorithm.
- **Overclaiming Dijkstra on unit weights.** Dijkstra is more general than BFS, but on normal unit-weight mazes it should not produce a shorter path than BFS.

## Experiment plan
The experiment should answer two questions: how do runtimes grow, and how do different maze styles affect solver behavior?

Use several grid sizes, such as small debugging sizes (`5x5`, `10x10`) and larger benchmark sizes. For each size and generator, run multiple seeds. Keep generation timing separate from solving timing, and keep both separate from visualization. Drawing can dominate time and hide the algorithmic behavior.

Record counters in addition to wall-clock time:

- cells visited,
- queue pops for BFS,
- stack pops for DFS/backtracking,
- heap pops and relaxations for Dijkstra,
- frontier choices for randomized Prim,
- carved edges,
- dead-end count,
- solution-path length,
- average branching factor,
- rough corridor length.

The qualitative metrics matter because the project is about mazes, not only runtimes. Recursive backtracking should often create longer corridors. Randomized Prim should often create more short branches. Recursive division should create more straight-wall structure. If the screenshots show those patterns and the metrics support them, the report will be much stronger.

## How to discuss results
The discussion should connect observations back to algorithm mechanics. For example, if recursive backtracking has longer corridors, explain that the stack keeps following a path deeply before backtracking. If randomized Prim has many short dead ends, explain that the frontier grows from many boundary points rather than one deep path. If recursive division looks more geometric, explain that it places long walls across regions rather than carving one passage at a time.

For solvers, do not only say which one was faster. Say what each one was doing. BFS explores in distance layers, so its path length is the baseline. DFS follows one branch deeply, so it can get lucky or unlucky depending on neighbor order and maze shape. Dijkstra uses a priority queue and relaxation; on unit weights it should agree with BFS but may have more overhead. That is the algorithmic story the project is trying to surface.

## Final report structure
The submitted writeup can follow this structure:

1. **Problem model**: define a maze as a grid graph and explain why adjacency lists fit.
2. **Generation algorithms**: explain recursive backtracking, randomized Prim, and recursive division.
3. **Solving algorithms**: explain BFS, DFS, and Dijkstra.
4. **Correctness**: use spanning-tree, reachability, and shortest-path arguments.
5. **Complexity**: state runtimes in terms of $V$ cells and $E$ passages.
6. **Experiments**: describe sizes, seeds, counters, timing, and visual metrics.
7. **Discussion**: compare generator style and solver behavior.
8. **Citations**: cite course materials, Jamis Buck, and routing papers where used.

The goal is not to write a giant encyclopedia. The goal is to make the professor see that the notebook is organized around graph algorithms: representation, invariants, implementation, validation, and measured behavior.

## Immediate next steps
- [ ] Open `Maze-Template.ipynb` and identify required functions.
- [ ] Open `Ch20(Graphs-CodeBase)-MAZE.ipynb` and identify the graph/printing utilities to reuse.
- [ ] Implement the cell/neighbor/wall helpers.
- [ ] Implement recursive backtracking and validate `reachable == |V|` and `edges == |V|-1`.
- [ ] Implement BFS and path reconstruction.
- [ ] Add randomized Prim.
- [ ] Add recursive division.
- [ ] Add DFS and Dijkstra behind the same interface.
- [ ] Add experiment harness and screenshots.
- [ ] Write the final report using the structure above.

## Concepts used
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11|Week - 11]]
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12|Week - 12]]
- [[Week - 13|Week - 13]]
- [[Chapter - 20|Chapter - 20]]
- [[Chapter - 21|Chapter - 21]]
- [[Chapter - 22|Chapter - 22]]
- [[Maze Project|Maze Project]]
- [[Maze Project Details|Maze Project Details]]

## Post-submit reflection
- What failed first?
- What pattern repeats?
