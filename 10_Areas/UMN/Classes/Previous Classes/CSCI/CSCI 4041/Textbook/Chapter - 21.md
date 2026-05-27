---
type: class
input_kind: book
status: sprout
created: 2026-04-13
updated: 2026-04-28
area:
  - "[[UMN Board]]"
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Textbook"
next: "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12|Week - 12]]"
---
# Chapter - 21
In the design of electronic circuits, a common problem is to interconnect a set of pins using the least amount of wire. To model this, we use a **connected, undirected graph** G=(V,E).

- **Vertices (**V**):** Represent the pins.
- **Edges (**E**):** Represent possible interconnections.
- **Weight Function (**w(u,v)**):** Represents the cost (e.g., wire length) of connecting u and v.

We seek an acyclic subset T⊆E that connects all vertices and minimizes the **total weight**: w(T)=(u,v)∈T∑​w(u,v)

[!NOTE] **Spanning Tree Properties** Since T is acyclic and connects all vertices, it must be a tree. This is called a **spanning tree** because it "spans" the graph G.

- **Edge Count (Appendix B.5):** A spanning tree for a graph with ∣V∣ vertices always contains exactly ∣V∣−1 edges.

--------------------------------------------------------------------------------

21.1 Growing a Minimum Spanning Tree

The algorithms for this problem use a **greedy strategy**, which makes the choice that looks best at the moment to yield a globally optimal solution.

The Generic Method

The procedure `GENERIC-MST` grows the MST one edge at a time. It maintains a set of edges A with the following **loop invariant**:

- **Prior to each iteration,** A **is a subset of some minimum spanning tree****.**

In each step, we identify a **safe edge** (u,v) to add to A such that A∪{(u,v)} remains a subset of an MST.

Recognizing Safe Edges: Cuts and Light Edges

To identify safe edges, the textbook provides several definitions:

- **Cut** (S,V−S)**:** A partition of the vertices V into two sets.
- **Crossing the cut:** An edge (u,v) "crosses" the cut if one endpoint is in S and the other is in V−S.
- **Respecting a set** A**:** A cut "respects" A if no edge in A crosses the cut.
- **Light edge:** An edge is a "light edge" crossing a cut if its weight is the minimum of any edge crossing that cut.

[!NOTE] **Theorem 21.1 (Safe Edge Rule)** Let (S,V−S) be any cut of G that respects A, and let (u,v) be a light edge crossing (S,V−S). Then edge (u,v) is safe for A.

As the algorithm proceeds, the graph GA​=(V,A) is a **forest** (a collection of disjoint trees). Initially, A is empty and the forest contains ∣V∣ trees (each vertex is its own tree). Any safe edge connects two distinct components (trees) of GA​.

--------------------------------------------------------------------------------

21.2 The Algorithms of Kruskal and Prim

These two algorithms are specific implementations of the generic greedy method.

[[MST-KRUSKAL|Kruskal’s Algorithm]]

Kruskal’s algorithm grows a forest. The safe edge added to A is always the lowest-weight edge in the entire graph that connects two distinct components.

**Mechanics:**

1. Initialize A to an empty set.
2. Create ∣V∣ sets (one for each vertex) using a **disjoint-set data structure** (see [[Chapter 19: Data Structures for Disjoint Sets]]).
3. Sort all edges E in non-decreasing order by weight.
4. For each edge (u,v) in sorted order:
    - If u and v belong to different sets (trees), add (u,v) to A and unite the two sets.
    - Otherwise, discard the edge to avoid creating a cycle.

**Analysis:**

- **Time Complexity:** O(ElgE), which is equivalent to O(ElgV) because ∣E∣<∣V∣2 and lg∣E∣=O(lgV).
- Sorting takes O(ElgE) and disjoint-set operations take O(Eα(V)).

[[MST-PRIM|Prim’s Algorithm]]

Prim’s algorithm grows a single tree from an arbitrary root vertex r. The tree A starts with only r and expands until it spans all vertices.

**Mechanics:**

