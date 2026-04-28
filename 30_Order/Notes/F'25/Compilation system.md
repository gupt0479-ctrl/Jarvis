---
type: input
input_kind: book
status: tree
created: 2025-10-17
source_url: CSAPP
related_progress:
  - "[[50_Archive/UMN/Classes/Previous Classes/CSCI 2021/Week - 1]]"
  - "[[50_Archive/UMN/Classes/Previous Classes/CSCI 2021/Midterm - 1]]"
  - "[[C Language]]"
tags:
  - input
---
```
gcc -o hello hello.c
```
You are telling the compiler driver (gcc) to take your source file (hello.c) and produce an executable (hello). That involves four distinct phases:
1. **Preprocessing Phase** (handled by `cpp`):
	Input: hello.c
	Output: hello.i (pure C source, with headers expanded)
	What happens here: The preprocessor looks for lines beginning with #.
	Examples: # include <stdio.h> → it literally copies the full contents of stdio.h into your code. # define PI 3.14 → replaces every occurrence of PI with 3.14.
2.  **Compilation Phase** (handled by `cc1`)
	Input: `hello.i`
	Output:`hello.s` (assembly code, human-readable but low-level)
	What happens here: The compiler translates C into assembly language.
	Assembly Language - Assembly language is a **low-level programming language** that provides a human-readable way to write instructions that directly correspond to the CPU’s machine code. Assembly language is the “middle ground” between high-level programming languages like C and the raw 0s and 1s (machine code) that the CPU actually executes.
3. **Assembly Phase** (handled by `as`)
	Input: `hello.s`
	Output: `hello.o` (object file, machine code in binary format)
	What happens here: The assembler converts the assembly instructions into **actual machine code** (the 0s and 1s your CPU understands).
	`hello.o` is a **relocatable object file**. “Relocatable” = its instructions/data aren’t tied to absolute memory addresses yet. If you open `hello.o` in a text editor, it looks like gibberish because it’s binary.
4. **Linking Phase** (handled by `ld`)
	Input: your `hello.o` + other needed object files (e.g., `printf.o`, part of libc)
	Output: `hello` (final executable program)
	What happens here: Your program isn’t self-sufficient, it calls functions like `printf`, `puts`, etc., which live in libraries. 
	The linker (`ld`): Merges your object file with the library object files. Resolves symbol references (e.g., “where is `printf`?”). Produces one unified **executable** (`hello`) that the OS loader can run.
```
hello.c
   |
   v   (cpp)
hello.i   <-- Preprocessor expands macros & headers
   |
   v   (cc1)
hello.s   <-- Compiler converts C → assembly
   |
   v   (as)
hello.o   <-- Assembler makes machine code (object file)
   |
   v   (ld)
hello     <-- Linker makes final executable
```
## The Workflow (edit → compile → run)
in c you have to **build** your program before running it. that’s why you see several commands in sequence.
### 1. editing source code
`$ vim hello.c`
- `vim` is a text editor (you could also use nano, code, emacs, etc.). 
- here you **write** your c source code (`hello.c`).
- `.c` is the standard suffix for c programs. 
🟢 **why first?** you need a source file before you can compile or run anything.
### 2. compiling with gcc
`$ gcc hello.c`
- `gcc` = gnu c compiler (the program that builds c code into machine code). 
- this command takes `hello.c` and:
    1. preprocesses it (`#include`, `#define`)
    2. compiles to assembly
    3. assembles to machine code (`hello.o`)
    4. links with libraries (like `libc`, `libm`)
- output: an **executable binary** named `a.out` (default name).
🟢 **why second?** c is not interpreted; it must be translated to machine code before execution.
### 3. running the executable
`$ ./a.out`
- `./` means: run the file named `a.out` in the current directory. 
- `a.out` is your compiled program (machine code).
- the shell runs it directly on the cpu.
🟢 **why third?** you can only run something after it’s been compiled.
### 4. naming the output file
`$ gcc -o hello hello.c`
- `-o hello` tells gcc: name the output file `hello` instead of `a.out`.
- so now you run it like:
    `$ ./hello`
🟢 **why do this?** because `a.out` is generic; naming helps you keep track of multiple programs.
### 5. linking with the math library
`$ gcc hello.c -lm`
- `-lm` means **link with the math library** (`libm`).
- required if you use functions like `sqrt`, `sin`, `cos`.
- without `-lm`, gcc will complain:  
    `undefined reference to 'sqrt'`.
🟢 **why optional?** only needed if your code calls math.h functions.
### 6. enabling warnings and debugging
`$ gcc -Wall -g -o hello hello.c`
- `-Wall` → show **all warnings** (helps you catch mistakes like unused variables, missing semicolons, bad `printf` format specifiers). 
- `-g` → include **debug info** so you can use a debugger (`gdb`) later.
- `-o hello` → name the output.
- `hello.c` → the source file.
🟢 **why helpful?** c gives very little safety by default; warnings help spot errors early, and `-g` lets you debug.