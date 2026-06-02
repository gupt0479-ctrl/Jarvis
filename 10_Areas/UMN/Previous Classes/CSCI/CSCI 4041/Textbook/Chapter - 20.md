---
type: class
input_kind: book
status: sprout
created: 2026-04-06
updated: 2026-04-28
area:
  - "[[UMN Board]]"
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Textbook/Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Textbook"
next: "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11|Week - 11]]"
---
# Chapter 20 - Graph Representations
Searching a graph is the process of systematically following edges to visit the vertices of a graph. Graph-searching algorithms discover structural information and serve as the foundation for many more complex algorithms.

Searching a graph is the process of systematically following the edges of the graph to visit its vertices. This chapter covers basic graph-searching techniques—Breadth-First Search (BFS) and Depth-First Search (DFS)—and their applications in topological sorting and decomposing graphs into strongly connected components.

[!NOTE] **Note on Minimum Spanning Trees:** While the query mentions focusing on Minimum Spanning Trees, according to the provided textbook sources, MSTs are covered in **[[Chapter 21: Minimum Spanning Trees]]**. Chapter 20 provides the elementary searching algorithms that serve as the foundation for MST algorithms.

--------------------------------------------------------------------------------

20.1 Representations of Graphs

There are two standard ways to represent a graph G=(V,E), applicable to both directed and undirected graphs.

20.1.1 Adjacency-List Representation

Consists of an array Adj of ∣V∣ lists, one for each vertex. For a vertex u, Adj[u] contains all vertices v such that an edge (u,v) exists.

- **Space Complexity:** Θ(V+E).
- **Best For:** Sparse graphs (where ∣E∣ is much less than ∣V∣2).
- **Trade-off:** Provides a compact representation but searching for a specific edge (u,v) can take O(Adj[u]) time.

20.1.2 Adjacency-Matrix Representation

Uses a ∣V∣×∣V∣ matrix A=(aij​) where aij​=1 if an edge (i,j) exists, and 0 otherwise.

- **Space Complexity:** Θ(V2).
- **Best For:** Dense graphs or when edge existence checks must be constant time O(1).
- **Symmetry:** For undirected graphs, the matrix is its own transpose (A=AT).

[!IMPORTANT] **Indexing Translation:**

- **Textbook (1-origin):** The textbook indices vertices from 1 to ∣V∣.
- **Code (0-origin):** Most programming languages (Java, Python, C++) use indices 0 to ∣V∣−1. When implementing, subtract 1 from vertex identifiers or allocate arrays of size ∣V∣+1 and ignore index 0.

--------------------------------------------------------------------------------

20.2 Breadth-First Search (BFS)

BFS is a simple algorithm for searching a graph and serves as a prototype for many important algorithms (like Prim’s MST or Dijkstra’s shortest paths). It finds the shortest distance (minimum number of edges) from a source vertex s to all reachable vertices.

Mechanics

BFS uses three attributes for each vertex v:

1. v.color: **WHITE** (undiscovered), **GRAY** (frontier/discovered but neighbors not explored), or **BLACK** (finished/all neighbors explored).
2. v.d: Stores the distance from s to v.
3. v.π: Stores v's predecessor in the breadth-first tree.

The algorithm utilizes a **First-In, First-Out (FIFO) queue** to manage gray vertices.

Complexity and Shortest Paths

- **Running Time:** O(V+E).
- **Shortest-Path Property:** BFS correctly computes v.d=δ(s,v) for all reachable v.
- **Breadth-First Tree:** The v.π attributes induce a tree rooted at s containing shortest paths to all reachable vertices.

--------------------------------------------------------------------------------

20.3 Depth-First Search (DFS)

DFS searches "deeper" in the graph whenever possible, exploring edges out of the most recently discovered vertex until all its edges are processed, then backtracking.

Timestamps

DFS assigns two timestamps to each vertex u:

1. **Discovery time (**u.d**):** When u is first discovered and painted gray.
2. **Finishing time (**u.f**):** When the search finishes examining u's adjacency list and paints u black.
3. **Parenthesis Theorem:** For any two vertices, their discovery/finish intervals are either entirely disjoint or one is nested within the other.

Classification of Edges

