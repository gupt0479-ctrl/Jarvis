---
type: class
input_kind: lecture
status: sprout
created: 2026-01-22
updated: 2026-04-16
area:
  - "[[CSCI 2041 Board]]"
  - "[[DSA]]"
  - "[[Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Lecture"
next: "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 3|Week - 3]]"
---
# Entire Week
## What you must be able to do
- [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 1 & 2#1.1 Algorithms|Chapter 1.1]] and [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 1 & 2#1.2 Algorithms as a Technology|Chapter 1.2]]: explain the difference between a computational problem, a problem instance, an algorithm, and algorithmic correctness, and explain why asymptotic growth matters more than raw hardware for large inputs.
- [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 1 & 2#2.1 Insertion Sort|Chapter 2.1]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 1 & 2#2.2 Analyzing Algorithms|Chapter 2.2]], and [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 1 & 2#2.3 Designing Algorithms|Chapter 2.3]]: prove correctness with loop invariants, distinguish best/worst/average case, and derive `T(n) = 2T(n/2) + Theta(n)` for merge sort.
- [[Sorting Algorithms#Core Ideas (Lecture)|Sorting Algorithms - Core Ideas (Lecture)]], [[Sorting Algorithms#Proof / Reasoning Toolkit|Sorting Algorithms - Proof / Reasoning Toolkit]], and [[Time Complexity#Definition|Time Complexity]]: compare the three insertion-sort variants, explain the FLOPS notebook's chosen cost model, and justify the merge-sort recursion-tree solution.
- [[Sorting Algorithms#Practice Map|Sorting Algorithms - Practice Map]]: connect the week's theory to concrete implementation practice such as insertion sort, merging sorted arrays, and hybrid merge-sort tuning.

## Key ideas (textbook)
- **1.1 Algorithms**: The chapter starts by separating the *problem* from the *procedure*. A computational problem specifies the input-output relationship, an instance is one concrete valid input, and an algorithm is one exact method for producing the output. Correctness means the algorithm halts and returns the right answer for every valid instance, which becomes the standard the course uses for all later data structures and graph algorithms.
- **1.2 Algorithms as a Technology**: This section makes the course's biggest framing point early: time and memory are limited resources, so asymptotic growth matters. Insertion sort grows like `n^2`, merge sort grows like `n lg n`, and that difference eventually overwhelms even very large constant-factor hardware advantages. The textbook's machine comparison is there to teach that algorithm design is not separate from systems performance; it is part of systems performance.
- **2.1 Insertion Sort**: Insertion sort is the first full algorithm analyzed for both correctness and runtime. Its central invariant is that the prefix already processed is sorted, and the body of the loop inserts the next key into that sorted prefix by shifting larger elements right. It is in-place, stable in the standard version, and especially good for small or nearly sorted inputs.
- **2.2 Analyzing Algorithms**: The RAM model treats primitive operations as constant-cost steps so we can reason about growth cleanly. Best case, worst case, and average case all describe the same algorithm under different input arrangements. The key simplification is order of growth: once the dominant term is identified, lower-order terms and constants no longer control the long-run behavior.
- **2.3 Designing Algorithms**: Divide-and-conquer introduces the main recursive design pattern used for the rest of the course. Merge sort splits the array into halves, recursively solves the halves, and merges in linear time. That yields the recurrence `T(n) = 2T(n/2) + Theta(n)`, and the recursion-tree argument shows why the algorithm runs in `Theta(n lg n)`.

## Concepts created / updated today
- [[Sorting Algorithms#Definition|Sorting Algorithms]]
- [[Sorting Algorithms#Core Ideas (Lecture)|Sorting Algorithms - lecture implementation notes]]
- [[Sorting Algorithms#Complexity + Tradeoffs|Sorting Algorithms - complexity and tradeoffs]]
- [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 1 & 2#2.3 Designing Algorithms|Chapter - 1 & 2 - merge sort and divide-and-conquer]]

## Lecture
### Chapter 1 and Chapter 2 - Insertion Sort, Cost Models, and Merge Sort
Week 1 itself was mostly orientation, course logistics, and syllabus changes. The real course content began in Week 2, and the important thing about that lecture was that it was not really "a week about insertion sort only." It was a week about how this class wants you to think. The professor used Chapter 2 to connect three different layers at once: the textbook algorithm, the implementation details of actual Python code, and the cost model used to analyze the implementation. That is why the week keeps bouncing between proofs, code, and runtime discussion. The algorithm is not just an abstract procedure. It lives inside a data structure, and the data structure changes what one "step" actually costs.

Insertion sort was the first place this became obvious. The CLRS in-place version mostly performs comparisons plus array writes like `A[j+1] = A[j]`, which is close to the RAM-model picture from the textbook. But the lecture also compared two Python-oriented alternatives: one version uses `list.pop(i)` and `list.insert(j, x)`, and another version builds a separate `sorted_array`. All three still feel like insertion sort at the idea level, yet they do different concrete work. The `pop` / `insert` version pays for shifting elements in the Python list representation, and the separate-array version pays `Theta(n)` extra memory. That comparison is one of the main "source of truth" ideas from the week: the same algorithmic idea can have different real costs depending on the representation.

The FLOPS notebook made this explicit. The `cost += ...` lines are not measuring actual CPU time. They are counting a chosen unit of primitive work. That is why the notebook comments distinguish the link-based interpretation from the array-based interpretation of the same insertion operation. If middle insertion were happening in a linked structure, the location update could be counted as constant once the node is found. In a Python list, the same logical insertion shifts later elements, so the array-based comments use terms like `n-i` or `n-(j+1)` to show the extra cost directly. Merge sort then supplied the week's main divide-and-conquer pattern: split the problem, recurse, and combine. The list-based `merge_list` implementation showed a very Python-specific design choice: it fills the output array from right to left and repeatedly pops from the end of the input lists because end pops are cheap. Homework 1 then turned this into a practical optimization question: if insertion sort has a small constant factor on tiny inputs, when should merge sort stop recursing and switch over? That is where the hybrid formula `Theta(nk + n lg(n/k))` enters the story.

### Jupyter Notebook Explanations
#### Ch2_Insertion_Sort.ipynb
This notebook isolates insertion sort in the clearest possible form before the asymptotic experiments. It is the best place to understand what the sorted-prefix invariant actually looks like in code.

```python
def insertion_sort(A,n):
    """sorts the array A (in-place) using the insertion sort algorithm from CLRS-ch2"""

    for i in range(1,n):
        # (Loop Invariant)
        # the elements in positions 0 to i-1 are sorted (start at 1)
        print(A[:i])

        key = A[i]                  # current element

        j = i-1
        while j>=0 and A[j]>key:    # walk back to find insertion point
            A[j+1] = A[j]           # copy element
            j = j-1                 # move back

        A[j+1] = key                # insert ith element (key) into position j+1
```

The code comments are already doing part of the proof. Before iteration `i`, the prefix `A[:i]` is supposed to be sorted. The loop stores the current key, moves every larger entry one slot to the right, then writes the key exactly once into the gap that remains. That is why the invariant is preserved. This is also the cleanest version to analyze in a RAM-style model because the operations are visible as comparisons and writes.

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

This version is useful because it exposes a different tradeoff. The search for the insertion position is still linear, and the call to `sorted_array.insert(k, key)` still shifts elements, so the runtime remains quadratic. But the algorithm is not in-place anymore because it keeps a second list alive for the whole run. That distinction matters when comparing algorithms later in the course.

#### ch2_Asymptotic_Analysis.ipynb
This notebook is where the lecture moves from "one insertion sort" to "multiple implementations of the same idea."

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

This still behaves like insertion sort conceptually, but the actual operations are now `pop(i)` and `insert(j+1, key)`. On a Python list, both middle operations can shift many elements. So the lecture's point is not that this stops being insertion sort; it is that the implementation has different concrete costs than the CLRS version.

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

    return output       # reference to new array with combined values

def merge_sort_list(A,n):
    """sorts the array A using the merge sort algorithm"""

    if n < 2:    # base case
        return A

    q = int(n/2) # split point
    L = merge_sort_list(A[:q],q)    # recursive case (left)
    R = merge_sort_list(A[q:],n-q)  # recursive case (right)

    return merge_list(L,R)          # combine partial solutions
```

This is the week's most important merge-sort implementation. The merge step stays linear because it removes items from the ends of the lists, and end pops are cheap in Python. But `A[:q]` and `A[q:]` allocate fresh sublists, so the memory story is much more visible than it is in the CLRS array-based wrapper.

#### ch2_Asymptotic_Analysis-FLOPS.ipynb
This notebook is where the course starts teaching cost models, not just code.

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

The comments are the key lesson. The notebook is making you decide what "one unit of work" means. If the structure is link-based, the insertion or removal itself can be treated as constant after the search. If the structure is array-based, the shift work is visible and must be counted. This is why the notebook matters: it teaches that asymptotic analysis depends on an explicit model, not vague intuition about speed.

#### CodingHW_1(chapter2-CLRS).ipynb
Homework 1 turns the week's theory into a practical algorithm-engineering question.

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
    L = merge_coarse(A[:q], q, k)        # left half sorted list
    R = merge_coarse(A[q:], n - q, k)    # right half sorted list

    # merge
    return merge_list(L, R)
```

The idea is to stop the merge-sort recursion once a subproblem is "small enough" and use insertion sort there instead. If the leaf size is `k`, then there are about `n/k` leaves, each costing `Theta(k^2)` to insertion-sort, which gives `Theta(nk)` total leaf work. Above those leaves, merge sort still contributes `Theta(n lg(n/k))`. So the total cost is
$$
Theta(nk + n lg(n/k)).
$$
This is one of the first places in the course where asymptotic analysis and implementation tuning are intentionally connected.

## Examples worth keeping
- **Sorting instance**: `⟨31,41,59,26,41,58⟩ -> ⟨26,31,41,41,58,59⟩`. This is the cleanest reminder of problem versus instance versus output requirement.
- **Three insertion-sort variants**: CLRS in-place, Python `pop` / `insert`, and Joy's separate-array version all represent the same high-level idea but not the same concrete cost.
- **FLOPS interpretation change**: the notebook's `cost += 1` versus `cost += n-i` comments show how the underlying data structure changes the model.
- **Merge-sort recursion tree**: level cost `cn`, height `lg n + 1`, total `cn(lg n + 1) = Theta(n lg n)`.
- **Hybrid sort threshold**: `Theta(nk + n lg(n/k))`, with `k = Theta(lg n)` preserving `Theta(n lg n)`.

## Takeaways (questions to resolve)
- [ ] Why is the CLRS in-place insertion sort the cleanest version for both correctness proofs and RAM-model analysis?
- [ ] What exactly is being counted in the FLOPS notebook, and what is intentionally not being counted?
- [ ] Why does Joy's `merge_list` fill from right to left instead of from left to right?
- [ ] How does the loop-invariant proof pattern for insertion sort compare to the proofs for `SUM-ARRAY` and Linear Search?
- [ ] Why does `k = Theta(lg n)` keep the hybrid merge sort asymptotically optimal?

## Flashcards
#cards/CSCI4041
1. What is an algorithm in this course's framing::A well-defined computational procedure that maps valid input instances to outputs and halts.
2. What is a problem instance::One concrete valid input to the computational problem.
3. Why is CLRS insertion sort in-place::It uses only a constant number of extra variables outside the array.
4. What does the FLOPS notebook measure::A chosen primitive-operation count, not wall-clock time.
5. Why can `insertion_sort_python` be slower than the CLRS version::Middle `pop` and `insert` on Python lists shift elements.
6. What is the merge-sort recurrence::`T(n) = 2T(n/2) + Theta(n)`.
7. What is the hybrid merge-sort cost from Homework 1::`Theta(nk + n lg(n/k))`.
