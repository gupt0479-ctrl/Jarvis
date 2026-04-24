---
type: evergreen
status: archived
created: 2025-12-31
topic: "ML Foundations from CSCI 2033"
tags:
  - "#ML"
  - "#LinearAlgebra"
  - "#Reference"
  - "#Foundations"
related: [[Python]], [[Week_11_to_13]], [[Graphs_and_PageRank]]
---

# ML Foundations — How CSCI 2033 Builds Toward Machine Learning

> This course is not just linear algebra. Every single algorithm here has a direct descendant in ML. This file maps what you built to where it leads.

---

## 1. Data as Vectors

**This course**: every data point is an $n$-vector. MNIST images are $784$-vectors. Documents are word-count vectors.

**ML continuation**:
- Features = coordinates of the vector
- Dataset = matrix $X$ ($N\times n$, rows are examples)
- **Embedding**: representing objects (words, graphs, images) as vectors → the core of modern deep learning

**Why it matters**: once data is a vector, every linear algebra tool applies. Distance, projection, matrix operations, optimization — all of it.

---

## 2. Regression → Supervised Learning

**This course**: linear regression model $\hat{y} = x^T\beta + v$. Minimize $\|A\beta - b\|^2$. Solved analytically with QR.

**ML continuation**:
| This course | ML equivalent |
|---|---|
| Linear regression | Backbone of all prediction models |
| Least squares loss | MSE loss (most common regression loss) |
| Feature engineering (poly, random) | Feature maps, kernel trick, neural network layers |
| Overfitting / train-test split | Bias-variance tradeoff, generalization, cross-validation |
| Relative prediction error | $R^2$, RMSE evaluation metrics |

**Critical concept — the train/test split**: Lab 9 showed that training error always decreases with model complexity but test error has a U-shape. The whole field of ML regularization (ridge, LASSO, dropout) exists to control this.

---

## 3. Classification → Supervised Learning

**This course**: least squares classifier, binary $\{+1,-1\}$ labels, $\hat{f}(x) = x^T\beta + v$, threshold at $0$.

**ML continuation**:
| This course | ML equivalent |
|---|---|
| Binary LS classifier | Linear SVM (hard-margin), logistic regression |
| One-vs-all multi-class | Standard strategy for multi-class SVMs |
| Feature engineering + classifier | Kernel methods (polynomial kernel = polynomial features) |
| Random features $\text{ReLU}(Rx)$ | Random kitchen sinks, Extreme Learning Machines (ELMs) |
| ROC curve | Standard binary classifier evaluation |
| Confusion matrix | Precision, recall, F1 score |

**Key insight**: the decision boundary $x^T\beta + v = 0$ is a hyperplane. Everything in ML classification is about finding hyperplanes (linear) or learning complex nonlinear boundaries (via features or neural nets).

---

## 4. Clustering → Unsupervised Learning

**This course**: k-means minimizes $J_\text{clust} = \frac{1}{N}\sum\|x_i - z_{c_i}\|^2$. Alternating optimization: assign → update.

**ML continuation**:
| This course | ML equivalent |
|---|---|
| k-means | Foundation of vector quantization, prototype methods |
| k-means on MNIST | Self-supervised feature learning, VQ-VAE |
| Centroid as "representative" | Prototypical networks in few-shot learning |
| k-NN classifier | Non-parametric classification, memory-based learning |
| Cosine similarity for nearest neighbor | Word embeddings (Word2Vec, GloVe), semantic search |

**Key insight**: k-means and kNN together cover the two ends of the unsupervised/supervised spectrum. Most modern clustering (GMM, spectral clustering) generalizes from k-means.

---

## 5. Gradient Descent → Optimization (Core of DL)

**This course**: minimize $\ell(w) = \frac{1}{2}\|Xw - y\|^2$ iteratively:
$$w^{(k+1)} = w^{(k)} - t\,\nabla\ell(w^{(k)})$$

**ML continuation**:
| This course | ML equivalent |
|---|---|
| Gradient descent (GD) | Exact same algorithm used to train neural networks |
| Step size $t$ | Learning rate (most important hyperparameter in DL) |
| Convergence plot (loss vs. iteration) | Training curves — standard diagnostic |
| Relative stopping criterion | Early stopping |
| Slow convergence (bad conditioning) | Why normalization and Adam optimizer exist |
| Stochastic GD (SGD) | Mini-batch SGD — how neural nets actually train |
| One-vs-all with GD | Multi-class softmax layer in neural net |

