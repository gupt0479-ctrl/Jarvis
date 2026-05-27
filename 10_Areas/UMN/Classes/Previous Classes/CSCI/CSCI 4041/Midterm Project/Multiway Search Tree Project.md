---
type: class
input_kind: project
status: sprout
created: 2026-04-27
updated: 2026-04-27
area:
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Project"
related:
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Midterm Project|Midterm Project]]"
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 6|Week - 6]]"
  - "[[Chapter - 18|Chapter - 18]]"
---
# Multiway Search Tree Project
## Overview
This project option implements a multiway search tree (2-3 tree variant). Multiway trees generalize BSTs by allowing nodes to hold multiple keys and have more than two children. The 2-3 tree is the simplest case: internal nodes have either 2 or 3 children, and all leaves sit at the same depth. This structure is the conceptual ancestor of B-trees, which Chapter 18 covers for disk-based storage.
## Source Files
- `Midterm_Project/Multiway Search Tree/Ch12_MultiWayTree.ipynb` — multiway tree implementation
- `Midterm_Project/Multiway Search Tree/DesignandAnalysisofExperiments-Chapter4.pdf` — experimental design reference
## Reference Papers
- `2-3-Trees(first_publication).pdf` — original 2-3 tree publication
- `AhoHopcroftUllman-DataStructuresandAlgorithms-Chapter5.pdf` — Aho, Hopcroft, Ullman treatment of multiway trees
- `ArtofComputerProgrammingVol3-BalancedTreesMultiwayTrees.pdf` — Knuth's treatment of balanced and multiway trees
- `DataStructuresandAlgorithmsinPython-Chapter11.pdf` — Python-oriented reference
## Key Algorithms and Data Structures
- **2-3 tree**: balanced search tree where internal nodes have 2 or 3 children, all leaves at the same depth
- **Node splitting**: when a node overflows (4 keys after insertion), split it and push the middle key up to the parent
- **B-tree generalization**: a B-tree of order $t$ generalizes the 2-3 idea to nodes with between $t$ and $2t$ children, optimized for disk I/O
- **Search**: walk down the tree comparing the search key against the keys stored in each node
- **Insertion**: search for the leaf, insert, and split upward if necessary
## Concept Links
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 6|Week - 6]] — B-Trees lecture and balanced tree context
- [[Chapter - 18|Chapter - 18]] — B-Trees (CLRS)
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 13|Chapter - 13]] — red-black trees (alternative balancing strategy)
- [[AVL Trees|AVL Trees]] — comparison: binary vs multiway balancing
## Complexity
| Operation | Average | Worst |
|---|---|---|
| Search | $O(\log n)$ | $O(\log n)$ |
| Insert | $O(\log n)$ | $O(\log n)$ |
| Delete | $O(\log n)$ | $O(\log n)$ |
| Space | $O(n)$ | $O(n)$ |

Multiway trees minimize tree height by packing more keys per node. For disk-based storage (B-trees), this reduces I/O operations because each node read brings in multiple keys at once.