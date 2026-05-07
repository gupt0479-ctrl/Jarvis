---
type: input
input_kind: lecture
status: tree
created: 2025-10-16
source_url: "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2033/Week - 6#Jacobi method|Linear Equations]]"
related_progress:
  - "[[Final]]"
  - "[[UMN Board]]"
tags:
  - input
next: "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2033/Week - 6|Week - 6]]"
---
```python
def Jacobi(A,b):
    """Jacobi iterative method (using A = M + N), where M is diagonal of A"""
    
    M = diag([A.data[i][i] for i in range(A.m)])             # Extract Diagonal
    Minv = diag([1.0 / A.data[i][i] for i in range(A.m)])    # Invert Diagonals
    N = A - M                                                # Extract non-diagonal
    
    TOL = 1.0E-12                                            # error tolerance
    xt = Vector([random.randint(-20,20) for i in range(A.n)])# random (initial) solution
    
    #--------------iteration (for a maximum of 1000 steps)--------------
    for i in range(1000):
        
        # see https://en.wikipedia.org/wiki/Jacobi_method
        x_new = Minv @ (b - N @ xt)    # update xt (Jacobi Iteration)
    
        #--------------check for good guess--------------
        error = (A@x_new - b).norm()
        if error < TOL:
            print("-"*50)
            print("computation required",i,"steps")
            print(x_new)
            return x_new
            break
        
        xt = x_new # save the updated value
    
        #--------------debugging--------------
        if i%100==0:
            print("step",i)
            print("error:",error)
            print(xt.transpose())
```
Key pieces:
- `xt` is the current approximation $x^{(k)}$.
- `x_new` is $x^{(k+1)}$.
- `error = (A @ x_new - b).norm()` is the **residual** $\|A x^{(k+1)} - b\|$.  
    If this residual is tiny, then $x^{(k+1)}$ is a very good solution.
- `TOL = 1e-12` sets how accurate we want to be.
- The loop stops as soon as error < TOL, or after 1000 steps if it never gets that good.