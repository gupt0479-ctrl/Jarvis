---
type: class
status: archived
created: 2025-10-10
updated: 2025-10-13
area:
  - "[[C Language]]"
  - "[[50_Archive/UMN/Classes/Previous Classes/CSCI 2021/Midterm - 1]]"
  - "[[Linked list]]"
  - "[[Text files]]"
tags:
  - "#class"
  - "#Textbook"
  - "#CSAPP"
  - "#DIS"
  - "#Lecture"
  - "#Lab"
  - "#Homework"
next: "[[50_Archive/UMN/Classes/Previous Classes/CSCI 2021/Week - 4|Week - 4]]"
---
# #Textbook Textbook (CSAPP - 2.1 - 2.4, DIS - 1.6, 2.7, 2.8)
## #CSAPP CSAPP
### 2.1 
- **Smallest Unit:** While everything is made of bits (0s and 1s), the smallest addressable unit of memory is a **byte**, which is a block of 8 bits. Your program sees memory as a giant array of bytes, and the address of any piece of data is the address of its first byte.
- **Hexadecimal Notation ("Hex"):** Writing numbers in binary is long and tedious. Decimal isn't great for seeing the underlying bit patterns. So, we use base-16, or hexadecimal, as a convenient shorthand.
	- It uses digits 0–9 and letters A–F.
	- Each hex digit represents exactly **4 bits** (e.g., `A` is `1010`, `F` is `1111`).
	- **Key Skill:** Converting between binary and hex is simple. Just group binary digits into sets of 4 and find the corresponding hex digit, or vice versa. For example, the binary `11001010` becomes `CA` in hex.
- **Word Size:** Every computer has a "word size," which is the nominal size for pointers and integers. It determines the maximum size of the virtual address space. Today, most machines are **64-bit** (8 bytes), a shift from the older 32-bit (4 bytes) standard. A 64-bit machine can access a vastly larger amount of memory.
- **Byte Ordering (Endianness):** When a piece of data is larger than one byte (like a 4-byte `int`), we need a rule for how to order the bytes in memory.
	- **Little Endian:** The "little end" (*least significant byte*) comes first, at the lowest memory address. Most Intel-compatible machines, including those running Linux and Windows, use this ordering.
	- **Big Endian:** The "big end" (*most significant byte*) comes first. Some machines from IBM and Oracle (Sun Microsystems) use this ordering.
	- **Why it Matters:** For most programming, this is invisible. But it becomes important when you are looking at raw byte sequences (like in a debugger) or sending data over a network between different machine types.
