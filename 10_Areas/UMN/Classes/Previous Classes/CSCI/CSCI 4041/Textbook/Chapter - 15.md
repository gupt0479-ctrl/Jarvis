---
type: class
input_kind: book
status: sprout
created: 2026-04-01
updated: 2026-04-28
area:
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Textbook"
next: "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 10|Week - 10]]"
---
# Chapter - 15
Greedy algorithms are used for optimization problems. A greedy algorithm always makes the choice that looks best at the moment - a **locally optimal choice** - in the hope that this choice will lead to a **globally optimal solution**. Unlike [[60_Jarvis/20_Distilled_Notes/Dynamic Programming|dynamic programming]], greedy algorithms do not always yield optimal solutions, but for many problems they do.

## 15.1 An Activity-Selection Problem
The goal is to schedule a maximum-size set of mutually compatible activities that require exclusive use of a common resource.
1. *Problem Definition*
	- **Input:** A set `S = {a_1, a_2, ..., a_n}` of `n` activities.
	- **Attributes:** Each activity `a_i` has a start time `s_i` and finish time `f_i`, where `0 <= s_i < f_i < inf`.
	- **Compatibility:** Two activities are compatible if their intervals do not overlap.
	- **Assumption:** Activities are sorted by increasing finish time.
2. *The Greedy Choice*
	The greedy strategy is to always choose the activity that **finishes first**, since it leaves the most remaining room for future activities.
	- After choosing the earliest-finishing compatible activity, the problem reduces to selecting from activities that start after its finish time.
> [!NOTE] **Indexing Note:** The textbook uses **1-origin indexing** for activities and introduces a fictitious activity `a_0` with `f_0 = 0`. In code, the lecture uses 0-indexed Python lists and often inserts explicit dummy activities at the front and back.
3. *Algorithms*
	- **RECURSIVE-ACTIVITY-SELECTOR(s, f, k, n)** recursively finds the first compatible activity after `a_k`.
	- **GREEDY-ACTIVITY-SELECTOR(s, f, n)** is the iterative `Theta(n)` version once the activities are finish-time sorted.

### Lecture Emphasis
The lecture did not present activity selection as a single black-box greedy proof. It compared three perspectives:
1. **Brute force**
	- Enumerate feasible compatible subsets and keep the largest one.
	- Correct, but combinatorial and too slow.
2. **Dynamic programming / memoization**
	- Use dummy boundary activities and recursively split around a valid intermediate choice.
	- Good for showing optimal substructure explicitly.
3. **Greedy recursion**
	- Once activities are sorted by finish time, choose the earliest activity compatible with the current boundary.
	- This is the lecture's central greedy example because the local earliest-finish choice can be proved safe.

```python
class activity:
    """these are the activites to schedule"""

    def __init__(self,name="",start = 0,finish = 0):
        """construct an activity to schedule"""
        self.name = "a_"+str(name)
        self.s = start
        self.f = finish

    def __str__(self):
        """printing utililty"""
        out = str(self.name) + "\t\t|\ttime slot: [" + str(self.s) + "," + str(self.f) + ")"
        return out
```

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

The important structural detail is that the lecture builds a sorted list with a dummy start activity. The greedy recursion then scans rightward until it finds the first activity whose start time does not conflict with the current chosen activity. That first compatible activity is the greedy choice.

### CodingHW7 Extensions
Coding Homework 7 pushes the standard activity-selection problem in several directions:
- **15.1-1 Reconstruct the DP solution:** store reconstruction data so the actual chosen activities can be recovered, not just the count.
- **15.1-2 Reverse greedy:** choose the last-starting compatible activity from the right side rather than the earliest-finishing from the left.
- **15.1-4 Room scheduling:** greedily assign activities into a list of rooms. This is not required to be optimal; the point is implementation practice.
- **15.1-5 Max-value activity selection:** change the score from "number of activities" to total value and solve it with dynamic programming.

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

## 15.2 Elements of the Greedy Strategy
A greedy algorithm is appropriate if a problem has the following two properties:
1. *Greedy-Choice Property:* You can assemble a globally optimal solution by making locally optimal choices.
	- **Greedy vs. DP:** Dynamic programming usually solves subproblems first and then chooses. Greedy makes the choice first and only then solves what remains.
2. *Optimal Substructure*
	An optimal solution to the whole problem contains optimal solutions to the subproblems left behind after the greedy choice.
