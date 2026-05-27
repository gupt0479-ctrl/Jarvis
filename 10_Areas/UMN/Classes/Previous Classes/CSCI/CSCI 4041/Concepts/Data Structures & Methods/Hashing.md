---
type: concept
course: CSCI 4041
status: sprout
mastery (1/10): 0
created: 2026-03-16
topics:
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 11]]"
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[Introduction to Algorithms]]"
related:
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 8|Week - 8]]"
---
# [[Hashing]]
## MOC
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 8#Jupyter Notebook Explanations|Week - 8]]
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 11#11.2 Hash Tables|Chapter - 11 - Hash Tables]]
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 11#11.4 Open Addressing|Chapter - 11 - Open Addressing]]
- [[Elementary Data Structures#Definition|Elementary Data Structures]]

## Definition
- **Hash table** maps a large key universe into a smaller table of slots.
- **Hash function** computes the slot index from the key.
- **Collision** means two distinct keys map to the same slot.
- **Load factor** is `n/m`, the number of stored keys divided by table size.
- **Goal** is expected constant-time insert, search, and delete under good hashing assumptions.

## Core Ideas (Textbook)
### Direct Addressing
- Perfect when the universe is small.
- Impractical when the universe is huge.
- Good conceptual starting point because it shows what hashing is approximating.

### Chaining
- Each table slot stores a linked list.
- Expected search time is $Θ(1+α)$ under independent uniform hashing.
- Collision cost is localized to one chain.
- Chaining allows load factor greater than 1.

### Hash Functions
- Division method: simple but sensitive to table-size choice.
- Multiplication method: often spreads arithmetic patterns better.
- Universal hashing: protects against adversarial key patterns.
- The quality of the hash function is part of the algorithmic guarantee, not just an implementation detail.

### Open Addressing
- Everything stays inside the table.
- Probe sequences become part of the data-structure definition.
- Load factor cannot exceed 1.
- Deletion is subtle because search depends on uninterrupted probe chains.

## Core Ideas (Lecture)
### `chainhashmap`
- table is an array of linked lists
- nested `item` object stores key/value pairs
- insert prepends into one chain
- search and delete operate only within one chain

This is the lecture's main example of how hashing reuses a simpler data structure underneath.

### `probehashmap`
- flat array table
- `__DELETED__` sentinel
- insertion probes until an empty or deleted slot is found
- search must continue through deleted slots

This version makes the probe sequence visible as an actual algorithm instead of just a formula in the textbook.

### CodingHW5 Code Patterns
#### Bit-Vector Set
```python
insert(x): self.set |= (1 << x)
search(x): return (self.set >> x) & 1
delete(x): self.set &= ~(1 << x)
```

#### Multiplicative Hashing
```python
h(k) = floor(m * ((k * A) % 1))
```

#### Double Hashing
```python
h(k, i) = (h1(k) + i * h2(k)) % m
h2(k) = 1 + (k % (m - 1))
```

#### Delete Without Tombstone
- remove key at slot j
- scan forward through the probe sequence
- move later keys backward when their natural slot allows it

The lecture point was that this is possible, but more delicate than using a tombstone.

### Empirical Analysis
- Chaining histograms support the load-factor story.
- Probe histograms show linear probing clusters.
- Double hashing behaves more like the "ideal random" model.

## Professor Code From Lecture
### Ch11_ChainHashMap.ipynb — Full `chainhashmap` Implementation
The `chainhashmap` class demonstrates separate chaining collision resolution. Each slot in the table is a linked list. The nested `item` class stores key-value pairs. The hash function `h` uses Python's built-in `hash()` with the division method (`hash(key) % m`). Insert checks for an existing key first — if found, it updates the value; otherwise it prepends a new item. Search hashes the key, walks the chain, and returns the item or `None`. Delete delegates to the linked list's own delete method. The table size `m` defaults to 11 (a prime, which helps distribute keys more evenly).

```python
class chainhashmap:
    """a hash map which implements separate chaining collision resolution"""
    
    ################################################################ nested item class
    class item:
        """items for the table"""
        
        def __init__(self,key,value):
            self.key = key
            self.value = value
        
        def __eq__(self,other):
            """comparison of item objects based on key attribute"""    
            return self.key == other.key
        
        def __ne__(self,other):
            """comparison of item objects based on key attribute"""    
            if type(other)==str:
                return self.key != other
            else:
                return self.key != other.key
        
        def __str__(self):
            """printing utility"""
            return "("+str(self.key)+","+str(self.value)+")"
    ################################################################
    
    
    def __init__(self,capacity=11):
        """constructor for table hash map with m max slots"""
        self.m = capacity                                     # table size
        self.table = [linkedlist() for i in range(capacity)]  # initialize with empty lists
    
    def h(self,key):
        """hash function for map -using python hash and division method"""
        return hash(key) % self.m
    
    def insert(self,x):
        """insert record x into the table"""
        L = self.table[self.h(x.key)]     # extract appropriate linked-list
        node = L.search(x.key)            # check for existing key
        if node:
            item = node.key               # extract existing item
            if item.key == x.key:
                item.value = x.value      # update existing value in table
        else:
            L.prepend(x)                  # insert new item in table

    def search(self,key):
        """search the table for key"""
        L = self.table[self.h(key)]       # extract appropriate linked-list
        node = L.search(key)              # call linked-list search for key
        if node:
            item = node.key               # extract item from node
            return item                   # return item
        else:
            return None                   # key not found
    
    def delete(self,x):
        """delete item x from the table"""
        L = self.table[self.h(x.key)]     # extract linked-list
        L.delete(x)                       # delete item from list
    
    def __str__(self):
        """printing utility for chain hash map"""
        out = ""
        for ll in M.table:
            out += str(ll) + "\n"
        return out
```

### Ch11_ProbeHashMap.ipynb — Full `probehashmap` Implementation
The `probehashmap` class demonstrates open addressing with linear probing. The table is a flat array (no linked lists). The `__DELETED__` sentinel string marks deleted slots so that search can continue through them without breaking the probe sequence. Insert probes linearly from the hash index until it finds an empty or deleted slot. Search probes linearly and stops at `None` (end of probe chain) or when the key is found. Delete simply marks the slot with `__DELETED__` — this is the tombstone approach discussed in the textbook (page 294 of CLRS). The key difference from chaining: everything lives inside the table, so load factor cannot exceed 1.

```python
class probehashmap:
    """a hash map which implements linear probing for collision resolution"""
    
    def __init__(self,capacity=11):
        """constructor for hash maps"""
        self.m = capacity # table size
        self.table = [None for i in range(capacity)]
    
    def h(self,key):
        """hash function for map -using python hash and division method"""
        return hash(key)%self.m
    
    def insert(self,k):
        """insert key k into the table"""
        hash_idx = self.h(k)     # compute the hash of key k
        
        i = 0
        while i < self.m:
            q = (hash_idx + i) % self.m  # linear probing
            if self.table[q] in [None,"__DELETED__"]:
                self.table[q] = k        # store key
                return q                 # return the storage index
            else:
                i = i + 1                # move forward
        if i==m:
            raise Exception("hash table overflow")
    
    def search(self,k):
        """search the table for key"""
        hash_idx = self.h(k)     # compute the hash of key k
        
        i = 0
        while i < self.m:
            q = (hash_idx + i) % self.m  # linear probing
            if self.table[q] == k:
                return q               # return the storage index
            elif self.table[q] == None:
                return None            # check for end of probe sequence
            else:
                i = i + 1              # move forward
        if i==self.m:
            return None
        
    def delete(self,q):
        """delete the key in index q (based on comments on page 294 of CLRS textbook)"""
        self.table[q] = "__DELETED__"
    
    def __str__(self):
        """printing utility for chain hash map"""
        return str(self.table)
```

## Proof / Reasoning Toolkit
### Load-Factor Checklist
1. Define n and m clearly.
2. Compute `α = n/m`.
3. State whether you are analyzing chaining or open addressing.
4. Use the correct expected-cost formula for that model.

### Hash-Function Checklist
1. Name the hash family or rule.
2. Explain why collisions are not prevented, only controlled.
3. State what distributional assumption is being used.
4. Do not claim worst-case $O(1)$ unless the universe is truly direct-addressed.

### Open-Addressing Deletion Checklist
1. Ask whether search would stop incorrectly if the slot were blanked.
2. If yes, use a tombstone or backward-shift repair.
3. Keep the probe sequence reachable after every delete.

## Complexity + Tradeoffs
| Method | Average Search | Worst Search | Main Tradeoff |
| --- | --- | --- | --- |
| Direct address | $O(1)$ | $O(1)$ | huge space requirement |
| Chaining | $Θ(1+α)$ | $Θ(n)$ | simple collision handling |
| Open addressing | depends on α, near constant when sparse | $Θ(n)$ | better locality, trickier deletion |

## Canonical Examples (Max 5)
### 1. Small-Universe Bit Vector
- Great when keys are small integers.
- Not practical for huge universes.
- Shows the "direct-address idea" in compressed form.

### 2. Chaining Chain Length
- If `α` grows, expected chain length grows with it.
- This is why resizing or keeping m large matters.

### 3. Linear Probing Cluster
- Consecutive occupied slots create a long run.
- Future insertions are more likely to extend that run.
- That feedback loop is primary clustering.

### 4. Double Hashing
- Second hash changes the step size.
- Different keys explore the table differently.
- Clustering is reduced compared with linear probing.

### 5. Tombstone Logic
- Deleting by blanking a slot can make later keys unreachable.
- Tombstones preserve search continuity.
- This is the easiest way to remember why deletion is special in open addressing.

## Practice Map
- Two Sum
- Group Anagrams
- Design HashMap
- Top K Frequent Elements
- Any counting/frequency-table problem that naturally wants key-to-bucket mapping
- CodingHW_5(chapter11-CLRS).ipynb: bit-vector set, multiplicative hashing, double hashing, delete without tombstone
- Paper HW - 5 (Ch - 11).pdf: written problems on hash functions, chaining analysis, and open addressing

## Mini-test
1. Why is hashing an average-case story?
2. What role does load factor play in chaining?
3. Why is deletion harder in open addressing than in chaining?
4. What is primary clustering?
5. Why can universal hashing help against adversarial inputs?

## Flashcards
#cards/CSCI4041
1. Collision definition::Two distinct keys hash to the same slot.
2. Load factor formula::`α = n/m`.
3. Expected chaining search::$Θ(1+α)$.
4. Open addressing requirement::All elements live in the table, so `α <= 1`.
5. Primary clustering::Long occupied runs formed by linear probing.
6. Why use `__DELETED__`::To keep later keys in the probe sequence searchable.
7. Universal hashing idea::Randomly choose a hash function from a family with low pairwise collision probability.
