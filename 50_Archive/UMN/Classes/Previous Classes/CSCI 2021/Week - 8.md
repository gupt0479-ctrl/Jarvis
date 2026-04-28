---
type: class
status: archived
created: 2025-11-12
updated: 2025-11-14
area:
  - "[[C Language]]"
tags:
  - "#class"
  - "#Textbook"
  - "#Lab"
  - "#Homework"
  - "#CSAPP"
  - "#Lecture"
next: "[[50_Archive/UMN/Classes/Previous Classes/CSCI 2021/Week - 9|Week - 9]]"
---
# #Textbook Textbook (CSAPP - 4.1 to 4.3)
## #CSAPP CSAPP
### 4.1 The Y86-64 Instruction Set Architecture (ISA)
The Y86-64 instruction set is a simplified subset of the x86−64 ISA, created specifically for studying processor implementation. While designing a processor to implement Y86-64, designers deal with many of the same challenges faced by real processor architects.
- **Programmer-Visible State**: To run programs, the Y86-64 processor maintains several components that reflect the current state of execution:
	1. **Program Registers**: A collection of 15 registers is maintained.
	2. **Condition Codes (CC)**: These store status information resulting from the most recent operation.
	3. **Program Counter (PC)**: Stores the address of the next instruction to be executed.
	4. **Memory**: A conceptual large array of bytes referenced using virtual addresses.
	5. **Status Code (Stat)**: Indicates the overall state of execution (e.g., normal operation or an exception like a `halt` instruction or invalid address access).
	The instruction set is complete enough to allow us to write programs manipulating integer data.
- **Instruction Encoding**: Y86-64 instructions are translated into binary byte sequences.
- **Fixed Structure**: Every instruction starts with a single byte divided into two 4-bit parts:
	- **Instruction code $(icode)$** (high-order) and the **function part $(ifun)$** (low-order):
		- The `icode` identifies the instruction type (e.g., jump, move, or arithmetic operation), and the `ifun` specifies variants (e.g., which specific arithmetic operation to perform).
- **Variable Length**: Instructions can vary in length from 1 to 10 bytes.
- **Addressing**: Some instructions require an additional 8-byte constant word, which serves as immediate data, memory displacement, or the **absolute address** for branch and call destinations. Using absolute addressing simplifies processor design compared to the PC-relative addressing found in x86−64.
### 4.2 Logic Design and the Hardware Control Language (HCL)
Processor implementation relies on digital hardware components that compute functions on bits and store bits in different kinds of memory elements.
- **Digital System Components**: Three major components are required to implement a digital system:
	1. **Combinational Logic**: These circuits have outputs that depend **only** on their current inputs; they have no memory.
		- **Logic Gates**: Basic building blocks (AND, OR, NOT) that operate on bits.
		- **ALU (Arithmetic Logic Unit)**: A key combinational circuit that performs operations like addition, subtraction, AND, or XOR, based on a control input.
		- **Word-Level Circuits**: Large networks of gates assembled to operate on data words (groups of bits representing integers, addresses, etc.).
	2. **Memory Elements (Sequential Logic)**: These circuits store bits over time.
		- **Hardware Registers**: Clocked storage devices used to hold elements of the program state (e.g., the PC, Status, and Condition Codes).
		- **Memory**: Large storage arrays (like the Instruction Memory and Data Memory).
	3. **Clock Signals**: These regulate the update of memory elements. Values only propagate from a hardware register's input to its output once per clock cycle, on the **rising clock edge**.
- **Hardware Control Language (HCL)**: HCL is a simple language used to describe the **control logic**—the part of the system that dictates what operations happen and how data is routed.
	1. **Signals and Comparisons**: HCL declares signals as `int` (word-level signals, size unspecified for simplicity) or `bool` (single-bit signals). It allows words to be compared for equality using the syntax `A == B`.
	2. **Case Expressions (Multiplexing)**: HCL uses `case` expressions, similar to C's `switch` statements, to describe multiplexors (circuits that select one output from several inputs). The selection expressions are evaluated sequentially, and the first one that yields 1 is selected. A selection expression of `1` is used to specify a default case.
	3. **Set Membership**: A concise expression to test if an integer value matches one of a number of possible matching values is the set membership test: `iexpr in {iexpr1, iexpr2, . . . , iexprk}`.
