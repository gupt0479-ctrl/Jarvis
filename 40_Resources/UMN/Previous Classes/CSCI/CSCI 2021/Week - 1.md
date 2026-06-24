---
type: class
status: archived
created: 2025-09-17
updated: 2025-09-25
area:
  - "[[C Language]]"
  - "[[50_Archive/Previous Classes/CSCI/CSCI 2021/Midterm - 1]]"
  - "[[Compilation system]]"
  - "[[Hardware Organization]]"
tags:
  - "#CSAPP"
  - "#DIS"
  - "#Lecture"
  - "#class"
next: "[[50_Archive/Previous Classes/CSCI/CSCI 2021/Week - 2]]"
---
# Textbook (CSAPP 1.1-1.6, DIS 1.1-1.4)
## CSAPP #CSAPP 
The programs that perform the four phases (preprocessor, compiler, assembler, and linker)are known collectively as the [[Compilation system]]. Once your `hello.c` program is compiled into an executable file `hello`, you can run it from a command-line interpreter called a **shell**. 

[[Hardware Organization]]: To understand what's happening under the hood, we need a basic model of the hardware.

**Running the** **hello** **program involves these steps:**
1. You type `./hello` on the keyboard, and the shell program reads it into memory.
2. The shell loads the code and data from the executable `hello` file on the disk into main memory. This data transfer often uses **direct memory access (DMA)**, which allows data to travel from disk to memory without passing through the CPU.
3. The CPU starts executing the machine-language instructions in `hello`'s `main` routine. It copies the bytes for the "hello, world\n" string from memory into registers, and then to the display device, where it appears on your screen.

**Caches Matter**: A key lesson is that systems spend a lot of time moving information around. A major goal for system designers is to make these copy operations as fast as possible.
	**The Processor-Memory Gap:** There's a significant speed difference between the processor and main memory. Processors have become much faster over the years, but main memory speed has not kept up. This is known as the **processor-memory gap**. 
		**Cache Memories as a Solution:** To bridge this gap, systems use smaller, faster storage devices called **cache memories** (or simply caches). These act as temporary staging areas for information the processor is likely to need soon. Caches, such as the L1 and L2 caches, are built with faster **SRAM** technology and are physically closer to the CPU.
		The main idea is based on the principle of **locality**: programs tend to access data and code in localized regions. By storing frequently accessed data in the fast caches, the system can get the performance of a very fast memory that has the capacity of a large, slow memory.

**Storage Devices Form a Hierarchy**: The idea of using a smaller, faster storage device to cache a larger, slower one is a universal concept that is organized into a **memory hierarchy**.
	**Hierarchy Levels:** As you move up the hierarchy (from bottom to top), devices become faster, smaller, and more expensive per byte.
	    ◦ **L0:** CPU Registers
	    ◦ **L1-L3:** Cache Memories (SRAM)
	    ◦ **L4:** Main Memory (DRAM)
	    ◦ **L5:** Local Secondary Storage (e.g., local disks)
	    ◦ **L6:** Remote Secondary Storage (e.g., Web servers)
	    • **The Main Idea:** Storage at one level acts as a cache for storage at the next lower level. For example, the L1 cache is a cache for the L2, which is a cache for the L3, which is a cache for main memory, and so on. As a programmer, understanding this entire hierarchy can help you write faster programs.

---
## DIS #DIS
### 1.1
```c
#include <stdio.h> // Standard i/o library
#include <math.h> // Libraries are imported using #include

int main(void) {
    printf("Hello World\n");
    printf("sqrt(4) is %f\n", sqrt(4));   // sqrt returns double
    return 0;
}
```
what is `printf`?
- `printf` is a **function** from `<stdio.h>` (standard i/o library). 
- its job: print a **formatted string** to the terminal. 
what is a **format string**?
- the first argument to `printf` (inside quotes) is a **format string**. 
- it’s just a normal c string literal, but it can also contain **special placeholders** (begin with `%`).
- `%f` means **print a floating-point number** (either `float` or `double`).
- by default, it prints 6 digits after the decimal point.
```c
printf("%f\n", 3.14);   // prints 3.140000 
printf("%.2f\n", 3.14); // prints 3.14 (precision set to 2)
```
in `printf("sqrt(4) is %f\n", sqrt(4));`:
- format string = `"sqrt(4) is %f\n"`
- literal text: `"sqrt(4) is "`
- placeholder: `%f` → expect a floating-point argument.
- `\n` → newline

In C, all variables must be declared before they can be used. To declare a variable, use the following syntax:

```c
type_name variable_name;
```

