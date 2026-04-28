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
## 1. Matrix–Matrix Multiplication

For $A$ of size $m \times p$ and $B$ of size $p \times n$, the product $C = AB$ is $m \times n$.

**The rule**: inner dimensions must match ($p = p$). Each entry of $C$ is:
$$C_{ij} = \sum_{k=1}^{p} A_{ik}\,B_{kj}$$

This is the inner product of row $i$ of $A$ with column $j$ of $B$.

### Three equivalent views

| View | Description |
|---|---|
| **Row-by-column** | Standard formula $C_{ij} = \sum_k A_{ik}B_{kj}$ |
| **Column view** | $C_{\cdot j} = A B_{\cdot j}$ — each column of $C$ is $A$ times the corresponding column of $B$ |
| **Outer-product (rank-1 sum)** | $C = \sum_{k=1}^p a_k b_k^T$ where $a_k$ is the $k$-th column of $A$ and $b_k^T$ is the $k$-th row of $B$ |

### Properties
- **Associative**: $(AB)C = A(BC)$
- **Distributive**: $A(B+C) = AB + AC$
- **NOT commutative**: $AB \ne BA$ in general
- **Transpose rule**: $(AB)^T = B^T A^T$

**Complexity**: multiplying $m \times p$ by $p \times n$ costs approximately $2mnp$ flops.

---

## 2. Composition of Linear Functions

The product $C = AB$ represents the **composition** of two linear functions: apply $B$ first, then $A$:
$$h(x) = f(g(x)) = A(Bx) = (AB)x$$

This is why order matters: $AB \ne BA$ in general (different compositions).

**Second difference matrix**: the difference matrix $D_n$ gives $(D_n x)_i = x_{i+1} - x_i$. The **second difference** is $\Delta = D_{n-1} D_n$:
$$(\Delta x)_i = x_i - 2x_{i+1} + x_{i+2}$$

This measures the curvature / roughness of a signal.

**Chain rule**: for composed vector-valued functions, the Jacobian of the composition is the product of the Jacobians: $Dh(z) = Df(g(z))\,Dg(z)$.

---

## 3. Matrix Powers and Linear Dynamical Systems

$A^k = A \cdot A \cdots A$ ($k$ times). Only defined for **square** matrices.

**Linear dynamical system (LDS)**: state evolves as $x_{t+1} = A x_t$. The state $L$ steps ahead is:
$$x_{t+L} = A^L x_t$$

$A^L$ captures the combined effect of $L$ sequential steps in one matrix.

**LDS with input**: if $x_{t+1} = Ax_t + Bu_t$, then:
$$x_{t+L} = A^L x_t + A^{L-1}Bu_t + A^{L-2}Bu_{t+1} + \cdots + Bu_{t+L-1}$$

**Graph paths**: if $A$ is an adjacency matrix, $(A^L)_{ij}$ = number of paths of length $L$ from vertex $j$ to vertex $i$.

---

## 4. Gram Matrix

The **Gram matrix** $G = A^T A$ has entries $G_{ij} = a_i \cdot a_j$ (inner product of columns $i$ and $j$ of $A$). It is always square and symmetric. Used in least squares and checking column orthogonality.

---

## 5. QR Factorization

The QR factorization decomposes an $m \times n$ matrix $A$ (with linearly independent columns, $m \ge n$) as:
$$A = QR$$

- $Q$ is $m \times n$ with **orthonormal columns**: $Q^T Q = I$
- $R$ is $n \times n$, **upper triangular**, with positive diagonal entries

QR is the matrix form of the Gram–Schmidt algorithm. A square matrix whose columns are orthonormal is called **orthogonal**; for such $Q$, the inverse is simply $Q^{-1} = Q^T$.

**Orthogonal matrices preserve geometry**: they keep vector lengths ($\|Qx\| = \|x\|$), inner products ($Qx \cdot Qy = x \cdot y$), and angles unchanged.

### Solving square systems $Ax = b$ via QR
1. Compute $A = QR$.
2. Compute $y = Q^T b$.
3. Solve $Rx = y$ using **back substitution** ($n^2$ flops).

Solution: $x = R^{-1} Q^T b$.

### Solving least squares problems $\min \|Ax - b\|^2$ via QR
Same steps — for a tall $A$ ($m > n$), the unique least-squares solution is $x = R^{-1} Q^T b$.

**Total cost**: dominated by the QR factorization, approximately $2mn^2$ flops.

---

## 6. Diagonal Matrices and Inverse

The **inverse** of a diagonal matrix $D = \text{diag}(d_1, \ldots, d_n)$ (all $d_i \ne 0$):
$$D^{-1} = \text{diag}(1/d_1, \ldots, 1/d_n)$$

