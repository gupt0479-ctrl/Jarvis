---
type: reference
status: complete
created: 2025-12-31
topic: "Matrix Operations"
tags:
  - "#LinearAlgebra"
  - "#Reference"
  - "#Matrices"
related: [[Week_5]], [[Week_8_and_9]], [[Week_10]]
---

# Matrix Operations — Complete Reference
### Everything in one place

---

## 1. Matrix Types

| Type | Condition | Notes |
|---|---|---|
| Square | $m = n$ | Can be invertible |
| Tall | $m > n$ | Least squares problems |
| Wide | $n > m$ | Under-determined systems |
| Zero $\mathbf{0}$ | All entries $0$ | Additive identity |
| Identity $I$ | $I_{ii}=1$, else $0$ | Multiplicative identity |
| Diagonal $\text{diag}(d)$ | Off-diagonal $= 0$ | Scales rows or columns |
| Symmetric | $A = A^T$ | Always square |
| Upper triangular | $A_{ij}=0$ for $i>j$ | From QR, back-sub |
| Lower triangular | $A_{ij}=0$ for $i<j$ | From LU |
| Orthogonal | $Q^TQ = I$ | Preserves lengths/angles |
| Column-stochastic | Columns sum to $1$, all $\ge 0$ | PageRank, Markov chains |
| Sparse | Many zeros | Real-world graphs |

---

## 2. Core Operations

### Addition and Scalar Multiplication
$(A+B)_{ij} = A_{ij} + B_{ij}$ (same size required).
$(\alpha A)_{ij} = \alpha A_{ij}$.

### Transpose
$(A^T)_{ij} = A_{ji}$. Size $m\times n \to n\times m$.

$(A^T)^T = A$, \quad $(A+B)^T = A^T + B^T$, \quad $(AB)^T = B^T A^T$

### Matrix–Vector Multiply ($Ax$)
$A$ is $m\times n$, $x$ is $n$-vector, $y = Ax$ is $m$-vector.

**Row view**: $y_i = (\text{row }i)^T x$

**Column view**: $y = x_1 a_1 + x_2 a_2 + \cdots + x_n a_n$ (linear combination of columns)

### Matrix–Matrix Multiply ($AB = C$)
$A$ is $m\times p$, $B$ is $p\times n$, $C$ is $m\times n$.

$$C_{ij} = \sum_{k=1}^p A_{ik}B_{kj}$$

**Column view**: $C_{\cdot j} = A B_{\cdot j}$

**Outer-product**: $C = \sum_{k=1}^p a_k b_k^T$ (sum of rank-1 matrices)

Not commutative: $AB \ne BA$ in general.

---

## 3. Diagonal Matrix Rules

$D = \text{diag}(d_1,\ldots,d_n)$

| Product | Effect |
|---|---|
| $AD$ | Scales **columns** of $A$ by $d_j$ |
| $DA$ | Scales **rows** of $A$ by $d_i$ |
| $PA$ (permutation) | **Reorders rows** of $A$ |
| $AP$ | **Reorders columns** of $A$ |

**Inverse**: $D^{-1} = \text{diag}(1/d_1,\ldots,1/d_n)$ (requires all $d_i \ne 0$).

---

## 4. The Frobenius Norm

$$\|A\|_F = \sqrt{\sum_{i,j} A_{ij}^2}$$

Satisfies: nonnegativity, definiteness, homogeneity, triangle inequality.

---

## 5. Inverses

**Square inverse** $A^{-1}$: $AA^{-1} = A^{-1}A = I$. Exists $\iff$ columns (= rows) are LI.

**Left inverse** $C$: $CA = I$ (tall $A$, LI columns).

**Right inverse** $B$: $AB = I$ (wide $A$, LI rows).

**Pseudo-inverse** $A^\dagger$:
- Tall: $A^\dagger = (A^TA)^{-1}A^T = R^{-1}Q^T$
- Wide: $A^\dagger = A^T(AA^T)^{-1}$

Key identities:
$(AB)^{-1} = B^{-1}A^{-1}$, \quad $(A^T)^{-1} = (A^{-1})^T$, \quad $Q^{-1} = Q^T$ (orthogonal)

---

## 6. Factorizations

### QR Factorization
$$A = QR, \qquad Q^TQ = I, \qquad R \text{ upper triangular}$$

- $Q$ has orthonormal columns; $R$ has positive diagonal
- For square $A$: $Q$ is orthogonal ($QQ^T = I$ also)
- Computed via **Gram–Schmidt** or **Householder reflectors** (preferred)

**Householder reflector**: $H = I - 2vv^T$, $\|v\|=1$

Algorithm: for $k = 0 \to n-1$:
$$A_{k:m,k:n} \leftarrow A_{k:m,k:n} - 2v_k(v_k^T A_{k:m,k:n})$$

**Applying $Q^T$** (forward pass): apply $v_k$ for $k=0\to n-1$

**Applying $Q$** (backward pass): apply $v_k$ for $k=n-1\to 0$

### SVD
$$A = U\Sigma V^T$$

$U$ ($m\times m$, orthogonal), $\Sigma$ ($m\times n$, diagonal, $\sigma_1 \ge \sigma_2 \ge \cdots \ge 0$), $V$ ($n\times n$, orthogonal).

Best rank-$\ell$ approximation: $\hat{A}_\ell = \sum_{k=1}^\ell \sigma_k u_k v_k^T$, error $= \sigma_{\ell+1}$.

---

## 7. Solving Linear Systems

| System | Shape | Method | Solution |
|---|---|---|---|
| $Ax = b$, square | $n\times n$ | QR: $A=QR$, solve $Rx = Q^Tb$ | $x = R^{-1}Q^Tb$ |
| $Ax \approx b$, over-det. | Tall | Least squares via QR | $\hat{x} = R^{-1}Q^Tb$ |
| $Rx = b$, triangular | Any | Back substitution | Direct, $n^2$ flops |

**Normal equations** (least squares): $A^TAx = A^Tb$ → $\hat{x} = (A^TA)^{-1}A^Tb$.

---

## 8. Complexity Summary

| Operation | Cost |
|---|---|
| Vector inner product (length $n$) | $2n$ |
| Matrix–vector ($m\times n$) | $2mn$ |
| Matrix–matrix ($m\times p$ times $p\times n$) | $2mnp$ |
| QR factorization ($m\times n$) | $\approx 2mn^2$ |
| Back substitution ($n\times n$) | $n^2$ |
| SVD ($m\times n$) | $O(mn\min(m,n))$ |
| Gram–Schmidt ($n$-vectors, $k$ of them) | $2nk^2$ |

---

## 9. Python Class Hierarchy

```
Matrix (base)
├── zeros(m,n)
├── ones(m,n)
├── diag(d)
│   └── eye(n)
└── Vector(X)       ← column vector (n×1 Matrix)
```

Key methods: `@` (matmul), `norm()`, `transpose()`, `__getitem__` / `__setitem__` with slices.

---

## 10. Gram Matrix

$G = A^TA$ (size $n\times n$). Entry $G_{ij}$ = inner product of columns $i$ and $j$ of $A$.

Always symmetric and positive semi-definite. Used in normal equations, kernel methods, and PCA.
