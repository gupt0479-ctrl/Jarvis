---
type: concept
course:
status: sprout
mastery (1/10): 0
created:
topics: []
related:
  - "[[40_Resources/CS/Links|Links]]"
---
# 
## MOC
- [[W__ L__ - ...]]
- [[HW__ - ...]]
## Definition
- 
## Resources
- 
### How to use them
1. 
2. 
## 1. Motivation — Random Surfer Model

Think of a person randomly clicking links on the web. At any time they're on some page. From that page they either:
- Follow one of the outgoing links (with probability $\alpha$), or
- "Teleport" to a completely random page (with probability $1-\alpha$).

The **state** of this system at time $t$ is a probability vector $x_t \in \mathbb{R}^n$, where $(x_t)_i$ is the probability of being on page $i$ at step $t$. Each step is a **linear dynamical system**:
$$x_{t+1} = G\, x_t$$

The steady-state distribution $x_\star$ satisfying $G x_\star = x_\star$ is the **PageRank vector** — its entries are the "importance scores."

---

## 2. Step 1 — Adjacency Matrix $A$

The graph is stored in `web-Stanford-small.txt` in coordinate format: each line `i j` means page $i$ has a hyperlink to page $j$.

Build the $n \times n$ adjacency matrix:
$$A_{ij} = \begin{cases} 1 & \text{if website } i \text{ links to website } j \\ 0 & \text{otherwise} \end{cases}$$

```python
n = 4109
A = zeros(n, n)

for link in MM:          # MM loaded from file, each row = [from, to]
    i = int(link[0])
    j = int(link[1])
    A.data[i][j] = 1     # page i links to page j
```

---

## 3. Step 2 — Transition Matrix $S$

Convert the adjacency matrix into a **column-stochastic** matrix: divide each column by its sum so that each column represents a valid probability distribution over destination pages.

$$S_{ij} = \frac{A_{ij}}{\sum_{i'} A_{i'j}}$$

- Column $j$ sums to $1$: "if I'm on page $j$, what's the probability I go to page $i$ by following a link?"
- **Dangling nodes** (pages with no outgoing links) would give a zero column — handle by setting that whole column to $1/n$ (uniform distribution), so the surfer teleports uniformly.

```python
S = 1.0 * A

col_sums = [sum(S.data[i][j] for i in range(n)) for j in range(n)]

for j in range(n):
    if col_sums[j] != 0:
        for i in range(n):
            S.data[i][j] = S.data[i][j] / col_sums[j]
    else:
        # dangling node: uniform teleport
        for i in range(n):
            S.data[i][j] = 1.0 / n
```

---

## 4. Step 3 — The Damped Google Matrix $G$

Real surfers don't always follow a link. The **damping factor** $\alpha = 0.85$ models this:

$$G_{ij} = \alpha\, S_{ij} + (1-\alpha)\,\frac{1}{n}$$

In matrix form:
$$G = \alpha\, S + \frac{(1-\alpha)}{n}\, J$$

where $J$ is the $n \times n$ all-ones matrix, so $J/n$ has every column equal to the uniform distribution.

- With probability $\alpha = 0.85$: follow a link according to $S$.
- With probability $1 - \alpha = 0.15$: jump to any random page uniformly.

$G$ is also column-stochastic (columns still sum to $1$).

```python
alpha = 0.85
J = Matrix([[1 for _ in range(n)] for _ in range(n)])
G = alpha * S + ((1 - alpha) / n) * J
```

---

## 5. Step 4 — Power Iteration (PageRank Algorithm)

We want the **dominant eigenvector** of $G$ (the eigenvector with eigenvalue $1$). The **power method** approximates it by repeatedly multiplying by $G$ and normalizing:

**Initialize**: $v_0 = [1/n, 1/n, \ldots, 1/n]^T$ (uniform distribution).

**Iterate** (at least 10–20 times):
$$w = G\, v^{(k)}, \qquad v^{(k+1)} = \frac{w}{\|w\|}$$

Each step moves the probability distribution one "click" forward. Normalizing keeps the vector bounded without changing its direction. After convergence, $v^{(k)} \to v_\star$ — the PageRank vector.

```python
v = Matrix([[1.0 / n] for i in range(n)])    # initial uniform vector

for i in range(10):
    w = G @ v                                 # one step of the dynamical system
    norm_w = w.norm()
    v = (1.0 / norm_w) * w                   # normalize
```

This is identical in structure to the LDS iteration $x_{t+1} = Ax_t$ from Chapter 9, just with a probability interpretation and a stochastic $G$.

---

## 6. Step 5 — Extracting the Top-Ranked Pages

After iteration, sort the entries of $v$ in descending order. The **top 10 indices** are the 10 highest-ranked pages in the network.

```python
scores = [v.data[i][0] for i in range(n)]
sorted_indices = sorted(range(n), key=lambda i: scores[i], reverse=True)

top_scores  = [scores[i] for i in sorted_indices[:10]]
top_indices = sorted_indices[:10]
```

---

## 7. Why This Works — Mathematical Perspective

$G$ is a **column-stochastic** matrix:
- All entries are nonneg.
- Every column sums to $1$.
- By the **Perron–Frobenius theorem**, such a matrix has a unique dominant eigenvalue $\lambda = 1$ with a unique positive eigenvector.

Because the teleportation term ($1-\alpha$ term) ensures every entry of $G$ is positive (not just nonneg.), the matrix is **primitive** (aperiodic and irreducible), which guarantees:
$$G^k x_0 \to x_\star \quad \text{for any starting } x_0 > 0 \text{ as } k \to \infty$$

The damping factor $\alpha = 0.85$ was chosen by Google empirically — it provides a good balance between following the link structure and allowing escape from "dangling" regions.

---

## Summary of key formulas

| Step | Formula |
|---|---|
| Adjacency matrix | $A_{ij} = 1$ if $i$ links to $j$ |
| Transition matrix | $S_{ij} = A_{ij}/\sum_{i'} A_{i'j}$ (columns sum to $1$) |
| Google matrix | $G = \alpha S + \frac{1-\alpha}{n}J$ |
| Power iteration | $v^{(k+1)} = Gv^{(k)}/\|Gv^{(k)}\|$ |
| Steady state | $Gv_\star = v_\star$ (eigenvector, $\lambda=1$) |
