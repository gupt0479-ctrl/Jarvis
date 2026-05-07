---
type: input
input_kind: book
status: tree
created: 2025-09-18
source_url: CSAPP
related_progress:
  - "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2021/Midterm - 1]]"
  - "[[C Language]]"
tags:
  - input
next: "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2021/Week - 1]]"
---
To understand what's happening under the hood, we need a basic model of the hardware.

**Buses:** These are electrical conduits that transfer bytes of information (called **words**) between the system components. The size of a word (e.g., 32 or 64 bits) is a fundamental system parameter.
**I/O Devices:** These are connections to the outside world, like your keyboard, display, and disk drive. The executable `hello` file initially resides on the disk.
**Main Memory (DRAM):** This is a temporary storage device that holds both the program and its data while it's running. Logically, it's a linear array of bytes, each with a unique address.
**Processor (CPU):** This is the engine that executes the instructions stored in main memory. At its core, the CPU has a **program counter (PC)**, which is a register that holds the address of the next instruction to execute. The CPU repeatedly fetches the instruction pointed to by the PC, interprets it, performs a simple operation (like loading data, storing data, or arithmetic), and then updates the PC to point to the next instruction. The set of simple operations a CPU can perform is defined by its **instruction set architecture**.