---
type: class
status: archived
created: 2025-11-07
updated: 2025-11-08
area:
  - "[[C Language]]"
tags:
  - "#class"
  - "#Textbook"
  - "#CSAPP"
  - "#Lecture"
  - "#Lab"
  - "#Homework"
next: "[[50_Archive/Previous Classes/CSCI/CSCI 2021/Week - 8|Week - 8]]"
---
# #Textbook Textbook (CSAPP - 3.6 to 3.11)
## #CSAPP CSAPP
### 3.6 Control
To implement conditional behavior and looping, machine code relies on condition codes and control transfer instructions.
- **Condition Codes**: These are single-bit registers (flags) within the CPU that capture information about the result of the most recent arithmetic or logical instruction. Examples include the Zero Flag (ZF), the Sign Flag (SF), and the Carry Flag (CF). Instructions like **cmp** **(compare)** and **test** are critical here because they perform subtraction or bitwise AND, respectively, purely to set the condition codes without changing any other registers.
- **Jump Instructions**: These instructions (e.g., `jmp`, `je` (jump equal), `jl` (jump less)) perform conditional control transfer by checking various combinations of the condition codes. In assembly code, jump targets are typically represented by **symbolic labels** that the assembler and linker translate into proper encodings, often using **PC-relative addressing**.
- **Conditional Data Transfers ($cmov)$**: Modern processors use conditional move instructions to transfer data between registers conditionally. This technique avoids the performance degradation caused by **branch misprediction** that can occur when using conditional jumps.
- **Switch Statements and Jump Tables**: C `switch` statements are often implemented very efficiently using **jump tables**. A jump table is an array of code addresses, allowing the program to branch to one of many distinct code locations (cases) via a single index lookup and indirect jump instruction. Read-only data (`.rodata`) stores the jump table.
### 3.7 Procedures
Procedures (functions) are a key abstraction, requiring mechanisms for transferring control, passing data, and managing local memory.
- **The Run-Time Stack**: Procedure execution is managed using the run-time stack, which grows downward (toward lower memory addresses).
- **Stack Frames**: Each procedure call creates a dedicated region of the stack called a **stack frame**. A stack frame may contain the **return address** (pushed onto the stack by the calling procedure) along with space for saved registers and local variables.
- **Control Transfer**: The `call` instruction pushes the address of the next instruction (the return address) onto the stack and sets the Program Counter (PC) to the start of the called function. The `ret` instruction pops this return address off the stack to resume execution in the caller.
- **Data Transfer (Arguments and Results)**: Integral values (pointers and integers) are preferentially passed via registers; only if more than **six** arguments are needed are they stored on the stack. Return values are also typically passed back via a designated register.
- **Local Storage**: Local variables that cannot be held in registers, or those whose addresses are referenced using the `&` operator, must be stored in memory within the stack frame. **Variable-size stack frames** are needed for procedures where the amount of local storage (e.g., for variable-size arrays) cannot be determined at compile time.
### 3.8 Array Allocation and Access
This section details how contiguous data structures are managed in memory.
- **Allocation and Layout**: Arrays are stored as a **contiguous block of memory**. The memory address of an element is computed using the array start address, the element size, and the index.
- **Pointer Arithmetic**: The C language's pointer arithmetic is essentially machine-level arithmetic where the compiler automatically scales array indices by the size of the data type being pointed to.
- **Nested Arrays**: Multi-dimensional arrays are stored in **row-major order**, meaning the elements of the first row are contiguous, followed by the second row, and so on.
### 3.9 Heterogeneous Data Structures
Structures and unions combine different data types, and their machine representation is heavily influenced by alignment rules.
- **Structures $(struct)$**: Fields within a structure are laid out **sequentially** in memory. The compiler determines the byte **offset** of each field from the structure's starting address, and this offset is used as a displacement in memory reference instructions.
- **Unions $(union)$**: A union's fields all reference the **same starting memory location**. The size of a union is determined by the size of its largest member. Unions are a mechanism used to circumvent the standard type system of C. 
- **Data Alignment**: Systems typically impose **alignment restrictions** requiring that objects of certain types (e.g., 4-byte integers or 8-byte pointers) must begin at memory addresses that are multiples of their size to ensure efficient hardware access. The compiler enforces alignment by inserting **padding** (unused gaps) between structure fields where necessary.
### 3.10 Combining Control and Data in Machine-Level Programs
This section links data representation (especially pointers) with control flow, particularly concerning security implications.
- **Pointers at the Machine Level**: A pointer is simply a **virtual address** of the first byte of a stored object. The pointer's type guides the compiler in generating the correct scaling factor for arithmetic and the proper number of bytes to retrieve during dereferencing.
- **Buffer Overflow (Security Vulnerability)**: This occurs due to an **out-of-bounds memory reference**, where a program writes data past the end of an allocated buffer (typically an array). If the buffer is on the stack, this can corrupt the stored control information, such as the **return address**. An attacker can exploit this by injecting malicious code and overwriting the return address to point to it, thus hijacking the program's control flow.
- **Thwarting Buffer Overflow Attacks**: Understanding machine-level representation is key to combating these attacks by knowing precisely how the vulnerability arises. The chapter discusses methods used by the programmer, the compiler, and the operating system to reduce these threats.
### 3.11 Floating-Point Code
This section introduces the low-level support for non-integer arithmetic.
- This part of the chapter covers the **machine-level support for programs operating on floating-point data**.
- It details how operations involving floating-point data utilize **modern instruction sets** (like AVX2) on x86−64 processors.

