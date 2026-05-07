---
type: concept
status: archived
created: 2025-09-30
updated: 2025-12-31
week: "3"
chapters: "Ch. 3"
tags:
  - "#Textbook"
  - "#Lecture"
  - "#Jupyter"
  - "#Quiz"
  - "#Homework"
  - "#LinearAlgebra"
  - "#ML"
prev: [[Week_1_and_2]]
next: [[Week_4]]
---

# Week 3 — Norm, Distance, Standard Deviation, and Angles
### Ch. 3: Norm and Distance

---

## 1. Euclidean Norm

The norm measures the "length" or magnitude of a vector:
$$\|x\| = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2} = \sqrt{x^T x}$$

Also written $\|x\|_2$ (L2 norm). Four required properties:

| Property | Statement |
|---|---|
| Nonnegativity | $\|x\| \ge 0$ |
| Definiteness | $\|x\| = 0 \iff x = \mathbf{0}$ |
| Homogeneity | $\|\beta x\| = |\beta|\,\|x\|$ |
| Triangle inequality | $\|x+y\| \le \|x\| + \|y\|$ |

**Norm of a sum** — useful identity derived from $(x+y)^T(x+y)$:
$$\|x+y\|^2 = \|x\|^2 + 2x^T y + \|y\|^2$$

### RMS Value

Normalizes the norm by dimension for comparability across different $n$:
$$\text{rms}(x) = \frac{\|x\|}{\sqrt{n}} = \sqrt{\frac{x_1^2 + \cdots + x_n^2}{n}}$$

Represents a "typical" entry size.

### Chebyshev Inequality

If $k$ entries of $x$ satisfy $|x_i| \ge a$:
$$k \le \frac{\|x\|^2}{a^2} \qquad \Longleftrightarrow \qquad \frac{k}{n} \le \left(\frac{\text{rms}(x)}{a}\right)^2$$

Bounds what fraction of entries can be "large" relative to the RMS. Justifies using RMS as a typical size.

```python
def norm(self):
    output = 0.0
    for i in range(self.n):
        output += self.data[i] ** 2
    return output ** 0.5

def rms(self):
    total = 0
    for x in self.data:
        total += x * x
    return (total / self.n) ** 0.5
```

---

## 2. Distance

$$\text{dist}(a, b) = \|a - b\|$$

Small distance ↔ vectors are "close" / "similar." The **RMS deviation** $\|a-b\|/\sqrt{n}$ normalizes for dimension.

**Triangle inequality**: $\|a - c\| \le \|a - b\| + \|b - c\|$ (one side of a triangle ≤ sum of other two).

