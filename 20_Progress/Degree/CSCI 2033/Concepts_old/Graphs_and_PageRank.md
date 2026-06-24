---
type: concept
status: complete
created: 2025-10-24
updated: 2025-12-31
topic: "Graphs and PageRank"
chapters: "Ch. 7.3 | Ch. 9 (LDS) | Lab 6"
tags:
  - "#Graphs"
  - "#LinearAlgebra"
  - "#ML"
  - "#PageRank"
  - "#Jupyter"
related: [[Week_6]], [[Week_8_and_9]], [[Matrix_Operations_Reference]]
---

# Graphs and the PageRank Algorithm
### A Standalone Reference — Applicable Across Courses

---

## 1. What is a Graph?

A **graph** $G = (V, E)$ consists of:
- $V$ = set of **vertices** (nodes) — $|V| = n$
- $E$ = set of **edges** (connections) — $|E| = m$

**Directed graph**: edges have direction. Edge $(i, j)$ goes from $i$ to $j$ (written $i \to j$).

**Undirected graph**: edges have no direction. Edge $\{i, j\}$ connects $i$ and $j$ symmetrically.

**Simple graph**: no self-loops, no multi-edges.

**Degree** of a node: number of edges connected to it.
- In-degree: edges coming in
- Out-degree: edges going out

---

## 2. Adjacency Matrix

For a graph with $n$ nodes, the **adjacency matrix** $A$ is $n \times n$:

$$A_{ij} = \begin{cases} 1 & \text{if there is an edge from } j \text{ to } i \\ 0 & \text{otherwise} \end{cases}$$

> **Convention in this course**: $A_{ij} = 1$ if page $i$ links to page $j$ (Lab 6 uses row = from, column = to).

**Undirected graph**: $A$ is **symmetric** ($A = A^T$).

**Directed graph**: $A$ is generally asymmetric.

### Example

Graph with nodes $\{0, 1, 2\}$ and edges $0\to1$, $1\to2$, $2\to0$:

$$A = \begin{bmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}$$

### Building from Edge List

```python
n   = 4109              # number of nodes
A   = zeros(n, n)

# MM loaded from file: each row = [from_node, to_node]
for link in MM:
    i = int(link[0])
    j = int(link[1])
    A.data[i][j] = 1    # edge i → j
```

### Adjacency Matrix Properties

| Property | Meaning |
|---|---|
| $(A^k)_{ij}$ | Number of **paths of length $k$** from $j$ to $i$ |
| $\sum_j A_{ij}$ | Out-degree of node $i$ |
| $\sum_i A_{ij}$ | In-degree of node $j$ |
| Symmetric | $\iff$ graph is undirected |
| Sparse | Real-world graphs are sparse (most entries zero) |

**Mutual friends via $A^2$**:
$$(A^2)_{ij} = \sum_k A_{ik}A_{kj} = \text{number of 2-hop paths from } j \text{ to } i$$

For a friendship network: $(A^2)_{ij}$ = number of mutual friends between $i$ and $j$.

```python
A2 = A @ A          # 2-hop paths
A3 = A @ A2         # 3-hop paths
```

---

## 3. Incidence Matrix

For a **directed graph** with $n$ nodes and $m$ edges, the **incidence matrix** $B$ is $n \times m$:

$$B_{ij} = \begin{cases} +1 & \text{if edge } j \text{ points TO node } i \\ -1 & \text{if edge } j \text{ points FROM node } i \\ 0 & \text{otherwise} \end{cases}$$

Each column has exactly **two nonzeros** ($+1$ and $-1$).

### Flow Conservation

Let $x$ = $m$-vector of flows on edges. Then $Bx$ = net flow surplus at each node:

$$Bx = \mathbf{0} \quad \Leftrightarrow \quad \text{flow is conserved at every node}$$

With external sources/sinks $s$: $Bx + s = \mathbf{0}$.

### Potential Differences (Dirichlet Energy)

Let $v$ = $n$-vector of node potentials (voltages, temperatures, etc.). Then $B^Tv$ = potential differences across edges.

**Dirichlet energy** measures roughness of the potential field:
$$D(v) = \|B^T v\|^2 = \sum_{\text{edges }(i,j)} (v_i - v_j)^2$$

Minimizing $D(v)$ forces adjacent nodes to have similar potentials (smoothness). This is the graph Laplacian energy — used in graph signal processing and semi-supervised learning.

---

## 4. Transition Matrix $S$ (Markov / PageRank)

Convert adjacency matrix to a **column-stochastic** matrix where each column sums to $1$:

$$S_{ij} = \frac{A_{ij}}{\sum_{i'} A_{i'j}}$$

Column $j$ = probability distribution over destinations from node $j$.

**Dangling nodes** (no outgoing edges → zero column): set the whole column to $1/n$ (uniform):

```python
S = 1.0 * A
col_sums = [sum(S.data[i][j] for i in range(n)) for j in range(n)]

for j in range(n):
    if col_sums[j] != 0:
        for i in range(n):
            S.data[i][j] /= col_sums[j]
    else:                           # dangling node
        for i in range(n):
            S.data[i][j] = 1.0 / n
```

---

## 5. The Google Matrix $G$

Real surfers don't always follow links — they sometimes jump to a random page. Model this with **damping factor** $\alpha = 0.85$:

$$G = \alpha\,S + \frac{1-\alpha}{n}\,J$$