---

# #Lecture Lectures
## Lecture 16
### %rip
In assembly, a CPU normally runs _line by line_: fetch an instruction, execute it, move to the next one. This happens because of one special register: 
- **`%rip`** (**Instruction Pointer**)
	- `%rip` register holds memory address of the next instruction to execute. 
	- **Default**: We start instruction at %rip, move %rip forward to point to next instruction.
	- **Labels** - are human-readable names for specific code addresses. They’re not stored at runtime; the assembler replaces them with actual addresses when compiling.
	- After each instruction, `%rip` is automatically incremented to point to the **next instruction’s memory address**. (also: if, while, return)
### Control Flow 
**FLAGS** - Tracks result of most recent operation (among other info). Can go several names: FLAGS
- 16 bits Holds most important bits  
- EFLAGS 32 bits Name shown in gdb  
- RFLAGS 64-bit Normally not used

| Flag   | Name          | Meaning                                  |
| ------ | ------------- | ---------------------------------------- |
| **ZF** | Zero Flag     | Set if the result = 0                    |
| **SF** | Sign Flag     | Set if result is negative (sign bit = 1) |
| **CF** | Carry Flag    | Set if unsigned overflow/borrow occurred |
| **OF** | Overflow Flag | Set if signed overflow occurred          |
1. **Unconditional Jump**: Instruction always sets %rip to the target location.
2. **Comparison/Test**: Sets special internal EFLAGS register to reflect relationship between specified register values.
3. **Conditional Jump**: Jumps to target location if certain bits in EFLAGS are set (equal 1), falls through to next otherwise.
### Conditional Jump Instructions
After a compare (`cmp`) or test (`test`), conditional jumps decide whether to move `%rip` elsewhere based on the flag bits. Here’s the meaning of the ones in your table:

|Instruction|Meaning|Triggered When|Typical in C|
|---|---|---|---|
|`jmp`|Unconditional jump|Always|`goto`, loop back|
|`je`, `jz`|Jump if Equal / Zero|ZF = 1|`==`|
|`jne`, `jnz`|Jump if Not Equal / Nonzero|ZF = 0|`!=`|
|`js`|Jump if Sign (negative)|SF = 1|`< 0`|
|`jns`|Jump if Non-sign (positive)|SF = 0|`>= 0`|
|`jg`|Jump if Greater (signed)|!ZF & (SF = OF)|`>`|
|`jge`|Jump if Greater or Equal (signed)|(SF = OF)|`>=`|
|`jl`|Jump if Less (signed)|SF ≠ OF|`<`|
|`jle`|Jump if Less or Equal (signed)|ZF ∨ (SF ≠ OF)|`<=`|
|`ja`|Jump if Above (unsigned)|!CF & !ZF|`>` (unsigned)|
|`jae`|Jump if Above or Equal (unsigned)|!CF|`>=` (unsigned)|
|`jb`|Jump if Below (unsigned)|CF = 1|`<` (unsigned)|
|`jbe`|Jump if Below or Equal (unsigned)|CF ∨ ZF|`<=` (unsigned)|