- **The Register File**: The Register File stores the program registers.
	- It has multiple read ports (which behave like **combinational logic**) and multiple write ports (whose updates are controlled by the **clock signal**).
	- A write occurs to the register specified by the Register ID on input `dstW` when the clock rises. If `dstW` is set to the special ID value **0xF** (RNONE), no program register is written.
	- A critical timing property: If the same register is read and written simultaneously, the data output on the read port transitions from the old value to the new value as the clock rises to start the next cycle.
### 4.3 Sequential Y86-64 Implementations (SEQ)
SEQ is the simplest processor model. Its core principle is that it executes a complete Y86-64 instruction entirely within a **single, long clock cycle**. All updates to the programmer-visible state occur simultaneously at the end of the cycle.
- **Organizing Processing into Stages**: All Y86-64 instructions are forced through a uniform sequence of six stages:
	1. **Fetch**: The processor reads the instruction bytes from the instruction memory and determines the address of the next instruction, denoted as `valP`.
	2. **Decode**: The register file is accessed to retrieve up to two source operands, `valA` and `valB`, based on the register identifiers present in the instruction.
	3. **Execute**: The ALU performs the required computation (e.g., arithmetic calculation, address calculation, or conditional test) and potentially sets the condition codes (CC).
	4. **Memory**: Data is either read from or written to the main data memory. The value read is referred to as `valM`.
	5. **Write Back**: Up to two results are written back to the register file. Register file write port E is used for values calculated by the ALU (`valE`), and port M is used for values read from memory (`valM`).
	6. **PC Update**: The Program Counter (PC) is updated to the address of the next instruction.
	The processor loops indefinitely through these stages, stopping only when an exception occurs (such as executing a `halt` instruction or attempting an invalid memory access).
- **SEQ Timing: The No Reading Back Principle**: Since SEQ completes an entire instruction in one clock cycle, a crucial design constraint must be followed:
	- **No Reading Back**: The processor must **never** need to read back state (like a register value) that was updated by the current instruction in order to complete the processing of that same instruction.
	- **Simultaneous Updates**: All changes to the programmer-visible state (registers, memory, condition codes, and PC) must happen **at the same time** when the clock rises to begin the next cycle.
	For example, when `pushq` is implemented, the new stack pointer address (`valE`) is generated combinatorially (in the Execute stage) and then used simultaneously as the address for the memory write and the data for the register write to `%rsp` (in the Write Back stage).

---

# #Lecture Lectures
## Lecture 19
You’ve descended the abstraction stack:
```c
Python → C → Assembly → Machine Code → Circuits (Hardware)
```
Every modern computer follows the **stored-program model** (von Neumann architecture):

| Component        | Function                                                     |
| ---------------- | ------------------------------------------------------------ |
| **Memory**       | Stores _both_ data and instructions (as binary)              |
| **CPU**          | Executes instructions sequentially, reading them from memory |
| **Control Unit** | Fetches, decodes, and dispatches instructions                |
| **ALU**          | Performs arithmetic & logic                                  |
| **Registers**    | Temporary fast storage for operands and addresses            |
🧠 Key idea: _Instructions themselves are just data in memory._ The CPU interprets those bit patterns as actions.
### Machine Language
Assembly is a _human-readable_ layer over **machine code** — sequences of bits representing operations.
1. Basic format: Each instruction = **opcode + operands**

| Example (bits) | Meaning                                                                      |
| -------------- | ---------------------------------------------------------------------------- |
| `0xFA2`        | Op = `0xF` → ADD operation • Operand 1 = Register A • Operand 2 = Register 2 |
Machine code is unambiguous - every bit position has a fixed meaning.
#### Y86 – A Simplified x86
Contains a subset of x86 operations.
- Only the q variants of the instructions we’ve seen before. Splits the versatile `movq` instruction into a few different instructions.
	- One to move from register to memory, memory to register, etc. 
- Bottom Line: Instructions are bit sequences, just like numbers. We interpret substrings within each sequence to identify operation and operands. ISA standardizes all this too!
- Instruction encoding principles:
	1. **First byte** → opcode + function bits
	2. **Next bytes** → register IDs, constants, and addresses
	3. **Little Endian** ordering (least-significant byte stored first)