where $J$ is the $n \times n$ all-ones matrix.

- With probability $\alpha$: follow a link (according to $S$)
- With probability $1-\alpha$: teleport uniformly to any page

$$G_{ij} = \alpha\,S_{ij} + \frac{1-\alpha}{n}$$

$G$ is still **column-stochastic**: columns sum to $1$, all entries positive.

```python
alpha = 0.85
J = Matrix([[1 for _ in range(n)] for _ in range(n)])
G = alpha * S + ((1 - alpha) / n) * J
```

**Why $\alpha = 0.85$?** Chosen by Google empirically. Higher $\alpha$ = more weight on link structure. Lower $\alpha$ = more uniform behavior.

---

## 6. PageRank — Power Iteration

The PageRank vector $v_\star$ is the **dominant eigenvector** of $G$ with eigenvalue $\lambda = 1$:
$$G\,v_\star = v_\star, \qquad v_\star \ge 0, \qquad \sum_i (v_\star)_i = 1$$

**Power iteration** (Chapter 9 LDS applied to probability):

1. Initialize: $v^{(0)} = [1/n, 1/n, \ldots, 1/n]^T$ (uniform)
2. Iterate:
$$v^{(k+1)} = G\,v^{(k)} \qquad \text{then normalize: } \quad v^{(k+1)} \leftarrow \frac{v^{(k+1)}}{\|v^{(k+1)}\|}$$
3. After convergence: $v^{(k)} \approx v_\star$

```python
v = Matrix([[1.0 / n] for i in range(n)])   # uniform start

for i in range(10):                          # at least 10 iterations
    w       = G @ v
    norm_w  = w.norm()
    v       = (1.0 / norm_w) * w
```

**Why does this converge?** $G$ is primitive (all entries positive due to teleportation term). By the **Perron–Frobenius theorem**, a primitive column-stochastic matrix has a unique dominant eigenvalue $\lambda = 1$ and a unique positive eigenvector. Power iteration always converges to it.

---

## 7. Extracting Top-Ranked Pages

```python
scores = [v.data[i][0] for i in range(n)]
sorted_indices = sorted(range(n), key=lambda i: scores[i], reverse=True)

top_scores  = [scores[i] for i in sorted_indices[:10]]
top_indices = sorted_indices[:10]

print("Top 10 Scores:", top_scores)
print("Top 10 Indices:", top_indices)
```

---

## 8. Graph Laplacian (Cross-Course Concept)

The **graph Laplacian** $L = D - A$ (where $D$ is the degree matrix — diagonal with $D_{ii} = $ degree of node $i$) is a fundamental object in graph theory.

$$L_{ij} = \begin{cases} \deg(i) & i = j \\ -1 & (i,j) \in E \\ 0 & \text{otherwise} \end{cases}$$

Properties:
- $L$ is symmetric and positive semi-definite
- $L = B B^T$ (for the incidence matrix $B$)
- $x^T L x = \sum_{(i,j)\in E}(x_i - x_j)^2 = D(x)$ (Dirichlet energy)
- Smallest eigenvalue is always $0$ (eigenvector = $\mathbf{1}$)
- Number of zero eigenvalues = number of connected components

The **graph Laplacian appears in**: spectral clustering, semi-supervised learning, graph neural networks (GNNs), physical simulations, dimensionality reduction (Laplacian Eigenmaps), and graph signal processing.

---

## 9. Full Pipeline Summary

```
Edge list file
    ↓
Adjacency matrix A  (n × n, sparse, {0,1})
    ↓  normalize columns
Transition matrix S  (column-stochastic)
    ↓  add teleportation
Google matrix G  (column-stochastic, all-positive)
    ↓  power iteration
PageRank vector v★  (dominant eigenvector)
    ↓  sort entries
Top-k ranked pages
```

---

## 10. Connections to Other Areas

| Graph concept | ML / CS application |
|---|---|
| Adjacency matrix $A$ | Graph neural networks (GNNs), link prediction |
| $(A^k)_{ij}$ | Graph kernels, path-based similarity |
| Transition matrix $S$ | Markov chains, random walks |
| PageRank power iteration | Node embeddings (DeepWalk, Node2Vec use random walks) |
| Dirichlet energy | Graph regularization, label propagation in SSL |
| Graph Laplacian $L$ | Spectral clustering, Laplacian Eigenmaps, GNNs |
| Column-stochastic matrices | Markov decision processes (MDPs) in RL |

---

## Summary

| Concept | Formula |
|---|---|
| Adjacency matrix | $A_{ij} = 1$ if edge $i \to j$ |
| Incidence matrix entry | $B_{ij} = +1$ (to), $-1$ (from) |
| Paths of length $k$ | $(A^k)_{ij}$ |
| Flow conservation | $Bx + s = \mathbf{0}$ |
| Dirichlet energy | $D(v) = \|B^Tv\|^2$ |
| Transition matrix | $S_{ij} = A_{ij} / \sum_{i'} A_{i'j}$ |
| Google matrix | $G = \alpha S + \frac{1-\alpha}{n}J$ |
| Power iteration | $v^{(k+1)} = Gv^{(k)}/\|Gv^{(k)}\|$ |
| PageRank eigenvector | $Gv_\star = v_\star$ |
| Graph Laplacian | $L = D - A$, $\;x^TLx = D(x)$ |
