---
type: class
input_kind: lecture
status: seed
created: 2026-03-09
updated: 2026-04-16
area:
  - "[[10_UMN/CSCI 4041/CSCI 4041/Concepts/DSA|DSA]]"
  - "[[10_UMN/CSCI 4041/CSCI 4041/Concepts/Introduction to Algorithms|Introduction to Algorithms]]"
  - "[[CSCI 4041 Board]]"
tags:
  - "#class"
  - "#Lecture"
next:
  - "[[50_Archive/UMN/Classes/CSCI 4041/Week - 9|Week - 9]]"
---
# Entire Week
## What you must be able to do
- [[Chapter - 11#11.2 Hash Tables|Chapter - 11 hash tables]], [[Chapter - 11#11.3 Hash Functions|hash functions]], and [[Chapter - 11#11.4 Open Addressing|open addressing]]: explain collisions, load factor, chaining, open addressing, and why hashing is average-case fast rather than worst-case fast.
- [[50_Archive/UMN/Classes/CSCI 4041/Concepts/Data Structures & Methods/Hashing#Core Ideas (Lecture)|Hashing - Core Ideas (Lecture)]], [[50_Archive/UMN/Classes/CSCI 4041/Concepts/Data Structures & Methods/Hashing#Complexity + Tradeoffs|Hashing - Complexity + Tradeoffs]], and [[Chapter - 11#11.5 Practical Considerations|practical considerations]]: compare `chainhashmap`, `probehashmap`, and the CodingHW5 variants.
- [[50_Archive/UMN/Classes/CSCI 4041/Concepts/Data Structures & Methods/Hashing#Proof / Reasoning Toolkit|Hashing - Proof / Reasoning Toolkit]]: use load factor and independent uniform hashing assumptions correctly in explanations.
- [[50_Archive/UMN/Classes/CSCI 4041/Concepts/Data Structures & Methods/Hashing#Practice Map|Hashing - Practice Map]]: map/frequency/counting practice remains open.

## Key ideas (textbook)
- **Hashing trades ordering for average-case speed.** If we only care about insert, delete, and search, hashing can beat balanced trees on average because it avoids maintaining sorted structure.
- **Collisions are unavoidable when the universe is much larger than the table.** The real question is not whether collisions happen, but how they are handled and how well the hash function spreads them.
- **Load factor is the core tuning variable.** In chaining it predicts expected chain length. In open addressing it measures how full the table is and therefore how expensive probing becomes.
- **Hash-function assumptions matter.** Statements like "$Θ(1)$ average search" are only true under distribution assumptions like independent uniform hashing or a well-designed universal family.
- **Open addressing turns deletion into a subtle invariance problem.** A blank slot can break a probe chain, which is why tombstones or backward-shifting repair are needed.

## Concepts created / updated today
- [[50_Archive/UMN/Classes/CSCI 4041/Concepts/Data Structures & Methods/Hashing#Definition|Hashing]]
- [[Chapter - 11#11.5 Practical Considerations|Chapter - 11 - practical considerations]]
- [[50_Archive/UMN/Classes/CSCI 4041/Concepts/Data Structures & Methods/Hashing#Canonical Examples (Max 5)|Hashing - Canonical Examples]]

## Lecture
### Chapter 11 - Hash Tables, Collision Handling, and Homework Variants
This week was about giving up ordering to gain speed. The lecture framed the whole chapter around one motivating comparison: BSTs support ordered operations like min, max, range queries, and inorder traversal, but if all we need is insert, delete, and search, we can often do better on average with hashing. That improvement is not magic. It comes from converting a huge universe of keys into a much smaller table of slots, accepting that collisions are unavoidable, and then designing collision-handling rules that keep expected work small.

The lecture's examples made the scale mismatch concrete through UMN-style email keys. The universe is enormous, but the number of stored keys is small. That is why direct-address tables are conceptually perfect but useless in practice. Hashing solves the space problem by storing only m slots and letting the hash function choose where each key should go. Once collisions appear, the chapter splits into two design directions. Chaining keeps external lists at each slot, so the table stays sparse and the load factor can exceed 1. Open addressing stores everything in the table itself, so probe sequences become part of the structure invariant and the load factor must stay below or equal to 1.

The Week 8 notebooks made both approaches concrete. `chainhashmap` reused the linked-list code from Chapter 10, which is a good reminder that data structures build on each other. `probehashmap` instead used a flat array and a `__DELETED__` marker, making it easy to see why deletion is trickier in open addressing. The analysis notebooks mattered because they turned theory into measurements: chain lengths tracked the load factor, and double hashing visibly reduced clustering compared with simple linear probing. CodingHW5 then added the kinds of implementation details that usually stick before an exam, like the bit-vector set, the multiplication method, double hashing, and deletion without tombstones.

### Jupyter Notebook Explanations
#### Ch11_ChainHashMap.ipynb
This notebook implements chaining directly on top of the linked-list code from Week 4.

```python
# conceptual structure
table = [linkedlist() for _ in range(m)]
# insert: prepend item(key, value) into table[h(key)]
```

The important point is that chaining localizes the collision cost. A key only competes with other keys in its own slot, so expected search time is "hash function cost plus expected chain length," which becomes $Θ(1 + α)$ under the standard assumptions.

#### Ch11_ProbeHashMap.ipynb
This notebook implements open addressing with a flat table and a tombstone marker.

```python
__DELETED__ = "__DELETED__"
# insert: probe h(key,0), h(key,1), ...
# search: keep probing through __DELETED__
# delete: mark slot as __DELETED__
```

The lecture's main point here was that deletion cannot simply clear a slot. If search stopped at the first empty location, later keys in the same probe chain would become unreachable.

#### Ch11_ChainHashMap-Analysis.ipynb and Ch11_ProbeHashMap-Analysis.ipynb
These notebooks turned the chapter's average-case claims into empirical data.
- Chain lengths under random insertion look like the load factor suggests they should.
- Probe lengths grow much faster under clustering.
- Double hashing behaves more like the random-permutation ideal than linear probing does.

#### CodingHW_5(chapter11-CLRS).ipynb
This homework captured the implementation-heavy side of hashing:

```python
# bit-vector set
insert(x): self.set |= (1 << x)
search(x): return (self.set >> x) & 1
delete(x): self.set &= ~(1 << x)
```

This is worth keeping because it shows the "array indexed by universe" idea in a compressed form when the universe is small enough.

The rest of the homework added:
- random key sampling from a chaining table using `max_length`
- multiplicative hashing with $A \approx 0.618$
- double hashing with a second step-size function
- deletion without tombstones by shifting keys backward when safe

## Examples worth keeping
- **Expected collisions:** with n distinct keys in a table of size m, expected collisions are $n(n-1)/(2m)$ under independent uniform hashing.
- **Bit-vector set:** small-universe membership can be stored in one integer with bit operations.
- **Division vs multiplication method:** `% m` can behave badly with some table sizes, while multiplicative hashing spreads regular patterns better.
- **Linear probing issue:** long occupied runs create primary clustering.
- **Double hashing:** second hash gives a much more varied probe sequence and usually shorter search chains.

## Takeaways (questions to resolve)
- [ ] Why is "$O(1)$ average search" only an average-case statement rather than a worst-case guarantee?
- [ ] How exactly does load factor affect chaining versus open addressing?
- [ ] Why does blanking a deleted slot break open-addressing search?
- [ ] Why does double hashing reduce clustering more effectively than linear probing?
- [ ] When does direct addressing still make sense despite the chapter's motivation for hashing?

## Flashcards
#cards/CSCI4041
1. Hash-table load factor::$α = n/m$.
2. Expected chaining search time::$Θ(1 + α)$.
3. Why are collisions unavoidable::Because the key universe is usually much larger than the number of table slots.
4. What is primary clustering::Long runs of occupied slots created by linear probing.
5. Why use a tombstone in open addressing::To preserve probe chains after deletion.
6. Multiplication method form::$h(k) = \lfloor m((kA) \bmod 1)\rfloor$.
7. Universal hashing promise::For any two distinct keys, collision probability is at most $1/m$.