Example – encoding `rmmovq %rax, 2021(%rcx)`:
	`0x40 01 E5 07 00 00 00 00 00 00`
		- `0x40` = opcode (store register to memory)
		- `01` = register IDs (%rax → 0, %rcx → 1)
		- `E5 07 00 00 00 00 00 00` = displacement 2021 (0x07E5) in little endian.
### Circuits
A **digital circuit** is a network of **logic gates** built from transistors.  
Each wire can carry only one of two voltage states:

| Voltage Level         | Logical Value |
| --------------------- | ------------- |
| Low (≈ 0 V)           | 0             |
| High (≈ 5 V or 3.3 V) | 1             |
Binary works perfectly because physical devices can easily detect two stable states.
#### Logic Gates - The Building Blocks
For truth tables:

| Gate    | Symbol | Boolean Rule               | Description         |
| ------- | ------ | -------------------------- | ------------------- |
| **NOT** | ¬A     | Output = opposite of input | Inverter            |
| **AND** | A·B    | 1 if both A,B = 1          | “Both must be true” |
| **OR**  | A + B  | 1 if A or B = 1            | “Either true”       |
| **XOR** | A ⊕ B  | 1 if A≠B                   | “Exactly one true”  |
![[Pasted image 20251107000101.png]]
These gates are physically implemented by _transistors wired together._
### Combinational Logic - Building Bigger Functions
You can connect gates to form circuits whose outputs depend only on current inputs.
1. **Bit Equality**: Circuit that outputs 1 if two bits are equal: `out = (A AND B) OR (NOT A AND NOT B)`
2. **Multiplexer (MUX)**: A “selector” circuit choosing between two inputs `a` and `b` based on control bit `s`.

| a   | b   | s   | out   |
| --- | --- | --- | ----- |
| 0   | 1   | 0   | a (0) |
| 0   | 1   | 1   | b (1) |
Boolean form: `out = (¬s · a) + (s · b)`
	- When `s=0` → choose `a`.
	- When `s=1` → choose `b`.
- MUX = foundation for conditional operations, like if/else or selecting an ALU operation.
- **Arithmetic Logic Unit (ALU)**: Supports 2-bit operands, Supports operations XOR, AND, OR, ADD.
	- Important to note: multiplexer doesn’t say what to compute.
	- Every operation is always computed, mux just says which to pass through
	- You can’t “turn off” parts within a circuit, only ignore them
	1. **Half Adder**: Computes sum and carry for single bits `a,b`:

| Output    | Boolean Expression |
| --------- | ------------------ |
| Sum `s`   | `a XOR b`          |
| Carry `c` | `a AND b`          |
2. **Full Adder**: Adds bits `a`, `b`, and carry-in `cin`:

| Output       | Boolean Expression                |
| ------------ | --------------------------------- |
| Sum `s`      | `a XOR b XOR cin`                 |
| Carry `cout` | `(a · b) + (a · cin) + (b · cin)` |
3. **Ripple Carry Adder**: Connect several full adders in series:
	- Each bit’s carry out feeds next bit’s carry in.
	- This creates a 4-, 8-, or 64-bit adder.
	- Final carry out indicates overflow.
	This is literally how CPUs perform addition in hardware.
### From Addition to Subtraction
In binary arithmetic: `A - B  =  A + (Two’s Complement of B)`
To negate B:
1. Invert each bit ( `NOT B` ) 
2. Add 1 → handled by initial carry-in of 1
The ALU implements subtraction by **feeding an inverted B** into the adder and setting carry-in = 1.
## Lecture 20
Combinational logic **can’t remember** anything.  
If the input changes, the output changes instantly — there’s no concept of _time_ or _history_. But computers need memory:
- To remember variables. 
- To store intermediate results.
- To maintain control flow (like program counters).
So, we need **state elements** — circuits that retain values.
### Sequential Logic - Circuits That Remember
Definition: A **sequential circuit** combines:
	- **State elements** (which store information) 
	- **Combinational logic** (which computes new information)
They update their state **only at certain times**, governed by a **clock**. Analogy:
	Think of the CPU as a classroom:
	- Combinational logic = students doing work immediately when given input.
	- Clock = the teacher saying, “Time’s up, everyone pass your work forward!”
	- State elements = notebooks storing what they’ve written.