A variable can have only a single type. The basic C types include `char`, `int`, `float`, and `double`. Declare all the variables at the top after the import in {..}.

In C, a string and a `char` are two very different types, and they evaluate differently. This difference is illustrated by contrasting a C string literal that contains one character with a C `char` literal. For example:

```c
'h'  // this is a char literal value   (its value is 104, the ASCII value of h)
"h"  // this is a string literal value (its value is NOT 104, it is not a char)
```
#### C Numeric Types
- `char` : 1 byte (small integer; can hold an ASCII code) 
- `short`: 2 bytes
- `int` : 4 bytes
- `long` : 8 bytes (on linux x86-64; 4 bytes on some 32-bit systems)
- `long long`: 8 bytes
- `float`: 4 bytes (single-precision real)
- `double`: 8 bytes (double-precision real)

You can print the exact size on a given machine using C’s `sizeof` operator, which takes the name of a type as an argument and evaluates to the number of bytes used to store that type. For example:
```c
printf("number of bytes in an int: %lu\n", sizeof(int));
printf("number of bytes in a short: %lu\n", sizeof(short));
```
The `sizeof` operator evaluates to an unsigned long value, so in the call to `printf`, use the placeholder `%lu` to print its value.
The mod operator (`%`) can only take integer-type operands (`int`, `unsigned int` - non-negative (0 … max)., `short`, and so on).
#### increment & decrement (pre vs post)

- `x++;` (post) uses old value **then** adds 1.
- `++x;` (pre) adds 1 **then** uses the new value.
````c
int x=6, y;
y = ++x + 2; // x becomes 7, y = 9 
x = 6; 
y = x++ + 2; // y = 8, then x becomes 7
````
### 1.2
C’s `printf` function prints values to the terminal, and the `scanf` function reads in values entered by a user. The `printf` and `scanf` functions belong to C’s standard I/O library.

%g:  placeholder for a float (or double) value
%d:  placeholder for a decimal value (int, short, char)
%s:  placeholder for a string value
C additionally supports the `%c` placeholder for printing a character value. Used for finding the value for ASCII values.

 C uses `scanf` to read in an `int` value and to store it at the location in memory of an `int` program variable (for example, `&num1`).
### 1.3
```c
	// a multibranch (chaining if-else if-...-else)
    // (has one or more 'else if' following the first if):
    if ( <boolean expression 1> ) {
        <true body>
    }
    else if ( <boolean expression  2> ) {
        // first expression is false, second is true
        <true 2 body>
    }
    // ... more else if's ...
    else if ( <boolean expression  N> ) {
        // first N-1 expressions are false, Nth is true
        <true N body>
    }
    else { // the final else part is optional
        // if all previous expressions are false
        <false body>
    }
```
Integer values evaluate to **true** or **false** when used in conditional statements. When used in conditional expressions, any integer expression that is:
- **zero (0)** evaluates to **false**
- **nonzero (any positive or negative value)** evaluates to **true**

Logical Operators - 
- logical negation (`!`)
- logical and (`&&`): stops evaluating at the first false expression (short-circuiting)
- logical or (`||`): stops evaluating at the first true expression (short-circuiting)

#### While loop 
Syntax:
```c
while ( <boolean expression> ) { 
	<true body>
}
```
`do-while` loop executes the loop body first and then checks a condition and repeats executing the loop body for as long as the condition is true. That is, a `do`-`while` loop will always execute the loop body at least one time:

```c
do {
    <body>
} while ( <boolean expression> );
```
#### for loop
Syntax is:
```c
for ( <initialization>; <boolean expression>; <step> ) {
    <body>
}
```
The `for` loop evaluation rules are:
1. Evaluate _initialization_ one time when first entering the loop.
2. Evaluate the _boolean expression_. If it’s 0 (false), drop out of the `for` loop (that is, the program is done repeating the loop body statements).
3. Evaluate the statements inside the loop _body_.
4. Evaluate the _step_ expression.
5. Repeat from step (2).
Here’s a simple example `for` loop to print the values 0, 1, and 2:
```c
int i;

for (i = 0; i < 3; i++) {
    printf("%d\n", i);
}
```
Executing the `for` loop evaluation rules on the preceding loop yields the following sequence of actions:
(1)
eval init: i is set to 0  (i=0)
(2) eval bool expr: i < 3 is true
(3) execute loop body: print the value of i (0)
(4) eval step: i is set to 1  (i++)
(2) eval bool expr: i < 3 is true
(3) execute loop body: print the value of i (1)
(4) eval step: i is set to 2  (i++)
(2) eval bool expr: i < 3 is true
(3) execute loop body: print the value of i (2)
(4) eval step: i is set to 3  (i++)
(2) eval bool expr: i < 3 is false, drop out of the for loop
- The loop pattern in C is always:
	1. **init** - The variable used in the loop
	2. **test** - What the loop is doing
	3. **body** - Inside the loop
	4. **update** - Change variable
	5. go back to **test** …
	The **test** runs **one extra time** at the end when the loop fails

