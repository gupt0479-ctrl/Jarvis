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
## 1. Linear Dependence and Independence

### Linear dependence
A collection of $n$-vectors $a_1, \ldots, a_k$ is **linearly dependent** if there exist coefficients $\beta_1, \ldots, \beta_k$, **not all zero**, such that:
$$\beta_1 a_1 + \cdots + \beta_k a_k = \mathbf{0}$$

Intuitively, at least one vector in the set is redundant — it can be written as a linear combination of the others.

Automatic dependence cases: a single zero vector is dependent; any set containing the zero vector is dependent; two vectors are dependent iff one is a scalar multiple of the other.

### Linear independence
The collection is **linearly independent** if the only solution to $\beta_1 a_1 + \cdots + \beta_k a_k = \mathbf{0}$ is $\beta_1 = \cdots = \beta_k = 0$.

**Key property**: when a set is linearly independent, the coefficients expressing any vector as a combination of the set are **unique**.

**Independence-dimension inequality**: if $a_1, \ldots, a_k$ are linearly independent $n$-vectors, then $k \le n$. In other words, you cannot have more than $n$ linearly independent $n$-vectors.

---

## 2. Basis

A collection of $n$ vectors $a_1, \ldots, a_n$ is a **basis** for $\mathbb{R}^n$ if it is linearly independent.

**Expansion in a basis**: if $a_1, \ldots, a_n$ is a basis, then **any** $n$-vector $b$ can be written uniquely as:
$$b = \alpha_1 a_1 + \cdots + \alpha_n a_n$$

The **standard basis** $e_1, \ldots, e_n$ is the most familiar example, where $e_i$ has a $1$ in position $i$ and $0$ elsewhere.

---

## 3. Orthonormal Vectors

**Orthogonal**: vectors $a_1, \ldots, a_k$ are orthogonal if every distinct pair satisfies $a_i^T a_j = 0$.

**Orthonormal**: orthogonal AND every vector has unit norm ($\|a_i\| = 1$).

**Compact condition**: $a_i^T a_j = \begin{cases} 1 & i = j \\ 0 & i \ne j \end{cases}$

Orthonormal vectors are always linearly independent. If $x$ is known to be a linear combination of orthonormal vectors $a_1, \ldots, a_k$, the coefficients are simply inner products:
$$\beta_i = a_i^T x$$

**Orthonormal basis expansion**: if $a_1, \ldots, a_n$ is an orthonormal basis for $\mathbb{R}^n$:
$$x = (a_1^T x)\,a_1 + \cdots + (a_n^T x)\,a_n$$

---

## 4. Gram–Schmidt Algorithm

Given vectors $a_1, \ldots, a_k$, the Gram–Schmidt algorithm produces an orthonormal set $q_1, \ldots, q_k$ and checks for linear independence.

**For each $a_i$, repeat**:

1. **Orthogonalize**: subtract the components parallel to all previous $q_j$:
$$\tilde{q}_i = a_i - \sum_{j=1}^{i-1} (q_j^T a_i)\,q_j$$

2. **Check independence**: if $\tilde{q}_i = \mathbf{0}$, then $a_i$ is a linear combination of the previous vectors → the set is **linearly dependent** → stop.

3. **Normalize**: $q_i = \tilde{q}_i / \|\tilde{q}_i\|$.

**QR factorization connection**: the Gram–Schmidt procedure on the columns of $A$ produces $A = QR$, where $Q$ has orthonormal columns and $R$ is upper triangular.

**Complexity**: approximately $2nk^2$ flops ($n$ = vector length, $k$ = number of vectors).

---

## 5. Matrices — Definitions and Types

A **matrix** is a rectangular array of numbers of size **$m \times n$** ($m$ rows, $n$ columns). Entry in row $i$, column $j$ is $A_{ij}$.

| Type | Condition |
|---|---|
| Square | $m = n$ |
| Tall | $m > n$ |
| Wide | $n > m$ |
| Column vector | $n \times 1$ (an $n$-vector) |
| Row vector | $1 \times n$ |
| Zero matrix $\mathbf{0}$ | all entries zero |
| Identity matrix $I$ | square, $I_{ij} = 1$ if $i=j$, else $0$ |
| Diagonal matrix | $A_{ij} = 0$ for $i \ne j$; written $\text{diag}(a_1,\ldots,a_n)$ |
| Upper triangular | $A_{ij} = 0$ for $i > j$ |
| Lower triangular | $A_{ij} = 0$ for $i < j$ |
| Sparse | many zero entries; density $= \text{nnz}(A)/(mn)$ |

A triangular $n \times n$ matrix has at most $n(n+1)/2$ nonzero entries (about half).

---

## 6. Transpose, Addition, and Matrix Norm

**Transpose**: $(A^T)_{ij} = A_{ji}$. Size goes from $m \times n$ to $n \times m$. $(A^T)^T = A$. A square matrix is **symmetric** if $A = A^T$.

**Addition**: element-wise, requires same size. $(A+B)^T = A^T + B^T$.

**Scalar multiplication**: multiply every entry by scalar $\gamma$.

**Frobenius norm** (matrix norm):
$$\|A\| = \sqrt{\sum_{i=1}^m \sum_{j=1}^n A_{ij}^2}$$

Satisfies the usual norm properties. Distance between matrices: $\|A - B\|$.

---

## 7. Matrix–Vector Multiplication

If $A$ is $m \times n$ and $x$ is an $n$-vector, $y = Ax$ is an $m$-vector.

**Row interpretation**: $y_i = (\text{row } i \text{ of } A)^T x$ — the $i$-th output is the inner product of the $i$-th row and $x$.

**Column interpretation**: $y = Ax$ is a linear combination of the columns of $A$:
$$y = x_1 a_1 + x_2 a_2 + \cdots + x_n a_n$$

**Special cases**:
- $A e_j = a_j$ (unit vector selects column $j$).
- The **difference matrix** $D$ satisfies $(Dx)_i = x_{i+1} - x_i$.

**Linear independence in matrix language**: columns of $A$ are linearly independent $\iff$ $Ax = \mathbf{0} \Rightarrow x = \mathbf{0}$.

---

## 8. Complexity of Matrix Operations

| Operation | Cost |
|---|---|
| Matrix addition $A + B$ or scalar mult. $\alpha A$ ($m \times n$) | $mn$ flops |
| Matrix transpose $A^T$ | $0$ flops (only copying) |
| Matrix–vector multiply $Ax$ ($m \times n$) | $2mn$ flops |
| Matrix storage ($m \times n$, dense) | $8mn$ bytes |
| Sparse matrix storage | $\approx 16\,\text{nnz}(A)$ bytes |

---

## Summary of key formulas

| Concept | Formula / Condition |
|---|---|
| Linear dependence | $\exists \beta \ne \mathbf{0}$ s.t. $\sum \beta_i a_i = \mathbf{0}$ |
| Basis expansion | $b = \alpha_1 a_1 + \cdots + \alpha_n a_n$ (unique) |
| Orthonormal condition | $a_i^T a_j = \delta_{ij}$ |
| Gram–Schmidt coefficient | $\beta_i = a_i^T x$ |
| Matrix–vector (column view) | $Ax = x_1 a_1 + \cdots + x_n a_n$ |
| Frobenius norm | $\|A\| = \sqrt{\sum_{i,j} A_{ij}^2}$ |
| QR factorization | $A = QR$, $Q^T Q = I$, $R$ upper triangular |
