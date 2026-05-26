---
type: class
status: archived
created: 2025-10-29
updated: 2025-10-30
area:
  - "[[C Language]]"
tags:
  - "#class"
  - "#CSAPP"
  - "#Lecture"
  - "#Lab"
  - "#Homework"
next: "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2021/Week - 7]]"
---
# #Textbook Textbook (CSAPP - 3.1 - 3.5 )
## #CSAPP CSAPP
### 3.1
This section establishes the context and the specific assembly language you will be studying.
- **Focus on x86-64:** The instruction set architecture covered is **x86-64**, which is the machine language used by most modern laptop and desktop computers, as well as those powering large data centers and supercomputers.
- **Evolutionary Path:** This language has a long history, starting with Intel’s first 16-bit processor (the 8086 in 1978), evolving through the 32-bit IA32 processors, and most recently expanding to 64 bits with x86-64.
- **Context:** The material focuses on how **C programs are executed on Linux** using x86-64 machine code.
### 3.2
This section details the vital link between high-level C code and the low-level instructions executed by the processor.
1. Machine-Level Code:
	- A C program is transformed by the **compiler** and **assembler** into machine code. The processor executes these elementary machine instructions.
	- **Assembly Code** is the bridge: it is a human-readable, textual representation that is very close to the binary **machine code**.
	- **Value of Learning Assembly:** While compilers generate the code, being able to read and understand assembly is crucial for serious programmers. It helps:
		- **Understand Compiler Optimizations:** By examining the generated code, you can see how efficiently the program runs and analyze inefficiencies.
		- **Analyze Runtime Behavior:** High-level languages sometimes hide information critical to understanding program execution, such as how shared data is accessed in concurrent programs (Chapter 12 material). 
		- **Understand Vulnerabilities:** Many security attacks (like buffer overflows) exploit nuances in how programs store control information; understanding machine code is necessary to comprehend these vulnerabilities and guard against them.
2. Code Examples: 
	- When the compiler transforms C code into assembly code, all **information about local variable names or data types has been stripped away**.
	- Assembly code consists of sequences of very elementary operations, such as adding two numbers in registers or transferring data between memory and a register.
	- The assembly listing includes instructions (e.g., `pushq %rbx`, `movq %rdx, %rbx`). Instructions are often indented, and each indented line corresponds to a single machine instruction.
	- When compiled, `gcc` generates an object-code file (e.g., `mstore.o`) in binary format.
3. Notes on Formatting:
	- The assembly code presented in the textbook is in the **ATT format** (named after AT&T), which is the default format used by the `gcc` compiler and related tools.
	- **Key difference from Intel Format:** 
		- **Operand Order:** ATT format lists operands in **reverse order** (Source, then Destination), which can be confusing when switching formats. 
		- **Memory Addressing:** In ATT format, memory locations are enclosed in parentheses (e.g., `(%rbx)`), while Intel format uses brackets (e.g., `[rbx]`).
### 3.3
This section explains the specific sizes and nomenclature used by the x86-64 architecture, derived from its historical roots.

|             |                   |                 |                                            |
| ----------- | ----------------- | --------------- | ------------------------------------------ |
| Data Size   | Intel Terminology | Assembly Suffix | C Data Type (x86-64 Linux)                 |
| 1 byte      | Byte              | `b`             | `char`                                     |
| 2 bytes     | Word              | `w`             | `short`                                    |
| 4 bytes     | Double Word       | `l` (Long word) | `int`, `float`                             |
| **8 bytes** | **Quad Word**     | **q**           | **long**, Pointers (e.g., char* ), double* |
- The term **"word" refers to 16 bits** (2 bytes) historically. 
- Standard C `int` values are stored as **double words (32 bits)**.
- **Pointers** (`char *`) and `long` integers are stored as **quad words (8 bytes)** on a 64-bit machine.
- The suffix **‘l’** denotes both a 4-byte integer and an 8-byte double-precision floating-point number, but this causes no ambiguity because floating-point code uses a separate set of instructions and registers.
- **Register Behavior:**
	- Instructions operating on **4-byte quantities** (double words) **set the upper 4 bytes of the destination register to zero**.
	- Instructions operating on 1- or 2-byte quantities leave the remaining higher-order bytes unchanged.
	- The 16 integer registers can be accessed as byte, word, double word, and quad word quantities through their low-order portions.