`for` loops are a more natural language construct for definite loops (like iterating over a range of values), whereas `while` loops are a more natural language construct for indefinite loops (like repeating until the user enters an even number). Both of them have equal significance and can be written in either while or for loop.
### 1.4
#### Functions
Functions break code into manageable pieces and reduce code duplication. Functions might take zero or more **parameters** as input and they **return** a single value of a specific type. A function **declaration** or **prototype** specifies the function’s name, its return type, and its parameter list (the number and types of all the parameters). A function **definition** includes the code to be executed when the function is called.
```c
// function definition format:
<return type> <function name> (<parameter list>)
{
    <function body>
}

// parameter list format:
<type> <param1 name>, <type> <param2 name>, ...,  <type> <last param name>
```

All functions in C must be declared before they’re called. Declaring a function is done through:
- Function prototype: A prototype at the top tells the compiler enough info to check your function calls. For doing vaste projects check [[C Language]].
```
return_type function_name(parameter_type1, parameter_type2, ...);

int max(int n1, int n2);   // prototype
```

**Function call** invokes a function, passing specific argument values for the particular call. 
```c
/ function call format:
function_name(<argument list>);

// argument list format:
<argument 1 expression>, <argument 2 expression>, ...,  <last argument expression>
```
#### Call Stack
The **execution stack** keeps track of the state of active functions in a program. When a function is called, a new stack frame is created for it (_pushed_ on the top of the stack), and space for its local variables and parameters is allocated in the new frame. When a function returns, its stack frame is removed from the stack (_popped_ from the top of the stack), leaving the caller’s stack frame on the top of the stack. 
# #Lecture Lecture
Model of a computer: CPU - executes instructions(Store something to an address, copy data from cell to cell, perform the action on the cell data), consumes input and sends output.
Memory - A very large array of cells. Each cell has a fixed index(address), contents may vary.
Program - A sequence of instructions.
RAM (Random Access Memory): Able to quickly store/retrieve data from any cell we want. 

Declaring and assigning to a variable: 
```c
int x = 12;
```
Reserves a cell, stores the value on the right in cell named on the left.
### [[C Language]] - 
is entirely pass-by-value because memory address is a perfectly legitimate value. you choose if your function arguments are a regular type  
f(int x, char y) or pointers ```
```c
f(int *x, char *y)
```
### Function Call Stack
1. Caller (`main`) pushes a stack frame **onto function call stack**
2. Frame has a space for all callee parameters and local variables
3. Caller records where it left off so it can resume later
4. Caller copies parameter values to callee frame
5. Callee (`swap`) begins executing at first instruction in function body 
```c
#include <stdio.h>

void swap(int a, int b);

int main() {
    int x = 16;
    int y = 23;
    printf("x: %d, y: %d\n", x, y);

    swap(x, y);
    printf("x: %d, y: %d\n", x, y);
    return 0;
}

void swap(int a, int b) {
    int tmp = a;
    a = b;
    b = tmp;
}
```
**Then when callee (`swap`) returns:**
1. Callee stack frame is popped
2. Control returns to caller, which then executes the next instruction
3. Callee may pass a return value to the caller
4. `swap()` does not alter variables in `main()`

Passing values: An address is a values. C allows you to work with memory addresses (**pointers**) directly. Pointers are variables that hold addresses. Every pointer has a type(int, char). 
Ex: ```
int *a = &x; //Declares an integer pointer a with address of x as value```

```c
#include <stdio.h>  
void swap(int *a, int *b); // Function exists, defined below  

int main() {  
	int x = 16;  
	int y = 23;  
	printf("x: %d, y: %d\n", x, y);  
	// Call swap function  
	swap(&x, &y); // Pass in addresses of x and y  
	printf("After swap -- x: %d, y: %d\n", x, y);  
	return 0;  
}
void swap(int *a, int *b) {  
	int tmp = *a; // Assign value at address in a to tmp  
	*a = *b; // Assign value at address in b to addr in a  
	*b = tmp; // Assign value of tmp to address in b  
}

OUTPUT:x = 23
		y = 16
```

