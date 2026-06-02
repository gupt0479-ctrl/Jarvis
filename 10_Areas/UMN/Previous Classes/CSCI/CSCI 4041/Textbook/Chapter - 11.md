---
type: class
input_kind: book
status: sprout
created: 2026-03-09
updated: 2026-04-28
area:
  - "[[UMN Board]]"
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Textbook/Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Textbook"
next: "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 8|Week - 8]]"
---
# Chapter 11 - Hash Tables
## Summary Links
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 8#Chapter 11 - Hash Tables, Collision Handling, and Homework Variants|Week - 8]]
- [[Hashing#Definition|Hashing]]
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

---

## Overview
- Chapter 11 studies dictionary implementations where array indexing is replaced by a hash function.
- In CSCI 4041, the lecture emphasis is practical collision behavior: chaining, probing, deleted sentinels, load factor, and how experiments expose average-case assumptions.
- This chapter is the first major place where worst-case and expected/average-case behavior sharply diverge.

## Core Definitions
- **Dictionary:** dynamic set supporting `INSERT`, `SEARCH`, and `DELETE`.
- **Direct-address table:** table indexed directly by key, practical only for small universes.
- **Hash function:** maps keys from a large universe into `m` table slots.
- **Collision:** two keys map to the same slot.
- **Chaining:** store colliding keys in a linked list or bucket at the slot.
- **Open addressing:** store all keys directly in the table and probe alternative slots.
- **Load factor:** `alpha = n/m`, the ratio of stored keys to table slots.
- **Tombstone / deleted sentinel:** marker that preserves a probe chain after deletion.

## Main Algorithms
- `CHAINED-HASH-INSERT`, `CHAINED-HASH-SEARCH`, `CHAINED-HASH-DELETE`.
- Division and multiplication hash methods.
- Universal hashing as the textbook framework for randomized hash-function choice.
- Linear probing, quadratic probing, and double hashing for open addressing.
- Lecture variants: `chainhashmap`, `probehashmap`, analysis versions that measure collisions, chain lengths, and probe lengths.

## Correctness Ideas
- Chaining correctness depends on searching exactly the chain selected by `h(k)`.
- Open-address search must follow the same probe sequence that insertion would have followed.
- Deletion in open addressing needs a tombstone; replacing a deleted key with `None` can break later searches.
- Uniform hashing assumptions are analysis assumptions, not guarantees from arbitrary Python string hashing.

## Complexity
- Direct addressing supports operations in `O(1)` time but can waste huge space.
- Chaining has worst-case `Theta(n)` search if all keys collide; expected search is `Theta(1+alpha)` under simple uniform hashing.
- Open addressing requires `alpha < 1`; expected probes grow as load factor approaches 1.
- Double hashing reduces clustering compared with linear probing when the step sequence covers the table.

## Lecture Emphasis
- `Lectures/Week - 8/Ch11_ChainHashMap.ipynb` implements chaining with a nested `item` object and linked-list buckets.
- `Ch11_ChainHashMap-Analysis.ipynb` and `Ch11_ChainHashMap-ChainLengthDistribution.ipynb` connect `alpha` to observed chain lengths.
- `Lectures/Week - 8/Ch11_ProbeHashMap.ipynb` implements probing and makes the deleted sentinel concrete:

```python
while i < self.m:
    q = self.h(k,i)
    if self.table[q] in [None,"__DELETED__"]:
        self.table[q] = k
        return q
    i += 1
```

- `Ch11_ProbeHashMap-Analysis.ipynb` and `Ch11_ProbeHashMap-ProbeLengthDistribution.ipynb` measure probe distances and collision behavior.
- `Homework/Coding/CodingHW_5(chapter11-CLRS).ipynb` supports dynamic sets with bit vectors, random key selection from chaining, and multiplicative hashing.
- Weekly/concept links: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 8|Week - 8]], [[Hashing|Hashing]], [[Elementary Data Structures|Elementary Data Structures]].

## Examples
- If `m=11` and `h(k)=k mod 11`, keys `22`, `33`, and `44` all collide at slot 0.
- In chaining, those keys can all live in the slot-0 chain.
- In probing, deleting `33` must leave a tombstone so searching for `44` still continues past the old `33` position.

## Connections
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 8|Week - 8]]
- [[Hashing|Hashing]]
- [[Elementary Data Structures|Elementary Data Structures]]
- Source homework read: `Homework/Coding/CodingHW_5(chapter11-CLRS).ipynb` and `Homework/Paper/Paper HW - 5 (Ch - 11).pdf`.
- TODO: source gap - no vault Homework/Paper Homework note exists for direct wikilinking.

## Common Pitfalls
- Saying hash tables are always `O(1)` without stating average-case assumptions.
- Letting load factor approach 1 in open addressing.
- Using `None` instead of a tombstone after deletion in a probe table.
- Comparing chaining and probing without accounting for memory layout and clustering.
- Forgetting that universal hashing is about choosing from a family of hash functions.

## Review Checklist
- [ ] Define direct addressing, hashing, collision, chaining, open addressing, and load factor.
- [ ] Implement chained insert/search/delete.
- [ ] Implement probe insert/search/delete with a deleted sentinel.
- [ ] Explain why tombstones are necessary.
- [ ] Analyze search time in terms of load factor and collision assumptions.
