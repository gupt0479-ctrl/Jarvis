---
type: class
status: archived
created: 2025-10-17
updated: 2025-12-20
area:
  - "[[C Language]]"
  - "[[50_Archive/Previous Classes/CSCI/CSCI 2021/Midterm - 1|Midterm - 1]]"
tags:
  - "#class"
  - "#Textbook"
  - "#CSAPP"
  - "#Lecture"
  - "#Lab"
  - "#Homework"
next: "[[50_Archive/Previous Classes/CSCI/CSCI 2021/Week - 6|Week - 6]]"
---
# #Textbook Textbook (CSAPP - 2.1 - 2.4)
## #CSAPP CSAPP
### 2.1 to 2.3 [[50_Archive/Previous Classes/CSCI/CSCI 2021/Week - 3|Week - 3]]
### 2.4
• **Fractional Binary Numbers:** These extend binary to include fractions, with bits to the right of a "binary point" having weights of 1/2, 1/4, 1/8, and so on. However, just as `1/3` cannot be represented exactly in decimal, numbers like `0.2` cannot be represented exactly in binary.
• **IEEE 754 Floating-Point Standard:** This is the universal standard for representing floating-point numbers. A number is represented as `V = (-1)^s * M * 2^E`.
    ◦ **Sign (s)**: 1 bit determines if the number is positive or negative.
    ◦ **Exponent (E)**: This field determines the scale (the `2^E` part). It is stored in a _biased_ form, meaning an offset is subtracted from the field's unsigned value to get `E`.
    ◦ **Significand (M):** This field is the fractional part (the `M` part).
• **Three Cases of Representation:**
    1. **Normalized:** The most common case. The exponent field is not all zeros or all ones. The significand `M` is `1 + f`, where `f` is the value of the fraction field. This "implied leading 1" gives an extra bit of precision for free.
    2. **Denormalized:** The exponent field is all zeros. This represents numbers very close to zero and allows for _gradual underflow_. In this case, the significand `M` is just `f` (no implied leading 1). The value `0.0` is a special denormalized number with all bits zero.
    3. **Special Values:** The exponent field is all ones. If the fraction field is all zeros, it represents **infinity** (`+∞` or `-∞`), used for overflows. If the fraction field is non-zero, it represents **Not a Number (NaN)**, used for results like `sqrt(-1)` or `∞ - ∞`.
• **Rounding:** Since floating-point numbers have limited precision, results of operations must be rounded. The default mode is **round-to-even** (or round-to-nearest), which rounds to the nearest value, but rounds a number halfway between two possibilities to the one with an even least significant digit. This avoids statistical bias.
• **Floating-Point Operations:** Unlike integer arithmetic, floating-point addition and multiplication are **not associative**. For example, `(3.14 + 1e20) - 1e20` might evaluate to `0.0`, while `3.14 + (1e20 - 1e20)` evaluates to `3.14`. This is a major difference and something programmers need to be aware of!

---

# #Lecture Lectures
## Lecture 9
### Unicode & UTF-8
- ASCII (128–256 chars) not enough for global languages.
- **Unicode**: assigns a unique number (code point) to ~159,000+ symbols.
- Multiple encodings exist: UTF-16, UTF-32, etc.
- **UTF-8** = most common:
    - 1–4 bytes per character.
    - ASCII compatible (0–127 identical).
    - Efficient for English, flexible for all languages.
### Bitwise Operations in C
Operate directly on bits: in brackets i have written binary conversions from decimal.
- `|` → OR (**1 if either bit is 1**)
- `&` → AND (1 only if both bits are 1)
- `^` → XOR (exclusive OR) - (1 if exactly one bit is 1 (different), 0 if same)
- `~` → NOT (invert all bits) - (Flips every bit: `1 → 0`, `0 → 1`.)
- `<<` → shift left (multiply by power of 2) - Shifts all bits left, fills new bits on the right with 0. Effect: multiply by 2 for each shift. For **12 (`1100`)**:
```c
x = 1100 (12)  
x << 1 = 11000 (24)  
x << 2 = 110000 (48)
```
- `>>` → shift right (divide by power of 2 for unsigned) - Shifts all bits right, discards the rightmost bits. Effect: divide by 2 for each shift (integer division). Behavior for negatives depends on compiler (arithmetic vs logical shift).
 ```c
 x = 1100 (12)  
 x >> 1 = 0110 (6)  
 x >> 2 = 0011 (3)
 ```
