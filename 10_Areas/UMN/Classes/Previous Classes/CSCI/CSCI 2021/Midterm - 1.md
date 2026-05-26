---
type: class
status: archived
created: 2025-10-29
updated: 2025-11-06
area:
  - "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2021/Week - 1]]"
  - "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2021/Week - 2]]"
  - "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2021/Week - 3|Week - 3]]"
  - "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2021/Week - 4|Week - 4]]"
tags:
  - "#class"
  - "#evergreen"
next: "[[C Language]]"
---
### Control Flow
Data sizes, registers, instruction suffixes
- 8-bit: `byte` → reg: `%al`, `%bl`… → suffix `b` (e.g., `movb`, `addb`) 
- 16-bit: `word` → `%ax` → `w`
- 32-bit: `int` → `%eax`, `%ebx`, `%ecx`, `%edx`, `%esi`, `%edi`, `%r8d`… → `l`
    - **Zero-extend rule:** writing to a 32-bit reg clears upper 32 of the 64-bit pair.
- 64-bit: `long`, pointer → `%rax`, `%rbx`, … `%r15` → `q`
- Arrays map _naturally_ to x86-64 addressing modes because array indexing is just **base + (index × element size)**. A memory operand can look like: `disp(base, index, scale)`
	- Meaning: `address = base + index × scale + disp`
	- `long a = a + b[2];` → `addq 16(%rbx), %rax` (2×8)
- There are **6 Argument Registers**: Each size of **64 bits** and for 32 bits just replace r with e.
	- `%rdi`, `%rsi`, `%rdx`, `%rcx`, `%r8`, `%r9`. 
	- If there are **more than 6 arguments**, the extras are pushed to the stack (in reverse order).
	- Return value → `%eax/%rax`
	- 1st arg → `%edi`, 2nd → `%esi`, 3rd → `%edx`, 4th → `%ecx`, 5th → `%r8d`, 6th → `%r9d`
- `a = a + b;` (int) → `addl %ebx, %eax`
- `a = a + *p;` (int*) → `addl (%rbx), %eax`
- `a = a + b;` (long) → `addq %rbx, %rax`
- `a = a + p[2];` (long*) → `addq 16(%rbx), %rax`

| 64-bit                                             | 32-bit                          | 16-bit | 8-bit  | used for                    |
| -------------------------------------------------- | ------------------------------- | ------ | ------ | --------------------------- |
| `%rax`                                             | `%eax`                          | `%ax`  | `%al`  | return values, temp         |
| `%rbx`                                             | `%ebx`                          | `%bx`  | `%bl`  | callee-saved general        |
| `%rcx`                                             | `%ecx`                          | `%cx`  | `%cl`  | loop counters               |
| `%rdx`                                             | `%edx`                          | `%dx`  | `%dl`  | 2nd arg, division remainder |
| `%rsi`                                             | `%esi`                          | `%si`  | `%sil` | 2nd arg / string src        |
| `%rdi`                                             | `%edi`                          | `%di`  | `%dil` | 1st arg / string dest       |
| `%rbp`                                             | `%ebp`                          | `%bp`  | `%bpl` | base/frame pointer          |
| `%rsp`                                             | `%esp`                          | `%sp`  | `%spl` | stack pointer               |
| `%r8`–`%r15`                                       | `%r8d`–`%r15d`                  | …      | …      | extra args/temp             |
| **caller-saved (volatile)**                        | **callee-saved (non-volatile)** |        |        |                             |
| `%rax`, `%rcx`, `%rdx`, `%rsi`, `%rdi`, `%r8–%r11` | `%rbx`, `%rbp`, `%r12–%r15`     |        |        |                             |
 - Jump mnemonics (`j*`)

