---
type: class
status: archived
created: 2025-11-19
updated: 2025-11-21
area:
  - "[[C Language]]"
tags:
  - "#class"
  - "#Textbook"
  - "#CSAPP"
  - "#Lecture"
  - "#Lab"
  - "#Homework"
next: "[[50_Archive/Previous Classes/CSCI/CSCI 2021/Week - 11|Week - 11]]"
---
# #Textbook Textbook (CSAPP - 4.4 to 4.6)
## #CSAPP CSAPP
### 4.4 General Principles of Pipelining
Pipelining is a fundamental technique used in processor design to dramatically increase performance. The goal is to maximize **throughput**—the number of instructions completed per unit of time—even though the time required for any single instruction (**latency**) might increase slightly.
1. **Computational Pipelines**: A computational pipeline divides a long computational process into a series of smaller, sequential stages.
	- **Components**: A pipeline consists of combinational logic (which performs the actual work) followed by a **hardware register**. The register holds the result of that stage, and its update is controlled by a **clock signal**.
2. **Throughput vs. Latency**: If a total computation time of 320 picoseconds (ps) is divided into three stages, each taking 100 ps, and a register delay of 20 ps is added, the new total cycle time is only 120 ps, leading to much higher throughput (GIPS—giga-instructions per second). The time taken for an individual instruction to pass through all stages is the **latency**. In steady state, a new instruction enters the system every clock cycle.
3. **Limitations of Pipelining**: The effectiveness of a pipeline is limited by the imbalance of its stages.
	- **Slowest Stage Limit**: The throughput of the entire system is limited by the delay of the **slowest stage**. If one stage takes 510 ps and others are faster, the clock cycle must still be set to accommodate the 510 ps stage plus the register overhead.
	- **ALU and Memory**: It is often difficult to subdivide certain critical hardware units in a processor, such as the ALU and memory components, into smaller blocks with shorter delays to achieve balanced stages.
4. **Pipelining a System with Feedback**: When the output of the system is fed back as an input to later instructions, complex problems called hazards arise, which can cause erroneous computation if not handled correctly.
	- **Dependencies**: Dependencies are relationships where one instruction relies on the results or control decisions of a previous instruction.
	- **Data dependencies**: When an instruction requires data (a register value) computed by an earlier, still-running instruction.
	- **Control dependencies**: When an instruction determines the address of the next instruction (e.g., a jump instruction).
### 4.5 Pipelined Y86-64 Implementations (PIPE)
This section moves from theory to practice, building the **PIPE** processor, a five-stage pipelined model of the Y86-64 ISA, which executes instructions using five stages: Fetch, Decode, Execute, Memory, and Write Back.
1. **SEQ+: Rearranging the Computation Stages**: To prepare the sequential processor (SEQ) for pipelining, the timing of the **PC update stage** is moved to the **beginning** of the clock cycle, computing the PC value for the _current_ instruction. This slightly modified structure is called SEQ+.
2. **Inserting Pipeline Registers**: **Pipeline registers** are inserted between the five stages to create the boundaries, allowing five different instructions to run concurrently (one in each stage).
	- The registers are labeled based on the boundaries they cross: **F** (holds predicted PC), **D** (Fetch/Decode boundary), **E** (Decode/Execute boundary), **M** (Execute/Memory boundary), and **W** (Memory/Write Back boundary).
	- The overall structure of this initial model (PIPE−) uses nearly the same hardware units as SEQ, but with pipeline registers separating them.
3. **Rearranging and Relabeling Signals**: Since multiple instructions are active at once, signals must be uniquely identified by the instruction they belong to.
	- **Naming Convention**: Signals stored in a pipeline register are labeled with the register name prefix (e.g., `W_stat` is the status code of the instruction currently in the Write Back stage).
	- **Information Integrity**: It is critical that all information about a particular instruction (e.g., its calculated value and its intended destination register) remain contained within its single pipeline stage to prevent mixing results.