1. **The Clock** — The CPU’s Heartbeat (New Concept). What It Is: A **clock** is a circuit that generates a **square wave**, a signal that flips between 0 and 1 at fixed intervals.
```c
 _       _       _
| |_____| |_____| |_____
 ↑       ↑       ↑
 rising edges → when updates happen
```
- **Frequency (Hz)**: how often it oscillates (e.g., 3 GHz = 3 billion cycles/sec)
- **Clock period**: time for one full up-and-down cycle.
- Why It Matters:
	- The **clock** synchronizes every sequential element (registers, memory, etc.).
	- Most circuits update on the **rising edge** of the clock signal.
	That’s how we keep millions of tiny logic gates working in harmony.
### The Flip-Flop - Storing One Bit (New Concept)
A **flip-flop** is the smallest state-holding element — it can store **one bit**. Behavior:
- Has an **input (d)** and **output (q)**. 
- Constantly outputs its _current_ value.
- On a **rising clock edge**, it captures whatever’s on `d` and stores it in `q`.

| Signal | Meaning                                 |
| ------ | --------------------------------------- |
| `d`    | Data input (next value)                 |
| `q`    | Stored output (current value)           |
| `clk`  | Clock signal controlling when to update |
Timing Requirements: Because hardware isn’t instantaneous:
	- **Setup time:** Data input must be stable _a little before_ the clock edge.
	- **Hold time:** Data must remain stable _a little after_ the clock edge.
	- **Clock-to-q delay:** Time it takes for `q` to reflect the new value.
	These constraints ensure data doesn’t get corrupted by racing signals.
### Hardware Registers — Storing Many Bits
A register is just a **collection of flip-flops** that update together. Example:
- 64 flip-flops in parallel → 64-bit register.
- Each bit has: `d_i → flip-flop_i → q_i`
All flip-flops share the same clock line, so the entire register updates _synchronously_.
1. **Connection to Assembly**: In assembly, we also talk about “registers” (`%rax`, `%rbx`, etc.).
	- In _assembly_, a **register** = a named storage location.
	- In _hardware_, a **register** = a physical circuit of flip-flops storing that data.
	So `%rax` in your code corresponds to one of many physical 64-bit hardware registers. There are also **hidden registers** used by the CPU internally (e.g., pipeline registers, condition codes, instruction buffers).
2. **The Register File**: A **register file** is a _collection_ of registers accessed as a group — the CPU’s “workspace.” Functions:
	- Store all general-purpose registers (`%rax`, `%rbx`, `%rcx`, …).
	- Provide **two read ports** and **one write port**:
	    - Read port A: read value of `srcA`.
	    - Read port B: read value of `srcB`.
	    - Write port W: write new value to `dstW`.
3. Implementation:
	- Each register has a numeric ID (e.g., `%rax` = 0, `%rcx` = 1, etc.).
	- **Multiplexers (MUXes)** select which register to read/write based on those IDs.
	- Data travels across **buses** — groups of 32 or 64 parallel wires carrying data.
	 MUX + register file design = allows random access to any register in a single cycle.
### Random Access Memory (RAM) - The Large-Scale Storage
Now that we can store a few registers, we need a much **larger memory** for programs and data. RAM Characteristics:

| Property                   | Meaning                                   |
| -------------------------- | ----------------------------------------- |
| **Random Access**          | Every address can be reached equally fast |
| **Volatile**               | Loses data when power is off              |
| **Addressed by bytes**     | Each memory cell has an address           |
| **Organized sequentially** | Stack → Heap → Globals → Text (code)      |
1. RAM Types:

| Type               | Description                                     | Used For                 |
| ------------------ | ----------------------------------------------- | ------------------------ |
| **SRAM** (Static)  | Fast, expensive, holds data as long as powered  | CPU caches, registers    |
| **DRAM** (Dynamic) | Slower, cheaper, must be periodically refreshed | Main memory (RAM sticks) |

### Sequential Circuits — Combining Logic + State
Once we connect:
- Combinational logic (e.g., ALU, MUXes)
- State elements (flip-flops, registers, RAM)
- A clock to synchronize updates
We get a **sequential circuit**, capable of _multi-step computation_ over time. That’s what makes a real computer possible.
1. Sequential Y86 Implementation — Building the CPU: The lecture shows how the **Y86 architecture** (a simplified x86) can be implemented using all these hardware building blocks.
2. Components Recap:

