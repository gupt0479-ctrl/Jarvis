---
type: concept
course: CSCI 4041
status: sprout
mastery (1/10): 3
created: 2026-04-27
topics:
  - "[[DSA]]"
  - "[[CSCI 4041 Board]]"
  - "[[Week - 14|Week - 14]]"
  - "[[Chapter - 24|Chapter - 24]]"
related:
  - "[[Graph Algorithms|Graph Algorithms]]"
  - "[[Shortest Paths|Shortest Paths]]"
---
# [[Maximum Flow]]
## MOC
- [[Week - 14#Chapter 24 - Maximum Flow|Week - 14 - Lecture]]
- [[Week - 14#Ch20(Graphs-CodeBase)-NETWORK.ipynb|Week - 14 - Network Codebase]]
- [[Week - 14#Ch24_Maximum_Flow.ipynb|Week - 14 - Flow Notebook]]
- [[Chapter - 24#24.1 Flow Networks|Chapter - 24 - Flow Networks]]
- [[Chapter - 24#24.2 The Ford-Fulkerson Method|Chapter - 24 - Ford-Fulkerson]]
- [[Graph Algorithms|Graph Algorithms]] (prerequisite: BFS for augmenting paths)
- [[Shortest Paths|Shortest Paths]] (related: both operate on weighted directed graphs)

## Definition
- **Flow network**: a directed graph $G = (V, E)$ with source $s$, sink $t$, and capacity function $c(u,v) \geq 0$.
- **Flow**: a function $f: V \times V \to \mathbb{R}$ satisfying capacity constraints ($0 \leq f(u,v) \leq c(u,v)$) and flow conservation (flow in = flow out at every vertex except $s$ and $t$).
- **Value of a flow**: $|f| = \sum_v f(s,v) - \sum_v f(v,s)$.
- **Residual network**: $G_f$ with forward edges (residual capacity $c - f$) and backward edges (residual capacity $f$).
- **Augmenting path**: any $s \to t$ path in $G_f$.
- **Max-flow min-cut theorem**: the maximum flow equals the minimum cut capacity.

## Core Ideas (Textbook)
### Flow Networks (Ch 24.1)
A flow must satisfy two constraints at every edge: capacity ($0 \leq f(u,v) \leq c(u,v)$) and conservation ($\sum_v f(v,u) = \sum_v f(u,v)$ for $u \neq s, t$). The residual network $G_f$ captures what flow changes are still possible. Forward edges have residual capacity $c(u,v) - f(u,v)$; backward edges have residual capacity $f(v,u)$.

### Ford-Fulkerson Method (Ch 24.2)
Repeatedly find an augmenting path in $G_f$, compute the bottleneck (minimum residual capacity along the path), push that much flow, and rebuild $G_f$. Terminates when no augmenting path exists. With integer capacities, terminates in at most $|f^*|$ iterations.

### Edmonds-Karp (Ch 24.2)
Using BFS to find the shortest augmenting path bounds the number of augmentations to $O(VE)$, giving $O(VE^2)$ total. BFS ensures that the shortest-path distance from $s$ to any vertex in $G_f$ never decreases across iterations.

### Max-Flow Min-Cut Theorem (Theorem 24.11)
Three equivalent statements: (1) $f$ is maximum, (2) $G_f$ has no augmenting path, (3) $|f| = c(S,T)$ for some cut $(S,T)$. The min-cut $(S,T)$ is found by taking $S$ = vertices reachable from $s$ in the final $G_f$.

### Bipartite Matching (Ch 24.3)
Maximum matching in a bipartite graph reduces to max flow: add supersource and supersink with unit-capacity edges. Not covered in lecture.

## Core Ideas (Lecture)
### Network Class
The professor extends the adjacency-list `graph` class with capacity and flow on each edge.

```python
class network(graph):
    """a sub-class of the adjacency list graph for network flow"""
    class edge:
        def __init__(self,vertex,capacity=1):
            self.vertex = vertex
            self.next = None
            self.flow = 0
            self.capacity = capacity
    def add_edge(self,i,j,capacity=1,flow=0):
        node = self.A[i]
        while node.next:
            node = node.next
            if node.vertex == j:
                return
        new_node = self.edge(vertex=j,capacity=capacity)
        new_node.flow = flow
        node.next = new_node
    def edges(self):
        for u in self.V:
            node = self.A[u.index]
            while node.next:
                node = node.next
                v = self.V[node.vertex]
                c,f = node.capacity,node.flow
                yield (u,v,c,f)
    def flow(self,u,v):
        node = self.A[u.index]
        while node.next:
            node = node.next
            w = self.V[node.vertex]
            if w.name==v.name:
                return node.capacity,node.flow
    def get_edge(self,u,v):
        node = self.A[u.index]
        while node.next:
            node = node.next
            w = self.V[node.vertex]
            if w.name==v.name:
                return node
```

### Residual Network Construction

```python
def residual_network(G):
    """constructs a residual network Gf from a given network flow G"""
    Gf = network(G.n)
    for i in range(G.n):
        Gf.V[i].name = G.V[i].name
        Gf.V[i].x , Gf.V[i].y = G.V[i].x , G.V[i].y
    for (u,v,c,f) in G.edges():
        if c-f > 0:
            Gf.add_edge(u.index,v.index,c,c-f)
        if f > 0:
            Gf.add_edge(v.index,u.index,c,f)
    return Gf
```

### Ford-Fulkerson / Edmonds-Karp Loop
The augmenting-path loop is the actual algorithm. BFS finds the shortest path in the residual network (Edmonds-Karp variant), the bottleneck is the minimum residual capacity along that path, and flow is pushed along the path. The residual network is then rebuilt and the process repeats until no augmenting path exists.

```python
def ford_fulkerson(G, s, t):
    """Ford-Fulkerson method using BFS (Edmonds-Karp) for augmenting paths"""
    Gf = residual_network(G)
    while True:
        path = bfs_path(Gf, s, t)
        if path is None:
            break
        bottleneck = min(Gf.get_edge(path[i], path[i+1]).flow 
                        for i in range(len(path)-1))
        for i in range(len(path)-1):
            u, v = path[i], path[i+1]
            edge = G.get_edge(u, v)
            if edge:
                edge.flow += bottleneck
            else:
                rev_edge = G.get_edge(v, u)
                rev_edge.flow -= bottleneck
        Gf = residual_network(G)
    return G
```

Each iteration: BFS for path → compute bottleneck → augment flow → rebuild residual. Terminates when BFS finds no $s \to t$ path, which by the max-flow min-cut theorem means the flow is maximum.

## Proof / Reasoning Toolkit
### Max-Flow Min-Cut Proof Sketch
1. For any flow $f$ and any cut $(S,T)$: $|f| \leq c(S,T)$.
2. When Ford-Fulkerson terminates, let $S$ = vertices reachable from $s$ in $G_f$, $T = V \setminus S$.
3. Since $t \notin S$ (no augmenting path), $(S,T)$ is a valid cut.
4. Every edge from $S$ to $T$ is saturated ($f(u,v) = c(u,v)$) and every edge from $T$ to $S$ has zero flow.
5. Therefore $|f| = c(S,T)$, so $f$ is maximum and $(S,T)$ is minimum.

### Ford-Fulkerson Termination (Integer Capacities)
1. Each augmentation increases $|f|$ by at least 1 (bottleneck $\geq 1$ with integer capacities).
2. $|f| \leq c(S,T)$ for any cut, so $|f|$ is bounded.
3. Therefore the algorithm terminates in at most $|f^*|$ iterations.

## Complexity + Tradeoffs

| Algorithm | Time | Path Selection | Notes |
|---|---|---|---|
| Ford-Fulkerson (generic) | $O(E \cdot \|f^*\|)$ | arbitrary | May not terminate with irrational capacities |
| Edmonds-Karp | $O(VE^2)$ | BFS (shortest) | Always terminates, polynomial |

## Canonical Examples (Max 5)
### 1. CLRS Textbook Flow Example
- **Goal**: trace Ford-Fulkerson on the 6-vertex network from CLRS Figure 24.6.
- **Key steps**: at each iteration, build $G_f$, find BFS augmenting path, compute bottleneck, push flow.
- **Common mistake**: forgetting backward edges in the residual network.

### 2. Residual Network with Backward Edges
- **Goal**: show how backward edges allow "undoing" flow.
- **Key steps**: after pushing flow on $s \to a \to b \to t$, the residual network has backward edges $b \to a$ and $a \to s$. A later augmenting path might use $b \to a$ to reroute flow.
- **Common mistake**: thinking flow can only increase on each edge. Backward edges allow redistribution.

### 3. Min-Cut Identification
- **Goal**: after Ford-Fulkerson terminates, find the min-cut.
- **Key steps**: BFS from $s$ in the final $G_f$. Reachable vertices form $S$. Unreachable vertices form $T$. Verify $|f| = c(S,T)$.
- **Common mistake**: including backward-edge reachability when computing cut capacity (cut capacity only counts forward edges from $S$ to $T$).

## Practice Map
- Final Project/Network Flow/Distribution-Network-Template.ipynb: applies network flow to distribution optimization.
- Final Project/Network Flow/Ch20(Graphs-CodeBase)-NETWORK.ipynb: network flow codebase for the project.
- [[Network Flow Project|Final Project - Network Flow]]: distribution network flow implementation
- Trace Ford-Fulkerson on a small network and verify max-flow min-cut.
- Construct a residual network by hand from a given flow.

## Mini-test
1. What two constraints must a valid flow satisfy?
2. How do you compute the residual capacity of a forward edge? A backward edge?
3. What is an augmenting path?
4. When does Ford-Fulkerson terminate?
5. State the max-flow min-cut theorem.
6. Why does Edmonds-Karp use BFS instead of DFS?
7. How does the `network` class differ from the base `graph` class?

## Flashcards
#cards/CSCI4041
1. Flow capacity constraint::$0 \leq f(u,v) \leq c(u,v)$.
2. Flow conservation::Flow in = flow out at every vertex except $s$ and $t$.
3. Residual capacity (forward)::$c_f(u,v) = c(u,v) - f(u,v)$.
4. Residual capacity (backward)::$c_f(v,u) = f(u,v)$.
5. Augmenting path::Any $s \to t$ path in the residual network $G_f$.
6. Bottleneck of augmenting path::Minimum residual capacity along the path.
7. Ford-Fulkerson termination::No augmenting path exists in $G_f$.
8. Max-flow min-cut theorem::Maximum flow value = minimum cut capacity.
9. Edmonds-Karp complexity::$O(VE^2)$.
10. Why backward edges matter::They allow rerouting previously assigned flow to find a better overall solution.