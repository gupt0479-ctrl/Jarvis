---
type: class
input_kind: book
status: tree
created: 2026-01-27
updated: 2026-04-16
area:
  - "[[UMN Board]]"
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[Sorting Algorithms]]"
  - "[[Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Textbook"
next: "[[50_Archive/UMN/Classes/CSCI 4041/Week - 1 & 2|Week - 1 & 2]]"
---
# CLRS (Ch - 1 & 2)
## The Role of Algorithms in Computing
### 1.1 Algorithms
An **algorithm** is informally defined as any **well-defined computational procedure** that takes a value (or set of values) as **input** and produces a value (or set of values) as **output**. Essentially, it is a sequence of computational steps that transform the input into the output.
1. **Algorithms as Tools for Problem Solving**
	An algorithm can be viewed as a tool for solving a **well-specified computational problem**. The problem statement defines the general desired relationship between the input and output, while the algorithm describes a specific procedure to achieve that relationship.
	- *Instance of a Problem:* A problem **instance** consists of the specific input (satisfying any constraints imposed by the problem statement) needed to compute a solution.
	- *Example: The Sorting Problem.*
		- **Input:** A sequence of n numbers `⟨a1, a2, ..., an⟩`.
		- **Output:** A permutation (reordering) `⟨a1', a2', ..., an'⟩` of the input such that `a1' <= a2' <= ... <= an'`.
		- **Example Instance:** Given `⟨31,41,59,26,41,58⟩`, a correct algorithm returns `⟨26,31,41,41,58,59⟩`.
2. **Correctness and Specification**
	- *Correctness:* An algorithm is **correct** if, for every input instance, it **halts** (finishes in finite time) and outputs the correct solution.
	- *Incorrect Algorithms:* An incorrect algorithm might not halt at all or might halt with a wrong answer. These can still be useful if their **error rate is controllable**, such as algorithms for finding large prime numbers (Chapter 31).
	- *Specification Formats:* Algorithms can be specified in **English**, as a **computer program**, or as a **hardware design**. The only requirement is a precise description of the procedure.
3. **Kinds of Problems Solved by Algorithms**
	Algorithms are ubiquitous and essential for various fields:
	1. *Human Genome Project:* Identifying 30,000 genes and 3 billion chemical base pairs in human DNA requires sophisticated algorithms for data analysis and sequence similarity (for example, dynamic programming in Chapter 14).
	2. *The Internet:* Managing massive data volumes relies on algorithms for **routing** and **search engines**.
	3. *Electronic Commerce:* Privacy and authentication depend on public-key cryptography and digital signatures.
	4. *Resource Allocation:* Commercial enterprises use linear programming to maximize profit or minimize cost.
	5. *Shortest Paths:* Finding the shortest route between two points on a map is modeled as a graph problem.
	6. *Mechanical Design:* Listing parts in an order so that every prerequisite part appears first is topological sorting.
	7. *Clustering:* Doctors use clustering algorithms to classify tumors as cancerous or benign.
	8. *Data Compression:* Algorithms like Huffman coding shrink files to use less space.
	9. *Signal Processing:* FFT converts signals from time domain to frequency domain.
4. **Data Structures and Techniques**
	*Data Structures:* A way to store and organize data to facilitate access and modifications. No single data structure works for all purposes, so understanding strengths and limitations is part of algorithm design.
	*Hard Problems (NP-Complete):* These are problems for which no efficient algorithm is known, and no proof yet says one cannot exist.
	- *Example:* The traveling-salesperson problem is NP-complete.
	- *Consequence:* If you can classify a problem as NP-complete, you often stop searching for a perfect efficient exact algorithm and instead build an approximation algorithm.
5. **Alternative Computing Models**
	*Parallelism:* Modern multicore computers act like several sequential computers on one chip. To benefit, we need task-parallel algorithms.
	*Online Algorithms:* Some problems receive inputs over time and must act without seeing the future, such as job scheduling or emergency-room triage.

