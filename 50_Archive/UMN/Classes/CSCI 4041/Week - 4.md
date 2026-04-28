---
type: class
input_kind: lecture
status: sprout
created: 2026-02-09
updated: 2026-04-16
area:
  - "[[CSCI 4041 Board]]"
  - "[[10_UMN/CSCI 4041/CSCI 4041/Concepts/DSA|DSA]]"
  - "[[10_UMN/CSCI 4041/CSCI 4041/Concepts/Introduction to Algorithms|Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Lecture"
next: "[[50_Archive/UMN/Classes/CSCI 4041/Week - 5|Week - 5]]"
---
# Entire Week
## What you must be able to do
- [[Chapter - 7 & 10#7.1 Description of Quicksort|Chapter - 7 quicksort]], [[Chapter - 7 & 10#7.4 Analysis of Quicksort|expected-analysis lemmas]], and [[QuickSort#Proof / Reasoning Toolkit|QuickSort - Proof / Reasoning Toolkit]]: trace partition, explain the four regions, and justify why randomized quicksort is expected $Θ(n \lg n)$.
- [[Chapter - 7 & 10#10.1 Simple Array-Based Data Structures|Chapter - 10 stacks and queues]], [[Chapter - 7 & 10#10.2 Linked Lists|linked lists]], and [[Elementary Data Structures#Core Ideas (Lecture)|Elementary Data Structures - Core Ideas (Lecture)]]: implement array stacks/queues, the circular queue conditions, and the main linked-list operations.
- [[Elementary Data Structures#BST Delete — 4 Cases|Elementary Data Structures - BST Delete — 4 Cases]] and [[Chapter - 7 & 10#10.3 Representing Rooted Trees|tree representation]]: know traversals, parent pointers, successor logic, and BST delete/transplant behavior.
- [[QuickSort#Practice Map|QuickSort - Practice Map]] and [[Elementary Data Structures#Practice Map|Elementary Data Structures - Practice Map]]: quickselect/partition problems and linked-list practice are still open.

## Key ideas (textbook)
- **Quicksort is divide-and-conquer without a combine step.** The algorithm spends its work budget inside `PARTITION`, placing the pivot in its final location and recursively sorting the two sides. That makes partition correctness far more important than any top-level quicksort pseudocode summary.
- **The partition invariant is the whole story.** The tan, blue, white, and yellow regions are not just a visualization aid; they are the proof structure. If you can state what each region means before and after one iteration of the loop, you can explain why the pivot ends in the correct position.
- **Expected quicksort analysis reduces runtime to comparisons.** The lecture's three-lemma argument shows that total runtime is $O(n + X)$ where $X$ is the number of comparisons. Once you know when a pair of elements can be compared and how often, the harmonic-series bound gives the expected $Θ(n \lg n)$ result.
- **Elementary data structures are about invariants plus operations.** Stacks and queues are defined by removal policy, linked lists by pointer structure, and binary trees by parent/child references. The chapter material is basic on purpose, because later trees, heaps, and hash tables all assume you can reason about these pointer-level invariants quickly.
- **BST operations depend on two-way structure.** The `left` and `right` pointers give search direction, but the parent pointer `p` is what makes delete, successor/predecessor, and later rebalancing practical. This week is the first place where "child-to-parent" links become structurally important.

## Concepts created / updated today
- [[QuickSort#Definition|QuickSort]]
- [[Elementary Data Structures#Definition|Elementary Data Structures]]
- [[Chapter - 7 & 10#10.3 Representing Rooted Trees|Chapter - 7 & 10 - rooted trees and BST context]]

## Lecture
### Chapter 7 and Chapter 10 - Quicksort, Partitioning, and Elementary Data Structures
This week has two halves that fit together more closely than they first appear. The quicksort half is about maintaining a strong loop invariant while a pointer scans an array, and the data-structure half is about maintaining strong representation invariants while pointers or indices change over time. In both cases, the algorithm is only as good as the invariant you can describe precisely. That is why the lecture spent so much time on the four partition regions instead of only showing the top-level recursive quicksort call.

The quicksort notebooks made the partition routine feel concrete. The pivot is always the last element `A[r]`, `j` scans from left to right through the unknown region, and `i` marks the end of the `<= pivot` region. Every time `A[j] <= x`, `i` moves right and that smaller element is swapped into the tan region. If `A[j] > x`, the element is implicitly left in the blue region. That is the reason partition works in one linear pass. The expected-runtime proof then reframed the algorithm in terms of comparisons between order statistics rather than recursive calls between subarrays. The three lemmas matter because they show that runtime can be bounded by counting pairwise comparisons, and each pair can only meet once.

Chapter 10 then shifted the same style of reasoning into data structures. The stack and circular queue examples are intentionally simple, but they force you to pay attention to representation conditions like "when is this structure empty?" and "how do we tell full from empty?" CodingHW3 added the more exam-relevant variants: two stacks in one array, deque operations on a circular array, linked-stack and linked-queue implementations, and iterative list reversal. The BST portion of lecture then gave the first serious tree mutation example through delete and transplant. The critical insight there is that transplant only reconnects a subtree at the parent boundary; it does not magically repair the deleted node's left or right child pointers for you. That is why successor-based deletion has to be handled in very specific cases.

### Jupyter Notebook Explanations
#### Ch7_QuickSort.ipynb
This notebook contains the core partition logic used all week.

```python
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1
```

The key to explaining this function is the meaning of `i`. It is not the pivot index and it is not "the current element." It is the last slot of the tan region, the part of the array already known to be `<= x`. The loop advances `j` through the white region, and only when the current value belongs on the tan side does `i` advance and a swap occur. The final pivot swap is therefore not a random cleanup step. It places the pivot immediately after all values known to be `<= x`.

#### Ch7_QuickSort-Visualization.ipynb and Ch7_QuickSort-Recursion-Tree.ipynb
These two notebooks turned the same algorithm into pictures:
- The visualization notebook animates tan, blue, white, and yellow regions so the loop invariant is visible instead of abstract.
- The recursion-tree notebook compares worst-case, balanced, and 9:1 split shapes to show that logarithmic height survives any constant-factor shrink on the larger subproblem.

#### Ch7_QuickSort(AlgorithmicModifcationExamples).ipynb
This notebook is where the lecture's practical quicksort changes came from.

```python
# median-of-3 idea
pivot = median(A[p], A[(p + r) // 2], A[r])
```

The point here was not a new asymptotic bound. It was that smarter pivot selection improves constants and real behavior on already structured inputs. The same notebook also introduced three-way partitioning so that all-equal arrays stop degenerating into repeated 0:n-1 splits.

#### Ch10_Stacks_and_Queues.ipynb
This notebook kept the structure definitions simple on purpose:

```python
# array stack
top = -1
# push: top += 1; A[top] = x
# pop:  if top == -1 -> underflow
```

```python
# circular queue
# empty: head == tail
# full: (tail + 1) % n == head
```

The one wasted slot in the queue is the main point to remember. Without it, the structure would need an extra counter or flag to distinguish full from empty.

#### Ch10_LinkedLists.ipynb and CodingHW_3(chapter10-CLRS).ipynb
The linked-list notebook plus CodingHW3 generated most of the implementation details we care about this week.

```python
prev, curr = None, head
while curr:
    nxt = curr.next
    curr.next = prev
    prev, curr = curr, nxt
return prev
```

This reverse routine is worth keeping because it is the cleanest pointer-manipulation invariant of the week: after each iteration, `prev` is the head of the reversed prefix and `curr` is the head of the unreversed suffix.

CodingHW3 also added:
- two stacks in one array with `l_top = -1`, `r_top = n`, overflow when `l_top + 1 == r_top`
- deque support on the circular array queue
- linked-stack via prepend/remove-head
- linked-queue with an explicit tail pointer so both enqueue and dequeue stay $O(1)$

#### Ch10_BinaryTree.ipynb
This notebook introduced the BST node structure and the deletion cases.

```python
class node:
    def __init__(self, k=None, parent=None, left_child=None, right_child=None):
        self.key = k
        self.p = parent
        self.left = left_child
        self.right = right_child
```

```python
def in_order(T, node):
    if node:
        in_order(T, node.left)
        print(node.key)
        in_order(T, node.right)
```

The in-order traversal matters because it gives sorted output if and only if the BST property still holds. The delete discussion then used the four-case breakdown:
- no left child
- no right child
- two children with successor equal to the right child
- two children with successor deeper in the right subtree

## Examples worth keeping
- **Partition trace:** `[3,7,8,5,2,1,9,5,4]` with pivot `4` ends one partition step as `[3,2,1,4,7,8,5,9,5]`.
- **All-equal quicksort failure:** ordinary partition makes one side contain every non-pivot element, which is why three-way partition is useful.
- **Circular queue invariant:** `head == tail` means empty, while `(tail + 1) % n == head` means full.
- **Two stacks in one array:** left stack grows right, right stack grows left, and real overflow occurs only when the two tops meet.
- **BST successor example:** deleting 67 when the right child is 89 but 89 has a left child 77 means 77 replaces 67, not 89.

## Takeaways (questions to resolve)
- [ ] Why can no two order statistics be compared more than once in randomized quicksort?
- [ ] What exactly do the tan, blue, white, and yellow regions represent at one fixed iteration of partition?
- [ ] Why does a circular queue waste one slot instead of using all n positions?
- [ ] Why is a parent pointer so useful for delete and later balanced-tree rebalancing?
- [ ] In BST delete, when is the successor not the direct right child?

## Flashcards
#cards/CSCI4041
1. What does the partition index `i` represent::The last position in the region known to contain elements `<= pivot`.
2. What is the worst-case quicksort recurrence::$T(n)=T(n-1)+T(0)+Θ(n)$.
3. Why is expected quicksort runtime analyzed through comparisons::Because total runtime is $O(n+X)$ where X is the number of comparisons.
4. Circular queue empty condition::`head == tail`.
5. Circular queue full condition::`(tail + 1) % n == head`.
6. What does `TRANSPLANT(u, v)` do::It replaces the subtree at u with v at the parent boundary and updates `v.p` if needed.
7. Why does in-order traversal matter in a BST::Because it prints the keys in sorted order when the BST property is correct.