### 3.4
This section describes the types of operands instructions can manipulate and how memory addresses are calculated.
1. Operand Specifiers: Instructions require operands that specify the source values and the destination location for the result. There are three main types of operands:
	1. **Immediate:** A constant numerical value. In assembly code, it is denoted by a dollar sign (`$`) preceding the value (e.g., `$0x104`).
	2. **Register:** The contents of one of the 16 available general-purpose registers (e.g., `%rax`).
	3. **Memory Reference:** Data stored in memory, accessed via its calculated address. The general form of memory addressing, used to calculate the **effective address**, is: $Imm(rb​,ri​,s)$ where the address is computed as: $$Imm+R[r_{b}​]+R[r_{i}​]⋅s$$
		- **Imm (Immediate offset):** A constant offset.
		- rb​ **(Base Register):** The value of the base register.
		- ri​ **(Index Register):** The value of the index register.
		- s **(Scale Factor):** A constant multiplier (must be 1, 2, 4, or 8).
2. Data Movement Instructions: These are among the most heavily used instructions, allowing data to be copied between registers and memory.
	- The basic move instruction is `mov` (with size suffixes: `movb`, `movw`, `movl`, `movq`).
	| **Instruction** | **Effect** | **Description** |
	|------------------|------------|-----------------|
	| `mov`            | `S, D → D ← S` | Move |
	| `movb`           | `S, D → D ← S` | Move **byte** |
	| `movw`           | `S, D → D ← S` | Move **word** (2 bytes) |
	| `movl`           | `S, D → D ← S` | Move **double word** (4 bytes) |
	| `movq`           | `S, D → D ← S` | Move **quad word** (8 bytes) |
	| `movabsq`        | `I, R → R ← I` | Move **absolute quad word** (immediate to register) |
	- **Pointers are 64-bit quad words** that hold virtual addresses. Dereferencing a pointer (e.g., `*xp`) requires a memory access based on the address stored in a register.
	- **Move instructions with conversion:** When moving a smaller value to a larger destination (e.g., moving a 4-byte value to an 8-byte register), special instructions handle the remaining bytes:
	- **movz** **(Zero extension):** Fills the high-order bytes with zeros.
		- **movs** **(Sign extension):** Fills the high-order bytes with a copy of the sign bit of the source value.
		- A special, compact instruction, `cltq`, is the equivalent of `movslq %eax, %rax`; it sign-extends the 32-bit `%eax` into the 64-bit `%rax`.
3. Data Movement Example: This section confirms that, by convention, function arguments are passed in registers (e.g., `%rdi`, `%rsi`, `%rdx`) and function return values are stored in the register `%rax`. 
	- Dereferencing a pointer involves copying that pointer into a register, and then using this register in a memory reference. 
	- Second, local variables such as x are often kept in registers rather than stored in memory locations. Register access is much faster than memory access.
4. Pushing and Popping Stack Data: We add data to a stack via a `push` operation and remove it via a pop operation, with the property that the value popped will always be the value that was most recently pushed and is still on the stack.
		- The **stack** is a memory region that operates under a **Last-In, First-Out (LIFO)** principle. It is managed by the **stack pointer register, %rsp**.
	- **pushq** **S:** Decrements `%rsp` by 8 and stores the 8-byte value S at the new stack address. The behavior of the instruction `pushq %rbp` is equivalent to that of the pair of instructions 
	```c
	subq $8,%rsp //Decrement stack pointer
	movq %rbp,(%rsp)  //Store %rbp on stack
	```
	- **popq** **D:** Reads the 8-byte value from the top of the stack, stores it in destination D (register or memory), and then increments `%rsp` by 8. The instruction `popq %rax` is equivalent to the following pair of instructions: 
	```c
	movq (%rsp),%rax //Read %rax from stack
	addq $8,%rsp  //Increment stack pointer
	```
### 3.5
This section covers the instructions used for computation, which set the stage for understanding how control flow works (Chapter 3.6).
#### Common x86-64 Instructions

