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
## 1. The Euclidean Norm

The **Euclidean norm** of an $n$-vector $x$ measures its magnitude (length):
$$\|x\| = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2}$$

It can also be written using the inner product:
$$\|x\| = \sqrt{x^T x}$$

The subscript-$2$ version $\|x\|_2$ refers to the same thing. The norm satisfies four properties:

| Property | Statement |
|---|---|
| Nonnegativity | $\|x\| \ge 0$ |
| Definiteness | $\|x\| = 0 \iff x = \mathbf{0}$ |
| Nonneg. homogeneity | $\|\beta x\| = \lvert \beta \rvert \|x\|$ |
| Triangle inequality | $\|x + y\| \le \|x\| + \|y\|$ |

**Norm of a sum formula** — follows from expanding $(x+y)^T(x+y)$:
$$\|x + y\|^2 = \|x\|^2 + 2x^T y + \|y\|^2$$

### Root-Mean-Square (RMS) value
The RMS value normalizes the norm by the dimension, making it comparable across vectors of different sizes:
$$\text{rms}(x) = \frac{\|x\|}{\sqrt{n}} = \sqrt{\frac{x_1^2 + \cdots + x_n^2}{n}}$$

The quantity under the square root is the **mean square** $\text{ms}(x)$.

### Chebyshev inequality
If $k$ entries of $x$ satisfy $|x_i| \ge a$ for some $a > 0$, then:
$$k \le \frac{\|x\|^2}{a^2} \qquad \Longleftrightarrow \qquad \frac{k}{n} \le \left(\frac{\text{rms}(x)}{a}\right)^2$$

This says the fraction of entries that are "large" (relative to the RMS) is bounded. It justifies thinking of $\text{rms}(x)$ as a "typical" entry size.

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

The **Euclidean distance** between two $n$-vectors $a$ and $b$ is:
$$\text{dist}(a, b) = \|a - b\|$$

- Small distance ↔ the vectors are "close" or "similar."
- The **RMS deviation** is $\|a-b\|/\sqrt{n}$, which normalizes for dimension.

**Triangle inequality (distance form)**:
$$\|a - c\| \le \|a - b\| + \|b - c\|$$
Named for the geometry: one side of a triangle cannot exceed the sum of the other two.

### Applications

- **Nearest neighbor**: find $z_j$ in a collection minimizing $\|x - z_j\|$.
- **RMS prediction error**: $\text{rms}(y - \hat{y})$ when $\hat{y}$ is a forecast.
- **Hamming distance** for Boolean vectors: $\|x - y\|$ counts how many entries differ (since entries are $0/1$), so $\|x - y\| = \sqrt{\text{number of differing entries}}$.

**Unit note**: when vector entries have different physical units, choose units so their magnitudes are roughly comparable — otherwise large-valued entries will dominate the distance unfairly.

---

## 3. Standard Deviation and z-scores

The **de-meaned vector** of $x$ is formed by subtracting the mean from every entry:
$$\tilde{x} = x - \text{avg}(x)\,\mathbf{1}$$

The mean of $\tilde{x}$ is always zero. The **standard deviation** is the RMS of the de-meaned vector:
$$\text{std}(x) = \frac{\|\tilde{x}\|}{\sqrt{n}} = \sqrt{\frac{(x_1 - \text{avg}(x))^2 + \cdots + (x_n - \text{avg}(x))^2}{n}}$$

A small $\text{std}(x)$ means the entries are nearly equal. In finance, $\text{std}$ of a return series is called **risk**.

**Fundamental identity** connecting all three measures:
$$\text{rms}(x)^2 = \text{avg}(x)^2 + \text{std}(x)^2$$

### Standardized vector (z-scores)
$$z = \frac{x - \text{avg}(x)\,\mathbf{1}}{\text{std}(x)}$$

Each entry $z_i$ tells you how many standard deviations $x_i$ is above or below the mean. The standardized vector has $\text{avg}(z) = 0$ and $\text{std}(z) = 1$.

```python
def mean(self):
    total = 0
    for x in self.data:
        total += x
    return total / self.n

def std(self):
    m = self.mean()
    total = 0
    for x in self.data:
        total += (x - m) * (x - m)
    return (total / self.n) ** 0.5

def standardize(self):
    m = self.mean()
    s = self.std()
    for i in range(self.n):
        self.data[i] = (self.data[i] - m) / s
```

---

## 4. Angle Between Vectors

### Cauchy–Schwarz inequality
This is the mathematical foundation for defining angles:
$$|a^T b| \le \|a\|\,\|b\|$$