**The gradient of a loss w.r.t. weights** $\nabla_W \ell = X^T(XW - Y)$ is the simplest case of **backpropagation**. Neural networks are just chains of these — by the chain rule.

---

## 6. SVD and Dimensionality Reduction → Representation Learning

**This course**: SVD $A = U\Sigma V^T$. Keep top $k$ singular values for best rank-$k$ approximation. Eigenfaces project faces onto a low-dimensional subspace.

**ML continuation**:
| This course | ML equivalent |
|---|---|
| SVD low-rank approximation | **PCA** (principal component analysis) — identical math |
| Eigenfaces ($k=20$ components) | PCA-based face recognition, standard baseline |
| De-mean before SVD | Centering data — required preprocessing for PCA |
| Top $k$ singular vectors | Principal components |
| Compression: $4096 \to 20$ dims | Dimensionality reduction, bottleneck representation |
| Nearest-neighbor in eigenspace | PCA + kNN classifier |
| $\sigma_k$ decay rate | How much variance each PC explains |

**Beyond PCA**: SVD is also the backbone of **collaborative filtering** (Netflix prize), **latent semantic analysis** (NLP), **matrix completion** (recommender systems), and the **Moore-Penrose pseudo-inverse** used everywhere.

---

## 7. PageRank → Graph ML

**This course**: random surfer model, transition matrix $S$, damped Google matrix $G = \alpha S + \frac{1-\alpha}{n}J$, power iteration.

**ML continuation**:
| This course | ML equivalent |
|---|---|
| Column-stochastic matrix | Markov chain / transition model |
| Power iteration | Approximating dominant eigenvectors |
| PageRank vector | Node importance / centrality measure |
| Random walk on graph | DeepWalk, Node2Vec (generate node embeddings) |
| Graph adjacency + powers | Message passing in Graph Neural Networks (GNNs) |
| Dirichlet energy on graph | Graph regularization in semi-supervised learning |
| Graph Laplacian | Spectral clustering, Laplacian Eigenmaps |

**Why this matters for ML**: graphs are everywhere — social networks, molecules, knowledge graphs, citation networks, transportation systems. The math you learned here (adjacency matrices, random walks, eigenvectors of stochastic matrices) is the foundation of modern graph ML.

---

## 8. The Big Picture

```
CSCI 2033                          ML / Later Courses
─────────────                      ─────────────────────
Vectors & inner products       →   Feature representations
Norm & distance                →   Loss functions, metrics
Linear functions               →   Linear models, affine layers
Regression (least squares)     →   Supervised learning
QR factorization               →   Numerical linear algebra in DL
Gradient descent               →   Neural network training
Classification (±1 labels)     →   Binary/multi-class learning
Feature engineering            →   Feature maps, kernels, NN layers
SVD / eigenfaces               →   PCA, dimensionality reduction
k-means clustering             →   Unsupervised learning
k-NN                           →   Non-parametric classification
PageRank / graph matrices      →   Graph neural networks, network analysis
```

---

## 9. Algorithms You Can Actually Implement from Scratch

After this course, you can build from first principles:

1. **Vector/Matrix class** — memory-efficient numerical objects
2. **Gram–Schmidt** → QR factorization
3. **Householder reflectors** → numerically stable QR
4. **Back substitution** → solving triangular systems
5. **QRSolve** → any linear system or least squares problem
6. **k-means** → unsupervised clustering
7. **kNN** → non-parametric classification
8. **Least squares classifier** → binary and multi-class
9. **Gradient descent** → optimization of any differentiable loss
10. **PageRank power iteration** → ranking nodes in any graph
11. **SVD + Eigenfaces** → dimensionality reduction and recognition

These are not toy implementations — they are the exact algorithms used in production systems, just without the engineering optimizations.

---

## 10. What Comes Next

| After CSCI 2033 | What you're ready for |
|---|---|
| CSCI 5512 (AI) | Search, constraint satisfaction, probabilistic reasoning |
| CSCI 5521 (ML) | All supervised/unsupervised learning algorithms |
| CSCI 5525 (ML theory) | PAC learning, generalization bounds, VC dimension |
| CSCI 5980 (DL) | Neural networks, backprop, CNNs — built on this math |
| CSCI 5607 (Computer Graphics) | Transforms, projections, rasterization — all linear algebra |
| Graph ML courses | GNNs, network analysis — built on graph + matrix concepts |