| Instruction | Effect        | Description                |
| ----------- | ------------- | -------------------------- |
| `leaq S, D` | `D ← &S`      | Load effective address     |
| `inc D`     | `D ← D + 1`   | Increment                  |
| `dec D`     | `D ← D - 1`   | Decrement                  |
| `neg D`     | `D ← -D`      | Negate                     |
| `not D`     | `D ← ~D`      | Bitwise complement         |
| `add S, D`  | `D ← D + S`   | Add                        |
| `sub S, D`  | `D ← D - S`   | Subtract                   |
| `imul S, D` | `D ← D * S`   | Multiply                   |
| `xor S, D`  | `D ← D ^ S`   | Exclusive-or               |
| `or S, D`   | `D ← D ∣ S`   | Bitwise OR                 |
| `and S, D`  | `D ← D & S`   | Bitwise AND                |
| `sal k, D`  | `D ← D << k`  | Left shift                 |
| `shl k, D`  | `D ← D << k`  | Left shift (same as `sal`) |
| `sar k, D`  | `D ← D >>A k` | Arithmetic right shift     |
| `shr k, D`  | `D ← D >>L k` | Logical right shift        |
|             |               |                            |
#### Explain
1. Load Effective Address (`leaq`):
	- The **leaq** instruction computes the source memory address (the effective address) but **does not actually access memory**.
	- It places the calculated address value into the destination register.
	- **Compiler Utility:** Because `leaq` can perform additions and multiplication by constants 1, 2, 4, or 8 (via the scale factor s in the address calculation formula), it is frequently used by compilers as a highly efficient way to implement general arithmetic expressions, not just pointer calculations.
2. Unary and Binary Operations:
	- **Unary Operations:** Operate on a single operand, which serves as both the source and the destination (e.g., `incq` (increment), `decq` (decrement), `negq` (negate), `notq` (bitwise complement)).
	- **Binary Operations:** Have two operands; the first operand is the source, and the second operand is simultaneously the source and the destination (e.g., `addq` (add), `subq` (subtract), `andq` (bitwise AND), `xorq` (bitwise XOR)).
	- **Condition Codes:** Most arithmetic and logical instructions set special **Condition Code** registers which reflect properties of the result (e.g., zero result, negative result).
3. Shift Operations: Shift instructions move the bits of an operand left or right. The shift amount is specified either by an immediate constant (e.g., `$4`) or by the single-byte register **%cl**.
	- **Left Shift** $(sal/shl)$: Shifts bits to the left, filling the low-order bits with zeros.
		- An immediate constant: `salq $4, %rax   # shift left by 4 bits`
		- Register `%cl` (ONLY `%cl` allowed!):`sarq %cl, %rax`
			- Weird **rule**: Only `%cl` can store variable shift amounts.
		- When shifting a **w-bit** value: You only use the **lowest log₂(w)** bits of `%cl`.

| Data Size     | Bits | Low bits used from `%cl` | Max shift |
| ------------- | ---- | ------------------------ | --------- |
| byte          | 8    | 3 bits → `0–7`           | 7         |
| word          | 16   | 4 bits → `0–15`          | 15        |
| long (32 bit) | 32   | 5 bits → `0–31`          | 31        |
| quad (64 bit) | 64   | 6 bits → `0–63`          | 63        |

- **Logical Right Shift $(shr)$:** Shifts bits to the right, filling the high-order bits with zeros. This is used for **unsigned** arithmetic division by powers of 2.
- **Arithmetic Right Shift $(sar)$:** Shifts bits to the right, filling the high-order bits with copies of the sign bit (sign extension). This is used for **signed** arithmetic division by powers of 2, ensuring correct rounding toward zero.
- Why SAR vs SHR matters