4. **Next PC Prediction**: To keep the pipeline full (achieving the target throughput of one instruction per cycle), the processor must predict the next Program Counter (PC) value as soon as the current instruction is fetched.
	- For most instructions (e.g., `irmovq`, `rrmovq`), the next PC is reliably determined during the fetch stage (either `valC` or the sequentially next address, `valP`).
	- For **conditional jumps** (`jXX`) or function **returns** (`ret`), the result (and thus the next instruction address) is not known until later stages (Execute or Memory). The processor must **predict** the outcome, fetch the predicted instruction, and handle the recovery if the prediction is wrong.
5. **Pipeline Hazards (Data and Control)**: Hazards are pipeline dependencies that threaten correctness and must be resolved.
	- **Data Hazards**: Occur when an instruction tries to read a register value that a previous instruction has not yet written back to the register file.
	- **Stalling (Inserting Bubbles)**: The simple solution is to **stall** the dependent instruction in the Decode (D) stage for one or more cycles. This involves holding the pipeline registers F and D fixed and injecting a **bubble** (a hardware NOP instruction) into the Execute (E) stage.
	- **Forwarding (Bypassing)**: A much faster solution is to feed the result directly back from a later pipeline stage (E, M, or W) to the Decode stage logic _before_ it is formally written back to the register file.
	- **Load/Use Hazard**: A special case where an instruction reads data from memory (`mrmovq` or `popq`) and the very next instruction tries to use that data. Since the memory read occurs in the Memory (M) stage, which is late, the data cannot be forwarded in time. This specific hazard requires a combination of **stalling the Decode stage for one cycle and forwarding** the result from the M stage.
	- **Control Hazards**: Occur when the processor fetches an instruction based on an incorrect prediction (e.g., mispredicted jump or `ret` instruction). These are handled by injecting **bubbles** into the D, E, and M stages immediately following the mispredicted instruction, clearing the incorrectly fetched instructions.
6. **Exception Handling**: The processor must handle internally generated exceptions (like `halt`, invalid instruction, or invalid address access).
	- **Precise Exceptions**: The execution must appear sequential: all instructions _before_ the excepting instruction must complete, and all instructions _after_ it must have **no effect** on the programmer-visible state (registers, memory).
	- **Status Codes**: The status code (`Stat`) is associated with the instruction as it moves down the pipeline. If an instruction causes an exception in the M or W stage, the pipeline control logic suppresses updates to state elements (like condition codes) generated by subsequent instructions.
7. **PIPE Stage Implementations**: This involves detailing the control logic (using HCL) for each stage to enable proper data flow and hazard detection.
	- **Write Back Logic**: The write ports of the register file must be fed by register IDs (`W_dstE`, `W_dstM`) originating from the Write Back stage, ensuring the correct destination register is updated for the instruction currently completing.
	- **Forwarding Logic**: Complex multiplexors (like **Sel+Fwd A** and **Fwd B**) check up to five different potential forwarding sources (e.g., ALU output from the E stage, memory output from the M stage, and results pending write back in the W stage). Forwarding sources must be prioritized; the value generated by the instruction furthest down the pipeline (closest in time) takes precedence.
8. **Pipeline Control Logic**: This logic manages the overall pipeline state using three primary mechanisms: **normal operation, stalling, and bubbling**.
	- **Stall**: Stops the clocking of a pipeline register, keeping its stored value fixed (e.g., stalling D and F registers for a load/use hazard).
	- **Bubble**: Forcibly overrides the next value written to a pipeline register with a specific signal pattern that makes it behave like a `nop` (no operation) instruction. This is used to flush incorrect instructions (after misprediction) or to delay execution (after a load/use hazard).
	- The control logic generates Boolean signals (`D_stall`, `E_bubble`, etc.) that dictate the action of each pipeline register based on the detected hazard conditions.
