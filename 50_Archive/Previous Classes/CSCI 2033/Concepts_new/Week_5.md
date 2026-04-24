---
type: concept
status: archived
created: 2025-10-17
updated: 2025-10-19
week: "5"
chapters: "Ch. 5 & 6"
tags:
  - "#Textbook"
  - "#Lecture"
  - "#Jupyter"
  - "#Homework"
  - "#LinearAlgebra"
prev: [[Week_4]]
next: [[Week_6]]
---

# Week 5 — Linear Independence, Gram–Schmidt, and the Matrix Class
### Ch. 5: Linear Independence | Ch. 6: Matrices

---

## 1. Linear Dependence and Independence

### Linear dependence
Vectors $a_1, \ldots, a_k$ are **linearly dependent** if there exist scalars $\beta_1, \ldots, \beta_k$ — **not all zero** — such that:
$$\beta_1 a_1 + \cdots + \beta_k a_k = \mathbf{0}$$

Dependence = redundancy: at least one vector is a linear combination of the others.

Automatic dependency cases: any set containing $\mathbf{0}$; two vectors where one is a scalar multiple of the other.

### Linear independence
The collection is **linearly independent** if the equation above has **only the trivial solution** $\beta_1 = \cdots = \beta_k = 0$.

**Key property**: when LI, coefficients expressing any vector as a combination are **unique**.

**Independence-dimension inequality**: if $a_1, \ldots, a_k$ are LI $n$-vectors, then $k \le n$. You cannot have more than $n$ LI vectors in $\mathbb{R}^n$.

**In matrix language**: columns of $A$ are LI $\iff$ $Ax = \mathbf{0}$ implies $x = \mathbf{0}$.

---

## 2. Basis

$n$ vectors $a_1, \ldots, a_n$ form a **basis** for $\mathbb{R}^n$ if they are linearly independent.

**Expansion**: any $n$-vector $b$ can be written **uniquely** as:
$$b = \alpha_1 a_1 + \cdots + \alpha_n a_n$$

The standard basis $e_1, \ldots, e_n$ is the most familiar example.

---

## 3. Orthonormal Vectors

**Orthogonal**: every distinct pair satisfies $a_i^T a_j = 0$.

**Orthonormal**: orthogonal AND every vector has unit norm:
$$a_i^T a_j = \begin{cases} 1 & i = j \\ 0 & i \ne j \end{cases}$$

Orthonormal vectors are always LI.

**Easy coefficient extraction**: if $x = \sum \beta_i a_i$ with orthonormal $a_i$:
$$\beta_i = a_i^T x$$

**Orthonormal basis expansion**:
$$x = (a_1^T x)\,a_1 + \cdots + (a_n^T x)\,a_n$$

---

## 4. Gram–Schmidt Algorithm

Takes $a_1, \ldots, a_k$ and produces an orthonormal set $q_1, \ldots, q_k$. Also detects linear dependence.

**For each $a_i$**:
1. **Orthogonalize**: remove the components parallel to all previous $q_j$:
$$\tilde{q}_i = a_i - \sum_{j=1}^{i-1} (q_j^T a_i)\,q_j$$
2. **Check**: if $\tilde{q}_i = \mathbf{0}$ → $a_i$ is a linear combination of earlier vectors → **dependent** → stop.
3. **Normalize**: $q_i = \tilde{q}_i / \|\tilde{q}_i\|$.

**Result**: if no early termination, $a_1, \ldots, a_k$ are LI and $q_1, \ldots, q_k$ are orthonormal.

**QR connection**: Gram–Schmidt on columns of $A$ gives $A = QR$ where $Q$ has orthonormal columns and $R$ is upper triangular.

**Complexity**: $\approx 2nk^2$ flops.

---

## 5. Matrix Types and Definitions (Lab 5)

A matrix is a rectangular array: **$m \times n$** ($m$ rows, $n$ columns). Entry in row $i$, column $j$ is $A_{ij}$.

