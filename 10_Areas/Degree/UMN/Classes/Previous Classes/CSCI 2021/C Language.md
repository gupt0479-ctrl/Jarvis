---
type: evergreen
status: sprout
created: 2025-09-24
tags:
  - evergreen
  - "#class"
notes:
  - "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2021/Midterm - 1|Midterm - 1]]"
  - missing midterm - 2 and final
---
# General
**C is not an object-oriented language.**
**Pass by Value**: All arguments in C are passed by value and follow pass-by-value semantics: the parameter gets a copy of its argument value, and modifying the parameter’s value does not change its argument’s value.
### Linux
[Tutorial](https://info-ee.surrey.ac.uk/Teaching/Unix/) - How to use Linux as an operating system. Commands. 
## Textbooks
![[Textbook.pdf]]: #CSAPP 

[**Dive Into Systems**(DIS)](https://diveintosystems.org/book/): #DIS
# Commands and methods

```c
scanf("%d", p); // Read an integer, store at address p
```
[[Mallac and free functions]] 
[[Placeholders]]
## Arrays 
[[Static and dynamic]]
[[Two Dimensional Arrays]]
# C use
## How to write projects?
Splitting into **multiple files** (common in bigger projects).
- **header file (.h)** → contains **function prototypes** (declarations). 
- **source file (.c)** → contains **function definitions** (bodies).
- **main file** → includes the header and calls the functions.