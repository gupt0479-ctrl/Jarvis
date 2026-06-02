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
## 1. Least Squares Classifier (Chapter 14)

A **classifier** predicts which of $K$ classes an input $x$ belongs to. The least squares approach turns this into a regression problem.

### Binary classifier
For two classes (+1 and −1), fit a linear model:
$$\hat{f}(x) = x^T \beta + v$$

Predict class $+1$ if $\hat{f}(x) > 0$, and class $-1$ if $\hat{f}(x) \le 0$. The **decision boundary** is the hyperplane $\{x \mid x^T \beta + v = 0\}$.

### Multi-class: one-vs-others
For $K$ classes, train $K$ separate binary classifiers. Classifier $k$ is trained to output $+1$ for class $k$ and $-1$ for all others. At test time, assign $x$ to the class with the **highest** $\hat{f}_k(x)$.

### Setting up the regression
Collect $N$ training examples $(x_1, y_1), \ldots, (x_N, y_N)$ where $y_i \in \{+1, -1\}$. Build the **feature matrix** $X$ (size $n \times N$) whose columns are the training vectors, and the label vector $\vec{y}$.

We want $\beta$ and $v$ minimizing:
$$\|X^T \beta + v\mathbf{1} - \vec{y}\|^2$$

Augment: let $\tilde{x}_i = [1, x_i]^T$ and $\tilde{\beta} = [v, \beta]^T$. Then the stacked system is $\tilde{X}^T \tilde{\beta} \approx \vec{y}$, solved with QR least squares.

### Section 14.2.2 — Sign of the regression determines the classification
The key formula from the lecture: the sign of $\hat{f}(x) = x^T \beta + v$ directly determines the predicted class. If $\hat{f}(x) > 0$, predict positive; if $\hat{f}(x) < 0$, predict negative.

---

## 2. Optimization — Setting the Stage

The least squares problem is a special case of a broader **optimization problem**:
$$\text{minimize} \quad J(\theta) \quad \text{over} \quad \theta \in \mathbb{R}^n$$

$J$ is the **objective function** (or cost function / loss function). For least squares, $J(\theta) = \|A\theta - b\|^2$.

A point $\theta^\star$ is a **minimizer** if $J(\theta^\star) \le J(\theta)$ for all $\theta$.

For differentiable $J$, the **necessary condition** for a minimum is that the gradient vanishes:
$$\nabla J(\theta^\star) = \mathbf{0}$$

For the least squares objective $J(\theta) = \|A\theta - b\|^2$:
$$\nabla J(\theta) = 2A^T(A\theta - b) = 2A^T r$$

where $r = A\theta - b$ is the residual. Setting $\nabla J = \mathbf{0}$ gives the **normal equations**: $A^T A\theta = A^T b$.

---

## 3. Gradient Descent

When the closed-form solution is unavailable or impractical (e.g., the matrix is too large to factor, or $J$ is not a simple quadratic), we use **gradient descent** — an iterative optimization algorithm.

**Core idea**: repeatedly take small steps in the direction of the negative gradient (steepest descent):
$$\theta^{(k+1)} = \theta^{(k)} - \alpha\, \nabla J(\theta^{(k)})$$

- $\alpha > 0$ is the **step size** (or **learning rate**).
- $\nabla J(\theta^{(k)})$ points in the direction of steepest increase of $J$.
- Subtracting it moves us toward the minimum.

### Algorithm
1. Initialize $\theta^{(0)}$ (e.g., all zeros or random).
2. For $k = 0, 1, 2, \ldots$:
   - Compute gradient $g = \nabla J(\theta^{(k)})$.
   - Update: $\theta^{(k+1)} = \theta^{(k)} - \alpha\, g$.
3. Stop when $\|g\|$ is sufficiently small or after a fixed number of iterations.

### For the least squares objective
Since $\nabla J(\theta) = 2A^T(A\theta - b)$, the update is:
$$\theta^{(k+1)} = \theta^{(k)} - 2\alpha\, A^T(A\theta^{(k)} - b)$$

### Choosing the step size $\alpha$
- Too large: the iteration may **diverge** (oscillate or blow up).
- Too small: convergence is very slow.
- A common rule of thumb: $\alpha < 1/\|A\|^2$ (where $\|A\|$ is the spectral norm).

### Convergence
Gradient descent converges for convex $J$ with a Lipschitz-continuous gradient, given a sufficiently small step size. The convergence rate depends on the condition number of $A^T A$ — the worse the conditioning, the slower the convergence.

### Stochastic gradient descent (SGD)
For large datasets, computing the full gradient $\nabla J$ is expensive. SGD approximates the gradient using a **mini-batch** (random subset of training examples), making each step much cheaper at the cost of some noise.

---

## 4. 2D Gradient Descent — Geometric Picture

In 2D, $J(\theta_1, \theta_2)$ defines a surface. The gradient $\nabla J$ points uphill. Gradient descent follows the **negative gradient** — downhill — until it reaches a valley (minimum).

The contours of $J$ are level curves. The gradient is always **perpendicular** to these curves. Gradient descent paths can look like a zigzag if the level curves are very elongated (bad conditioning), which is why step size selection matters.

---

## 5. Connection to Least Squares Classifiers

For a least squares classifier, the full pipeline is:

1. **Feature matrix** $\tilde{X}$ ($n+1 \times N$, augmented with intercept column).
2. **Solve** $\min_{\tilde{\beta}} \|\tilde{X}^T \tilde{\beta} - \vec{y}\|^2$ using QRSolve or gradient descent.
3. **Classify** a new point $x$ by computing $\hat{f}(x) = \tilde{x}^T \tilde{\beta}$ and taking the sign.

Feature engineering (polynomial features, cross terms, etc.) makes the classifier more expressive without changing the linear algebra framework — just use a richer feature vector.

---

## Summary of key formulas

| Concept | Formula |
|---|---|
| Binary classifier prediction | $\hat{y} = \text{sign}(x^T\beta + v)$ |
| Regression objective | $J(\theta) = \|A\theta - b\|^2$ |
| Gradient of $J$ | $\nabla J(\theta) = 2A^T(A\theta - b)$ |
| Normal equations | $A^TA\theta = A^Tb$ |
| Gradient descent update | $\theta^{(k+1)} = \theta^{(k)} - \alpha\,\nabla J(\theta^{(k)})$ |
| GD for least squares | $\theta^{(k+1)} = \theta^{(k)} - 2\alpha\, A^T(A\theta^{(k)} - b)$ |
