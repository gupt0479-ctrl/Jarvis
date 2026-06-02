---
type: concept
course: CSCI 4041
status: sprout
mastery (1/10): 3
created: 2026-04-27
topics:
  - "[[DSA]]"
  - "[[CSCI 4041 Board]]"
  - "[[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 13|Week - 13]]"
  - "[[Chapter - 22|Chapter - 22]]"
  - "[[Chapter - 23|Chapter - 23]]"
related:
  - "[[Graph Algorithms|Graph Algorithms]]"
  - "[[Minimum Spanning Trees|Minimum Spanning Trees]]"
  - "[[Maximum Flow|Maximum Flow]]"
---
# [[Shortest Paths]]
## MOC
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 13#Chapter 22 and Chapter 23 - Shortest Paths (Single-Source and All-Pairs)|Week - 13 - Lecture]]
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 13#Ch22_Single-Source_Shortest_Path.ipynb|Week - 13 - SSSP Notebook]]
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 13#Ch23_All-Pairs_Shortest_Path.ipynb|Week - 13 - APSP Notebook]]
- [[Chapter - 22#22.1 The Bellman-Ford Algorithm|Chapter - 22 - Bellman-Ford]]
- [[Chapter - 22#22.3 Dijkstra's Algorithm|Chapter - 22 - Dijkstra]]
- [[Chapter - 23#23.1 Shortest Paths and Matrix Multiplication|Chapter - 23 - Matrix APSP]]
- [[Chapter - 23#23.2 The Floyd-Warshall Algorithm|Chapter - 23 - Floyd-Warshall]]
- [[Graph Algorithms|Graph Algorithms]] (prerequisite: BFS, DFS, adjacency lists)
- [[Minimum Spanning Trees|Minimum Spanning Trees]] (related: Prim uses same heap structure as Dijkstra)

## Definition
- **Shortest path**: given a weighted directed graph $G = (V, E)$ with weight function $w: E \to \mathbb{R}$, the shortest-path weight from $u$ to $v$ is $\delta(u, v) = \min\{w(p) : u \leadsto v\}$ if a path exists, $\infty$ otherwise.
- **Single-source shortest paths (SSSP)**: find $\delta(s, v)$ for all $v \in V$ from a fixed source $s$.
- **All-pairs shortest paths (APSP)**: find $\delta(u, v)$ for every pair $(u, v) \in V \times V$.
- **Relaxation**: the operation that tightens an upper-bound estimate $v.d$ on $\delta(s, v)$ by checking whether routing through a neighbor improves it.

## Core Ideas (Textbook)
### Relaxation Framework (Ch 22)
Every SSSP algorithm uses the same two primitives. `INITIALIZE-SINGLE-SOURCE` sets $v.d = \infty$ and $v.\pi = \text{NIL}$ for all vertices, then $s.d = 0$. `RELAX(u, v, w)` checks if $v.d > u.d + w(u,v)$ and updates if so. The key properties (Section 22.5):
- **Triangle inequality**: $\delta(s, v) \leq \delta(s, u) + w(u, v)$.
- **Upper-bound**: $v.d \geq \delta(s, v)$ always.
- **Convergence**: if $u.d = \delta(s, u)$ before relaxing $(u, v)$, then $v.d = \delta(s, v)$ afterward.
- **Path relaxation**: relaxing edges in shortest-path order guarantees correct distances.

### Bellman-Ford (Ch 22.1)
Handles negative-weight edges. Performs $|V| - 1$ passes, each relaxing all edges. Detects negative-weight cycles in a final pass. Complexity: $O(VE)$.

### Dijkstra (Ch 22.3)
Greedy algorithm for nonnegative weights. Extracts the nearest vertex from a min-priority queue and relaxes its outgoing edges. Each vertex extracted exactly once. Complexity: $O((V + E) \lg V)$ with binary heap, $O(V \lg V + E)$ with Fibonacci heap.

### APSP via Matrix Multiplication (Ch 23.1)
Treats the weight matrix as a (min, +) semiring. `EXTEND-SHORTEST-PATHS` is the analogue of matrix multiplication. Slow variant: $O(n^4)$. Repeated squaring: $O(n^3 \lg n)$.

### Floyd-Warshall (Ch 23.2)
DP over intermediate vertices. $D^{(k)}[i][j] = \min(D^{(k-1)}[i][j], D^{(k-1)}[i][k] + D^{(k-1)}[k][j])$. Complexity: $\Theta(n^3)$. Path reconstruction via predecessor matrix $\Pi$.

### Johnson's Algorithm (Ch 23.3)
Reweights edges using Bellman-Ford to make all weights nonneg, then runs Dijkstra from each vertex. Best for sparse graphs with negative weights. Complexity: $O(V^2 \lg V + VE)$ with Fibonacci heaps. Not covered in lecture.

## Core Ideas (Lecture)
### SSSP: Initialization and Relaxation
The professor's implementation starts with two foundational subroutines that every SSSP algorithm builds on.

```python
def initialize_single_source(G,s):
    """initialize the vertex attributes of G for single-source s"""
    for v in G.V:
        v.d = float("inf")    # initial distance
        v.prev = None         # initial predecessor node (in tree)
    s.d = 0                   # set source s distance to zero
```

```python
def relax(u,v,w_uv):
    """relaxation procedure - check if path to v should go through u"""
    if v.d > u.d + w_uv:
        v.d = u.d + w_uv    # update distance to v (though u)
        v.prev = u          # update previous node reference for v
```

### SSSP: Bellman-Ford
Brute-force relaxation of all edges $|V|-1$ times. Works with negative weights. Detects negative cycles.

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

### SSSP: Path Reconstruction
Recursive predecessor walk from any vertex back to the source.

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

### SSSP: Dijkstra
Greedy extraction from a min-heap. Requires nonneg weights. Modified init and relax to integrate with the heap.

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

### APSP: Matrix Multiplication Approach
The (min, +) matrix extension step, plus slow ($O(n^4)$) and fast ($O(n^3 \lg n)$) variants.

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

### APSP: Floyd-Warshall
DP over intermediate vertices. The simplest and most efficient APSP code.

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

### APSP: Floyd-Warshall with Path Reconstruction

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

## Proof / Reasoning Toolkit
### Bellman-Ford Correctness Argument
1. After pass $i$, every vertex reachable via a shortest path of $\leq i$ edges has its correct distance.
2. A shortest path has at most $|V| - 1$ edges (no negative cycles means no repeated vertices).
3. Therefore $|V| - 1$ passes suffice.
4. If any edge can still be relaxed after $|V| - 1$ passes, a negative-weight cycle exists.

### Dijkstra Greedy Invariant
1. When vertex $u$ is extracted from the min-heap, $u.d = \delta(s, u)$.
2. Proof by contradiction: suppose $u.d > \delta(s, u)$ at extraction. Then some unextracted vertex $x$ lies on a shorter path $s \leadsto x \to \cdots \to u$. But $x.d \geq u.d$ (since $u$ was extracted first), and all edges are nonneg, so $\delta(s, u) \leq \delta(s, x) + w(\text{path}) \leq x.d + w(\text{path})$. This contradicts $u.d > \delta(s, u)$.
3. This argument fails with negative edges because $w(\text{path})$ could be negative, allowing $\delta(s, u) < x.d$.

### Floyd-Warshall Correctness
1. $D^{(0)}[i][j] = w_{ij}$ — correct for paths with no intermediate vertices.
2. Inductive step: $D^{(k)}[i][j]$ correctly captures the shortest path using intermediates $\{0, \ldots, k-1\}$.
3. Either the shortest path avoids vertex $k$ (use $D^{(k-1)}[i][j]$) or goes through $k$ (use $D^{(k-1)}[i][k] + D^{(k-1)}[k][j]$).
4. After $n$ iterations, all vertices are allowed as intermediates, so $D^{(n)} = \delta$.

## Complexity + Tradeoffs

| Algorithm | Problem | Time | Space | Neg Weights | Neg Cycle Detection |
|---|---|---|---|---|---|
| Bellman-Ford | SSSP | $O(VE)$ | $O(V)$ | Yes | Yes |
| Dijkstra (binary heap) | SSSP | $O((V+E) \lg V)$ | $O(V)$ | No | No |
| Dijkstra (Fibonacci heap) | SSSP | $O(V \lg V + E)$ | $O(V)$ | No | No |
| DAG shortest paths | SSSP (DAG) | $\Theta(V+E)$ | $O(V)$ | Yes | N/A (DAG) |
| Slow APSP | APSP | $O(n^4)$ | $O(n^2)$ | Yes | No |
| Faster APSP | APSP | $O(n^3 \lg n)$ | $O(n^2)$ | Yes | No |
| Floyd-Warshall | APSP | $\Theta(n^3)$ | $O(n^2)$ | Yes | No (but detectable) |
| Johnson's | APSP | $O(V^2 \lg V + VE)$ | $O(V^2)$ | Yes (no neg cycles) | Via Bellman-Ford |

## Canonical Examples (Max 5)
### 1. Bellman-Ford with Negative Edge
- **Goal**: find shortest paths from $s$ in a graph with one negative edge.
- **Key steps**: after each pass, show which distances improve. The negative edge causes a non-obvious shortest path that only emerges after multiple passes.
- **Common mistake**: assuming the shortest path uses the fewest edges. A longer path through a negative edge can be shorter.

### 2. Dijkstra Failure on Negative Edge
- **Goal**: show a 3-vertex graph where Dijkstra gives the wrong answer.
- **Key steps**: $s \to a$ with weight 1, $s \to b$ with weight 3, $a \to b$ with weight $-5$. Dijkstra extracts $a$ first, then $b$ with $d = 3$. But the true shortest path is $s \to a \to b$ with weight $-4$.
- **Common mistake**: thinking Dijkstra "just works" on all graphs.

### 3. Floyd-Warshall Trace on 4 Vertices
- **Goal**: trace $D^{(k)}$ for $k = 0, 1, 2, 3$ on a small graph.
- **Key steps**: at each step, check whether routing through vertex $k$ improves any pair. Show the predecessor matrix $\Pi$ updating alongside.
- **Common mistake**: forgetting to use a fresh copy `Dk` and overwriting values needed in the same iteration.

### 4. Slow vs. Faster APSP Comparison
- **Goal**: show that both produce the same result but faster APSP uses fewer iterations.
- **Key steps**: on a 4-vertex graph, slow APSP takes 3 iterations; faster APSP takes 2 (since $2^2 \geq 4$).
- **Common mistake**: confusing the number of matrix multiplications with the matrix size.

### 5. Dijkstra vs. Prim Structural Comparison
- **Goal**: show that Dijkstra and Prim use the same heap operations but with different key meanings.
- **Key steps**: Dijkstra key = $v.d$ (shortest-path estimate). Prim key = lightest edge connecting $v$ to the tree. Both use `extract_min` and `decrease_key`.
- **Common mistake**: thinking Dijkstra builds a spanning tree. It builds a shortest-path tree, which is not necessarily minimum weight.

## Practice Map
- CodingHW_9(chapter20-23-CLRS).ipynb: graph construction, SSSP, and APSP exercises.
- Paper HW - 9 (Ch - 21).pdf: written problems on graph algorithms (overlaps with MST but connects to shortest paths).
- Trace Bellman-Ford on a 5-vertex graph with negative edges.
- Trace Dijkstra with a min-heap on a 6-vertex graph.
- Trace Floyd-Warshall on a 4-vertex graph and reconstruct a path using $\Pi$.
- [[Heuristic Pathfinding Project|Final Project - Heuristic Pathfinding]]: A* search on weighted grid graphs (inferred connection)

## Mini-test
1. What are the two constraints that define a valid relaxation update?
2. Why does Bellman-Ford need exactly $|V| - 1$ passes?
3. Give a 3-vertex counterexample where Dijkstra fails with a negative edge.
4. What is the recurrence for Floyd-Warshall?
5. How does repeated squaring reduce APSP from $O(n^4)$ to $O(n^3 \lg n)$?
6. What does the predecessor matrix $\Pi$ store in Floyd-Warshall, and how do you reconstruct a path from it?
7. Why does Dijkstra reuse the same min-heap infrastructure as Prim?

## Flashcards
#cards/CSCI4041
1. Relaxation test::If $v.d > u.d + w(u,v)$, update $v.d$ and $v.\text{prev}$.
2. Bellman-Ford passes::$|V| - 1$ passes over all edges.
3. Bellman-Ford negative-cycle check::After $|V|-1$ passes, if any edge still relaxes, negative cycle exists.
4. Bellman-Ford complexity::$O(VE)$.
5. Dijkstra greedy invariant::Once extracted from heap, $u.d = \delta(s, u)$ (requires nonneg weights).
6. Dijkstra complexity (binary heap)::$O((V+E) \lg V)$.
7. Why Dijkstra fails with negative edges::An extracted vertex's distance could be improved by a later negative-weight path.
8. Slow APSP complexity::$O(n^4)$.
9. Faster APSP key idea::Repeated squaring reduces iterations to $O(\lg n)$, giving $O(n^3 \lg n)$.
10. Floyd-Warshall recurrence::$D^{(k)}[i][j] = \min(D^{(k-1)}[i][j], D^{(k-1)}[i][k] + D^{(k-1)}[k][j])$.
11. Floyd-Warshall complexity::$\Theta(n^3)$.
12. Floyd-Warshall predecessor update::Set $\Pi[i][j] = k$ when path through $k$ is shorter.
13. Dijkstra vs. Prim key difference::Dijkstra key = shortest-path estimate $v.d$. Prim key = lightest connecting edge weight.