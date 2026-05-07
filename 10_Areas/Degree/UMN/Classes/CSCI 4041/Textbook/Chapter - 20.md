---
type: class
input_kind: book
status: seed
created: 2026-04-06
updated: 2026-04-16
area:
  - "[[UMN Board]]"
  - "[[CSCI 4041 Board]]"
  - "[[Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Textbook"
next: "[[10_Areas/Degree/UMN/Classes/CSCI 4041/Week - 11|Week - 11]]"
---
# Chapter 20 - Graph Representations
Searching a graph is the process of systematically following edges to visit the vertices of a graph. Graph-searching algorithms discover structural information and serve as the foundation for many more complex algorithms.

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
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Week - 11#Chapter 20 - Graph Representations, BFS, and DFS|Week - 11 lecture reference]]
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Week - 12#Chapter 20 - Topological Sort and Strongly Connected Components|Week - 12 lecture reference]]
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Graphs/Graph Algorithms#Definition|Graph Algorithms concept]]