| Component         | Purpose                                |
| ----------------- | -------------------------------------- |
| **ALU**           | Executes arithmetic/logic instructions |
| **Register File** | Stores operands & results              |
| **Clock**         | Coordinates timing                     |
| **RAM**           | Stores instructions & data             |
| **Buses**         | Move 64-bit values between units       |
All connected together in a pipeline that executes one instruction at a time.
### The 5 Stages of a Sequential CPU
Every modern processor executes instructions in these **five stages** — introduced here and used throughout the rest of the course (especially pipelining and performance).

| Stage            | Description                                                                        |
| ---------------- | ---------------------------------------------------------------------------------- |
| **1. Fetch**     | Get instruction from memory; increment Program Counter (%rip).                     |
| **2. Decode**    | Determine opcode; read operands (`valA`, `valB`) from registers.                   |
| **3. Execute**   | ALU performs arithmetic/logic; compute memory addresses; evaluate jump conditions. |
| **4. Memory**    | Load or store data (read/write RAM).                                               |
| **5. Writeback** | Write results back to register file (or update PC for next instruction).           |
These stages happen **sequentially** for each instruction in a simple CPU. Later, pipelining will let multiple instructions overlap.
### Hardware Description Languages (New Topic)
Before CPUs were built by hand on drafting paper; now we use **HDLs** (Hardware Description Languages) to describe and simulate logic.

| HDL         | Description                             |
| ----------- | --------------------------------------- |
| **VHDL**    | Verbose, Ada-like hardware language     |
| **Verilog** | C-style syntax, widely used in industry |
Example — VHDL for ALU
```c
case OPER is
   when "00" => OUTP <= A_IN xor B_IN; -- XOR   
   when "01" => OUTP <= A_IN and B_IN; -- AND   
   when "10" => OUTP <= A_IN or B_IN;  -- OR   when "11" => OUTP <= A_IN + B_IN;   -- ADD 
end case;
```
This looks like software but **actually describes gates and wires**.


---

# #Lab Lab - 7
## Quiz
1. Question: which instructions can extend/grow the stack?
	- `subq $20, %rsp`: Stack grows “downward” to smaller addresses. Subtracting from `%rsp` reserves space → **yes, grows stack**.
	- `pushq $99`: `pushq` does two things:
	    1. `%rsp -= 8`
	    2. store 8 bytes on stack  
	        That definitely grows stack → **yes**.
	- `pushl %ebx`: In AT&T syntax, `pushl` pushes 4 bytes (32-bit). It still decreases `%rsp` and stores → still grows. (In x86-64 you normally see `pushq`, but the concept is: a push extends the stack.). 
		- So **yes**.
	Therefore: **All of the above** is correct
2. `callq foo`:
	1. pushes the **return address** (8 bytes) onto the stack
	2. jumps to `foo`
	Pushing return address means `%rsp -= 8`.
	So after a call:
	- `%rsp` changed by **-8**
	- if it was divisible by 16 before the call, it becomes divisible by 8 but **not** 16 after the call.
3. You’re told:
	- locals need **36 bytes** in memory
	- but you will call functions inside this function
	- call requires `%rsp` aligned to 16 **at the moment of the call**    
	Key rule (System): Before executing a `call`, `%rsp` must be **16-byte aligned**. 
	But inside a function, you already have a return address on the stack from whoever called you. 
	- So at function entry, `%rsp` is typically **8 mod 16**. That’s why we add “padding” so that when we call something, the stack is aligned.
	- *The lab’s logic*: 
		- If you allocate exactly 36 bytes: `%rsp` shifts by 36 → that’s 4 mod 16 → alignment will be wrong for calls.
		- If you allocate 40 bytes: `%rsp` shifts by 40 (8 mod 16). Combined with the extra 8-byte return address effect, you land back on a 16 boundary when making calls. That’s exactly what the quiz answer says: “40 bytes; this + 8 bytes for return address means aligned.”
    - So the right answer is **40 bytes**, not 36 or 48.
## Code
```bash
subq $56, %rsp
...
addq $56, %rsp
```
You only *need* 36 bytes for 9 ints, but they allocated 56. Why?
Two reasons:
1. **space for locals (36)**  
2. **padding to maintain 16-byte alignment across multiple calls**. 
	Remember: `call` pushes 8 bytes. You want `%rsp` aligned to 16 right before each `call`.
	Allocating 56 is a safe “round up”:
	- 56 is divisible by 8, and it gives comfortable alignment + space (and many compilers over-allocate similarly).
	So this matches the quiz mindset: don’t just allocate “bare minimum” if it ruins alignment. 