So `cmp` sets the flags, and these `j*` instructions check them to decide whether to jump.
1. `cmp B, A`: Does `A − B`, sets FLAGS based on the result, but doesn’t modify either operand. Example:
```bash
cmp $10, %eax   # effectively does %eax - 10 
je  equal_label # jump if %eax == 10 
jl  less_label  # jump if %eax < 10
```
2. `test B, A`: Does `A & B` (bitwise AND), sets FLAGS. Used for checking specific bits or whether something is zero/nonzero. Example: It’s often used as an optimization instead of `cmp $0, %rax`.
```bash
test %rax, %rax   # ANDs with itself
jz   zero_case    # jump if %rax == 0
js   negative_case# jump if %rax < 0
```
## Lecture 17
### Function Call

#### Stack
Stack: Automatic, push/pop frames with function calls. **Last-In, First-Out** order matches sequence of in-progress function calls.
- *On a call*: Add information to the stack  
- *On a return*: Remove information from stack
1. `%rsp` register stores the address where the stack ends in memory. Traditionally considered the “top” of the stack.
	- The stack grows **downward** (toward smaller addresses).
	- Each function call creates a _stack frame_ — its own local workspace.
	- We use push to add to the stack, Example: `pushq %rbx`  
		- Subtracts 8 from stack pointer
		- Stores value of `%rbx` at top of stack, i.e., memory address in `%rsp`
	-  This is equivalent to: `subq $8, %rsp, movq %rbx, (%rsp)`
		1. What if we want to allocate a chunk of space for later use?
			- Subtract from `%rsp` to grow stack (e.g.: `subq $24, %rsp`)
		2. What if we are done using this chunk of stack memory?
			- Add to `%rsp` to shrink stack (e.g.:`addq $24, %rsp`)
	- There are **6 Argument Registers**: Each size of **64 bits**
		- `%rdi`
		- `%rsi`
		- `%rdx`
		- `%rcx`
		- `%r8`
		- `%r9`
		- If there are **more than 6 arguments**, the extras are pushed to the stack (in reverse order).
2. **Return Values**
	- The return value is placed in `%rax` (`%eax` for 32-bit ints).
	- The caller assumes `%rax` holds the result immediately after the call.
#### `call` Instruction
1. Pushes the **return address** (the next instruction’s address in `%rip`) onto the stack.
2. Sets `%rip` to the address of `func` (the function label). So: `call g` is equivalent to:
```bash
pushq %rip        # address of next instruction 
jmp g             # jump into function g
```
#### `ret`
Does the reverse:
1. Pops an 8-byte value from the stack.
2. Stores it into `%rip` (jumping back to the return address). So `ret` is equivalent to: `popq %rip`
### x86-64 Calling Convention
To keep everything predictable, x86-64 defines strict rules on:
1. **Where arguments go**
2. **Where return values go**
3. **Which registers you can overwrite**
- *Caller*: Code invoking a new function  
- *Callee*: Function that is being invoked
- Since _all_ functions share registers, there must be an agreement about who saves what.

| Type             | Responsibility                                                    | Example Registers                                  |
| ---------------- | ----------------------------------------------------------------- | -------------------------------------------------- |
| **Caller-saved** | The _caller_ must save (push/pop) before calling another function | `%rax`, `%rcx`, `%rdx`, `%rdi`, `%rsi`, `%r8–%r11` |
| **Callee-saved** | The _callee_ must save/restore before modifying                   | `%rbx`, `%rbp`, `%r12–%r15`                        |
**Rule of thumb:**
- Caller-saved = _temporary registers_.
	- A called function is free to do whatever it wants with a caller-save register. If caller cares about register’s value, it must `push reg` to stack before call and `pop reg` once it resumes.
	- Register’s value can change between call and corresponding `ret`, but caller restores it with a pop from stack
- Callee-saved = _preserved registers_.
	- A called function f must `push` a callee-saved register to the stack before it may use this register.
	- Then `pop` that value back before executing a `ret`.
	- Register has same value before call f and after f’s ret.
1. **Stack Alignment**: x86-64 requires `%rsp` to be **16-byte aligned** when executing `call`.
	- This ensures proper performance and stack safety for SIMD operations (e.g. 128-bit registers).
	- If `%rsp` is not aligned, the return address may go to the wrong place, crashing your program.
