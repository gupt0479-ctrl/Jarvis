---
type: class
status: archived
created: 2025-10-03
updated: 2025-10-06
area:
  - "[[C Language]]"
  - "[[50_Archive/UMN/Classes/Previous Classes/CSCI 2021/Midterm - 1]]"
  - "[[Mallac and free functions]]"
  - "[[Static and dynamic]]"
  - "[[Two Dimensional Arrays]]"
tags:
  - "#class"
  - "#DIS"
  - "#Lecture"
  - "#Lab"
  - "#Homework"
next: "[[50_Archive/UMN/Classes/Previous Classes/CSCI 2021/Week - 3|Week - 3]]"
---
# #Textbook Textbook (DIS - 1.5, 2.1 - 2.5)
## #DIS DIS
### 1.5
#### Arrays
**Statically declared** arrays, meaning that the total capacity (the maximum number of elements that can be stored in an array) is fixed and is defined when the array variable is declared.
An **array** is a C construct that creates an ordered collection of data elements of the same type and associates this collection with a single program variable. **Ordered** means that each element is in a specific position in the collection of values (that is, there is an element in position 0, position 1, and so on), not that the values are necessarily sorted. Specify its type (the type of each value stored in the array) and its total capacity (the maximum number of storage locations). For example:
```c
int  arr[10];  // declare an array of 10 ints

char str[20];  // declare an array of 20 chars
```
Valid index values range from 0 to the capacity of the array minus 1. Here are some examples:
```c
int i, num;
int arr[10];  // declare an array of ints, with a capacity of 10

num = 6;      // keep track of how many elements of arr are used

// initialize first 5 elements of arr (at indices 0-4)
for (i=0; i < 5; i++) {
    arr[i] = i * 2;
}

arr[5] = 100; // assign the element at index 5 the value 100

// Arrays can also be passed in a function
void print_array(int arr[], int size) {
    int i;
    for (i = 0; i < size; i++) {
        printf("%d\n", arr[i]);
    }
}
```
To call a function that has an array parameter, pass **the name of the array** as the argument.
```c
print_array(some, 5);
```
**All arguments in c are passed by value.** but for arrays, the “value” being passed is just the **address of the first element**. that’s why:
    - modifying elements via the pointer → changes the original array.        
    - reassigning the local parameter (like `size = 2`) → only affects the local copy.
