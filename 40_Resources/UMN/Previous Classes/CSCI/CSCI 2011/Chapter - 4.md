---
type: class
status: archived
created: 2025-10-23
updated: 2025-10-30
area:
  - "[[Main Examples]]"
  - "[[Material]]"
  - "[[Finals]]"
tags:
  - "#class"
  - "#Homework"
  - "#Textbook"
  - "#Discussion"
next: "[[50_Archive/Previous Classes/CSCI/CSCI 2011/Chapter - 5]]"
---
# #Textbook Textbook & Videos
## 4.1
### The Divides Notation
**Definition**: $a|b$ (read as "a divides b") means there exists a positive integer c such that $a × c = b$
**Example**: Does 3 divide 15?
	- We need: 3 × c = 15. Solving: c = 5 (which is a positive integer)
	- Therefore: 3|15 is TRUE ✓  
- **Counter-example**: Does 3 divide 22?
	- We need: 3 × c = 22. Solving: c = 22/3 = 7.33... (NOT a positive integer)
	- Therefore: $3∤22$ is FALSE ✗
*Three Key Properties of Divisibility (with Proofs!)*:
1. **Property 1:** If $a|b$ and $a|c$, then $a|(b+c)$
	**Example**: If 3|15 and 3|6, then 3|(15+6) = 3|21 ✓  
	- **Proof Steps**:
		- Since $a|b$, we know $b = a×s$ for some integer s
		- Since $a|c$, we know $c = a×t$ for some integer t
		- Therefore: $b + c = (a×s) + (a×t) = a×(s+t)$
		- Since $(s+t)$ is an integer, $a|(b+c)$ ✓
2. **Property 2:** If $a|b$, then $a|(b×c)$ for any integer c
	**Example**: If 3|15, then 3|(15×2) = 3|30 ✓  
	- **Proof Steps**:
		- Since $a|b$, we know $b = a×t$ for some integer t
		- Therefore: $b×c = (a×t)×c = a×(t×c)$
		- Since $(t×c)$ is an integer, $a|(b×c)$ ✓
3. **Property 3:** If $a|b$ and $b|c$, then $a|c$ (Transitive Property)
	**Example**: If 3|6 and 6|18, then 3|18 ✓  
	- **Proof Steps**:
		- Since $a|b$, we know $b = a×t$ for some integer t
		- Since $b|c$, we know $c = b×s$ for some integer s
		- By substitution: $c = (a×t)×s = a×(t×s)$
		- Since $(t×s)$ is an integer, $a|c$ ✓
