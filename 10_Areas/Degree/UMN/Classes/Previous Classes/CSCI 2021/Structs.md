---
type: class
status: archived
created: 2025-10-26
updated: 2025-10-11
area:
  - "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2021/Week - 3|Week - 3]]"
  - "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2021/Week - 11|Week - 11]]"
  - "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2021/Midterm - 1|Midterm - 1]]"
tags:
  - "#class"
next: "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2021/Week - 3|Week - 3]]"
---
# Defining a Struct type
A struct type definition should appear _outside of any function_, typically near the top of the program’s `.c` file. The syntax (`struct` is a reserved keyword):
```c
struct <struct_name> {
    <field 1 type> <field 1 name>;
    <field 2 type> <field 2 name>;
    <field 3 type> <field 3 name>;
    ...
};

EX:
struct studentT { // named struct, no typedef
    char name[64];
    int age;
    float gpa;
    int grad_yr;
};

typedef struct studentT {
    char name[64];
    int age;
    float gpa;
    int grad_yr;
} student_t;
```
`struct studentT { ... };` → define a type `struct studentT`. you must always prefix with `struct`.
`typedef struct studentT { ... } student_t;` → best of both worlds: named struct with a clean typedef alias.
# Declaring Variables
the name of our new struct type is two words, `struct studentT`.
```c
struct studentT student1, student2; // student1, student2 are struct studenT
```
# Accessing Field Values
use _dot notation_:
```c
<variable name>.<field name>

// The 'name' field is an array of characters, so we can use the 'strcpy'. string library function to fill in the array with a string value.
strcpy(student1.name, "Kwame Salter");

// The 'age' field is an integer.
student1.age = 18 + 2;

// The 'gpa' field is a float.
student1.gpa = 3.5;
```
# Pointer Structs
```c
struct studentT s;
struct studentT *sptr;

// think very carefully about the type of each field when
// accessing it (name is an array of char, age is an int ...)
strcpy(s.name, "Freya");
s.age = 18;
s.gpa = 4.0;
s.grad_yr = 2020;

// malloc space for a struct studentT for sptr to point to:
sptr = malloc(sizeof(struct studentT));
if (sptr == NULL) {
    printf("Error: malloc failed\n");
    exit(1);
}
```
Note that the call to `malloc` initializes `sptr` to point to a dynamically allocated struct in heap memory.
## Pointer fields
Structs can also be defined to have pointer types as field values. For example:

```c
struct personT {
    char *name;     // for a dynamically allocated string field
    int  age;
};

int main(void) {
    struct personT p1, *p2;

    // need to malloc space for the name field:
    p1.name = malloc(sizeof(char) * 8);
    strcpy(p1.name, "Zhichen");
    p1.age = 22;


    // first malloc space for the struct:
    p2 = malloc(sizeof(struct personT));

    // then malloc space for the name field:
    p2->name = malloc(sizeof(char) * 4);
    strcpy(p2->name, "Vic");
    p2->age = 19;
    ...

    // Note: for strings, we must allocate one extra byte to hold the
    // terminating null character that marks the end of the string.
}
```