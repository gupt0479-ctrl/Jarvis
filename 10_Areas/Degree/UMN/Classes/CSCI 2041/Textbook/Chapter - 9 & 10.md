---
type: class
input_kind: book
status: sprout
created: 2026-02-27
updated:
area:
  - "[[UMN Board]]"
  - "[[10_Areas/Degree/UMN/Classes/CSCI 2041/Week - 4|Week - 4]]"
  - "[[CSCI 2041 Board]]"
  - "[[OCaml]]"
tags:
  - "#class"
  - "#Textbook"
next: "[[10_Areas/Degree/UMN/Classes/CSCI 2041/Week - 3|Week - 3]]"
---
# Chapter 9 - Exceptions
In OCaml, **exceptions** are a sophisticated control mechanism used to signal that a computation cannot proceed normally due to a run-time error or to intentionally alter the flow of execution. When an exception is raised, the current operation is **aborted**, and control jumps to the nearest active handler.
## 9.1 The Mechanics of Exceptions
### 9.1.1 Defining and Raising
- **Definition:** New exceptions are created using the `exception` keyword and must start with an **uppercase letter**. They can optionally carry data (a "payload").
    - _Example:_ `exception AL_error of string`.
- **The** **exn** **Type:** All exceptions belong to the built-in type `exn`. Uniquely, `exn` is an **open type**, meaning you can add new constructors (exceptions) to it at any point in your program.
- **Raising:** The `raise` function triggers the exception. Its type is `exn -> 'a`, which is "striking" because it appears to produce a value of any type. In reality, it never returns a value to the caller; it jumps away, so its "return type" is irrelevant to the local computation.
### 9.1.2 Handling with `try...with`
- **Syntax:** The `try expression with patterns` construct evaluates an expression.
- **Outcome:** If the expression evaluates to a value, that value is returned. If an exception is raised, OCaml performs **[[OCaml - Types of Programming#“Mix-match logic” (how the course expects you to use both styles)|match–with]]** logic against the patterns in the `with` block.
- **The Exception Stack:** OCaml maintains an internal **exception stack** that mirrors the call stack. When a `try` block is entered, a handler is pushed; when the block finishes, it is popped. If an exception is raised, OCaml searches the stack from top to bottom for the first matching handler.
> [!INFO] **First-Class Exceptions** Because exceptions are values of the type `exn`, they are **first-class objects**. You can pass them as arguments, return them from functions, or even store them in data structures like a `list`.
## 9.2 Standard Library Exceptions
The textbook and professor highlight several "built-in" emergencies the [[match–with|Dispatcher]] must handle:
1. **[[Not_found]]:** Raised by search functions (like `List.assoc`) when a key is missing. This is considered a **routine** exception expected during normal operation.
2. **[[Invalid_argument]]:** Signals **programming errors** that should never happen in a correct program, such as array bounds violations (`index out of bounds`).
3. **[[Failure]]:** Used for **benign errors** or external events from which a program might reasonably recover, such as failing to parse a string into an integer.
4. **[[Match_failure]]:** Raised when a value is passed to an **incomplete pattern match**. The compiler warns you about this at compile-time; heeding these warnings prevents this exception at runtime.
5. **[[Stack_overflow]] & [[Out_of_memory]]:** Severe system-level exceptions indicating resource exhaustion. These should rarely be caught.
## 9.3 Advanced Uses and Analogies
1. The "Billion-Dollar Mistake": The professor notes that OCaml has **no general null pointer**. In languages like C or Java, a failed search returns `null`, leading to frequent crashes. OCaml avoids this by using exceptions (like `Not_found`) or the `'a option` type, forcing the programmer to handle the "empty" case explicitly.
2. Flow Control and Optimization
	- **Breaking Loops:** Since OCaml has no `break` or `continue` keywords, exceptions are used to abort loops prematurely.
	- **Memory Efficiency:** Exceptions can prevent **needless list copying**. Instead of a recursive function rebuilding a list only to find a value wasn't there, it can `raise` an exception to return the original, unchanged list immediately.
	- **Finally (Unwind-Protect):** A custom `finally` function can be written to ensure resources (like files) are closed even if an error occurs during processing.
## 9.4 Code Example: `alget` with Custom Exception
_This concept was covered in_ **Lecture 6** _during the discussion on [[Association list|Association Lists]]._
```ocaml
exception AL_error of string (* Ch 9.1.1: Define constructor with string payload *)
let rec algetting pairs key =
  match pairs with
  | [] -> raise (AL_error "no such key") (* Ch 9.1.1: Abort search *)
  | (other_key, other_value) :: other_pairs ->
      if key = other_key then other_value
      else algetting other_pairs key (* Tail-recursive search *)
(* Usage *)
let find_it p k =
  try algetting p k with
  | AL_error msg -> Printf.printf "Error: %s\n" msg; 0 (* Catch and handle *)
```
Line-by-Line Explanation:
1. **exception AL_error**: Extends the `exn` open type with a new tagged variant.
2. **raise (AL_error ...)**: Signals an emergency to the [[match–with|Dispatcher]]. The function stops here and begins searching the exception stack for a handler.
3. **try ... with**: Sets up a handler on the exception stack.
4. **AL_error msg -> ...**: Uses **pattern matching** to extract the "no such key" string (the payload) and resolve the error gracefully.
## Midterm Check
# Chapter 10 - Input and Output
This chapter details the OCaml I/O library, which provides portable system calls for interacting with files, devices, and communication channels. Unlike the purely **[[functional programming|applicative]]** style of earlier chapters, I/O operations are inherently **imperative**, relying on side-effects and specific execution orders.
## 10.1 Channels: The Foundation of I/O
OCaml uses two primary data types to handle I/O:
- **in_channel**: A channel from which characters can be read.
- **out_channel**: A channel to which characters can be written.
1. *Standard Channels*: At program startup, three standard Unix-style descriptors are automatically opened:
	1. **stdin**: The standard input stream.
	2. **stdout**: The standard output stream.
	3. **stderr**: The standard output stream for error messages.
2. *File Opening and Closing*: Files are opened using specific functions that return a channel:
	- **Text Mode**: `open_out` and `open_in` perform line-termination translation on certain systems (like Windows).
	- **Binary Mode**: `open_out_bin` and `open_in_bin` write/read data exactly as provided, with no translation.
	- **General Opening**: `open_out_gen` and `open_in_gen` allow for complex flags (e.g., `Open_append`, `Open_creat`, `Open_trunc`) and Unix permissions.
	- **Manual Closing**: Channels are **not** closed automatically; you must use `close_out` and `close_in` to release system resources.
> [!INFO] **Sys_error** If a file cannot be opened (due to missing permissions or incorrect paths), OCaml raises the `Sys_error` exception.
## 10.2 Reading and Writing Data
Basic Operations
- **Writing**: `output_char` (single char), `output_string` (entire string), and `output` (a specified substring length).
- **Reading**: `input_char` (one char) and `input_line` (reads until a newline, discarding the terminator).
> [!INFO] **End_of_file (EOF)** Reading functions raise the `End_of_file` exception when they reach the end of the stream before completing the read. This is a common way to terminate a reading loop.
> - [[OCaml primitive data types|Value I/O]] (Binary & Unsafe)

OCaml can pass arbitrary values through binary channels using `output_value` and `input_value`.
- **The Unsafe Rule**: The textbook warns that `input_value` is **unsafe**. It returns a value of type `'a`, and the compiler cannot verify that the type being read matches the type that was originally written. If they differ, the program may fail unpredictably.
## 10.3 Channel Manipulation and Buffering
- **Seeking**: `seek_out` and `seek_in` change the current position in a file.
- **Positioning**: `pos_out` and `pos_in` return the current byte offset.
- **[[Persistence|Buffering]]**: OCaml I/O is **buffered** for efficiency. Data may not be physically written to the disk until the buffer is full or the channel is closed.
- **flush**: Use the `flush` function to force the writing of any data currently sitting in the output buffer.
## 10.4 The [[Printf]] and [[Scanf]] Modules
*Formatted Output (`Printf`)*: The `Printf` module provides type-safe formatting. The compiler analyzes the **format string** (e.g., `"%d"`) to ensure arguments match the required types.
- **Specifiers**: `%d` (int), `%f` (float), `%s` (string), `%b` (bool), and `%a` (user-defined printer).
- **Functions**: `printf` (to stdout), `fprintf` (to any channel), and `sprintf` (returns a string).
*Formatted Input (`Scanf`)*: The `Scanf` module parses input based on format strings.
- **Scanning Actions**: Plain characters match literals, while a space in the format string matches **any** amount of whitespace (tabs, newlines, etc.).
## 10.5 Lecture Connections and Analogies
This material relates strongly to **Lecture 10** (Sequencing) and **Lecture 13** (Streams).
- **The Semicolon (;) Operator**: The professor notes that the semicolon is one of the few places in OCaml where things **must happen in order**. It evaluates the left side, discards the result, and then evaluates the right side. This is essential for I/O "Side Effects"—like printing multiple strings in a specific order.
- **I/O Streams vs. [[What a generator is|Applicative Streams]]**: In Lecture 13, the professor clarifies that "I/O Streams" are interfaces to hardware (Chapter 10), while "Applicative Streams" are data structures containing a `next` function to simulate an infinite series.
- **The Dispatcher Loop**: I/O is often implemented with a `while true` loop that processes data until a "Dispatcher" (the exception handler) catches an `End_of_file` to stop the program.
## 10.6 Code Example: The `unique` Program
_Relating Chapter 10 (input_line, stdout) to Lecture 11._
The textbook provides a program that prints only unique lines from the input, demonstrating the integration of I/O with **[[OCaml lists|lists]]**.
```ocaml
let rec unique already_read =
  output_string stdout "> ";        (* Ch 10.1: Writing to stdout *)
  flush stdout;                     (* Ch 10.3: Forcing the buffer *)
  let line = input_line stdin in    (* Ch 10.2: Reading from stdin *)
  if not (List.mem line already_read) then begin
    output_string stdout line;
    output_char stdout '\n';        (* Ch 10.2: Writing char *)
    unique (line :: already_read)   (* Recursion with updated list *)
  end 
  else unique already_read;;

(* Main Execution *)
try unique [] with 
| End_of_file -> ();;               (* Ch 10.2: Handling EOF exception *)
```
Line-by-Line Explanation:
1. **output_string stdout "> "**: Sends a prompt string to the standard output channel.
2. **flush stdout**: Because I/O is **buffered**, the prompt might not appear immediately without this call.
3. **input_line stdin**: Reads the user input until a newline is hit. If the user hits Ctrl-D (Unix), it raises `End_of_file`.
4. **if not (List.mem ...)**: Uses standard list functions to check for duplicates.
5. **output_char stdout '\n'**: Manually adds a newline to the output since `input_line` discards it.
6. **try ... with End_of_file -> ()**: This is the standard "loop break" pattern. It stops the infinite recursion gracefully when the input stream ends.
## Midterm Check
1. **The Semicolon**: In an applicative language, argument evaluation order is usually flexible. Why is the **[[OCaml semicolon|semicolon (;)]]** different?.
2. **Type Safety**: Why is using `input_value` considered **unsafe** compared to using the `Printf` or `Scanf` modules?.
3. **Streams**: Explain the difference between an `in_channel` and an "Applicative Stream" (from Lecture 13).