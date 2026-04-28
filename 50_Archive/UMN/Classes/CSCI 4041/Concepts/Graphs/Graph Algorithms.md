---
type: concept
course: CSCI 4041
status: sprout
mastery (1/10): 3
created: 2026-04-16
topics:
  - "[[DSA]]"
  - "[[CSCI 4041 Board]]"
  - "[[50_Archive/UMN/Classes/CSCI 4041/Week - 11|Week - 11]]"
  - "[[50_Archive/UMN/Classes/CSCI 4041/Week - 12|Week - 12]]"
  - "[[Chapter - 20]]"
related:
  - "[[Minimum Spanning Trees]]"
---
# [[50_Archive/UMN/Classes/CSCI 4041/Concepts/Graphs/Graph Algorithms]]
## MOC
- [[50_Archive/UMN/Classes/CSCI 4041/Week - 11#Chapter 20 - Graph Representations, BFS, and DFS|Week - 11]]
- [[50_Archive/UMN/Classes/CSCI 4041/Week - 12#Chapter 20 - Topological Sort and Strongly Connected Components|Week - 12]]
- [[Chapter - 20#20.1 Representations of Graphs|Chapter - 20 - Representations]]
- [[Chapter - 20#20.5 Strongly Connected Components (SCC)|Chapter - 20 - SCC]]
## Definition
- **Graph**: a structure `G = (V, E)` with a set of vertices and a set of edges.
- **Adjacency list**: a representation that stores, for each vertex, the list of outgoing neighbors.
- **Adjacency matrix**: a `V x V` representation storing whether or how strongly vertices are connected.
- **BFS**: breadth-first search, which explores by layers from a source.
- **DFS**: depth-first search, which explores by recursive descent before backtracking.
- **Topological sort**: a linear ordering of a DAG's vertices so every directed edge points forward.
- **SCC**: a maximal set of vertices that are mutually reachable.
## Core Ideas (Textbook)
### Graph Representations
- Adjacency lists use `Theta(V+E)` space and are the standard choice for sparse graphs and traversals.
- Adjacency matrices use `Theta(V^2)` space and are natural for dense graphs or constant-time edge lookup.
### BFS
- Uses White/Gray/Black colors, predecessor pointers, and a FIFO queue.
- Computes shortest path length in number of edges in an unweighted graph.
- Runs in `O(V+E)` on adjacency-list graphs.
### DFS
- Uses recursive exploration and timestamps.
- Discovery time and finish time expose nested structure in the search forest.
- Runs in `O(V+E)`.
### Topological Sort + SCC
- Topological sort is DFS finishing order reversed, but only for DAGs.
- SCC uses DFS on `G`, then DFS on the transpose graph `G^T` in decreasing finish-time order.
## Core Ideas (Lecture)
### Graph code base
The lecture uses both adjacency-matrix and adjacency-list graph classes, but almost every later algorithm uses the adjacency-list class.
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
```
### BFS
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
BFS is the lecture's shortest-path template for unweighted graphs because Gray vertices form the current frontier layer.
### DFS
```python
def DFS(G):
    """Depth-First Search from CLRS - Section 20.3"""
    
    def DFS_VISIT(G,u):
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
DFS timestamps are the lecture's main bridge to topological sort and SCC.
### Topological Sort + SCC
```python
def Topological_Sort(G):
    """Topological Sorting Algorithm from CLRS - Section 20.4"""
    
    def DFS_VISIT(G,u):
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
## Proof / Reasoning Toolkit
### BFS Checklist
1. Initialize all vertices White and infinitely far away.
2. Set source distance to 0 and push it into the queue.
3. Discover only White neighbors.
4. Gray means frontier, Black means finished.
### DFS Checklist
1. Discovery time when entering.
2. Finish time when every descendant is complete.
3. Tree edges are created only to White vertices.
4. Gray encounters signal an ancestor on the current recursion stack.
### Topological Sort Checklist
1. Verify the graph is acyclic.
2. Run DFS to compute finish times.
3. Reverse finish-time order.
4. Every directed edge must point left to right in the final ordering.
### SCC Checklist
1. Run DFS on `G`.
2. Build `G^T`.
3. Run DFS on `G^T` in decreasing finish-time order from the first pass.
4. Each second-pass DFS tree is one SCC.
## Complexity + Tradeoffs
| Structure / Algorithm | Time                                 | Space / Tradeoff                   |
| --------------------- | ------------------------------------ | ---------------------------------- |
| Adjacency list        | neighbor scan proportional to degree | `Theta(V+E)`                       |
| Adjacency matrix      | constant-time edge check             | `Theta(V^2)`                       |
| BFS                   | `O(V+E)`                             | shortest path in unweighted graphs |
| DFS                   | `O(V+E)`                             | timestamps expose deeper structure |
| Topological sort      | `O(V+E)`                             | valid only on DAGs                 |
| SCC                   | `O(V+E)` plus transpose construction | needs two DFS passes               |
## Canonical Examples (Max 5)
### 1. BFS from a source
- **Goal:** compute shortest path lengths in edges.
- **Key steps:** queue the source, discover White neighbors, assign `d = u.d + 1`.
- **Common mistake:** using BFS distance logic on weighted graphs.
### 2. DFS timestamp nesting
- **Goal:** understand discovery and finish intervals.
- **Key steps:** note that descendants finish before ancestors finish.
- **Common mistake:** mixing up discovery order with topological order.
### 3. Topological sort on a DAG
- **Goal:** produce a dependency-respecting order.
- **Key steps:** DFS, collect finished vertices, reverse.
- **Common mistake:** forgetting that a cycle makes topological sort impossible.
### 4. Reverse graph construction
- **Goal:** build `G^T`.
- **Key steps:** for every edge `(u,v)` in `G`, insert `(v,u)` in `G^T`.
- **Common mistake:** copying the edges without reversing them.
### 5. SCC two-pass structure
- **Goal:** separate maximal mutually reachable groups.
- **Key steps:** finish times on `G`, second DFS on `G^T` in decreasing finish-time order.
- **Common mistake:** running the second DFS in arbitrary vertex order.
## Practice Map
- BFS on grids
- BFS / shortest path in unweighted graphs
- DFS connected components
- Cycle detection in directed graphs
- Course schedule / topological ordering
## Mini-test
1. Why does BFS compute shortest-path distance only in unweighted graphs?
2. What extra information does DFS provide that BFS does not?
3. Why does topological sort rely on finishing times?
4. What is the transpose graph `G^T`?
5. Why does SCC require two DFS passes instead of one?
## Flashcards
#cards/CSCI4041
1. Adjacency-list space::`Theta(V+E)`.
2. Adjacency-matrix space::`Theta(V^2)`.
3. BFS main data structure::FIFO queue.
4. DFS timestamps::Discovery time and finishing time.
5. Topological order source::Reverse DFS finishing order on a DAG.
6. SCC second pass::DFS on `G^T` in decreasing finish-time order from the first pass.
7. Gray vertex in DFS::A vertex currently on the recursion stack / active search path.
