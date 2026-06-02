---
type: class
input_kind: lecture
status: sprout
created:
updated: 2026-04-16
area:
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Concepts/Introduction to Algorithms]]"
tags:
next: []
---
# Entire Week
## What you must be able to do
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 15#15.1 An Activity-Selection Problem|Chapter 15.1]], [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 15#15.2 Elements of the Greedy Strategy|Chapter 15.2]], and [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 15#15.3 Huffman Codes|Chapter 15.3]]: explain greedy-choice property, optimal substructure, activity selection, and Huffman coding.
- [[Greedy Algorithms#Core Ideas (Textbook)|Greedy Algorithms - Core Ideas (Textbook)]], [[Greedy Algorithms#Core Ideas (Lecture)|Greedy Algorithms - Core Ideas (Lecture)]], and [[Dynamic Programming#Definition|Dynamic Programming]]: compare greedy reasoning against dynamic programming and say when the greedy shortcut is valid.
- [[Greedy Algorithms#Canonical Examples (Max 5)|Greedy Algorithms - Canonical Examples]]: trace earliest-finish activity selection, Huffman tree construction, room scheduling, and the greedy failure boundary around knapsack-style problems.
- [[Greedy Algorithms#Practice Map|Greedy Algorithms - Practice Map]]: map the week's material to interval scheduling, min-heap combination patterns, and greedy proof patterns.

## Key ideas (textbook)
- **15.1 Activity Selection**: The optimization goal is to choose a maximum-size subset of pairwise compatible activities. Once activities are sorted by finish time, the earliest-finishing compatible activity is the safe greedy choice because it leaves the maximum room for all later choices. The lecture reinforces this by comparing brute force, dynamic programming, and greedy versions of the same problem.
- **15.2 Greedy Strategy**: A greedy algorithm is appropriate when the problem has both the greedy-choice property and optimal substructure. This week keeps contrasting that with [[Dynamic Programming#Definition|dynamic programming]]: DP solves subproblems first and then chooses, while greedy chooses first and only solves what remains.
- **15.3 Huffman Codes**: Huffman coding builds an optimal prefix-free code by repeatedly combining the two least frequent symbols. The cost function is the frequency-weighted sum of codeword lengths, so low-frequency symbols should be deeper in the tree. This is why the implementation naturally uses a min-priority queue.
- **15.4 Offline Caching**: The furthest-in-future rule shows that greedy thinking extends beyond intervals and compression. If the full future is known, evicting the block used furthest in the future is the safe local choice.

## Concepts created / updated today
- [[Greedy Algorithms#Definition|Greedy Algorithms]]
- [[Greedy Algorithms#Core Ideas (Lecture)|Greedy Algorithms - lecture details]]
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 15#15.3 Huffman Codes|Chapter - 15 - Huffman Codes]]

## Lecture
### Chapter 15 - Greedy Algorithms and Huffman Coding
This week is where the course starts separating "I can write a recurrence" from "I can justify a safe local choice." That is the conceptual jump from [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 9#Chapter 14 - Dynamic Programming|Week - 9 dynamic programming]] into greedy algorithms. The professor uses activity selection as the main example because it lets you see three viewpoints on the same problem. First, you can brute-force it by checking feasible compatible subsets. Second, you can write a dynamic program using dummy start and end activities and recursively optimize over all valid intermediate choices. Third, once the activities are sorted by finish time, you can make the greedy move: take the earliest-finishing activity compatible with what has already been selected. The lecture's point is that the greedy version is not "lucky." It works because that earliest finish leaves maximum room for the rest of the solution, and the remaining suffix is still an optimal subproblem.

The Huffman notebook then shows a different flavor of greedy reasoning. Instead of interval compatibility, the objective is compression cost. The local move is to combine the two least frequent characters first, because the deepest leaves in the final tree should correspond to the smallest frequencies. That is why the implementation builds a min-heap of weighted tree nodes, repeatedly extracts two minima, and inserts the merged parent back into the queue. The lecture is also practical here: it does not stop at "construct the tree." It turns a source string into frequency counts, builds the tree, derives an encoding dictionary by traversing the tree, compresses the original string into a bitstring, and decodes it back. This full pipeline is what makes the concept stick for exams.

Coding Homework 7 extends the week in a useful way. It asks for DP reconstruction of the activity-selection solution, a reverse-greedy version, a room scheduler, a maximum-value activity-selection variant, and a simplified greedy knapsack. Together, these tasks teach the important boundary: greedy is powerful, but only when the proof matches the problem structure. If the scoring rule changes, or if the local choice can block a better global combination, the correct tool may shift back toward dynamic programming.

### Jupyter Notebook Explanations
#### Ch15_GreedyAlgorithms(ActivitySelectionProblem).ipynb
The notebook begins with an activity class and a randomized generator that builds interval-style scheduling instances.

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

The code mirrors the proof. Sort by finish time, add a dummy start activity, then scan until the first compatible activity appears. That first compatible activity is the greedy choice.

#### Ch15_GreedyAlgorithms(HuffmanCoding).ipynb
This notebook shows the entire compression pipeline, not just the tree construction.

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

The min-heap repeatedly exposes the two lightest trees. The encoder then records the `0/1` path to each leaf, and the decoder walks those same paths from the root until it reaches a character leaf.

#### CodingHW_7(chapter15-CLRS).ipynb
Homework 7 pressure-tests the lecture ideas by changing the objective or the local rule.

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

```python
def recursive_selectionGreedyLatest(S):
    """solve the activity selection problem recursively"""
    solution = []
    
    def recursive_selection_GreedyRLatest(sorted_S,i,j):
        """generic recursive solution to the Activity-Selection Problem"""
        nonlocal solution
        
        ai = sorted_S[i]
        aj = sorted_S[j]

        best_k = None

        for k in range(1,len(sorted_S)-1):
            ak = sorted_S[k]

            if ai.f <= ak.s and ak.f <= aj.s:
                if best_k == None or ak.s > sorted_S[best_k].s:
                    best_k = k

        if best_k != None:
            output_left = recursive_selection_GreedyRLatest(sorted_S,i,best_k)
            solution.append(sorted_S[best_k])
            return output_left + 1
        else:
            return 0
        
    sorted_S = [activity("_",0,0)] + sorted(S,key=lambda a:a.s) + [activity("_",24,24)]
    n = len(sorted_S)
    output = recursive_selection_GreedyRLatest(sorted_S,0,n-1)
    
    return output,solution
```

These two exercises are useful because they force you to ask whether the original greedy proof still applies or whether the problem has changed enough to need a different argument.

## Examples worth keeping
- **Earliest-finish activity selection**: after sorting by finish time, choose the first compatible activity and recurse on the suffix.
- **Reverse greedy**: scan for the latest-starting activity still compatible with the current left/right boundaries.
- **Room scheduling**: sort by start time and place each activity into the first room whose final activity finishes in time.
- **Huffman merge step**: repeatedly combine the two minimum-frequency nodes into a parent with summed weight.
- **Greedy boundary case**: simplified greedy knapsack is easy to code, but full 0-1 knapsack still belongs to [[Dynamic Programming#Definition|dynamic programming]].

## Takeaways (questions to resolve)
- [ ] Why does the earliest-finishing compatible activity count as a safe greedy choice?
- [ ] What is the exact difference between greedy-choice property and optimal substructure?
- [ ] Why does the Huffman algorithm use a min-priority queue rather than a sorted array or linked list?
- [ ] Which CodingHW7 variations preserve the original greedy proof, and which ones force a DP-style rethink?

## Flashcards
#cards/CSCI4041
1. Greedy-choice property::A globally optimal solution can be built by making a locally optimal choice first.
2. Activity-selection greedy rule::Choose the compatible activity with the earliest finish time.
3. Why greedy differs from DP::Greedy chooses first and solves the remainder; DP solves subproblems first and then chooses.
4. Huffman local rule::Repeatedly combine the two least frequent nodes.
5. Prefix-free code::No codeword is a prefix of any other codeword.
6. Huffman structure::A full binary tree whose leaves are characters and whose root-to-leaf paths define codewords.
7. Room-scheduling greedy idea::Place each activity into the first room whose current last activity finishes before the new one starts.
