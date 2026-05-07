---
type: class
input_kind: book
status: seed
created:
updated: 2026-04-16
area:
  - "[[UMN Board]]"
tags:
  - "#class"
  - "#Textbook"
next: "[[10_Areas/Degree/UMN/Classes/CSCI 4041/Week - 8|Week - 8]]"
---
# Chapter 11 - Hash Tables
## Summary Links
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Week - 8#Chapter 11 - Hash Tables, Collision Handling, and Homework Variants|Week - 8]]
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Data Structures & Methods/Hashing#Definition|Hashing]]
- [[Elementary Data Structures#Definition|Elementary Data Structures]]

Hash tables are an effective data structure for implementing **dictionaries**, which support the dynamic-set operations `INSERT`, `SEARCH`, and `DELETE`. While worst-case search can take $Θ(n)$ time, hashing performs extremely well on average when the hash function behaves well and load is controlled.

## 11.1 Direct-Address Tables
Direct addressing works when the universe U of keys is small.

- Table slot k corresponds directly to key k.
- `SEARCH`, `INSERT`, and `DELETE` all take $O(1)$ time.
- The drawback is space: if the universe is huge but only a small number of keys are present, most of the table is wasted.

### Lecture Emphasis
The lecture used UMN-style email strings as the motivating example: the universe is enormous, but the set actually stored is comparatively small. That is why direct addressing is conceptually perfect but practically impossible in most real applications.

## 11.2 Hash Tables
When the set K of keys actually stored is much smaller than the universe U, a hash table uses a **hash function** $h: U \to \{0,1,\dots,m-1\}$ to compute a slot index.

### Collisions and Chaining
- A **collision** occurs when two distinct keys map to the same slot.
- In **chaining**, each slot stores a linked list of all elements hashing there.

Under independent uniform hashing:
- **load factor:** $α = n/m$
- **expected search time:** $Θ(1 + α)$

### Lecture `chainhashmap` Class
The Week 8 notebook implemented chaining directly:
- table is an array of linked-list objects
- nested `item` class stores `key` and `value`
- `insert(x)` prepends to the chain at `h(x.key)`
- `search(key)` walks only the relevant chain
- `delete(x)` removes from that chain using linked-list delete logic

That matters because it connects the chapter formula $Θ(1+α)$ to actual code that depends on the linked-list implementation from Chapter 10.

## 11.3 Hash Functions
A good hash function should approximate independent uniform hashing.

### Static Hashing Methods
- **Division:** $h(k)=k \bmod m$
- **Multiplication:** $h(k)=\lfloor m(kA \bmod 1)\rfloor$
- **Multiply-shift:** efficient word-level variant for tables of power-of-two size

### Universal Hashing
Choose a hash function at random from a family H such that for any two distinct keys,
$$
\Pr[h(k_1)=h(k_2)] \leq 1/m.
$$

### Lecture Emphasis
The coding homework used the multiplication method in a practical way:
$$
h(k) = \lfloor m((kA) \bmod 1)\rfloor
$$
with Knuth's recommended constant $A \approx 0.618$. The point was not only the formula itself, but why it often distributes nonrandom-looking keys better than naive `% m` when m has bad arithmetic structure.

## 11.4 Open Addressing
In **open addressing**, all elements live directly in the table itself. The load factor must satisfy $α \leq 1$.

Each key has a **probe sequence**:
$$
\langle h(k,0), h(k,1), \dots, h(k,m-1)\rangle
$$

### Common Probe Families
- **Linear probing:** $(h'(k) + i) \bmod m$
  - main issue: **primary clustering**
- **Double hashing:** $(h_1(k) + i h_2(k)) \bmod m$
  - better spread across the table

### Lecture `probehashmap` Class
The Week 8 notebook implemented:
- flat array table
- `__DELETED__` sentinel string for deleted slots
- insertion that reuses empty or deleted slots
- search that must continue through deleted slots
- delete that marks a slot as deleted rather than blanking it

This is the operational reason tombstones are needed: a blank slot would incorrectly terminate the probe sequence for keys inserted later in the same cluster.

## 11.5 Practical Considerations
### Deletion
Standard open addressing uses a tombstone marker to keep probe chains intact. The textbook also discusses a more careful deletion strategy that shifts keys backward to close the gap.

### Lecture / CodingHW5 Extensions
- **Bit-vector set:** use integer bit operations for `insert`, `search`, and `delete`
- **Uniform random key from chaining map:** sample `(row, col)` positions using `max_length`
- **Multiplicative hashing:** compare against division method
- **Double hashing:** use a second step-size hash
- **Delete without tombstone:** shift subsequent keys backward when their natural slot would allow it

### Empirical Analysis Notes
The analysis notebooks are important because they connect the theory to observed behavior:
- chain-length distributions for chaining cluster around what the load factor predicts
- probe-length distributions show double hashing behaves better than linear probing
- the histogram notebooks make primary clustering visible instead of just stated

> [!IMPORTANT] The chapter's big lesson is not "hash tables are always O(1)." It is "hash tables are O(1) on average under specific assumptions about hashing and load."
