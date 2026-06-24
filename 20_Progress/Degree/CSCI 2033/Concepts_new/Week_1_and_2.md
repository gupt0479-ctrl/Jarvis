---
type: concept
status: complete
created: 2025-09-17
updated: 2025-10-16
week: "1 & 2"
chapters: "Ch. 1 & 2"
tags:
  - "#Textbook"
  - "#Lecture"
  - "#Jupyter"
  - "#Quiz"
  - "#Homework"
  - "#LinearAlgebra"
next: [[Week_3]]
---

# Week 1 & 2 — Vectors and Linear Functions
### Ch. 1: Vectors | Ch. 2: Linear Functions

---

## 1. Vectors

A **vector** is an ordered finite list of numbers. An $n$-vector $x$ has entries $x_1, x_2, \ldots, x_n$ (textbook indexes from $1$; Python from $0$).

**Key notation**:
- Subvector / slice: $x_{r:s}$ gives entries from $r$ to $s$
- Stacked vector: $(a, b)$ is a longer vector formed by writing $a$ then $b$
- Two vectors are **equal** only if same size AND every entry matches

**Sparsity**: a vector is sparse when most entries are $0$. The count of nonzeros is $\text{nnz}(x)$. Unit vectors $e_i$ (one `1`, rest `0`) are the canonical sparse vectors.

### Vector Addition and Scalar Multiplication

Addition only works for same-size vectors — add corresponding entries. Properties:

| Property | Statement |
|---|---|
| Commutativity | $a + b = b + a$ |
| Zero vector | $a + \mathbf{0} = a$ |
| Scalar associativity | $\alpha(\beta a) = (\alpha\beta)a$ |
| Distributivity | $\alpha(a+b) = \alpha a + \alpha b$ |

**Linear combination** of vectors $a_1, \ldots, a_m$ with scalars $\beta_1, \ldots, \beta_m$:
$$\beta_1 a_1 + \cdots + \beta_m a_m$$

- Coefficients sum to $1$ → **affine combination**
- Coefficients sum to $1$ AND all $\ge 0$ → **convex combination** (point on segment between vectors)

### Inner Product

$$a^T b = a_1 b_1 + a_2 b_2 + \cdots + a_n b_n$$

Key identities:

| Identity | Formula |
|---|---|
| Select entry $i$ | $e_i^T a = a_i$ |
| Sum of entries | $\mathbf{1}^T a = a_1 + \cdots + a_n$ |
| Mean | $(\mathbf{1}/n)^T a = \text{avg}(a)$ |
| Sum of squares | $a^T a = \|a\|^2$ |

Properties: commutative ($a^T b = b^T a$), distributive ($(a+b)^T c = a^T c + b^T c$).

### Complexity

| Operation | Flops | Memory |
|---|---|---|
| Vector addition (length $n$) | $n$ | — |
| Scalar × vector | $n$ | — |
| Inner product | $2n$ | — |
| Storage of $n$-vector | — | $8n$ bytes |

---

## 2. The Vector Class (Lab 1)

Built entirely from scratch. Every arithmetic operator creates a **new Vector object** via the constructor — important for understanding memory and constructor call counts.

```python
class Vector:
    def __init__(self, X=[]):
        self.data = [x for x in X]   # NEW list in memory
        self.n    = len(X)

    def __add__(self, other):
        if self.n != other.n: raise Exception("Vector sizes do not match")
        output = Vector(self.data)           # copy
        for i in range(self.n):
            output.data[i] += other.data[i]
        return output

    def __matmul__(self, other):             # dot product: x @ y
        output = 0.0
        for i in range(self.n):
            output += self.data[i] * other.data[i]
        return output

    def __rmul__(self, other):               # scalar * vector
        output = Vector(self.data)
        for i in range(self.n):
            output.data[i] *= other
        return output
```

**Constructor call count rule**: every `+`, `-`, `*` calls `__add__`/`__sub__`/`__mul__`, each of which calls `Vector(self.data)` once. So `3*e1 + (-2)*e2 + 4*e3` = 3 scalar mults + 2 additions = **5 constructor calls**.

