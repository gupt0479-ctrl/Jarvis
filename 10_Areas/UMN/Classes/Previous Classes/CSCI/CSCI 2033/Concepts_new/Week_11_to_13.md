---
type: concept
status: complete
created: 2025-11-25
updated: 2025-12-04
week: "11-13"
chapters: "Ch. 12, 13, 14 + SVD"
tags:
  - "#Textbook"
  - "#Lecture"
  - "#Jupyter"
  - "#Quiz"
  - "#Homework"
  - "#ML"
prev: [[Week_10]]
---

# Weeks 11–13 — Least Squares, Classifiers, Gradient Descent, SVD
### Ch. 12: Least Squares | Ch. 13: Feature Engineering | Ch. 14: Classifiers | SVD

---

## Week 11 — Least Squares and Feature Engineering (Ch. 12 & 13)

### The Least Squares Problem

Given tall (over-determined) $Ax \approx b$ ($m > n$), minimize:
$$\min_x \|Ax - b\|^2$$

Solution: $\hat{x} = A^\dagger b = R^{-1}Q^T b$ (via QR).

The **residual** $r = b - A\hat{x}$ measures fit quality. $\|r\| > 0$ is expected for noisy data.

**Normal equations** (alternative derivation from setting $\nabla J = 0$):
$$A^T A\, x = A^T b \qquad \Rightarrow \qquad \hat{x} = (A^TA)^{-1}A^Tb$$

QR is numerically preferred — forming $A^TA$ squares the condition number.

```python
# Normal equations approach (less stable)
AtA  = A.T @ A
Atb  = A.T @ b
x_hat = np.linalg.solve(AtA, Atb)

# QR approach (preferred)
c = QRSolve(V, y)
```

### Fitting $\sin(x)$ — A Concrete Example

5 points from the unit circle, fit a cubic polynomial $\hat{p}(x) = c_0 + c_1 x + c_2 x^2 + c_3 x^3$:

$$V = \begin{bmatrix}1 & x_1 & x_1^2 & x_1^3\\ \vdots & \vdots & \vdots & \vdots\\ 1 & x_5 & x_5^2 & x_5^3\end{bmatrix} \quad \vec{y} = \begin{bmatrix}\sin(x_1)\\ \vdots\\ \sin(x_5)\end{bmatrix}$$

Solve $V\vec{c} \approx \vec{y}$ with QRSolve. Adding noise to $\vec{y}$ tests robustness — least squares absorbs it gracefully.

Taylor polynomial reference: $\sin(x) \approx x - x^3/6 + x^5/120$, so coefficients are $[0, 1, 0, -1/6, 0, 1/120]$.

### Feature Engineering (Ch. 13)

The key insight: even when the model is **nonlinear in the raw input**, it can be **linear in engineered features**. This keeps least squares applicable.

| Raw input $t$ | Engineered feature vector $\vec{x}(t)$ | Model type |
|---|---|---|
| Scalar $t$ | $[1, t, t^2, \ldots, t^{n-1}]$ | Polynomial |
| Scalar $t$ | $[1, \sin(t), \cos(t), \ldots]$ | Trigonometric |
| Vector $x$ | $[x_1, x_2, x_1x_2, x_1^2, x_2^2]$ | Quadratic |
| Vector $x$ | $\text{ReLU}(Rx)$ (random projection) | Random features |

The Vandermonde matrix $V$ IS the feature matrix for polynomial regression.

### Overfitting vs. Underfitting

- **Underfitting** (low $n$): model too simple → high training AND test error
- **Overfitting** (high $n$): model fits training data perfectly → low training error, high test error
- **Good fit**: both training and test errors small

Lab 9 finding: best polynomial degree for that dataset was $n = 9$ (minimized test error). For $n < 9$: underfitting. For $n > 9$: overfitting.

---

## Week 12 — Least Squares Classifiers and Gradient Descent (Ch. 14)

### Binary Classifier (Lab 10)

For two classes ($+1$ and $-1$), fit a linear model:
$$\hat{f}(x) = x^T\beta + v$$

