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
## 1. Vectors

A **vector** is an ordered finite list of numbers, written vertically as a column or horizontally in parentheses. An **$n$-vector** $x$ has $n$ entries indexed $x_1, x_2, \ldots, x_n$ (from $1$ to $n$ in textbook notation; Python uses $0$ to $n-1$).

**Notation reminders**
- Two vectors are **equal** if they have the same size and every corresponding entry is equal.
- **Subvector / slice**: $x_{r:s}$ denotes the entries from index $r$ through $s$.
- **Stacked vector**: $(a, b)$ is a single longer vector formed by writing $a$ then $b$.

### Sparsity
A vector is **sparse** when many of its entries are zero. The number of nonzero entries is written $\text{nnz}(x)$. Unit vectors $e_i$ (one $1$, rest zeros) are the canonical sparse vectors.

### Vector addition and scalar multiplication
Addition is defined only for vectors of the **same size** — add corresponding entries. Subtraction works the same way.

**Properties** (all hold for vectors $a, b, c$ and scalars $\alpha, \beta$):

| Property | Statement |
|---|---|
| Commutativity | $a + b = b + a$ |
| Associativity | $(a + b) + c = a + (b + c)$ |
| Zero vector | $a + \mathbf{0} = a$ |
| Scalar associativity | $\alpha(\beta a) = (\alpha\beta)a$ |
| Scalar distributivity | $(\alpha + \beta)a = \alpha a + \beta a$ and $\alpha(a + b) = \alpha a + \alpha b$ |

### Linear combinations
A **linear combination** of vectors $a_1, \ldots, a_m$ with coefficients $\beta_1, \ldots, \beta_m$ is:
$$\beta_1 a_1 + \cdots + \beta_m a_m$$

- If the coefficients sum to $1$ it is an **affine combination**.
- If additionally $0 \le \beta_i \le 1$ for all $i$ it is a **convex combination** (a point on the segment between the vectors).

### Inner product
The **inner product** (dot product) of two $n$-vectors $a$ and $b$ is the scalar:
$$a^T b = a_1 b_1 + a_2 b_2 + \cdots + a_n b_n$$

**Key identities**

| Identity | Formula |
|---|---|
| Select entry $i$ | $e_i^T a = a_i$ |
| Sum of entries | $\mathbf{1}^T a = a_1 + \cdots + a_n$ |
| Average | $(\mathbf{1}/n)^T a = \text{avg}(a)$ |
| Sum of squares | $a^T a = a_1^2 + \cdots + a_n^2$ |

**Properties**: commutativity $a^T b = b^T a$; associativity with scalar $(\gamma a)^T b = \gamma(a^T b)$; distributivity $(a+b)^T c = a^T c + b^T c$.

```python
def inner_product(x, y):
    """accumulate the sum products of corresponding elements from x and y"""
    if x.n != y.n:
        raise Exception("Vector sizes do not match")
    total = 0
    for i in range(x.n):
        total += x.data[i] * y.data[i]
    return total
```

### Complexity of vector operations

| Operation | Cost |
|---|---|
| Vector addition (length $n$) | $n$ flops |
| Scalar-vector multiplication | $n$ flops |
| Inner product | $2n$ flops |
| Memory for an $n$-vector | $8n$ bytes |

---

## 2. The Vector Class in Python

The `Vector` class stores components in a Python list `self.data` of length `self.n`. Operator overloading (`__add__`, `__sub__`, `__mul__`, `__rmul__`, `__matmul__`) lets you write natural math syntax directly.

Important pattern — every arithmetic method **creates a new Vector** via the constructor. So `3*e1 + (-2)*e2 + 4*e3` calls the constructor **5 times** (3 scalar multiplications + 2 additions).

```python
class Vector:
    def __init__(self, X=[]):
        self.data = [x for x in X]
        self.n = len(X)

    def __matmul__(self, other):
        """dot product: x @ y"""
        output = 0.0
        for i in range(self.n):
            output += self.data[i] * other.data[i]
        return output
```

Convenience subclasses built from `Vector`:

```python
class zeros(Vector):
    def __init__(self, n):
        super().__init__([0] * n)

class ones(Vector):
    def __init__(self, n):
        super().__init__([1] * n)
```

