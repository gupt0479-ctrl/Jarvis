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
## 1. Left and Right Inverses

Matrix division doesn't exist in the usual sense — instead, we have left and right inverses depending on the shape of $A$.

### Left inverse
A matrix $C$ is a **left inverse** of $A$ if $CA = I$.

- Requires $A$ to be **tall or square** ($m \ge n$) with **linearly independent columns**.
- For an over-determined system $Ax = b$ (tall $A$): if $A(Cb) = b$, then $x = Cb$ is the unique solution; if not, no solution exists.

### Right inverse
A matrix $B$ is a **right inverse** of $A$ if $AB = I$.

- Requires $A$ to be **wide or square** ($m \le n$) with **linearly independent rows**.
- For an under-determined system $Ax = b$ (wide $A$): $x = Bb$ is always a solution.

| Problem type | Matrix shape | Method | Result |
|---|---|---|---|
| Over-determined $Ax = b$ | Tall ($m > n$) | Left inverse $C$: $x = Cb$ | Unique solution if $A(Cb)=b$ |
| Under-determined $Ax = b$ | Wide ($m < n$) | Right inverse $B$: $x = Bb$ | One solution (not unique) |

---

## 2. The Inverse $A^{-1}$

When $A$ is **square** and both left- and right-invertible, its unique **inverse** satisfies:
$$A A^{-1} = A^{-1} A = I$$

A square matrix is invertible $\iff$ its columns are linearly independent $\iff$ its rows are linearly independent.

For an invertible square $A$, the system $Ax = b$ has the **unique solution** $x = A^{-1} b$.

**Important formulas**:

| Property | Formula |
|---|---|
| Transpose inverse | $(A^T)^{-1} = (A^{-1})^T$ |
| Product inverse | $(AB)^{-1} = B^{-1} A^{-1}$ |
| Orthogonal matrix | $A^{-1} = A^T$ (when columns are orthonormal) |

---

## 3. Solving Square Systems: Back Substitution and QR

### Back substitution
When the coefficient matrix $R$ is **upper triangular**, the system $Rx = b$ is solved cheaply starting from the last equation:

- Solve $x_n = b_n / R_{nn}$.
- Substitute into the $n-1$ equation to find $x_{n-1}$, and continue upward.

Cost: $n^2$ flops.

```python
def BackSub(R, b):
    x = [0.0 for i in range(R.n)]
    for k in range(R.n - 1, -1, -1):      # backward loop
        out = b[k][0]
        for j in range(k + 1, R.n):
            out -= R[k][j] * x[j]
        x[k] = out / R[k][k]
    return Matrix([x]).transpose()
```

### QR-based solve (Algorithm 11.2)
For a square invertible $A$:
1. **Factor**: compute $A = QR$ (cost $\approx 2n^3$ flops).
2. **Compute** $y = Q^T b$ (cost $2n^2$ flops).
3. **Back-substitute**: solve $Rx = y$ (cost $n^2$ flops).

Result: $x = R^{-1} Q^T b$. Total cost is dominated by step 1: $\approx 2n^3$ flops.

```python
def QRSolve(A, b):
    V, R = HouseHolderQR(A)       # A = QR
    Qtb  = Qstarb(V, b)           # y = Q^T b
    xt   = BackSub(R, Qtb)        # solve Rx = y
    return xt
```

**Multiple right-hand sides** $AX = B$: factor $A = QR$ **once**, then solve for each column of $B$ separately. Total cost: $2n^3 + 3kn^2$ for $k$ systems.

---

## 4. The Pseudo-Inverse $A^\dagger$

The pseudo-inverse generalizes the inverse to non-square matrices. It exists whenever the relevant columns or rows are linearly independent.

| Case | Condition | Formula | Property |
|---|---|---|---|
| Tall ($m \ge n$) | Columns of $A$ are LI $\Rightarrow$ $A^T A$ invertible | $A^\dagger = (A^T A)^{-1} A^T$ | Left inverse: $A^\dagger A = I$ |
| Wide ($m \le n$) | Rows of $A$ are LI $\Rightarrow$ $A A^T$ invertible | $A^\dagger = A^T (A A^T)^{-1}$ | Right inverse: $A A^\dagger = I$ |

**Via QR (for tall $A$)**: $A^\dagger = R^{-1} Q^T$ (from $A = QR$). Cost: $\approx 3mn^2$ flops.

