---
type: concept
course: CSCI 4041
status: sprout
mastery (1/10): 3
created: 2026-04-16
topics:
  - "[[DSA]]"
  - "[[CSCI 4041 Board]]"
  - "[[10_Areas/Degree/UMN/Classes/CSCI 4041/Week - 10|Week - 10]]"
  - "[[10_Areas/Degree/UMN/Classes/CSCI 4041/Textbook/Chapter - 15]]"
related:
  - "[[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Algorithms/Dynamic Programming]]"
  - "[[HeapSort]]"
---
# [[Greedy Algorithms]]
## MOC
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Week - 10#Chapter 15 - Greedy Algorithms and Huffman Coding|Week - 10]]
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Textbook/Chapter - 15#15.1 An Activity-Selection Problem|Chapter - 15 - Activity Selection]]
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Textbook/Chapter - 15#15.3 Huffman Codes|Chapter - 15 - Huffman Codes]]
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Algorithms/Dynamic Programming#Definition|Dynamic Programming]]
- [[HeapSort#Definition|HeapSort]]

## Definition
- **Greedy algorithm**: an algorithm that commits to the locally best choice at each step and never revisits that choice.
- **Greedy-choice property**: there exists an optimal solution whose first choice is the greedy one.
- **Optimal substructure**: after making the greedy choice, the remaining work is itself an optimal solution to the remaining subproblem.
- **Prefix-free code**: a code in which no codeword is the prefix of another codeword.

## Core Ideas (Textbook)
### 15.1 Activity Selection
- Activities are interval requests on a shared resource, and the goal is to maximize the number of pairwise compatible activities.
- Once activities are sorted by finish time, the earliest-finishing compatible activity is the safe greedy choice.
- The reduced problem is the suffix of activities that start after the chosen activity finishes.

### 15.2 Elements of the Greedy Strategy
- Greedy algorithms need both greedy-choice property and optimal substructure.
- Dynamic programming solves subproblems first and then chooses; greedy chooses first and solves the residual problem afterward.
- Fractional knapsack is greedily solvable, but 0-1 knapsack is not in general.

### 15.3 Huffman Codes
- Prefix-free codes can be represented as full binary trees.
- The objective is to minimize the weighted external path length `B(T) = sum c.freq * d_T(c)`.
- The greedy rule is to combine the two least frequent nodes at every step.

### 15.4 Offline Caching
- With full future knowledge, evict the cached block whose next use is furthest in the future.
- This is another example where a local choice can be proved globally safe.

## Core Ideas (Lecture)
### Activity-selection implementations
The lecture made activity selection useful by comparing three ways to solve the same problem:
1. brute force
2. dynamic programming / memoization
3. greedy recursion

```python
def recursive_selectionGreedy(S):
    """solve the activity selection problem recursively"""
    count = 0
    solution = []
    
    def recursive_selection_GreedyR(sorted_S,i,j):
        """generic recursive solution to the Activity-Selection Problem"""
        nonlocal count,solution
        count += 1
        
        ai = sorted_S[i]

        k = i+1
        while k <= j:
            ak = sorted_S[k]
            if ai.f <= ak.s:
                solution.append(ak)
                return recursive_selection_GreedyR(sorted_S,k,j) + 1
            k+=1
        return 0
    
    sorted_S = [activity("_",0,0)] + sorted(S,key=lambda a:a.f)
    n = len(sorted_S)
    
    output = recursive_selection_GreedyR(sorted_S,0,n-1)
    
    print("total recursive calls:",count)
    return output,solution
```

The structure matters: sort by finish time, insert a dummy boundary, then repeatedly take the first compatible activity.

### Huffman coding pipeline
The Huffman notebook matters because it includes the entire encode/decode workflow:

```python
def Huffman(C):
    """performs the Huffman encoding for the set of n characters and frequencies in C"""
    sorted_heap_items = [heap_item(x[0],x[1]) for x in C]
    
    n = len(sorted_heap_items)
    Q = minheap(n,sorted_heap_items)
    
    for i in range(n-1):
        z = heap_item()
        x = Q.extract_min()
        y = Q.extract_min()
        
        z.left = x
        z.right = y
        z.key = x.key+","+y.key
        z.value = x.value + y.value
        
        Q.insert(z)
    
    return Q.extract_min()
```

```python
def get_encoder(root_node):
    """returns the encoding dictionary for the tree T"""
    Encoder = {}

    def traverse(node,string):
        nonlocal Encoder
        
        if node.left == None and node.right == None:
            Encoder[node.key] = string
        else:
            if node.left:
                traverse(node.left,string+"0")
            if node.right:
                traverse(node.right,string+"1")

    traverse(root_node,"")
    return Encoder
```

### CodingHW7 variants
- Reverse greedy for activity selection
- Room scheduling by greedy placement into rooms
- Max-value activity selection by dynamic programming
- Simplified greedy knapsack

```python
def room_scheduler(S):
    """greedy algorithm for scheduling rooms """
    solution_list = []
    sorted_S = sorted(S,key=lambda a:a.s)

    for a in sorted_S:
        placed = False
        
        for room in solution_list:
            if room[-1].f <= a.s:
                room.append(a)
                placed = True
                break
        
        if placed == False:
            solution_list.append([a])
    
    return solution_list
```

## Proof / Reasoning Toolkit
### Greedy Safety Checklist
1. Name the local choice clearly.
2. Show that some optimal solution can be modified to use that choice.
3. Show the remaining problem is still of the same form.
4. Conclude by induction on the reduced problem.

### Exchange-Argument Checklist
1. Start from an optimal solution that does not use the greedy choice.
2. Exchange part of that solution with the greedy choice.
3. Show feasibility is preserved.
4. Show the value does not get worse.

### Huffman Reasoning Checklist
1. Lowest-frequency symbols should appear deepest in the tree.
2. Pair the two minimum frequencies as siblings.
3. Contract them into one combined frequency.
4. Recurse on the smaller alphabet.

## Complexity + Tradeoffs
| Problem / Method | Time | Main Tradeoff |
| --- | --- | --- |
| Activity selection greedy | `Theta(n)` after sorting | Very simple once finish-time order is known |
| Activity-selection brute force | Exponential | Correct but impractical |
| Huffman with min-heap | `O(n lg n)` | Needs priority-queue support |
| Room scheduling greedy | Depends on room scan strategy | Easy to implement, not required to be optimal here |
| Simplified greedy knapsack | Fast, but not fully general | Good coding exercise, not full 0-1 knapsack |

## Canonical Examples (Max 5)
### 1. Earliest-finish activity selection
- **Goal:** maximize the number of compatible activities.
- **Key steps:** sort by finish time, take the first compatible one, recurse on the suffix.
- **Common mistake:** sorting by start time instead of finish time for the standard proof.

### 2. Reverse greedy activity selection
- **Goal:** choose activities from the right boundary backward.
- **Key steps:** sort by start time, choose the latest-starting compatible activity, recurse left.
- **Common mistake:** assuming the standard finish-time proof transfers automatically without checking the new boundary condition.

### 3. Room scheduling
- **Goal:** assign intervals to rooms greedily.
- **Key steps:** sort by start time, try to append to an existing room, otherwise open a new room.
- **Common mistake:** forgetting to compare against the last activity already placed in a room.

### 4. Huffman merge trace
- **Goal:** build an optimal prefix-free code.
- **Key steps:** extract two minimum-frequency nodes, join them under a new parent, reinsert.
- **Common mistake:** thinking the greedy step is "pick the two largest" because they seem most important.

### 5. Greedy versus DP boundary
- **Goal:** understand when greedy is insufficient.
- **Key steps:** compare activity selection with 0-1 knapsack.
- **Common mistake:** assuming every optimization problem with subproblems should be greedily solvable.

## Practice Map
- Interval scheduling / non-overlapping intervals
- Merge intervals versus select intervals
- Min-heap combine-cost pattern
- Simple greedy room assignment
- Huffman-style compression reasoning

## Mini-test
1. What is the greedy choice in the standard activity-selection problem?
2. Why does the activity-selection proof use finish-time order rather than start-time order?
3. What is the cost function minimized by Huffman coding?
4. Why is a min-priority queue the right data structure for Huffman?
5. Which part of the week shows that not every optimization problem should be solved greedily?

## Flashcards
#cards/CSCI4041
1. Greedy-choice property::A globally optimal solution can be built by making a locally optimal choice first.
2. Activity-selection greedy rule::Pick the compatible activity with the earliest finish time.
3. Optimal substructure::An optimal solution contains optimal solutions to the remaining subproblems.
4. Huffman local step::Combine the two minimum-frequency nodes.
5. Prefix-free code::No codeword is the prefix of another codeword.
6. Why greedy can fail::A locally best choice can block a better later combination.
7. Why Huffman uses a min-heap::Each round needs two current minimum-frequency nodes quickly.
