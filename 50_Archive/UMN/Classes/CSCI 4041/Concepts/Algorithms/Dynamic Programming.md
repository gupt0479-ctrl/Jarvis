---
type: concept
course: CSCI 4041
status: seed
mastery (1/10): 0
created: 2026-03-25
topics:
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[Introduction to Algorithms]]"
  - "[[Chapter - 14]]"
related:
  - "[[50_Archive/UMN/Classes/CSCI 4041/Week - 9|Week - 9]]"
---
# [[50_Archive/UMN/Classes/CSCI 4041/Concepts/Algorithms/Dynamic Programming]]
## MOC
- [[50_Archive/UMN/Classes/CSCI 4041/Week - 9#Chapter 14 - Dynamic Programming|Week - 9]]
- [[Chapter - 14#14.1 Rod Cutting|Chapter - 14 - Rod Cutting]]
- [[Chapter - 14#14.4 Longest Common Subsequence (LCS)|Chapter - 14 - LCS]]
- [[Divide and Conquer#Definition|Divide and Conquer]]
- [[Greedy Algorithms#Definition|Greedy Algorithms]]

## Definition
- **Dynamic programming (DP)**: solve a problem by solving overlapping subproblems once each and storing the answers.
- **Optimal substructure**: an optimal solution contains optimal solutions to the relevant subproblems.
- **Overlapping subproblems**: the recursion revisits the same subproblems repeatedly.
- **Memoization**: top-down recursion plus a cache.
- **Bottom-up**: fill a table from smallest subproblems upward.

## Core Ideas (Textbook)
### 14.1 Rod Cutting
- Revenue recurrence: `r_n = max_{1 <= i <= n}(p_i + r_{n-i})`, with `r_0 = 0`.
- Naive recursion is exponential because subproblems repeat.
- Memoized and bottom-up versions run in `Theta(n^2)`.

### 14.2 Matrix-Chain Multiplication
- Choose a split `k` and minimize the scalar multiplication cost.
- `m[i,j] = min(m[i,k] + m[k+1,j] + p_{i-1}p_kp_j)`.
- Fill by increasing chain length.

### 14.3 Elements of DP
- Optimal substructure plus overlapping subproblems are the two hallmarks.
- Cut-and-paste is the standard proof technique for optimal substructure.
- Divide-and-conquer usually does not revisit the same subproblems enough to need a DP table.

### 14.4 LCS
- If the last symbols match, extend the subsequence.
- If not, take the better of deleting one symbol from either string.
- Time `Theta(mn)`.

### 14.5 Optimal BST
- Choose the root that minimizes expected search cost.
- Time `Theta(n^3)`, space `Theta(n^2)`.

## Core Ideas (Lecture)
### Fibonacci implementations

```python
def FibRecursive(n):
    """naive (recursive) implementation of the Fibonacci sequence"""
    if n==0: return 0
    if n==1: return 1
    return FibRecursive(n-2) + FibRecursive(n-1)
```

```python
def FibMemoize(n):
    """Memoized implementation of the Fibonacci sequence"""
    F = {}
    F[0] = 0
    F[1] = 1
    
    def FibMemR(n):
        nonlocal F
        if n in F:
            return F[n]

        if n-2 in F:
            A = F[n-2]
        else:
            A = FibMemR(n-2)
            F[n-2] = A
        
        if n-1 in F:
            B = F[n-1]
        else:
            B = FibMemR(n-1)
            F[n-1] = B
        
        return A + B

    return FibMemR(n)
```

```python
def FibBottomUp(n):
    """Bottom-Up implementation of the Fibonacci sequence"""
    if n==0: return 0
    if n==1: return 1
    
    A = 0
    B = 1
    for i in range(2,n+1):
        F = A + B
        A = B
        B = F
    return F
```

```python
def FibBottomUp2(n):
    """Bottom-Up implementation of the Fibonacci sequence"""
    F = [0 for i in range(n+2)]
    F[1] = 1
    
    for i in range(2,n+1):
        F[i] = F[i-1] + F[i-2]
    return F[n]
```

The lecture uses Fibonacci to show the full DP arc: exponential recursion, memoized top-down, bottom-up with constant space, and bottom-up with full table retention.

### Knapsack notebook

```python
class item:
    """these are the items to steal"""

    def __init__(self,name="",size=1,value=1):
        """construct an item to steal"""
        self.name = "x_"+str(name)
        self.size = size
        self.value = value

    def __str__(self):
        """printing utililty"""
        out = str(self.name) + "  |  (" + str(self.size) + "," + str(self.value) + ")"
        return out
```

```python
def generate_item_set(N,M):
    """generates a set of items to use for a Knapsack problem of size N,M"""
    Items = []
    for i in range(N):
        if N < 27:
            name = chr(ord('A')+i)
        else:
            name = str(i)
        
        size = random.randrange(1,M)
        value = random.randrange(M,2*M)
        Items.append(item( name , size , value ))
    return Items
```

```python
def re_construct(Items,best,M,N):
    """Re-constructs the sub-set based on the best array of sub-choices"""
    slack = M
    row = N-1
    
    max_combDP = []
    
    for row in range(N-1,-1,-1):
        idx = best[row][slack]
        if idx != None:
            x = Items[idx]
            if x not in max_combDP:
                max_combDP.append(x)
                slack = slack - x.size

    max_scoreDP = sum(x.value for x in max_combDP)
    max_sizeDP = sum(x.size for x in max_combDP)
    
    print("-"*100)
    print("Max score:",max_scoreDP)
    print("Knapsack Size:",max_sizeDP,"<=",M)
    print("\nOptimal sub-set:")
    for x in max_combDP:
        print(x)
    
    return max_scoreDP, max_sizeDP, max_combDP
```

The lecture contrast here is crucial: brute force checks all `2^N` subsets, greedy can fail, and the DP table `dp[k][slack]` is what systematically preserves the optimal answer.

## Proof / Reasoning Toolkit
### Cut-and-Paste Checklist
1. Assume an optimal solution contains a non-optimal subproblem solution.
2. Replace that subproblem solution with the optimal one.
3. Show the overall solution gets no worse.
4. Conclude the subproblem inside an optimal solution must itself be optimal.

### DP Design Checklist
1. Define the subproblem state.
2. Write the recurrence.
3. Identify base cases.
4. Decide memoized top-down or bottom-up order.
5. If needed, store reconstruction data.

## Complexity + Tradeoffs
| Problem | Time | Space |
| --- | --- | --- |
| Fibonacci naive recursion | `O(2^n)` | recursion stack |
| Fibonacci memoized | `Theta(n)` | table plus stack |
| Fibonacci bottom-up | `Theta(n)` | `O(1)` or `Theta(n)` depending on whether the full table is kept |
| Rod cutting | `Theta(n^2)` | `Theta(n)` or table-based |
| LCS | `Theta(mn)` | `Theta(mn)` |
| 0-1 knapsack DP | `O(NM)` | `O(NM)` |

## Canonical Examples (Max 5)
### 1. Fibonacci explosion
- **Goal:** show why memoization matters.
- **Key steps:** naive recursion repeats `F(2)`, `F(3)`, and other subproblems many times.
- **Common mistake:** thinking recursion alone makes something dynamic programming.

### 2. Bottom-up Fibonacci
- **Goal:** keep only the needed history.
- **Key steps:** track the previous two values.
- **Common mistake:** keeping a full table when only the final value is needed.

### 3. Greedy knapsack failure
- **Goal:** show why DP is needed for 0-1 knapsack.
- **Key steps:** compare one large locally attractive item against a better later combination.
- **Common mistake:** assuming value-to-weight or size-first greedy rules always work.

### 4. Rod cutting
- **Goal:** maximize revenue from cuts.
- **Key steps:** try the first cut at every position and combine with the optimal remainder.
- **Common mistake:** forgetting the "no cut" option embedded in the recurrence.

### 5. LCS
- **Goal:** compute longest common subsequence, not substring.
- **Key steps:** match case extends diagonal, mismatch case takes max of left/up.
- **Common mistake:** treating adjacency in the strings as required.

## Practice Map
- Fibonacci-style 1D DP
- Knapsack / capacity DP
- LCS / 2D DP
- Rod cutting / unbounded-choice DP
- State-definition practice

## Mini-test
1. What are the two hallmarks of a DP problem?
2. Why is naive Fibonacci exponential?
3. What is the role of the `best` reconstruction table in knapsack?
4. Why does greedy fail for general 0-1 knapsack?
5. How does bottom-up order correspond to a topological order of the subproblem graph?

## Flashcards
#cards/CSCI4041
1. Two hallmarks of DP::Optimal substructure and overlapping subproblems.
2. Memoization::Top-down recursion plus a cache.
3. Bottom-up DP::Solve smallest subproblems first and fill a table forward.
4. Rod-cutting recurrence::`r_n = max_{1 <= i <= n}(p_i + r_{n-i})`.
5. LCS match case::`c[i,j] = c[i-1,j-1] + 1`.
6. Knapsack time complexity::`O(NM)` pseudo-polynomial.
7. DP versus divide-and-conquer::DP revisits and stores overlapping subproblems; divide-and-conquer usually does not.