3. *Knapsack Problems*
	- **0-1 Knapsack:** Cannot take fractions of items, so greedy does not solve the general problem.
	- **Fractional Knapsack:** Greedy works by taking the highest value-per-weight item first.

### Lecture Emphasis
The lecture's comparison point was greedy versus [[Dynamic Programming#Definition|dynamic programming]].
- In activity selection, a dynamic program can be written and understood, but the greedy solution is dramatically simpler once the safe choice is proved.
- In 0-1 knapsack, greedy fails because the locally best immediate choice can block a better combination later.
- In the **simplified** CodingHW7 `{0,1}` knapsack exercise, the greedy code sorts items by size and fills until full. That is an implementation exercise, not a proof that greedy solves the full knapsack problem.

```python
def knapsack_simple(Items,M):
    """Solve the Knapsack problem for the set of Items and total capacity M (using Dynamic Programming)"""
    solution = []

    sorted_Items = sorted(Items,key=lambda x:x.size)
    current_size = 0

    for x in sorted_Items:
        if current_size + x.size <= M:
            solution.append(x)
            current_size += x.size
        else:
            break
    
    return solution
```

## 15.3 Huffman Codes
Huffman codes are an efficient way to compress data by using variable-length bit sequences to encode characters.
1. *Prefix-Free Codes*
	A **prefix-free code** is one where no codeword is a prefix of any other codeword. This is what makes decoding unambiguous.
2. *Representation*
	Prefix-free codes are represented as **full binary trees**.
	- **Leaves:** characters and their frequencies.
	- **Path:** left edges contribute `0`, right edges contribute `1`.
	- **Depth:** the depth of a leaf is the length of its codeword.
3. *Cost Function*
	The number of bits required to encode a file is
	$$
	B(T) = \sum_{c \in C} c.freq \cdot d_T(c).
	$$
4. *The Huffman Algorithm*
	Huffman's algorithm builds the optimal tree from the bottom up.
	1. Put all characters into a min-priority queue keyed by frequency.
	2. Extract the two minimum-frequency nodes.
	3. Create a new parent node whose frequency is their sum.
	4. Insert the parent back into the queue.
	5. Repeat until one root remains.
	**Complexity:** With a binary min-heap, `O(n lg n)`.

### Lecture Emphasis
The lecture notebook is useful because it shows the whole pipeline: count character frequencies, build the tree, derive the encoder, compress a string, and decode it back.

```python
def make_C(s):
    """converts a string s to a (sorted) list of tuples of characters and counts"""
    freq = {}
    
    total_bits = 0
    total_chars = 0
    for c in s:
        total_chars += 1
        total_bits += 8
        
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    
    print("total number of bits used:",total_bits)
    print("total characters:",total_chars)
    C = list(reversed(sorted(list(freq.items()),key=lambda x:x[1])))
    return C
```

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

```python
def uncompress(root_node,compressed_format):
    """decode the encoded string 'encoding' which uses the Huffman code from tree T"""
    out = ""
    node = root_node
    
    for bit in compressed_format:
        if node.right == None and node.left == None:
            out += node.key
            node = root_node
        
        if bit=="1":
            node = node.right
        elif bit=="0":
            node = node.left
    
    if node.right == None and node.left == None:
        out += node.key
    return out
```

## 15.4 Offline Caching
This section applies greedy strategies to memory management.
1. *Problem Definition*
	- A cache can hold `k` blocks.
	- The system receives a sequence of memory requests.
	- **Cache hit:** block already present.
	- **Cache miss:** block absent; if the cache is full, some block must be evicted.
2. *Furthest-In-Future Strategy*
	If the full future request sequence is known in advance, evict the block whose next use occurs furthest in the future.
3. *Correctness*
	- The problem has optimal substructure.
	- The furthest-in-future choice is safe and leads to an optimal offline strategy.