**Matrix factorization from scaling**: if $S = A D^{-1}$ (scale columns of $A$ by $D^{-1}$), then $A = S D$.

---

## 7. Householder Reflector

A **Householder reflector** is an orthogonal matrix of the form:
$$Q = I - 2vv^T, \qquad \|v\| = 1$$

Properties:
- $Q$ is **orthogonal**: $Q^T Q = I$
- $Q$ is **symmetric**: $Q^T = Q$
- $Q$ is its own inverse: $Q^{-1} = Q^T = Q$
- It reflects any vector across the hyperplane perpendicular to $v$

### Constructing $v$ to zero out a column
Given a vector $x$, we want $Qx = \pm\|x\| e_1$ (all zeros below the first entry). The numerically stable procedure:

1. Compute $u = x + \text{sgn}(x_1)\,\|x\|\,e_1$ (adding to the first entry only)
2. Normalize: $v = u / \|u\|$
3. Then $Q = I - 2vv^T$ satisfies $Qx = -\text{sgn}(x_1)\,\|x\|\,e_1$

The sign choice prevents subtracting nearly equal numbers (avoids cancellation error).

```python
# constructing a Householder reflector for vector x
x[0][0] += x.norm() if x[0][0] >= 0 else -x.norm()   # update first entry (now x holds u)
v = x * (1 / x.norm())                                  # normalize to get v
Qt = I - 2 * v @ v.transpose()                          # reflector Q = I - 2vv^T
```

### Householder QR Algorithm
Apply a sequence of reflectors to zero out entries below the diagonal in each column:

$$H_1 A \to \begin{bmatrix} * & * & * \\ 0 & * & * \\ 0 & * & * \end{bmatrix} \quad \xrightarrow{H_2} \quad \begin{bmatrix} * & * & * \\ 0 & * & * \\ 0 & 0 & * \end{bmatrix} = R$$

$Q$ is the product of all reflectors: $Q = H_1 H_2 \cdots H_{n-1}$.

**Efficient implementation** (implicit $Q$ storage): instead of building the full $Q$, store the vectors $v_1, \ldots, v_{n-1}$ and apply them when needed.

**Update rule for submatrix at step $k$**:
$$A_{k:m,\;k:n} \leftarrow A_{k:m,\;k:n} - 2\,v\,\bigl(v^T A_{k:m,\;k:n}\bigr)$$

**Applying $Q^T$ to a vector $b$**: apply reflectors $k = 0 \to n-1$:
$$Q^T b: \quad \text{for } k = 0,1,\ldots,n-1: \quad b_{k:m} \leftarrow b_{k:m} - 2v_k(v_k^T b_{k:m})$$

**Applying $Q$ to a vector $x$**: apply reflectors **in reverse** $k = n-1 \to 0$.

### Gram–Schmidt vs. Householder

| Property | Classical Gram–Schmidt | Householder QR |
|---|---|---|
| Numerical stability | Poor | Excellent |
| Orthogonality of $Q$ | Approximate | Perfect (to machine precision) |
| Cost | $O(2mn^2)$ | $O(2mn^2 - 2n^3/3)$ |

Householder is the standard choice in practice.

---

## 8. PageRank as a Linear Dynamical System

The Google PageRank algorithm is an instance of an LDS with a stochastic matrix:

$$x_{t+1} = G x_t$$

where $x_t$ is the probability distribution over pages at step $t$ and $G$ is the **Google matrix** (column-stochastic). The steady-state vector satisfying $G x_\star = x_\star$ is the PageRank vector. This is exactly a matrix power iteration as in Chapter 9.

---

## Summary of key formulas

| Concept | Formula |
|---|---|
| Matrix product entry | $C_{ij} = \sum_k A_{ik} B_{kj}$ |
| Outer-product form | $AB = \sum_k a_k b_k^T$ |
| Transpose of product | $(AB)^T = B^T A^T$ |
| LDS state after $L$ steps | $x_{t+L} = A^L x_t$ |
| QR factorization | $A = QR$, $Q^T Q = I$, $R$ upper triangular |
| Solution via QR | $x = R^{-1} Q^T b$ |
| Orthogonal matrix inverse | $Q^{-1} = Q^T$ |
| Householder reflector | $Q = I - 2vv^T$, $\|v\|=1$ |
| Householder update | $A_{k:m,k:n} \leftarrow A_{k:m,k:n} - 2v(v^T A_{k:m,k:n})$ |
| Diagonal inverse | $(D^{-1})_{ii} = 1/d_i$ |
