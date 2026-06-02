---
type: concept
status: complete
created: 2025-11-07
updated: 2025-11-15
week: "8 & 9"
chapters: "Ch. 9 & 10"
tags:
  - "#Textbook"
  - "#Lecture"
  - "#Jupyter"
  - "#Quiz"
  - "#Homework"
  - "#LinearAlgebra"
prev: [[Week_6]]
next: [[Week_10]]
---

# Weeks 8 & 9 — Matrix Products, QR Factorization, and Householder Reflectors
### Ch. 9: Linear Dynamical Systems | Ch. 10: Matrix–Matrix Products and Factorizations

---

## 1. Matrix–Matrix Multiplication

$A$ is $m \times p$, $B$ is $p \times n$ → $C = AB$ is $m \times n$. Inner dimensions must match.

$$C_{ij} = \sum_{k=1}^{p} A_{ik}\,B_{kj}$$

This is the inner product of row $i$ of $A$ with column $j$ of $B$.

### Three equivalent views

| View | Description | When useful |
|---|---|---|
| **Row-by-column** | $C_{ij} = \sum_k A_{ik}B_{kj}$ | Standard formula |
| **Column view** | $C_{\cdot j} = A\,B_{\cdot j}$ | Solving $AX = B$ for multiple RHS |
| **Outer-product (rank-1 sum)** | $C = \sum_{k=1}^p a_k b_k^T$ | Understanding low-rank structure |

### Properties

- **Associative**: $(AB)C = A(BC)$
- **Distributive**: $A(B+C) = AB + AC$
- **NOT commutative**: $AB \ne BA$ in general
- **Transpose rule**: $(AB)^T = B^T A^T$

**Complexity**: multiplying $m \times p$ by $p \times n$ costs $\approx 2mnp$ flops.

---

## 2. Composition of Linear Functions

$C = AB$ represents applying $B$ first, then $A$:
$$h(x) = f(g(x)) = A(Bx) = (AB)x$$

This is why order matters: $AB \ne BA$ in general.

**Second difference matrix**: $D_n$ computes consecutive differences $(D_n x)_i = x_{i+1} - x_i$. The composition $\Delta = D_{n-1} D_n$ computes:
$$(\Delta x)_i = x_i - 2x_{i+1} + x_{i+2}$$

This measures curvature / roughness of a signal — reappears in signal processing and regularization.

**Chain rule** for Jacobians: $Dh(z) = Df(g(z))\,Dg(z)$.

---

## 3. Matrix Powers and Linear Dynamical Systems

$A^k$ = $A$ multiplied by itself $k$ times (only for **square** matrices).

**LDS**: $x_{t+1} = Ax_t$ → state $L$ steps later:
$$x_{t+L} = A^L x_t$$

**LDS with input** $u$: $x_{t+1} = Ax_t + Bu_t$:
$$x_{t+L} = A^L x_t + A^{L-1}Bu_t + A^{L-2}Bu_{t+1} + \cdots + Bu_{t+L-1}$$

**Graph paths**: for adjacency matrix $A$, entry $(A^L)_{ij}$ = number of paths of **length $L$** from vertex $j$ to vertex $i$.

**PageRank connection**: $x_{t+1} = Gx_t$ is an LDS. The steady-state $x_\star = Gx_\star$ is the PageRank vector. See [[Graphs_and_PageRank]].

---

## 4. QR Factorization

Decomposes $A$ ($m \times n$, $m \ge n$, LI columns) as:
$$A = QR$$

- $Q$ is $m \times n$ with **orthonormal columns**: $Q^T Q = I$
- $R$ is $n \times n$, **upper triangular**, positive diagonal entries

QR is the matrix form of Gram–Schmidt. A square orthogonal matrix satisfies $Q^{-1} = Q^T$.

**Orthogonal matrices preserve geometry**: $\|Qx\| = \|x\|$, $Qx \cdot Qy = x \cdot y$, and angles unchanged.

### Solving $Ax = b$ via QR (square, invertible $A$)
1. Compute $A = QR$
2. Compute $y = Q^T b$
3. Solve $Rx = y$ using **back substitution** ($n^2$ flops)

Solution: $x = R^{-1} Q^T b$. Total cost dominated by factorization: $\approx 2mn^2$ flops.

### Solving least squares $\min \|Ax - b\|^2$ (tall $A$)
Same three steps — unique least squares solution is $\hat{x} = R^{-1}Q^T b$.

---

## 5. Diagonal Matrices and Scaling

$$D_{ij} = \begin{cases} d_j & i = j \\ 0 & i \ne j \end{cases}$$

- **$AD$ (right-multiply)** → scales **columns**: $(AD)_{ij} = A_{ij}\,d_j$
- **$DA$ (left-multiply)** → scales **rows**: $(DA)_{ij} = d_i\,A_{ij}$

**Inverse of diagonal**: $(D^{-1})_{ii} = 1/d_i$ (all $d_i \ne 0$).