### Step-by-Step Function Call Sequence
Let’s visualize function `P()` calling `Q()`:

|Step|Action|Description|
|---|---|---|
|1|Save caller-saved regs|Push if needed|
|2|Move args into registers|`%rdi`, `%rsi`, etc.|
|3|Align `%rsp` to 16|Optional adjustment|
|4|`call Q`|Push return address, jump to Q|
|5|`Q`’s prologue|Reserve locals with `subq $N, %rsp`|
|6|Execute body|Possibly modify caller-saved regs|
|7|Put return value in `%rax`|For caller to use|
|8|`Q`’s epilogue|Free locals, restore callee-saved regs|
|9|`ret`|Pop return address into `%rip`, go back|
|10|Caller resumes|Pops saved regs, continues|
## Lecture 18
### Arrays in Assembly 
Arrays map _naturally_ to x86-64 addressing modes because array indexing is just **base + (index × element size)**. A memory operand can look like: `disp(base, index, scale)`
Meaning: `address = base + index × scale + disp`
1. **Writing to an array element**: `int arr[10]; arr[i] = 48;`
	Assembly (assuming):
		- `%rdx` holds address of `arr`
		- `%rcx` holds `i`
	`movl $48, (%rdx, %rcx, 4)`
	Why `4`? Because each `int` = 4 bytes.  
	So effective address = `%rdx + (%rcx × 4)` = `&arr[i]`.
2. **Pointer arithmetic**: `int *b = a + i;`
	If `a` is in `%rdx` and `i` in `%rcx`:`leaq (%rdx, %rcx, 4), %rax`
	- `leaq` = “load effective address” → calculates address without touching memory.
	- `%rax` now contains pointer `a + i`.
	If the array contained `long`s (8 bytes each):`leaq (%rdx, %rcx, 8), %rax` because `scale = 8`.
3. Accessing array elements in loops:`for (int i=0; i<10; i++)      arr[i] = i*i;` Typical assembly pattern:
```bash
movl $0, %ecx         # i = 0 
loop:
     cmpl $10, %ecx
     jge done     
     movl %ecx, %eax     
     imull %ecx, %eax     
     movl %eax, (%rdx, %rcx, 4)   # arr[i] = i*i     
     addl $1, %ecx     
     jmp loop 
done:
```
That’s how array indexing translates into base + scaled index addressing.
### Structs
A **struct** is a contiguous block of memory - each field has a _fixed offset_ from the base address, sometimes with padding to align fields. Example:
```c
typedef struct {
     int   i;      // offset 0     
     short s;      // offset 4     
     char  c[8];   // offset 6 
} st;
```
If `st_ptr` is in `%rdi`:

| Field  | C access              | Assembly                  | Offset explanation                     |
| ------ | --------------------- | ------------------------- | -------------------------------------- |
| `i`    | `st_ptr->i`           | `movl 0(%rdi), %esi`      | starts at 0                            |
| `s`    | `st_ptr->s`           | `movw 4(%rdi), %si`       | +4 bytes after `i`                     |
| `c[i]` | `st_ptr->c[i] = 'X';` | `movb $88, 6(%rdi, %rcx)` | base + 6 offset to array field + index |
Padding ensures each field begins on an alignment boundary (e.g., 2 bytes for `short`, 4 for `int`).
### Butter Overflows
What happens in C:
```c
int main() {
     char name[32];     
     scanf("%s", name);   // dangerous 
}
```
If user types > 32 bytes, it keeps writing beyond the array. Memory layout in stack frame:
```c
Higher addr
----------------------
Return address
Saved registers
Local vars
char name[32]
----------------------
Lower addr (%rsp)
```
Writing too much → overwrite return address → CPU `ret` jumps to attacker-supplied code. Why it’s dangerous? 
	- If attacker inputs machine code (payload) and overwrites return address with the payload’s address, CPU will execute it on `ret`.  This is the classic **stack-smashing exploit**.
### Mitigations
1. **Safe I/O functions**  
    Use `fgets()` instead of `gets()` or `scanf("%s")`.  
    Always specify max input size.
2. **Address Space Layout Randomization (ASLR)**  
    Makes stack and heap start at random addresses → harder for attacker to guess.    
3. **Stack Canaries**  
    Compiler inserts a random value before return address; checks it before `ret`.  
    If changed → abort.
