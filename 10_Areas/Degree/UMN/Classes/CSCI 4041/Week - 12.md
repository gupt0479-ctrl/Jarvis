---
type: class
input_kind: lecture
status: seed
created: 2026-04-13
updated: 2026-04-16
area:
  - "[[UMN Board]]"
tags:
next: []
---
# Entire Week
## What you must be able to do
- [[Chapter - 20#20.4 Topological Sort|Chapter 20.4]], [[Chapter - 20#20.5 Strongly Connected Components (SCC)|Chapter 20.5]], and [[Chapter - 21#21.1 Growing a Minimum Spanning Tree|Chapter 21.1]]: explain topological sort, SCC, safe edges, cuts, and light edges.
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Graphs/Graph Algorithms#Core Ideas (Lecture)|Graph Algorithms - advanced lecture notes]] and [[Minimum Spanning Trees#Core Ideas (Lecture)|Minimum Spanning Trees - lecture notes]]: connect DFS finishing times to topological sort and SCC, and connect cut/light-edge reasoning to Kruskal and Prim.
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Graphs/Graph Algorithms#Canonical Examples (Max 5)|Graph Algorithms - Canonical Examples]] and [[Minimum Spanning Trees#Canonical Examples (Max 5)|Minimum Spanning Trees - Canonical Examples]]: trace DAG ordering, reverse-graph SCC discovery, Kruskal component merging, and Prim heap updates.
- [[Minimum Spanning Trees#Practice Map|Minimum Spanning Trees - Practice Map]]: connect the week to course-schedule topological ordering, SCC intuition, union-find MST patterns, and heap-based graph growth.

## Key ideas (textbook)
- **20.4 Topological Sort**: A topological order exists only for a DAG. DFS finishing times provide the ordering because every directed edge in a DAG points from a larger finishing time to a smaller one.
- **20.5 SCC**: Strongly connected components are maximal sets of mutually reachable vertices. The two-pass DFS algorithm works because finishing times from the first DFS identify the right order to explore the transpose graph.
- **21.1 Growing an MST**: The generic MST method grows a forest while preserving the invariant that the chosen edge set is a subset of some MST. Cuts and light edges provide the language for proving an edge is safe.
- **21.2 Kruskal and Prim**: Kruskal grows many components by taking globally light safe edges, while Prim grows one tree by repeatedly choosing the cheapest outside connection. Both are greedy algorithms justified by the same safe-edge theorem.

## Concepts created / updated today
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Graphs/Graph Algorithms#Topological Sort + SCC|Graph Algorithms - Topological Sort + SCC]]
- [[Minimum Spanning Trees#Definition|Minimum Spanning Trees]]
- [[Chapter - 21#21.2 The Algorithms of Kruskal and Prim|Chapter - 21 - Kruskal and Prim]]

## Lecture
### Chapter 20 - Topological Sort and Strongly Connected Components
This week continues directly from [[10_Areas/Degree/UMN/Classes/CSCI 4041/Week - 11#Chapter 20 - Graph Representations, BFS, and DFS|Week - 11]], but now DFS is no longer just a traversal. It becomes a tool for extracting structure from directed graphs. The first major application is topological sort. The lecture viewpoint is simple: if a graph is a DAG, then DFS finishing times already contain an ordering that respects direction. A vertex cannot finish before all vertices reachable from it finish, so reversing finishing order produces a valid topological order. The notebook implementation makes that concrete by running DFS, appending finished vertices to a list, and reversing the list at the end. It also prints a warning when it sees a Gray neighbor, because that means a back edge and therefore a directed cycle.

Strongly connected components are the next layer of structure. The lecture definition is "every vertex in the component can reach every other vertex in the component." The two-pass algorithm is what matters operationally. First run DFS on `G` to compute finishing times. Then build the reverse graph `G^T` and run DFS again, but this time in decreasing order of the original finishing times. Each DFS tree in that second pass is one SCC. The reason this works is that the first pass orders the component graph so the second pass enters each SCC from the right place. The key exam idea is that SCC is not just "another DFS." It is a carefully ordered DFS on the transpose graph.

### Chapter 21 - Minimum Spanning Trees
MSTs shift the course from directed-graph reachability to weighted undirected structure. The generic MST framework says we maintain a set `A` that is always a subset of some MST and repeatedly add safe edges. The proof vocabulary here is essential: cuts, edges crossing cuts, and light edges. Kruskal and Prim look different operationally, but they are both implementations of that same safe-edge idea. Kruskal grows a forest by taking the lightest edge that connects two different components. Prim grows a single tree from a root by taking the lightest edge that attaches a new vertex to the tree. The lecture notebook is especially helpful because it does not hide the data structures: Kruskal uses explicit component sets, and Prim uses a custom min-heap where each vertex stores a current best key value and predecessor.

### Jupyter Explanations
#### Ch20_Topological_Sort_Connected_Components.ipynb
The topological sort code is just DFS with one extra list and one extra cycle warning.

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

The major lecture takeaway is that SCC needs both the transpose graph and the correct ordering from the first DFS. Without both pieces, the second DFS trees would not line up with components correctly.

#### Ch21_MinimumSpanningTree.ipynb
The Kruskal notebook code makes the component structure visible instead of hiding it behind abstract disjoint-set operations.

```python
def kruskal(G):
    """constructs and returns a minimum (weight) spanning tree from weighted graph G"""
    A,D,Edges = [],{},[]
    for v in G.V:
        D[v] = set([v])
    
    for u,v,w in G.edges():
        Edges.append((u,v,w))
    Edges.sort(key=lambda x:x[2])
    
    for e in Edges:
        set1,set2 = D[e[0]],D[e[1]]
        if set1 != set2:
            A.append(e)
            S = set1.union(set2)
            for v in S:
                D[v] = S
    return A
```

The Prim code shows the other MST viewpoint: one growing tree and a min-heap frontier.

```python
def prim(G,r):
    """constructs and returns a minimum weight spanning tree for the weighted graph G"""
    for u in G.V:
        u.key = float("inf")
        u.prev = None
    r.key = 0
    Q = minheap(G.n)
    for u in G.V:
        Q.insert(u)
    while Q.size:
        u = Q.extract_min()
        for v in G.adj(u):
            w = G.weight(u,v)
            if v in Q.A and w < v.key:
                v.prev = u
                v.key = w
                Q.decrease_key(Q.A.index(v),v.key)
```

Kruskal answers "what is the lightest edge connecting two different components?" Prim answers "what is the lightest edge that attaches a new vertex to my current tree?" The proof language underneath both is still cut/light-edge safety.

## Examples worth keeping
- **Topological sort by finish time**: reverse the DFS finishing order for a DAG.
- **Cycle detection in DFS**: encountering a Gray neighbor reveals a back edge, so no valid topological ordering exists.
- **Reverse-graph SCC discovery**: run DFS on `G`, build `G^T`, then DFS on `G^T` in decreasing finish-time order.
- **Kruskal component merge**: sort edges, keep only those that join different components.
- **Prim frontier update**: each vertex outside the tree stores the lightest edge currently known that can connect it to the tree.

## Takeaways (questions to resolve)
- [ ] Why do finish times from the first DFS determine the correct second-pass order for SCC?
- [ ] Why does a Gray neighbor in DFS imply a cycle for topological sort?
- [ ] What exactly makes an edge "safe" in the MST framework?
- [ ] How are Kruskal and Prim operationally different even though they use the same safe-edge theorem?

## Flashcards
#cards/CSCI4041
1. Topological sort requirement::The graph must be a DAG.
2. Topological-sort rule from DFS::Return vertices in decreasing order of finishing time.
3. Strongly connected component::A maximal set of vertices where every pair is mutually reachable.
4. SCC algorithm structure::DFS on `G`, build `G^T`, DFS on `G^T` in decreasing original finish-time order.
5. Safe MST edge::An edge that can be added while keeping the chosen set a subset of some MST.
6. Kruskal's choice::Take the globally lightest edge that connects two different components.
7. Prim's choice::Take the lightest edge that adds one new vertex to the current tree.