1. All vertices not yet in the tree are stored in a **min-priority queue** Q (see [[Chapter 6: Heapsort]]).
2. Each vertex v has a `v.key` (minimum weight of an edge connecting v to the tree) and `v.π` (parent of v in the tree).
3. Initialize all `v.key` to ∞ and `r.key` to 0.
4. While Q is not empty:
    - Extract the vertex u with the minimum key from Q (this adds u to the tree).
    - For each vertex v adjacent to u:
        - If v∈Q and w(u,v)<v.key, set v.π=u, v.key=w(u,v), and update the priority queue via `DECREASE-KEY`.

**Analysis:**

- **Binary Min-Heap:** Total time is O(ElgV).
- **Fibonacci Heap:** Time improves to O(E+VlgV), which is faster for dense graphs.

--------------------------------------------------------------------------------

Implementation & Indexing Notes

[!IMPORTANT] **Indexing Translation**

- **Textbook (1-origin):** Vertices are indexed 1 to ∣V∣.
- **Code (0-origin):** In Java, Python, or C++, vertices are indexed 0 to ∣V∣−1.
- **Adjustment:** Subtract 1 from vertex identifiers or allocate arrays of size ∣V∣+1 and ignore index 0.

## Chapter 21 - Minimum Spanning Trees
In the design of electronic circuits, a common problem is to interconnect a set of pins using the least amount of wire. To model this, we use a **connected, undirected graph** `G = (V, E)`. The vertices represent pins, the edges represent possible interconnections, and a weight function `w(u,v)` represents the cost of connecting `u` and `v`.

We seek an acyclic subset `T subseteq E` that connects all vertices and minimizes the total weight:
$$
w(T) = \sum_{(u,v)\in T} w(u,v)
$$
Since `T` is acyclic and connects all vertices, it must be a tree. This is called a **spanning tree**, and the problem of finding one with minimum total weight is the **minimum-spanning-tree problem**.

> [!NOTE] **Tree Property:** A spanning tree for a graph with `|V|` vertices always contains exactly `|V|-1` edges.

## 21.1 Growing a Minimum Spanning Tree
The algorithms for this problem use a **greedy strategy**. A greedy algorithm makes the choice that looks best at the moment, which for MSTs is proven to yield a globally optimal solution.

### The Generic Method
The procedure `GENERIC-MST` grows the MST one edge at a time by maintaining a set of edges `A` with the following loop invariant:
- **Prior to each iteration,** `A` **is a subset of some minimum spanning tree.**

In each step, we find a **safe edge** `(u,v)` to add to `A` such that `A union {(u,v)}` is still a subset of an MST.

### Recognizing Safe Edges: Cuts and Light Edges
To identify safe edges, use:
- **Cut `(S, V-S)`**: a partition of the vertices into two sets.
- **Crossing the cut**: an edge has one endpoint in `S` and the other in `V-S`.
- **Respecting a set `A`**: a cut respects `A` if no edge in `A` crosses the cut.
- **Light edge**: an edge of minimum weight crossing a given cut.

> [!NOTE] **Theorem 21.1:** Let `(S, V-S)` be any cut of `G` that respects `A`, and let `(u,v)` be a light edge crossing the cut. Then `(u,v)` is safe for `A`.

As the method proceeds, the graph `G_A = (V, A)` is a forest. Initially, `A` is empty and the forest has `|V|` one-vertex trees. Every safe edge connects two different components.

