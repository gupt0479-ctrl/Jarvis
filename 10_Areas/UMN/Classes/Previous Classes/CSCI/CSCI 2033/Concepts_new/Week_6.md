---
type: concept
status: complete
created: 2025-10-24
updated: 2025-10-25
week: "6"
chapters: "Ch. 7 & 8"
tags:
  - "#Textbook"
  - "#Lecture"
  - "#Jupyter"
  - "#Quiz"
  - "#Homework"
  - "#Graphs"
  - "#LinearAlgebra"
prev: [[Week_5]]
next: [[Week_8_and_9]]
---

# Week 6 — Geometric Transforms, Graphs, and Linear Equations
### Ch. 7: Matrix Examples | Ch. 8: Linear Equations

---

## 1. Geometric Transformations (Ch. 7.1)

A matrix $A$ is a machine that maps $x \mapsto y = Ax$. To know what a matrix does geometrically, you only need to know what it does to the standard basis vectors — the **columns of $A$** are the images of $e_1, e_2, \ldots$

### Scaling (uniform)
$$A = aI = \begin{bmatrix}a & 0 \\ 0 & a\end{bmatrix}$$

Every vector is stretched/shrunk by factor $a$. Direction preserved (unless $a < 0$, which flips).

### Dilation (non-uniform scaling)
$$D = \text{diag}(d_1, d_2) = \begin{bmatrix}d_1 & 0 \\ 0 & d_2\end{bmatrix}$$

Each axis scaled differently. Direction of vector **can change**.

