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
## 1. The Least Squares Problem
Given a **tall** (over-determined) system $Ax \approx b$ with $m > n$ (more equations than unknowns), an exact solution generally does not exist. Instead, we look for $\hat{x}$ that minimizes the **sum of squared residuals**:
$$\min_x \|Ax - b\|^2$$

The solution is the **least squares solution** $\hat{x} = A^\dagger b = R^{-1} Q^T b$ (via QR factorization).

The **residual vector** is $r = b - A\hat{x}$. Its norm $\|r\|$ measures the fit quality. For perfect fit, $\|r\| = 0$; for a noisy or overdetermined system, $\|r\| > 0$.

---

## 2. Setup — Least Squares for Polynomial Fitting

The canonical setup: approximate a function $y = f(x)$ using a polynomial of degree $n-1$:
$$p(x) = c_0 + c_1 x + \cdots + c_{n-1} x^{n-1}$$

Given $m > n$ data points $(x_1, y_1), \ldots, (x_m, y_m)$, we want the coefficients $\vec{c}$ that minimize:
$$\sum_{i=1}^m (p(x_i) - y_i)^2$$

Stack all evaluations into the **Vandermonde matrix** $V$ and vector $\vec{y}$:
$$V \vec{c} \approx \vec{y} \qquad (\text{tall system, } m > n)$$

Then $\hat{c} = V^\dagger \vec{y} = R^{-1} Q^T \vec{y}$ (via QRSolve).

---

## 3. Normal Equations

An alternative to QR: the least squares problem $\min\|Ax - b\|^2$ is solved by the **normal equations**:
$$A^T A\, x = A^T b$$

Solution: $\hat{x} = (A^T A)^{-1} A^T b$ (assuming linearly independent columns of $A$).

```python
AtA  = A.T @ A
Atb  = A.T @ b
x_hat = np.linalg.solve(AtA, Atb)
```

Numerically, **QR is preferred** because forming $A^T A$ squares the condition number. For large or ill-conditioned problems, the normal equation approach can lose accuracy.

---

## 4. Example — Approximating $\sin(x)$

Fit a cubic polynomial to 5 points on the unit circle: $x_1 = -\pi/2,\; x_2 = -\pi/4,\; x_3 = 0,\; x_4 = \pi/4,\; x_5 = \pi/2$.

Build the $5 \times 4$ Vandermonde matrix:
$$V = \begin{bmatrix} 1 & x_1 & x_1^2 & x_1^3 \\ 1 & x_2 & x_2^2 & x_2^3 \\ \vdots & \vdots & \vdots & \vdots \\ 1 & x_5 & x_5^2 & x_5^3 \end{bmatrix}, \qquad \vec{y} = \begin{bmatrix}\sin(x_1)\\ \vdots \\ \sin(x_5)\end{bmatrix}$$

Then $\hat{c} = V^\dagger \vec{y}$. The resulting polynomial approximates $\sin(x)$ on $[-\pi/2, \pi/2]$.

For reference, the Taylor polynomial for $\sin(x)$ has coefficients $[0, 1, 0, -1/6, 0, 1/120]$.

**What happens when we add noise?** Perturbing the $\vec{y}$ values by small random errors moves the fitted polynomial slightly but the least squares minimization absorbs most of the error gracefully. More data points help.

---

## 5. Evaluating a Polynomial

```python
def f(c, x):
    """evaluate polynomial with coefficient vector c at point x"""
    out = c[0][0]        # constant term c_0
    exp = x              # tracks x^i
    for i in range(1, len(c.data)):
        out += c[i][0] * exp
        exp *= x         # x^{i+1}
    return out
```

---

## 6. RMS Error and Relative Prediction Error

After fitting $\hat{c}$, measure quality with:

**RMS residual** (fits how well):
$$\text{RMS error} = \sqrt{\frac{1}{m}\sum_{i=1}^m (\hat{p}(x_i) - y_i)^2}$$

**RMS of target values** (scale of the signal):
$$\text{RMS}_y = \sqrt{\frac{1}{m}\sum_{i=1}^m y_i^2}$$

**Relative prediction error**:
$$\text{Rel. error} = \frac{\text{RMS error}}{\text{RMS}_y}$$

Interpretation:
- $\approx 1$ → model is no better than guessing zero → terrible.
- $\ll 1$ → model explains the data well → good fit.

These are computed on both **training data** (fit quality) and **test data** (generalization).

---

## 7. Feature Engineering (Chapter 13)

**Feature engineering** is the idea that the regression model $\hat{y} = \vec{x}^T \beta + v$ doesn't require $\vec{x}$ to be the raw inputs. We can choose engineered features that make the model more expressive.

**Key insight**: even though the model is nonlinear in the original input, it remains **linear in the parameters** $\beta$. This means we can still solve it with least squares.

### Examples of engineered features

| Raw input $t$ | Engineered feature vector $\vec{x}(t)$ |
|---|---|
| Scalar $t$ | $[1, t, t^2, \ldots, t^{n-1}]$ (polynomial) |
| Scalar $t$ | $[1, \sin(t), \cos(t)]$ (trigonometric) |
| Vector $x$ | $[x_1, x_2, x_1 x_2, x_1^2, x_2^2]$ (quadratic) |

### Continuing the $\sin(x)$ example
Using 9 training points and degree-3 fit via `QRSolve`:

```python
c = QRSolve(V, y)   # V is 9×4 Vandermonde, y is 9-vector of sin values
```

The coefficients $\vec{c}$ that come out are the **learned parameters**. Evaluating the polynomial at new points gives predictions.

The feature matrix $V$ is the core connection — it transforms the nonlinear regression problem (fit a sine curve) into a **linear** least squares problem (find $\vec{c}$ minimizing $\|V\vec{c} - \vec{y}\|^2$).

---

## 8. Overfitting vs. Underfitting

- **Too few features / low degree**: the model is too simple (underfitting) and cannot capture the pattern → high training and test error.
- **Too many features / high degree**: the model fits the training data very closely (small training error) but performs poorly on new data (overfitting) → high test error.
- **Good fit**: training and test errors are both small.

This is why you split data into **training** and **test** sets and track both errors. The relative prediction error on the test set is the real measure of model quality.

---

## Summary of key formulas

| Concept | Formula |
|---|---|
| Least squares problem | $\min_x \|Ax - b\|^2$ |
| Solution via pseudo-inverse | $\hat{x} = A^\dagger b = R^{-1}Q^T b$ |
| Normal equations | $A^TAx = A^Tb$ |
| Vandermonde system | $V\vec{c} \approx \vec{y}$ (tall, $m > n$) |
| Polynomial evaluation | $p(\alpha) = \vec{c}^{\,T}[1,\alpha,\alpha^2,\ldots]$ |
| RMS residual | $\sqrt{\frac{1}{m}\sum (p(x_i)-y_i)^2}$ |
| Relative error | $\text{RMS error} / \text{RMS}_y$ |