### The Division Algorithm
**The Big Formula:** $$a = d×q + r$$**a** = the number being divided   
**d** = divisor (what you're dividing by)  
**q** = quotient (the answer)
**r** = remainder (what's left over)  
- **CRUCIAL RULE**: 0 ≤ r < d (remainder must be less than divisor!)
- [[Main Examples#Division Algorithm|Division Algorithm Examples]]
1. *Example(to note)*: Negative numbers (-112 ÷ 10)
	- **Wrong way**: -112 = 10×(-11) + (-2) ❌ (remainder can't be negative!)  
	- **Right way**: -112 = 10×(-12) + 8 ✓  
	- Check: 10×(-12) = -120, and -120 + 8 = -112 ✓  
	- **Quotient**: q = -112 ÷ 10 = -12  
	- **Remainder**: r = -112 mod 10 = 8
### Modular Arithmetic
**Think of it like a clock!** Just like a clock resets after 12 hours, modular arithmetic "wraps around" after reaching a certain number. 
**It's all about remainders** - when you divide a number, what's left over?  
**Example with mod 4**: The only possible remainders are 0, 1, 2, or 3
- If you get remainder 4, that's really the same as remainder 0
- Numbers follow the pattern: ...0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3...
- **a ≡ b (mod m)** means "a is congruent to b modulo m"  
- **This happens when**: m divides (a - b) evenly  
- **In simple terms**: Two numbers are congruent mod m if they have the same remainder when divided by m.
#### Testing Congruence - Two Methods
1. **Method 1: Check if remainders are equal**:
	- **Example**: Is 2 ≡ 6 (mod 4)?
		- 2 ÷ 4 = remainder 2
		- 6 ÷ 4 = remainder 2
		- Same remainders = YES, they're congruent!
2. **Method 2: Check if the difference is divisible**
	- **Same example**: Does 4 divide (6 - 2)?
		- 6 - 2 = 4
		- 4 ÷ 4 = 1 (no remainder)
		- YES, so 2 ≡ 6 (mod 4)
	- Counter-Example
		- **Question**: Is 24 ≡ 14 (mod 6)?  
		- **Check**: Does 6 divide (24 - 14)?
		- 24 - 14 = 10
		- 10 ÷ 6 = 1 remainder 4 (not evenly divisible)
		- NO, they're not congruent!
3. **Key Theorem: The Remainder Rule: **a ≡ b (mod m)** if and only if **a mod m = b mod m**. 
	This just confirms what we already know - if remainders are equal, numbers are congruent!
4. **Theorem**: a ≡ b (mod m) if and only if a = b + km for some integer k. 
	- **Proof Direction 1** (congruent → equation):  
		- Start: a ≡ b (mod m)  
		- This means: m divides (a - b)  
		- So: a - b = km for some integer k  
		- Add b to both sides: a = b + km ✓
	- **Proof Direction 2** (equation → congruent):  
		- Start: a = b + km  
		- Subtract b: a - b = km  
		- This means m divides (a - b)  
		- So: a ≡ b (mod m) ✓
#### Super Important Arithmetic Rules
**If a ≡ b (mod m) and c ≡ d (mod m), then:**  
- **Addition**: a + c ≡ b + d (mod m)  
- **Multiplication**: ac ≡ bd (mod m)
1. **Proof for Addition:**
	- We know: a = b + km and c = d + lm  
	- So: a + c = (b + km) + (d + lm) = b + d + m(k + l)  
	- This means: (a + c) - (b + d) = m(k + l)  
	- Therefore: m divides the difference, so a + c ≡ b + d (mod m) ✓
2. **Proof for Multiplication:**
	- We know: a = b + km and c = d + lm  
	- So: ac = (b + km)(d + lm) = bd + blm + kdm + klm²  
	- Rearranging: ac = bd + m(bl + kd + klm)  
	- This means: ac - bd = m(bl + kd + klm)  
	- Therefore: m divides the difference, so ac ≡ bd (mod m) ✓
- [[Main Examples#Arithmetic Rules|Arithmetic Rules Examples]]
- Special Notation to Watch For: 
	- **+ₘ** means "addition mod m"  
	- **×ₘ** means "multiplication mod m"  
		- **Example**: 4 +₃ 5 = 9 ≡ 0 (mod 3)  
		- **Example**: 4 ×₃ 5 = 20 ≡ 2 (mod 3)
## 4.2
### Number Base Conversions: From Different Bases to Decimal
**Expansion Formula**: Any positive integer can be written as: $a_k × B^k + a_{(k-1)} × B^(k - 1) + ... + a_1 × B^1 + a_0 × B^0$
**B = the base** (2 for binary, 8 for octal, 10 for decimal, 16 for hexadecimal)  
**The coefficients (a_k, a_(k-1), etc.)** are the digits in that base system
1. *Decimal Expansion (Base 10)* - Just for Practice
	- **Example**: 10,456 in decimal expansion form  
		- **Place values**: 10^4 (ten thousands), 10^3 (thousands), 10^2 (hundreds), 10^1 (tens), 10^0 (ones)  
		- **Written as**: 1×10^4 + 0×10^3 + 4×10^2 + 5×10^1 + 6×10^0  
	- **Note**: We don't usually write decimal numbers this way since we're already used to base 10!
2. *Binary to Decimal (Base 2 to Base 10)*:
	- **Binary uses only**: 0s and 1s (because base 2 = remainders can only be 0 or 1)  
	- **Example**: 10111101₂ (the subscript 2 means base 2)
		**Step-by-step conversion**:  
		- **Label positions from right to left**: 0, 1, 2, 3, 4, 5, 6, 7 (these become exponents) 
		- **Write expansion**: 1×2^7 + 0×2^6 + 1×2^5 + 1×2^4 + 1×2^3 + 1×2^2 + 0×2^1 + 1×2^0  
		- **Calculate powers of 2**: 2^7=128, 2^5=32, 2^4=16, 2^3=8, 2^2=4, 2^0=1  
		- **Skip the zeros** (they don't contribute to the sum)  
		- **Add them up**: 128 + 32 + 16 + 8 + 4 + 1 = 189  
		- **Final answer**: 189₁₀ (or just 189 since decimal is our default)
3. *Octal to Decimal (Base 8 to Base 10)*:
	- **Octal uses digits**: 0, 1, 2, 3, 4, 5, 6, 7  
	- **Example**: 4072₈
		**Step-by-step conversion**:  
		- **Label positions from right to left**: 0, 1, 2, 3  
		- **Write expansion**: 4×8^3 + 0×8^2 + 7×8^1 + 2×8^0  
		- **Calculate**: 4×512 + 0×64 + 7×8 + 2×1  
		- **Simplify**: 2048 + 0 + 56 + 2 = 2106  
		- **Final answer**: 2106
4. *Hexadecimal to Decimal (Base 16 to Base 10)*:
	- **Hexadecimal uses**: 0-9 and A-F  
	- **Special hex digits**: A=10, B=11, C=12, D=13, E=14, F=15  
	- **Why letters?** We need single digits for values 10-15, so we use A-F  
	- **Example**: 2AE0B₁₆
		**Step-by-step conversion**:  
		- **Label positions from right to left**: 0, 1, 2, 3, 4  
		- **Translate letters to numbers**: A=10, E=14, B=11  
		- **Write expansion**: 2×16^4 + 10×16^3 + 14×16^2 + 0×16^1 + 11×16^0  
		- **Calculate**: 2×65536 + 10×4096 + 14×256 + 0×16 + 11×1  
		- **Add up**: 131072 + 40960 + 3584 + 0 + 11 = 175,627  
		- **Final answer**: 175,627
5. *Key Memory Tips*: **Start from the RIGHT** and work left when labeling positions  
	- **Position numbers become exponents** of your base.
### Number Base Conversions: From Decimal to Different Bases
**Main idea**: Use the division algorithm to convert from decimal (base 10) to any other base  
**Formula**: Any number = (divisor × quotient) + remainder  
**Key rule**: Keep dividing until your quotient becomes 0 (not just when remainder is 0!)  
**Reading the answer**: Take all remainders and read them from bottom to top
1. *Converting Decimal to Octal (Base 8)*:
	- **Example: Convert 12,543 to octal**
		**Step-by-step process:** Start with 12,543 ÷ 8 = 1,567 remainder 7  
		- Take quotient 1,567 ÷ 8 = 195 remainder 7  
		- Take quotient 195 ÷ 8 = 24 remainder 3  
		- Take quotient 24 ÷ 8 = 3 remainder 0  
		- Take quotient 3 ÷ 8 = 0 remainder 3 ← **Stop here because quotient is 0**
	- **Reading the answer:** Take remainders from bottom to top: 3, 0, 3, 7, 7 
	- **Final answer: 30377₈**
	**What this actually means:** 3×8⁴ + 0×8³ + 3×8² + 7×8¹ + 7×8⁰ = 12,543
2.  *Converting Decimal to Hexadecimal (Base 16)*: **Remember the hex letters:**  A = 10, B = 11, C = 12, D = 13, E = 14, F = 15
	- **Example: Convert 19,472 to hexadecimal** 
		- **Step-by-step process:** 19,472 ÷ 16 = 1,217 remainder 0  
		- 1,217 ÷ 16 = 76 remainder 1  76 ÷ 16 = 4 remainder 12 (which is C in hex) 
		- 4 ÷ 16 = 0 remainder 4
	**Reading the answer:**  Take remainders from bottom to top: 4, 12, 1, 0. Convert 12 to C: 4, C, 1, 0.
	- **Final answer: 4C10₁₆**
3. *Converting Decimal to Binary (Base 2)*
	- **Example: Convert 141 to binary**
		**Step-by-step process:** 141 ÷ 2 = 70 remainder 1  
		- 70 ÷ 2 = 35 remainder 0  
		- 35 ÷ 2 = 17 remainder 1  
		- 17 ÷ 2 = 8 remainder 1  
		- 8 ÷ 2 = 4 remainder 0  
		- 4 ÷ 2 = 2 remainder 0  
		- 2 ÷ 2 = 1 remainder 0  
		- 1 ÷ 2 = 0 remainder 1
	**Reading the answer:** Take remainders from bottom to top: 1, 0, 0, 0, 1, 1, 0, 1  
	**Final answer: 10001101₂**
- **Binary formatting tip:**  Group binary digits in sets of 4 for easier reading. 
	- 10001101₂ can be written as 1000 1101₂
- **Critical rules to remember:** **Never stop when remainder = 0** - only stop when **quotient = 0**. Always read remainders from **bottom to top**. In binary, remainders can only be 0 or 1 (if you get anything else, you made an error).
### Converting Between Number Bases and Base Operations
1. *Converting Binary to Octal and Hexadecimal*: 
	- **The Key Insight:** Octal is base 8 = 2³, so group binary digits in **groups of 3**  
		- Hexadecimal is base 16 = 2⁴, so group binary digits in **groups of 4**
	- **Binary to Octal Process:** Start from the RIGHT side of your binary number. 
		- Group digits into sets of 3 (add zeros on the left if needed)  
		- For each group of 3, calculate: (4×first digit) + (2×second digit) + (1×third digit)  
		- Example: 1111011₂
			- Group: 001|111|011
			- 001 = 0×4 + 0×2 + 1×1 = 1
			- 111 = 1×4 + 1×2 + 1×1 = 7
			- 011 = 0×4 + 1×2 + 1×1 = 3
			- Result: 173₈
	- **Binary to Hexadecimal Process:** Start from the RIGHT side of your binary number. 
		- Group digits into sets of 4 (add zeros on the left if needed). 
		- For each group of 4, calculate: (8×first) + (4×second) + (2×third) + (1×fourth) 
		- Remember: 10=A, 11=B, 12=C, 13=D, 14=E, 15=F  
		- Example: 1111011₂
			- Group: 0011|1011
			- 0011 = 0×8 + 0×4 + 1×2 + 1×1 = 3
			- 1011 = 1×8 + 0×4 + 1×2 + 1×1 = 11 = B
			- Result: 3B₁₆
2. *Converting Octal to Binary and Hexadecimal*: 
	- **Octal to Binary Process:** Each octal digit converts to exactly 3 binary digits. 
		- Convert each octal digit separately using place values (4, 2, 1). 
		- Example: 372₈
			- 3 = 011₂ (0×4 + 1×2 + 1×1)
			- 7 = 111₂ (1×4 + 1×2 + 1×1)
			- 2 = 010₂ (0×4 + 1×2 + 0×1)
			- Result: 011111010₂
	- **Octal to Hexadecimal Process:** First convert octal to binary (as above). 
		- Then convert binary to hexadecimal (group by 4s from right). 
		- This is a two-step process - you MUST go through binary!
3. *Converting Hexadecimal to Binary and Octal*:
	- **Hexadecimal to Binary Process:** Each hex digit converts to exactly 4 binary digits. Convert each hex digit separately using place values (8, 4, 2, 1). Remember: A=10, B=11, C=12, D=13, E=14, F=15. 
		- Example: A8D₁₆
			- A(10) = 1010₂ (1×8 + 0×4 + 1×2 + 0×1)
			- 8 = 1000₂ (1×8 + 0×4 + 0×2 + 0×1)
			- D(13) = 1101₂ (1×8 + 1×4 + 0×2 + 1×1)
			- Result: 101010001101₂
	- **Hexadecimal to Octal Process:** First convert hex to binary (as above). 
		- Then convert binary to octal (group by 3s from right). 
		- Again, this requires going through binary as an intermediate step!
4. *Operations in Different Bases*:
	- **Addition in Any Base:** Add column by column from right to left. 
		- When sum ≥ base number, subtract the base and carry 1. 
		- Example in binary: 1 + 1 = 2, but 2 = 10₂, so write 0 and carry 1  
		- Example: 101₂ + 111₂
			- Rightmost: 1+1=2=10₂ → write 0, carry 1
			- Middle: 0+1+1(carry)=2=10₂ → write 0, carry 1
			- Leftmost: 1+1+1(carry)=3=11₂ → write 11
			- Result: 1100₂
	- **Multiplication in Any Base:** Use traditional long multiplication method. 
		- Multiply each digit of bottom number by entire top number. 
		- Shift positions appropriately (add zeros for place value).
		- Add all partial products together. Remember to convert any results ≥ base back to proper base format.
### Integer Operations Algorithms
#### Base B Expansion Algorithm
**What it does**: Converts a number from base 10 to any other base (like binary)  
**Example**: Converting 101 (base 10) to base 2  
**The process**:
- Start with your number (N = 101) and the base you want (B = 2)
- Keep dividing by the base and collecting remainders
- 101 ÷ 2 = 50 remainder 1
- 50 ÷ 2 = 25 remainder 0
- 25 ÷ 2 = 12 remainder 1
- 12 ÷ 2 = 6 remainder 0
- 6 ÷ 2 = 3 remainder 0
- 3 ÷ 2 = 1 remainder 1
- 1 ÷ 2 = 0 remainder 1  
	- **Stop when quotient = 0**  
	- **Read remainders backwards**: 1100101 (base 2)  
	- **Key insight**: The algorithm just formalizes what we already know how to do!
#### Binary Addition Algorithm
**What it does**: Adds two binary numbers step by step  
**Example**: 1011 + 1110  
**The process**:
- Start from rightmost bits
- Add each pair of bits plus any carry from previous step
- If sum = 2, write 0 and carry 1
- If sum = 3, write 1 and carry 1 
	- **Step by step for our example**:
- 1 + 0 = 1 (no carry)
- 1 + 1 = 2 → write 0, carry 1
- 0 + 1 + 1(carry) = 2 → write 0, carry 1
- 1 + 1 + 1(carry) = 3 → write 1, carry 1
- Final carry becomes leftmost digit  
	- **Answer**: 11001  
	- **Pro tip**: This is exactly like regular addition, but remember 2 = 10 in binary!
#### Binary Multiplication Algorithm
**What it does**: Multiplies two binary numbers using the traditional method  
**Example**: 101 × 110  
**The process**:
- Multiply first number by each digit of second number
- Shift results left for each position (add zeros as placeholders)
- Add all partial products together  
	- **Step by step**:
- 101 × 0 = 000
- 101 × 1 = 101 (shifted left once) = 1010
- 101 × 1 = 101 (shifted left twice) = 10100
- Add: 000 + 1010 + 10100 = 11110  
	- **Algorithm version**: Same idea but written as a×(rightmost bit)×2⁰ + a×(next bit)×2¹ + etc.  
- **Key point**: It's the same multiplication you learned in elementary school!
#### Division Algorithm (Pseudocode Only)
**What it does**: Finds quotient and remainder when dividing integers  
**Process**:
- Start with quotient = 0, remainder = |a| (absolute value)
- While remainder ≥ divisor: subtract divisor from remainder, add 1 to quotient
- Handle negative numbers specially to keep remainder positive  
	- **Returns**: Both quotient and remainder  
#### Modular Exponentiation Algorithm ⭐
**What it does**: Calculates $B^N mod (M)$ efficiently for huge numbers  
**Why it matters**: Essential for cryptography and computer security!  
**Key insight**: Convert the exponent to binary, then use properties of exponents
- *Example:* 3^6 mod 5
	- **Step 1**: Convert exponent to binary.
		- 6 in binary = 110 (which is 4 + 2 + 0).
	- **Step 2**: Use the algorithm.
		- Start: X = 1, power = 3 mod 5 = 3.
		- Binary digit 0 (rightmost): X stays 1, power = 3² mod 5 = 9 mod 5 = 4
		- Binary digit 1: X = 1 × 4 mod 5 = 4, power = 4² mod 5 = 16 mod 5 = 1
		- Binary digit 1: X = 4 × 1 mod 5 = 4, power = 1² mod 5 = 1  
		- **Answer**: 4  
	- **Verification**: 3^6 = 729, and 729 mod 5 = 4 ✓
- *The Binary Trick Explained*: **Any exponent can be written in binary**: 6 = 4 + 2 = 2² + 2¹. 
	- **So**: 3^6 = 3^(4+2) = 3^4 × 3^2  
	- **The algorithm**: Builds up the answer by squaring and multiplying only when needed. **Efficiency**: Instead of 6 multiplications, we only need 3!
- Why This Algorithm is Genius:
	- **Without it**: You'd have to calculate 3^6 = 729, then find 729 mod 5  
	- **With it**: You never deal with huge numbers - everything stays manageable!  
	- **For cryptography**: Imagine calculating something like 7^1000000 mod 12345 - impossible without this algorithm!


---

# #Homework Homework 5


---
# #Discussion Discussion 5


---
