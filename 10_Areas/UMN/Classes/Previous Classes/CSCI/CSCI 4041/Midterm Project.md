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
  - "[[AVL Trees|AVL Trees]]"
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 6|Week - 6]]"
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 7|Week - 7]]"
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 13|Chapter - 13]]"
  - "[[Chapter - 18|Chapter - 18]]"
---
# Midterm Project
## Overview
The midterm project implements one of three balanced search tree variants. Each option extends a shared `balancedtree` scaffold with a specific balancing strategy. The project tests understanding of rotations, invariant maintenance, and correctness validation through stress testing.
## Project Options
### AVL Tree (chosen)
- [[AVL Tree Project|AVL Tree Project]] — height-balanced BST with rotation-based rebalancing
- Implements insertion, deletion, and a 4-invariant validation suite
- Core algorithms: LL/RR/LR/RL rotations, fix-up walk, balance factor computation
- Source: `Midterm_Project/AVL Tree/AVLTree.ipynb`, `Experiment.ipynb`
- Reference papers include the original Adelson-Velsky and Landis paper (1962)
### Red Black Tree
- [[Red Black Tree Project|Red Black Tree Project]] — color-based balanced BST using Sedgewick's LLRB formulation
- Implements the 5 red-black properties with left-leaning simplification
- Core algorithms: recoloring, rotations, insert/delete fix-up
- Source: `Midterm_Project/Red Black Tree/Ch13_DiChromaticTrees.ipynb`
- Reference papers include Guibas and Sedgewick's dichromatic framework and Sedgewick's 2008 LLRB paper
### Multiway Search Tree
- [[Multiway Search Tree Project|Multiway Search Tree Project]] — 2-3 tree variant with node splitting
- Generalizes BSTs to nodes with multiple keys and more than two children
- Core algorithms: multiway search, node splitting, B-tree-style insertion
- Source: `Midterm_Project/Multiway Search Tree/Ch12_MultiWayTree.ipynb`
- Reference papers include the original 2-3 tree publication and Knuth's treatment
## Chosen Project: AVL Tree
The AVL tree project was the most directly connected to the lecture material. [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 7|Week - 7]] covered both the CLRS red-black tree chapter and the AVL project implementation. The four rotation trigger sequences (`[30,20,10]` for LL, `[10,20,30]` for RR, `[30,10,20]` for LR, `[10,30,20]` for RL) are the core mechanical skill. The stress test in `Experiment.ipynb` used `random.seed(4041)`, 600 mixed insert/delete operations, key space 200, and 60% insert / 40% delete ratio.
The validation suite checks four independent invariants:
1. Inorder traversal produces sorted output (BST property)
2. Every node's balance factor is in $\{-1, 0, 1\}$ (AVL property)
3. Parent pointers are consistent in both directions
4. Stored height equals recomputed height
This multi-invariant approach is the right mental model for debugging any tree implementation.
## Concept Links
- [[AVL Trees|AVL Trees]] — full concept note
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 6|Week - 6]] — balanced trees, rotations, B-Trees
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 7|Week - 7]] — red-black trees and AVL project
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 13|Chapter - 13]] — red-black trees (CLRS)
- [[Chapter - 18|Chapter - 18]] — B-Trees (CLRS)