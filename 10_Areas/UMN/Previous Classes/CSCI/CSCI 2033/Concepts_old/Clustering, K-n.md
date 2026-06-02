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
## 1. What is Clustering?

**Clustering** partitions a collection of $N$ vectors $x_1, \ldots, x_N \in \mathbb{R}^n$ into $k$ groups so that vectors within the same group are as close to each other as possible.

In practice the vectors are usually high-dimensional ($n \gg 2$), so visual inspection is not possible. The distance between vectors is the sole measure of similarity.

**Typical applications**: topic discovery in documents, patient grouping by symptoms, customer market segmentation, weather-zone identification, image clustering (MNIST digits), recommendation systems.

---

## 2. Formalizing the Clustering Problem

### Assignment vector
The clustering is described by an $N$-vector $c$ where entry $c_i \in \{1, \ldots, k\}$ is the group number assigned to $x_i$.

**Index sets**: $G_j = \{i \mid c_i = j\}$ contains all indices belonging to group $j$.

### Group representatives (centroids)
Each group $j$ has a representative $z_j \in \mathbb{R}^n$. The goal is for $z_{c_i}$ to be close to $x_i$. The optimal representative for a fixed assignment is the **centroid** (mean) of the group:
$$z_j = \frac{1}{|G_j|} \sum_{i \in G_j} x_i$$

### Clustering objective $J_\text{clust}$
The quality of a clustering is measured by the mean squared distance from every vector to its assigned representative:
$$J_\text{clust} = \frac{1}{N} \sum_{i=1}^{N} \|x_i - z_{c_i}\|^2$$

A smaller $J_\text{clust}$ means a better clustering. The goal is to minimize it jointly over the assignment $c$ and the representatives $z_1, \ldots, z_k$.

---

## 3. The k-Means Algorithm

The k-means algorithm alternates between two steps, each of which can only decrease (or maintain) $J_\text{clust}$.

**Input**: data $x_1, \ldots, x_N$ and an initial set of representatives $z_1, \ldots, z_k$.

**Step 1 — Assignment**: assign every $x_i$ to its closest representative:
$$c_i = \arg\min_{j} \|x_i - z_j\|$$

**Step 2 — Update**: recompute each representative as the mean of its current group:
$$z_j = \frac{1}{|G_j|} \sum_{i \in G_j} x_i$$

Repeat until assignments no longer change.

**Convergence**: because $J_\text{clust}$ decreases or stays the same every step and there are finitely many possible assignments, the algorithm always terminates.

**Complexity per iteration**: approximately $(3k + 1)Nn$ flops — linear in $N$, $n$, and $k$.

---

## 4. k-Nearest Neighbors (kNN)

While k-means groups all data up front, **kNN** makes predictions by finding the $k$ most similar data points to a new query at prediction time.

**Algorithm for a query vector $x$**:
1. Compute $\text{dist}(x, x_i)$ for all $i$ in the training set.
2. Find the $k$ indices with smallest distance.
3. Predict the label by **majority vote** among those $k$ neighbors.

```python
# sorted indices by distance (smallest first), take first k
indices = sorted(range(N_train), key=lambda i: distances[i])[:k]
labels  = y_train[indices]   # labels of k nearest neighbors

# majority vote — count occurrences of each digit 0–9
max_count  = counts[0]
prediction = 0
for i in range(1, 10):
    if counts[i] > max_count:
        max_count  = counts[i]
        prediction = i
```

`heapq.nsmallest(k, iterable, key=...)` is a convenient built-in for this.

---

## 5. k-Means vs. k-NN — Key Differences

| Aspect | k-Nearest Neighbors | k-Means Clustering |
|---|---|---|
| Similarity notion | Finds the $k$ most similar individual data points | Groups all data into $k$ clusters |
| Computation | Recompute distances for every query — slower for large $N$ | Pre-computes clusters once — faster for new queries |
| Personalization | Highly individualized (unique neighbors) | More generalized (same centroid for all in cluster) |
| Prediction source | Average of $k$ nearest data points | Centroid $z_j$ of the nearest cluster |
| Best when | Dataset is small or fine-grained personalization needed | Dataset is large and scalable, grouped output is fine |

---

## 6. Group Representative Matrix

When there are $k$ clusters and each data point is an $n$-vector, the **group representative matrix** $A$ has $k$ rows and $n$ columns. Row $g$ is the centroid $z_g$ of cluster $g$, so entry $A_{gj}$ is the mean value of feature $j$ within cluster $g$.

For the nearest-neighbor search in 2D / higher-dimensional cosine similarity:

**Euclidean distance** measures absolute proximity: $\|x - y\|$.

**Cosine similarity** (angle-based) measures directional alignment regardless of magnitude:
$$\cos\theta = \frac{x \cdot y}{\|x\|\,\|y\|}$$

For unit vectors both measures give the same ranking.

---

## 7. Applications in Practice

**MNIST clustering**: applying k-means to $N = 60{,}000$ images ($784$-vectors) with $k = 20$ produces recognizable digit archetypes as centroids — the algorithm discovers digit structure without any label information.

**Wikipedia topic discovery**: clustering $N = 500$ articles (word-count vectors) with $k = 9$ produces groups with clear separate themes (movies, sports, holidays, etc.).

**Missing entry imputation**: run k-means on complete data, then for an incomplete vector find the closest centroid using only known entries, and fill in the missing entries from that centroid.

---

## Summary of key formulas

| Concept | Formula |
|---|---|
| Centroid of group $j$ | $z_j = \frac{1}{\lvert G_j\rvert}\sum_{i \in G_j} x_i$ |
| Clustering objective | $J_\text{clust} = \frac{1}{N}\sum_{i=1}^{N}\|x_i - z_{c_i}\|^2$ |
| k-means assignment step | $c_i = \arg\min_j \|x_i - z_j\|$ |
| k-means complexity/iter. | $\approx (3k+1)Nn$ flops |
| Cosine similarity | $\cos\theta = \frac{x \cdot y}{\|x\|\|y\|}$ |
