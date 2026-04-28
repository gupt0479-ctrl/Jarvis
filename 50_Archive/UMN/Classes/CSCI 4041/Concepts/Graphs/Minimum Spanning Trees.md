---
type: concept
course: CSCI 4041
status: sprout
mastery (1/10): 3
created: 2026-04-16
topics:
  - "[[DSA]]"
  - "[[CSCI 4041 Board]]"
  - "[[50_Archive/UMN/Classes/CSCI 4041/Week - 12|Week - 12]]"
  - "[[Chapter - 21]]"
related:
  - "[[50_Archive/UMN/Classes/CSCI 4041/Concepts/Graphs/Graph Algorithms]]"
---
# [[Minimum Spanning Trees]]
## MOC
- [[50_Archive/UMN/Classes/CSCI 4041/Week - 12#Chapter 21 - Minimum Spanning Trees|Week - 12]]
- [[Chapter - 21#21.1 Growing a Minimum Spanning Tree|Chapter - 21 - Generic MST]]
- [[Chapter - 21#21.2 The Algorithms of Kruskal and Prim|Chapter - 21 - Kruskal and Prim]]
- [[50_Archive/UMN/Classes/CSCI 4041/Concepts/Graphs/Graph Algorithms#Definition|Graph Algorithms]]

## Definition
- **Spanning tree**: an acyclic subset of edges that connects all vertices of a connected graph.
- **Minimum spanning tree (MST)**: a spanning tree of minimum total edge weight.
- **Cut**: a partition of the vertex set into two parts `(S, V-S)`.
- **Light edge**: a minimum-weight edge crossing a cut.
- **Safe edge**: an edge that can be added while keeping the current chosen set a subset of some MST.

## Core Ideas (Textbook)
### Generic MST
- Maintain a set `A` that is always a subset of some MST.
- Add safe edges until `A` becomes a spanning tree.
- Cuts and light edges provide the proof language for safety.

### Kruskal
- Grow a forest of components.
- Always add the globally lightest edge that joins two different components.
- Sorting edges dominates the running time.

### Prim
- Grow one tree from a chosen root.
- Maintain a frontier of cheapest outside connections using a min-priority queue.
- The `key` of a vertex is the cheapest edge currently known that can attach it to the tree.

## Core Ideas (Lecture)
### Kruskal implementation

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

The lecture version makes the component idea extremely explicit by storing a Python set for each current component.

### Prim implementation

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

Prim is easiest to remember as "one growing tree plus a min-heap frontier."

### Min-heap support

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
```

## Proof / Reasoning Toolkit
### Safe-Edge Checklist
1. Identify a cut that respects the current edge set `A`.
2. Find the light edge crossing that cut.
3. Apply the safe-edge theorem.
4. Add the edge without violating the invariant.

### Kruskal Checklist
1. Sort edges by weight.
2. Maintain components.
3. Skip edges within one component.
4. Accept edges that merge two components.

### Prim Checklist
1. Start from a root.
2. Store a cheapest-known connection for every outside vertex.
3. Extract the smallest key.
4. Relax neighboring vertices still outside the tree.

## Complexity + Tradeoffs
| Algorithm | Time | Main Tradeoff |
| --- | --- | --- |
| Kruskal | `O(E lg E)` | Needs sorted edges and component tracking |
| Prim with binary heap | `O(E lg V)` | Good with adjacency lists and heap frontier |
| Prim with Fibonacci heap | `O(E + V lg V)` | Better asymptotically, more complex structure |

## Canonical Examples (Max 5)
### 1. Kruskal edge acceptance
- **Goal:** build an MST without creating cycles.
- **Key steps:** sort edges, accept only those connecting different components.
- **Common mistake:** forgetting that low weight alone is not enough if the edge closes a cycle.

### 2. Prim root start
- **Goal:** grow one tree from a root.
- **Key steps:** set root key to 0, others to infinity, then repeatedly extract minimum.
- **Common mistake:** treating Prim like a global edge-sorting algorithm rather than a frontier algorithm.

### 3. Safe-edge theorem
- **Goal:** justify a greedy step.
- **Key steps:** pick a cut respected by `A`, then take the light edge across it.
- **Common mistake:** choosing a cut crossed by an edge already in `A`.

### 4. `|V|-1` edge fact
- **Goal:** know when the forest has become a spanning tree.
- **Key steps:** once a connected acyclic structure on all vertices has `|V|-1` edges, it is a tree.
- **Common mistake:** adding extra edges after the tree is already complete.

### 5. Prim key updates
- **Goal:** keep the frontier accurate.
- **Key steps:** if edge `(u,v)` is lighter than `v.key`, update `v.prev` and `v.key`.
- **Common mistake:** updating vertices that are no longer in the heap.

## Practice Map
- Union-find MST patterns
- Kruskal by sorted edges
- Prim with a heap
- Weighted-graph greedy proofs
- Compare MST with shortest path goals

## Mini-test
1. What is the difference between a spanning tree and an MST?
2. What makes an edge safe?
3. How do Kruskal and Prim differ operationally?
4. Why does Kruskal need component tracking?
5. What does `v.key` mean in Prim?

## Flashcards
#cards/CSCI4041
1. Spanning tree::A cycle-free set of edges connecting all vertices.
2. MST::A spanning tree with minimum total weight.
3. Light edge::A minimum-weight edge crossing a cut.
4. Kruskal's rule::Take the lightest edge that joins two different components.
5. Prim's rule::Take the lightest edge that adds one new vertex to the current tree.
6. Safe-edge theorem::A light edge crossing a cut that respects `A` is safe for `A`.
7. Prim vertex key::The lightest currently known edge that can connect the vertex to the growing tree.
