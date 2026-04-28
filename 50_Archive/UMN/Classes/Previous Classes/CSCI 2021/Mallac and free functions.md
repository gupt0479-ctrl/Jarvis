---
type: input
input_kind: book
status: tree
created: 2025-10-04
source_url: CSAPP
related_progress:
  - "[[C Language]]"
  - "[[50_Archive/UMN/Classes/Previous Classes/CSCI 2021/Midterm - 1|Midterm - 1]]"
  - "[[50_Archive/UMN/Classes/Previous Classes/CSCI 2021/Week - 2]]"
tags:
  - input
  - "#class"
next: "[[50_Archive/UMN/Classes/Previous Classes/CSCI 2021/Week - 2|Week - 2]]"
---
`Malloc` function returns the base address of the allocated heap memory to the caller (or `NULL` if an error occurs). step by step:
1. `malloc(sizeof(int))` asks for **enough bytes to hold 1 int**.
    - on many systems, `sizeof(int)` = 4 bytes.
2. `malloc` returns a `void *` pointing to 4 newly allocated bytes.
    - type = `void *`.
3. assignment: `p = malloc(sizeof(int));`
    - since `p` is `int *`, the compiler implicitly converts the `void *` to `int *` (in C this is automatic);
    - now `p` is a pointer to int, meaning: _treat those 4 bytes as an integer slot_.
```c
// Determine the size of an integer and allocate that much heap space. malloc(sizeof(int));

#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *p;

    p = malloc(sizeof(int));  // allocate heap memory for storing an int

    if (p != NULL) {
        *p = 6;   // the heap memory p points to gets the value 6
    }
```