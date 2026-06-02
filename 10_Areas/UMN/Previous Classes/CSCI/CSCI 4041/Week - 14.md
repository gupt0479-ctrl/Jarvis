---
type: class
input_kind: lecture
status: sprout
created: 2026-04-27
updated: 2026-04-27
area:
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Concepts/Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Lecture"
next: []
---
# Entire Week
## What you must be able to do
- [[Chapter - 24#24.1 Flow Networks|Chapter 24.1]] and [[Maximum Flow#Definition|Maximum Flow - Definition]]: define flow networks, capacity constraints, flow conservation, and the value of a flow.
- [[Chapter - 24#24.2 Ford-Fulkerson|Chapter 24.2]] and [[Maximum Flow#Ford-Fulkerson|Maximum Flow - Ford-Fulkerson]]: trace the Ford-Fulkerson method on a small network, construct residual graphs, identify augmenting paths, and explain why the algorithm terminates with integer capacities.
- [[Maximum Flow#Residual Networks|Maximum Flow - Residual Networks]]: construct a residual network from a given flow, explain forward and backward edges, and compute residual capacities.
- [[Maximum Flow#Practice Map|Maximum Flow - Practice Map]]: connect the week to augmenting-path reasoning, residual graph construction, and the max-flow min-cut theorem.

## Key ideas (textbook)
- **Ch 24 - Maximum Flow**: A flow network is a directed graph where each edge has a nonneg capacity and flow must satisfy capacity constraints and conservation (flow in = flow out at every vertex except source and sink). The Ford-Fulkerson method repeatedly finds augmenting paths in the residual network and pushes flow along them until no augmenting path exists. The max-flow min-cut theorem proves that the maximum flow equals the minimum cut capacity. Using BFS to find augmenting paths (Edmonds-Karp) guarantees $O(VE^2)$ time.

## Concepts created / updated today
- [[Maximum Flow#Definition|Maximum Flow]] (new concept note)
- [[Chapter - 24#24.1 Flow Networks|Chapter - 24 - Flow Networks and Ford-Fulkerson]]

## Lecture
### Chapter 24 - Maximum Flow
This week shifts from shortest paths to a fundamentally different graph optimization problem: how much "stuff" can we push through a network from a source to a sink? The flow network model adds capacity constraints to directed edges and requires flow conservation at every internal vertex. The professor builds the entire infrastructure from scratch: a `network` class that extends the adjacency-list `graph` class with capacity and flow attributes on each edge, a function to construct residual networks, and a BFS-based augmenting-path search that implements the Edmonds-Karp variant of Ford-Fulkerson.

The lecture arc follows the textbook structure closely. First, the flow network model is defined: a directed graph $G = (V, E)$ with source $s$, sink $t$, and capacity function $c(u,v) \geq 0$. A flow $f$ assigns a value $f(u,v)$ to each edge satisfying two constraints: capacity ($0 \leq f(u,v) \leq c(u,v)$) and conservation ($\sum_{v} f(v,u) = \sum_{v} f(u,v)$ for all $u \neq s, t$). The value of the flow is $|f| = \sum_{v} f(s,v) - \sum_{v} f(v,s)$.

The residual network $G_f$ captures remaining capacity. For each edge $(u,v)$ in $G$: if $c(u,v) - f(u,v) > 0$, add a forward edge with residual capacity $c(u,v) - f(u,v)$; if $f(u,v) > 0$, add a backward edge $(v,u)$ with residual capacity $f(u,v)$. An augmenting path is any $s \to t$ path in $G_f$. The bottleneck of the path is the minimum residual capacity along it. Ford-Fulkerson pushes flow equal to the bottleneck along the augmenting path, updates the flow, rebuilds the residual network, and repeats until no augmenting path exists.

The professor's notebook demonstrates this step by step on the CLRS textbook example, showing the residual network and augmenting path at each iteration. The `network` class, `residual_network` function, and BFS path-finding are the key code artifacts. The final project (`Final Project/Network Flow/`) extends this to distribution network problems.

### Jupyter Notebook Explanations
#### Ch24_Maximum_Flow.ipynb
This notebook walks through the Ford-Fulkerson method using the CLRS textbook example. It demonstrates the iterative process: construct the residual network, find an augmenting path via BFS, compute the bottleneck capacity, push flow along the path, and repeat. The notebook uses the `network` class and `residual_network` function defined in the codebase notebook.

The Ford-Fulkerson method (Edmonds-Karp variant) uses BFS to find the shortest augmenting path in the residual network at each step. BFS guarantees that the number of augmenting-path iterations is $O(VE)$, giving an overall complexity of $O(VE^2)$. The notebook shows each iteration's residual graph and the chosen augmenting path, making the algorithm's progress visible.

#### Ch20(Graphs-CodeBase)-NETWORK.ipynb
This notebook defines the `network` class that extends the base `graph` class from [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11|Week - 11]]. The key extension is that each edge now stores both a `capacity` and a `flow` value, rather than just a weight.

The `network` class uses the same adjacency-list structure as the base graph, but its `edge` inner class carries `capacity` and `flow` attributes instead of just a weight.

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

- **`edge` inner class**: each edge stores `vertex` (destination index), `next` (linked-list pointer), `flow` (current flow), and `capacity`.
- **`add_edge`**: traverses the adjacency list for vertex $i$. If edge $(i, j)$ already exists, it returns without adding a duplicate. Otherwise, creates a new edge node with the given capacity and flow.
- **`edges` generator**: yields all edges as tuples $(u, v, c, f)$ where $c$ is capacity and $f$ is current flow. This is used to iterate over the entire network.
- **`flow(u,v)`**: returns the `(capacity, flow)` tuple for a specific edge by traversing $u$'s adjacency list until finding $v$.
- **`get_edge(u,v)`**: returns the actual edge node object (not just values), which allows direct modification of flow during the Ford-Fulkerson update step.

The `residual_network` function constructs $G_f$ from a given network $G$. For each edge $(u,v)$ with capacity $c$ and flow $f$: if $c - f > 0$, add a forward edge $(u,v)$ with residual capacity $c - f$; if $f > 0$, add a backward edge $(v,u)$ with residual capacity $f$.

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

- **Vertex copying**: the residual network has the same vertices as $G$, with names and positions preserved for visualization.
- **Forward edges**: if the edge is not fully saturated ($c - f > 0$), there is room to push more flow forward. The residual capacity is $c - f$. The `flow` field of the residual edge stores this residual capacity.
- **Backward edges**: if the edge carries positive flow ($f > 0$), we can "undo" some of that flow by pushing flow backward. The residual capacity for the backward edge is $f$.
- This function is called at each iteration of Ford-Fulkerson to rebuild the residual graph from the current flow state.

#### Ch20(Graphs-CodeBase)-2.ipynb
This notebook extends the graph codebase with additional utility functions used by the maximum flow implementation. It includes the BFS-based path-finding used by the Edmonds-Karp variant of Ford-Fulkerson. The BFS finds the shortest (fewest-edge) augmenting path from source $s$ to sink $t$ in the residual network. The path is reconstructed using the `v.prev` predecessor chain (the same mechanism used in [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11#Ch20_Graphs_and_BFS.ipynb|Week - 11 BFS]]). The bottleneck capacity is the minimum residual capacity along the path. After finding the path and bottleneck, the algorithm updates the flow on each edge: increase flow on forward edges, decrease flow on backward edges.

## Examples worth keeping
- **CLRS textbook flow example**: the professor traces Ford-Fulkerson on the standard 6-vertex network from CLRS Figure 24.6. Each iteration shows the residual network, the BFS-chosen augmenting path, the bottleneck capacity, and the updated flow.
- **Residual network construction**: given a network with edges carrying partial flow, construct $G_f$ by hand. Verify that forward edges have residual capacity $c - f$ and backward edges have residual capacity $f$.
- **Augmenting path bottleneck**: on a residual network, find the $s \to t$ path with BFS and identify the minimum residual capacity along it. That minimum is the amount of flow pushed in this iteration.
- **Max-flow min-cut verification**: after Ford-Fulkerson terminates, identify the min-cut $(S, T)$ where $S$ is the set of vertices reachable from $s$ in the final residual network. Verify that the flow value equals the total capacity of edges crossing the cut.

## Takeaways (questions to resolve)
- [ ] Why does BFS (Edmonds-Karp) guarantee $O(VE)$ augmenting-path iterations while arbitrary DFS does not?
- [ ] What happens to Ford-Fulkerson with irrational capacities? (It may not terminate.)
- [ ] How does the max-flow min-cut theorem connect to LP duality?
- [ ] How does the final project's distribution network problem map onto the flow network model?

## Flashcards
#cards/CSCI4041
1. Flow network capacity constraint::$0 \leq f(u,v) \leq c(u,v)$ for every edge.
2. Flow conservation::For every vertex $u \neq s, t$: flow in equals flow out.
3. Value of a flow::$|f| = \sum_{v} f(s,v) - \sum_{v} f(v,s)$ (net flow out of source).
4. Residual capacity (forward edge)::$c_f(u,v) = c(u,v) - f(u,v)$ when $c - f > 0$.
5. Residual capacity (backward edge)::$c_f(v,u) = f(u,v)$ when $f > 0$.
6. Augmenting path::Any $s \to t$ path in the residual network $G_f$.
7. Ford-Fulkerson termination::When no augmenting path exists in $G_f$, the flow is maximum.
8. Max-flow min-cut theorem::The maximum flow value equals the minimum cut capacity.
9. Edmonds-Karp complexity::$O(VE^2)$ — BFS finds shortest augmenting paths, bounding iterations to $O(VE)$.
10. Why `network` extends `graph`::Same adjacency-list structure, but each edge stores `capacity` and `flow` instead of just weight.