**Factorization insight**: if $S = A D^{-1}$ then $A = SD$. Scaling-then-factoring = factorization.

---

## 6. Householder Reflector

A Householder reflector is an orthogonal matrix:
$$Q = I - 2vv^T, \qquad \|v\| = 1$$

Properties:
- Orthogonal: $Q^TQ = I$
- Symmetric: $Q^T = Q$
- Self-inverse: $Q^{-1} = Q^T = Q$
- Reflects any vector across the hyperplane perpendicular to $v$

### Construction — how to zero out entries below the first

Given vector $x$, build $Q$ such that $Qx = -\text{sgn}(x_1)\|x\|e_1$:

1. $u = x + \text{sgn}(x_1)\,\|x\|\,e_1$ (add to the first entry only)
2. Normalize: $v = u / \|u\|$
3. $Q = I - 2vv^T$

The $\text{sgn}(x_1)$ sign choice prevents numerical cancellation (catastrophic subtraction).

```python
x[0][0] += x.norm() if x[0][0] >= 0 else -x.norm()   # u = x + sgn(x1)||x||e1
v  = x * (1.0 / x.norm())                              # normalize to get v
Qt = I - 2 * v @ v.transpose()                         # Q = I - 2vv^T
```

### Householder QR Algorithm (Lab 7)

Apply a sequence of reflectors to zero out below the diagonal in each column:

**Pseudo-code**:
```
for k = 0 to n-1:
    x  = A[k:m, k]                               # extract current column
    v  = sgn(x[0]) * ||x|| * e_0 + x            # compute u
    v  = v / ||v||                               # normalize
    A[k:m, k:n] = A[k:m, k:n] - 2v(v^T A[k:m, k:n])   # update submatrix
```

After all steps, $A$ becomes $R$ (upper triangular). The stored vectors $v_0, \ldots, v_{n-1}$ implicitly define $Q$.

**Why store $v$ vectors instead of $Q$?** Storing the full $Q$ would cost $m^2$ memory. Storing the $n$ vectors costs $O(mn)$, and we can apply $Q$ or $Q^T$ on the fly.

### Applying $Q^T$ to a vector $b$ (Qstarb)

Apply reflectors **forward** ($k = 0 \to n-1$):
$$\text{for } k = 0, 1, \ldots, n-1: \quad b_{k:m} \leftarrow b_{k:m} - 2v_k(v_k^T b_{k:m})$$

```python
def Qstarb(V, b):
    out = 1.0 * b
    for k in range(len(V)):
        out[k:m] = out[k:m] - 2 * V[k] * (V[k].transpose() @ out[k:m])[0][0]
    return out
```

### Applying $Q$ to a vector $x$ (Qx)

Apply reflectors **backward** ($k = n-1 \to 0$):

```python
def Qx(V, x):
    out = 1.0 * x
    for k in range(len(V) - 1, -1, -1):
        out[k:m] = out[k:m] - 2 * V[k] * (V[k].transpose() @ out[k:m])[0][0]
    return out
```

**Forming $Q^T$ explicitly**: apply `Qstarb(V, e_i)` for each standard basis vector $e_i$ and collect as columns.

**Forming $Q$ explicitly**: apply `Qx(V, e_i)` for each $e_i$ and collect as columns.

---

## 7. Gram–Schmidt vs. Householder

| Property | Classical Gram–Schmidt | Householder QR |
|---|---|---|
| Numerical stability | Poor | Excellent |
| $Q$ orthogonality | Approximate | Perfect (to machine precision) |
| Cost | $O(2mn^2)$ | $O(2mn^2 - 2n^3/3)$ |
| How $Q$ is stored | Explicitly | Implicitly (Householder vectors $v_k$) |

Householder is the standard algorithm in practice for this reason.

---

## Quiz Notes

- $(AB)^T = B^T A^T$ — most commonly tested transpose rule
- $AB \ne BA$ in general
- A Householder reflector uses **reflections**, NOT rotations
- Inverting a matrix entry-wise ($(A^{-1})_{ij} = 1/A_{ij}$) is **wrong** — only works for diagonal matrices

---

## Summary

| Concept | Formula |
|---|---|
| Matrix product entry | $C_{ij} = \sum_k A_{ik}B_{kj}$ |
| Outer-product form | $AB = \sum_k a_k b_k^T$ |
| Transpose of product | $(AB)^T = B^T A^T$ |
| LDS state after $L$ steps | $x_{t+L} = A^L x_t$ |
| QR factorization | $A = QR$, $Q^TQ = I$, $R$ upper triangular |
| Solve via QR | $x = R^{-1}Q^Tb$ |
| Orthogonal inverse | $Q^{-1} = Q^T$ |
| Householder reflector | $Q = I - 2vv^T$, $\|v\|=1$ |
| Submatrix update | $A_{k:m,k:n} \leftarrow A_{k:m,k:n} - 2v(v^T A_{k:m,k:n})$ |