9. **Performance Analysis**: The PIPE processor is limited to executing at most **one instruction per clock cycle**. Therefore, the average performance measure, **CPI** (Cycles Per Instruction), can never be less than 1.0. More advanced processors achieve CPI less than 1.0 using techniques like _superscalar_ operation and _out-of-order execution_.
### 4.6 Summary
The **Instruction Set Architecture (ISA)** provides a sequential execution model, acting as an **abstraction layer** between the processor's behavior and its implementation.
- **Concurrency**: By using pipelining, the processor achieves higher performance by performing multiple operations simultaneously.
- **Complexity Management**: The architecture manages complexity and maximizes hardware utilization by creating a simple, **uniform framework** (the stages) through which all instruction types flow.
- **ISA Fidelity**: Despite complex, concurrent execution, careful design (using hazard detection, stalling, and forwarding) ensures that the PIPE processor computes the same final result as the abstract sequential ISA model.

---

# #Lecture Lectures
## Lecture 21
### Sequential CPU (SQU)
- **ALU** — does math and logic
- **Register file** — stores operands/results
- **RAM** — stores data and instructions
- **Clock** — controls timing
- **Buses** — move data between all components
All of these form a **Sequential CPU**, meaning: Each instruction executes _completely_ in one clock cycle. That’s why it’s sometimes called a **Single-Cycle CPU**.
- Each instruction from fetch to writeback — must:
	1. Be fully computed by the ALU and logic circuits.
	2. Update memory and registers by the **next clock tick**.
