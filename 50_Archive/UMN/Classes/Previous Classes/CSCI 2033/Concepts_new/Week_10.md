---
type: concept
status: archived
created: 2025-11-21
updated: 2025-11-22
week: "10"
chapters: "Ch. 11"
tags:
  - "#Textbook"
  - "#Lecture"
  - "#Jupyter"
  - "#Quiz"
  - "#Homework"
  - "#LinearAlgebra"
prev: [[Week_8_and_9]]
next: [[Week_11]]
---

# Week 10 — Linear System Solvers and Polynomial Interpolation
### Ch. 11: Linear and Affine Functions of Vectors (Inverses and Solvers)

---

## 1. Left and Right Inverses

Matrix "division" splits into two cases because multiplication is not commutative.

**Left inverse $C$**: $CA = I$. Requires $A$ **tall or square** ($m \ge n$) with **LI columns**.
- Solving over-determined $Ax = b$ (tall $A$): if $A(Cb) = b$ then $x = Cb$ is unique; otherwise no solution.

**Right inverse $B$**: $AB = I$. Requires $A$ **wide or square** ($m \le n$) with **LI rows**.
- Solving under-determined $Ax = b$ (wide $A$): $x = Bb$ is always a solution (not unique).

| Problem | Shape | Method | Result |
|---|---|---|---|
| Over-determined | Tall ($m > n$) | Left inverse: $x = Cb$ | Unique if $A(Cb)=b$ |
| Under-determined | Wide ($m < n$) | Right inverse: $x = Bb$ | One solution |
| Square | $m = n$ | Inverse: $x = A^{-1}b$ | Unique |

---

## 2. The Inverse $A^{-1}$

When $A$ is **square** and both left- and right-invertible:
$$AA^{-1} = A^{-1}A = I$$

Invertible $\iff$ columns are LI $\iff$ rows are LI.

| Property | Formula |
|---|---|
| Transpose inverse | $(A^T)^{-1} = (A^{-1})^T$ |
| Product inverse | $(AB)^{-1} = B^{-1}A^{-1}$ |
| Orthogonal matrix | $A^{-1} = A^T$ |

---

## 3. Back Substitution (Algorithm 11.1)

For **upper triangular** $R$, solve $Rx = b$ starting from the last equation:

$$x_n = b_n / R_{nn}, \quad x_k = \frac{b_k - \sum_{j=k+1}^n R_{kj}x_j}{R_{kk}}$$

Cost: $n^2$ flops.

```python
def BackSub(R, b):
    x = [0.0 for i in range(R.n)]
    for k in range(R.n - 1, -1, -1):    # backward loop
        out = b[k][0]
        for j in range(k + 1, R.n):
            out -= R[k][j] * x[j]       # substitute known values
        x[k] = out / R[k][k]            # solve for x_k
    return Matrix([x]).transpose()
```

---

## 4. QR-Based Linear System Solver (Algorithm 11.2 — Lab 8)

For square invertible $A$:
1. **Factor**: $A = QR$ via Householder (cost $\approx 2n^3$ flops)
2. **Apply $Q^T$**: compute $y = Q^T b$ using `Qstarb`
3. **Back-substitute**: solve $Rx = y$

Result: $x = R^{-1}Q^T b$.

```python
def QRSolve(A, b):
    V, R = HouseHolderQR(A)     # A = QR
    Qtb  = Qstarb(V, b)         # y = Q^T b
    xt   = BackSub(R, Qtb)      # solve Rx = y
    return xt
```

**Multiple RHS $AX = B$**: factor $A = QR$ once, then solve for each column of $B$ separately. Total cost $2n^3 + 3kn^2$ for $k$ systems.

---

## 5. Pseudo-Inverse $A^\dagger$

Generalizes the inverse to non-square matrices.

| Case | Condition | Formula | Role |
|---|---|---|---|
| Tall ($m \ge n$) | LI columns → $A^TA$ invertible | $A^\dagger = (A^TA)^{-1}A^T = R^{-1}Q^T$ | Left inverse |
| Wide ($m \le n$) | LI rows → $AA^T$ invertible | $A^\dagger = A^T(AA^T)^{-1}$ | Right inverse |

- Least squares (tall $A$): $\hat{x} = A^\dagger b$ minimizes $\|Ax - b\|^2$.
- Under-determined (wide $A$): $x = A^\dagger b$ is the **least-norm** solution.

---

## 6. Polynomial Interpolation (Lab 8)

Degree $n-1$ polynomial: $p(x) = c_0 + c_1 x + \cdots + c_{n-1}x^{n-1}$

Evaluating at $\alpha$ is a **dot product**:
$$p(\alpha) = \vec{c}^{\,T}\underbrace{[1,\,\alpha,\,\alpha^2,\,\ldots,\,\alpha^{n-1}]^T}_{\text{evaluation vector}}$$

### Vandermonde matrix
Stack evaluation vectors for $m$ data points:

$$V = \begin{bmatrix} 1 & x_1 & x_1^2 & \cdots & x_1^{n-1} \\ 1 & x_2 & x_2^2 & \cdots & x_2^{n-1} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_m & x_m^2 & \cdots & x_m^{n-1} \end{bmatrix}$$

System: $V\vec{c} = \vec{y}$ (or $\approx \vec{y}$ if $m > n$).

```python
# Build Vandermonde matrix recursively
for i in range(m):
    x_i, y_i = data[i]
    A_data[i][0] = 1.0
    for j in range(1, n):
        A_data[i][j] = A_data[i][j-1] * x_i    # x_i^j = x_i^{j-1} * x_i
    b_vals[i] = y_i

# Solve: coefficients = QRSolve(A, b)
c = QRSolve(Matrix(A_data), Vector(b_vals))
```

**Evaluate polynomial at point $x$**:
```python
def f(c, x):
    out = c[0][0]
    exp = x
    for i in range(1, len(c.data)):
        out += c[i][0] * exp
        exp *= x
    return out
```

---

## 7. Error Metrics (Lab 9)

**RMS residual**:
$$\text{RMS error} = \sqrt{\frac{1}{m}\sum_{i=1}^m (\hat{y}_i - y_i)^2}$$

**RMS of target values** (signal scale):
$$\text{RMS}_y = \sqrt{\frac{1}{m}\sum_{i=1}^m y_i^2}$$

**Relative prediction error**:
$$\text{Rel. error} = \frac{\text{RMS error}}{\text{RMS}_y}$$

- $\approx 1$ → model no better than zero → bad
- $\ll 1$ → model explains data well → good

Train/test split: parameter $n$ that minimizes test error is the right choice (Lab 9 answer: $n = 9$ for that dataset).

---

## Summary

| Concept | Formula |
|---|---|
| Left inverse | $CA = I$ (tall $A$, LI columns) |
| Right inverse | $AB = I$ (wide $A$, LI rows) |
| Square inverse | $(AB)^{-1} = B^{-1}A^{-1}$ |
| Pseudo-inverse (tall) | $A^\dagger = R^{-1}Q^T$ |
| Least-squares solution | $\hat{x} = A^\dagger b$ |
| Normal equations | $A^TAx = A^Tb$ |
| Back-sub cost | $n^2$ flops |
| QR solve cost | $\approx 2n^3$ flops |