## Summary Links
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 10#Chapter 15 - Greedy Algorithms and Huffman Coding|Week - 10 lecture reference]]
- [[Greedy Algorithms#Definition|Greedy Algorithms concept]]
- [[Dynamic Programming#Definition|Dynamic Programming contrast]]

---

## Overview
- Chapter 15 studies optimization problems where a locally safe choice can be made before solving the remaining subproblem.
- In CSCI 4041, the major lecture examples are activity selection and Huffman coding, with homework variants that contrast greedy, DP, and scheduling implementations.
- The chapter's central skill is proving that a greedy choice is safe; speed alone does not make an algorithm correct.

## Core Definitions
- **Greedy-choice property:** some optimal solution begins with the greedy choice.
- **Optimal substructure:** after committing to the greedy choice, the remaining problem has the same form.
- **Exchange argument:** transform an optimal solution into one that uses the greedy choice without worsening its value.
- **Prefix-free code:** no codeword is a prefix of another.
- **Huffman tree:** full binary tree minimizing weighted external path length.
- **Offline caching:** cache replacement with full knowledge of future requests.

## Main Algorithms
- Recursive and iterative activity selection after sorting by finish time.
- Dynamic-programming activity selection used as contrast in lecture/homework.
- Huffman coding using a min-priority queue.
- Offline caching by evicting the item whose next request is furthest in the future.
- Homework-supported variants: reverse greedy activity selection, room scheduling, max-value activity selection, and simplified greedy knapsack.

## Correctness Ideas
- Activity selection uses an exchange argument: replacing the first activity in an optimal solution with the earliest-finishing compatible activity leaves at least as much room.
- Huffman correctness uses the fact that the two least frequent symbols can be made siblings at maximum depth, then contracted.
- Greedy proofs must name the local choice and prove it is safe; examples alone are not proofs.
- Greedy and DP both use optimal substructure, but DP solves subproblems before choosing while greedy chooses before solving the residual problem.

## Complexity
- Activity selection is `Theta(n)` after activities are sorted by finish time; sorting costs `O(n lg n)` if needed.
- Huffman coding with a binary min-heap is `O(n lg n)`.
- Offline caching can be implemented efficiently with future-use information, but the proof idea matters more than implementation in this course note.
- Greedy algorithms often have low runtime, but correctness depends on the problem structure.

## Lecture Emphasis
- `Lectures/Week - 10/Ch15_GreedyAlgorithms(ActivitySelectionProblem).ipynb` compares brute force, DP/memoization, and greedy recursion.

```python
sorted_S = [activity("_",0,0)] + sorted(S,key=lambda a:a.f)
```

- The dummy boundary activity in lecture is the Python bridge to the textbook's fictitious `a_0`.
- `Lectures/Week - 10/Ch15_GreedyAlgorithms(HuffmanCoding).ipynb` uses a min-heap to repeatedly merge the two least frequent nodes:

```python
x = Q.extract_min()
y = Q.extract_min()
z.left, z.right = x, y
z.value = x.value + y.value
Q.insert(z)
```

- `Lectures/Week - 10/Ch6_Ch12(required_for_Huffman).ipynb` is the heap prerequisite needed by the Huffman implementation.
- `Homework/Coding/CodingHW_7(chapter15-CLRS).ipynb` grounds reverse greedy, room scheduling, and solution reconstruction practice.
- Weekly/concept links: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 10|Week - 10]], [[Greedy Algorithms|Greedy Algorithms]], [[Dynamic Programming|Dynamic Programming]].

## Examples
- Activity selection: choose the compatible activity with the earliest finish time, then recurse on activities starting after it.
- Huffman: if frequencies are `5, 9, 12, 13, 16, 45`, the first merge combines `5` and `9`.
- Offline caching: evict the cached item whose next use lies furthest in the future.

## Connections
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 10|Week - 10]]
- [[Greedy Algorithms|Greedy Algorithms]]
- [[Dynamic Programming|Dynamic Programming]]
- [[HeapSort|HeapSort]] for the priority queue used by Huffman.
- Source homework read: `Homework/Coding/CodingHW_7(chapter15-CLRS).ipynb` and `Homework/Paper/Paper HW - 7 (Ch - 15).pdf`.
- TODO: source gap - no vault Homework/Paper Homework note exists for direct wikilinking.

## Common Pitfalls
- Sorting activity selection by start time instead of finish time.
- Proving greedy with a few examples instead of a safety/exchange argument.
- Assuming 0-1 knapsack is greedily solvable because fractional knapsack is.
- Merging largest frequencies first in Huffman.
- Forgetting that Huffman needs a prefix-free code tree.

## Review Checklist
- [ ] State the greedy-choice property and optimal substructure.
- [ ] Prove activity selection with an exchange argument.
- [ ] Trace Huffman coding with a min-priority queue.
- [ ] Explain when greedy differs from dynamic programming.
- [ ] Identify a greedy rule and prove or disprove its safety.
