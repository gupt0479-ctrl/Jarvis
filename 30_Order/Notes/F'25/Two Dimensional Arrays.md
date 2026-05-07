---
type: class
status: archived
created: 2025-09-19
updated: 2025-09-20
area:
  - "[[C Language]]"
  - "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2021/Week - 2]]"
tags:
  - "#class"
next: "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2021/Week - 2]]"
---
```c
#define COLS  (100)

/*
 * init_matrix: initializes the passed matrix elements to the
 *              product of their index values
 *   m: a 2D array (the column dimension must be 100)
 *   rows: the number of rows in the matrix
 *   return: does not return a value
 */
void init_matrix(int m[][COLS], int rows) {
    int i, j;
    for (i = 0; i < rows; i++) {
        for (j = 0; j < COLS; j++) {
            m[i][j] = i*j;
        }
    }
}

int main(void) {
    int matrix[50][COLS];
    int bigger[90][COLS];

    init_matrix(matrix, 50);
    init_matrix(bigger, 90);
    ...
```

- Method 1:  **Single malloc and Function Parameters**
Here’s an example of how a programmer would structure code to initialize all the elements of a 2D array:
```c
// access using [] notation:
//   cannot use [i][j] syntax because the compiler has no idea where the
//   next row starts within this chunk of heap space, so the programmer
//   must explicitly add a function of row and column index values
//   (i*M+j) to map their 2D view of the space into the 1D chunk of memory
for (i = 0; i < N; i++) {
    for (j = 0; j < M; j++) {
        two_d_array[i*M + j] = 0;
    }
}

Example:
/*
 * initialize all elements in a 2D array to 0
 *  arr: the array
 *  rows: number of rows
 *  cols: number of columns
 */
void init2D(int *arr, int rows, int cols) {
    int i, j;
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            arr[i*cols + j] = 0;
        }
    }
}

int main(void) {
    int *array;
    array = malloc(sizeof(int) * N * M);
    if (array != NULL) {
        init2D(array, N, M);
    }
    ...
```

- Method 2: **The Programmer-Friendly Way**
A programmer can use double indexing syntax to access individual elements of the 2D array (the first index is an index into the array of rows, the second index is an index into the array of column elements within that row).
```c
// the 2D array variable is declared to be `int **` (a pointer to an int *)
// a dynamically allocated array of dynamically allocated int arrays
// (a pointer to pointers to ints)
int **two_d_array;
int i;

// allocate an array of N pointers to ints
// malloc returns the address of this array (a pointer to (int *)'s)
two_d_array = malloc(sizeof(int *) * N);

// for each row, malloc space for its column elements and add it to
// the array of arrays
for (i = 0; i < N; i++) {
// malloc space for row i's M column elements
    two_d_array[i] = malloc(sizeof(int) * M);
}
```
The programmer declares a variable (`two_d_array`) of type `int **` that will store the address of a dynamically allocated array of `int *` element values.

- Method 3: **An Array of Arrays and Function Parameters**
```c
/*
 * initialize a 2D array
 * arr: the array
 * rows: number of rows
 * cols: number of columns
 */
void init2D_Method2(int **arr, int rows, int cols) {
    int i,j;

    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            arr[i][j] = 0;
        }
    }
}

/*
 * main: example of calling init2D_Method2
 */
int main(void) {
    int **two_d_array;

    // some code to allocate the row array and multiple col arrays
    // ...

    init2D_Method2(two_d_array, N, M);
    ...
```