### 1.2 Algorithms as a Technology
If computers were infinitely fast and memory were free, any correct method would suffice, provided it followed good software engineering. However, **computing time and memory are bounded resources**.
1. **Efficiency**
	Different algorithms for the same problem differ dramatically in efficiency.
	*Example:* **Sorting** `n` items.
	- **Insertion Sort:** Takes time roughly equal to `c_1 n^2`, where `c_1` is a constant.
	- **Logarithm (`lg n`):** In computer science, `lg n` usually means `log_2 n`.
	- **Merge Sort:** Takes time roughly equal to `c_2 n log_2 n`.
	- **Rate of Growth:** For small inputs, insertion sort is often faster due to a smaller constant factor. Once `n` becomes large enough, the `lg n` factor in merge sort makes it more efficient than the extra `n` factor in insertion sort.
		- *Example:* If `n = 1,000`, then `lg n` is about 10. If `n = 1,000,000`, then `lg n` is about 20. The logarithm grows slowly, so merge sort scales far better.
	- **Crossover Point:** There is always a point where merge sort becomes faster than insertion sort, regardless of constant factors.
	**Hardware versus algorithms**
	- **Computer A (Fast):** Executes 10 billion instructions per second and runs insertion sort at about `2n^2` instructions.
	- **Computer B (Slow):** Executes 10 million instructions per second and runs merge sort at about `50 n lg n` instructions.
	- **Sorting 10 million numbers:**
		- **Computer A:** More than 5.5 hours.
		- **Computer B:** Less than 20 minutes.
		- **Conclusion:** A slower asymptotic growth rate can dominate huge hardware disadvantages.
2. **Algorithms in Contemporary Systems**
	Algorithms should be treated as a **technology** alongside fast hardware, GUIs, and networking. They are part of:
	- GUIs
	- Networking
	- Compilers and assemblers
	- Machine learning
	- Data science
	A strong algorithmic foundation is one of the clearest markers of a skilled programmer.

## Getting Started
### 2.1 Insertion Sort
This section introduces the **sorting problem**, defined as:
- **Input:** A sequence of `n` numbers `⟨a_1, a_2, ..., a_n⟩`.
- **Output:** A permutation `⟨a'_1, a'_2, ..., a'_n⟩` of the input such that `a'_1 <= a'_2 <= ... <= a'_n`.

**Key Terminology:**
- *Keys:* The numbers to be sorted.
- *Satellite Data:* Other data associated with a key.
- *Record:* The combination of a key and its satellite data.
- *In-place:* An algorithm is in-place if only a constant number of elements are stored outside the input array at any time.

**The Algorithm:** Insertion sort works like sorting a hand of cards. You pick up one card at a time and insert it into the proper place among the cards already sorted.

**Loop Invariants and Correctness:** The textbook invariant is:
> At the start of each iteration of the `for` loop, the subarray `A[1:i-1]` consists of the elements originally in `A[1:i-1]`, but in sorted order.

You must show:
1. *Initialization:* Before the first iteration, the invariant is true.
2. *Maintenance:* If it is true before one iteration, it remains true before the next.
3. *Termination:* When the loop ends, the invariant implies the whole array is sorted.

```python
# CLRS version

def insertion_sort(A,n):
    """sorts the array A (in-place) using the insertion sort algorithm from CLRS ch2"""
    for i in range(1,n):
        # (Loop Invariant)
        # the elements in positions 0 to i-1 are sorted (start at 1)
        #print(A[:i])

        key = A[i]                  # current element
        j = i-1
        while j>=0 and A[j]>key:    # walk back to find insertion point
            A[j+1] = A[j]           # copy element
            j = j-1                 # move back
        A[j+1] = key                # insert ith element (key) into position j+1
    return A
```