### Lecture Emphasis
This chapter is where the cut/light-edge framework becomes the common proof language for both [[Minimum Spanning Trees#Definition|Kruskal]] and [[Minimum Spanning Trees#Core Ideas (Lecture)|Prim]].
- Kruskal's view: maintain many components and always add the globally cheapest edge that connects two different components.
- Prim's view: maintain one growing tree and always add the lightest edge from the tree to an outside vertex.
- Both are greedy, but the "safe edge" argument is the same underneath.

## 21.2 The Algorithms of Kruskal and Prim
These two algorithms are specific implementations of the generic method.

### Kruskal's Algorithm
Kruskal's algorithm grows a forest. The safe edge added to `A` is always a lowest-weight edge in the entire graph that connects two distinct components.

**Mechanics:**
1. Initialize `A` to the empty set.
2. Create one disjoint-set for each vertex.
3. Sort all edges in nondecreasing order by weight.
4. For each edge `(u,v)` in sorted order:
   - If `u` and `v` are in different sets, add the edge and union the sets.
   - Otherwise discard it because it would create a cycle.

**Analysis:**
- Sorting edges takes `O(E lg E)`.
- Disjoint-set operations take near-linear time.
- Total running time: `O(E lg E) = O(E lg V)`.

### Lecture Code - Kruskal
The notebook implementation uses a Python dictionary of sets instead of a full disjoint-set forest, which makes the component logic easy to see directly.

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

This version is especially good for exams because it exposes the real invariant: only edges joining different components are allowed into the tree.

### Prim's Algorithm
Prim's algorithm grows a single tree from an arbitrary root vertex `r`. The tree starts with only `r` and expands until it spans all vertices.

**Mechanics:**
1. All vertices not yet in the tree are kept in a **min-priority queue** `Q`.
2. Each vertex `v` stores:
   - `v.key`: the lightest edge currently known that connects `v` to the tree.
   - `v.pi` or `v.prev`: the parent of `v` in the MST.
3. Initialize all `v.key` to infinity and set `r.key = 0`.
4. Repeatedly extract the minimum-key vertex from `Q` and relax its outgoing edges into still-unseen vertices.

**Analysis:**
- With a binary min-heap: `O(E lg V)`.
- With a Fibonacci heap: `O(E + V lg V)`.

### Lecture Code - `minheap` and Prim
The notebook implements Prim with a custom adaptable min-heap.

```python
class minheap:
    """an adaptable, min-heap priority queue class"""

    def __init__(self,n,A=None):
        if A:
            self.A = A
            self.size = n
            self.build_min_heap()
        else:
            self.A = [None for i in range(n)]
            self.size = 0
        self.capacity = n
    
    def left(self,i):
        return 2*i + 1
    
    def right(self,i):
        return 2*i + 2
    
    def parent(self,i):
        return (i-1)//2
    
    def insert(self,x):
        self.A[self.size] = x
        self.size += 1
        self.decrease_key(self.size-1,x.key)
    
    def extract_min(self):
        out = self.A[0]
        self.A[0] = self.A[self.size - 1]
        self.A[self.size - 1] = None
        self.size = self.size - 1
        self.min_heapify(0)
        return out
```

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

The lecture implementation makes Prim feel like "BFS with weights plus a heap." The `key` field stores the best currently known light edge that brings a vertex into the tree.

## Bayer and McCreight Connection
While Chapter 21 itself is about MSTs, the lecture sequence links it back to the graph code base from [[Chapter - 20#20.1 Representations of Graphs|Chapter 20]]. The same adjacency-list graph class is reused, and MST algorithms become applications of weighted graph traversal plus safe-edge reasoning.

## Worked Examples
- **Kruskal example:** sort edges by weight and add them if they connect different components; skip any edge that would form a cycle.
- **Prim example:** start from a root, keep the frontier in a min-heap, and repeatedly attach the cheapest outside vertex.
- **Cut/light-edge proof pattern:** if a cut respects the current forest, any light edge crossing it is safe.
- **Tree size fact:** once `|V|-1` edges have been accepted without cycles, the result is a spanning tree.

## Summary Links
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12#Chapter 21 - Minimum Spanning Trees|Week - 12 lecture reference]]
- [[Minimum Spanning Trees#Definition|Minimum Spanning Trees concept]]
- [[Chapter - 20#20.1 Representations of Graphs|Graph code base from Chapter 20]]

---

## Overview
- Chapter 21 studies minimum spanning trees in connected, undirected, weighted graphs.
- In CSCI 4041, MSTs are the graph-greedy unit: the proof language is cuts, light edges, safe edges, and the generic MST invariant.
- The lecture code implements both Kruskal and Prim on the Week 12 graph code base.

## Core Definitions
- **Spanning tree:** acyclic edge set connecting all vertices.
- **Minimum spanning tree:** spanning tree with minimum total weight.
- **Cut:** partition `(S,V-S)` of vertices.
- **Light edge:** minimum-weight edge crossing a cut.
- **Safe edge:** edge that can be added to the current set while preserving the possibility of completing to an MST.
- **Disjoint sets / components:** structure Kruskal uses to detect whether an edge connects two different trees.

## Main Algorithms
- `GENERIC-MST`: maintain `A` as a subset of some MST and repeatedly add safe edges.
- Kruskal: sort all edges by weight and accept edges connecting different components.
- Prim: grow one tree from a root using a min-priority queue of cheapest frontier connections.
- Lecture min-heap support: same core heap operations later reused by Dijkstra.

## Correctness Ideas
- The generic MST invariant is that `A` is always a subset of some MST.
- Cut property: if a cut respects `A`, a light edge crossing the cut is safe.
- Kruskal applies the cut property to the cut separating one current component from the rest.
- Prim applies the cut property to the cut separating the grown tree from all outside vertices.
- Cycle property can explain why Kruskal skips edges inside the same component.

## Complexity
- Kruskal is typically `O(E lg E)` because of sorting, plus disjoint-set operations.
- Prim with a binary heap and adjacency lists is `O(E lg V)`.
- Prim with a Fibonacci heap is `O(E + V lg V)` in the textbook but not implemented in lecture.
- MST space is `O(V+E)` for graph storage plus component/priority-queue state.

## Lecture Emphasis
- `Lectures/Week - 12/Ch21_MinimumSpanningTree.ipynb` implements Kruskal with explicit Python component sets:

```python
for e in Edges:
    set1,set2 = D[e[0]],D[e[1]]
    if set1 != set2:
        A.append(e)
        S = set1.union(set2)
        for v in S:
            D[v] = S
```

- The same notebook implements Prim with `extract_min`, adjacency scans, and `decrease_key`.
- `Lectures/Week - 12/Ch20(Graphs-CodeBase).ipynb` supplies the graph class used by MST code.
- `Homework/Coding/CodingHW_9(chapter20-23-CLRS).ipynb` asks for a CLRS-style reimplementation of Joy's Kruskal using collection of sets / union-find ideas.
- Weekly/concept links: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12|Week - 12]], [[Minimum Spanning Trees|Minimum Spanning Trees]], [[Graph Algorithms|Graph Algorithms]].

## Examples
- Kruskal accepts the next lightest edge only if it joins two different components.
- Prim starts with root key `0`, all other keys infinity, then updates neighbors with cheaper connecting edges.
- A spanning tree on `|V|` vertices has exactly `|V|-1` edges.

## Connections
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12|Week - 12]]
- [[Minimum Spanning Trees|Minimum Spanning Trees]]
- [[Graph Algorithms|Graph Algorithms]]
- [[Maze Project|Maze Project]] uses spanning-tree ideas for maze generation according to the project note.
- Source homework read: `Homework/Coding/CodingHW_9(chapter20-23-CLRS).ipynb` and `Homework/Paper/Paper HW - 9 (Ch - 21).pdf`.
- TODO: source gap - no vault Homework/Paper Homework note exists for direct wikilinking.

## Common Pitfalls
- Confusing MST with shortest-path tree; MST minimizes total tree weight, not distances from a source.
- Adding a low-weight edge that creates a cycle in Kruskal.
- Updating vertices already removed from Prim's priority queue.
- Stating the cut property without requiring that the cut respects `A`.
- Forgetting the graph must be connected for a spanning tree; otherwise the output is a spanning forest.

## Review Checklist
- [ ] Define cut, light edge, safe edge, spanning tree, and MST.
- [ ] Trace Kruskal with component updates.
- [ ] Trace Prim with vertex keys and predecessor pointers.
- [ ] Prove safety using the cut property.
- [ ] Compare MST goals with shortest-path goals.
