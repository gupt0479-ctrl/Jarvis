---
type: class
input_kind: book
status: sprout
created: 2026-04-01
updated: 2026-04-16
area:
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
tags:
  - "#class"
  - "#Textbook"
next: "[[50_Archive/UMN/Classes/CSCI 4041/Week - 10|Week - 10]]"
---
# Chapter - 15
Greedy algorithms are used for optimization problems. A greedy algorithm always makes the choice that looks best at the moment - a **locally optimal choice** - in the hope that this choice will lead to a **globally optimal solution**. Unlike [[60_Claude/20_Distilled_Notes/Dynamic Programming|dynamic programming]], greedy algorithms do not always yield optimal solutions, but for many problems they do.

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
The lecture's comparison point was greedy versus [[50_Archive/UMN/Classes/CSCI 4041/Concepts/Algorithms/Dynamic Programming#Definition|dynamic programming]].
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
- [[50_Archive/UMN/Classes/CSCI 4041/Week - 10#Chapter 15 - Greedy Algorithms and Huffman Coding|Week - 10 lecture reference]]
- [[Greedy Algorithms#Definition|Greedy Algorithms concept]]
- [[50_Archive/UMN/Classes/CSCI 4041/Concepts/Algorithms/Dynamic Programming#Definition|Dynamic Programming contrast]]