1. **Tree edges:** Edges in the depth-first forest.
2. **Back edges:** Connects u to an ancestor v (includes self-loops).
3. **Forward edges:** Nontree edges connecting u to a descendant v.
4. **Cross edges:** All other edges (between subtrees or non-ancestral nodes).

**Complexity:** Θ(V+E).

--------------------------------------------------------------------------------

20.4 Topological Sort

A **topological sort** of a **Directed Acyclic Graph (DAG)** is a linear ordering of all its vertices such that if G contains an edge (u,v), then u appears before v in the ordering.

The Algorithm

1. Call `DFS(G)` to compute finishing times v.f for each vertex.
2. As each vertex is finished, insert it onto the **front** of a linked list.
3. Return the linked list.
4. **Lemma:** A directed graph is acyclic if and only if a DFS yields no back edges.
5. **Complexity:** Θ(V+E).

--------------------------------------------------------------------------------

20.5 Strongly Connected Components (SCC)

An SCC is a maximal set of vertices C such that for every pair u,v∈C, both u is reachable from v and v is reachable from u.

The SCC Algorithm

This algorithm uses the **transpose** of the graph GT (where all edges are reversed).

1. Call `DFS(G)` to compute finishing times u.f.
2. Compute GT.
3. Call `DFS(G^T)`, but in the main loop, consider vertices in order of **decreasing** finishing times (u.f) from the first pass.
4. Each tree in the resulting depth-first forest is a separate SCC.

**Complexity:** Θ(V+E).

## 20.1 Representations of Graphs
There are two standard ways to represent a graph `G = (V, E)`, both applicable to directed and undirected graphs.

### Adjacency-List Representation
An adjacency-list representation consists of an array `Adj` of `|V|` lists, one for each vertex in `V`. For each vertex `u`, the list contains all vertices `v` such that there is an edge `(u,v) in E`.
- **Best For:** Sparse graphs, where `|E|` is much less than `|V|^2`.
- **Space Complexity:** `Theta(V + E)`.
- **Trade-off:** More space-efficient than a matrix, but edge lookup is not constant-time in the general case.

### Adjacency-Matrix Representation
This representation uses a `|V| x |V|` matrix `A = (a_ij)` such that `a_ij = 1` if edge `(i,j)` exists and `0` otherwise.
- **Best For:** Dense graphs or settings where quick edge-existence tests matter.
- **Space Complexity:** `Theta(V^2)`.
- **Weighted Graphs:** Edge weights can be stored directly as matrix entries.

> [!NOTE] **Indexing Translation:** The textbook uses **1-origin indexing** for vertices. The lecture code uses **0-indexed** vertex objects and arrays. Conceptually the algorithms are the same; only the indexing changes.

### Lecture Emphasis
The lecture code base explicitly implements both representations so you can compare them as actual Python classes, not just abstract diagrams.

```python
class matrixgraph:
    """an adjacency matrix graph"""
    
    class vertex:
        def __init__(self,name,index):
            self.name = name
            self.index = index
            self.color = "White"
            self.d = float("inf")
            self.f = None
            self.prev = None
            self.key = None
            self.x = None
            self.y = None

        def __lt__(self,other):
            return self.key < other.key
        
        def __str__(self):
            return str(self.name)
    
    def __init__(self,n):
        self.A = [[0 for j in range(n)] for i in range(n)]
        self.n = n
        self.V = [self.vertex("x_"+str(i),i) for i in range(n)]
    
    def add_edge(self,i,j,weight=1):
        self.A[i][j] = weight
    
    def adj(self,u):
        u_idx = u.index
        out = []
        for j in range(self.n):
            if self.A[u_idx][j]!=0:
                out.append(self.V[j])
        return out
```

```python
class graph:
    """an adjacency list graph"""
    
    class vertex:
        def __init__(self,name,index):
            self.name = name
            self.index = index
            self.color = "White"
            self.d = float("inf")
            self.f = None
            self.prev = None
            self.key = None
            self.x = None
            self.y = None
        
        def __lt__(self,other):
            return self.key < other.key
        
        def __str__(self):
            return str(self.name)
    
    class edge:
        def __init__(self,vertex,weight=1):
            self.weight = weight
            self.vertex = vertex
            self.next = None
    
    def __init__(self,n):
        self.A = [self.edge(None,None) for i in range(n)]
        self.n = n
        self.V = [self.vertex("x_"+str(i),i) for i in range(n)]
    
    def add_edge(self,i,j,weight=1):
        node = self.A[i]
        while node.next:
            node = node.next
            if node.vertex == j:
                return
        new_node = self.edge(vertex=j,weight=weight)
        node.next = new_node
```