3. How to “translate” a C call `order3(&r,&t,&v)` into assembly, C call: `order3(&r,&t,&v);`
	Assembly must:
	1) put arg1 (a pointer) into `%rdi`
	2) arg2 into `%rsi`
	3) arg3 into `%rdx`
	4) `call order3`
	And “&r” means “address of r” = `%rsp + offset`.
	That’s why you see:
```bash
movq %rsp, %rdi       # &r  (same as leaq 0(%rsp), %rdi)
leaq 4(%rsp), %rsi    # &t
leaq 8(%rsp), %rdx    # &v
call order3
```
Why `movq %rsp, %rdi` works for &r: Because r is at offset 0. So the address of r *is* just `%rsp`. They even comment that `leaq 0(%rsp), %rdi` is equivalent.
4. Why we use `movl` for ints but `movq/leaq` for addresses:
	- `r`, `t`, etc. are **int** → 4 bytes → use `movl` to store/load them.
	- `&r`, `&t` are **addresses** → 8 bytes on x86-64 → use `leaq` / `movq` into the argument registers.
	That’s why:
```bash
movl $17, 0(%rsp)    # store int
leaq 0(%rsp), %rdi   # compute address (8-byte pointer)
```
5. How the “TODO blocks” were solved (order3 calls)
	Second call: `order3(&q,&e,&d)`
	In C: `order3(&q, &e, &d);`
	In assembly, q/e/d are at 12/16/20 offsets, so:
```bash
movl $5,  12(%rsp)
movl $9,  16(%rsp)
movl $2,  20(%rsp)
leaq 12(%rsp), %rdi
leaq 16(%rsp), %rsi
leaq 20(%rsp), %rdx
call order3
```
That is literally “repeat the pattern with different offsets”.
	Third call: `order3(&i,&j,&k)`
	In C: `order3(&i, &j, &k);`
	Offsets 24/28/32:
```bash
movl $24, 24(%rsp)
movl $27, 28(%rsp)
movl $29, 32(%rsp)
leaq 24(%rsp), %rdi
leaq 28(%rsp), %rsi
leaq 32(%rsp), %rdx
call order3
```
(Notice: the comment table says `i` init is 24; the C file you pasted earlier said 25 for i, but your assembly uses 24 and expects output `24 27 29` — the lab’s expected output confirms 24. Follow the lab’s assembly file + expected output.)
6. How `printf` calls work and why `%eax=0` is required
	Example given:
```bash
leaq .FORMAT1(%rip), %rdi
movl (%rsp), %esi
movl 4(%rsp), %edx
movl 8(%rsp), %ecx
movl $0, %eax
call printf@PLT
```
Why these registers?
- System V calling convention:
	- arg1 → `%rdi`
	- arg2 → `%rsi`
	- arg3 → `%rdx`
	- arg4 → `%rcx`
	So printf format string is arg1, then the three ints are args 2–4.
Why `movl $0, %eax`?
For variadic functions like `printf`, `%al` (low 8 bits of `%rax`) is used to indicate how many vector registers are used for floating-point args. Since there are none here, it must be 0. That’s why the lab forces it.
- Then the TODO blocks for the other two printf calls are the same pattern with different format labels and offsets.
7. Why we must restore the stack before returning
	If you do:
```bash
subq $56, %rsp
you must undo it before ret:

asm
Copy code
addq $56, %rsp
ret
```
Because `ret` expects the **return address** to be at the top of the stack. If `%rsp` is off, `ret` pops garbage and jumps to garbage → segfault (exactly like the scary transcript in QUESTIONS.txt).
- That transcript is there to hammer home: **incorrect stack size = corrupted return address**.
---

