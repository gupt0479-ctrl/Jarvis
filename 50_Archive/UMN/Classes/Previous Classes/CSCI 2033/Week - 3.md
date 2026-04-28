---
type: class
status: archived
created: 2025-09-30
updated: 2025-12-31
area:
  - "[[Final]]"
  - "[[50_Archive/UMN/Classes/Previous Classes/CSCI 2033/Midterm - 1]]"
  - "[[Quiz]]"
tags:
  - "#class"
  - "#Textbook"
  - "#Jupyter"
  - "#Lecture"
  - "#Quiz"
  - "#Homework"
next: "[[50_Archive/UMN/Classes/Previous Classes/CSCI 2033/Week - 4|Week - 4]]"
---
# #Textbook Textbook (Ch - 3)
## 3.1 Norm
The concept of a norm provides a measure of a vector's magnitude or "length".
The **Euclidean Norm** ($\|x\|$): an n-vector x, denoted $\|x\|$, is the square root of the sum of the squares of its entries: 
$$
\|x\|= \sqrt{x_1^2+x_2^2+\cdots+x_n^2}
$$
It can also be expressed concisely as the square root of the inner product of the vector with itself: **inner product form**
$$
\|x\|= \sqrt{x^T x}
$$
The Euclidean norm is sometimes written with a subscript 2, as $\|x\|_2$. Properties of the Norm
The Euclidean norm satisfies four important properties:
1. Nonnegativity: $\|x\|\ge0$.
2. Definiteness: $\|x\|=0$ only if $x=0$. (The combination of these two is called positive definiteness.)
3. Nonnegative Homogeneity: $\|\beta x\|=|\beta|\|x\|$. Multiplying a vector by a scalar scales the norm by the absolute value of the scalar.
4. Triangle Inequality (Subadditivity): $\|x+y\|\le\|x\|+\|y\|$. The norm of a sum of two vectors is never more than the sum of their norms. (This property is proven later using the Cauchy–Schwarz inequality.)
**Note**: Any real-valued function satisfying these four properties is generally called a (general) norm, but this textbook focuses solely on the Euclidean norm.
**Norm of a Sum**: A useful formula relating the norm of a sum to the individual norms and the inner product is: 
$$
\|x+y\|^2 = \|x\|^2 + 2x^Ty + \|y\|^2
$$
This formula is derived from $\|x+y\|^2 =(x+y)^T(x+y)$.
### Root-Mean-Square (RMS) Value:
The root-mean-square (RMS) value of an n-vector x is defined as: 
$$
\text{rms}(x)= \frac{\|x\|}{\sqrt{n}} = \sqrt{\frac{x_1^2+\cdots+x_n^2}{n}}
$$
- The argument under the square root is the mean square value, denoted ms(x).
- RMS value is useful for comparing the magnitude of vectors with different dimensions (n). It represents a "typical" value of $|x_i|$
### Chebyshev Inequality
The Chebyshev inequality provides a limit on how many entries of a vector can be large relative to its RMS value. If k entries of vector x satisfy $|x_i|\ge a$ (where $a>0$), then: 
$$
k\le \frac{\|x\|^2}{a^2}
$$
or, more simply,  
$$
\frac{k}{n}\le\left(\frac{\text{rms}(x)}{a}\right)^2
$$
This inequality partially justifies the idea that the RMS value is representative of a typical entry size.
## 3.2 Distance
The Euclidean distance between two n-vectors a and b is the norm of their difference: 
$$
\text{dist}(a,b)=\|a-b\|
$$
- If a and b are two- or three-vectors, this corresponds precisely to the usual geometric distance. It is defined for vectors of any dimension.
- If the distance is small, vectors are considered "close" or "similar" (e.g., in feature distance).
- The RMS value of the difference, $\|a-b\|/\sqrt{n}$, is called the RMS deviation between a and b.
**Triangle Inequality Interpretation**: The triangle inequality, $\|a-c\|\le\|a-b\|+\|b-c\|$, gains its name from geometry, stating that the length of one side of a triangle cannot exceed the sum of the lengths of the other two sides.
**Applications**: Distance is used in various applications:
- Feature Distance: Measures how different two objects are based on their feature vectors x and y, via $\|x-y\|$.
- RMS Prediction Error: If y is an observed time series and $\hat{y}$ is its prediction, $\text{rms}(y-\hat{y})$ measures the error.
- Nearest Neighbor: Finding the vector $z_j$ in a collection that minimizes the distance $\|x-z_j\|$ to a given vector x.
- Document Dissimilarity: Using the distance between word count histogram vectors as a measure of how dissimilar two documents are.
- **Units for Heterogeneous Vector Entries**: When vector entries represent different types of quantities (heterogeneous vectors), the choice of units affects the distance calculation. It is a rule of thumb to choose units such that the numerical values of different entries have approximately the same magnitude so that they contribute equally to determining the distance.
## 3.3 Standard Deviation
Standard deviation measures how much the entries of a vector deviate from their mean value. The de-meaned vector $\tilde{x}$ of an n-vector x is formed by subtracting the mean (average) value of x from every entry:
$$
\tilde{x}=x-\text{avg}(x)\mathbf{1}
$$
The mean of the entries of $\tilde{x}$ is always zero. **Definition of Standard Deviation ($\text{std}(x)$)**: The standard deviation of x is the RMS value of the de-meaned vector: 
$$
\text{std}(x)= \frac{\|\tilde{x}\|}{\sqrt{n}} = \sqrt{\frac{(x_1-\text{avg}(x))^2+\cdots+(x_n-\text{avg}(x))^2}{n}}
$$
- A small standard deviation means the entries of x are nearly the same.
- In some applications, std(x) is called risk (e.g., when x is a return time series).
Relationship between rms, avg, and std: These three measures are related by the identity: 
$$
\text{rms}(x)^2=\text{avg}(x)^2+\text{std}(x)^2
$$
### Standardized Vector (z-scores)
The standardized version of x, denoted z, has a mean of zero and a standard deviation of one: $$
z=\frac{x-\text{avg}(x)\mathbf{1}}{\text{std}(x)}
$$
The entries $z_i$ are called the z-scores and indicate how many standard deviations $x_i$ is above or below the mean avg(x).
## 3.4 Angle
The angle between two vectors is defined using their inner product and norms.
**Cauchy–Schwarz Inequality**: A critical foundation for defining the angle is the Cauchy–Schwarz inequality: 
$$
|a^Tb|\le\|a\|\|b\|
$$
This inequality ensures that the argument of the arc cos function used in the angle definition always lies between −1 and 1.
**Angle Definition**: For two nonzero n-vectors a and b, the angle between them, θ, is defined as: 
$$
\theta=\arccos\left(\frac{a^Tb}{\|a\|\|b\|}\right)
$$
The angle θ lies in the interval [0,π].
Key Angle Cases:
- **Orthogonal**: $a⊥b$ if $a^Tb=0$ (angle is π/2 or 90°).
- Aligned: $a^Tb=\|a\|\|b\|$ (angle is 0). Each vector is a positive multiple of the other.
- Anti-aligned: $a^Tb=-\|a\|\|b\|$ (angle is π or 180°). Each vector is a negative multiple of the other.
- Acute Angle: $a^Tb>0$ (angle is less than 90°).
- Obtuse Angle: $a^Tb<0$ (angle is greater than 90°).
**Pythagorean Theorem**:If x and y are orthogonal vectors (θ=90°), the Pythagorean theorem holds: 
$$
\|x+y\|^2=\|x\|^2+\|y\|^2
$$
## **NOTE**: 
1. **Transforming between two encodings for Boolean vectors**: *Paper Hw - 1 & 2*
	**Hw 1**: A Boolean n-vector is one for which all entries are either 0 or 1. Such vectors are used to encode whether each of n conditions holds, with $a_i = 1$ meaning that condition i holds. Another common encoding of the same information uses the two values −1 and +1 for the entries. For example the Boolean vector $[0,1,1,0]^T$ would be written using this alternative encoding as $[−1,+1,+1,−1]^T$.
	A **Boolean n-vector** is simply a list (vector) of _n_ binary entries: $$x=[x1,x2,…,xn]^T$$Where each $x_i∈{0,1}$.
	- $x_i=1$ → means the condition, feature, or item _i_ is **present/true/on**.
	- $x_i=0$ → means it is **absent/false/off**.
	**Hw 2**: The norm gives the **magnitude or count of “true” entries”** — i.e., how many features are active. 
	The distance ddd measures **how many features differ** between x and y.  
	It’s exactly the **Hamming distance** (up to a square root): $d = \sqrt{\text{number of differing entries}}$
	If two sparse Boolean vectors differ only in a few active features, their **distance is small** — meaning they’re similar.