Predict $+1$ if $\hat{f}(x) > 0$, predict $-1$ if $\hat{f}(x) \le 0$. Decision boundary: $\{x \mid x^T\beta + v = 0\}$.

**Setting up the regression**: label training data as $y_i \in \{+1, -1\}$. For "0 vs not-0":
```python
y_binary = [+1 if label == '0' else -1 for label in y_train]
```

**Dimension reduction** (Lab 10, Task 1): remove pixel features that appear in fewer than 10 training images:
```python
Idx = [i for i in range(n_pixels) if Counts[i] >= 10]  # active pixels only
```

**Augment with bias**: add a column of ones to the feature matrix so the solver finds the offset too.

### Multi-Class: One-vs-All (Lab 11)

Train $K$ binary classifiers (one per digit). Classifier $k$ outputs $+1$ for class $k$ and $-1$ for all others. At test time:
$$\hat{y} = \arg\max_k \hat{f}_k(x)$$

**Matrix formulation**: weight matrix $W$ of shape $(d \times K)$. One gradient descent run optimizes all classifiers simultaneously:

$$\ell(W) = \frac{1}{2}\|XW - Y\|_F^2 \qquad \nabla\ell(W) = X^T(XW - Y)$$

### Feature Engineering for Classification (Lab 10)

Random features (page 273/293): build $K \times n$ random matrix $R$, compute $\text{ReLU}(Rx)$ or $|Rx|$ as engineered features. Append a bias column of $1$s. These nonlinear features make the classifier more expressive without changing the linear framework.

### Receiver Operating Characteristics (ROC)

A binary classifier with threshold $\alpha$: predict $+1$ if $\hat{f}(x) > \alpha$, else $-1$.

- $\alpha < 0$ → fewer false positives (stricter about predicting positive)
- $\alpha > 0$ → fewer false negatives (more permissive)

The ROC curve traces accuracy vs. false-positive rate as $\alpha$ varies. Use it to tune the trade-off based on what matters more in your application.

### Gradient Descent (Lab 11)

When the closed-form solution is impractical (large data, non-quadratic losses), use iterative optimization.

**Update rule**: step in the negative gradient direction:
$$\theta^{(k+1)} = \theta^{(k)} - t\,\nabla\ell(\theta^{(k)})$$

- $t$ = step size / learning rate
- For least squares: $\nabla\ell(w) = X^T(Xw - y)$

**Loss function** (Lab 11 formulation):
$$\ell(w) = \frac{1}{2}\|Xw - y\|_2^2 \qquad \nabla\ell(w) = X^T(Xw - y)$$

**Stopping criterion** — relative change in loss:
$$\frac{|f_{k+1} - f_k|}{|f_k|} < \varepsilon$$

**Step size guidance**: $t < 1/\|A\|^2$ (spectral norm). Too large → diverge. Too small → very slow.

```python
def gradient_descent(x0, landdl, t, eps, max_iter=1000):
    x = x0
    f_prev = None
    for k in range(max_iter):
        f, g = landdl(x)            # loss and gradient
        x    = x - t * g            # update
        if f_prev and abs(f - f_prev) / abs(f_prev) < eps:
            break
        f_prev = f
    return x
```

**Convergence rate**: depends on condition number of $X^TX$. Poor conditioning → slow zigzag convergence.

---

## Week 13 — SVD and Eigenfaces (Lab 12)

### Singular Value Decomposition

Every $m \times n$ matrix (any shape, any rank) has an SVD:
$$A = U\Sigma V^T$$

| Factor | Size | Properties |
|---|---|---|
| $U$ | $m \times m$ | Orthogonal: $U^TU = I$; columns = left singular vectors |
| $\Sigma$ | $m \times n$ | Diagonal: $\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_r > 0$ (singular values) |
| $V$ | $n \times n$ | Orthogonal: $V^TV = I$; columns = right singular vectors |

$r = \text{rank}(A)$ = number of nonzero singular values.

**Rank-1 sum** (outer product form):
$$A = \sum_{k=1}^r \sigma_k\,u_k v_k^T$$

