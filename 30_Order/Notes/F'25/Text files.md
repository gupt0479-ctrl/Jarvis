---
type: class
status: archived
created: 2025-10-23
updated: 2025-09-12
area:
  - "[[50_Archive/UMN/Classes/Previous Classes/CSCI 2021/Week - 3|Week - 3]]"
  - "[[C Language]]"
  - "[[50_Archive/UMN/Classes/Previous Classes/CSCI 2021/Midterm - 1|Midterm - 1]]"
tags:
  - "#class"
next: "[[50_Archive/UMN/Classes/Previous Classes/CSCI 2021/Week - 3|Week - 3]]"
---
### Standard and File I/O Functions in `stdio.h`
The C `stdio.h` library has many functions for reading and writing to files and to the standard file-like streams (`stdin`, `stdout`, and `stderr`).
```c
// ---------------
// Character Based
// ---------------

// returns the next character in the file stream (EOF is an int value)
int fgetc(FILE *f);

// writes the char value c to the file stream f
// returns the char value written
int fputc(int c, FILE *f);

// pushes the character c back onto the file stream
// at most one char (and not EOF) can be pushed back
int ungetc(int c, FILE *f);

// like fgetc and fputc but for stdin and stdout
int getchar();
int putchar(int c);

// -------------
// String  Based
// -------------

// reads at most n-1 characters into the array s stopping if a newline is
// encountered, newline is included in the array which is '\0' terminated
char *fgets(char *s, int n, FILE *f);

// writes the string s (make sure '\0' terminated) to the file stream f
int fputs(char *s, FILE *f);

// ---------
// Formatted
// ---------

// writes the contents of the format string to file stream f
//   (with placeholders filled in with subsequent argument values)
// returns the number of characters printed
int fprintf(FILE *f, char *format, ...);

// like fprintf but to stdout
int printf(char *format, ...);

// use fprintf to print stderr:
fprintf(stderr, "Error return value: %d\n", ret);

// read values specified in the format string from file stream f
//   store the read-in values to program storage locations of types
//   matching the format string
// returns number of input items converted and assigned
//   or EOF on error or if EOF was reached
int fscanf(FILE *f, char *format, ...);

// like fscanf but reads from stdin
int scanf(char *format, ...);
```
In general, scanf and fscanf are sensitive to badly formed input. Here are a few example calls to `fscanf` (and one to `fprintf`) with different format strings (let’s assume that the `fopen` calls from above have executed successfully):

```c
int x;
double d;
char c, array[MAX];

// write int & char values to file separated by colon with newline at the end
fprintf(outfile, "%d:%c\n", x, c);

// read an int & char from file where int and char are separated by a comma
fscanf(infile, "%d,%c", &x, &c);

// read a string from a file into array (stops reading at whitespace char)
fscanf(infile,"%s", array);

// read a double and a string up to 24 chars from infile
fscanf(infile, "%lf %24s", &d, array);

// read in a string consisting of only char values in the specified set (0-5)
// stops reading when...
//   20 chars have been read OR
//   a character not in the set is reached OR
//   the file stream reaches end-of-file (EOF)
fscanf(infile, "%20[012345]", array);

// read in a string; stop when reaching a punctuation mark from the set
fscanf(infile, "%[^.,:!;]", array);

// read in two integer values: store first in long, second in int
// then read in a char value following the int value
fscanf(infile, "%ld %d%c", &x, &b, &c);
```