- **Binary addition**: Same algorithm as decimal addition, but base 2. 
	- Overflow: Adding two values may require more bits than available. Extra bits are discarded silently. Hardware discards carry → incorrect value. 
- **Binary subtraction**: Subtraction can borrow past available bits. If we need an extra carry then, pretend there’s an extra significant digit for us to borrow from. Becomes maximum value representable when there is **underflow**. 
### Two's-Complement Encodings
We need a way to represent **negative integers** in binary. **8-bit: −128 to +127.**
Options historically: [[50_Archive/Previous Classes/CSCI/CSCI 2021/Week - 3#Two's-Complement Encodings|Two's]]
1. **Sign-and-Magnitude**: leftmost bit = sign (0 = positive, 1 = negative).
    - Problem: two versions of 0 (`+0` and `-0`).
**Negative number → positive number and vice versa is same. Rule: invert bits, add 1.**
2. Overflow in Two’s Complement: Overflow happens if the result is too large for the bit width. Example (8-bit):
```c
0111 1111 (127) + 0000 0001 (1) = 1000 0000 (-128)
```
→ Overflows from max positive to min negative.
## Lecture - 10
Integer Operations and Speed, Cost measured in **CPU cycles**. 
- Typical cycle counts:
    - Addition: 1
    - Subtraction: 1
    - Multiplication: ~3
    - Division: >30 (very slow)
- Multiplication/division mimic base-10 methods but slower in hardware.
- Compilers often replace division/multiplication with bit-shifts when possible.
### Undefined Behavior in C
- Once overflow happens in signed arithmetic → **undefined behavior**.w Compiler may optimize differently:
    - `gcc` assumes no overflow → may generate surprising code.
    - `clang` handles overflow explicitly but slower.
- Rule: Never rely on signed overflow behavior in portable C.
- Detecting a Sign Change  
```c
if (i > 0 && (i+1) < 0) {  
...  
}  
```
gcc produces assembly that does roughly:  
1. Check if i > 0 
2. Check if i < -1
Ranges of data types: `char, 8 bits, Signed - yes, -128 to 127. unsigned char	8 bits, Signed - No, 0 to 255`
### Bit shifting
shift bits by right: - Shifting signed negatives can cause surprises.
Example: Sign flipped!
```c
0x1101 0010 (-46) 
>> 3 → 0x0001 1010 = +26 (logical shift)
```
- **Arithmetic shift** preserves sign:
`0x1101 0010 >> 3 = 0x1111 1010 = -6`
- Unsigned → logical shift (fills with 0).
- Signed → arithmetic shift (fills with MSB).
- Strictly speaking: right shift of signed type with negative value is “implementation defined” but most compilers do the above.
1. With n Bits: We Can Represent 2n Things.
	- Unsigned Integer Value - Ranges from 0 to 2n-1. Good for representing memory addresses.
	- Alternative: Two’s Complement for Signed Integer - Ranges from -2n-1 to 2n-1 – 1
2. **Endianness** is the rule a CPU uses to lay out the **bytes** of a multi-byte value (like `int`, `long`, `float`, `double`) in memory. it does **not** change the numeric value; it only changes how the bytes are ordered in RAM.
	- **big-endian**: the **most significant byte** (MSB) is stored at the **lowest** memory address.  
    think: left-to-right (big end first).
	- **little-endian**: the **least significant byte** (LSB) is stored at the **lowest** memory address.  
    think: right-to-left (little end first).
```c
void print_bytes(void *data, size_t len) {
    uint8_t *p = (uint8_t *) data;
    for (int i = 0; i < len; i++) {
        printf("%x\t", *p);
        p++;
    }
    printf("\n");
}

int main(void) {
    int x = 0x000758EC;        // hex literal (same numeric value everywhere)
    printf("%x\n", x);         // prints the value in hex (no leading zeros)
    print_bytes(&x, sizeof(x)); // dump the raw bytes in memory order
    return 0;
}
```
for `x = 0x000758EC`, the four bytes are `00 07 58 EC`.
- on a **little-endian** machine (x86/x86-64, most ARM configs), `print_bytes` prints:
    `ec    58    07    0`
    (lowest address holds LSB `EC`)
- on a **big-endian** machine, you’d see:
    `0     7     58    ec`
    (lowest address holds MSB `00`
## Lecture 11
### Representing Fractions
We also need to represent real numbers like 1.5, 3.14, 2.71828, or very large/small values.
1. Decimal Example:`2021.125` =`2×10³ + 0×10² + 2×10¹ + 1×10⁰ + 1×10⁻¹ + 2×10⁻² + 5×10⁻³`
2. Binary Example: Binary point works like decimal point:
`1011.101` = `1×2³ + 0×2² + 1×2¹ + 1×2⁰ + 1×2⁻¹ + 0×2⁻² + 1×2⁻³ = 11.625`
### Fixed Point vs Floating Point
- **Fixed point**: fixed number of bits before and after binary point.
    - Range and precision limited by split.
- **Floating point**: binary point “floats” using scientific notation.
    - Provides wide range and adjustable precision.
#### Scientific Notation
- Decimal: `6.02 × 10²³` 
    - Mantissa: 6.02
    - Exponent: 23
    - Base: 10
- Binary: `1.01 × 2²³`
    - Mantissa: 1.01
    - Exponent: 23
    - Base: 2
Conversion Example: Convert `-248.75` to binary scientific notation:
1. Break down in binary:  
    `-248.75 = -(128 + 64 + 32 + 16 + 8 + 0.5 + 0.25)` = `-11111000.11₂`
#### Bias Representation
- Interpret value as `unsigned_value + bias`.
- Example: Bias = -127.
    - `00000000` = -127
    - `11111111` = 128
- Pro: flexible ranges.
- Con: arithmetic is awkward (need to subtract bias on add).
#### Normalized Values (Type 1/3)
- Exponent stored in **biased form** (not two’s complement).
	- Float bias = -127, Double bias = -1023.
	- Example: Exponent bits `10000110` = 134. 
    - True exponent = 134 - 127 = 7.
- **Normalization digit** rule: mantissa always begins with `1.` → not stored explicitly.
- Example: -248.75 in IEEE 754
	- Sign = 1 (negative)
	- Exponent = `10000110` = 134 → 134 - 127 = 7
	- Mantissa = `111100011`
So: `-1.111100011 × 2⁷ = -248.75`
#### Denormalized Values (Type 2/3)
 - Exponent bits all 0.
 - No implied leading 1 in mantissa.
- Allows representing numbers smaller than 2⁻¹²⁶.
#### Special Values (Type 3/3)
- Exponent bits all 1:
- Mantissa all 0 → ±Infinity.
- Mantissa non-zero → NaN (Not a Number).         
#### Zero
- Exponent = 0, Mantissa = 0.    
- Two versions: +0.0 and -0.0.     
#### Smallest Possible Number
- Denormalized form: exponent fixed at -126, smallest mantissa = `0...01`.
- Value = `1 × 2⁻²³ × 2⁻¹²⁶ = 2⁻¹⁴⁹ ≈ 1.4 × 10⁻⁴⁵`.
#### Zero in Floating Point
- Represented with exponent = 0, mantissa = 0.
- Both +0.0 and -0.0 exist.
- Needed for limits: approaching 0 from positive vs negative side.
#### Infinity and NaN
- **+∞ / -∞**: exponent = all 1’s, mantissa = 0, sign determines positive/negative.
    - Example: `1.0 / 0.0 = +∞`.
- **NaN (Not a Number)**: exponent = all 1’s, mantissa ≠ 0
    - Examples: `0.0 / 0.0`, `sqrt(-4)`.
    - NaN contaminates all operations: `NaN + 5 = NaN`.
    - Multiple bit patterns can represent NaN (quiet vs signaling NaN).

---

# #Lab Lab - 4 
## `masking.c`
`masking.c`: what every block is doing (and why it works). [[#Bitwise Operations in C]]
1. Helper: `print_intbits(num)`: 
	- This function prints a 32-bit view of `num` (grouped by 4 bits) and labels bit positions. It uses: `bits[idx] = num & (1 << (31 - i)) ? '1' : '0';`
	- Meaning: “check whether bit (31-i) is set.” If yes, print `'1'` else `'0'`. So every time you do something to `x`, the next print shows you exactly what bits changed.
2. *“set 19th bit as well”*: `x = x | (1 << 19);`
	This is **set bit k** pattern: `x |= (1 << k)` sets bit `k` to 1, leaving all other bits unchanged.
	Why it works: [[#Bit shifting]]
	- `(1<<19)` has a 1 only at bit 19 and 0 elsewhere.
	- OR has the identity behavior: `0|x = x`, `1|x = 1` (slides explicitly emphasize this).
3. *“clear the 8th bit”*: `x = x & ~(1 << 8);`
	This is the **clear bit k** pattern: `x &= ~(1 << k)` forces bit `k` to 0, leaving other bits unchanged.
	Why it works:
	- `(1<<8)` is mask with a 1 only at bit 8
	- `~(1<<8)` turns it into all 1s except bit 8 becomes 0.
	- AND has: `1 & x = x`, `0 & x = 0`. Slides say AND is used to “set some bits to 0 and leave others unchanged.”
4. *“clear all bits via xor”*: `x = x ^ x;`
	- XOR property: `a ^ a = 0`.  
	- So any number XOR itself becomes zero (all bits cancel). This is a classic bit trick that shows up in puzzles.
5. *“place the pattern 110101 starting at bit 8”*: `x = x | (0b110101 << 8);`
	This is **inject a pattern**:`(pattern << start)` moves the pattern into the desired bit positions. [[#Bit shifting]]
	- OR merges it into `x` (sets those bits to match the pattern, assuming x was 0 there)
	Important nuance:
	- OR can only **force bits to 1**; it can’t force a bit to 0 if x already had 1 there.
	- In the quiz they say “if x is cleared” to avoid that complication.
6. *About Project 2:*
```c
int is_even(int n) {
    return !(n & 1);
}
```
What it means at the bit level ([[#Two's-Complement Encodings]])
- The least significant bit (bit 0) tells you if a number is odd/even:
	- even → LSB = 0
	- odd → LSB = 1
- `(n & 1)` isolates bit 0:
	- if bit 0 is 1 → result is 1 (odd)
	- if bit 0 is 0 → result is 0 (even)
- `!` converts “truthy” to `0` and `0` to `1`:
	- even: `(n&1)=0` → `!0 = 1`
	- odd: `(n&1)=1` → `!1 = 0`

---

# #Homework Homework - 4
## Problem 1
[[50_Archive/Previous Classes/CSCI/CSCI 2021/Week - 3#Lecture 8|Conversions]]
1. **Fill the table**: Key moves:
	- **Hex ↔ Binary:** 1 hex digit = 4 bits.
	- **Oct ↔ Binary:** 1 oct digit = 3 bits.
	- **ASCII chars:** `0x20` is SPACE, `0x41` is `A`, `0x61` is `a`, etc.    

| Dec | Hex  | Oct | Binary    | Char           |
| --- | ---- | --- | --------- | -------------- |
| 9   | 0x09 | 11  | 0000 1001 | TAB            |
| 10  | 0x0A | 12  | 0000 1010 | `\n` (newline) |
| 32  | 0x20 | 40  | 0010 0000 | SPACE          |
| 50  | 0x32 | 62  | 0011 0010 | `2`            |
| 65  | 0x41 | 101 | 0100 0001 | A              |
| 66  | 0x42 | 102 | 0100 0010 | B              |
| 79  | 0x4F | 117 | 0100 1111 | O              |
| 80  | 0x50 | 120 | 0101 0000 | P              |
| 91  | 0x5B | 133 | 0101 1011 | [              |
| 97  | 0x61 | 141 | 0110 0001 | a              |
| 122 | 0x7A | 172 | 0111 1010 | z              |
| 145 | 0x91 | 221 | 1001 0001 | none           |
| 160 | 0xA0 | 240 | 1010 0000 | none           |
| 180 | 0xB4 | 264 | 1011 0100 | none           |
| 255 | 0xFF | 377 | 1111 1111 | none           |
2. **32-bit unsigned practice**
	1. *NUMBER 1*: Binary is given: `0000 0000 0010 1111 0011 1010 1000 1101`
		Group into hex nibbles:
		- `0000 0000 0010 1111 0011 1010 1000 1101`
		- `00 2F 3A 8D` → **Hex = 002F3A8D**
		Decimal (from 0x2F3A8D):
		-  = 2·16^5 + 15·16^4 + 3·16^3 + 10·16^2 + 8·16 + 13 = **3,095,181**
		- **Hex:** `002F3A8D`
		- **Decimal:** `3095181`
	2. *NUMBER 2*: Hex is given: `7F835A0B`
		Binary: convert each hex digit → 4 bits: 7 = 0111, F = 1111, 8 = 1000, 3 = 0011, 5 = 0101, A = 1010, 0 = 0000, B = 1011
		- So **Binary =** `0111 1111 1000 0011 0101 1010 0000 1011`
		- Decimal: 0x7F835A0B = **2,139,314,699**
## PROBLEM 2: Signed Integer Conversions
1. **Negate 0111 1100 (124) in 8-bit two’s complement**: Given: `0111 1100 = 0x7C = 124`
	- To negate (two’s complement): **Invert bits:**`0111 1100` → `1000 0011`
	- **Add 1:** `1000 0011 + 1` → `1000 0100`
	- So **-124 = `1000 0100` (0x84)**
	- Convert back to positive (same process): 
	- invert `1000 0100` → `0111 1011`
	- add 1 → `0111 1100` (original)
	This matches the demo idea in `twos_complement.c`: `neg = (~num) + 1;`
2. **Complete the 8-bit signed table**: (“Inverse” column = flip bits, **not** “add 1” — just bitwise invert.)

| Dec  | Hex  | Binary    | Inverse   |
| ---- | ---- | --------- | --------- |
| +5   | 0x05 | 0000 0101 | 1111 1010 |
| -5   | 0xFB | 1111 1011 | 0000 0100 |
| +32  | 0x20 | 0010 0000 | 1101 1111 |
| -32  | 0xE0 | 1110 0000 | 0001 1111 |
| +127 | 0x7F | 0111 1111 | 1000 0000 |
| -127 | 0x81 | 1000 0001 | 0111 1110 |
| -128 | 0x80 | 1000 0000 | 0111 1111 |
| +2   | 0x02 | 0000 0010 | 1111 1101 |
| -2   | 0xFE | 1111 1110 | 0000 0001 |
| +1   | 0x01 | 0000 0001 | 1111 1110 |
| -1   | 0xFF | 1111 1111 | 0000 0000 |
| 0    | 0x00 | 0000 0000 | 1111 1111 |
## PROBLEM 3: Converting Strings to Numbers (convert.c)
Look at `convert()` in `convert.c`.
1. **What kind of data is input?** 
	A **C string** (`char *str`) containing digits like `"124"` or `"-212"` (and possibly invalid ones like `"51a3"`).
2. **What result is produced?**
	An **integer value** computed from that string (base-10), stored into `*num`.
3. **How is success vs error reported?**
	- **Success:** returns `0` and sets `*num`
	- **Error:** prints an error message and returns `-1` when it hits an invalid char (or `'-'` not at position 0).
4. **Why is this conversion needed?**
	Because lots of input comes in as **strings** (command-line args, file tokens, user input), but you often need **numeric** types to compute with.
5. **Which built-in C function does this conversion correspond to, and how is calling different?**
	This function is essentially a “manual `atoi`/`strtol`-style” conversion.
	- `atoi(str)` returns the int directly (and is weak on error reporting).
	- `strtol(str, &endptr, 10)` returns the number and gives extra error-checking via `endptr`.
	**Calling convention difference vs `convert(str, &num)`**:
	- `convert()` returns an **error code** and writes the result through an `int *num` output parameter.
	- `atoi/strtol` return the **number as the return value**, not through an out-pointer.
6. **How does switch/case work here?**
	Inside the loop, it does `switch(digit)` and matches one of the `case '0' ... case '9'` blocks to assign `value`. Each case ends with `break` to stop “fall-through.”.
	- Special case:
		- `case '-'`: only allowed at `pos == 0`, which sets `negate = true`. Otherwise it **falls through** into `default` (error).    
	    - Then it updates the running total like:`total = total * 10 + value;`.	At the end, it negates if needed and stores into `*num`.

---