---
# #Lecture Lecture
## #Jupyter Jupyter
### Vector_Norm 
- [[Week - 1 & 2#Vector Class]] Added - __matmul__, get and set,
```python
# creating the standard basis vectors for R^3
e1 = Vector([1,0,0])
e2 = Vector([0,1,0])
e3 = Vector([0,0,1])

# computing the norm squared
e1 @ e1
# 1.0
# checking orthogonality
e1 @ e2
# 0.0
x = 3*e1 - 2*e2 + 4*e3  # create vector with linear combination
y = Vector([1,1,1])     # create vector with constructor

# Computing the sum of the components
x @ y                   # compute the dot product
# 5.0
```
2. Vector_Tools -  [[Week - 1 & 2#Vector Class]] Added -
- ```__getitem__```
    * modified to include
        * index lists
* ```__truediv__(self,other)```
    * adds functionality for division by a scalar
    * ```y = x / 5``` meaning to scale $\vec{x}$ by $\frac{1}{5}$ and save in $\vec{y}$
* ```vec_dist(self,other)```
	* computes the distance between a vector and another vector
```python
def __getitem__(self,i):
        """used to access elements via x[i] notation"""
        if type(i)==list:
            return Vector([self.data[k] for k in i])
        elif -self.n < i < self.n:
            return self.data[i]
        else:
            raise Exception("Index out of bounds")

 def __truediv__(self,other):
        """returns the vector divided by the scalar other"""
        output = Vector(self.data)           # copy current vector
        
        return output * (1.0/other)            # return the output vector

def vec_dist(self,other):
        """returns the distance between vectors self and other"""
        if self.n!=other.n: raise Exception("Dimensions do not match")
        
        out = 0.0                         # variable for distance calculation
    
        for i in range(self.n):           # loop over the vectors
            d = self[i] - other[i]        # differnce of ith components
            out += d*d                    # add the square of the distance
        return out**0.5                   # return the squareroot of the sum
```
### Exploring MNSIT 
- Import syntax - 
	- Fetch syntax -
```python
from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784', version=1, as_frame=False)
X, y = mnist.data, mnist.target
X_train, y_train = X[:60000], y[:60000]
X_test,  y_test  = X[60000:], y[60000:]
```
	- X = all images, each row = a 784-dim vector
	- y = their digit labels (0–9)
	- Split into training (60 000) + test (10 000)
- Each image = a **vector in ℝ⁷⁸⁴**, because 28 × 28 = 784 pixels.
- Convert arrays into `Vector` objects
```python
N_train = 600 
L_train = [Vector(X_train[i]) / 255 for i in range(N_train)] 
y_train = Vector(y_train[:N_train])
  
N_test = 100 
L_test  = [Vector(X_test[i]) / 255 for i in range(N_test)]
y_test  = Vector(y_test[:N_test])
```
	- The raw `numpy` rows are turned into `Vector` objects defined in earlier labs. 
	- `/255` scales pixel values (0–255) → [0, 1] so magnitudes are consistent.
	- `L_train` = list of Vector objects (each a 784-D vector).
Display Images
```python
visualization([0], L_train, y_train) 
visualization([0,1,2], L_train, y_train)`
```
You’re now looking at actual vectors from ℝ⁷⁸⁴ as images. Each black-and-white picture = one point in 784-D space.
```python
# search the data set for certain digits and display them
digit_to_find = '1'
how_many_you_want = 3

indices = []
count = 0
for i in range(len(L_train)):
    if y_train[i]==digit_to_find:
        indices.append(i)
        visualization([i],L_train,y_train)
        count += 1
        if count == how_many_you_want: break
print("indices for",digit_to_find,"=",indices)
```
- Loops through labels → find all indices where label = 4.
- Visualizes first 3 examples.
Load and Normalize a Custom Image
```python
from PIL import Image, ImageFilter 
import numpy as np  
im_frame = Image.open('six.png') 
np_frame = np.array(im_frame.getdata()) 
np_vec = np_frame[:,0] 
# normalized input vector (from image above) 
xt = Vector([1 for i in range(784)]) - (Vector(list(np_vec)) / 255)
```
- Reads your own “6” image.
- Converts → vector of 784 pixels.
- Scales to [0, 1].
- Subtracts from a “white” vector → so darker pixels → larger values.
## #Quiz Quiz
1. [[Week - 1 & 2#Regression Model]] - A linear regression model predicts an output variable $\hat{y}$ as a **linear combination** of input features:
- $x_1, x_2, \dots$: input features (e.g., total area, number of beds).
- $\beta_1, \beta_2, \dots$: coefficients (showing how sensitive $\hat{y}$ is to each feature).
- $v$: intercept term (baseline prediction).
Each coefficient $\beta_i$ represents **the expected change in $\hat{y}$** for a 1-unit increase in $x_i$, **holding all other variables constant**.
> The model parameter $\beta_1 = 148.73$ represents the amount the regression model price prediction $\hat{y}$ increases when the number of beds increases.
**Answer:** ❌ False
**Reasoning:** $\beta_1$ corresponds to the first feature $x_1$ — **total area**, not number of beds. Therefore, $\beta_1 = 148.73$ means that when the **area** increases by 1 unit (keeping number of beds fixed), the predicted price increases by 148.73 units.

1. Problem 3
> The model parameter $\beta_2 = -18.85$ represents the amount the regression model price prediction $\hat{y}$ decreases when the number of beds increases.
**Answer:** ✅ True
**Reasoning:** $\beta_2$ corresponds to $x_2$, the **number of beds**. Since $\beta_2$ is **negative**, it means: Increasing the number of beds (while keeping total area fixed) **reduces** the predicted sale price. So, the predicted price decreases by 18.85 units for each additional bed, assuming the house area remains the same.
# #Homework Coding HW
[[Week - 1 & 2#Vector Class]] - This class used in lab. 
2. Vector Projections:
	Vector projection of $\vec{b}$ onto $\vec{a}: \hspace{0.5in} \text{proj}_{\vec{a}}(\vec{b}) = \left(\frac{\vec{a}\cdot\vec{b}}{\|\vec{a}\|}\right)\frac{\vec{a}}{\|\vec{a}\|} = \left( \frac{\vec{a}\cdot\vec{b}}{\vec{a}\cdot\vec{a}} \right) \vec{a}$
	Component of $\vec{b}$ orthogonal to $\vec{a}: \hspace{0.5in} \vec{b}_{\perp \vec{a}} = \vec{b} - \text{proj}_{\vec{a}}(\vec{b})$
	Meaning
	- `parallel()` → “shadow” of self on other.
	- `perp()` → the remainder at 90° to other.
```python
class Vector2(Vector):
    """a sub-class of the class above with additional methods"""

    def parallel(self,other):
        """returns the component of self parallel to other (projection)"""
        ###################################################################
        # insert your code here
        coeff = (self @ other) / (other @ other)
        return Vector([coeff * x for x in other.data])
        
    def perp(self,other):
        """returns the component of self perpendicular to other"""
    ###################################################################
        # insert your code here
        return self - self.parallel(other)
```
3. [[#3.4 Angle]] - $$\vec{a}^T\vec{b} = \|\vec{a}\|\|\vec{b}\|\cos(\theta)$$where $\theta = \arccos\left( \frac{\vec{a}^T\vec{b}}{\|\vec{a}\|\|\vec{b}\|} \right)$ is the smaller of two angles between $\vec{a}$ and $\vec{b}$.
4. [[#Root-Mean-Square (RMS) Value]]
	[[#3.3 Standard Deviation]]
```python
 def rms(self):
        """returns the root mean square of the data"""
        ###################################################################
        # insert your code here
        total = 0
        for x in self.data:
            total += x * x
        return (total/self.n) ** 0.5
        
def mean(self):
        """returns the average(mean) of the data"""
        ###################################################################
        # insert your code here
        total = 0
        for x in self.data:
            total += x
        return total/self.n
def std(self):
        """returns the standard deviation of the data"""
        ###################################################################
        # insert your code here
        m = self.mean()
        total = 0
        for x in self.data:
            total += (x-m) * (x-m)
        return (total/self.n) ** 0.5
```
5. [[#Standardized Vector (z-scores)]]
```python
class Data1DS(Data1D):
    """a sub-class for the statistical class which includes standardization"""

    def standardize(self):
        """convert vector entries to z-score (standardized) values"""
###################################################################
        # insert your code here
        m = self.mean()
        s = self.std()
        for i in range(self.n):
            self.data[i] = (self.data[i] - m) / s
```
---