| Jump                       | Meaning (after `cmp src, dest`)                        | Condition (C)                  | Typical C syntax |
| -------------------------- | ------------------------------------------------------ | ------------------------------ | ---------------- |
| `je` / `jz`                | equal / zero                                           | ZF = 1                         | `==`             |
| `jne` / `jnz`              | not equal                                              | ZF = 0                         | `!=`             |
| `jg` / `jnle`              | greater (signed)                                       | ZF = 0 and SF = OF             | `>`              |
| `jge` / `jnl`              | greater or equal (signed)                              | SF = OF                        | `>=`             |
| `jl` / `jnge`              | less (signed)                                          | SF ≠ OF                        | `<`              |
| `jle` / `jng`              | less or equal (signed)                                 | ZF = 1 or SF ≠ OF              | `<=`             |
| `ja`                       | above (unsigned)                                       | CF = 0 and ZF = 0              | `>` (unsigned)   |
| `jae`                      | above or equal (unsigned)                              | CF = 0                         | `>=` (unsigned)  |
| `jb`                       | below (unsigned)                                       | CF = 1                         | `<` (unsigned)   |
| `jbe`                      | below or equal (unsigned)                              | CF = 1 or ZF = 1               | `<=` (unsigned)  |
| `js` / `jns`               | sign / not sign                                        | SF = 1 / 0                     | check negative   |
| `jp` / `jnp`               | parity / not parity                                    | PF = 1 / 0                     | rarely used      |
| **instruction**            | **effect**                                             | **sets flags for use by…**     |                  |
| `cmp src, dest`            | computes `dest − src` (**does not** store it)          | all `j*` conditions            |                  |
| `test src, dest`           | computes `dest & src` (**used for zero / sign tests**) | zero flag (ZF), sign flag (SF) |                  |
| `inc`, `dec`, `add`, `sub` | also set flags automatically                           | —                              |                  |
For all midterm 2 code, you’ll mostly use `je`, `jne`, `jl`, `jle`, `jg`, `jge`.
- `call foo` pushes **return address**; `ret` pops it into `%rip`.
- Every `pushq` subtracts 8 from `%rsp`, stores value at `[rsp]`.
- **After function returns**, don’t dereference pointers to its locals (dangling).
1. If/Else pattern (signed comparison)
```c
# if (a < b) T; else F; 
cmp  %ebx, %eax      # a-b 
jge  .Else           # if a >= b → skip T   
	...T...   
	jmp .End 
.Else:
   ...F...
   .End:
```
2. While loop:
```c
# while (i < n) body; 
.Loop:   
	cmp  %esi, %edi     # i ? n   
	jge  .Done   
	... body ...   
	addl $1, %edi   
	jmp  .Loop 
.Done:
```
### Bit operations
- Extract bit **k**: `((x >> k) & 1)` or `(x & (1u << k)) != 0`
- Set bit k: `x |= (1u << k)`
- Clear bit k: `x &= ~(1u << k)`
- Toggle bit k: `x ^= (1u << k)`
- **Parity (even # of 1s):**
    - brute-force count ones; bp=0 if even, 1 if odd.
    - pack `(bp << 8) | (n & 0xFF)` when n is 8-bit.
1. Mini-float (typical custom format problem)
	- Given: `sign | exp(k bits, bias B) | frac(m bits)`, normalized → significand = `1.frac`
	- Steps to decode:
	    1. `s = (-1)^{sign}`
	    2. `e = exp − B`
	    3. `M = 1 + (frac / 2^m)`
	    4. value = `s * M * 2^e`
	- Example (1|3|4, bias=4): `0111 1111` → +, `e=7−4=3`, `M=1.1111₂=1.9375` → `1.9375×8=15.5`
### Pipeline hazards
- **5-stage pipeline** Stages:
	1. **IF** – fetch instruction 
	2. **ID** – decode, read registers
	3. **EX** – ALU / address calculation / branch decision
	4. **MEM** – data memory access (for loads/stores)
	5. **WB** – write results back to register file
Key timing
	- Regfile read in **ID**, write in **WB**.
	- Load: data returns in **MEM**, written in **WB** next.
	- ALU ops: result produced in **EX**, written in **WB**.
Types of hazards: Data Hazards (most important here). All are about **RAW** (“read after write”) in this course.
1. Forwarding (bypassing)
	- Bypasses producer value from EX/MEM/WB to consumer in EX.
	- Fixes most **ALU→ALU** 1-apart deps with **no stall**: `addq %rax, %rbx addq %rbx, %rcx     # consumes %rbx`
	- **Load→use**: forwarding **cannot** fix immediate consumer; needs a gap or a stall: `movq (%rax), %rbx addq %rbx, %rcx     # immediate use`
2. Stalling (bubbles)
	- Freezes earlier stages so consumer waits until value is ready; guarantees correctness.
	- With stalls only (no forwarding): everything can be made correct but with more bubbles.
	- With both forwarding + stalling: only the minimal bubbles (usually tight load-use).
3. Multiple steps away can become safe depending on spacing. For each pair of consecutive-ish instructions.
	1. Does instr2 **read** a register that instr1 **writes**?
	    - If no → no RAW hazard.
	2.  If yes:
	    - Case ALU → ALU:
	        - With no fwd/no stall → usually incorrect if close.
	        - With forwarding → OK (no stall).
	        - With stalls → OK but slower.
	    - Case Load → Use:
	        - Tight (immediately next):
	            - Needs both: forwarding + stall.
	            - If stall forbidden → incorrect.
        - With one gap:
            - Forwarding only: OK.
            - No forwarding/no stall: incorrect.
	3. For “both fwd + stall”:
	    - Code is always **correct**.