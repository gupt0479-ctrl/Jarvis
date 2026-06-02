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
  - "[[Graph Algorithms|Graph Algorithms]]"
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11|Week - 11]]"
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12|Week - 12]]"
  - "[[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 13|Week - 13]]"
  - "[[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 14|Week - 14]]"
---
# Final Project
## Overview
The final project applies the graph algorithms from Weeks 11–14 to one of three application domains. Each option uses the course adjacency-list graph code base from [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11|Week - 11]] and [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12|Week - 12]] as its foundation.
## Project Options
### Maze (chosen)
- [[Maze Project|Maze Project]] — maze generation and solving
- Generates a maze as a random spanning tree of a grid graph, then solves it with BFS or DFS
- Core algorithms: BFS, DFS, spanning tree generation
- Source: `Final Project/Maze/Ch20(Graphs-CodeBase)-MAZE.ipynb`, `Maze-Template.ipynb`
- Reference papers include Lee's path connection algorithm (1961) and Soukup's fast maze router (1978)
### Heuristic Pathfinding
- [[Heuristic Pathfinding Project|Heuristic Pathfinding Project]] — A* and heuristic search
- Extends Dijkstra with a heuristic estimate to guide search toward the goal
- Core algorithms: A* search, Dijkstra's algorithm, admissible and consistent heuristics
- Source: `Final Project/Heuristic Pathfinding/Ch20(Graphs-CodeBase)-HeuristicSearch.ipynb`, `HeuristicPathfinding-Template.ipynb`
- Reference papers include Hart, Nilsson, Raphael's original A* paper (1968)
### Network Flow
- [[Network Flow Project|Network Flow Project]] — distribution network flow
- Maximizes flow from source to sink using Ford-Fulkerson with augmenting paths
- Core algorithms: Ford-Fulkerson, Edmonds-Karp, residual graphs, max-flow min-cut theorem
- Source: `Final Project/Network Flow/Ch20(Graphs-CodeBase)-NETWORK.ipynb`, `Distribution-Network-Template.ipynb`
- Reference papers include Ford and Fulkerson's original max-flow paper (1956)
## Chosen Project: Maze
The maze project models a 2D grid as a graph. Each cell is a vertex, and edges connect adjacent cells. Maze generation removes walls to create a random spanning tree, which guarantees exactly one path between any two cells. Solving then uses BFS (for shortest path) or DFS (for any path) to find a route from start to finish.
This project ties directly to the graph traversal algorithms from [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11|Week - 11]] (BFS and DFS) and the graph code base from [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12|Week - 12]]. The spanning tree generation connects to [[Chapter - 21|Chapter - 21]] (minimum spanning trees), though the maze version uses a random spanning tree rather than a minimum-weight one.
The key insight is that BFS on an unweighted grid graph computes shortest-path distance in number of cells, which is exactly what "shortest maze path" means. DFS finds a path but not necessarily the shortest one, which makes the BFS vs DFS comparison a natural part of the project analysis.
## Concept Links
- [[Graph Algorithms|Graph Algorithms]] — BFS, DFS, graph representations
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11|Week - 11]] — BFS and DFS introduction
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12|Week - 12]] — topological sort, connected components, graph code base
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 13|Week - 13]] — shortest paths (Dijkstra, Bellman-Ford)
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 14|Week - 14]] — maximum flow
- [[Chapter - 20|Chapter - 20]] — graph representations, BFS, DFS
- [[Chapter - 21|Chapter - 21]] — minimum spanning trees
- [[Chapter - 22|Chapter - 22]] — single-source shortest paths
- [[Chapter - 24|Chapter - 24]] — maximum flow