#### String
Programs that use these string library functions need to include the `string.h` header.
```c
#include <string.h> // include the C string library
int main(void) {
    char str1[10];
    char str2[10];
    int len;
    
    strcpy(str2, "hello");  // copy the string "hello" to str2
    len = strlen(str2); // length of the string
    printf("%s has %d chars\n", str2, len);   // prints: hello has 5 chars
}
```
When printing the value of a string with `printf`, use the `%s` placeholder in the format string. The `printf` function will print all the characters in the array argument until it encounters the `'\0'` character(every string ends with null character).
### 2.1
#### Scope
Declaring a variable outside of any function body creates a **global variable**. 
**Global variables** remain permanently in scope and can be used by any code in the program because they’re always bound to one specific memory location. Every global variable must have a unique name. 
**Local variables and parameters** are only in scope inside the function in which they are defined. The function that the local variable is in, only that function can use the variable. It is *popped off* the call stack after running through the function. 
### 2.2
#### Pointer
A **pointer variable** stores the address of a memory location in which a value of a specific type can be stored. For example, a pointer variable can store the value of an `int` address at which the integer value 12 is stored. 
A pointer provides _a level of indirection_ for accessing values stored in memory.
1. **"Pass by pointer" parameters**, for writing functions that can modify their argument’s value through a pointer parameter
2. **Dynamic memory allocation**, for writing programs that allocate (and free) space as the program runs. Dynamic memory is commonly used for dynamically allocating arrays. It is useful when a programmer doesn’t know the size of a data structure at compile time (e.g., the array size depends on user input at runtime).
While a **null pointer** (one whose value is `NULL`) should never be used to access memory, the value `NULL` is useful for testing a pointer variable to see if it points to a valid memory address.
#### Rules
1. First, **declare a pointer variable** using `type_name *var_name`:
```c
int *ptr;   // stores the memory address of an int (ptr "points to" an int)
char *cptr; // stores the memory address of a char (cptr "points to" a char)
```
2. Next, **initialize the pointer variable** (make it point to something). Pointer variables _store address values_. 
```c
int x;
char ch;

ptr = &x;    // ptr gets the address of x, pointer "points to" x
cptr = &ch;  // cptr gets the address of ch, pointer "points to" ch

cptr = &x; // ERROR: cptr can hold a char memory location 
		   // (&x is the address of an int)
```
3. Finally, **use the pointer variable**: the **dereference operator** (`*`) follows a pointer variable to the location in memory that it points to and accesses the value at that location:
```c
ptr = &x;   /* initialize ptr to the address of x (ptr points to variable x) */
*ptr = 8;   /* the memory location ptr points to is assigned 8 */
```
### 2.3
#### Pass by pointer
**Pass by pointer** pattern uses a pointer function parameter that _gets the value of the address of some storage location_ passed to it by the caller. By dereferencing a pointer parameter, the function can change the contents of memory that both the parameter and its argument refer to; through a pointer parameter, a function can modify a variable that is visible to the caller after the function returns. 
1. Declare the function parameter to be a pointer to the variable type:
```c
    /* input: an int pointer that stores the address of a memory
     *        location that can store an int value (it points to an int)
     */
    int change_value(int *input) {
```
2. When making the function call, pass in the address of a variable as the argument:
```c
    int x;
    change_value(&x);
```
In the preceding example, since the parameter’s type is `int *`, the address passed must be the address of an `int` variable.
3. In the body of the function, dereference the pointer parameter to change the argument’s value:
```c
    *input = 100;  // the location input points to (x's memory) is assigned to 100
```
### 2.4
#### Heap Memory
Dynamic memory allocation grants flexibility to programs that:
- do not know the size of arrays or other data structures until runtime (e.g. the size depends on user input) 
- need to allow for a variety of input sizes (not just up to some fixed capacity)
- want to allocate exactly the size of data structures needed for a particular execution (don’t waste capacity)
- grow or shrink the sizes of memory allocated as the program runs, reallocating more space when needed and freeing up space when it’s no longer required.
Dynamically allocated memory occupies the [**heap memory**](https://diveintosystems.org/book/C2-C_depth/scope_memory.html#_memoryparts) region of a program’s address space. When a program dynamically requests memory at runtime, the heap provides a chunk of memory whose address must be assigned to a pointer variable. 
- Addresses in the heap are not bound to variable names. 
- A local or global pointer variable can store the address of an anonymous heap memory location (e.g. a local pointer variable on the stack can point to heap memory), and dereferencing such a pointer enables a program to store data in the heap.
#### **[[Mallac and free functions]]**: 
**Malloc** and **free** are functions in the standard C library (`stdlib`) that a program can call to allocate and deallocate memory in the **heap**. To allocate heap memory, call `malloc`, passing in the total number of bytes of contiguous heap memory to allocate. Use the **`sizeof` operator** to compute the number of bytes to request. 
- Malloc returns a **pointer** (an address in memory), not a number. Its type is `void *` (generic pointer).
- **Prototype** (from `<stdlib.h>`):
```c
void *malloc(size_t size);
```
- **free functions**: When a program no longer needs the heap memory it dynamically allocated with `malloc`, it should explicitly deallocate the memory by calling the `free` function. It’s also a good idea to set the pointer’s value to `NULL` after calling `free`. 
```c
free(p); 
p = NULL; // good practice
```
#### Dynamically allocated Arrays and Strings
A dynamic array in c is an array whose memory is allocated at runtime, usually with `malloc` (or `calloc`/`realloc`), rather than being statically declared with a fixed size. Key characteristics:
- **lives in the heap** instead of the stack.
- **size chosen at runtime**, not compile time.
- **accessed with the same syntax** `arr[i]` as static arrays.
- must be **manually freed** with `free` when no longer needed.
```c
sizeof(<type>) * <number of elements>

// declare the variable array
int *arr; 
// allocate an array of 20 ints on the heap: 
arr = malloc(sizeof(int) * 20);
```
We recommend using the `[i]` syntax to access the elements of a dynamically allocated array. However, programs can also use the pointer dereferencing syntax (the `*` operator) to access array elements.
```c 
/* these two statements are identical: both put 8 in index 0 */
d_array[0] = 8; // put 8 in index 0 of the d_array
*d_array = 8;   // in the location pointed to by d_array store 8
```
Inside the function, it doesn’t matter whether the array came from, the *base address is only passed*: [[Static and dynamic]] 
- a **static declaration** (`int s_array[20];` → memory on stack), or
- a **dynamic allocation** (`int *d_array = malloc(...);` → memory on heap).
### 2.5
#### Single dimensional Arrays
Whether an array is statically declared or dynamically allocated via a single call to `malloc`. The exact address of the ith element depends on the number of bytes of the type stored in the array. For example, consider the following array declarations:
```c
int  iarray[6];  // an array of six ints, each of which is four bytes
char carray[4];  // an array of four chars, each of which is one byte
iarray and carray are just variable names, it can be anything.
```
The addresses of their individual array elements might look something like this:
 ```c
 addr   element
 1230:  iarray[0]
 1234:  iarray[1]
 1238:  iarray[2]
 1242:  iarray[3]
     ...
 1280:  carray[0]
 1281:  carray[1]
 1282:  carray[2]
 1283:  carray[3] 
```
#### Two dimensional Arrays
To statically declare a multidimensional array variable, specify the size of each dimension. For example:
```c
int   matrix[50][100];
short little[10][10];
```
Here, `matrix` is a 2D array of `int` values with 50 rows and 100 columns, and `little` is a 2D array of `short` values with 10 rows and 10 columns.
To access an individual element, indicate both the row and the column index:
```c
int   val;
short num;

val = matrix[3][7];  // get int value in row 3, column 7 of matrix
num = little[8][4];  // get short value in row 8, column 4 of litlle
```
the following nested loop initializes all elements in `matrix` to 0:
```c
int i, j;

for (i = 0; i < 50; i++) {  // for each row i
    for (j = 0; j < 100; j++) { // iterate over each column element in row i
        matrix[i][j] = 0;
    }
}
```
- The parameter points to the argument’s array elements and therefore the function can change values stored in the passed array.[[Two Dimensional Arrays]]
	`#define COLS  (100)`- The column dimension must be specified in the parameter definition of a 2D array so that the compiler can calculate the offset from the base address of the 2D array to the start of a particular row of elements.
- Statically allocated 2D arrays are arranged in memory in **row-major order**, meaning that all of row 0’s elements come first, followed by all of row 1’s elements, and so on.
- A single call to `malloc` allocates the total number of bytes needed to store the _N x M_ array of values:
```c
// allocate in a single malloc of N x M int-sized elements:
two_d_array = malloc(sizeof(int) * N * M);
```
#### Dynamically allocate 2D Arrays
- Method 1: **Single malloc and Function Parameters**
	- The programmer must explicitly compute the offset into the contiguous chunk of heap memory using a function of row and column index values (`[i*M + j]`, where `M` is the column dimension). [[Two Dimensional Arrays]] 
- Method 2: **The Programmer-Friendly Way**
	- Stores the array as an array of _N_ 1D arrays (one 1D array per row). It requires _N+1_ calls to `malloc`: one `malloc` for the array of row arrays, and one `malloc` for each of the _N_ row’s column arrays. [[Two Dimensional Arrays]]
	- Use if want to access individual elements in the matric of arrays.
	- Once allocated, individual elements of the 2D array can be accessed using double-indexing notation. `two_d_array[i][j] = 0;`
- Method 3: **An Array of Arrays and Function Parameters**
	- The array argument’s type is `int **` (a pointer to a pointer to an `int`), and the function parameter matches its argument’s type. Additionally, row and column sizes should be passed to the function. Because this is a different type from method 1, both array types cannot use a common function. [[Two Dimensional Arrays]]

---

# #Lecture Lectures
## Lecture 3
### Common Data Types in C 
- int: Signed integer, can be positive or negative  
- unsigned int (or just unsigned for short): Zero or positive values only  
- char: Character value (or a number, usually between -128 and 127)  
- float: Floating point number (i.e., allows for fractional values)  
- double: Floating point number (but with wider range of values
- Booleans: Could just use an int to represent a Boolean value. If int is 0, we interpret that as false. If int is 1, we interpret it as true.
	- C later “bolted on” Booleans with library in stdbool.h. Defines the bool data type and true/false literals. So you can just write:
```
bool is_attending_class = true;
```
### Hardware and Data Types
- Data is stored as **bits** (0s and 1s). 8 bits = 1 byte.
- Types use fixed numbers of bytes → determines range/precision.
- Use `sizeof(type)` to check size. [[C Language]]
### [[#Pointer]] 
Memory Addresses as Values. Functions may need addresses to modify variables outside their scope (e.g., swap). 
- For **pointers**: The special NULL pointer is false, all others true
![[Pasted image 20251001023344.png]]
### [[#Heap Memory]]
- **32-bit machine:** 2³² = 4 GiB addressable memory.
- **64-bit machine:** 2⁶⁴ = 16 exabytes.
- Key idea: bits are just bits; interpretation depends on type.
### [[#Arrays]]
- Elements are **contiguous in memory**.
- Array name = base address.
- Arrays and pointers are closely related:
    - `a[i]` is equivalent to `*(a + i)`.
	- Differences:
		- Array location fixed by compiler.
		- Pointer location can be reassigned.
## Lecture 4
### [[#String]]
- No built-in string type.
- Implemented as **char arrays**.
- Copying strings: 
```c
void string_copy(char *dst, char *src);
void string_copy_arr(char *dst, char *src) {
	int i = 0;
	while (src[i] != ‘\0’) {
		dst[i] = src[i];
		i++;
	}
	dst[i] = ‘\0’;
}
```
### Memory Image of a Program
Run Time vs Compile Time Sizes: Compile-time arrays: fixed size, known by compiler. 
Run-time arrays: size determined during execution.
Solution: use heap memory (via malloc).
- **Text**: machine instructions.
- **Global**: global + static vars.
- **Heap**: manual allocations (`malloc`).
- **Stack**: local variables + function calls.
- Stack and heap grow toward each other.
### Valgrind
- Tool to check memory usage.
- Usage: `valgrind ./program`
- Finds:
	- Memory leaks
	- Double free errors
	- Out-of-bounds access
## Lecture 5
Same as 3 and 4

---

# #Lab Lab - 2
Implementing pass by pointers, malloc and free functions, linked list implementation. Analyze the `list_funcs.c` file first and then go on to the `funcs_main.c`. Quiz questions are too basic.

---

# #Homework Homework - 2
1. **Q1, C**: Attempt to enter some absurd ages for the age computation.
	- Enter 5000
	- Enter -5000  
	Describe anything strange that seems to be happening based your  
    understanding of how basic arithmetic is supposed to work. If you happen to know WHY this strangeness is happening, describe it below. If not, you will find out soon.
	**Answer:** If you enter `5000` or `-5000`, the printed number of minutes is probably very large and may even be **negative** or otherwise “nonsense” compared to what you’d expect from normal arithmetic. 
	- This happens because `age_minutes` is an `int`, and the expression`age_minutes = age_years * 365 * 24 * 60;`overflows the range of a 32-bit signed integer for such huge ages.
	- When an `int` overflows, it wraps around according to two’s complement arithmetic [[50_Archive/UMN/Classes/Previous Classes/CSCI 2021/Week - 3#** Two's-Complement Encodings **|Two's complement]], producing incorrect (and sometimes negative) results. That’s why the output looks strange.
2. **Q1, D**: Describe which function is used to print information to the screen. Describe how it seems to work to substitute values into output and what _format specifier_ indicates an integer should be substituted.
	**Answer:** The function used to print to the screen is **`printf`**. It takes a _format string_ plus additional arguments. Inside the format string, placeholders like `%d` are used, and `printf` substitutes the extra arguments into those placeholders when printing.
	- Example from `age.c`:`printf("You are %d minutes old.\n", age_minutes);`
		Here `%d` is the **format specifier for an `int`**, so `age_minutes` is printed as a decimal integer in that spot.
3. **Q1, E**: Describe what function is used to read typed input interactively from a user in the 'age.c' program. Describe how its arguments differ from those for the arguments for printing to the screen earlier. Why is this difference necessary?
	**Answer:** The function used to read input is **`scanf`**. In `age.c` it is called like this: `scanf("%d", &age_years);` [[50_Archive/UMN/Classes/Previous Classes/CSCI 2021/Week - 1#1.2|Format Strings and scanf]]
	- Differences from `printf`:
		- `printf` takes values (e.g., `age_minutes`) to be **printed**.
		- `scanf` takes **addresses** of variables (e.g., `&age_years`) so it can **store** the user’s input into those variables. This difference is necessary because `scanf` needs to _modify_ the caller’s variables. Passing the address (using `&`) lets `scanf` write the read value into `age_years`.
4. **Q2 All problems are in the QUESTIONS.txt file in the homework 2**

---


