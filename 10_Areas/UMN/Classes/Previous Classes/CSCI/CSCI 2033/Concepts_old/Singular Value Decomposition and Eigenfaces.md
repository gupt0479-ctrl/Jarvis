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
## 1. Eigenvalues and Eigenvectors (Review)

For a **square** matrix $A$, a nonzero vector $v$ is an **eigenvector** with **eigenvalue** $\lambda$ if:
$$A v = \lambda v$$

The eigenvector is unchanged in direction by $A$ — it is only scaled by $\lambda$.

**Dominant eigenvector**: the eigenvector associated with the **largest eigenvalue** (in magnitude). Power iteration (repeatedly multiplying and normalizing) converges to the dominant eigenvector. This is exactly what the PageRank algorithm does with the Google matrix $G$.

---

## 2. Singular Value Decomposition (SVD)

The **SVD** generalizes the eigendecomposition to arbitrary $m \times n$ matrices (not just square). Every matrix has an SVD.

**Decomposition**:
$$A = U \Sigma V^T$$

| Factor | Size | Properties |
|---|---|---|
| $U$ | $m \times m$ | **Orthogonal**: $U^T U = UU^T = I$; columns are **left singular vectors** |
| $\Sigma$ | $m \times n$ | **Diagonal**: entries $\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_r > 0$ are the **singular values** (rest are $0$) |
| $V$ | $n \times n$ | **Orthogonal**: $V^T V = VV^T = I$; columns are **right singular vectors** |

$r = \text{rank}(A)$ is the number of nonzero singular values.

### Rank-1 sum representation
The SVD can be written as a sum of rank-1 matrices:
$$A = \sum_{k=1}^r \sigma_k\, u_k v_k^T$$

where $u_k$ and $v_k$ are the $k$-th columns of $U$ and $V$ respectively.

---

## 3. Low-Rank Approximation

Keeping only the **top $\ell$** terms of the rank-1 sum gives the **best rank-$\ell$ approximation** of $A$ (in the Frobenius norm):
$$\hat{A}_\ell = \sum_{k=1}^{\ell} \sigma_k\, u_k v_k^T$$

This is the **Eckart–Young theorem**: no other rank-$\ell$ matrix is closer to $A$ in Frobenius norm.

**Approximation error**:
$$\|A - \hat{A}_\ell\| = \sigma_{\ell+1}$$

If the singular values decay quickly (most energy in first few terms), a low-rank approximation is very accurate and much more compact than the full matrix.

---

## 4. Eigenfaces (SVD for Faces)

The **eigenfaces** method applies SVD to a matrix of face images for dimensionality reduction and recognition.

**Setup**:
- Collect $N$ face images, each a vector in $\mathbb{R}^{784}$ (or larger for real images).
- Stack into data matrix $X$ (size $784 \times N$, columns are images).
- (Optionally) subtract the mean face: $\tilde{X} = X - \bar{x}\mathbf{1}^T$.

**Compute SVD**: $\tilde{X} = U \Sigma V^T$.

The columns of $U$ (left singular vectors) are the **eigenfaces** — the principal directions of variation across the face dataset. The first few eigenfaces capture the most variation.

**Dimensionality reduction**: project each face onto the top $\ell$ eigenfaces:
$$z_i = U_\ell^T (x_i - \bar{x})$$

where $U_\ell$ is the first $\ell$ columns of $U$. The compressed representation $z_i \in \mathbb{R}^\ell$ is much smaller than the original $x_i \in \mathbb{R}^{784}$.

**Reconstruction**: recover an approximation to the original face from the compressed representation:
$$\hat{x}_i = \bar{x} + U_\ell z_i$$

---

## 5. SVD-Based Least Squares Classifier

SVD feature reduction can be combined with the least squares classifier:
1. Compute SVD of training data matrix.
2. Project all training and test images onto the top $\ell$ left singular vectors.
3. Train a least squares classifier in the compressed $\ell$-dimensional space.

This reduces the cost of the classifier and often improves generalization (by removing noise dimensions).

---

## 6. Gradient Descent in 2D (Supplement)

Extending the gradient descent from Week 12 to 2D objective functions:
$$J(\theta_1, \theta_2) = \text{some scalar function}$$

The gradient is now a 2-vector:
$$\nabla J = \begin{bmatrix} \partial J / \partial \theta_1 \\ \partial J / \partial \theta_2 \end{bmatrix}$$

Update rule remains the same:
$$\begin{bmatrix} \theta_1^{(k+1)} \\ \theta_2^{(k+1)} \end{bmatrix} = \begin{bmatrix} \theta_1^{(k)} \\ \theta_2^{(k)} \end{bmatrix} - \alpha \begin{bmatrix} \partial J/\partial \theta_1 \\ \partial J/\partial \theta_2 \end{bmatrix}_{\theta^{(k)}}$$

Geometrically, the path spirals or zigzags toward the minimum of the bowl-shaped surface.

---

## 7. Connection to PageRank (Power Iteration)

The PageRank steady-state vector is the **dominant eigenvector** of the Google matrix $G$. The iteration:
$$v^{(k+1)} = G v^{(k)} / \|G v^{(k)}\|$$

is exactly **power iteration**. This is guaranteed to converge (since $G$ is column-stochastic with a unique dominant eigenvalue $\lambda = 1$) and is equivalent to finding the top left singular vector of $G$.

---

## 8. Summary of Dimensionality Reduction Methods Seen in the Course

| Method | What it compresses | How |
|---|---|---|
| k-means clustering | Data points into $k$ clusters | Replace each point with its centroid |
| Polynomial fitting | $m$ data pairs into $n$ coefficients | Vandermonde + least squares |
| SVD / Eigenfaces | $m \times n$ matrix into rank-$\ell$ approximation | Keep top $\ell$ singular value terms |

---

## Summary of key formulas

| Concept | Formula |
|---|---|
| Eigenvector equation | $Av = \lambda v$ |
| SVD decomposition | $A = U\Sigma V^T$ |
| Rank-1 sum (SVD) | $A = \sum_{k=1}^r \sigma_k\, u_k v_k^T$ |
| Best rank-$\ell$ approx. | $\hat{A}_\ell = \sum_{k=1}^\ell \sigma_k\, u_k v_k^T$ |
| Approximation error | $\|A - \hat{A}_\ell\| = \sigma_{\ell+1}$ |
| Eigenface projection | $z_i = U_\ell^T(x_i - \bar{x})$ |
| Reconstruction | $\hat{x}_i = \bar{x} + U_\ell z_i$ |
| Power iteration (PageRank) | $v^{(k+1)} = Gv^{(k)}/\|Gv^{(k)}\|$ |