**Convenience subclasses**:
```python
class zeros(Vector):
    def __init__(self, n): super().__init__([0]*n)

class ones(Vector):
    def __init__(self, n): super().__init__([1]*n)
```

**In-place operators** (don't create new objects — modify `self.data` directly):
```python
def __iadd__(self, other):      # +=
    for i in range(self.n): self.data[i] += other[i]
    return self

def __iter__(self):             # for e in v:
    for value in self.data: yield value
```

---

## 3. Inner Product — Implementation and Uses

```python
def inner_product(x, y):
    if x.n != y.n: raise Exception(...)
    total = 0
    for i in range(x.n):
        total += x.data[i] * y.data[i]
    return total

def vector_sum(x):
    """sum(x) = 1^T x"""
    ones = Vector([1 for i in range(x.n)])
    return inner_product(x, ones)
```

Run another notebook's code: `%run Matrix_Tools.ipynb` (Jupyter magic, not Python).

---

## 4. Linear and Affine Functions

A function $f : \mathbb{R}^n \to \mathbb{R}$ is **linear** if it satisfies superposition for all $x, y$ and all scalars $\alpha, \beta$:
$$f(\alpha x + \beta y) = \alpha f(x) + \beta f(y)$$

This breaks into **homogeneity** $f(\alpha x) = \alpha f(x)$ and **additivity** $f(x+y) = f(x)+f(y)$.

**Key theorem**: if $f$ is linear, there exists a unique $a$ such that $f(x) = a^T x$. The vector $a$ is found by $a_i = f(e_i)$.

**Affine function**: linear + constant:
$$f(x) = a^T x + b$$

Satisfies restricted superposition: $f((1-\theta)x + \theta y) = (1-\theta)f(x) + \theta f(y)$ (coefficients must sum to $1$). If $b \ne 0$, it is **not** linear.

**First-order Taylor approximation** — best affine approximation near point $z$:
$$\hat{f}(x) = f(z) + \nabla f(z)^T (x - z)$$

$\nabla f(z)$ is the gradient (vector of partial derivatives evaluated at $z$). Good approximation when $x$ is close to $z$.

**In-class framing** (from lecture):
- 1 variable: $\hat{y} = mx + b$ → a line
- 2 variables: $\hat{y} = m_1 x_1 + m_2 x_2 + b$ → a plane
- $n$ variables: $\hat{y} = m^T x + b$ → a hyperplane

---

## 5. Regression Model

The regression model is an affine function used to predict scalar output from feature vector input:
$$\hat{y} = x^T \beta + v$$

- $\hat{y}$ — prediction (label / dependent variable)
- $x$ — feature vector (regressors)
- $\beta$ — $n$-vector of **weights** (coefficients)
- $v$ — **offset** (intercept / bias)

Each $\beta_i$ = change in $\hat{y}$ for a 1-unit increase in $x_i$, holding all other features fixed.

**Augmented form**: let $\tilde{x} = [1,\, x]^T$ and $\tilde{\beta} = [v,\, \beta]^T$, then $\hat{y} = \tilde{x}^T \tilde{\beta}$.

```python
def f(x, beta, v):
    """Generic Linear Regression Function"""
    return inner_product(x, beta) + v
```

> **Quiz note**: $\beta_1$ corresponds to feature $x_1$ (e.g., total area), NOT the second feature. Always match subscripts carefully.

---

## 6. Boolean Vectors

Entries $\in \{0, 1\}$ where $1$ = condition true, $0$ = condition false. Alternative encoding: $\{-1, +1\}$.

- $a^T b$ for Boolean vectors = number of indices where **both** are $1$ (intersection size)
- $\|x - y\|$ = $\sqrt{\text{number of differing entries}}$ = **Hamming distance** (up to square root)

---

## Summary

| Concept | Formula |
|---|---|
| Inner product | $a^T b = \sum_i a_i b_i$ |
| Linear function | $f(x) = a^T x$ |
| Affine function | $f(x) = a^T x + b$ |
| Taylor approximation | $\hat{f}(x) = f(z) + \nabla f(z)^T(x-z)$ |
| Regression model | $\hat{y} = x^T\beta + v$ |
| Sum via dot product | $\text{sum}(x) = \mathbf{1}^T x$ |
