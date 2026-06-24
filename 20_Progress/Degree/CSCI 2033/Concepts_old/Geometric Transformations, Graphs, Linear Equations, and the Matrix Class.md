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
## 1. Geometric Transformations

A matrix $A$ acts as a **machine** that maps an input vector $x$ to a new output vector $y = Ax$. Understanding what a matrix *does geometrically* is crucial.

**Key insight**: the columns of $A$ are the images of the standard basis vectors.
- First column $= A e_1$
- Second column $= A e_2$, etc.

So if you know how the transformation acts on $e_1$ and $e_2$, you know the whole matrix.

### Scaling (uniform)
$$A = aI = \begin{bmatrix} a & 0 \\ 0 & a \end{bmatrix}$$
Every vector is stretched or shrunk by factor $a$. Direction is preserved (unless $a < 0$, which flips it). Length changes, angle does not.

### Dilation (non-uniform scaling)
$$D = \text{diag}(d_1, d_2) = \begin{bmatrix} d_1 & 0 \\ 0 & d_2 \end{bmatrix}$$
Each coordinate axis is scaled by a different factor. The direction of the vector **can change** because the $x$- and $y$-components are stretched differently.

### Rotation (2D, counterclockwise by angle $\theta$)
$$R(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$
- Length of the vector is **preserved**.
- Direction is rotated by $\theta$.
- All points rotate around the origin.

For example, $R(\pi/4)$ rotates $45°$ counterclockwise. The columns of $R(\theta)$ are exactly the rotated basis vectors.

### Reflection
Reflects the vector across a line through the origin (the **mirror line**). Special cases:
- Reflect across the $x$-axis: $\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$
- Reflect across the $y$-axis: $\begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}$

Key properties: $A^2 = I$ (reflecting twice returns to start); length is preserved; orientation is reversed.

### Projection (onto a line through the origin)
For projection onto the line spanned by unit vector $u$:
$$P = u u^T$$

For projection onto the $x$-axis ($u = e_1$): $P = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$.

Key property: $P^2 = P$ (**idempotent** — projecting twice does nothing extra).

---

## 2. Selector Matrices and Permutation Matrices

A **selector matrix** has each row equal to a transposed unit vector $e_{k_i}^T$. When applied to a vector, it selects (picks out) specific entries. Uses: slicing, down-sampling, image cropping.

A **permutation matrix** is a square selector matrix with exactly one $1$ per row and per column. Multiplying a vector by a permutation matrix **reorders its entries**.

---

## 3. Incidence Matrix

For a directed graph with $n$ nodes and $m$ edges, the **incidence matrix** $A$ is $n \times m$. Each column corresponds to one edge and has exactly two nonzero entries: $+1$ at the node the edge points **to** and $-1$ at the node the edge points **from**.

### Flow conservation
Let $x$ be an $m$-vector of flow rates on edges. Then $y = Ax$ gives the **net flow surplus** at each node. If $Ax = \mathbf{0}$, flow is conserved everywhere. With external sources/sinks $s$: $Ax + s = \mathbf{0}$.

### Potentials and Dirichlet energy
Let $v$ be an $n$-vector of node potentials (e.g., voltages). Then $u = A^T v$ gives the **potential differences** across edges.

**Dirichlet energy** measures roughness:
$$D(v) = \|A^T v\|^2$$

Minimizing $D(v)$ forces adjacent node potentials to be similar (smooth). For a chain graph, $D(v)$ is the sum of squared consecutive differences.

### Adjacency matrix for an undirected graph
For a graph with $n$ vertices $\{0, \ldots, n-1\}$:
$$A[i,j] = \begin{cases} 1 & \text{if there is an edge between } i \text{ and } j \\ 0 & \text{otherwise} \end{cases}$$

For an undirected graph, $A$ is **symmetric**: $A[i,j] = A[j,i]$. The entry $(A^k)_{ij}$ counts the number of paths of length $k$ from vertex $j$ to vertex $i$.

---

## 4. Convolution