In-place operators `+=`, `-=`, `*=` use `__iadd__`, `__isub__`, `__imul__` — they modify `self.data` directly and return `self`, avoiding a new object.

---

## 3. Linear and Affine Functions

### Linearity and superposition
A scalar-valued function $f : \mathbb{R}^n \to \mathbb{R}$ is **linear** if it satisfies the **superposition property** for all vectors $x, y$ and all scalars $\alpha, \beta$:
$$f(\alpha x + \beta y) = \alpha f(x) + \beta f(y)$$

This breaks into two smaller conditions: **homogeneity** $f(\alpha x) = \alpha f(x)$ and **additivity** $f(x+y) = f(x)+f(y)$.

**Key fact**: if $f$ is linear, there exists a unique vector $a$ such that:
$$f(x) = a^T x \qquad \text{for all } x$$
The vector $a$ is found by $a_i = f(e_i)$, evaluating $f$ at each standard unit vector.

### Affine functions
An **affine function** adds a constant offset $b$ to a linear function:
$$f(x) = a^T x + b$$

- If $b \ne 0$, the function is **not** linear in the strict mathematical sense.
- It satisfies a restricted superposition: $f((1-\theta)x + \theta y) = (1-\theta)f(x) + \theta f(y)$ (coefficients must sum to 1).
- Parameters are uniquely determined by $b = f(0)$ and $a_i = f(e_i) - f(0)$.

### First-order Taylor approximation
For a differentiable function $f : \mathbb{R}^n \to \mathbb{R}$, the best affine approximation near a point $z$ is:
$$\hat{f}(x) = f(z) + \nabla f(z)^T (x - z)$$

$\nabla f(z)$ is the **gradient** (vector of partial derivatives $\partial f / \partial x_i$ evaluated at $z$). The approximation is very good when $x$ is close to $z$, and is an affine function of $x$.

---

## 4. The Regression Model

The **regression model** is the most common affine function in data science. Given a feature vector $x \in \mathbb{R}^n$, it predicts a scalar $\hat{y}$:
$$\hat{y} = x^T \beta + v$$

- $\hat{y}$ — predicted value (label / dependent variable)
- $x$ — feature vector (regressors)
- $\beta$ — $n$-vector of **weights** (coefficients)
- $v$ — **offset** (intercept)

Each coefficient $\beta_i$ gives the change in $\hat{y}$ for a 1-unit increase in $x_i$ while keeping all other features fixed.

The model can be simplified by **augmenting**: let $\tilde{x} = [1, x]^T$ and $\tilde{\beta} = [v, \beta]^T$, so $\hat{y} = \tilde{x}^T \tilde{\beta}$.

```python
def f(x, beta, v):
    """Generic Linear Regression Function"""
    return inner_product(x, beta) + v
```

**Lecture note (multi-variable form)**:
- 1-variable: $\hat{y} = m x + b$ (a line in 2D)
- 2-variable: $\hat{y} = m_1 x_1 + m_2 x_2 + b$ (a plane in 3D)
- $n$-variable: $\hat{y} = m_1 x_1 + \cdots + m_n x_n + b$ (a hyperplane)

---

## 5. Boolean Vectors and Applications

A **Boolean $n$-vector** has entries $x_i \in \{0, 1\}$ where $1$ means a condition is true/active and $0$ means it is false/off. An alternative encoding uses $\{-1, +1\}$ — so $[0,1,1,0]^T$ becomes $[-1,+1,+1,-1]^T$.

The inner product $a^T b$ of two Boolean vectors counts the number of indices where **both** entries are $1$ (the intersection size).

---

## Summary of key formulas

| Concept | Formula |
|---|---|
| Inner product | $a^T b = \sum_{i=1}^n a_i b_i$ |
| Linear function | $f(x) = a^T x$ |
| Affine function | $f(x) = a^T x + b$ |
| Taylor approximation | $\hat{f}(x) = f(z) + \nabla f(z)^T(x-z)$ |
| Regression model | $\hat{y} = x^T \beta + v$ |
| Vector sum via dot product | $\text{sum}(x) = \mathbf{1}^T x$ |