**Applications**:
- Nearest neighbor: find $z_j$ minimizing $\|x - z_j\|$
- RMS prediction error: $\text{rms}(y - \hat{y})$
- Hamming distance for Boolean vectors: $\|x-y\| = \sqrt{\text{# differing entries}}$

**Units rule**: when vector entries have different physical units, choose units so all entries have roughly the same magnitude — otherwise large-valued entries unfairly dominate the distance.

---

## 3. Standard Deviation and Z-Scores

**De-meaned vector**: subtract the mean from every entry:
$$\tilde{x} = x - \text{avg}(x)\,\mathbf{1}$$

The mean of $\tilde{x}$ is always zero.

**Standard deviation** = RMS of the de-meaned vector:
$$\text{std}(x) = \frac{\|\tilde{x}\|}{\sqrt{n}} = \sqrt{\frac{(x_1 - \text{avg}(x))^2 + \cdots + (x_n - \text{avg}(x))^2}{n}}$$

Small $\text{std}$ → entries are nearly equal. In finance: std of returns = **risk**.

**Fundamental identity**:
$$\text{rms}(x)^2 = \text{avg}(x)^2 + \text{std}(x)^2$$

**Standardized vector (z-scores)**:
$$z = \frac{x - \text{avg}(x)\,\mathbf{1}}{\text{std}(x)}$$

Entry $z_i$ tells you how many standard deviations $x_i$ is above/below the mean. Always has $\text{avg}(z) = 0$ and $\text{std}(z) = 1$.

```python
def mean(self):
    total = 0
    for x in self.data: total += x
    return total / self.n

def std(self):
    m = self.mean()
    total = 0
    for x in self.data: total += (x - m) ** 2
    return (total / self.n) ** 0.5

def standardize(self):           # convert to z-scores in place
    m, s = self.mean(), self.std()
    for i in range(self.n):
        self.data[i] = (self.data[i] - m) / s
```

---

## 4. Angle Between Vectors

**Cauchy–Schwarz inequality** (guarantees the angle is well-defined):
$$|a^T b| \le \|a\|\,\|b\|$$

This ensures $a^T b / (\|a\|\|b\|) \in [-1,\,1]$, so arccos is valid.

**Angle definition**:
$$\theta = \arccos\!\left(\frac{a^T b}{\|a\|\,\|b\|}\right), \qquad \theta \in [0,\,\pi]$$

Equivalently: $a^T b = \|a\|\|b\|\cos\theta$.

| Case | Condition | Angle |
|---|---|---|
| Orthogonal | $a^T b = 0$ | $90°$ |
| Aligned | $a^T b = \|a\|\|b\|$ | $0°$ |
| Anti-aligned | $a^T b = -\|a\|\|b\|$ | $180°$ |
| Acute | $a^T b > 0$ | $< 90°$ |
| Obtuse | $a^T b < 0$ | $> 90°$ |

**Pythagorean theorem**: if $x \perp y$ (i.e., $x^T y = 0$):
$$\|x + y\|^2 = \|x\|^2 + \|y\|^2$$

---

## 5. Vector Projections (Lab 2)

**Projection of $\vec{b}$ onto $\vec{a}$** (the "shadow" of $b$ along $a$):
$$\text{proj}_{\vec{a}}(\vec{b}) = \left(\frac{\vec{a} \cdot \vec{b}}{\vec{a} \cdot \vec{a}}\right)\vec{a}$$

**Component of $\vec{b}$ orthogonal to $\vec{a}$** (the "remainder"):
$$\vec{b}_{\perp \vec{a}} = \vec{b} - \text{proj}_{\vec{a}}(\vec{b})$$

```python
def parallel(self, other):
    """component of self parallel to other (projection)"""
    coeff = (self @ other) / (other @ other)
    return Vector([coeff * x for x in other.data])

def perp(self, other):
    """component of self perpendicular to other"""
    return self - self.parallel(other)
```

---

## 6. Extended Vector Class (Lab 2 / Vector_Tools)

Adds three important methods on top of the base `Vector`:

```python
def __getitem__(self, i):
    if type(i) == list:                      # index list: x[[0,2,4]]
        return Vector([self.data[k] for k in i])
    elif -self.n < i < self.n:
        return self.data[i]
    else: raise Exception("Index out of bounds")

def __truediv__(self, other):               # division: x / 5
    return self * (1.0 / other)

def vec_dist(self, other):                  # Euclidean distance
    out = 0.0
    for i in range(self.n):
        d = self[i] - other[i]
        out += d * d
    return out ** 0.5
```

---

## 7. MNIST — Vectors in $\mathbb{R}^{784}$ (Lab 2 / 3)

Each MNIST image is $28 \times 28 = 784$ pixels → a vector in $\mathbb{R}^{784}$.

```python
from sklearn.datasets import fetch_openml
mnist   = fetch_openml('mnist_784', version=1, as_frame=False)
X, y    = mnist.data, mnist.target

# scale [0,255] → [0,1] and convert to Vector objects
L_train = [Vector(X_train[i]) / 255 for i in range(N_train)]
```

Distance $\|x - y\|$ between two image-vectors measures pixel-by-pixel dissimilarity. All nearest-neighbor and clustering work rests on this.

---

## ML Connection

- **Distance** is the backbone of kNN, k-means, and anomaly detection.
- **Cosine similarity** ($= \cos\theta$) is the standard metric in NLP (word embeddings, document similarity).
- **Standardization** (z-scores) is preprocessing step #1 before any gradient-based model.
- **RMS error** is the loss function for regression.

---

## Summary

| Concept | Formula |
|---|---|
| Norm | $\|x\| = \sqrt{x^T x}$ |
| RMS value | $\text{rms}(x) = \|x\|/\sqrt{n}$ |
| Distance | $\text{dist}(a,b) = \|a-b\|$ |
| Norm of sum | $\|x+y\|^2 = \|x\|^2 + 2x^Ty + \|y\|^2$ |
| Std deviation | $\text{std}(x) = \|\tilde{x}\|/\sqrt{n}$ |
| rms–avg–std identity | $\text{rms}^2 = \text{avg}^2 + \text{std}^2$ |
| Z-score | $z = (x - \text{avg}\cdot\mathbf{1})/\text{std}$ |
| Cauchy–Schwarz | $|a^Tb| \le \|a\|\|b\|$ |
| Angle | $\theta = \arccos(a^Tb/(\|a\|\|b\|))$ |
| Projection | $\text{proj}_a(b) = (a^Tb/a^Ta)\,a$ |