| Type | Condition |
|---|---|
| Square | $m = n$ |
| Tall | $m > n$ |
| Wide | $n > m$ |
| Zero matrix $\mathbf{0}$ | all entries zero |
| Identity $I$ | $I_{ij} = 1$ if $i=j$, else $0$ |
| Diagonal $\text{diag}(d)$ | $A_{ij} = 0$ for $i \ne j$ |
| Upper triangular | $A_{ij} = 0$ for $i > j$ |
| Sparse | many zeros; density $= \text{nnz}(A)/(mn)$ |

Triangular $n \times n$ matrix has ≤ $n(n+1)/2$ nonzeros (≈ 50% full — not considered sparse).

---

## 6. Matrix Class (Lab 5)

The `Matrix` class stores data as a list of lists. All operators defined to enable clean math syntax.

```python
class Matrix:
    def __init__(self, X=[[]]):
        self.data  = [[x for x in row] for row in X]
        self.m     = len(X)          # rows
        self.n     = len(X[0])       # cols
        self.shape = self.m, self.n

    def __matmul__(self, other):     # C = A @ B
        if self.n != other.m: raise Exception("Dimensions do not match")
        output = Matrix([[0]*other.n for _ in range(self.m)])
        for i in range(self.m):
            for j in range(other.n):
                for k in range(self.n):
                    output.data[i][j] += self.data[i][k] * other.data[k][j]
        return output

    def norm(self):                  # Frobenius norm
        output = 0.0
        for i in range(self.m):
            for j in range(self.n):
                output += self.data[i][j] ** 2
        return output ** 0.5

    def transpose(self):
        output = Matrix([[0]*self.m for _ in range(self.n)])
        for i in range(self.n):
            for j in range(self.m):
                output.data[i][j] = self.data[j][i]
        return output
```

**Subclasses**:
```python
class zeros(Matrix):
    def __init__(self, m, n):
        super().__init__([[0.0]*n for _ in range(m)])

class diag(Matrix):
    def __init__(self, d):
        super().__init__([[0.0]*len(d) for _ in range(len(d))])
        for i in range(len(d)): self.data[i][i] = d[i]

class eye(diag):
    def __init__(self, n=3): super().__init__([1.0]*n)

class Vector(Matrix):              # Vector as a column matrix
    def __init__(self, X=[]):
        super().__init__([[x] for x in X])
```

**Slicing** (colon notation): `A[k:m, k:n]` returns a submatrix. Setitem supports the same for in-place updates.

---

## 7. Matrix–Vector Multiplication

$A$ is $m \times n$, $x$ is $n$-vector → $y = Ax$ is $m$-vector.

**Row interpretation**: $y_i = (\text{row } i \text{ of } A)^T x$

**Column interpretation**: $y = Ax$ is a linear combination of the columns of $A$:
$$y = x_1 a_1 + x_2 a_2 + \cdots + x_n a_n$$

$Ae_j = a_j$ — unit vector selects column $j$.

---

## 8. Transpose, Norm, Complexity

**Transpose**: $(A^T)_{ij} = A_{ji}$, size $n \times m$. $(A^T)^T = A$. Symmetric if $A = A^T$.

$(A+B)^T = A^T + B^T$

**Frobenius norm** (matrix norm):
$$\|A\| = \sqrt{\sum_{i,j} A_{ij}^2}$$

| Operation | Cost |
|---|---|
| Matrix add/scalar mult ($m \times n$) | $mn$ flops |
| Transpose | 0 flops |
| Matrix–vector multiply $Ax$ | $2mn$ flops |
| Matrix storage (dense) | $8mn$ bytes |
| Sparse storage | $\approx 16\,\text{nnz}(A)$ bytes |

---

## Summary

| Concept | Formula / Condition |
|---|---|
| Linear dependence | $\exists\,\beta \ne \mathbf{0}$ s.t. $\sum\beta_i a_i = \mathbf{0}$ |
| Basis expansion | $b = \sum \alpha_i a_i$ (unique) |
| Orthonormal condition | $a_i^T a_j = \delta_{ij}$ |
| G–S coefficient | $\beta_i = a_i^T x$ |
| Column view of $Ax$ | $Ax = x_1 a_1 + \cdots + x_n a_n$ |
| Frobenius norm | $\|A\| = \sqrt{\sum_{i,j}A_{ij}^2}$ |
| QR (from G–S) | $A = QR$, $Q^TQ = I$, $R$ upper triangular |