### Rotation (CCW by $\theta$)
$$R(\theta) = \begin{bmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{bmatrix}$$

Length preserved. Angle changed by $\theta$. Columns = rotated basis vectors.

### Reflection (across line at angle $\phi$)
Special cases:
- $x$-axis: $\begin{bmatrix}1 & 0\\0 & -1\end{bmatrix}$ — $y$-component negated
- $y$-axis: $\begin{bmatrix}-1 & 0\\0 & 1\end{bmatrix}$

Key property: $A^2 = I$ (applying reflection twice returns to start). Length preserved, orientation reversed.

### Projection (onto unit vector $u$)
$$P = uu^T$$

For projection onto $x$-axis ($u = e_1$): $P = \begin{bmatrix}1 & 0\\0 & 0\end{bmatrix}$.

Key property: $P^2 = P$ (**idempotent** — projecting twice does nothing extra).

### Matrix Factorization View

From lecture: the matrix $G = \frac{1}{\sqrt{2}}R(-\pi/4)$ is geometrically $\approx A^{-1}$ for some $A$. If $G = A^{-1}$, then $G \cdot A = I$.

"Scale by $1/\sqrt{2}$, then rotate by $-\pi/4$" undoes "rotate by $+\pi/4$, then scale by $\sqrt{2}$."

---

## 2. Selector and Permutation Matrices (Ch. 7.2)

A **selector matrix** has each row = one transposed unit vector $e_{k_i}^T$. Multiplying by it picks specific entries from a vector: $y = Ax$ where $y_i = x_{k_i}$.

Applications: slicing, down-sampling (every 2nd entry), image cropping.

A **permutation matrix** is a square selector with exactly one $1$ per row and column. Multiplying re-orders the entries of a vector.

---

## 3. Graphs and Adjacency Matrices (Lab 6)

For a graph with $n$ vertices $\{0, \ldots, n-1\}$:
$$A[i,j] = \begin{cases}1 & \text{edge between } i \text{ and } j\\0 & \text{otherwise}\end{cases}$$

**Undirected graph**: $A$ is **symmetric** ($A[i,j] = A[j,i]$). Row $i$ = neighbors of $i$.

**Directed graph**: $A$ asymmetric. Different in/out degrees.

**Graph powers**: $(A^k)_{ij}$ = number of paths of length $k$ from $j$ to $i$.

```python
# mutual friends = number of 2-hop paths between i and j
A2 = A @ A
A3 = A @ A2     # 3-hop paths
```

Full graph theory reference: [[Graphs_and_PageRank]]

---

## 4. Incidence Matrix (Ch. 7.3)

For a **directed graph** ($n$ nodes, $m$ edges), the $n \times m$ incidence matrix $B$:
$$B_{ij} = \begin{cases}+1 & \text{edge }j\text{ points TO node }i\\-1 & \text{edge }j\text{ points FROM node }i\\0 & \text{otherwise}\end{cases}$$

**Flow conservation**: $Bx = \mathbf{0}$ means total flow in = total flow out at every node. With sources/sinks $s$: $Bx + s = \mathbf{0}$.

**Potential differences**: $u = B^T v$ gives potential differences across edges.

**Dirichlet energy** (roughness of potential field):
$$D(v) = \|B^T v\|^2 = \sum_{\text{edges}} (v_{\text{head}} - v_{\text{tail}})^2$$

---

## 5. Convolution (Ch. 7.4)

Convolution $c = a * b$ (sizes $n$ and $m$) produces vector $c$ of size $n + m - 1$:
$$c_k = \sum_{i+j=k+1} a_i b_j$$

If $a, b$ are polynomial coefficients, $c = a * b$ = product polynomial coefficients.

Matrix form: $c = T(a)\,b$ where $T(a)$ is a **Toeplitz matrix** (constant diagonals, shifted columns of $a$).

Applications: signal filtering, moving averages, image blurring (2D convolution).

---

## 6. Linear and Affine Functions of Vectors (Ch. 8.1)

$f : \mathbb{R}^n \to \mathbb{R}^m$ is **linear** $\iff$ $f(x) = Ax$ for some unique $m \times n$ matrix $A$.

**Columns of $A$**: the $k$-th column is $f(e_k)$ — the output for the $k$-th standard basis vector.

**Affine function**: $f(x) = Ax + b$. Satisfies superposition only for affine combinations ($\alpha + \beta = 1$).

**Jacobian** of $f$ at $z$: the $m \times n$ matrix $Df(z)$ of partial derivatives. Taylor approximation:
$$\hat{f}(x) = f(z) + Df(z)(x - z)$$

---

## 7. Systems of Linear Equations (Ch. 8.3)

$$Ax = b \qquad (m \text{ equations}, n \text{ unknowns})$$

- **Over-determined** ($m > n$, tall $A$): usually no exact solution → least squares
- **Under-determined** ($m < n$, wide $A$): infinitely many solutions
- **Square** ($m = n$): unique solution if $A$ invertible
- **Homogeneous** ($Ax = \mathbf{0}$): $x = \mathbf{0}$ always works; nontrivial solution exists iff columns are LD

**Geometric (column) view**: $Ax = b$ asks "is $b$ a linear combination of the columns of $A$?"

---

## 8. Diagonal Matrix Scaling Rules (Quiz 5)

| Multiplication | Effect |
|---|---|
| $cA$ | Scale all entries by $c$ |
| $AD$ | Scale **columns** of $A$: $(AD)_{ij} = A_{ij}d_j$ |
| $DA$ | Scale **rows** of $A$: $(DA)_{ij} = d_i A_{ij}$ |
| $PA$ (permutation) | Reorder **rows** of $A$ |
| $AP$ | Reorder **columns** of $A$ |

---

## 9. Jacobi Iterative Method

Solve $Ax = b$ iteratively. Split $A = M + N$ where $M = \text{diag}(A)$.

**Fixed-point form**: $x = M^{-1}(b - Nx)$

**Iteration** (starting from guess $x^{(0)}$):
$$x^{(k+1)} = M^{-1}(b - Nx^{(k)})$$

Converges when $A$ is diagonally dominant. Each step: invert $M$ (free, it's diagonal), multiply by $N$, subtract from $b$.

---

## Summary

| Concept | Formula |
|---|---|
| 2D rotation (CCW $\theta$) | $R(\theta) = \begin{bmatrix}\cos\theta & -\sin\theta\\\sin\theta & \cos\theta\end{bmatrix}$ |
| Projection onto $u$ | $P = uu^T$, $P^2 = P$ |
| Reflection | $A^2 = I$ |
| Incidence matrix | $B_{ij} = +1$ (to), $-1$ (from) |
| Flow conservation | $Bx + s = \mathbf{0}$ |
| Dirichlet energy | $D(v) = \|B^Tv\|^2$ |
| Convolution output size | $n + m - 1$ |
| Right-mult by diagonal | Scales columns |
| Left-mult by diagonal | Scales rows |
| Jacobi iteration | $x^{(k+1)} = M^{-1}(b-Nx^{(k)})$ |