**Convolution** $c = a * b$ of an $n$-vector $a$ and $m$-vector $b$ produces a vector $c$ of size $n + m - 1$:
$$c_k = \sum_{i + j = k+1} a_i b_j$$

If $a$ and $b$ are polynomial coefficients, then $c = a * b$ gives the coefficients of the product polynomial.

Because convolution is linear, it can be written as $c = T(a)\,b$ where $T(a)$ is a **Toeplitz matrix** — constant along diagonals, columns are shifted versions of $a$.

Applications: signal filtering, moving averages, image blurring (2D convolution).

---

## 5. Chapter 8 Recap — Linear and Affine Functions (Vector-Valued)

A function $f : \mathbb{R}^n \to \mathbb{R}^m$ is **linear** iff there exists a unique $m \times n$ matrix $A$ with $f(x) = Ax$. The **columns of $A$** are $f(e_1), f(e_2), \ldots, f(e_n)$.

An **affine function** is $f(x) = Ax + b$. The matrix $A$ is the Jacobian (derivative) matrix. For scalar functions, this reduces to $\hat{f}(x) = f(z) + \nabla f(z)^T(x-z)$.

**Systems of linear equations**: $Ax = b$.
- Over-determined ($m > n$, tall $A$): more equations than unknowns, generally no exact solution.
- Under-determined ($m < n$, wide $A$): fewer equations than unknowns, generally infinitely many solutions.
- Square ($m = n$): same number of equations and unknowns.

---

## 6. Diagonal Matrix Scaling — Left vs. Right

Let $D = \text{diag}(d_1, \ldots, d_n)$.

**Right-multiply $AD$** (scales **columns**):
$$(AD)_{ij} = A_{ij}\,d_j$$
Column $j$ of $A$ is multiplied by $d_j$.

**Left-multiply $DA$** (scales **rows**):
$$(DA)_{ij} = d_i\,A_{ij}$$
Row $i$ of $A$ is multiplied by $d_i$.

Other useful rules: $PA$ (permutation on left) **reorders rows** of $A$; $AP$ **reorders columns** of $A$; $A^T$ **swaps rows and columns**.

---

## 7. Jacobi Iterative Method

For a linear system $Ax = b$, the **Jacobi method** finds an approximate solution iteratively instead of solving exactly.

**Idea**: split $A = M + N$ where $M$ is the diagonal part of $A$ and $N$ is the off-diagonal remainder. Then $Ax = b$ becomes $Mx = b - Nx$, which gives a fixed-point equation:
$$x = M^{-1}(b - Nx)$$

**Iteration**: starting from an initial guess $x^{(0)}$:
$$x^{(k+1)} = M^{-1}\!\left(b - N x^{(k)}\right)$$

For a diagonal $M$, $M^{-1}$ is free to compute (just invert each diagonal entry). This converges when $A$ is diagonally dominant.

---

## 8. Graph Power Interpretation

If $C$ is the adjacency matrix of a friendship network:
- $(C^2)_{ij} = \sum_k C_{ik} C_{kj}$ = number of **mutual friends** between $i$ and $j$ (2-hop paths).
- $(C^3)_{ij}$ = number of 3-step paths from $j$ to $i$.

```python
A2 = A @ A        # 2-step paths
A3 = A @ A2       # 3-step paths
```

---

## Summary of key formulas

| Concept | Formula |
|---|---|
| 2D rotation (CCW by $\theta$) | $R(\theta) = \begin{bmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{bmatrix}$ |
| Projection onto unit vector $u$ | $P = uu^T$, satisfies $P^2 = P$ |
| Reflection double application | $A^2 = I$ |
| Incidence matrix flow balance | $Ax + s = \mathbf{0}$ |
| Dirichlet energy | $D(v) = \|A^T v\|^2$ |
| Convolution size | $n + m - 1$ |
| Right-mult. by diagonal | $(AD)_{ij} = A_{ij}\,d_j$ (scales columns) |
| Left-mult. by diagonal | $(DA)_{ij} = d_i\,A_{ij}$ (scales rows) |
| Jacobi iteration | $x^{(k+1)} = M^{-1}(b - Nx^{(k)})$ |