| Value            | Operation                  | Result                            |
| ---------------- | -------------------------- | --------------------------------- |
| -8 → `11111000b` | `sar 1`                    | `11111100b` = -4 ✅ keeps negative |
| -8 → `shr 1`     | `01111100b` = +124 ❌ wrong |                                   |
So:
- Signed numbers use **sar** 
- Unsigned numbers use **shr**
This is why two’s complement is preferred → uniform left shift [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2021/Week - 3#** Two's-Complement Encodings **| Two's Complement]]
4. Discussion: A key advantage of **two's-complement arithmetic** is that most arithmetic and logical operations (`add`, `sub`, `mul`, `and`, `or`, etc.) are identical for both signed and unsigned data representations. The only common operation that requires distinct instructions based on whether the data is signed or unsigned is the **right shift**.
5. Special Arithmetic Operations: Complex operations like multiplication and division have dedicated instructions that require specific register usage:
	- **Multiplication $(imulq)$:** A special one-operand `imulq S` instruction performs a signed multiplication where the source S is multiplied by the 64-bit value in `%rax`. The 128-bit result is stored across two registers: the high-order 64 bits in **%rdx** and the low-order 64 bits in **%rax**.
	- **Division $(idivq)$[[#Division]]:** Signed division uses the `idivq S` instruction, where the dividend is the 128-bit quantity stored across `%rdx` (high-order) and `%rax` (low-order). The instruction stores the quotient in **%rax** and the remainder in **%rdx**.
	- **Unsigned Division $(divq)$:** Similar instruction for unsigned operands

---

# #Lecture Lectures
## Lecture 13
We study machine code and assembly not to write it but to understand what our C programs truly do, how compilers translate them, how processors execute them, and how to reason about performance, correctness, and security at the hardware level.
[[#3.1]] - History
[[#3.2]] - Basics
[[#3.3]] - **Assembly Suffix**
![[Pasted image 20251102175737.png]]
Note the **overlap**: 
	- `%eax` is bottom 32 bits of `%rax`.  
	- `%ax` is bottom 16 bits of `%eax`, and therefore of `%rax`.
	- **RULES**:

| Register written        | What happens to %rax?                                       |
| ----------------------- | ----------------------------------------------------------- |
| Write to `%rax`         | All 64 bits updated ✅                                       |
| Write to `%eax`         | ✅ Lower 32 bits updated  <br>❌ Upper 32 bits are **zeroed** |
| Write to `%ax` or `%al` | ✅ Lower bits updated  <br>✅ Upper bits **not touched**      |

- Generating Assembly with `gcc`: gcc generates and works with x86-64 assembly code.
	- To compile C code to executable file: gcc –Og –S. 
	- To run the executable: `./a.out`
```c
gcc –Og –S
gcc –Og –S mstore.c    //Example
```
1. **NOTE:** **Scaled Indexed Addressing Mode**, Format: 
	`(base, index, scale) → base + index * scale`

| Register       | Meaning                            |
| -------------- | ---------------------------------- |
| base (`%rax`)  | address of start of an array       |
| index (`%rbx`) | which element we want              |
| scale          | how large each element is in bytes |
	- `(%rax, %rbx, 4)` Scaled Index `rax[rbx]` - Array access with element size 4
	- `(%rax, %rbx, 8)` Scaled Index `rax[rbx]` - Array access with element size 8
## Lecture 14
### Instruction types
1. Fundamentals: [[#Common x86-64 Instructions]]
	1. Memory Management: `mov`
	2. Stack Manipulation: `push`, `pop`
	3. Addressing Modes: `(%eax), 12(%eax, %ebx)`
2. Arithmetic/Logic: 
	1. Arithmetic: `add, sub, mul, div, lea`
	2. Bitwise Logical: `and, or, xor, not`
	3. Bitwise Shifts: `sal, sar, shr, shl`
3. Control Flow: 
	1. Compare / Test:`cmp, test`
	2. Set on Result: `set`
	3. Jumps (Un)Conditional: `jmp, je, jne, jl, jg, …`
4. Procedure Calls:
	1. Stack Manipulation: `push, pop`
	2. Call/Return: `call, ret`
	3. System Calls: `syscall`

- **Addition** - $$add<size> <operand_A>, <operand_B>: B = B + A$$
	- Size is w, l, or q for 16, 32, or 64 bits
	- Like a move, different kinds of operands supported:
		- Register and Register  
		- Register and Memory Location
		- Memory Location and Register  
		- Immediate Value and Register  
		- Immediate Value and Mem Address  
	- No memory/memory or immediate/immediate addition
- **System Call**: A **system call** is how a user program **asks the operating system** to do something it is not allowed to do directly. Why?
	- User programs **do not** have direct access to hardware (keyboard, file system, screen, network).
	- The OS controls everything for safety and security.
```c
movq $1, %rax     # system call: write
movq $1, %rdi     # file descriptor: stdout
movq $message, %rsi  # pointer to message
movq $13, %rdx       # length 13
syscall
```
In C, when you call `printf`, the **C library** ends up making these system calls for you.
### movq Operand Combinations
[[#3.4]] - Operands, `mov` and Stack.

| Source    | Dest     | Assembly (Src, Dest) | C Analog         |
| --------- | -------- | -------------------- | ---------------- |
| Immediate | Register | `movq $0x4, %rax`    | `temp = 0x4;`    |
| Imm       | Memory   | `movq $-147, (%rax)` | `*p = -147;`     |
| Reg       | Reg      | `movq %rax, %rdx`    | `temp2 = temp1;` |
| Reg       | Mem      | `movq %rax, (%rdx)`  | `*p = temp;`     |
| Mem       | Reg      | `movq (%rax), %rdx`  | `temp = *p;`     |
Cannot do memory-memory transfers with a single `movq` instruction. 
`movX SRC, DST`: Move from source to destination
	- From register to register  
	- From memory to register  
	- From register to memory  
	- From immediate to mem/reg
- `movzXY`: Move quantity of size X to register of size Y, fill top bits with zero bits (“zero extend”).
- `movsXY`: Move quantity of size X to register of size Y, sign extend to fill top bits (“sign extend”). 
- Examples:
```c
movabsq $0x112233445566AABB, %rdx 
movzwq %dx, %rax //%rax = 0x00 00 00 00 00 00 AA BB  
movswq %dx, %rax //%rax = 0xFF FF FF FF FF FF AA BB  
```
## Lecture 15
### `leaX`: Load Effective Address
`lea` **does NOT load a value from memory**. It **computes an address (or arithmetic result)** and stores that number into a register. Think:
- `mov`: take the value **at** memory  
- `lea`: take the **address** (or offset math result)
- CPU performs `base + index * scale` efficiently
- To compute array element addresses  
- To compute pointer + offset  
- To optimize arithmetic
- Example (Collatz update):
```c
# n = 3*n + 1 
leal 1(%eax, %eax, 2), %eax   # 1 + eax + 2*eax = 3*eax + 1`
```
This is **faster** than:
```c
imull $3, %eax 
addl $1, %eax`
```
### Division
| Purpose   | Used Register                  |
| --------- | ------------------------------ |
| Dividend  | `%rax:%rdx` together           |
| Divisor   | The operand you pass to `idiv` |
| Quotient  | Stored in `%rax`               |
| Remainder | Stored in `%rdx`               |
Before calling `idiv`, You **must**:
	- Move the dividend into `%rax`  
	- **Sign extend** into `%rdx` (using `cltq`, `cqto`, or related)
Then:
	- Put divisor in any register  
	- Call `idivX`
Example from lecture:
```c
movl $15, %eax 
cltq        # sign-extend eax → rax 
cqto        # sign-extend rax → rdx 
movl $2, %esi 
idivl %esi

/*Dividend = RDX:RAX   ← 128-bit combined register
Divisor = operand you pass to idiv
Result:
    RAX = quotient
    RDX = remainder
*\
```
Result:
```c
rax = 7   (15 / 2) 
rdx = 1   (15 % 2)
```
Why all these steps?
- `idiv` divides a **128-bit** number (`rdx:rax`) by a value → high precision  
- So CPU demands registers be set **perfectly** beforehand.
They **sign extend** so that the dividend is correctly represented across `%rax` + `%rdx`.

|Instruction|When Used|What It Does|
|---|---|---|
|`cwtl`|8→16 bits|Sign extend `%al` → `%ax`|
|`cltq`|32→64 bits|Sign extend `%eax` → `%rax`|
|`cqto`|64→128 bits|Sign extend `%rax` → `%rdx:%rax`|

Why sign extension? Because division must work with **negative numbers** too.
### “Undefined Behavior” Example
```c
if (i > 0 && (i+1) < 0) {
     printf("Sign Change\n");
     printf("i: %d\n", i);     
     printf("i + 1: %d\n", i + 1); 
}
```
Goal: detect when `i` overflows from positive → negative
Overflow is **undefined behavior in C**. Meaning: the compiler is **allowed** to assume signed overflow **never happens**. So **different compilers** generate different behavior.
1. GCC’s Assembly:
```c
cmpl $0, -4(%rbp) 
jle  .L4        # if i <= 0, skip (so i > 0) 
cmpl $-1, -4(%rbp) 
jge .L4        # if i >= -1, skip (so i < -1)
```
This means GCC rewrites: `if (i > 0 && i < -1)`
But **no integer can be > 0 and < -1**, so GCC assumes:
	- The condition is impossible  
	- Removes behavior
Because **overflow is undefined**, compiler assumes `(i+1) < 0` never becomes true.
**Moral**: Undefined behavior = unpredictable compiler behavior → rely on defined logic only.
2. Version 1
```c
cmpl $0, %eax     # Compare x with 0 
jle  .L4          # If x <= 0, jump (done) 
cmpl $-1, %eax    # Compare x with -1 
jge  .L4          # If x >= -1, jump (done)
```
Let’s translate conditions:

| Instruction | Means           |
| ----------- | --------------- |
| `jle`       | jump if x <= 0  |
| `jge`       | jump if x >= -1 |
Combined logic:
```c
if (x <= 0) goto L4;
if (x >= -1) goto L4;
```
This simplifies to: `if (x <= 0 OR x >= -1) → jump`
Which covers **all integers**:
- True for x = 100  
- True for x = -50  
- True for x = -1, -2, 8, 123…
Version 1 ALWAYS jumps → Execution at `.L4` ALWAYS happens. Condition never triggers fall through.

---

# #Lab Lab - 5
## GDB Guide
Debuggers are an essential tool for any serious coder. They provide the ability to stop a program at any point and inspect its state by examining variables, traversing memory, and showing stack traces. 
```bash
> make puzzlebox
gcc -Wall -Werror -g -o puzzlebox puzzlebox.c

# Note the -g option while compiling which adds debugging symbols for
# the debugger: very useful

# Start gdb with the text user interface on program puzzlebox
> gdb -tui ./puzzlebox
```
1. TUI Mode (Recommended): The _Text User Interface_ (TUI) is enabled by running `gdb` with the `-tui` option. It shows
	- Commands and history towards the bottom
	- Source code position towards the top
	The screen will occasionally get “messed up” which can be corrected by pressing `Control-l` to force a redraw of the terminal screen. 
	- When in normal mode, one can enter TUI mode with the command
```bash
tui enable
```
	- Switching to normal mode is done via
```bash
tui disable
```
2. **Running Programs**: Either: `(gdb) run input.txt` or: 
```bash
(gdb) set args input.txt 
(gdb) run
```
	You _must_ do this when the program expects an input file
3. **Essential commands**:
	1. *Setting Breakpoints*: You can stop execution anywhere:
		- `break main`
		- `break file.c:42`
		- `break function_name`
		- `info breakpoints` lists all
		- `disable N` / `enable N` turns them off/on
		- `clear` removes them, `delete` deletes them permanently
	2. *Running and Arguments*: You can supply command-line args inside GDB:
		- `set args input.txt`
		- `show args`
		- `run` starts the program
		- `kill` stops it
		- `file program` reloads after recompiling
		- `quit` exits GDB
	3. *Stepping through Code*: After hitting a breakpoint:
		- `step` → go into functions
		- `next` → skip over them
		- `stepi` / `nexti` → step by individual assembly instructions
		- `finish` → run until current function returns
		- `continue` → resume normal execution
	4. *Printing and Examining Values*:
		- `print var` → show variable value
		- `print/x var` → show as hex
		- `print/t var` → binary
		- `print/s var` → string
		- `x addr` → examine memory pointed to by addr
			- `x/d` → show as decimal
			- `x/s` → show as string
			- `x $rax` → show memory at a register
	5. *Debugging Assembly*:
		- `layout asm` → show assembly listing.
		- `layout regs` → show register window.
		- `info reg` → dump register values.
		- `disas` → print assembly of current function.
		- `stepi` → execute one instruction.
		- `winheight regs +2` → resize register window.
	6. *Debugging Without Source*: If no source code is available:
		- `layout asm` shows assembly instead of C code.
		- You’ll need to step with `stepi` instead of `step`.
	7. *ARM-Specific Section*: On Apple M-series or ARM systems, use `make gdb` instead of `gdb` manually. No need to `run`; the Makefile handles that.

| Command           | What it does                             | Use it when                                           |
| ----------------- | ---------------------------------------- | ----------------------------------------------------- |
| `break main`      | Stops execution at start of main()       | To debug from the very beginning                      |
| `break phase03`   | Stop when entering a function            | In puzzlebox phases                                   |
| `break file.c:42` | Stop at a specific line                  | When chasing a bug                                    |
| `run` / `r`       | Run the program                          | After setting breakpoints                             |
| `next` / `n`      | Step _over_ a line (skip into functions) | To trace logic line by line                           |
| `step` / `s`      | Step _into_ function calls               | To go deeper                                          |
| `continue` / `c`  | Resume until next breakpoint             | After inspecting                                      |
| `finish`          | Run until current function returns       | Check return values                                   |
| `print var`       | Print a variable                         | To see C values                                       |
| `print/x var`     | Print in hex                             | Useful for bit problems                               |
| `x/s ptr`         | Examine memory at a pointer as string    | When debugging char*                                  |
| `x/d ptr`         | Examine memory as ints                   | When debugging heap data                              |
| `info locals`     | Show all local vars                      | Quick summary in current frame                        |
| `quit`            | Exit GDB                                 | —                                                     |
| `file program`    | Load `program` and start debugging       | Convenient way to reload executable after a recompile |
| `quit`            | Exit the debugger                        |                                                       |
4. Use these when dealing with `.s` or binary-only phases:
```bash
layout asm        # show assembly instructions 
layout regs       # show CPU registers 
disas             # disassemble current function 
info reg          # show all register values 
stepi / nexti     # step one assembly instruction at a time
```
	In puzzlebox, these commands let you trace the binary’s logic when you don’t have source code.
5. **Breakpoints without source**: When you only have a **binary**, break by **function name (symbol)**:
```bash
nm puzzlebox     # shows all symbols
gdb ./puzzlebox
(gdb) break main
(gdb) break phase01
(gdb) run
```
or by **instruction address**:
```bash
(gdb) disas
(gdb) break *0x5555555559e7
(gdb) continue
```
The `*` means “break at instruction address” - used when there are no source line numbers.
## Implementing GDB in Lab
1. Understanding the key variables: `int hash = 8765309;`
```c
int targ = 1 << ((hash % 7) + 24) | 1 << (hash % 17) | 1 << (hash % 19);
```
That means:
	- Compute **three positions** in the 32-bit number based on `hash`:
	    - `(hash % 7) + 24`    
	    - `(hash % 17)`
	    - `(hash % 19)`
	- Then turn those bit positions **on** (set to 1) using `1 << n`.
	- Example: `1 << 5  = 0b100000  = decimal 32`
2. The “success” check: You pass if every bit in `shot` equals the bits in `targ`.
```c
int hit = shot ^ targ;   // XOR compares bit-by-bit 
hit = !hit;              // True (1) if XOR result is 0 → i.e., all bits matched
```
3. General rule (for any hash):
```c
(hash % 7) + 24 //24
(hash % 17) //7
(hash % 19) //1
and repeat any one of them for the 4th input //1
```
4. **Summary of how to use GDB for Lab 5**: 
	1. Step 0: Compile with debug symbols: 
```bash
make clean 
gcc -Wall -Werror -g -o phase03 phase03.c
```

| Step | Command                                      | Purpose                       |
| ---- | -------------------------------------------- | ----------------------------- |
| 1    | `gdb -tui ./phase03`                         | start debugger                |
| 2    | `break phase03`                              | stop at start of the function |
| 3    | `run input.txt`                              | run with input file           |
| 4    | `print hash`, `print/x targ`, `print/x shot` | see values                    |
| 5    | `next` / `step`                              | move line by line             |
| 6    | `continue`                                   | resume execution              |
| 7    | `quit`                                       | exit GDB                      |
| 8    | `print shot == targ`                         | checks equality               |

---

# #Homework Homework - 5
## Problem 1
### A
Compile and run these as programs using either of the below:
```bash
gcc ipow_main.c ipow_for.c 
./a.out 3 5
3^5 = 243
```
Compile `ipow_for.c` to assembly code: 
- `-S` = stop at assembly.  
- `-Og` = disable optimizations so loops stay readable.
```bash
gcc -Og -S ipow_for.c
gcc -Og -S ipow_while.c
```
### B & C
Compile both the files for A and compare them: Both of them are the same. [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2021/Week - 7#Conditional Jump Instructions| Jump Instructions]]
1. `ipow_for.c`
```bash
ipow:
    movl    $0, %eax      # initialize i = 0
    movl    $1, %edx      # pow = 1
    jmp     .L2           # jump to the loop condition check
    
.L3:
    imull   %edi, %edx    # pow *= base
    addl    $1, %eax      # i++
    
.L2:
    cmpl    %esi, %eax    # compare i and exp
    jl      .L3           # if (i < exp) jump to body
    movl    %edx, %eax    # move pow into return register
    ret
```
Here’s what’s going on:
	- `%edi` = base
	- `%esi` = exp
	- `%eax` = loop variable `i`
	- `%edx` = running power `pow`
	- `imul` multiplies `%edx` (pow) by `%edi` (base).  
	- `addl $1, %eax` increments `i`.
	- `cmp` sets flags as if it computed `i - exp`.  
	- `jl` = “jump if less” (signed comparison). If not less, execution falls through to `movl %edx,%eax` → return.
GCC translates both loops into the same sequence of `cmp`, `jl`, and `jmp` instructions because, at the machine level, “for” and “while” loops share the same structure: initialization, test, body, and increment implemented with jumps and comparisons.
## Problem 2
### A
```bash
    cmpl $99, %edi        # Describe this block
    jg .OOB
    cmpl $0, %edi
    jl .OOB
```
- `%edi` = 32-bit register holding `cents` (first argument).
- `cmpl $99,%edi; jg .OOB` → if `cents > 99`, jump to `.OOB`
- `cmpl $0,%edi; jl .OOB` → if `cents < 0`, jump to `.OOB`
### B
```bash
    movl %edi, %eax      # eax now has cents
    cltq
    cqto                 # prep for division
    movl $25, %r8d
    idivl %r8d
    movb %al, 0(%rsi)    # coins->quarters = cents / 25
    movl %edx, %eax      # cents = cents % 25
  
    cltq
    cqto                 # prep for division
    movl $10, %r8d
    idivl %r8d
    movb %al, 1(%rsi)    # coins->dimes = cents / 10
    movl %edx, %eax      # cents = cents % 10
    cltq
    cqto                 # prep for division
```
[[#Division]] 
1. Copy `cents` from %edi → %eax because `idivl` always divides the 64-bit pair **EDX:EAX / operand**. 
2. `cltq`/`cqto` (sign-extend) prepare the high half of the dividend.
3. Divide by 25:
    - quotient (EAX) → `coins->quarters`
    - remainder (EDX) → `cents % 25`
4. Divide that remainder by 10 for dimes in exactly the same way.
    - quotient (AL) → `coins->dimes`
    - remainder → new `cents`.
- Why use `%eax` + `movb`: 
	- `idivl` works only on **EDX:EAX**
	- The smallest field in the struct is a single byte → `movb` stores only the low 8 bits of the quotient into memory.
### C
We left off with `%eax = remainder` (cents % 10) → need nickels (÷ 5) and pennies (remainder). Add this code: 
```bash
## BLOCK C: nickels and pennies 
movl $5, %r8d 
idivl %r8d                 # divide remainder by 5 
movb %al, 2(%rsi)          # coins->nickels = quotient 
movl %edx, %eax            # cents = remainder (0–4) 
movb %al, 3(%rsi)          # coins->pennies = remainder
```
Explanation:
1. Reuse the remainder from dimes (already in %eax).
2. Divide by 5 → quotient = nickels, remainder = pennies.
3. Store both as bytes in the struct (`coins_t*` pointed to by %rsi).
4. No extra divisions needed—one `idiv` gives both values.
### D
Pennies are worth 1 ¢, so we don’t multiply at all — just add their raw count to `%eax`. That’s why in the penny block I **removed** the `imull` entirely.
```bash
## Nickels
movq %rdi, %rdx
sarq $16, %rdx
andq $0xFF, %rdx
imull $5, %edx        # 5 ¢ each
addl %edx, %eax       # tot += nickels*5

## Pennies
movq %rdi, %rdx
sarq $24, %rdx
andq $0xFF, %rdx
addl %edx, %eax       # tot += pennies (1 ¢ each)
```

---