### Low-Rank Approximation

Keep only the top $\ell$ terms:
$$\hat{A}_\ell = \sum_{k=1}^\ell \sigma_k\,u_k v_k^T$$

This is the **best rank-$\ell$ approximation** in Frobenius norm (Eckart–Young theorem):
$$\|A - \hat{A}_\ell\| = \sigma_{\ell+1}$$

If singular values decay fast, a few terms capture most of the "energy."

### Eigenfaces Algorithm (Lab 12)

**Setup**: $N$ face images, each a vector in $\mathbb{R}^{4096}$ (64×64). Stack as data matrix $X$ ($4096 \times N$).

**Step 1 — De-mean**:
$$\tilde{X} = X - \frac{1}{N}X\mathbf{1}\mathbf{1}^T$$

Remove the "average face" from every column. This centers the data.

**Step 2 — SVD**: $\tilde{X} = U\Sigma V^T$ via `np.linalg.svd`.

**Step 3 — Extract top $k = 20$ components**:
$$\hat{B} = U[:, 0:k] \qquad \hat{W} = \hat{\Sigma}\hat{V}^T$$

$\hat{B}$ = eigenfaces (principal directions of variation). $\hat{W}$ = compressed representation of all training images.

**Step 4 — Predict (nearest neighbor in eigenspace)**:
1. De-mean test vector: $\bar{z} = z - \text{mean}$
2. Project: $\vec{w} = \hat{B}^T\bar{z}$ (since $\hat{B}^T\hat{B} = I_k$, no solve needed)
3. Find nearest column of $\hat{W}$: $\hat{i} = \arg\min_i \|\vec{w} - \hat{W}_{:,i}\|$
4. Predict: training image $\hat{i}$

```python
# Step 2: SVD
np_U, sigma, np_Vt = np.linalg.svd(np_A)
k = len(sigma)
U   = Matrix(np_U[:, :k])
V_T = Matrix(np_Vt[:k, :])

# Step 3: B_hat and W_hat
B_hat = U[:, 0:k_top]          # top k eigenfaces
W_hat = diag(sigma[:k_top]) @ V_T[:k_top, :]   # representations

# Step 4: predict
z_bar    = z - mean_vector
w        = B_hat.transpose() @ z_bar
distances = [vec_dist(w, W_hat[:, i]) for i in range(N_train)]
prediction = sorted_indices[0]   # nearest neighbor
```

---

## ML Connection (All Three Weeks)

| This course concept | ML equivalent |
|---|---|
| Least squares regression | Linear regression, ridge regression |
| Least squares classifier | Linear SVM (unconstrained form), logistic regression (approximation) |
| Feature engineering | Feature maps, kernel methods, neural network hidden layers |
| Random features $\text{ReLU}(Rx)$ | Random kitchen sinks, extreme learning machines |
| Gradient descent | Backbone of all deep learning optimization |
| SVD low-rank approx. | PCA, matrix factorization (collaborative filtering), autoencoders |
| Eigenfaces | PCA-based face recognition; same math as PCA |
| ROC curve | Standard evaluation for binary classifiers |

---

## Summary

| Concept | Formula |
|---|---|
| Least squares solution | $\hat{x} = A^\dagger b = R^{-1}Q^Tb$ |
| Normal equations | $A^TAx = A^Tb$ |
| GD update rule | $\theta^{(k+1)} = \theta^{(k)} - t\,\nabla\ell(\theta^{(k)})$ |
| GD gradient (LS) | $\nabla\ell(w) = X^T(Xw - y)$ |
| Relative prediction error | $\text{RMS residual}/\text{RMS}_y$ |
| SVD | $A = U\Sigma V^T$ |
| Best rank-$\ell$ approx. | $\hat{A}_\ell = \sum_{k=1}^\ell \sigma_k u_k v_k^T$ |
| Eigenface projection | $w = \hat{B}^T \bar{z}$ |
| One-vs-all prediction | $\hat{y} = \arg\max_k \hat{f}_k(x)$ |
