---
type: class
status: archived
created: 2025-11-26
updated: 2025-11-28
area:
  - "[[C Language]]"
tags:
  - "#class"
  - "#Textbook"
  - "#CSAPP"
  - "#DIS"
  - "#Lecture"
  - "#Lab"
  - "#Homework"
next: "[[Week - 12 & 13]]"
---
# #Textbook Textbook (CSAPP - 6.2 to 6.6 & 5.1 to 5.6)
## #CSAPP CSAPP
### 5.1 Capabilities and Limitations of Optimizing Compilers
Optimizing compilers are sophisticated tools that automatically transform source code to improve efficiency by simplifying expressions, identifying reusable computations, and reducing the frequency of operations. Programmers often specify an optimization level, such as **-Og**, when compiling with tools like `gcc`.
- However, the compiler's optimization capabilities are constrained by certain aspects of high-level languages like C, known as **optimization blockers**:
1. **Memory Aliasing**: Memory aliasing occurs when **two different expressions or references point to the same memory location**.
	- **Impact:** If the compiler encounters code involving pointers (`xp` and `yp`), it must assume that a write through `xp` could potentially modify the value read through `yp`. Because the compiler cannot prove that memory references are independent, it must adopt a **conservative approach**. This forces the compiler to reload values from memory repeatedly, even if they appear locally, restricting optimizations like keeping variables in registers.
2. **Procedure Calls**: When a compiler encounters a function call (a procedure call) within a block of code, it generally assumes the function might have **arbitrary side effects**.
	- **Impact:** The called function could modify global program state or perform I/O operations. Critically, it could also engage in **memory aliasing**. Because the compiler cannot predict what the procedure will do, function calls effectively **block most forms of optimization** within the surrounding code block, preventing the compiler from reordering instructions or managing register allocation effectively.
### 5.2 Expressing Program Performance
To measure the effectiveness of optimization techniques, performance must be quantified, often relating the program's running time to the input size (n).
1. **The Performance Model**: The overall runtime (T) is often modeled linearly: $$T=C_{init}​+C_{elem​}⋅n$$
	where:
	- `Cinit`​ is the fixed overhead (startup cost).
	- `n` is the measure of the input size (e.g., the number of vector elements).
	- `Celem`​ **is the performance-limiting constant, measured in Cycles Per Element (CPE)**.
2. **Cycles Per Element (CPE)**: CPE is the primary metric used in performance analysis problems. It represents the **average number of clock cycles required by the processor to process a single data element**.
	- **Problem-Solving Focus:** Textbook problems require comparing different performance equations (e.g., V1​:60+35n vs. V2​:136+4n) and determining the range of input sizes (n) for which each version is the fastest by comparing their total runtimes (T). Generally, minimizing $C_{elem}$ is the goal for large inputs (n).
### 5.3 Program Example
The running example used throughout the chapter to illustrate optimization is the generic **combine** **function**, designed to accumulate all elements of a vector into a single value.
- *Vector Data Structure*: A vector is defined using an *abstract data type structure ([[Structs]])* (e.g., `vec_rec`) that contains two main fields:
	1. `long len`: The total length or size of the vector.
	2. `data_t data`: A pointer to the array of elements.
