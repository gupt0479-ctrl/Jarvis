---
type: class
status: archived
created: 2025-09-27
updated: 2025-10-03
area:
  - "[[50_Archive/UMN/Classes/Previous Classes/CSCI 2021/Week - 2]]"
  - "[[C Language]]"
tags:
  - "#class"
next: "[[50_Archive/UMN/Classes/Previous Classes/CSCI 2021/Week - 2]]"
---
When you pass **any array** (static or dynamic) to a function, what actually gets passed is **just the base address** (pointer to element 0). The function gets a copy of the base address → `arr` points to the same heap block.
```
void init_array(int *arr, int size);
void init_array(int arr[], int size);
```
Are completely equivalent declarations because arrays always decay to pointers when passed to functions.