4. **Non-Executable Stack**  
    OS marks stack pages as “data-only”; even if overwritten, can’t run injected code.

---

# #Lab Lab - 6
Assembly.
[[50_Archive/Previous Classes/CSCI/CSCI 2021/Week - 6#Lab Lab - 5|Assembly Basics]]

---

# #Homework Homework - 6
## Problem 1
### A & B
You’re using: `movl %eax, (%rdx)`
The `movl` instruction is **32-bit**, which is correct for storing an `int` — **but the pointer register `%rdx` must be 64-bit valid memory address**. So the issue is not with this instruction itself — the problem is that **your `%rdx` value got clobbered** earlier.
1. Root cause, The instruction: `cqto` extends `%rax` → `%rdx`, because **`cqto` writes into `%rdx`** to prepare for signed division.
	- So before division:
		- `%rdx` contained your pointer to `quot`
		- but `cqto` **overwrote `%rdx`** with the sign-extension of `%rax` (0 or -1)!
That means when the program executes `movl %eax, (%rdx)` later, it’s trying to write to address **0x00000000** or **0xFFFFFFFFFFFFFFF**, which are **invalid memory addresses**, causing the segmentation fault
### C
1. What instruction caused the error?
	- movl %eax, (%rdx) on line 18.
2. Values of registers when it happened?
	- %rdx = 0x9 (garbage after cqto), %eax = 3.
3. Why is this a problem?
	- cqto overwrites %rdx with sign-extension of %rax, destroying the pointer to quot.
	- The program then writes to an invalid address (0x9), causing the segmentation fault.
4. Difference from the corrected version: The fixed version saves %rdx and %rcx into temporary registers (%r8, %r9) before cqto, so they remain valid pointers when writing results.
### D
**C → Assembly correspondence**

|**Location in main()**|**C Code**|**Assembly Instructions**|
|---|---|---|
|**Call to dodiv()**|`int numer = 42;`  <br>`int denom = 11;`  <br>`&quot`  <br>`&rem`|`subq $8, %rsp` → make 8 bytes for `quot` (4 bytes) and `rem` (4 bytes) on stack.  <br>`movl $42, %edi` → put `numer` (42) in first argument register.  <br>`movl $11, %esi` → put `denom` (11) in second argument register.  <br>`movq %rsp, %rdx` → store address of stack variable (bottom 4 bytes) into `%rdx` (pointer to `quot`).  <br>`leaq 4(%rsp), %rcx` → compute address 4 bytes above stack pointer for `rem`, and put it in `%rcx`.  <br>`call dodiv` → call the function.|
|**Call to printf() arguments**|`printf("%d / %d = %d rem %d\n", numer, denom, quot, rem);`|`leaq .FMT_STRING(%rip), %rdi` → load format string into first argument register.  <br>`movl $42, %esi` → second printf argument (`numer`).  <br>`movl $11, %edx` → third printf argument (`denom`).  <br>`movl (%rsp), %ecx` → load `quot` from stack into next printf argument.  <br>`movl 4(%rsp), %r8d` → load `rem` from stack into next printf argument.  <br>`movl $0, %eax` → per the x86-64 ABI, `printf` requires %eax = 0 before call.  <br>`call printf@PLT` → execute printf.|
Explanations of stack alignment instructions

| **Instruction** | **Meaning**                                                    | **Why it’s used**                                                                                                                                                                   |
| --------------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `subq $8, %rsp` | Decreases stack pointer by 8 bytes (allocates space on stack). | The stack must be **16-byte aligned** before a function call in x86-64. This reserves 8 bytes for the two local integers (`quot`, `rem`) and ensures the call alignment is correct. |
| `addq $8, %rsp` | Increases stack pointer by 8 bytes (frees space).              | After returning from `printf`, the function restores the stack pointer to its original position before returning to the OS.                                                         |
|                 |                                                                |                                                                                                                                                                                     |
## Problem 2
### A
Make use of the 'strings' program which is available on most Unix platforms. This program shows the ASCII strings present in a binary object such as verify.o. Run it by typing the following: `strings verify.o`
### B
Run the 'nm' utility which is short for "names". It produces the set of symbols present in a binary file. `nm verify.o`
### C
**GDB with assembly** - See the homework itself, it has a lot of instructions, follow the instructions. Go through the entire disassembly and get the output. 

---
