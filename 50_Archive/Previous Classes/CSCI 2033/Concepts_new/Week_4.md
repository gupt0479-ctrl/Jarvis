---
type: concept
status: archived
created: 2025-10-10
updated: 2025-11-01
week: "4"
chapters: "Ch. 4"
tags:
  - "#Textbook"
  - "#Lecture"
  - "#Jupyter"
  - "#Quiz"
  - "#Homework"
  - "#ML"
prev: [[Week_3]]
next: [[Week_5]]
---

# Week 4 — Clustering and k-Nearest Neighbors
### Ch. 4: Clustering

---

## 1. What is Clustering?

**Clustering** partitions $N$ vectors $x_1, \ldots, x_N \in \mathbb{R}^n$ into $k$ groups so that vectors in the same group are as close as possible. The only signal is distance — there are no labels.

In real applications, $n$ is large ($784$ for MNIST, thousands for text), so visual inspection is impossible. Distance alone drives everything.

**Applications**: topic discovery in documents, patient grouping by symptoms, customer segmentation, image compression, weather-zone identification, recommendation systems.

---

## 2. Formal Setup

**Assignment vector** $c$ (length $N$): entry $c_i \in \{1,\ldots,k\}$ = which group $x_i$ belongs to.

**Index set** $G_j = \{i \mid c_i = j\}$: all indices in group $j$.

**Group representative / centroid** $z_j \in \mathbb{R}^n$: the "archetype" of group $j$. The optimal representative (for fixed assignment) is:
$$z_j = \frac{1}{|G_j|} \sum_{i \in G_j} x_i$$

**Clustering objective** $J_\text{clust}$ — mean squared distance from every point to its representative:
$$J_\text{clust} = \frac{1}{N} \sum_{i=1}^{N} \|x_i - z_{c_i}\|^2$$

Goal: minimize $J_\text{clust}$. Smaller = better clustering.

---

## 3. k-Means Algorithm (Lab 4)

Alternates between two steps, each of which can only **decrease** $J_\text{clust}$:

**Step 1 — Assignment**: assign each $x_i$ to its nearest representative:
$$c_i = \arg\min_j \|x_i - z_j\|$$

**Step 2 — Update**: recompute each centroid as the mean of its current group:
$$z_j = \frac{1}{|G_j|} \sum_{i \in G_j} x_i$$

Repeat until no assignments change.

**Convergence**: guaranteed because $J_\text{clust}$ decreases every step and there are finitely many assignments.

**Complexity per iteration**: $\approx (3k+1)Nn$ flops — linear in $N$, $n$, and $k$.

**MNIST result**: $N = 60{,}000$ images, $k = 20$ → centroids look like recognizable digits. The algorithm finds structure with zero label knowledge.

---

## 4. k-Nearest Neighbors (Lab 3)

kNN predicts labels for new data by looking at what the nearest neighbors say.

**Algorithm for query $x$**:
1. Compute $\text{dist}(x, x_i)$ for all $i$ in training set.
2. Find indices of $k$ smallest distances.
3. Predict by **majority vote** among their labels.

```python
# sort ALL training indices by their distance to test_vec
indices = sorted(range(N_train), key=lambda i: distances[i])[:k]
labels  = y_train[indices]

# majority vote — count each digit 0–9
max_count  = counts[0]
prediction = 0
for i in range(1, 10):
    if counts[i] > max_count:
        max_count  = counts[i]
        prediction = i
```

`heapq.nsmallest(k, iterable, key=...)` is the efficient built-in alternative.

---

## 5. k-Means vs. k-NN

| Aspect | k-Nearest Neighbors | k-Means Clustering |
|---|---|---|
| Goal | Predict label for new point | Discover groups in data |
| At prediction time | Recompute all distances | Look up nearest centroid |
| Computation | $O(Nn)$ per query — slow at scale | Pre-computes $k$ centroids — fast |
| Personalization | Highly individual (unique neighbors) | Generalized (everyone in cluster gets same rep) |
| What "k" means | # neighbors to vote | # clusters |
| Requires labels | Yes (supervised) | No (unsupervised) |

---

## 6. Measuring Similarity: Two Notions

**Euclidean distance** — absolute proximity:
$$\text{dist}(x, y) = \|x - y\|$$

**Cosine similarity** — directional alignment (ignores magnitude):
$$\cos\theta = \frac{x \cdot y}{\|x\|\,\|y\|}$$

For unit vectors, both give the **same ranking**. In NLP and recommendation systems, cosine similarity is often preferred because magnitude doesn't matter (a short and long document on the same topic should be close).

---

## 7. Group Representative Matrix

When there are $k$ clusters, the $k \times n$ **group representative matrix** $A$ has row $g$ = centroid of cluster $g$. Entry $A_{gj}$ is the mean value of feature $j$ in cluster $g$. Used in recommendation: "all users in cluster $g$ get the same recommended playlist."

---

## ML Connection

- **k-means** is foundational unsupervised learning — same ideas appear in Vector Quantization, EM algorithm, Gaussian Mixture Models.
- **kNN** is the simplest non-parametric classifier — no training phase, decision boundary is implicit.
- **Centroid as representative** → the idea of "prototype" reappears in cluster-based neural networks, Radial Basis Functions, and attention mechanisms.
- $J_\text{clust}$ is an instance of a broader **within-cluster variance** objective used throughout ML.

---

## Summary

| Concept | Formula |
|---|---|
| Centroid of group $j$ | $z_j = \frac{1}{|G_j|}\sum_{i \in G_j} x_i$ |
| Clustering objective | $J_\text{clust} = \frac{1}{N}\sum_{i=1}^N \|x_i - z_{c_i}\|^2$ |
| k-means assignment | $c_i = \arg\min_j \|x_i - z_j\|$ |
| Complexity per iter. | $\approx (3k+1)Nn$ flops |
| Cosine similarity | $\cos\theta = x^Ty/(\|x\|\|y\|)$ |