The adjacency-list `graph` class is the main representation used for BFS, DFS, topological sort, SCC, and MSTs later. The adjacency-matrix `matrixgraph` is useful when the algorithm needs direct weight lookup or dense connectivity.

## 20.2 Breadth-First Search (BFS)
Breadth-first search is a simple archetype for graph searching that finds the shortest distance, in number of edges, from a source vertex `s` to every reachable vertex.
1. *Mechanics*
	Each vertex `v` stores:
	1. `v.color`: White, Gray, or Black.
	2. `v.d`: distance from the source.
	3. `v.pi` or `v.prev`: predecessor in the breadth-first tree.
	The algorithm uses a FIFO queue to manage the current frontier.
2. *Complexity and Shortest Paths*
	- **Total Running Time:** `O(V + E)`.
	- **Shortest-Path Property:** At termination, `v.d = delta(s,v)` for every reachable vertex `v`.
	- **Breadth-First Tree:** The predecessor subgraph gives a shortest-path tree from the source.

### Lecture Emphasis
The lecture BFS implementation uses `collections.deque` and explicitly colors vertices as they move from undiscovered to frontier to finished.

```python
from collections import deque 

def BFS(G,s):
    """a breadth-first search of the vertices of graph G"""
    count = 0
    for u in G.V:
        u.color = "White"
        u.d = float("inf")
        u.prev = None
    s.color = "Gray"
    s.d = 0
    s.prev = None
    Q = deque()
    Q.append(s)
    while Q:
        u = Q.popleft()
        print(u)
        for v in G.adj(u):
            if v.color == "White":
                v.color = "Gray"
                v.d = u.d + 1
                v.prev = u
                Q.append(v)
        u.color = "Black"
```

The essential lecture interpretation is that Gray means "discovered but not fully processed yet." BFS processes vertices in layers, and that is exactly why it computes shortest path length in unweighted graphs.

## 20.3 Depth-First Search (DFS)
Depth-first search goes as deep as possible before backtracking.
1. *Timestamps*
	DFS records two timestamps for each vertex `u`:
	1. **Discovery time (`u.d`)**
	2. **Finishing time (`u.f`)**
	The intervals `[u.d, u.f]` are either nested or disjoint, which gives DFS much richer structure than BFS.
2. *Classification of Edges*
	DFS classifies edges into:
	1. Tree edges
	2. Back edges
	3. Forward edges
	4. Cross edges
	- **Complexity:** `O(V + E)`.

### Lecture Emphasis
The notebook's DFS code is the reference implementation for the rest of the graph material.

```python
def DFS(G):
    """Depth-First Search from CLRS - Section 20.3"""
    
    def DFS_VISIT(G,u):
        """Depth-First Search vertex u - visit procedure"""
        nonlocal time
        print(u)
        u.d = time
        u.color = "Gray"
        for v in G.adj(u):
            if v.color=="White":
                v.prev = u
                DFS_VISIT(G,v)
        time = time + 1
        u.f = time
        u.color = "Black"

    for u in G.V:
        u.color = "White"
        u.prev = None
    time = 0
    for u in G.V:
        if u.color=="White":
            print("depth first tree:")
            DFS_VISIT(G,u)
            print("\n")
```

The code makes the recursive structure explicit. Every time DFS discovers a White neighbor, that edge becomes part of the DFS tree. Finishing times are assigned only after all descendants are done, which is why they are so useful for topological sort and SCC.

### CodingHW8 Extensions
Coding Homework 8 asks you to modify and extend the DFS implementation:
- compute in-degree and out-degree for adjacency-list graphs
- construct the reverse graph `G^T`
- clean a multigraph into a simple undirected graph
- replace DFS recursion with an explicit stack
- print every edge together with its edge type

