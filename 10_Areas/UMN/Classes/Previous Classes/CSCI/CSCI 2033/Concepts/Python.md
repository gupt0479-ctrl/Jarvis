---
type: class
status: seed
created: 2025-10-02
updated:
area:
  - "[[Final]]"
  - "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2033/Midterm - 1|Midterm - 1]]"
tags:
  - "#class"
next: "[[Final]]"
---
# CSCI 2033 — Concepts Folder Index
## Master Map of Content
This is the home file for everything in this course. The course uses **Boyd & Vandenberghe — Introduction to Applied Linear Algebra** and builds up to real ML applications. Every concept here has a direct counterpart in machine learning, data science, and graph analysis.
## Course Arc (How it all connects)

```
Vectors → Norms/Distance → Linear Functions → Regression
    ↓
Matrices → Matrix–Vector Products → Linear Systems
    ↓
Decompositions (QR, SVD, Householder)
    ↓
Least Squares → Classifiers → Gradient Descent
    ↓
PageRank / Graph Networks / Eigenfaces
```
## Weekly Notes

| File | Week | Core Topic |
|---|---|---|
| [[Week_1_and_2]] | 1 & 2 | Vectors, inner product, linear functions, regression model, Vector class |
| [[Week_3]] | 3 | Norm, distance, std dev, angle, projections, MNIST |
| [[Week_4]] | 4 | k-means clustering, k-NN classification |
| [[Week_5]] | 5 | Linear independence, orthonormality, Gram–Schmidt, Matrix class |
| [[Week_6]] | 6 | Geometric transforms, graphs, adjacency matrices, linear equations, Jacobi |
| [[Week_8_and_9]] | 8 & 9 | Matrix products, composition, QR factorization, Householder reflectors |
| [[Week_10]] | 10 | Left/right inverses, back substitution, polynomial interpolation |
| [[Week_11]] | 11 | Least squares regression, feature engineering, train/test error |
| [[Week_12]] | 12 | Least squares classifiers, gradient descent, ROC curves |
| [[Week_13]] | 13 | SVD, low-rank approximation, eigenfaces, facial recognition |
## Chapter-to-week mapping

| Textbook chapter                   | Week  |
| ---------------------------------- | ----- |
| Ch. 1 — Vectors                    | 1 & 2 |
| Ch. 2 — Linear Functions           | 1 & 2 |
| Ch. 3 — Norms                      | 3     |
| Ch. 4 — Clustering                 | 4     |
| Ch. 5 — Linear Independence        | 5     |
| Ch. 6 — Matrices                   | 5     |
| Ch. 7 — Matrix Examples            | 6     |
| Ch. 8 — Linear Equations           | 6     |
| Ch. 9 — Dynamical Systems          | 8     |
| Ch. 10 — Matrix–Matrix Products    | 8 & 9 |
| Ch. 11 — Linear Systems            | 10    |
| Ch. 12 — Least Squares             | 11    |
| Ch. 13 — Feature Engineering       | 11    |
| Ch. 14 — Least Squares Classifiers | 12    |
| Supplement — Gradient Descent      | 12    |
| Supplement — SVD                   | 13    |


## Concept Reference Files (Cross-Course)

| File | What it covers |
|---|---|
| [[Graphs_and_PageRank]] | Graph theory, adjacency matrices, incidence matrices, PageRank algorithm — standalone reference |
| [[Matrix_Operations_Reference]] | Every matrix operation in one place: types, products, inverses, factorizations |
| [[ML_Foundations]] | How this course maps directly to ML: regression, classification, gradient descent, dimensionality reduction |

---

## Labs Map

| Lab | Topic | Key algorithm |
|---|---|---|
| Lab 1 | Vector Tools | Vector class, inner product, slicing |
| Lab 2 | Vector Norm | Norm, distance, angle, projections |
| Lab 3 | k-Nearest Neighbors | kNN on MNIST |
| Lab 4 | k-Means Clustering | k-means on MNIST |
| Lab 5 | Matrix Class | Matrix, zeros, ones, diag, eye |
| Lab 6 | PageRank | Adjacency → S → G → power iteration |
| Lab 7 | Householder QR | QR factorization, $Q^T b$, $Qx$ |
| Lab 8 | Linear Systems + Interpolation | BackSub, QRSolve, Vandermonde |
| Lab 9 | Least Squares Regression | Polynomial fit, train/test error |
| Lab 10 | Least Squares Classifier | Binary classifier, feature engineering, ROC |
| Lab 11 | Gradient Descent | GD on MNIST, one-vs-all classifier |
| Lab 12 | Eigenfaces | SVD, de-mean, $\hat{B}$, $\hat{W}$, kNN in eigenspace |

---

## Core Formulas at a Glance

$$a^T b = \sum_i a_i b_i \qquad \|x\| = \sqrt{x^T x} \qquad \theta = \arccos\!\left(\frac{a^T b}{\|a\|\|b\|}\right)$$

$$y = Ax \qquad A = QR \qquad x = R^{-1}Q^T b$$

$$A = U\Sigma V^T \qquad G = \alpha S + \frac{1-\alpha}{n}J \qquad \theta^{(k+1)} = \theta^{(k)} - \alpha\nabla J(\theta^{(k)})$$

---

## Python Tools Built in this Course

```python
# Hierarchy of classes built from scratch
Vector          → Vector1/2/3/4/5 (extended methods)
Matrix          → zeros, ones, diag, eye, Vector (as subclass)

# Algorithms implemented
HouseHolderQR(A)         → V, R
Qstarb(V, b)             → Q^T b
Qx(V, x)                 → Q x
BackSub(R, b)            → x  (solves Rx = b)
QRSolve(A, b)            → x  (solves Ax = b via QR)
```

---

## Tags Used Across Notes

`#Textbook` `#Lecture` `#Jupyter` `#Quiz` `#Homework` `#Lab` `#ML` `#Graphs` `#LinearAlgebra`