It guarantees the ratio $\dfrac{a^T b}{\|a\|\|b\|}$ always lies in $[-1, 1]$, so the arccosine below is well-defined.

### Definition of angle
For two nonzero $n$-vectors $a$ and $b$, the angle between them is:
$$\theta = \arccos\!\left(\frac{a^T b}{\|a\|\,\|b\|}\right), \qquad \theta \in [0, \pi]$$

Equivalently: $a^T b = \|a\|\|b\|\cos\theta$.

| Case | Condition | Angle |
|---|---|---|
| Orthogonal | $a^T b = 0$ | $\theta = \pi/2$ |
| Aligned | $a^T b = \|a\|\|b\|$ | $\theta = 0$ |
| Anti-aligned | $a^T b = -\|a\|\|b\|$ | $\theta = \pi$ |
| Acute | $a^T b > 0$ | $\theta < \pi/2$ |
| Obtuse | $a^T b < 0$ | $\theta > \pi/2$ |

**Pythagorean theorem**: if $x \perp y$ (i.e., $x^T y = 0$):
$$\|x + y\|^2 = \|x\|^2 + \|y\|^2$$

---

## 5. Vector Projections

**Projection of $\vec{b}$ onto $\vec{a}$** (the "shadow" of $b$ along $a$):
$$\text{proj}_{\vec{a}}(\vec{b}) = \left(\frac{\vec{a} \cdot \vec{b}}{\vec{a} \cdot \vec{a}}\right)\vec{a}$$

**Component of $\vec{b}$ orthogonal to $\vec{a}$** (the "remainder" at $90°$ to $a$):
$$\vec{b}_{\perp \vec{a}} = \vec{b} - \text{proj}_{\vec{a}}(\vec{b})$$

```python
def parallel(self, other):
    """projection of self onto other"""
    coeff = (self @ other) / (other @ other)
    return Vector([coeff * x for x in other.data])

def perp(self, other):
    """component of self perpendicular to other"""
    return self - self.parallel(other)
```

---

## 6. Vector Tools — Extended Class

The `Vector_Tools` class adds the following methods on top of the base `Vector`:

- `__getitem__` extended to accept **index lists**: `x[[0, 2, 4]]` returns a new vector of entries at those indices.
- `__truediv__`: `y = x / 5` scales $x$ by $\frac{1}{5}$.
- `vec_dist(other)`: Euclidean distance $\|$`self` $-$ `other`$\|$.

```python
def vec_dist(self, other):
    out = 0.0
    for i in range(self.n):
        d = self[i] - other[i]
        out += d * d
    return out ** 0.5
```

---

## 7. MNIST as Vectors in $\mathbb{R}^{784}$

Each MNIST image is $28 \times 28 = 784$ pixels. Flattening it gives a vector in $\mathbb{R}^{784}$. Pixel values $[0, 255]$ are rescaled to $[0, 1]$ by dividing by $255$:

```python
from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784', version=1, as_frame=False)
X, y = mnist.data, mnist.target

L_train = [Vector(X_train[i]) / 255 for i in range(N_train)]
```

Now distance $\|x - y\|$ between two image-vectors measures pixel-by-pixel dissimilarity. Nearest-neighbor search in $\mathbb{R}^{784}$ finds visually similar images.

---

## Summary of key formulas

| Concept | Formula |
|---|---|
| Euclidean norm | $\|x\| = \sqrt{x^T x}$ |
| RMS value | $\text{rms}(x) = \|x\|/\sqrt{n}$ |
| Distance | $\text{dist}(a,b) = \|a-b\|$ |
| Norm of sum | $\|x+y\|^2 = \|x\|^2 + 2x^Ty + \|y\|^2$ |
| Std. deviation | $\text{std}(x) = \|\tilde{x}\|/\sqrt{n}$, $\;\tilde{x} = x - \text{avg}(x)\mathbf{1}$ |
| rms–avg–std identity | $\text{rms}^2 = \text{avg}^2 + \text{std}^2$ |
| z-score | $z = (x - \text{avg}(x)\mathbf{1})/\text{std}(x)$ |
| Cauchy–Schwarz | $\lvert a^T b\rvert \le \|a\|\|b\|$ |
| Angle | $\theta = \arccos\!\bigl(a^T b / (\|a\|\|b\|)\bigr)$ |
| Projection | $\text{proj}_a(b) = \bigl(a^T b / a^T a\bigr)\,a$ |