- **Bit-level and Logical Operations in C:** C provides operators to manipulate data at the bit level. [[50_Archive/UMN/Classes/Previous Classes/CSCI 2021/Week - 4#Bitwise Operations in C|Bit and Logical Operations]]
	- `&` (AND), `|` (OR), `^` (XOR), `~` (NOT). These are great for masking operations, like isolating a specific byte from a word (e.g., `x & 0xFF`). 
	- `&&` (Logical AND), `||` (Logical OR), `!` (Logical NOT). **Crucially, these are different!** They treat any non-zero value as `true` and return either `0` (false) or `1` (true). They also "short-circuit," meaning they don't evaluate the second argument if the result is already determined.
	- `<<` (Left Shift) and `>>` (Right Shift). A left shift `x << k` is like multiplying `x` by 2<sup>k</sup>. A right shift has two forms: [[50_Archive/UMN/Classes/Previous Classes/CSCI 2021/Week - 4#Bit shifting|Bit Shift]]
		- **Logical Right Shift:** Fills with 0s. Used for `unsigned` data in C.
		- **Arithmetic Right Shift:** Fills with copies of the most significant bit (sign extension). Used for signed data in C and is like dividing by 2<sup>k</sup> (rounding down).
### 2.2
**Unsigned Encodings:** This is a straightforward interpretation of a binary number. For a `w`-bit number, the values range from 0 to 2<sup>w</sup> - 1. Every number in this range has a unique bit pattern.
### Two's-Complement Encodings
This is the most common way to represent signed integers (positive, negative, and zero).
- **The Key Idea:** The most significant bit is a **sign bit** with a _negative_ weight. For a `w`-bit number, its weight is -2<sup>w-1</sup>. 
	- **Example (4 bits):** The number `1011` is `-1*8 + 0*4 + 1*2 + 1*1 = -5`.
- **Asymmetric Range:** Because zero is non-negative, the range of representable numbers is not symmetric. It goes from TMin = -2<sup>w-1</sup> to TMax = 2<sup>w-1</sup> - 1. For example, a signed 8-bit `char` can represent -128 to 127.
- **Conversions Between Signed and Unsigned:** In C, when you cast between signed and unsigned numbers of the same size, the **underlying bit pattern does not change**. This is a critical rule with surprising consequences.
	- Casting a negative number to `unsigned` makes it a large positive number. E.g., for 16 bits, casting `-1` (binary `1111...1`) to `unsigned short` results in 65,535.
	- When an operation involves both signed and unsigned values, C implicitly casts the signed value to unsigned. This can lead to unexpected behavior, especially with comparisons like `<` or `>`. For instance, `-1 < 0U` is **false** because `-1` is cast to the largest unsigned value!
### 2.3
1. **Unsigned Addition**: When you add two `w`-bit unsigned numbers in C, the operation is performed modulo 2<sup>w</sup>. This means if the result is too large to fit into `w` bits, it "wraps around.
	- **The Principle:** Imagine two unsigned numbers, `x` and `y`, each fitting within `w` bits. Their true mathematical sum `x + y` might require `w+1` bits. The computer discards the extra bit, effectively calculating the sum modulo 2<sup>w</sup>.
	- **Normal Case:** If `x + y < 2^w`, the sum doesn't overflow and the result is just `x + y`.
	- **Overflow Case:** If `x + y >= 2^w`, the sum overflows. The result is `x + y - 2^w`. This happens because the most significant bit (with a weight of 2<sup>w</sup>) is discarded.
	- **How to Detect Unsigned Overflow:** There's a simple trick to check if an unsigned addition overflowed. This works because if there's no overflow, the sum `s` must be greater than or equal to both `x` and `y`. 
		- If there is an overflow, the sum wraps around to a smaller number.
2. **Two’s-Complement Addition**: Same Bits, Different Meaning. This is a critical concept: **w-bit two's-complement addition has the exact same bit-level behavior as unsigned addition**. The processor uses the same hardware instruction for both. The only difference is how the result is interpreted.
	- **The Principle:** The result is the integer sum truncated to `w` bits. This can result in both positive and negative overflow.
	- **Normal Case:** When the sum `x + y` is within the two's-complement range (`TMin <= x+y <= TMax`), the result is simply `x + y`.
	- **Positive Overflow:** If you add two large positive numbers and the sum `x + y` becomes greater than `TMax`, the result wraps around to a negative number. The value becomes `x + y - 2^w`.
	- **Negative Overflow:** If you add two large negative numbers and the sum `x + y` becomes less than `TMin`, the result wraps around to a positive number. The value becomes `x + y + 2^w`.
	**How to Detect Two's-Complement Overflow:** The check is different from the unsigned case. In other words, overflow happens if and only if you add two numbers with the same sign and get a result with the opposite sign.
3. **Two’s-Complement Negation**:
	- **The Principle:** For any number `x`, its two's-complement negative is `-x`, with one crucial exception. The most negative number, `TMin`, has no positive counterpart. Its negation is `TMin` itself (`-TMin = TMin`). This is due to the asymmetric range of two's-complement numbers.
	- **Bit-Level Tricks for Negation:** There are two ways to compute the negative of a number `x` at the bit level:
		1. **Invert and Add 1:** The expression `-x` is identical to `~x + 1`. For example, for 4-bit `5` (`0101`), `~5` is `1010`. Adding 1 gives `1011`, which is `-5`.
		2. **Find Rightmost '1' and Flip:** Find the position of the rightmost '1' in the binary representation of `x`. Then, flip all the bits to the left of that position. For example, for `-4` (`1100`), the rightmost '1' is at position 2. Flipping the bit to its left gives `0100`, which is `4`.
4. **Unsigned and Two’s-Complement Multiplication**: Similar to addition, the multiplication of two `w`-bit numbers can result in a product that needs up to `2w` bits to be stored. C truncates this product to `w` bits.
	- **The Principle:** For **unsigned multiplication**, the result is the true product modulo 2<sup>w</sup>. `x *u_w y = (x * y) mod 2^w`.
		- For **two's-complement multiplication**, the result is the true product modulo 2<sup>w</sup>, which is then interpreted as a two's-complement number. `x *t_w y = U2Tw((x * y) mod 2^w)`.
	- **The Crucial Insight:** Just like addition, the bit-level representation of the `w`-bit product is **identical** for both unsigned and two's-complement multiplication. The same hardware instruction can be used for both.
5. **Multiplying and Dividing by Powers of 2**: Because `multiply` and `divide` instructions have historically been slow, compilers often try to replace them with faster **shift** and **add/subtract** operations when dealing with powers of 2.
	- **Multiplication by 2^k:** This is achieved by a **left shift** **<< k**.
		- The bit-level operation `x << k` gives the same result as both unsigned multiplication (`x *u_w 2^k`) and two's-complement multiplication (`x *t_w 2^k`).
		- Compilers cleverly use this property to multiply by any constant. For example, `x * 14` can be optimized to `(x << 4) - (x << 1)` which is `16*x - 2*x`.
	- **Division by 2^k:** This is achieved by a **right shift** **>> k**. However, the type of shift matters:
		- **Unsigned Division:** Use a **logical right shift** (fills with 0s). `x >> k` gives `floor(x / 2^k)`. 
	- **Two's-Complement Division (Rounding toward zero):** C integer division rounds toward zero (e.g., `-7 / 4 = -1`). An **arithmetic right shift** (fills with the sign bit) rounds negative numbers _down_ (e.g., `-7 >> 2 = -2`). To get the correct rounding, the compiler adds a "bias" before shifting if the number is negative. The expression `(x<0 ? x+(1<<k)-1 : x) >> k` correctly computes `x / 2^k`.

---

## #DIS DIS
### 1.6
#### [[Structs]]
Structs are used to create a collection of data elements of different types. A struct is a type used to represent a heterogeneous collection of data; it’s a mechanism for treating a set of different types as a single, coherent unit. There are three steps to defining and using `struct` types in C programs: [[Structs]] 
1. Define a new `struct` type that represents the structure.
2. Declare variables of the new `struct` type.
3. Use dot (`.`) notation to access individual field values of the variable.
C struct types are **lvalues** (they can appear on the left-hand side of an assignment statement). A struct variable can be assigned the value of another struct variable using a simple assignment statement.
```c
student2 = student1;  // student2 gets the value of student1
                      // (student1's field values are copied to
                      //  corresponding field values of student2)
                      
/* function prototype (prototype: a declaration of the
 *    checkID function so that main can call it, its full
 *    definition is listed after main function in the file):
 */
int checkID(struct studentT s1, int min_age);
// passing a struct
    can_vote = checkID(student1, 18);
```
### 2.7
#### Struct Pointers
A programmer can declare variables of type `struct studentT` or `struct studentT *` (a pointer to a `struct studentT`): [[Structs]]
To access individual fields in a pointer to a `struct`, the pointer variable first needs to be **dereferenced**.
```c
// the grad_yr field of what sptr points to gets 2021:
(*sptr).grad_yr = 2021;

// the age field of what sptr points to gets s.age plus 1:
(*sptr).age = s.age + 1;
```
C provides a special operator (`→`) that both dereferences a `struct` and accesses one of its field values. For example, `sptr→year` is equivalent to `(*sptr).year`
```c
// the gpa field of what sptr points to gets 3.5:
sptr->gpa = 3.5;

// the name field of what sptr points to is a char *
// (can use strcpy to init its value):
strcpy(sptr->name, "Lars");
```
![[Pasted image 20251001145211.png]]
#### Array of Structs
```c
struct studentT classroom1[40];   // an array of 40 struct studentT

struct studentT *classroom2;      // a pointer to a struct studentT
                                  // (for a dynamically allocated array)

struct studentT *classroom3[40];  // an array of 40 struct studentT *
                                  // (each element stores a (struct studentT *)

// classroom1 is an array:
//    use indexing to access a particular element
//    each element in classroom1 stores a struct studentT:
//    use dot notation to access fields
classroom1[3].age = 21;

// classroom2 is a pointer to a struct studentT
//    call malloc to dynamically allocate an array
//    of 15 studentT structs for it to point to:
classroom2 = malloc(sizeof(struct studentT) * 15);

// each element in array pointed to by classroom2 is a studentT struct
//    use [] notation to access an element of the array, and dot notation
//    to access a particular field value of the struct at that index:
classroom2[3].year = 2013;

// classroom3 is an array of struct studentT *
//    use [] notation to access a particular element
//    call malloc to dynamically allocate a struct for it to point to
classroom3[5] = malloc(sizeof(struct studentT));

// access fields of the struct using -> notation
// set the age field pointed to in element 5 of the classroom3 array to 21
classroom3[5]->age = 21;
```
A function that takes an array of type struct studentT as a parameter might look like this:
```c
void updateAges(struct studentT *classroom, int size) {
    int i;

    for (i = 0; i < size; i++) {
        classroom[i].age += 1;
    }
}
```
#### Self-Referential Structs
A struct can be defined with fields whose type is a pointer to the same `struct` type. A **[[Linked list]]** is one way to implement a **list abstract data type**. A list represents a sequence of elements that are ordered by their position in the list.
```c
struct node {
    int data;           // used to store a list element's data value
    struct node *next;  // used to point to the next node in the list
};
```
### 2.8
#### Standard Input/Output
Every running program begins with three default I/O streams: standard out (`stdout`), standard in (`stdin`), and standard error (`stderr`). A program can write (print) output to `stdout` and `stderr`, and it can read input values from `stdin`. `stdin` is usually defined to read in input from the keyboard, whereas `stdout` and `stderr` output to the terminal.
```c
#  redirect a.out's stdin to read from file infile.txt:
$ ./a.out < infile.txt

#  redirect a.out's stdout to print to file outfile.txt:
$ ./a.out > outfile.txt

# redirect a.out's stdout and stderr to a file out.txt
$ ./a.out &> outfile.txt

# redirect all three to different files:
#   (< redirects stdin, 1> stdout, and 2> stderr):
$ ./a.out < infile.txt 1> outfile.txt 2> errorfile.txt
```
The `fprintf` and `fscanf` functions serve as the file I/O counterparts in `stdio.h` to `printf` and `scanf`. They use a format string to specify what to write or read, and they include arguments that provide values or storage for the data that gets written or read.
#### getchar and putchar
The C functions `getchar` and `putchar` respectively read or write a single character value from `stdin` and to `stdout`. 
```c
ch = getchar();  // read in the next char value from stdin
putchar(ch);     // write the value of ch to stdout
```
#### [[Text files]]
To read or write a file in C, follow these steps:
1. _Declare_ a `FILE *` variable:
```c
    FILE *infile;
    FILE *outfile;
```
These declarations create pointer variables to a library-defined `FILE *` type. These pointers cannot be dereferenced in an application program. Instead, they refer to a specific file stream when passed to I/O library functions.    
2. _Open_ the file: associate the variable with an actual file stream by calling `fopen`. When opening a file, the _mode_ parameter determines whether the program opens it for reading (`"r"`), writing (`"w"`), or appending (`"a"`):
```c
    infile = fopen("input.txt", "r");  // relative path name of file, read mode
    if (infile == NULL) {
        printf("Error: unable to open file %s\n", "input.txt");
        exit(1);
    }
    
    // fopen with absolute path name of file, write mode
    outfile = fopen("/home/me/output.txt", "w");
    if (outfile == NULL) {
        printf("Error: unable to open outfile\n");
        exit(1);
    }
```
3. _Use_ I/O operations to read, write, or move the current position in the file:
```c
    int ch;  // EOF is not a char value, but is an int.
             // since all char values can be stored in int, use int for ch
    
    ch = getc(infile);      // read next char from the infile stream
    if (ch != EOF) {
        putc(ch, outfile);  // write char value to the outfile stream
    }
```
4. _Close_ the file: use `fclose` to close the file when the program no longer needs it:
```c
    fclose(infile);
    fclose(outfile);
```
The `stdio` library also provides functions to change the current position in a file:
```c
// to reset current position to beginning of file
void rewind(FILE *f);

rewind(infile);

// to move to a specific location in the file:
fseek(FILE *f, long offset, int whence);

fseek(f, 0, SEEK_SET);    // seek to the beginning of the file
fseek(f, 3, SEEK_CUR);    // seek 3 chars forward from the current position
fseek(f, -3, SEEK_END);   // seek 3 chars back from the end of the file
```


---

# #Lecture Lectures
## Lecture 5
#### [[#Structs]]
- Like arrays, but fields can be different types.
- Declared with `typedef struct`:
```c
typedef struct {
	double height;     
	int age;     
	char name[16]; 
} person_t;
```
`typedef struct { ... } person_t;` → define an anonymous struct and create a short alias `person_t`.
- Access with dot `.` operator.
- Example: 
```c
person_t wizard; 
wizard.height = 6.023; 
wizard.age = 106;
strcpy(wizard.name, "Gandalf");
```
## Lecture - 6
### Padding to Ensure Alignment
- Hardware prefers accessing aligned memory.
- Rules:
    1. Instance of type T must start at an address multiple of `sizeof(T)`.
    2. Struct must start at an address multiple of its largest field size.
- Example:`student_b_t`: `char` + padding (7 bytes) + `double` → size 16.
### [[#Text files]]
`FILE *` = file handle.
- Functions:
    - `fopen(name, mode)` → open file.
    - `fclose(handle)` → close file.
    - `rewind(handle)` → reset file position. 
    - Always check return values
- Reading/Writing Text Files:
	- `fscanf(FILE *fh, char *format, ...)` → read from file.
	- `fprintf(FILE *fh, char *format, ...)` → write to file.
	- `fscanf` returns `EOF` at end of file.
```c
FILE *fh = fopen("my_integer.txt", "w"); 
int x = 42; 
fprintf(fh, "%d\n", x); 
fclose(fh);
```
- Reading/Writing Binary Files: 
	- `fread(dest, byte_size, count, FILE *fh)`
	- `fwrite(src, byte_size, count, FILE *fh)`
- Work with raw bytes → efficient but less portable.
```c
FILE *fh = fopen("my_integer.bin", "w");
int x = 42;
fwrite(&x, sizeof(int), 1, fh);
fclose(fh);

//Write arrays of these structs to a text and to a binary file. 
//Return 0 on success and -1 on failure.
typedef struct {
	double height;
	int age;
	char initial;
} person_t;

//Text file
int write_people_text(char *file_name, person_t *people, int n_people) {
	FILE *f = fopen(file_name, "w");
	if (f == NULL) {
		return -1;
	}
	for (int i = 0; i < n_people; i++) {
		fprintf(f, "%f %d %c\n", people[i].height, people[i].age,
			people[i].initial);
	}
	fclose(f);
	return 0;
}

//Binary file
int write_people_text(char *file_name, person_t *people, int n_people) {
	FILE *f = fopen(file_name, "w");
	if (f == NULL) {
		return -1;
	}
	// All in one operation:
	fwrite(people, sizeof(person_t), n_people, f);
	// Or use a loop like so:
	for (int i = 0; i < n_people; i++) {
		fwrite(people + i, sizeof(person_t), 1, f);
	}
	fclose(f);
	return 0;
}
```
## Lecture 7
Same Things as lecture 6, lecture 6 has some lecture 8 stuff in text files.
## Lecture 8
### Decimal Numbers
- Humans use **base 10 (decimal)**. Each digit represents a power of 10.
- Example:`2021 = 2×10^3 + 0×10^2 + 2×10^1 + 1×10^0`.
- **Binary Numbers**: Computers use **base 2 (binary)**.
	- Each digit = power of 2.
	- Example:`1001 = 1×2^3 + 0×2^2 + 0×2^1 + 1×2^0 = 9`
	- Patterns:
	    - Decimal: largest with n digits = 10^n – 1 (e.g., 9999).        
	    - Binary: largest with n bits = 2^n – 1 (e.g., 1111 = 15).
- **Hexadecimal (Base 16)**: Convenient because *1 hex digit = 4 bits*.
	- Example: `0x1A = 1×16^1 + 10×16^0 = 26`.
	- Used for printing pointers (`%p`). Prefix `0x` → hex.
	- *Trick*: Convert decimal → binary (divide by 2, or recall powers of 2), then group into 4-bit chunks → directly into hex. Example: Decimal 66
		1. Write 66 in binary: 66 ÷ 2 repeatedly → `1000010` → pad to 8 bits → `0100 0010`.
		2. Split into 4-bit chunks: `0100 | 0010`
		3. Convert each chunk to hex: `0100 = 4`, `0010 = 2`→ **0x42**
	- `0 1 2 3 4 5 6 7 8 9 A B C D E F`
	- A in hex = decimal 10
	- B in hex = decimal 11
	- C in hex = decimal 12
	- D in hex = decimal 13
	- E in hex = decimal 14
	- F in hex = decimal 15
	- So whenever a 4-bit binary group equals decimal 10–15, we write a letter instead of a number.
- **Octal (Base 8)**: *1 octal digit = 3 bits*. Less common today, but appears in some legacy systems. 
	- Example: `137₈ = 1×64 + 3×8 + 7 = 95`.
	- Trick: Convert decimal → binary → group into 3-bit chunks. Example: Decimal 66
		- Binary = `1000010`. Group in 3s (pad left): `001 | 000 | 010`= `1 | 0 | 2` → **Octal = 102₈**
### Converting From Decimal to Other Bases  
1. Start with: What’s the largest power of (2, 8, 16)`p`that does not exceed the current number(decimal) `n`?  
2. Determine the multiple of this power that doesn’t exceed `n` – that is your first binary digit `d` 
3. Subtract `d × p` from n, and now consider next highest power and find multiple (including 0) of this power that doesn’t exceed `new n`
4. Repeat
	Example: Decimal 21 → Binary `n = 21`
	- Largest power of 2 ≤ 21 = 16(2^4), `p = 16` 
	- How many times does 16 fit into 21? `21 ÷ 16 = 1` → so `d = 1`.
	- 21 – 16 = 5. `n - p * d`
	- Next: `new n = 5`. Next power of 2 down = 2^3(8). Does 8 fit into 5?
		- No → digit `d = 0`.
		- Keep `n = 5`.
	- Next: 2^2 = 4, fit into 5. `p = 4 & d = 1`. `new n = 1`
	- Next: 2^1 = 2, does not fit into 1. `d = 0`
	- Next: 1^1 = 1, fit into 1. `p = 1 & d = 1`
	- Binary = `10101`.
|Decimal | Binary | Octal | Hex |
|---      |---               |-      |--- |
|77      |`01001101`  |115   |`0x4D`|
|61      |`00111101`  |75     |`0x3D`|
|167     |`10100111` |247   |`0xA7`|
|38332|`1001010110111100`|112674|`0x95BC`|
Why do programmers confuse Halloween and Christmas?
- Oct 31 = Decimal 31.
- Dec 25 = Decimal 25.
- But in octal, `31₈ = 25₁₀`
**Conversion Tricks**
- Group bits into chunks:
    - 4 bits = hex digit.
    - 3 bits = octal digit.
- Example: Decimal 38332 = binary `1001 0101 1011 1100`.
    - In hex: `0x95BC`.
- Hex digits grouped in pairs = 1 byte (8 bits).
### Representing Characters
- With **n bits**, can represent 2^n values.
- ASCII → 7-bit encoding of characters.
- 128 unique chars: letters, numbers, punctuation, control codes.
- Extended ASCII (8 bits) → 256 chars.
- Each character assigned a number (e.g., `'A' = 65`). 
- Universal → allows text exchange between systems.

---

# #Lab Lab - 3 
## The “story” of execution
When you run: `./treasure_main -txt map1.txt`
1. **main reads command line**:
	- `argc` tells how many tokens
	- `argv[1]` is `-txt`, `argv[2]` is filename  
	That’s exactly the quiz answer in QUESTIONS.txt
2. main chooses which loader:
	- `strcmp(file_mode, "-txt") == 0` → call `treasuremap_load_text`
	- else → assume binary and call `treasuremap_load_binary`
3. loader returns a **heap-allocated** `treasuremap_t *`
4. program prints it (using `treasuremap_print`)
5. program frees it (using `treasuremap_free`)
## Concepts
1. **Endianness** (where it matters here): Binary reading uses `fread(&tmap->height, sizeof(int), 1, file_handle);`
	This copies raw bytes directly into an `int`. That assumes:
	- same `sizeof(int)` (4 bytes here)
	- same endianness for writer/reader  
	This is why CSAPP emphasizes endianness and “binary isn’t portable across machines.”. Text mode avoids this because parsing digits with `fscanf` is portable.
2. [[#Text files|File I/O]]: text vs binary (DIS 2.8 + lecture notes)
	- Text open: `fopen(file_name, "r")`
	- Binary open: `fopen(file_name, "rb")`
	Text reads with `fscanf(...)` (parses formatted tokens).
	Binary reads with `fread(...)` (copies raw bytes into memory).
3. *Allocate the struct*: `treasuremap_t *tmap = malloc(sizeof(treasuremap_t));. 
	- Heap allocation is needed because `main()` returns this pointer and uses it after the function ends.  
	- If you used a local `treasuremap_t t;` and returned `&t`, it would be a dangling pointer.
4. *Read header fields*:
```c
fscanf(file_handle, "%d %d", &tmap->height, &tmap->width);
fscanf(file_handle, "%d", &tmap->ntreasures);
```  
`tmap` is a pointer to a struct.`tmap->height` accesses the `height` field of that struct. 
- Important: **`tmap->height` is an actual int variable stored inside the struct**.`&tmap->height` takes the address of that int field.
- So:`&tmap->height` is a pointer to the height field inside the heap-allocated struct.
- Are you dereferencing `tmap`? Yes, conceptually: 
	- The `->` operator is basically shorthand for:`(*tmap).height`/`tmap->height`
	But **you are not “dereferencing a pointer to a variable called `tmap`”**. You’re dereferencing `tmap` (a pointer) to access the struct it points to.
- Why do we need `&` if we already used `->`? Because:
	- `->` gives you the **int field**
	- `&` then turns that into **address of that int field**
	- and `fscanf` needs the address 
*So the full meaning is*: “read an int from the file, and store it into the `height` field of the struct that `tmap` points to.”
5. *Allocate the locations array*: `tmap->locations = malloc(sizeof(treasureloc_t) * tmap->ntreasures);`. 
	- So `tmap->locations` means: “Go to the `treasuremap_t` struct that `tmap` points to, and access its `locations` field.”. 
	- That field (`locations`) is itself a pointer — it will point to the _start of a dynamically allocated array_ of `treasureloc_t`.
	- This is classic pattern: read size → malloc array → fill it.
6. Read each treasure
```c
fscanf(file_handle, "%d", &tmap->locations[i].row);
fscanf(file_handle, "%d", &tmap->locations[i].col);
fscanf(file_handle, "%127s", tmap->locations[i].description);
```
**Important detail:** `%127s` prevents overflow into the `description[128]` buffer (safety). Also `%s` stops at whitespace. That’s why the map uses names like `Death_Crystals` with underscores (no spaces).
7. The *“nested struct syntax” question* (this is exam gold): This line from the quiz:`&tmap->locations[i].row`
	Breakdown:
	- `tmap` is a pointer → use `->` to access its field `locations`
	- `locations` is a pointer to an array of `treasureloc_t` → use `[i]` to pick element i
	- `.row` accesses the row field inside that struct element
	- `&` because `fscanf` needs an **address** to store into
	So it’s literally: **(pointer deref) → (array index) → (field select) → (address-of)**
	This is the cleanest example of DIS 2.7 you’ll ever see.
8. *Binary loader*: why it has “description_len”:
	- Binary format includes: height(int), width(int), ntreasures(int)
	- for each treasure: row(int), col(int), description_len(int), description bytes
	Why? Because in binary we don’t have whitespace/newlines to “separate tokens.” We need an explicit length so we know how many bytes to read.
	In code:
```c
fread(&description_len, sizeof(int), 1, file_handle);
fread(tmap->locations[i].description, sizeof(char), description_len, file_handle);
tmap->locations[i].description[description_len] = '\0';
``` 
That last line is crucial: fread does **not** add a null terminator. You must. This maps to your “Text files vs raw bytes” notes perfectly.
9. *Freeing memory (ownership rules)*:`treasuremap_free` does:
```c
free(tmap->locations);
free(tmap);
```
Why this exact order?
- `tmap->locations` was allocated separately; it lives *inside* the heap struct.
- If you free `tmap` first, you lose access to `tmap->locations` (and can’t safely free it).
So the rule is: **free children first, then free the parent.**

---

# #Homework Homework - 3
## Problem 1
2. Identify which code does each action (in `read_all_doubles()`)
	1. *Opens the file for reading and checks for errors:*
		- Open: `FILE *fin = fopen(filename, "r");`    
		- Check failure: `if (fin == NULL) { return NULL; }`
	2. *Counts all the doubles in the file (first pass)*:
		- Setup: `double tmp; int count = 0;`    
		- Counting loop + stopping at EOF: 
			- `while (1) { ... }`
		    - `int ret = fscanf(fin, "%lf", &tmp);`        
			- `if (ret == EOF) break;`        
		    - `count++;`
	3. *Allocates memory for doubles in the file*:`double *data = malloc(count * sizeof(double));`
	4. *Moves the file read position to the beginning of the file*:`rewind(fin);`    
	5. *Closes the file when reading is complete*: `fclose(fin);`    
3. **Where is the malloc’d memory freed and why?**
	The memory returned by `read_all_doubles()` is freed in `main()` using:`free(nums);`
	**Why:** `read_all_doubles()` allocates the array with `malloc` and returns it, so **the caller owns that heap memory** and must free it after it’s done using it. Otherwise you leak memory.
4. **Explain the `printf` formatting (“table-like” output)**
	In `main()`, the print line is: `printf("[%d] : %8.2f == %10.4e\n", i, nums[i], nums[i]);`
	- Breakdown:
		- `[%d]` prints the **index** `i` as a decimal int.
		- `%8.2f` prints `nums[i]` in **fixed-point** format:
		- `8` = minimum field width of 8 characters (pads with spaces on the left)
	    - `.2` = 2 digits after the decimal
	    - so values line up in a column.
    - `%10.4e` prints the same number in **scientific notation**:
	    - `10` = minimum field width 10
	    - `.4` = 4 digits after decimal in mantissa
	    - `e` = exponent form (like `3.7066e+04`)
	- The spaces + fixed widths create the “aligned columns” look.
## PROBLEM 2: Binary Files
1. What do you see when opening `items.bin` in a text editor?
	I see some item names because the file stores names as raw ASCII bytes, but I also see NUL/garbage because the file also stores integers (lengths and counts) in binary, and those bytes aren’t printable characters.
2. Run `read_items.c` on `items.bin`
	When you upload `items.bin`, you’ll compile/run like this:`gcc -Wall -Wextra read_items.c -o read_items`, `./read_items items.bin`.
	-  The output lines will look like: `<count> of Item '<name>'` And that output explains what you saw in the editor:
		- the readable bits correspond to the item **names** and the unreadable bits correspond to binary **ints** (length + count).
3. **How do we learn the string length, and what does it help us do?**
	The program first reads an integer `name_len` from the file:`fread(&name_len, sizeof(int), 1, f);`
	That length helps with **two critical things**:
	1. **Read exactly the right number of bytes for the name**:`fread(current.name, sizeof(char), name_len, f);`
	2. **Turn those raw bytes into a valid C string** by adding the null terminator:`current.name[name_len] = '\0';`
	(Without knowing `name_len`, you wouldn’t know how many bytes to read, and you wouldn’t know where to put `'\0'`.)

---