These are important because they turn the CLRS pseudocode into operational graph-tooling code.

## 20.4 Topological Sort
A **topological sort** of a DAG `G = (V, E)` is a linear ordering of its vertices such that every directed edge `(u,v)` places `u` before `v`.
1. *Key Concept: DAGs*
	Topological sorting is defined only for directed acyclic graphs. If a directed cycle exists, no such ordering is possible.
	- **Lemma 20.11:** A directed graph is acyclic if and only if DFS yields no back edges.
2. *The Algorithm*
	1. Run `DFS(G)` to compute finishing times.
	2. Insert each vertex onto the front of a list when it finishes.
	3. Return the list.
	- **Complexity:** `Theta(V + E)`.

### Lecture Emphasis
The notebook implementation makes cycle detection explicit by checking for Gray neighbors during DFS.

```python
def Topological_Sort(G):
    """Topological Sorting Algorithm from CLRS - Section 20.4"""
    
    def DFS_VISIT(G,u):
        """Depth-First Search vertex u - visit procedure"""
        nonlocal time,L
        u.d = time
        u.color = "Gray"
        for v in G.adj(u):
            if v.color=="White":
                v.prev = u
                DFS_VISIT(G,v)
            elif v.color=="Gray":
                print("Cycle Detected !!!")
                print("\tBack Edge at",v)
        time = time + 1
        u.f = time
        u.color = "Black"
        L.append(u)

    L = []
    for u in G.V:
        u.color = "White"
        u.prev = None
    time = 0
    for u in G.V:
        if u.color=="White":
            DFS_VISIT(G,u)
    L.reverse()    
    return L
```

The key invariant is that if `(u,v)` is an edge in a DAG, then `u.f > v.f`. Reversing the finishing-time order gives a valid topological order.

## 20.5 Strongly Connected Components (SCC)
A strongly connected component of a directed graph is a maximal set of vertices where every vertex is reachable from every other vertex in the set.
1. *The SCC Algorithm*
	1. Run `DFS(G)` to compute finishing times.
	2. Construct the transpose graph `G^T`.
	3. Run DFS on `G^T` in decreasing order of finishing times from step 1.
	4. Each DFS tree in the second pass is one SCC.

### Lecture Emphasis
The notebook implements both the reverse graph and the two-pass SCC algorithm directly.

```python
def construct_reverse_graph(G):
    """constructs and returns the graph G^T (the reverse graph of directed graph G)"""
    Gt = graph(G.n)
    Gt.V = [u for u in G.V]
    
    for u in G.V:
        node = G.A[u.index]
        while node.next:
            node = node.next
            Gt.add_edge(node.vertex,u.index)
    
    return Gt
```

```python
def Strongly_Connected_Components(G):
    """this is the algorithm on page 577 of the CLRS textbook"""
    print("initial DFS of G")
    DFS(G)

    print("\nconstructing the reverse graph ...")
    Gt = construct_reverse_graph(G)
    
    print("\nfinal DFS of G^T")
    DFS_SCC(Gt)
```

The lecture's practical takeaway is that the first DFS is not finding SCCs directly. It is computing the finish-time order that makes the second DFS on the reversed graph work cleanly.

