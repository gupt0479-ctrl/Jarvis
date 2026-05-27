---
type: class
input_kind: lecture
status: sprout
created: 2026-04-27
updated: 2026-04-27
area:
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Lecture"
next:
  - "[[Week - 14|Week - 14]]"
---
# Entire Week
## What you must be able to do
- [[Chapter - 22#22.1 The Bellman-Ford Algorithm|Chapter 22.1]] and [[Shortest Paths#Bellman-Ford|Shortest Paths - Bellman-Ford]]: trace Bellman-Ford on a graph with negative edges, explain why $|V|-1$ passes suffice, and detect negative-weight cycles.
- [[Chapter - 22#22.3 Dijkstra's Algorithm|Chapter 22.3]] and [[Shortest Paths#Dijkstra|Shortest Paths - Dijkstra]]: trace Dijkstra with a min-heap, explain why it fails on negative edges, and compare its complexity to Bellman-Ford.
- [[Chapter - 23#23.1 Shortest Paths and Matrix Multiplication|Chapter 23.1]] and [[Shortest Paths#APSP via Matrix Multiplication|Shortest Paths - APSP Matrix Multiplication]]: explain the (min, +) matrix multiplication analogy and repeated squaring optimization.
- [[Chapter - 23#23.2 The Floyd-Warshall Algorithm|Chapter 23.2]] and [[Shortest Paths#Floyd-Warshall|Shortest Paths - Floyd-Warshall]]: trace Floyd-Warshall on a small graph, state the recurrence, and reconstruct paths using the predecessor matrix.
- [[Shortest Paths#Practice Map|Shortest Paths - Practice Map]]: connect the week to relaxation reasoning, negative-cycle detection, and APSP matrix patterns.

## Key ideas (textbook)
- **Ch 22 - Single-Source Shortest Paths**: Given a weighted directed graph $G = (V, E)$ and source $s$, find shortest-path weights $\delta(s, v)$ for all $v \in V$. The core mechanism is relaxation: maintain upper-bound estimates $v.d$ and tighten them by checking whether routing through a neighbor improves the estimate. Bellman-Ford handles negative edges in $O(VE)$ by relaxing all edges $|V|-1$ times. Dijkstra assumes nonnegative weights and uses a greedy min-heap extraction in $O(E \lg V)$ with a binary heap.
- **Ch 23 - All-Pairs Shortest Paths**: Find $\delta(u, v)$ for every pair $(u, v)$. The matrix-multiplication approach treats the weight matrix like a (min, +) semiring and computes successive "powers" — the slow version takes $O(n^4)$, repeated squaring brings it to $O(n^3 \lg n)$. Floyd-Warshall uses a different DP formulation based on intermediate vertices and runs in $\Theta(n^3)$ with simple code and easy path reconstruction via a predecessor matrix $\Pi$.

## Concepts created / updated today
- [[Shortest Paths#Definition|Shortest Paths]] (new concept note)
- [[Chapter - 22#22.1 The Bellman-Ford Algorithm|Chapter - 22 - Bellman-Ford and Dijkstra]]
- [[Chapter - 23#23.2 The Floyd-Warshall Algorithm|Chapter - 23 - APSP and Floyd-Warshall]]

## Lecture
### Chapter 22 and Chapter 23 - Shortest Paths (Single-Source and All-Pairs)
This week builds directly on the graph infrastructure from [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11|Week - 11]] and [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12|Week - 12]]. Where Week 12 asked "how do we connect all vertices cheaply?" (MST), Week 13 asks "what is the cheapest way to get from one vertex to another?" The shift is from undirected spanning structure to directed path optimization.

The lecture arc has two halves. The first half covers single-source shortest paths (SSSP): given one source vertex $s$, find shortest paths to all other vertices. The foundational mechanism is relaxation — checking whether routing through a neighbor improves the current best estimate. Two algorithms implement this differently. Bellman-Ford relaxes every edge $|V|-1$ times, which is brute-force but handles negative weights and detects negative-weight cycles. Dijkstra is greedy: it extracts the nearest unfinished vertex from a min-heap and relaxes its outgoing edges, never revisiting a vertex. Dijkstra is faster ($O(E \lg V)$ vs $O(VE)$) but requires nonnegative edge weights.

The second half covers all-pairs shortest paths (APSP): find $\delta(u, v)$ for every pair. The professor shows three approaches. The slow APSP method uses (min, +) matrix multiplication and iterates $n-1$ times for $O(n^4)$. The faster variant uses repeated squaring to cut iterations to $O(\lg n)$, giving $O(n^3 \lg n)$. Floyd-Warshall takes a completely different DP angle — instead of counting edges, it adds one intermediate vertex at a time — and achieves $\Theta(n^3)$ with the simplest code of all three. The professor also shows Floyd-Warshall with a predecessor matrix for path reconstruction.

The graph codebase notebook (`Ch20(Graphs-CodeBase)-1.ipynb`) extends the adjacency-list graph class from [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12|Week - 12]] with weighted-edge support and a separate matrix-graph class for APSP. The homework (`CodingHW_9(chapter20-23-CLRS).ipynb`) ties together graph construction, SSSP, and APSP.

### Jupyter Notebook Explanations
#### Ch22_Single-Source_Shortest_Path.ipynb
This notebook implements the single-source shortest path algorithms from CLRS Chapter 22. It starts with the two foundational subroutines — initialization and relaxation — then builds Bellman-Ford and Dijkstra on top of them. It also includes path reconstruction via the predecessor chain.

The initialization sets every vertex's distance estimate to infinity and predecessor to `None`, then sets the source distance to zero. This is the starting point for both Bellman-Ford and Dijkstra.

```python
def initialize_single_source(G,s):
    """initialize the vertex attributes of G for single-source s"""
    for v in G.V:
        v.d = float("inf")    # initial distance
        v.prev = None         # initial predecessor node (in tree)
    s.d = 0                   # set source s distance to zero
```

Every vertex starts at $\infty$ distance from $s$. The source itself starts at $0$. The `v.prev` attribute will eventually form the shortest-path tree — each vertex points back to its predecessor on the shortest path from $s$.

Relaxation is the single most important operation in shortest-path algorithms. It checks whether the current best path to $v$ can be improved by going through $u$.

```python
def relax(u,v,w_uv):
    """relaxation procedure - check if path to v should go through u"""
    if v.d > u.d + w_uv:
        v.d = u.d + w_uv    # update distance to v (though u)
        v.prev = u          # update previous node reference for v
```

The test `v.d > u.d + w_uv` asks: "is the current estimate for $v$ worse than going through $u$?" If yes, update both the distance and the predecessor. After enough relaxations, $v.d = \delta(s, v)$ for all reachable $v$. The textbook's path-relaxation property (Lemma 22.15) guarantees this: if edges along a shortest path are relaxed in order, the endpoint gets the correct distance.

Bellman-Ford relaxes every edge $|V|-1$ times. A shortest path in a graph with no negative-weight cycles has at most $|V|-1$ edges, so $|V|-1$ passes guarantee that relaxation propagates along the entire shortest path regardless of edge ordering. The final loop checks for negative-weight cycles: if any edge can still be relaxed after $|V|-1$ passes, a negative cycle exists.

```python
def bellman_ford(G,s):
    """The Bellman-Ford (single-source) shortest path algorithm"""
    initialize_single_source(G,s)
    for i in range(G.n-1):        # do the following n-1 times
        for (u,v,w) in G.edges(): # loop over edges
            relax(u,v,w)          # relax each
    for (u,v,w) in G.edges():     # this checks if it messed up
        if v.d > u.d + w:         # specifically this is negative weight cycle
            return False
    return True
```

- **Outer loop**: $n-1$ iterations where $n = |V|$. Each iteration relaxes all $|E|$ edges.
- **Negative-cycle check**: after $n-1$ passes, if any edge $(u,v)$ still satisfies $v.d > u.d + w(u,v)$, then a negative-weight cycle is reachable from $s$. The algorithm returns `False` in that case.
- **Complexity**: $O(VE)$ — the outer loop runs $|V|-1$ times, each pass touches all $|E|$ edges.

Path reconstruction walks backward from any vertex $v$ to the source $s$ using the `v.prev` chain built during relaxation.

```python
def print_path(G,s,v):
    """prints the path from s -> v (based on v.prev attribute)"""
    if v==s:
        print(s,end=", ")
    elif v.prev == None:
        print("no path from",s,"to",v,"exists")
    else:
        print_path(G,s,v.prev) # walk back in the list
        print(v,end=", ")      # print after (reverse list)
```

This is a recursive walk: go to the predecessor first, then print the current vertex. The recursion bottoms out at the source. If `v.prev` is `None` and $v \neq s$, then $v$ is unreachable from $s$.

Dijkstra's algorithm requires modified initialization and relaxation to work with a min-heap priority queue. The `v.key` attribute is the heap key, initially $\infty$ for all vertices except the source.

```python
def initialize_single_source_dijkstra(G,s):
    """initialize the vertex attributes of G for single-source s"""
    for v in G.V:
        v.d = float("inf")    # initial distance
        v.key = float("inf")
        v.prev = None         # initial predecessor node (in tree)
    s.key = 0                 # set source key to zero
    s.d = 0                   # set source s distance to zero
```

The Dijkstra relaxation also updates the heap. When a shorter path to $v$ is found, the heap key must decrease so $v$ moves up in the priority queue.

```python
def relax_dijkstra(Q,u,v,w_uv):
    """relaxation procedure - check if path to v should go through u"""
    if v.d > u.d + w_uv:
        v.d = u.d + w_uv    # update distance to v (though u)
        v.prev = u          # update previous node reference for v
        if v in Q.A:        # queue operations for Dijkstra Algorithm
            v.key = v.d
            Q.decrease_key(Q.A.index(v),v.d)
```

The `if v in Q.A` check ensures we only update vertices still in the queue. Once a vertex has been extracted, its distance is final (this is the greedy property that requires nonnegative weights).

The main Dijkstra loop extracts the minimum-key vertex, then relaxes all its outgoing edges. Each vertex is extracted exactly once, and each edge is relaxed at most once.

```python
def dijkstra(G,s):
    """Dijkstra's algorithm for single-source shorted path"""
    initialize_single_source_dijkstra(G,s)  # call the initialization
    Q = minheap(G.n)                        # construct heap
    for u in G.V:                           # loop over vertices
        Q.insert(u)                         # insert into min heap
    while Q.size:                           # while heap is non-empty
        u = Q.extract_min()                 # extract 'nearest' vertex
        for v in G.adj(u):                  # loop over adjacencies
            relax_dijkstra(Q,u,v,G.weight(u,v)) # check for better distance to v
```

- **Heap construction**: all vertices inserted with key $\infty$ except source with key $0$.
- **Main loop**: extract the vertex with smallest $d$ value, relax its neighbors. The `decrease_key` call maintains the heap invariant.
- **Complexity**: $O((V + E) \lg V)$ with a binary min-heap. Each `extract_min` is $O(\lg V)$ and happens $|V|$ times. Each `decrease_key` is $O(\lg V)$ and happens at most $|E|$ times total.
- **Why nonnegative weights**: once $u$ is extracted, we rely on the fact that no future path through an unextracted vertex can improve $u.d$. A negative edge could violate this.

#### Ch23_All-Pairs_Shortest_Path.ipynb
This notebook implements the all-pairs shortest path algorithms from CLRS Chapter 23. It uses a matrix representation of the graph (adjacency/weight matrix) rather than adjacency lists. The three approaches shown are: slow APSP ($O(n^4)$), faster APSP with repeated squaring ($O(n^3 \lg n)$), and Floyd-Warshall ($\Theta(n^3)$).

The core subroutine `extend_shortest_paths` is the (min, +) analogue of matrix multiplication. Standard matrix multiplication computes $C[i][j] = \sum_k A[i][k] \cdot B[k][j]$. Here, we replace $(\times, +)$ with $(+, \min)$: instead of multiplying and summing, we add and take the minimum.

```python
def extend_shortest_paths(L_prev,W,L,n):
    """computes a step of the all-pairs shortest path
        L_prev = previous iterate
        W = (modified) Adjacency matrix from matrixgraph object
        L = next iterate (being computed)
        n = number of vertices
    """
    for i in range(n):
        for j in range(n):
            for k in range(n):
                L[i][j] = min( L[i][j] , L_prev[i][k] + W[k][j] )
```

- `L_prev[i][k]` is the best known distance from $i$ to $k$ using paths of the previous length bound.
- `W[k][j]` is the direct edge weight from $k$ to $j$.
- The `min` over all $k$ finds the best intermediate vertex to extend through.
- **Complexity per call**: $O(n^3)$ — three nested loops over $n$ vertices.

The slow APSP calls `extend_shortest_paths` exactly $n-1$ times, computing $L^{(1)}, L^{(2)}, \ldots, L^{(n-1)}$. Each call extends the maximum path length by one edge.

```python
def slow_apsp(W,L0,n):
    """ the 'inefficient' variant from the textbook"""
    L = [[L0[i][j] for j in range(n)] for i in range(n)]
    for r in range(n-1):
        M = [[float("inf") for j in range(n)] for i in range(n)]
        for i in range(n):
            M[i][i] = 0
        extend_shortest_paths(L,W,M,n)
        L = [[M[i][j] for j in range(n)] for i in range(n)]
    return L
```

- `L0` is the initial distance matrix (typically the weight matrix $W$ with $0$ on the diagonal and $\infty$ for non-edges).
- Each iteration creates a fresh matrix `M` initialized to $\infty$ with $0$ on the diagonal, then extends.
- **Complexity**: $O(n^4)$ — $n-1$ calls to an $O(n^3)$ subroutine.

The faster variant exploits the fact that `extend_shortest_paths` is associative (like matrix multiplication). Instead of computing $L^{(1)}, L^{(2)}, \ldots, L^{(n-1)}$ one at a time, we square: $L^{(1)}, L^{(2)}, L^{(4)}, L^{(8)}, \ldots$ This is repeated squaring, the same idea used for fast exponentiation.

```python
def faster_apsp(W,n):
    """ the more 'efficient' variant from the textbook"""
    L = [[W[i][j] for j in range(n)] for i in range(n)]
    M = [[float("inf") for j in range(n)] for i in range(n)]
    r = 1
    while r < n:
        M = [[float("inf") for j in range(n)] for i in range(n)]
        extend_shortest_paths(L,L,M,n)
        r = 2*r
        L = [[M[i][j] for j in range(n)] for i in range(n)]
    return L
```

- The key difference: `extend_shortest_paths(L,L,M,n)` — both inputs are $L$, so we are squaring.
- The `while r < n` loop runs $\lceil \lg(n-1) \rceil$ times.
- **Complexity**: $O(n^3 \lg n)$ — $O(\lg n)$ calls to an $O(n^3)$ subroutine.

Floyd-Warshall takes a fundamentally different DP approach. Instead of bounding the number of edges, it bounds the set of allowed intermediate vertices. $D^{(k)}[i][j]$ is the shortest path from $i$ to $j$ using only vertices $\{0, 1, \ldots, k-1\}$ as intermediates. The recurrence is:
$$D^{(k)}[i][j] = \min\left(D^{(k-1)}[i][j],\; D^{(k-1)}[i][k] + D^{(k-1)}[k][j]\right)$$

Either the shortest path does not use vertex $k$ (first term), or it goes through $k$ (second term).

```python
def floyd_warshall(W,n):
    """ the more 'efficient' variant from the textbook"""
    D = [[W[i][j] for j in range(n)] for i in range(n)]
    for k in range(n):
        Dk = [[D[i][j] for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                Dk[i][j] = min( D[i][j] , D[i][k] + D[k][j] )
        D = [[Dk[i][j] for j in range(n)] for i in range(n)]
    return D
```

- **Outer loop over $k$**: adds vertex $k$ to the allowed intermediate set.
- **Inner loops over $i, j$**: update every pair using the recurrence.
- `Dk` is a fresh copy so we do not overwrite values needed in the same iteration.
- **Complexity**: $\Theta(n^3)$ — three nested loops, each running $n$ times.

The path-reconstruction variant maintains a predecessor matrix $\Pi$ alongside the distance matrix $D$. When the path from $i$ to $j$ improves by going through $k$, we record $\Pi[i][j] = k$.

```python
def floyd_warshall_path(W,n):
    """ the more 'efficient' variant from the textbook"""
    D = [[W[i][j] for j in range(n)] for i in range(n)]
    PI = [[None for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if W[i][j] == float('inf'):
                PI[i][j] = None
            else:
                PI[i][j] = i
        PI[i][i] = i
    for k in range(n):
        Dk = [[D[i][j] for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if D[i][k] + D[k][j] < D[i][j]:
                    Dk[i][j] = D[i][k] + D[k][j]
                    PI[i][j] = k
        D = [[Dk[i][j] for j in range(n)] for i in range(n)]
    return D,PI
```

- **Predecessor initialization**: if there is a direct edge from $i$ to $j$, set $\Pi[i][j] = i$. If no edge, set `None`. Self-loops get $\Pi[i][i] = i$.
- **Update rule**: when the path through $k$ is shorter, record $\Pi[i][j] = k$. To reconstruct the full path from $i$ to $j$, recursively look up $\Pi[i][k]$ and $\Pi[k][j]$.
- **Complexity**: same $\Theta(n^3)$ as the basic version, with constant-factor overhead for maintaining $\Pi$.

#### Ch20(Graphs-CodeBase)-1.ipynb
This notebook extends the graph codebase from [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12|Week - 12]] to support weighted edges for shortest-path algorithms. The adjacency-list `graph` class gains a `weight(u,v)` method that traverses the adjacency list to find the edge weight between two vertices. A separate `matrixgraph` class stores the graph as an $n \times n$ weight matrix $W$ where $W[i][j]$ is the edge weight from $i$ to $j$ (or $\infty$ if no edge exists, and $0$ on the diagonal). The matrix representation is used by the APSP algorithms (`slow_apsp`, `faster_apsp`, `floyd_warshall`) because they operate on $n \times n$ matrices directly. The adjacency-list representation is used by Bellman-Ford and Dijkstra because they iterate over edges or adjacencies.

The notebook also includes the `minheap` class used by Dijkstra. This is the same min-heap from [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 5|Week - 5]] and [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12|Week - 12]] (Prim's algorithm), with `insert`, `extract_min`, and `decrease_key` operations. Dijkstra reuses the same heap infrastructure as Prim — the only difference is what the key represents (shortest-path estimate $v.d$ for Dijkstra vs. lightest connecting edge weight for Prim).

## Examples worth keeping
- **Bellman-Ford with negative edges**: trace the algorithm on a 5-vertex graph with one negative edge. Show how relaxation order does not matter — after $|V|-1$ passes, all distances converge. Then add a negative cycle and show the final check returning `False`.
- **Dijkstra min-heap trace**: start from source $s$, show the heap state after each `extract_min`. Verify that extracted vertices never get re-updated (the greedy invariant).
- **Slow vs. faster APSP**: run both on the same 4-vertex graph. Show that `slow_apsp` takes 3 iterations while `faster_apsp` takes 2 (since $2^2 = 4 \geq n$). Both produce the same distance matrix.
- **Floyd-Warshall with predecessor matrix**: trace the $D^{(k)}$ and $\Pi$ matrices for $k = 0, 1, 2, 3$ on a 4-vertex graph. Reconstruct a specific path using $\Pi$.
- **Dijkstra vs. Bellman-Ford tradeoff**: on the same nonneg-weight graph, Dijkstra finishes faster because it processes each vertex once. Bellman-Ford re-relaxes edges redundantly but handles negative weights.

## Takeaways (questions to resolve)
- [ ] Why exactly $|V|-1$ passes in Bellman-Ford? What if the graph has fewer edges on the longest shortest path?
- [ ] Why does Dijkstra fail with negative edges? Construct a concrete 3-vertex counterexample.
- [ ] What is the relationship between the (min, +) matrix multiplication and the tropical semiring?
- [ ] Why does Floyd-Warshall need a fresh copy `Dk` each iteration instead of updating in place?
- [ ] How does Johnson's algorithm (CLRS 23.3) combine Bellman-Ford and Dijkstra for sparse graphs with negative weights? (Not covered in lecture but in textbook.)

## Flashcards
#cards/CSCI4041
1. What does `initialize_single_source` set for each vertex?::$v.d = \infty$ and $v.\text{prev} = \text{None}$, except $s.d = 0$.
2. Relaxation test for edge $(u, v)$::If $v.d > u.d + w(u,v)$, update $v.d = u.d + w(u,v)$ and $v.\text{prev} = u$.
3. Bellman-Ford number of passes::$|V| - 1$ passes over all edges.
4. Bellman-Ford negative-cycle detection::After $|V|-1$ passes, if any edge $(u,v)$ still has $v.d > u.d + w(u,v)$, a negative cycle exists.
5. Bellman-Ford complexity::$O(VE)$.
6. Dijkstra complexity with binary min-heap::$O((V + E) \lg V)$.
7. Why Dijkstra requires nonnegative weights::Once a vertex is extracted from the heap, its distance is final. A negative edge could later provide a shorter path, violating this invariant.
8. Slow APSP complexity::$O(n^4)$ — $n-1$ calls to an $O(n^3)$ matrix extension.
9. Faster APSP optimization::Repeated squaring reduces iterations from $n-1$ to $O(\lg n)$, giving $O(n^3 \lg n)$.
10. Floyd-Warshall recurrence::$D^{(k)}[i][j] = \min(D^{(k-1)}[i][j],\; D^{(k-1)}[i][k] + D^{(k-1)}[k][j])$.
11. Floyd-Warshall complexity::$\Theta(n^3)$.
12. Floyd-Warshall predecessor update::When $D[i][k] + D[k][j] < D[i][j]$, set $\Pi[i][j] = k$.
13. Key difference between SSSP and APSP representations::SSSP uses adjacency lists (edge iteration). APSP uses weight matrices ($n \times n$ arrays).