# #Homework Homework - 7
## Problem 1
### A
From the homework: use `nm` / `objdump` to print symbols.
```bash
nm quote_data.o
objdump -t quote_data.o
objdump -d quote_data.o | less
objdump -s -j .rodata quote_data.o | less
```
1. What `objdump -d quote_data.o` is (disassembly): `-d` means:
	- “disassemble the machine code in `.text` into assembly”. This is how you see _what the functions actually do_, even without source code.
	Typical things you learn from `objdump -d`:
		- Does `get_it` call `list_get`?
		- Does it do bounds checking?
		- Does it index an array (`i*8` patterns)?
		- Does it use RIP-relative addressing to load a table of strings?
	When you open it in `less`, use:
	- `/get_it` then Enter (search for the function label)
	- `n` to jump to next search match
	- `q` to quit
2. What `objdump -s -j .rodata quote_data.o` is (raw bytes of read-only data)
	- `-s` means “dump full contents of sections (hex + ASCII)”
	- `-j .rodata` means “only show the `.rodata` section” (read-only data)
	This is where **string literals** live, like:
		- `"C makes it easy to shoot yourself in the foot; ..."`
		- `"This is why most programmers are such poor dancers."`
	So in that output, you’ll see
	- left column: addresses
	- middle: hex bytes
	- right: ASCII interpretation (readable strings)
	This is exactly how you confirm “the choices are stored as strings in rodata”, and sometimes you can even see them all and count how many.
	(Also, some compilers store strings in `.rodata.str1.1` which your symbol table shows exists: `.rodata.str1.1` with `.LC0`.)
3. How your `nm` output connects to the big picture
	Your `nm quote_data.o` output:`D choices D choices_actual T get_it T list_get T max_size D nodes`
	Interpretation:
	- `T` = code (Text section): functions
	- `D` = data (global initialized data): variables
	- `r .LC0` = read-only local constant (often a string label)
	So the “quote database” is not a simple array — it’s likely:
	- a list stored in `nodes`, and
	- `list_get(i)` returns the ith element from that list,
	- `get_it(i)` is a wrapper that calls `list_get`.
	That would perfectly match the symbol names.
4. Quick cheat sheet: which tool for which question
	1. “What symbols exist? What functions/data are in this file?" 
		- `nm quote_data.o`
		- `objdump -t quote_data.o` (more detailed)
	2. “What does the function actually do?”
		- `objdump -d quote_data.o | less`
	    - search `/get_it`, `/list_get`
	3. “Where are the strings? What text is embedded?"
		- `objdump -s -j .rodata quote_data.o | less`
	    - search `/C makes` or `/dance` etc.
	 4. “How do I find where a symbol is stored in memory at runtime?”
		- use `gdb` (`break get_it`, `x/s $rax`, etc.
## Problem 2
1. What error is it?
	**Out-of-bounds write / buffer overflow on a stack-allocated array**.
	1. Why “stack smashing”?
		Because `arr` lives on the **stack frame** of `demo()`. Writing beyond `arr[3]` overwrites whatever memory comes next in the stack frame:
		- saved registers
		- saved frame pointer
		- return address
		- stack canary (if enabled)
		Modern GCC often inserts a **stack canary**; when it detects it was overwritten, it aborts with: `*** stack smashing detected ***`
	2. Which code causes it?
		The bug is the mismatch:
		- allocated size: 4 ints (`arr[4]`)
		- written size: 8 ints (`END 8`)
		The specific offending line is `a[i] = ...` when `i=4..7` inside `fill_seq`.
2. `smash2.c`: what errors do you see, and are they similar?
	In `smash2.c`, the only change is:
```c
int *arr = malloc(sizeof(int) * 4);
...
free(arr);
```
But `fill_seq` is unchanged and still writes 8 ints.
- What changes about the failure?
	- Now the out-of-bounds write is on the **heap**, not the stack.
	So:
	- You probably **won’t** get “stack smashing detected”
	- Instead you may see:
	  - no immediate crash (silent heap corruption)
	  - or later crash like `malloc(): corrupted top size`
	  - or crash during `free(arr)` because allocator metadata was smashed
- Are they similar?
	Yes: both are **buffer overflows**, but:
	- smash1: stack overflow → stack canary catches it quickly
	- smash2: heap overflow → may corrupt allocator metadata and fail later (or not deterministically)
3. Run both under Valgrind and compare what it reports. Which memory area is monitored better?
	Homework asks you to compile with `-g` and run valgrind.
	1. Commands
```bash
gcc -g smash1.c -o smash1
valgrind ./smash1
gcc -g smash2.c -o smash2
valgrind ./smash2
```
---