#### Lecture Emphasis
Lecture treated [[Sorting Algorithms#Definition|sorting algorithms]] as implementation families, not just one pseudocode block.
1. **CLRS in-place insertion sort**
	- Uses direct array reads and writes.
	- Keeps `O(1)` extra space.
	- Matches the RAM-model analysis most closely because the inner loop is just comparisons and shifts.
2. **`insertion_sort_python`**
	- Uses `list.pop(i)` and `list.insert(j+1, key)`.
	- Preserves the same high-level insertion-sort idea, but middle edits on Python lists shift elements.
	- The lecture used this version to show that the data structure changes the hidden cost model.
3. **`insertion_sort_Joy`**
	- Builds a separate `sorted_array`.
	- Still does insertion-sort logic, but it is no longer in-place and uses `Theta(n)` extra space.
	- This is the cleanest example of "same algorithmic idea, different implementation tradeoffs."

```python
def insertion_sort_python(A,n):
    """sorts the array A (in-place) using the insertion sort algorithm from CLRS-ch2"""

    for i in range(1,n):
        # (Loop Invariant)
        # the elements in positions 0 to i-1 are sorted (start at 1)
        #print(A[:i])

        key = A.pop(i)               # pop current element

        j = i-1
        while j>=0 and A[j]>key:    # walk back to find insertion point
            j = j-1                 # move back

        A.insert(j+1,key)           # insert ith element (key) into position j+1

    return A
```

```python
def insertion_sort_Joy(A,n):
    """simpler insertion sort (not in place)"""

    sorted_array = [A[0]]          # array to hold sorted values

    for i in range(1,n):                  # this loop runs n times
        key = A[i]                        # remove current value from A -O(1)

        k = 0
        while k < i:                      # find insertion point in sorted array -O(n)
            if sorted_array[k]>key: break
            k += 1
        sorted_array.insert(k,key)        # this operation is O(n)

    return sorted_array
```

#### CLRS Exercise Proofs
##### SUM-ARRAY
Consider:
```text
SUM-ARRAY(A, n)
    sum = 0
    for i = 1 to n
        sum = sum + A[i]
    return sum
```

**Loop invariant:** At the start of each iteration with index `i`, `sum` equals the sum of the first `i-1` entries:
$$
sum = \sum_{k=1}^{i-1} A[k].
$$

**Initialization:** Before the first iteration, `i = 1`, so the sum of the first `0` elements is `0`. The algorithm sets `sum = 0`, so the invariant is true.

**Maintenance:** Assume the invariant is true at the start of iteration `i`. After the statement `sum = sum + A[i]`, we have
$$
sum = \sum_{k=1}^{i} A[k].
$$
That is exactly the statement needed for the start of the next iteration.

**Termination:** After the loop ends,
$$
sum = \sum_{k=1}^{n} A[k],
$$
so the returned value is the sum of the whole array.

##### Linear Search
Consider:
```text
LINEAR-SEARCH(A, n, v)
    for j = 1 to n
        if A[j] == v
            return j
    return NIL
```

**Loop invariant:** At the start of iteration `j`, the value `v` does not occur in `A[1..j-1]`.

**Initialization:** Before the first iteration, `j = 1` and the prefix `A[1..0]` is empty, so the claim is true.

**Maintenance:** Assume the invariant holds at the start of iteration `j`. If `A[j] == v`, the algorithm correctly returns `j`. Otherwise `A[j] != v`, so after checking position `j`, the value `v` is still absent from `A[1..j]`. Therefore the invariant holds for the next iteration.

**Termination:** If the algorithm returns during the loop, it returns a correct index. If the loop finishes and returns `NIL`, then by the invariant `v` was not present in any checked position, so `NIL` is correct.

> [!summary] Insertion Sort: Time Complexity
> **Best:** `Theta(n)` when the input is already sorted
> **Average:** `Theta(n^2)`
> **Worst:** `Theta(n^2)` when the input is reverse sorted
> **Space:** `O(1)` extra for the in-place version
> **Stable:** Yes for the standard implementation

### 2.2 Analyzing Algorithms
Analyzing an algorithm means predicting the resources it requires, most often **computational time**.
1. **The RAM Model:** Analysis assumes a **Random-Access Machine (RAM)** model where instructions execute one after another with no concurrency.
	- *Constant Time:* Basic instructions and data accesses take constant time.
	- *Data Types:* Includes integer, floating point, and character.
	- *Word Size:* For inputs of size `n`, integers are represented with enough bits to index the input.
2. **Running Time Analysis:** Running time is the number of instructions and data accesses executed, expressed as a function of input size.
	- *Best Case:* For insertion sort, already sorted input gives `Theta(n)`.
	- *Worst Case:* Reverse-sorted input gives `Theta(n^2)`.
	- *Average Case:* For insertion sort, still `Theta(n^2)`.
3. **Order of Growth:** We focus on the leading term, ignoring constant coefficients and lower-order terms.
	- **Theta notation:** Indicates a tight asymptotic bound.

#### Lecture Emphasis
The FLOPS notebook sharpened the difference between [[Time Complexity#Definition|asymptotic growth]] and a chosen cost model.
1. **`cost += ...` is not wall-clock timing**
	- The notebook is not timing Python execution.
	- It is counting an abstract number of primitive operations.
2. **Data structure changes the count**
	- For the same insertion-sort logic, a linked-list interpretation can count middle insertion as `O(1)` once the location is known.
	- An array-based interpretation must count the element shifts.
3. **Merge sort looks cheaper in the chosen model**
	- The merge routines pay linear combine work per recursion level.
	- Insertion sort pays cumulative shift work that grows quadratically on many inputs.

```python
def insertion_sort_python_cost(A,n):
    """sorts the array A (in-place) using the insertion sort algorithm from CLRS-ch2"""
    cost = 0

    for i in range(1,n):
        # (Loop Invariant)
        # the elements in positions 0 to i-1 are sorted (start at 1)
        #print(A[:i])

        key = A.pop(i)               # pop current element
        cost += 1       # this is the cost for link-based structures
        #cost += n-i    # this is the cost for array-based structures

        j = i-1
        cost += 1

        while j>=0 and A[j]>key:    # walk back to find insertion point
            j = j-1                 # move back
            cost += 1

        A.insert(j+1,key)           # insert ith element (key) into position j+1
        cost += 1        # this is the cost for link-based -O(1)
        #cost += n-(j+1) # this is the cost for array-based -O(length)

    return A,cost
```

> [!summary] Cost-Model Takeaway
> The lecture's main point was not only that insertion sort is `Theta(n^2)`, but that the hidden work inside one "step" depends on the operations your data structure actually performs.

### 2.3 Designing Algorithms
While insertion sort uses an **incremental** approach, this section introduces the **divide-and-conquer** method.
1. **Divide** the problem into one or more smaller subproblems.
2. **Conquer** the subproblems by solving them recursively.
3. **Combine** the solutions if needed.

### Merge Sort
- **Divide:** Split the `n`-element sequence into two `n/2` subsequences.
- **Conquer:** Recursively sort the two halves.
- **Combine:** Use `MERGE` to combine two sorted subarrays in `Theta(n)` time.

```python
# CLRS version

def merge(A,p,q,r):
    """merges the two bits between p and r"""
    nl = q-p+1
    nr = r-q
    L = [ A[p+i]   for i in range(nl) ] # left half
    R = [ A[q+j+1] for j in range(nr) ] # right half
    i,j = 0,0 # start locations in L and R
    k = p     # fill location in k
    while i < nl and j < nr:
        if L[i]<=R[j]:    # check for lower value
            A[k] = L[i]   # merge lower value (from L) to A
            i+=1          # move L forward
        else:
            A[k] = R[j]   # merge lower value (from R) to A
            j+=1          # move R forward
        k+=1
    ############################# only one of the loops below should run
    while i<nl:         # copy any remaining part of L
        A[k] = L[i]
        i+=1
        k+=1
    while j<nr:         # copy any remaining part of R
        A[k] = R[j]
        j+=1
        k+=1

def merge_sort2(A,p,r):
    """sorts the array A using the merge sort algorithm"""
    if p>=r:               # base case
        return
    q = int((p+r)/2)       # split point
    merge_sort2(A,p,q)     # recursive case (left)
    merge_sort2(A,q+1,r)   # recursive case (right)
    merge(A,p,q,r)         # combine partial solutions

def merge_sort(A,n):
    """wrapper function for merge sort to have the same args"""
    merge_sort2(A,0,n-1)
    return A
```

1. **Analyzing Divide-and-Conquer (Recurrences):**
	- A recurrence equation describes the overall running time in terms of smaller inputs.
	- **Merge sort recurrence:** `T(n) = 2T(n/2) + Theta(n)`
	- **Solution:** Merge sort has worst-case running time `Theta(n lg n)`.

#### Lecture Emphasis
Lecture paired the CLRS in-place merge sort with Joy's list-based version from [[Sorting Algorithms#Core Ideas (Lecture)|Sorting Algorithms]].
1. **`merge_list` uses end pops**
	- It compares `A[-1]` and `B[-1]`.
	- It fills the output from right to left.
	- End pops on Python lists are cheap, so the merge step stays linear.
2. **`merge_sort_list` uses slicing**
	- `A[:q]` and `A[q:]` create fresh sublists.
	- The algorithm is still `Theta(n lg n)` in time, but its memory behavior is more visible than the array-based wrapper.
3. **Homework coarsening**
	- The hybrid merge sort stops the recursion at a threshold `k` and uses insertion sort on the leaves.
	- This is the first explicit example of tuning an asymptotically good algorithm using a small-input optimization.

```python
def merge_list(A,B):
    """merges lists A and B (assuming they are each in order)"""

    N = len(A)+len(B)
    output = [None for i in range(N)]   # space requirement O( |A| + |B| )

    k = N-1  # location to copy to
    while A and B:
        if A[-1] > B[-1]:               # load output from the back
            key = A.pop()               # remove from A
        else:
            key = B.pop()               # remove from B
        output[k] = key
        k-=1
    ######################## empty A or B when they are the only one left
    while A:
        key = A.pop()
        output[k] = key
        k-=1
    while B:
        key = B.pop()
        output[k] = key
        k-=1

    return output
```

#### Merge Sort Recursion Tree
For merge sort,
$$
T(n) = 2T(n/2) + cn.
$$

The lecture recursion-tree argument goes in three clean steps:
1. **Height**
	- At depth `k`, subproblem size is `n / 2^k`.
	- The base case occurs when `n / 2^k = 1`.
	- Therefore `2^k = n`, so `k = lg n`.
	- Counting the root level and leaf level gives `lg n + 1` total levels.
2. **Cost per level**
	- At level `i`, there are `2^i` subproblems of size `n / 2^i`.
	- The combine work at that level is
	$$
	2^i \cdot c(n / 2^i) = cn.
	$$
	- So every level contributes the same linear amount.
3. **Total**
	- There are `lg n + 1` levels, each costing `cn`.
	- Total cost:
	$$
	cn(lg n + 1).
	$$
	- Therefore,
	$$
	T(n) = Theta(n lg n).
	$$

#### Hybrid Coarsening from Paper HW 1 Q4
The coding and paper homework use a hybrid merge sort:

```python
def merge_coarse(A,n,k=8):
    """sorts the array A using the merge sort algorithm with insertion sort for leaf cases of size less than k"""

    # base cases
    if n < 2:
        return A[:]
    if n <= k:
        return insertion_sort_python(A[:], n)   # sort a copy using insertion sort

    # recursive case
    q = int(n/2)
    L = merge_coarse(A[:q], q, k)
    R = merge_coarse(A[q:], n - q, k)

    # merge
    return merge_list(L, R)
```

If there are `n/k` leaf subproblems and each insertion-sorted leaf of size `k` costs `Theta(k^2)`, then:
- Total leaf work is `Theta((n/k) * k^2) = Theta(nk)`.
- The merge phase still has `lg(n/k)` levels, each costing `Theta(n)`.
- Total merge work is `Theta(n lg(n/k))`.

So the hybrid total is
$$
Theta(nk + n lg(n/k)).
$$
Choosing `k = Theta(lg n)` keeps the total at `Theta(n lg n)` while using insertion sort where its constants are most favorable.

> [!summary] Merge Sort (CLRS): Time Complexity
> **Best/Average/Worst:** `Theta(n log n)`
> **Space:** `Theta(n)` extra for temporary arrays or sliced sublists
> **Stable:** Yes for the usual merge implementation