## Summary Links
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11#Chapter 20 - Graph Representations, BFS, and DFS|Week - 11 lecture reference]]
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12#Chapter 20 - Topological Sort and Strongly Connected Components|Week - 12 lecture reference]]
- [[Graph Algorithms#Definition|Graph Algorithms concept]]

---

## Overview
- Chapter 20 is the foundation for graph algorithms: representations, BFS, DFS, topological sorting, and strongly connected components.
- In CSCI 4041, this chapter feeds directly into MSTs, shortest paths, maximum flow, and the maze final-project option.
- The lecture code builds a reusable graph class first, then layers traversal algorithms on top of it.

## Core Definitions
- **Graph:** `G=(V,E)`, directed or undirected.
- **Adjacency list:** stores outgoing neighbors for each vertex; space `Theta(V+E)`.
- **Adjacency matrix:** stores a `V x V` table; space `Theta(V^2)`.
- **BFS:** explores outward in layers from a source using a FIFO queue.
- **DFS:** explores as deep as possible before backtracking, recording discovery/finish times.
- **Topological order:** linear order of DAG vertices where every edge points forward.
- **Strongly connected component:** maximal set of vertices mutually reachable from each other.

## Main Algorithms
- `BFS(G,s)`: initializes colors/distances/predecessors and explores by queue.
- `DFS(G)`: calls `DFS-VISIT` on each white vertex, producing a depth-first forest.
- `TOPOLOGICAL-SORT`: run DFS and reverse finish order.
- `STRONGLY-CONNECTED-COMPONENTS`: run DFS on `G`, build `G^T`, then DFS in decreasing finish-time order.
- Homework-supported tasks: out-degree/in-degree, transpose graph, equivalent undirected graph, alternative topological sort, and component graph.

## Correctness Ideas
- BFS correctness is a layer invariant: vertices are discovered in nondecreasing distance from the source.
- DFS correctness uses color states: white undiscovered, gray active, black finished.
- Topological sort works because in a DAG, every edge goes from a vertex with later finish time to earlier finish time, so reversing finish order is valid.
- SCC correctness depends on the first DFS finish-time order making source components in the component graph appear first in the second pass on `G^T`.

## Complexity
- Adjacency-list BFS/DFS/topological sort/SCC are `Theta(V+E)`.
- Adjacency-matrix neighbor scanning costs `Theta(V)` per vertex, often `Theta(V^2)` total.
- BFS space is `O(V)` for queue, color, distance, and predecessor arrays.
- DFS space is `O(V)` for recursion stack and timestamps.

## Lecture Emphasis
- `Lectures/Week - 11/Ch20_Graphs_and_BFS.ipynb` introduces the graph class and BFS.
- `Lectures/Week - 11/Ch20_AdjacencyLists_and_DFS.ipynb` shifts to adjacency lists and DFS timestamps.

```python
while Q:
    u = Q.popleft()
    for v in G.adj(u):
        if v.color == "White":
            v.color = "Gray"
            v.d = u.d + 1
            v.prev = u
            Q.append(v)
```

- `Lectures/Week - 12/Ch20_Topological_Sort_Connected_Components.ipynb` uses DFS finish order for both topological sorting and SCC.
- `Homework/Coding/CodingHW_8(chapter20-CLRS).ipynb` directly supports graph representation exercises.
- `Homework/Coding/CodingHW_9(chapter20-23-CLRS).ipynb` extends Chapter 20 with alternative topological sort and component graph tasks.
- [[Maze Project|Maze Project]] is supported by its project note: it models mazes as grid graphs and uses BFS/DFS.
- Weekly/concept links: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11|Week - 11]], [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12|Week - 12]], [[Graph Algorithms|Graph Algorithms]].

## Examples
- BFS from a source in an unweighted graph computes shortest path length in number of edges.
- DFS discovery/finish intervals nest for descendants.
- For a DAG, reversing DFS finish order gives a dependency-respecting order.
- SCC uses the transpose graph; copying edges without reversing them breaks the algorithm.

## Connections
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11|Week - 11]]
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12|Week - 12]]
- [[Graph Algorithms|Graph Algorithms]]
- [[Maze Project|Maze Project]]
- Source homework read: `Homework/Coding/CodingHW_8(chapter20-CLRS).ipynb`, `Homework/Coding/CodingHW_9(chapter20-23-CLRS).ipynb`, and `Homework/Paper/Paper HW - 8 (Ch - 20).pdf`.
- TODO: source gap - no vault Homework/Paper Homework note exists for direct wikilinking.

## Common Pitfalls
- Using BFS shortest-path claims on weighted graphs.
- Confusing DFS discovery order with topological order.
- Forgetting to reverse edges when constructing `G^T`.
- Running SCC's second DFS in arbitrary order.
- Assuming adjacency matrix is always simpler; it can hide a `Theta(V^2)` cost.

## Review Checklist
- [ ] Choose adjacency list or matrix based on graph density and operation needs.
- [ ] Implement BFS with colors, distances, predecessors, and a queue.
- [ ] Implement DFS with discovery/finish times.
- [ ] Derive topological sort from DFS finish order.
- [ ] Trace SCC using `G`, `G^T`, and decreasing finish-time order.