### Applications
- **Least squares** (tall $A$, over-determined): the solution minimizing $\|Ax - b\|^2$ is $x = A^\dagger b$.
- **Under-determined** (wide $A$): $x = A^\dagger b$ is the **least-norm** solution.

---

## 5. Polynomial Interpolation

A degree $n-1$ polynomial is fully described by its coefficient vector $\vec{c}$:
$$p(x) = c_0 + c_1 x + c_2 x^2 + \cdots + c_{n-1} x^{n-1}$$

Evaluating at a single point $\alpha$ is just a **dot product**:
$$p(\alpha) = \vec{c}^{\,T} \underbrace{[1,\, \alpha,\, \alpha^2,\, \ldots,\, \alpha^{n-1}]^T}_{\vec{x}_\alpha}$$

### Vandermonde matrix
If we have $m$ sample points $\alpha_1, \ldots, \alpha_m$ and corresponding values $y_1, \ldots, y_m$, stacking the evaluation equations gives the linear system $V\vec{c} = \vec{y}$:

$$V = \begin{bmatrix} 1 & \alpha_1 & \alpha_1^2 & \cdots & \alpha_1^{n-1} \\ 1 & \alpha_2 & \alpha_2^2 & \cdots & \alpha_2^{n-1} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & \alpha_m & \alpha_m^2 & \cdots & \alpha_m^{n-1} \end{bmatrix}$$

Each row of $V$ is the evaluation vector $\vec{x}_{\alpha_i}$.

| Situation | System | Solution method |
|---|---|---|
| $m = n$ distinct points | $V$ is square, usually invertible | $\vec{c} = V^{-1}\vec{y}$ |
| $m > n$ (more data than coefficients) | $V$ is tall (over-determined) | Least squares: $\vec{c} = V^\dagger \vec{y} = R^{-1}Q^T\vec{y}$ |

**Building the Vandermonde matrix** — each row is $[1, x_i, x_i^2, \ldots]$, built recursively:
```python
A_data[i][0] = 1.0
for j in range(1, n):
    A_data[i][j] = A_data[i][j-1] * x_i   # multiply by x_i each time
```

---

## 6. Error and Relative Prediction Error

After fitting polynomial coefficients $\vec{c}$ to data, two error measures matter:

**RMS residual error**:
$$\text{RMS error} = \sqrt{\frac{1}{m}\sum_{i=1}^m (p(\alpha_i) - y_i)^2}$$

**RMS of output values** (the "signal"):
$$\text{RMS}_y = \sqrt{\frac{1}{m}\sum_{i=1}^m y_i^2}$$

**Relative prediction error**:
$$\text{Rel. error} = \frac{\text{RMS error}}{\text{RMS}_y}$$

- Relative error $\approx 1$: the model error is as large as the signal → bad fit.
- Relative error $\ll 1$: the model describes the data well → good fit.

---

## 7. Normal Equations

An alternative to QR for the least-squares problem $\min\|Ax - b\|^2$ is to solve the **normal equations**:
$$A^T A x = A^T b$$

The solution is $x = (A^T A)^{-1} A^T b = A^\dagger b$ (when columns of $A$ are LI).

In code (using NumPy):
```python
AtA = A.T @ A           # n×n
Atb = A.T @ b           # n-vector
x   = np.linalg.solve(AtA, Atb)
```

The QR-based approach is numerically preferred because forming $A^T A$ can lose information (it squares the condition number).

---

## Summary of key formulas

| Concept | Formula |
|---|---|
| Left inverse | $CA = I$ (tall $A$, LI columns) |
| Right inverse | $AB = I$ (wide $A$, LI rows) |
| Square inverse | $AA^{-1} = A^{-1}A = I$ |
| Product inverse | $(AB)^{-1} = B^{-1}A^{-1}$ |
| Pseudo-inverse (tall) | $A^\dagger = (A^TA)^{-1}A^T = R^{-1}Q^T$ |
| Pseudo-inverse (wide) | $A^\dagger = A^T(AA^T)^{-1}$ |
| Least-squares solution | $x = A^\dagger b = R^{-1}Q^T b$ |
| Vandermonde system | $V\vec{c} = \vec{y}$ |
| Normal equations | $A^TAx = A^Tb$ |
| Back-substitution cost | $n^2$ flops |
| QR solve cost | $\approx 2n^3$ flops |