```c
/*Move call to vec_length out of loop*/
void combine2(vec_ptr v, data_t *dest) {
	long i;
	*dest = IDENT; //0 or 1
	for (i = 0; i < vec_length; i++) {
		data_t val;
		get_vec_element(v, i, &val);
		*dest = *dest OP val; // OP: + or *
	}
}
```
- *Generic Operation*: The `combine` function is defined such that it can perform various associative operations (like summing or multiplying) by defining two compile-time constants:
	- **OP**: The combining operation itself (e.g., `+` or `*`).
	- **IDENT**: The identity value for that operation (e.g., **0 for addition** or **1 for multiplication**).
	*Below code is Updated after Reading [[#5.4 Eliminating Loop Inefficiencies|5.4]], [[#5.5 Reducing Procedure Calls|5.5]], [[#5.6 Eliminating Unneeded Memory References|5.6]]*
```c
/* Implementation with maximum use of data abstraction*/
/* 5.4 - Move call to vec_length out of loop */
/* 5.5 - Direct access to vector data */
/* 5.6 - Accumulate result in local variable */
void combine2(vec_ptr v, data_t *dest) {
	long i;
	long length = vec_length(v); // Loop Ineffeciency
	data_t *data = get_vec_element(v); //Remove function calls from loop
	data_t acc = IDENT; //0 or 1
	for (i = 0; i < length; i++) {
		acc = acc OP data[i]; // OP: + or *
	}
	*dest = acc;
}
```
### 5.4 Eliminating Loop Inefficiencies
This initial optimization focuses on making simple changes to the C code that yield performance improvements on any machine.
- **Key Concept:** Programmers should identify **loop-invariant computations**—results of computations that do not change from one iteration of the loop to the next.
- **Goal:** Move these loop-invariant computations **outside the loop** body.
- **Relevance to Problems:** Common loop inefficiencies include continually calculating an array access or boundary condition (like array length above) inside the loop when that value remains constant.
### 5.5 Reducing Procedure Calls
This section directly addresses the **procedure call optimization blocker** (Section 5.1).
- **Loop Inefficiency:** Functions that retrieve constant information (like `get_vec_element` retrieving the vector length or checking bounds). The repeated procedure call overhead slows the program down.
- **Solution:** The programmer should rewrite the code to perform a single call to retrieve the necessary invariant value (e.g., the vector length, `length = vec_length(v)`) **before the loop begins**. The loop then references this local variable, removing the repeated call overhead and enabling further compiler optimizations within the loop body.
### 5.6 Eliminating Unneeded Memory References
This section addresses performance bottlenecks caused by how intermediate results are stored, allowing performance to approach the theoretical limit imposed by the processor's functional units.
- **The Problem (Accumulators in Memory):** In the unoptimized `combine` function, the intermediate accumulated value (the accumulator) might be stored in a memory location(`*dest`). In the tight inner loop, repeatedly reading and writing this value to memory (even fast cache memory) is far slower than working directly with a CPU register. Compilers sometimes avoid using registers for accumulators if they cannot rule out memory aliasing.
- **The Solution (Register Accumulator):** The programmer performs a **store-to-load translation** manually by declaring a **local variable** (e.g., `acc`) to hold the result of the combining operation during the loop. This variable is explicitly used to compute the intermediate results (e.g., `acc = acc OP data[i]`).
	- By making the data dependency explicit and local, the programmer makes it easy for the compiler to optimize: the compiler typically assigns this local accumulator variable to a fast **CPU register**.
	- **Result:** Accessing a register is nearly 100 times faster than accessing memory, drastically improving loop performance by eliminating unneeded memory references. This transformation is essential for achieving good CPE.
- **Practice Question 5.4**: When we use `gcc` to compile `combine3` with command-line option -O2 ,we get code with substantially better CPE performance than with -O1.
	- **`-O1` (less optimized)**: At the start of _every_ iteration:
		- Loads old value from `*dest`: `vmovsd (%rbx), %xmm0 # reload the accumulator`
	    - `%xmm0` is just a **temporary mirror** of memory.
		- True accumulator lives in **memory (`*dest`)**.
	- **`-O2` (more optimized)**: Eliminates the redundant load: `vmulsd (%rdx), %xmm0, %xmm0   # directly use accumulated value`
		- `%xmm0` becomes the **true accumulator**, stored back to `*dest` only once per iteration.
		- Replicates the structure of `combine4` (“accumulate in a local variable”).
	- Does removing the memory load break correctness if `dest` aliases `data`?
		- No correctness issues. Here's why: At start of iteration `i`, the value at `*dest` is **exactly** the value written at end of iteration `i–1`.
		- `%xmm0` in `-O2` contains that same value. Even with aliasing:
			- The _reads of `data[i]`_ behave identically.
			- The _writes to `*dest`_ occur at the same times.
		- **Conclusion**: The `-O2` version still matches the exact dataflow of the original C code, even when `dest` aliases elements of the vector.
### 6.2 Locality
**Locality** is the fundamental principle that enables memory hierarchies to work effectively. Programs with good locality run faster.
1. **Locality of References to Program Data**: Locality is defined in two ways:
	1. **Temporal Locality:** Recently referenced data items are likely to be referenced again soon. (Example: using a loop counter variable repeatedly).
	2. **Spatial Locality:** If a memory location is referenced, nearby memory locations are likely to be referenced soon. (Example: iterating through an array sequentially).
	- **Stride:** *Number of bytes you jump between consecutive memory accesses*.
		- Accessing data with a **stride-1 reference pattern** (sequential access) has good spatial locality.
		- Accessing data with a large stride (e.g., accessing columns of a large 2D array stored in row-major order) has **poor spatial locality**.
2. **Locality of Instruction Fetches**: Programs typically exhibit good temporal and spatial locality when fetching instructions, especially within tight loops.
### 6.3 The Memory Hierarchy
The **memory hierarchy** is an organization of storage devices into a pyramid, with smaller, faster, and more expensive storage at the top (near the CPU) and larger, slower, and cheaper storage at the bottom. ![[Pasted image 20251202131830.png]]
1. **Caching in the Memory Hierarchy**: The hierarchy relies on **caching**, where storage at level k acts as a cache for storage at level k+1.
	- **Blocks:** Data is copied between adjacent levels in fixed-size transfer units called **blocks**. Block size generally increases lower down the hierarchy to amortize slower access times.
	 - **Cache Hit:** The requested data object is found in the cache at level k (fast).
	 - **Cache Miss:** The requested data object is not found at level k and must be fetched from level k+1 (slow).
	 - **Kinds of Misses:**
		 - **Compulsory (Cold) Miss:** Occurs when the cache is initially empty.
		 - **Conflict Miss:** Occurs when multiple blocks compete for the same cache location (set), causing one block to constantly evict another (thrashing). This is common in **direct-mapped caches**.
	- **SRAM Cache vs. DRAM Cache:** **SRAM caches** are L1, L2, L3. The **DRAM cache** (main memory caching disk data) is managed by the Virtual Memory (VM) system.
2. *Summary of Memory Hierarchy Concepts*: The hierarchy works by exploiting locality: **Temporal locality** ensures that once an object is cached, subsequent hits are fast. **Spatial locality** ensures that when a block is loaded on a miss, the cost is amortized over multiple subsequent references to other objects within that large block.
### 6.4 Cache Memories
This section provides the necessary detail for modeling and calculating cache performance (critical for most textbook problems).
1. **Generic Cache Memory Organization**: A cache is characterized by the tuple `(S,E,B,m)`:
	- `M = 2^m`: Total number of physical addresses.
	- `S = 2^s`: Number of **cache sets**.
	-  `E`: Number of **cache lines** per set (associativity).
	- `B = 2^b`: **Block size** (in bytes).
	- `C = S × E × B`: Total cache **capacity** (size in bytes, excluding overhead).
	- A physical memory address A is partitioned into three fields:
		1. `t` **tag bits:** Used to uniquely identify the block among those mapped to the same set. `t = m − (s + b)`.
		2. `s` **set index bits:** Used to select the correct set S (index into the array of sets). $s=log_{2}​(S)$.
		3. b **block offset bits:** Used to select the correct byte or word within the block B. $b=log_{2}​(B)$.
2. **Direct-Mapped Caches (E=1)**: Each set contains exactly one line.
	- **Set Selection:** The address's s bits are used as the index to select a unique set.
	- **Line Matching (Hit Check):** A hit occurs if the line's **valid bit** is set **AND** the line's **tag bits match** the address's tag bits.
	- **Word Selection:** If a hit occurs, the b bits select the offset of the desired byte/word within the block.
	- **Indexing Strategy:** Caches use **middle-order bits** for the set index (not high-order bits) because this allows contiguous memory blocks to map to different sets, improving spatial locality exploitation and minimizing conflict misses.
3. **Set Associative Caches (E>1)**: Each set contains E lines.
	- **Set Selection:** Identical to direct-mapped caches: s bits select the set S.
	- **Line Matching:** The cache must search all E lines in the selected set simultaneously. A hit occurs if any of the lines are valid and their tag matches the address tag.
	- **Replacement Policy:** If a miss occurs, and the set is full, one line must be evicted. The cache uses a replacement policy (e.g., Least Recently Used (LRU)) to select a **victim line**.
4. **Fully Associative Caches (E=C/B)**: The cache consists of a single set (S=1) containing all E lines.
	- **Set Selection:** Trivial; there is only one set (set 0).
	- **Address Partitioning:** The address is partitioned only into t **tag bits** and b **block offset bits** (no s bits).
	- **Usage:** Fully associative caches are typically small, expensive, and used at very high levels of the hierarchy, such as the **Translation Lookaside Buffer (TLB)**, which caches Page Table Entries (PTEs).
5. **Issues with Writes**: Handling write operations involves two primary policy decisions:
	- **Handling Write Hits:** What happens when the CPU writes to a cached word?
		- **Write-through:** Write immediately propagates down to the next memory level. 
		- **Write-back:** Write is deferred; the updated block is written down only when it is evicted. Requires a **dirty bit** to track modifications, but reduces bus traffic.
	- **Handling Write Misses:** What happens when the CPU writes to a word not currently in the cache?
		- **Write-allocate:** Load the corresponding block into the cache first, then update the cache line (exploits spatial locality for subsequent writes).
		- **No-write-allocate:** Write directly to the next level, bypassing the current cache level.
6. *Anatomy of a Real Cache Hierarchy*: Modern CPUs use separate **i-caches** (instructions) and **d-caches** (data). These are often private per core (L1, L2), while a larger **unified cache** (holding both instruction and data) is often shared (L3).
7. **Performance Impact of Cache Parameters**: Cache performance is quantified by:
	- **Miss Rate:** Fraction of references that miss (#misses/#references).
	- **Hit Rate:** 1−Miss Rate.
	- **Hit Time:** Time to deliver a word from the cache (very short, e.g., 4 cycles for L1).
	- **Miss Penalty:** Additional time required due to a miss (e.g., 10 cycles if served from L2, 200 cycles from main memory).
	These metrics are affected by: cache size (C), block size (B), and associativity (E).
### 6.5 Writing Cache-Friendly Code
Programmers can significantly improve performance by writing code that optimizes locality and reduces cache misses:
1. **Focus on Inner Loops:** These are the critical sections where the program spends most of its time.
2. **Maximize Spatial Locality:** Use **stride-1 reference patterns** (sequential access) to ensure that when a cache block is loaded, all data within it are used before the block is evicted.
3. **Maximize Temporal Locality:** Reuse local variables frequently, as they can often be stored in fast CPU registers or repeatedly accessed from L1 cache.
### 6.6 Putting It Together: The Impact of Caches on Program Performance
1. **The Memory Mountain**: The **Memory Mountain** graphically represents the system's memory performance by plotting the **read throughput** (bandwidth, MB/s) as a function of **working set size** (temporal locality) and **stride** (spatial locality).
	- **Ridges:** Horizontal ridges show throughput when the entire **working set** fits within a cache level (L1, L2, L3, Main Memory). This highlights the importance of **temporal locality**.
	- **Slopes:** Decreasing slopes show throughput drop as stride increases. This highlights the importance of **spatial locality**. When the stride becomes equal to or greater than the block size, performance drops sharply.
2. **Rearranging Loops to Increase Spatial Locality**: Performance depends heavily on the access pattern defined by nested loops. In operations like matrix multiplication, rearranging the loop indices (e.g., permuting `i, j, k`) can change access patterns from high-stride (poor spatial locality) to low-stride (good spatial locality), leading to dramatically different performance (CPE).
3. **Exploiting Locality in Your Programs**: To write efficient programs: focus on **inner loops** and maximize spatial locality by using **stride 1** when accessing data.
4. **Analogy for Caching and Locality:** The memory hierarchy is like a student studying for an exam.
	- **CPU Registers (L0):** The notes you are actively holding in your hand right now. Extremely fast access. (High Temporal Locality).
	- **L1/L2 Caches:** Your open textbook or notebook, sitting right beside you on the desk. Faster than fetching from the library, but you can only keep a few open pages at once. (Good Temporal and Spatial Locality for recently used concepts).
	- **Main Memory (DRAM):** The stack of 20 books sitting on the floor nearby. You have access to a large volume of data, but getting the right information takes a few minutes (hundreds of clock cycles).
	- **Disk/SSD:** The entire university library catalog. Massive capacity, but retrieving one specific piece of information takes a long time (milliseconds/millions of cycles).
	If you keep rereading the same note card (**temporal locality**) or if you read all the adjacent sentences on a page (**spatial locality**), you reduce the need to go to the main memory, maximizing your **read throughput** and lowering your **miss rate**. Conversely, if you jump randomly between chapters in 20 different books for every question, you introduce high overhead (**conflict misses**) and slow down your overall study time.

---

# #Lecture Lectures
## Lecture 24
### “CPU cache” introduction
Core idea: build storage **between registers and RAM**—faster than RAM, slower than registers; smaller than RAM, larger than registers; implemented as **SRAM** acting as an intermediary between CPU core and DRAM.
- Cache = SRAM storage between CPU and main memory.
- New view of a load: check cache → hit fast; miss → fetch from DRAM (slow).
- Memory hierarchy: huge access-time jumps as you go down (regs → L1/L2 → DRAM → disk).
### The “new view” of a load
Instead of “CPU asks RAM and waits,” the “real” flow is:
- check cache
- hit → fast
- miss → request from RAM and wait    
1. *Memory hierarchy + “Jeff Dean numbers”*:
	The lecture shows the _huge_ jump in access time as you go down the hierarchy (registers → caches → DRAM → disk), with the well-known “Numbers every programmer should know” style analogy.
## Lecture 25


---

# #Lab Lab


---

# #Homework Homework


---
