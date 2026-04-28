---
type: class
input_kind: lecture
status: seed
created:
updated: 2026-04-16
area:
  - "[[UMN Board]]"
tags:
next: []
---
# Entire Week
## What you must be able to do
- [[Chapter - 20#20.1 Representations of Graphs|Chapter 20.1]], [[Chapter - 20#20.2 Breadth-First Search (BFS)|Chapter 20.2]], and [[Chapter - 20#20.3 Depth-First Search (DFS)|Chapter 20.3]]: explain graph representations, BFS, DFS, predecessor trees, timestamps, and `O(V+E)` runtime.
- [[50_Archive/UMN/Classes/CSCI 4041/Concepts/Graphs/Graph Algorithms#Core Ideas (Textbook)|Graph Algorithms - Core Ideas (Textbook)]], [[50_Archive/UMN/Classes/CSCI 4041/Concepts/Graphs/Graph Algorithms#Core Ideas (Lecture)|Graph Algorithms - Core Ideas (Lecture)]], and [[Chapter - 20#20.1 Representations of Graphs|Chapter - 20]]: compare adjacency-list and adjacency-matrix representations and explain why the lecture code base prefers adjacency lists for traversal algorithms.
- [[50_Archive/UMN/Classes/CSCI 4041/Concepts/Graphs/Graph Algorithms#Canonical Examples (Max 5)|Graph Algorithms - Canonical Examples]]: trace BFS level discovery, DFS tree growth, timestamps, and reverse-graph construction.
- [[50_Archive/UMN/Classes/CSCI 4041/Concepts/Graphs/Graph Algorithms#Practice Map|Graph Algorithms - Practice Map]]: connect the week's content to BFS/DFS grid problems, connected components, and directed-graph reasoning.
## Key ideas (textbook)
- **20.1 Graph Representations**: Graphs can be stored either as adjacency lists or adjacency matrices. Adjacency lists use `Theta(V+E)` space and are better for sparse graphs and traversal algorithms. Adjacency matrices use `Theta(V^2)` space and are better when dense connectivity or constant-time edge lookup matters.
- **20.2 BFS**: Breadth-first search explores a graph layer by layer using a FIFO queue. It colors vertices White, Gray, and Black, computes shortest-path distance in number of edges from the source, and builds a breadth-first tree through predecessor pointers.
- **20.3 DFS**: Depth-first search goes as deep as possible before backtracking. Its discovery and finishing times expose much more structure than BFS, which is why it becomes the engine for topological sort and strongly connected components in the following week.
- **Traversal Complexity**: Both BFS and DFS run in `O(V+E)` on adjacency-list graphs because each vertex is initialized and each edge is explored a constant number of times. This complexity statement is one of the most important recurring graph facts in the course.
## Concepts created / updated today
- [[50_Archive/UMN/Classes/CSCI 4041/Concepts/Graphs/Graph Algorithms#Definition|Graph Algorithms]]
- [[50_Archive/UMN/Classes/CSCI 4041/Concepts/Graphs/Graph Algorithms#Core Ideas (Lecture)|Graph Algorithms - BFS and DFS]]
- [[Chapter - 20#20.2 Breadth-First Search (BFS)|Chapter - 20 - BFS]]
## Lecture
### Chapter 20 - Graph Representations, BFS, and DFS
This week is the first real graph week, so the main conceptual job is learning how the class wants graphs to be represented before it wants them to be searched. The lecture starts with the graph model itself: a graph `G = (V, E)` is a set of vertices and a set of edges that represent relationships among those vertices. From there the course quickly shifts to representation, because once the graph is in memory, the representation controls which operations are easy. The lecture code base includes both an adjacency-matrix graph and an adjacency-list graph. The matrix version is conceptually straightforward and useful for dense weighted graphs, but the adjacency-list version is the one that actually powers BFS, DFS, topological sort, SCC, and MST work later. That is because traversal wants "who are the neighbors of this vertex?" far more often than it wants "does edge `(u,v)` exist?" in constant time.

BFS was presented as the cleanest search template: initialize every vertex as White and infinitely far away, make the source Gray at distance 0, push it into a queue, then repeatedly pop the oldest frontier vertex and discover all still-White neighbors. The reason BFS matters is not just traversal order. On an unweighted graph, it computes shortest-path distance in number of edges. The predecessor pointers define the breadth-first tree, and the `d` values tell you exactly which layer each vertex belongs to. DFS is different in purpose and in feel. Instead of exploring by layers, it dives down one path until it cannot go deeper. That is why timestamps matter. Discovery time tells you when the search first entered a vertex, and finish time tells you when its entire descendant subtree was completed. Those timestamps are the hidden structure that makes the next week's topological sort and SCC algorithms work.

The CodingHW8 prompts also matter this week because they turn the graph code into a toolkit rather than a single lecture demo. Computing in-degree and out-degree, constructing the reverse graph, cleaning a multigraph, replacing recursion with an explicit stack, and labeling DFS edge types are all ways of learning the graph representation by using it.

### Jupyter Notebooks
#### Ch20_Graphs_and_BFS.ipynb
The BFS notebook introduces the adjacency-matrix graph class and the first traversal algorithm.

```python
class graph:
    """an adjacency matrix graph"""
    
    class vertex:
        def __init__(self,name,index):
            self.name = name
            self.index = index
            self.color = "White"
            self.d = float("inf")
            self.f = None
            self.prev = None
            self.x = None
            self.y = None
        
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
The important thing to notice is how color and queue state line up. White means undiscovered, Gray means currently on the frontier, and Black means fully processed. That makes the layer-by-layer nature of BFS very explicit.
#### Ch20_AdjacencyLists_and_DFS.ipynb
This notebook switches to the adjacency-list representation and then adds DFS.
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
        def __init__(self,vertex,weight=1,name=""):
            self.weight = weight
            self.vertex = vertex
            self.next = None
    
    def __init__(self,n):
        self.A = [self.edge(None,None) for i in range(n)]
        self.n = n
        self.V = [self.vertex("x_"+str(i),i) for i in range(n)]
```

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

DFS is where timestamps first appear, and that is the main concept to carry forward. The recursive call stack itself is the depth-first tree while the algorithm is running.
#### CodingHW_8(chapter20-CLRS).ipynb
Homework 8 turns the graph representation into a set of actual graph utilities.
```python
def construct_reverse_graph(G):
    """constructs and returns the graph G^T (the reverse graph of directed graph G)"""
    Gt = graph(G.n)
    ####################################################
    # insert your code here
    
    
    
    
    return Gt
```
```python
def DFS_with_edge_type(G):
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
```

Even the partially completed homework scaffolds are useful study material because they reveal exactly which graph operations the course expects you to know how to implement on top of the core graph class.

## Examples worth keeping
- **Adjacency list versus matrix**: list for sparse traversal-heavy algorithms, matrix for dense graphs or fast edge lookups.
- **BFS layer picture**: source at distance 0, neighbors at distance 1, their newly discovered neighbors at distance 2, and so on.
- **DFS timestamps**: discovery when entering a vertex, finish time only after every descendant is complete.
- **Reverse graph idea**: transpose `G^T` by reversing every directed edge.
- **Traversal complexity**: both BFS and DFS are `O(V+E)` on adjacency lists because every vertex and edge is handled only a constant number of times.

## Takeaways (questions to resolve)
- [ ] Why does BFS compute shortest path length only in *unweighted* graphs?
- [ ] What exact information do discovery and finish times capture that BFS distances do not?
- [ ] Why is adjacency-list representation the right default for this class's graph algorithms?
- [ ] How should DFS edge types be recognized from colors and timestamps?

## Flashcards
#cards/CSCI4041
1. Adjacency-list space::`Theta(V+E)`.
2. Adjacency-matrix space::`Theta(V^2)`.
3. BFS data structure::A FIFO queue.
4. BFS shortest-path meaning::`v.d` is the minimum number of edges from the source to `v` in an unweighted graph.
5. DFS timestamps::`d` = discovery time, `f` = finishing time.
6. Traversal runtime on adjacency lists::`O(V+E)`.
7. White / Gray / Black::Undiscovered / discovered but active / fully processed.