That means: During one cycle → all five stages (Fetch → Decode → Execute → Memory → Writeback) happen.
- At the _next_ rising clock edge → results are stored, and the next instruction begins. This is the simplest working CPU model — before adding **pipelining** (which overlaps stages).
These stages were introduced in [[50_Archive/Previous Classes/CSCI/CSCI 2021/Week - 8#Lecture 20]], but Lecture 21 now shows _how each stage works in hardware_.

| Stage            | Description                                                      | What Happens Electrically                                                                                                           |
| ---------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **1. Fetch**     | Read the next instruction from instruction memory.               | Program Counter (PC / `%rip`) provides address → instruction bytes read from RAM.                                                   |
| **2. Decode**    | Parse the instruction to identify opcode, registers, immediates. | Control logic splits bits into `icode`, `ifun`, `rA`, `rB`, and immediate value. The register file outputs `valA` and `valB`.       |
| **3. Execute**   | Perform arithmetic or logic operation.                           | ALU computes result: `valE = valB + valC` (for addq), or compares for jumps.                                                        |
| **4. Memory**    | Load or store data (if needed).                                  | If `mrmovq`, read from memory at address `valE`. If `rmmovq`, write to memory.                                                      |
| **5. Writeback** | Write results back to registers.                                 | The `valE` or `valM` (from memory) are written to destination register (`dstE` or `dstM`). Also update `%rip` for next instruction. |
**At the end of the cycle**, the new register values and memory contents are stored permanently — ready for the next instruction.
### Y86 Fetch Hardware
- Instruction bytes come from **Instruction Memory**.
- The **first byte** is split:
    - **4 bits = opcode** (main operation)
    - **4 bits = function** (sub-type)
- Next bytes: register IDs and immediate values.
- The PC (program counter) increments to the address of the next instruction.
### Y86 Execute Hardware
At this stage:
- `valA`, `valB`, `valC` are already fetched.
- They travel on **buses** into the **ALU**.
- ALU performs addition, subtraction, AND, OR, etc.
- **Condition codes (flags)** are set if needed (e.g., ZF, SF, OF).
- For jump instructions:
    - A **condition signal (cond)** decides whether to take the branch.
### The Clock Coordinates It All
#### SQU
“Each instruction is processed in one clock cycle.” That means:
- All signals propagate through logic between two rising edges. 
- At the next edge, results are committed.
⏱️ But — There’s a Limit: The Critical Path. The **critical path** = the _slowest_ route through the hardware. It includes:
- Memory access delays
- ALU computation
- Signal propagation through buses and multiplexers
The **clock period** must be **longer than** this delay, or the CPU will fail (signals won’t settle before the next tick).
> The **shorter** the critical path → the **higher** the possible clock speed. This explains why faster CPUs require better circuit design and smaller transistors

Within that cycle:
- Combinational logic is busy working. 
- Nothing is stored until the clock edge.
On the rising edge:
- All changes take effect simultaneously (registers, memory, PC).
#### Pipelined CPU
- The clock marks **transition between stages.**
- One instruction finishes when it leaves Writeback.
- One new instruction enters Fetch each cycle.
- Clock frequency can increase (because each stage is shorter than whole instruction).
- Clock period = time for **slowest stage**, not entire critical path.
## Lecture 22 & 23
### Pipelining
A **pipelined CPU** executes different instructions in different stages _simultaneously_.  
Each stage has dedicated hardware and each hardware group works on a different instruction every cycle.
- **Making Pipelining Work**: 
	1. Stage Registers: New hardware added between stages: **pipeline registers**. **Cycle Steps**:
		1. Stage _n_ executes instruction _i_ → stores its result into register between stages (_n_ → _n + 1_).
		2. On next clock edge, that register **latches** results.
		3. Stage _n_ starts instruction _i + 1_, while stage _n + 1_ works on instruction _i_.
	- All stages busy → max utilization.
	-  But registers add delay → slightly higher latency
- **Performance Metrics**
	- *Throughput* : Amount of work done per unit time.
		- Sequential: low throughput (1 instr per long cycle)
		- Pipelined: high throughput (1 instr per short cycle after fill)
	- *Latency*: Time for one instruction to finish (from Fetch → Writeback).
		- Sequential: low (1 long cycle)
		- Pipelined: higher (multiple short cycles per instr)
	- Classic trade-off across all systems (e.g., CPUs vs GPUs):
		- CPUs → low latency; GPUs → high throughput
### Pipeline Hazards
Pipelining is powerful but creates new problems (**hazards**) that didn’t exist in single-cycle CPUs. There are three broad kinds (only the first two are covered deeply here):

| Type                  | Cause                                                               | Example                                     |
| --------------------- | ------------------------------------------------------------------- | ------------------------------------------- |
| **Data Hazard**       | An instruction depends on data from another still in the pipeline.  | `addq %rax,%rbx` right after `movq $1,%rax` |
| **Control Hazard**    | We don’t yet know the next instruction address because of a branch. | `je SOME_LABEL`                             |
| **Structural Hazard** | Two stages compete for the same hardware resource (rare in Y86).    | Fetch and Memory both need the memory bus.  |
If unhandled, hazards make the CPU use _old_ or _wrong_ data.
#### Data Hazard
```bash
movq $1, %rax   # I1 
addq %rax, %rbx # I2`
```
- I2 needs updated `%rax` value during Decode (Cycle 3).
- But I1 writes `%rax` only in Writeback (Cycle 5).
- I2 reads the old value → **incorrect result.** 
1. **Rearrange Instructions**: Insert unrelated instructions between dependent ones to let earlier results finish.
```bash
movq $1, %rax 
movq $2, %rcx 
movq $3, %rdx 
movq $4, %rdi 
addq %rax, %rbx`
```
- ✅ All hardware busy (100% utilization)
- ❌ Programmer must know pipeline depth – error prone & non-portable
- ❌ If no spare work, insert “no-ops” (nop instructions) → lower utilization
2. **Stalling**:Hardware detects dependency and automatically pauses pipeline until data ready.
	- CPU inserts temporary “bubbles” (fake nops).
	- Stalls only when required → simpler for programmers.
	- Throughput drops temporarily but correctness preserved.
	Example:
```bash
movq $10, %rdx
movq $3,  %rax
  bubble
  bubble 
  bubble 
addq %rdx, %rax
```
#### Forwarding
Also called **bypassing**. Rather than waiting for a value to reach the register file in Writeback, the CPU **forwards** the result signal directly from a later stage to an earlier one. *Concept*:
- Normally: Decode reads old register values; Writeback updates them later. 
- Forwarding: Add extra buses that carry ALU results (backward) to Decode.
Implementation Details:
1. Add new wires (e.g., `W_valE`) from Writeback → Decode.
2. Hardware detects when `rA` or `rB` = the destination register of an instruction still in Execute/Mem/Writeback.
3. Use multiplexers to choose between register value and forwarded value.
4. Similar paths exist for:
    - Memory → Decode (for loads/stores)
    - Execute → Decode (for ALU results)
Why it works: In hardware, a “value” is just an electrical signal on a bus. We can route that signal directly before it is written into the register file.
#### Load/Use Hazard
```bash
movq 4(%rdx), %rax  # I1 (load from memory) 
addq %rax, %rbx     # I2 (uses rax)
```
- Here, the value of `%rax` is only known after the **Memory stage**, because it comes from RAM.
- But I2 needs it in Decode stage → forwarding alone isn’t enough.
1. Fix
	- Stall for 1 cycle (so I1 reaches Memory).
	- Then forward from Memory → Decode.  
	    This combines stall + forwarding.
#### Control Hazard
Occurs when the CPU does not yet know _which instruction address to fetch next_.
Example:
```bash
cmpl $1, %rcx 
je   SOME_LABEL
```
When `je` is in Decode, the CPU must already be fetching the next instruction – but should it be the next sequential address or the branch target? We won’t know until the comparison finishes Execute.
1. Option 1: Stall Until Decision
	- Wait for the branch result before fetching.
	- Wastes cycles no matter what the outcome is.
2. Option 2: *Branch Prediction*: Instead of waiting, **guess** and continue fetching down the predicted path.
	- If prediction is correct → no penalty.  
	- If wrong → discard (f lush) wrong instructions and restart fetching the correct path.
	- Prediction Strategies

| Strategy                                  | Rule                                                                    | Approx. Accuracy |
| ----------------------------------------- | ----------------------------------------------------------------------- | ---------------- |
| Always taken                              | Assume every branch jumps                                               | ≈ 60 %           |
| Never taken                               | Assume no branches jump                                                 | ≈ 40 %           |
| Backward Taken, Forward Not Taken (BTFNT) | Assume loops (backward jumps) are taken and forward jumps (ifs) are not | ≈ 65 %           |
If prediction fails → **pipeline flush**, discarding all in-flight wrong-path instructions. 
#### Functions and Returns
- `call` is simple – target address is encoded in the instruction → acts like an unconditional jump. 
- `ret` (return) is harder – the target address comes from the stack (memory) → hard to predict.
- Real CPUs use a small **Return Address Stack** to remember recent calls and predict the return target.

---

# #Lab Lab - 8
## Time Complexity
- If the body is **O(1)** (constant operations), whole loop is **O(n)**.
- If the body itself calls something **O(n)**, then total becomes **O(n) * O(n) = O(n²)**.
- If you have nested loops: That’s clearly **O(n²)**.
> **Time complexity = (# of iterations) × (cost of each iteration)**

Finding Time complexity: 
- **Choose the input size variable**
    - Here: `n = list->size` or `n = num_elems`. 
- **Identify loops and recursion**
    - For each loop, ask: how many iterations in terms of `n`?
- **Look inside the loop body**
    - Are you doing only O(1) work?
    - Or calling another function whose complexity you know?
- **Multiply**
    - `loop_iterations × cost_per_iteration`.
    - Add the contributions of different stages:
        - If program does `Stage A (O(n²))` + `Stage B (O(n))`, total is **O(n²)** (take the dominant term).
- **Ignore fixed constants**
    - `for (i = 0; i < 1000; i++)` is **O(1)** if 1000 doesn’t depend on input size.
1. `list_find(list_t *list, int value)` — the intentionally bad one. Let’s plug in what we know:
	- Outer loop: `for (i = 0; i < list->size; i++)` → runs **n** times.
	- Inside: every iteration calls `list_get(list, i)`.
	- We already know:`list_get` in worst case is **O(n)**.
	- So **per iteration** of `list_find`
		- Cost ≈ O(n).
	- Total: Outer loop runs n times × each call O(n) → **O(n²)** overall.
2. **Main**: 
	- **Build data structure**:
	    - Linked list: `list_init` + `list_add` in a loop → overall **O(n²)**.
	    - Array: `malloc` + single loop to fill → **O(n)**.
	- **Search stage**:
		- Runs **2 × n** searches (for values `0..2n-1`):
	        - If `mode = list_find`: each call = O(n²) → total search time O( (2n) * n² ) = **O(n³)**.
	        - If `mode = list_find_student`:each call = O(n) → total search time O( (2n) * n ) = **O(n²)**.
	        - If `mode = array_find`: each call = O(n) → total search time O( (2n) * n ) = **O(n²)**.
	- **Validate & print**
	    - `validate_results` is O(n) on 2n elements → O(n).
	- Original `list_find` is much worse than `list_find_student`.
	- Linked list searching is slower than array searching because of **memory layout**, not just big-O.
## Why Arrays Are Faster than Linked Lists
(Even When Both Are O(n))
1. Array layout: `[ 0 ][ 1 ][ 2 ][ 3 ][ 4 ]  (contiguous memory)`
	- linear in memory
	- predictable pattern
	- CPU prefetcher loads upcoming values
	- cache hits are extremely likely
2. Linked list layout: `node1 → node2 → node3 → node4 → ... (each node allocated anywhere in memory)`
	- scattered around heap
	- cache misses on almost every node
	- pointer chasing = slow
	- no prefetch advantage
**Result**: Even though both are O(n), arrays run MUCH faster.

---

# #Homework Homework - 8
## `time` reports
```bash
real = wall clock time (how long YOU waited) 
user = how long the CPU spent executing YOUR program 
sys  = how long the CPU spent inside the OS for your program
```
1. Practical rules
	- Use: `time ./prog args...`
	- `real` is the number used for performance comparisons.
## Key Takeaways
1. *Pipelining*: Pipelining increases _throughput_ (instructions per second), but does **not** reduce individual instruction latency.
2. **Superscalar (multiple workers at each stage)**
	- CPU has multiple ALUs, multiple multipliers, etc.
	- It can run **multiple independent instructions at the same time**.
	**Key idea:** If instructions do NOT depend on each other, they can run _in parallel_.
### Timing Rules
1. **Multiply is slower than Add**: `ret *= del;   → higher latency ret += del;   → lower latency`
	So: A loop with a multiply per iteration is **slower** than a loop with an add per iteration (same dependency structure).
2. **Same destination = dependency chain (slow)** Example:
	`retA += delA; retA += delB;      // depends on previous result`
	- Second instruction **must wait** for the first  
	    → no parallelism  
	    → pipeline stalls
    So: Operations on the **same variable** inside the same iteration are slower.
3. **Multiple multiplies on different vars ≈ same time as one multiply** Example:
	`retA *= del; retB *= del;`
	- Multiplier is pipelined (can start new multiply before old finishes)
	- Often has spare throughput
	- Two independent chains
	So: Two independent multiplies ≈ one multiply.
4. **Adding multiple independent operations doesn't necessarily make the loop slower** Example: `retA += del; retB += del; retM *= del;`
	- Multiply determines the loop's critical path (slowest chain) 
	- Adds fit into idle integer ALUs
	- No dependencies → CPU overlaps everything
	So: A loop with 2 adds + 1 multiply can take **almost the same time** as a loop with only 1 multiply.

---
