---
type: evergreen
course: CSCI 4041
status: sprout
mastery (1/10): 0
created: 2026-01-22
topics:
  - "[[CSCI 4041 Board]]"
  - "[[40_Resources/CS/Links|Links]]"
  - "[[Introduction to Algorithms]]"
related:
  - "[[UMN Board]]"
---
# Data Structures & Algorithms
## MOC
- *Textbook*: [[Introduction to Algorithms|Introduction to Algorithms]]
- *Main File*: [[DSA]]
### Concepts
1. [[Sorting Algorithms#Definition|Sorting Algorithms]]
2. [[Time Complexity#Definition|Time Complexity]]
3. [[Divide and Conquer#Definition|Divide and Conquer]]
4. [[QuickSort#Definition|QuickSort]]
5. [[HeapSort#Definition|HeapSort]]
6. [[Elementary Data Structures#Definition|Elementary Data Structures]]
7. [[AVL Trees#Definition|AVL Trees]]
8. [[B-Trees#Definition|B-Trees]]
9. [[Hashing#Definition|Hashing]]
10. [[Dynamic Programming#Definition|Dynamic Programming]]
11. [[Greedy Algorithms#Definition|Greedy Algorithms]]
12. [[Graph Algorithms#Definition|Graph Algorithms]]
13. [[Minimum Spanning Trees#Definition|Minimum Spanning Trees]]
14. [[Shortest Paths#Definition|Shortest Paths]]
15. [[Maximum Flow#Definition|Maximum Flow]]
## Definition
- This note is the course-level map tying together weekly lecture notes, textbook chapter notes, and concept notes.
- The week numbering below matches the vault week files directly.
- Spring break is kept as a separate schedule marker and does not offset the vault week numbering.
## Resources
1. ==The textbook solutions==: [OP Link](https://sites.math.rutgers.edu/~ajl213/CLRS/CLRS.html) → [[60_Claude/30_Source_Summaries/Vault Web Ingestion/OP Link (sites.math.rutgers.edu)|source note]]
2. Supplementary Book for the project: The art of computing 3rd edition.
3. Puru Links:
   - DSA: https://drive.google.com/drive/folders/1hQwxDwuz5Kw4sdEnxmcsK1Ynpgf11s4N
   - [[60_Claude/30_Source_Summaries/Vault Web Ingestion/1Hqwxdwuz5kw4sdenxmcsk1ynpgf11s4n (drive.google.com)|drive folder 1 source note]]
   - DAA: https://drive.google.com/drive/folders/1CtWO-3T0OzMwvKPWEk2ihqME2NJuK4qR
   - [[60_Claude/30_Source_Summaries/Vault Web Ingestion/1Ctwo 3T0ozmwvkpwek2ihqme2njuk4qr (drive.google.com)|drive folder 2 source note]]
4. [Miniconda Help](https://docs.conda.io/projects/conda/en/latest/user-guide/index.html) → [[60_Claude/30_Source_Summaries/Vault Web Ingestion/Miniconda Help (docs.conda.io)|source note]]
5. Entire coursework available: [Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/) → [[60_Claude/30_Source_Summaries/Vault Web Ingestion/Introduction to Algorithms (ocw.mit.edu)|source note]]
6. Another [Coursework](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) → [[60_Claude/30_Source_Summaries/Vault Web Ingestion/Coursework (ocw.mit.edu)|source note]]
## How to use them
1. Read the linked textbook chapter notes before or after lecture.
2. Use the weekly note as the main study sheet.
3. Use the concept note when you need a focused explanation, proof toolkit, or extra code.
4. Do 3-5 targeted practice problems after each week instead of trying to cover everything at once.
## LeetCode / Weekly Plan
### Week 1 & 2 - Introduction, Insertion Sort, Merge Sort
- Vault notes: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 1 & 2#Entire Week|Week - 1 & 2]]
- Textbook: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 1 & 2#Getting Started|Chapter - 1 & 2]]
- Concept: [[Sorting Algorithms#Practice Map|Sorting Algorithms - Practice Map]]
- Practice themes:
  - implement insertion sort once
  - merge two sorted arrays/lists
  - compare built-in sort against your own implementation
### Week 3 - Asymptotic Analysis and Divide-and-Conquer
- Vault notes: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 3#Entire Week|Week - 3]]
- Textbook: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 3 & 4#Chapter - 3|Chapter - 3 & 4]]
- Concept: [[Divide and Conquer#Practice Map|Divide and Conquer - Practice Map]]
- Practice themes:
  - binary search templates
  - merge-sort reasoning
  - recurrence setup and Master Method drills
### Week 4 - Quicksort and Elementary Data Structures
- Vault notes: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 4#Entire Week|Week - 4]]
- Textbook: [[Chapter - 7 & 10#Chapter 7 - Quicksort|Chapter - 7 & 10]]
- Concepts:
  - [[QuickSort#Practice Map|QuickSort - Practice Map]]
  - [[Elementary Data Structures#Practice Map|Elementary Data Structures - Practice Map]]
- Practice themes:
  - partition-based reasoning
  - stack and queue patterns
  - linked-list pointer manipulation
### Week 5 - Heaps and Binary Search Trees
- Vault notes: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 5#Entire Week|Week - 5]]
- Textbook: [[Chapter - 6 & 12#Chapter - 6 Heapsort|Chapter - 6 & 12]]
- Concepts:
  - [[HeapSort#Practice Map|HeapSort - Practice Map]]
  - [[Elementary Data Structures#Practice Map|Elementary Data Structures - Practice Map]]
- Practice themes:
  - heap push/pop and top-k patterns
  - BST validate, insert, delete
### Week 6 - Rotations, AVL, and B-Trees
- Vault notes: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 6#Entire Week|Week - 6]]
- Textbook:
  - [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 13#Chapter - 13 Red-Black Trees|Chapter - 13]]
  - [[Chapter - 18#Chapter - 18 B-trees|Chapter - 18]]
- Concepts:
  - [[AVL Trees#Practice Map|AVL Trees - Practice Map]]
  - [[B-Trees#Practice Map|B-Trees - Practice Map]]
- Practice themes:
  - rotation intuition
  - height-balanced checks
  - B-tree insert/search tracing
### Week 7 - Red-Black Trees and AVL Project
- Vault notes: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 7#Entire Week|Week - 7]]
- Textbook: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 13#Chapter - 13 Red-Black Trees|Chapter - 13]]
- Concept: [[AVL Trees#Practice Map|AVL Trees - Practice Map]]
- Practice themes:
  - RB properties and fix-up cases
  - AVL trigger sequences
  - tree validation checks
### Spring Break (Not Counted in Vault Weeks)
- Review weakest topics from Weeks 1-7.
- Redo 2-3 prior problems from memory.
### Week 8 - Hash Maps
- Vault notes: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 8#Entire Week|Week - 8]]
- Textbook: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 11#Chapter 11 - Hash Tables|Chapter - 11]]
- Concept: [[Hashing#Practice Map|Hashing - Practice Map]]
- Practice themes:
  - frequency counting
  - hashing collision intuition
  - design HashMap / set style problems
### Week 9 - Dynamic Programming
- Vault notes: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 9#Entire Week|Week - 9]]
- Textbook: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 14#Chapter 14 - Dynamic Programming|Chapter - 14]]
- Concept: [[Dynamic Programming#Practice Map|Dynamic Programming - Practice Map]]
- Practice themes:
  - 1D DP
  - memoization vs bottom-up
  - 2D DP state definitions
### Week 10 - Greedy Algorithms and Huffman Coding
- Vault notes: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 10#Entire Week|Week - 10]]
- Textbook: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 15#Chapter - 15 Greedy Algorithms|Chapter - 15]]
- Concept: [[Greedy Algorithms#Practice Map|Greedy Algorithms - Practice Map]]
- Practice themes:
  - interval scheduling
  - greedy choice proofs
  - combine-smallest-first heap patterns
### Week 11 - Graphs, BFS, and DFS
- Vault notes: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 11#Entire Week|Week - 11]]
- Textbook: [[Chapter - 20#Chapter - 20 Graphs, BFS, DFS, Topological Sort, and SCC|Chapter - 20]]
- Concept: [[Graph Algorithms#Practice Map|Graph Algorithms - Practice Map]]
- Practice themes:
  - BFS levels and parents
  - DFS traversal and edge classification
  - graph representation tradeoffs
### Week 12 - Topological Sort, SCC, and MST
- Vault notes: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 12#Entire Week|Week - 12]]
- Textbook:
  - [[Chapter - 20#Chapter - 20 Graphs, BFS, DFS, Topological Sort, and SCC|Chapter - 20]]
  - [[Chapter - 21#Chapter - 21 Minimum Spanning Trees|Chapter - 21]]
- Concepts:
  - [[Graph Algorithms#Practice Map|Graph Algorithms - Practice Map]]
  - [[Minimum Spanning Trees#Practice Map|Minimum Spanning Trees - Practice Map]]
- Practice themes:
  - topological ordering
  - strongly connected components
  - Kruskal and Prim tracing
### Week 13 - Shortest Paths (Single-Source and All-Pairs)
- Vault notes: [[Week - 13#Entire Week|Week - 13]]
- Textbook:
  - [[Chapter - 22#Chapter - 22 Single-Source Shortest Paths|Chapter - 22]]
  - [[Chapter - 23#Chapter - 23 All-Pairs Shortest Paths|Chapter - 23]]
- Concept: [[Shortest Paths#Practice Map|Shortest Paths - Practice Map]]
- Practice themes:
  - Bellman-Ford tracing with negative edges
  - Dijkstra min-heap tracing
  - Floyd-Warshall on small dense graphs
  - APSP matrix multiplication vs Floyd-Warshall comparison
### Week 14 - Maximum Flow
- Vault notes: [[Week - 14#Entire Week|Week - 14]]
- Textbook: [[Chapter - 24#Chapter - 24 Maximum Flow|Chapter - 24]]
- Concept: [[Maximum Flow#Practice Map|Maximum Flow - Practice Map]]
- Practice themes:
  - residual network construction
  - augmenting path identification via BFS
  - Ford-Fulkerson / Edmonds-Karp tracing
  - max-flow min-cut verification
### Week 15 - Study / Finals Review
- Redo 1-2 representative problems from each major block:
  - sorting/heaps
  - trees
  - hashing
  - DP
  - greedy
  - graphs
## Mini-test (answer without looking)
- [ ] Can I explain the week-to-concept mapping without opening the files?
- [ ] Do my practice problems match the same numbering as the vault week notes now?
## Flashcards
#cards/CSCI4041
1. What is the main purpose of this note::It maps the course schedule to the vault's weekly notes, chapter notes, and concept notes.
2. Does spring break count as Week 8 in the vault::No, spring break is separate and Week 8 in the vault is hashing.
3. Main study rule for this vault::Use the weekly note as the central reference and the concept note as the focused deep dive.
