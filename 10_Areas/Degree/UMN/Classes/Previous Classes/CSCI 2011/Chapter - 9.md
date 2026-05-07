---
type: class
status: archived
created: 2025-11-27
updated: 2025-11-29
area:
  - "[[Main Examples]]"
  - "[[Finals]]"
  - "[[Material]]"
tags:
  - "#class"
  - "#Textbook"
  - "#Homework"
  - "#Discussion"
next: "[[Chapter - 10]]"
---
# #Textbook Textbook & Videos
## 9.1
### Relations and Their Properties
**Basic Definition**: A relation from set A to set B is just a subset of A × B (all possible ordered pairs where first element comes from A, second from B)  
**Key Point**: It doesn't have to include ALL possible pairs - just some of them  
**Example**: If A = {1, 2, 3} and B = {a, b, c}, a relation might be {(1,a), (1,b), (2,b), (2,c), (3,a)} - only 5 out of the 9 possible pairs.
1. *Different Ways to Show Relations*:
	- **Arrow notation**: 1 → a, 1 → b, 2 → b, etc.  
	- **Table with X's**: Put an X where the relation exists (like a grid)  
	- **Set notation**: R = {(1,a), (1,b), (2,b), (2,c), (3,a)}  
	- **Relation symbol**: Write "1 R a" to mean "1 is related to a"
#### Relations vs Functions - The Key Difference!
- **Function**: Every element in the first set maps to EXACTLY ONE element in the second set.
- **Relation**: More flexible - elements can map to multiple things, or nothing at all.
- **Remember**: All functions are relations, but not all relations are functions!
## Real Example: Students and Classes
• A = {Adam, Kevin}, B = {discrete math, programming, nutrition, composition}  
• Adam takes: discrete math, programming, nutrition  
• Kevin takes: discrete math, composition  
• **The relation**: {(Adam, discrete math), (Adam, programming), (Adam, nutrition), (Kevin, discrete math), (Kevin, composition)}
## Relations on the Same Set (A to A)
• **Example**: A = {1, 2, 3, 4}, relation R where "a divides b"  
• **"a divides b" means**: b ÷ a gives a whole number (no remainder)  
• **Working it out**:
- 1 divides everything: (1,1), (1,2), (1,3), (1,4)
- 2 divides 2 and 4: (2,2), (2,4)
- 3 only divides 3: (3,3)
- 4 only divides 4: (4,4)  
    • **Final relation**: {(1,1), (1,2), (1,3), (1,4), (2,2), (2,4), (3,3), (4,4)}
## Counting Relations - The Big Formula!
• **Question**: How many relations exist from set A to itself?  
• **If A has n elements**: A × A has n² ordered pairs  
• **Since a relation is a subset**: Each of the n² pairs can either be included or not  
• **Answer**: 2^(n²) possible relations  
• **Example**: If A has 3 elements, there are 2^9 = 512 possible relations!
## Practice Problem Breakdown
Given ordered pairs: (1,1), (1,3), (2,4), (2,1) and these relation definitions:
-  **R₁: a = b** (equal values)
	- Only (1,1) works because 1 = 1
	- Others don't work: 1≠3, 2≠4, 2≠1
- **R₂: a ≤ b** (less than or equal)
	- (1,1) ✓ because 1 ≤ 1
	- (1,3) ✓ because 1 ≤ 3
	- (2,4) ✓ because 2 ≤ 4
	- (2,1) ✗ because 2 > 1
- **R₃: a > b** (greater than)
	- (1,1) ✗ because 1 is not > 1
	- (1,3) ✗ because 1 is not > 3
	- (2,4) ✗ because 2 is not > 4
	- (2,1) ✓ because 2 > 1
-  **R₄: a + b ≤ 3** (sum is at most 3)
	- (1,1) ✓ because 1+1 = 2 ≤ 3
	- (1,3) ✗ because 1+3 = 4 > 3
	- (2,4) ✗ because 2+4 = 6 > 3
	- (2,1) ✓ because 2+1 = 3 ≤ 3
### Properties of Relations
**The Four Properties of Relations**
1. **REFLEXIVE PROPERTY**:
	- **Definition**: A relation is reflexive if (a,a) is in the relation for ALL elements a in the set  
	- **Simple way to think about it**: Every element must be related to itself  
	- **Test**: Check if all pairs like (1,1), (2,2), (3,3) etc. are in the relation
	**Examples from class:**  
	- **R1: a = b** → REFLEXIVE ✓ (because a always equals a)  
	- **R2: a ≤ b** → REFLEXIVE ✓ (because a is always ≤ a)  
	- **R3: a > b** → NOT REFLEXIVE ✗ (because a cannot be > a)  
	- **R4: a + b ≤ 3** → NOT REFLEXIVE ✗ (works for (0,0) and (1,1) but not all values)
	**Key point**: It must work for EVERY element in the set, not just some!
2. **SYMMETRIC PROPERTY**:
	- **Definition**: If (a,b) is in the relation, then (b,a) must also be in the relation  
	- **Simple way to think about it**: If you can go from a to b, you can go from b to a  
	- **Test**: For every pair (a,b) in the relation, check if (b,a) is also there
	**Examples from class:**  
		- **R1: a = b** → SYMMETRIC ✓ (if a = b, then b = a)  
		- **R2: a ≤ b** → NOT SYMMETRIC ✗ (if 3 ≤ 4, then 4 ≤ 3 is false)  
		- **R3: a > b** → NOT SYMMETRIC ✗ (if 4 > 3, then 3 > 4 is false)  
		- **R4: a + b ≤ 3** → SYMMETRIC ✓ (if a + b ≤ 3, then b + a ≤ 3 because addition is commutative)
3. **ANTI-SYMMETRIC PROPERTY**:
	- **Definition**: If BOTH (a,b) AND (b,a) are in the relation, then a must equal b  
	- **Important**: This is NOT the same as "not symmetric"!  
	- **Logic form**: If (a,b) ∈ R AND (b,a) ∈ R, then a = b  
	- **Key insight**: We only care about cases where BOTH directions exist
	**Examples from class:**  
	- **R1: a = b** → ANTI-SYMMETRIC ✓ (trivially true since a always equals b)  
	- **R2: a ≤ b** → ANTI-SYMMETRIC ✓ (the only way both a ≤ b AND b ≤ a is if a = b) 
	- **R3: a > b** → ANTI-SYMMETRIC ✓ (vacuously true - you can never have both a > b AND b > a).
	- **R4: a + b ≤ 3** → NOT ANTI-SYMMETRIC ✗ (counterexample: (2,1) and (1,2) are both in relation but 2 ≠ 1)
	**Professor X's trick**: When the implication's premise is false, the whole statement is "vacuously true"
4. **TRANSITIVE PROPERTY**
	- **Definition**: If (a,b) is in the relation AND (b,c) is in the relation, then (a,c) must also be in the relation  
	- **Simple way to think about it**: If you can go from a to b, and from b to c, then you can go directly from a to c  
	- **Test**: Look for chains and verify the "shortcut" exists
**Examples from class:**  
- **R1: a = b** → TRANSITIVE ✓ (if a = b and b = c, then a = c)  
- **R2: a ≤ b** → TRANSITIVE ✓ (if a ≤ b and b ≤ c, then a ≤ c)  
- **R3: a > b** → TRANSITIVE ✓ (if a > b and b > c, then a > c)  
- **R4: a + b ≤ 3** → NOT TRANSITIVE ✗ (counterexample: (3,0) and (0,2) are in relation, but (3,2) is not since 3+2 = 5 > 3).
#### Working with Listed Ordered Pairs
Professor X showed us an example with R = {(1,1), (1,2), (2,1), (2,2), (3,3)} on set {1,2,3}:
**Checking Reflexive:** Need (1,1), (2,2), (3,3) all in R  
✓ All present → REFLEXIVE
**Checking Symmetric:**  
(1,1) → need (1,1) ✓  
(1,2) → need (2,1) ✓  
(2,1) → need (1,2) ✓  
(2,2) → need (2,2) ✓  
(3,3) → need (3,3) ✓  
All symmetric pairs present → SYMMETRIC
**Checking Anti-symmetric:**  
(1,2) and (2,1) both in R, but 1 ≠ 2  
Counterexample found → NOT ANTI-SYMMETRIC
**Checking Transitive:** Must check ALL possible chains:  
(1,1) and (1,2) → need (1,2) ✓  
(1,2) and (2,1) → need (1,1) ✓  
(1,2) and (2,2) → need (1,2) ✓  
(2,1) and (1,1) → need (2,1) ✓  
(2,2) and (2,1) → need (2,1) ✓  
(3,3) and (3,3) → need (3,3) ✓  
All chains work → TRANSITIVE
## **Exam Strategy Tips**

**To prove a property is TRUE:**  
• You need to show it works for ALL possible cases (usually requires reasoning through the general case)

**To prove a property is FALSE:**  
• You only need ONE counterexample!

**Common mistakes to avoid:**  
• Don't confuse "not symmetric" with "anti-symmetric"  
• For anti-symmetric, only check pairs where BOTH directions exist  
• For transitive, you must check ALL possible chains, not just some  
• Remember that properties must hold for ALL elements in the domain

**Quick checks:**  
• Reflexive: Are all (a,a) pairs present?  
• Symmetric: For every (a,b), is (b,a) also there?  
• Anti-symmetric: When both (a,b) and (b,a) exist, does a = b?  
• Transitive: For every chain (a,b), (b,c), is (a,c) also there?
# Operations on Relations and Matrix Representations

## Combining Relations (Union, Intersection, Difference, XOR)

**The Big Idea:** Relations are just sets of ordered pairs, so we can combine them using the same rules as regular sets!

### Union (R₁ ∪ R₂)

• **What it means:** All ordered pairs that are in EITHER R₁ OR R₂ (or both)  
• **Example:** If R₁ = {(1,0), (1,1), (1,2), (2,2)} and R₂ = {(1,1), (3,2), (4,2)}  
• **Result:** R₁ ∪ R₂ = {(1,0), (1,1), (1,2), (2,2), (3,2), (4,2)}  
• **Key point:** Include everything from both relations!

### Intersection (R₁ ∩ R₂)

• **What it means:** Only ordered pairs that are in BOTH R₁ AND R₂  
• **Using same example:** Only (1,1) appears in both relations  
• **Result:** R₁ ∩ R₂ = {(1,1)}  
• **Key point:** Only the common elements survive!

### Difference (R₁ - R₂)

• **What it means:** All pairs in R₁ EXCEPT those that are also in R₂  
• **R₁ - R₂:** Start with R₁, remove anything that's also in R₂  
• **Result:** R₁ - R₂ = {(1,0), (1,2), (2,2)} (removed (1,1) because it's in R₂)  
• **R₂ - R₁:** Start with R₂, remove anything that's also in R₁  
• **Result:** R₂ - R₁ = {(3,2), (4,2)} (removed (1,1) because it's in R₁)  
• **Key point:** ORDER MATTERS! R₁ - R₂ ≠ R₂ - R₁

### XOR (Exclusive OR)

• **What it means:** Pairs that are in R₁ OR R₂ but NOT in both  
• **Formula:** (R₁ ∪ R₂) - (R₁ ∩ R₂)  
• **Result:** {(1,0), (1,2), (2,2), (3,2), (4,2)} (everything except (1,1))  
• **Key point:** It's like saying "one or the other, but not both!"

## Composition of Relations

**The Big Idea:** Just like function composition f(g(x)), but with relations! We work from RIGHT to LEFT.

### Requirements for Composition

• **Must have:** R₁ goes from set A to set B, R₂ goes from set B to set C  
• **Critical:** The "middle set" B must be the SAME in both relations  
• **Result:** New relation from set A to set C

### How Composition Works (R₂ ∘ R₁)

• **Step 1:** Start with an ordered pair (a,b) from R₁  
• **Step 2:** Look for (b,c) in R₂ (the b must match!)  
• **Step 3:** If you find it, include (a,c) in your result  
• **Step 4:** Repeat for all pairs

### Detailed Example

**Given:** R₁ = {(1,1), (1,3), (1,4), (2,3), (3,1), (3,4)} and R₂ = {(1,0), (3,1), (3,2), (4,1)}

**Process:**  
• (1,1) from R₁ → look for (1,?) in R₂ → find (1,0) → result: (1,0)  
• (1,3) from R₁ → look for (3,?) in R₂ → find (3,1) and (3,2) → results: (1,1) and (1,2)  
• (1,4) from R₁ → look for (4,?) in R₂ → find (4,1) → result: (1,1) [already have it]  
• (2,3) from R₁ → look for (3,?) in R₂ → find (3,1) and (3,2) → results: (2,1) and (2,2)  
• (3,1) from R₁ → look for (1,?) in R₂ → find (1,0) → result: (3,0)  
• (3,4) from R₁ → look for (4,?) in R₂ → find (4,1) → result: (3,1)

**Final Answer:** R₂ ∘ R₁ = {(1,0), (1,1), (1,2), (2,1), (2,2), (3,0), (3,1)}

## Powers of Relations

**The Big Idea:** R² = R ∘ R, R³ = R² ∘ R, R⁴ = R³ ∘ R, etc.

### Self-Composition Example

**Given:** R = {(1,1), (2,1), (3,2), (4,3)}

**R² (R composed with itself):**  
• (1,1) → 1 maps to 1, 1 maps to 1 → (1,1)  
• (2,1) → 2 maps to 1, 1 maps to 1 → (2,1)  
• (3,2) → 3 maps to 2, 2 maps to 1 → (3,1)  
• (4,3) → 4 maps to 3, 3 maps to 2 → (4,2)  
• **Result:** R² = {(1,1), (2,1), (3,1), (4,2)}

**R³ (R² composed with R):**  
• Following same process...  
• **Result:** R³ = {(1,1), (2,1), (3,1), (4,1)}

**R⁴ and R⁵:**  
• **Result:** R⁴ = R⁵ = {(1,1), (2,1), (3,1), (4,1)}  
• **Pattern:** From R³ onward, all powers give the same result!

### Key Insights About Powers

• **R¹ = R** (by definition)  
• **Higher powers** often stabilize to the same result  
• **Each power** represents paths of that length in the relation  
• **R²** shows 2-step connections, **R³** shows 3-step connections, etc.
## 9.3
# Matrix Representations of Relations

## Creating Matrix Representations

• **Basic Setup**: Use a 0-1 matrix where 1 = ordered pair IS in the relation, 0 = ordered pair is NOT in the relation  
• **Matrix Dimensions**: If set A has size m and set B has size n, your matrix will be m × n (m rows, n columns)  
• **Example Process**:

- Set A = {0, 1, 2} and Set B = {1, 2, 3, 4} creates a 3×4 matrix
- Check each possible ordered pair (like 0,1 or 1,2)
- If the pair is in your relation, put a 1; if not, put a 0  
    • **Reading Matrices Backwards**: You can decode a matrix by finding all the 1s and writing out the corresponding ordered pairs

## Visual Property Detection (Square Matrices Only!)

**Important Note**: These visual checks only work for relations from a set to itself (square matrices)

### Reflexive Property

• **What to look for**: Main diagonal must be ALL 1s  
• **Why**: Every element must relate to itself (a,a must be in relation)  
• **Visual check**: Draw a line from top-left to bottom-right - all entries on this line should be 1

### Irreflexive Property

• **What to look for**: Main diagonal must be ALL 0s  
• **Why**: No element can relate to itself (a,a cannot be in relation)  
• **Visual check**: Same diagonal line, but all entries should be 0

### Symmetric Property

• **What to look for**: Matrix equals its own transpose  
• **Easy visual method**: "Fold" the matrix along the main diagonal - everything should match up perfectly  
• **Why**: If (a,b) is in relation, then (b,a) must also be in relation  
• **Check**: If position (i,j) has a 1, then position (j,i) must also have a 1

### Anti-symmetric Property

• **What to look for**: For positions across the diagonal, at most ONE can be a 1  
• **Rule**: Either position (i,j) is 0 OR position (j,i) is 0 (or both are 0)  
• **Why**: If both (a,b) and (b,a) are in relation, then a must equal b  
• **Visual**: Look at mirror positions across diagonal - they can't both be 1s

### Asymmetric Property

• **Requirements**: Must be BOTH anti-symmetric AND irreflexive  
• **What to look for**: Diagonal all 0s AND mirror positions can't both be 1s

## Matrix Operations for Relations

### Union of Relations (Join Operation)

• **Process**: Add corresponding positions using OR logic  
• **Rule**: Result is 1 if EITHER original matrix has a 1 in that position  
• **Examples**: 1∨0=1, 0∨0=0, 1∨1=1

### Intersection of Relations (Meet Operation)

• **Process**: Combine corresponding positions using AND logic  
• **Rule**: Result is 1 only if BOTH original matrices have 1s in that position  
• **Examples**: 1∧1=1, 1∧0=0, 0∧0=0

### Composition of Relations

• **Key Point**: Use Boolean product in REVERSE order (S∘R uses matrix R × matrix S)  
• **Process**:

- Take each row from first matrix
- Multiply with each column from second matrix using Boolean arithmetic
- Use AND for individual multiplications, OR to combine results  
    • **Example**: For row [1,0,1] and column [1,1,0]: (1∧1)∨(0∧1)∨(1∧0) = 1∨0∨0 = 1

### Matrix Squaring

• **Purpose**: Find R² (composition of relation with itself)  
• **Process**: Same as composition but multiply matrix by itself  
• **Use**: Essential for checking transitivity

## Checking Transitivity (The Hard One!)

• **Process**:

1. Square the original matrix (compute R²)
2. Compare R² with original matrix R
3. Check if every 1 in R² corresponds to a 1 in original R  
    • **Rule**: If R² has a 1 somewhere that R has a 0, then NOT transitive  
    • **Why it works**: R² shows all 2-step paths; transitivity requires these to already be direct connections  
    • **Example**: If R² has a 1 at position (1,3) but original R has 0 there, the relation is not transitive

## Complete Example Walkthrough

Given matrix:

```
[1 1 1]
[1 0 1] 
[1 1 1]
```

**Checking each property:**  
• **Reflexive**: NO (diagonal isn't all 1s - middle position is 0)  
• **Irreflexive**: NO (diagonal isn't all 0s)  
• **Symmetric**: YES (matrix equals its transpose)  
• **Anti-symmetric**: NO (has 1s in mirror positions)  
• **Asymmetric**: NO (not both anti-symmetric and irreflexive)  
• **Transitive**: NO (when squared, position (2,1) becomes 1 but was 0 in original)
# Equivalence Relations and Partitions

## What is an Equivalence Relation?

• An equivalence relation is a special type of relation that has THREE specific properties:

- **Reflexive**: Every element is related to itself (a ~ a)
- **Symmetric**: If a is related to b, then b is related to a (if a ~ b, then b ~ a)
- **Transitive**: If a is related to b AND b is related to c, then a is related to c (if a ~ b and b ~ c, then a ~ c)  
    • Uses the tilde symbol (~) to show "a is equivalent to b"  
    • If ALL THREE properties hold true, then it's an equivalence relation!

## Example 1: Real Numbers Relation

**The relation**: a ~ b if and only if (a - b) is an integer

**Testing the properties:**  
• **Reflexive**: Does a ~ a? Yes! Because a - a = 0, and 0 is an integer ✓  
• **Symmetric**: If a ~ b, does b ~ a? Yes! If a - b = some integer C, then b - a = -C (also an integer) ✓  
• **Transitive**: If a ~ b and b ~ c, does a ~ c? Yes! Because a - c = (a - b) + (b - c), and integer + integer = integer ✓

**Result**: This IS an equivalence relation because all three properties work!

## Example 2: String Length Relation

**The relation**: Two strings are related if they have the same length

**Testing the properties:**  
• **Reflexive**: Is a string related to itself? Yes! "cat" has 3 letters, and 3 = 3 ✓  
• **Symmetric**: If string a has same length as string b, does b have same length as a? Yes! If both have 4 letters, then 4 = 4 both ways ✓  
• **Transitive**: If a and b have same length, and b and c have same length, do a and c have same length? Yes! If all three have 7 letters, then a and c both have 7 letters ✓

**Result**: This IS an equivalence relation!

## Example 3: Division Relation (Counter-example)

**The relation**: a ~ b if a divides b (a goes into b evenly)

**Testing the properties:**  
• **Reflexive**: Does every number divide itself? Yes! 7 ÷ 7 = 1 (no remainder) ✓  
• **Symmetric**: If a divides b, does b divide a? NO! Counter-example: 2 divides 8 (8 ÷ 2 = 4), but 8 does NOT divide 2 (2 ÷ 8 = 0.25) ✗  
• **Transitive**: We don't need to check this since symmetric already failed!

**Result**: This is NOT an equivalence relation because it fails the symmetric property!

## Equivalence Classes

• An **equivalence class** is a group of all elements that are related to each other  
• Example: If a ~ b when a = b or a = -b, then:

- Equivalence class of 1: {1, -1}
- Equivalence class of 0: {0}
- Equivalence class of 2: {2, -2}
- Equivalence class of 3: {3, -3}  
    • We use brackets [a] to represent the equivalence class containing element a

## Partitions

**Definition**: A partition of a set S is a way to divide S into smaller groups where:

1. **No empty subsets** (each group has at least one element)
2. **No overlap** (no element appears in more than one group)
3. **All elements included** (every element from S appears in exactly one group)

## Partition Examples with Digits 1-9

**Random partition**: {1,2,3}, {4,5}, {6,7,8,9}  
• No empty sets ✓  
• No overlap ✓  
• All elements included ✓  
• This IS a valid partition!

**Even/Odd partition**: {2,4,6,8}, {1,3,5,7,9}  
• No empty sets ✓  
• No overlap ✓  
• All elements included ✓  
• This IS a valid partition!

**Mod 3 partition** (remainder when divided by 3):  
• [0]: {3,6,9} (remainder 0)  
• [1]: {1,4,7} (remainder 1)  
• [2]: {2,5,8} (remainder 2)  
• This IS a valid partition!

## Mod 4 Partition for All Integers

**Equivalence classes based on remainder when divided by 4:**  
• [0]: {..., -8, -4, 0, 4, 8, 12, ...} (divisible by 4)  
• [1]: {..., -7, -3, 1, 5, 9, 13, ...} (remainder 1)  
• [2]: {..., -6, -2, 2, 6, 10, 14, ...} (remainder 2)  
• [3]: {..., -5, -1, 3, 7, 11, 15, ...} (remainder 3)

## Testing Partitions - Four Examples

**P1**: {1,2}, {3,4,5}, {6,7}, { } (empty set)  
• Contains empty set ✗  
• **NOT a partition!**

**P2**: {1,2}, {3,4,5}, {6,7}  
• No empty sets ✓  
• No overlap ✓  
• All elements included ✓  
• **IS a partition!**

**P3**: {1,2,3}, {3,4,5}, {6,7}  
• Element 3 appears twice ✗  
• **NOT a partition!**

**P4**: {1,2,3}, {4,5}, {6}  
• Missing element 7 ✗  
• **NOT a partition!**
## 9.5
# Equivalence Relations and Partitions

## What is an Equivalence Relation?

• An equivalence relation is a special type of relation that has THREE specific properties:

- **Reflexive**: Every element is related to itself (a ~ a)
- **Symmetric**: If a is related to b, then b is related to a (if a ~ b, then b ~ a)
- **Transitive**: If a is related to b AND b is related to c, then a is related to c (if a ~ b and b ~ c, then a ~ c)  
    • Uses the tilde symbol (~) to show "a is equivalent to b"  
    • If ALL THREE properties hold true, then it's an equivalence relation!

## Example 1: Real Numbers Relation

**The relation**: a ~ b if and only if (a - b) is an integer

**Testing the properties:**  
• **Reflexive**: Does a ~ a? Yes! Because a - a = 0, and 0 is an integer ✓  
• **Symmetric**: If a ~ b, does b ~ a? Yes! If a - b = some integer C, then b - a = -C (also an integer) ✓  
• **Transitive**: If a ~ b and b ~ c, does a ~ c? Yes! Because (a - b) + (b - c) = (a - c), and integer + integer = integer ✓

**Result**: This IS an equivalence relation because all three properties work!

## Example 2: String Length Relation

**The relation**: Two strings are related if they have the same length

**Testing the properties:**  
• **Reflexive**: Is a string related to itself? Yes! "cat" has 3 letters, and 3 = 3 ✓  
• **Symmetric**: If string a has same length as string b, does b have same length as a? Yes! If both have 4 letters, then 4 = 4 both ways ✓  
• **Transitive**: If a and b have same length, and b and c have same length, do a and c have same length? Yes! If all three have 7 letters, then a and c both have 7 letters ✓

**Result**: This IS an equivalence relation!

## Example 3: Division Relation (Counter-example)

**The relation**: a ~ b if a divides b (a goes into b evenly)

**Testing the properties:**  
• **Reflexive**: Does every number divide itself? Yes! 7 ÷ 7 = 1 (no remainder) ✓  
• **Symmetric**: If a divides b, does b divide a? NO! Counter-example: 2 divides 8 (8 ÷ 2 = 4), but 8 does NOT divide 2 (2 ÷ 8 = 0.25) ✗  
• **Transitive**: We don't need to check this since symmetric already failed!

**Result**: This is NOT an equivalence relation because it fails the symmetric property!

## Equivalence Classes

• An **equivalence class** is a group of all elements that are related to each other  
• Example: If a ~ b when a = b or a = -b, then:

- Equivalence class of 1: {1, -1}
- Equivalence class of 0: {0}
- Equivalence class of 2: {2, -2}
- Equivalence class of 3: {3, -3}  
    • We use brackets [a] to represent the equivalence class containing element a

## Partitions

**Definition**: A partition of a set S is a way to divide S into smaller groups where:

1. **No empty subsets** (each group has at least one element)
2. **No overlap** (no element appears in more than one group)
3. **All elements included** (every element from S appears in exactly one group)

## Partition Examples with Digits 1-9

**Random Partition:**  
• A₁ = {1, 4, 7}, A₂ = {2, 5, 8}, A₃ = {3, 6, 9}  
• This works! No overlap, no empty sets, all digits included

**Even/Odd Partition:**  
• A₁ = {2, 4, 6, 8} (even numbers)  
• A₂ = {1, 3, 5, 7, 9} (odd numbers)  
• This works too!

**Mod 3 Partition (remainder when divided by 3):**  
• [0] = {3, 6, 9} (remainder 0)  
• [1] = {1, 4, 7} (remainder 1)  
• [2] = {2, 5, 8} (remainder 2)

## Mod 4 Partition for All Integers

• [0] = {..., -8, -4, 0, 4, 8, 12, ...} (divisible by 4)  
• [1] = {..., -7, -3, 1, 5, 9, 13, ...} (remainder 1)  
• [2] = {..., -6, -2, 2, 6, 10, 14, ...} (remainder 2)  
• [3] = {..., -5, -1, 3, 7, 11, 15, ...} (remainder 3)

## Testing if Something is a Partition - Quick Examples

**P₁ = {{1,2}, {3,4,5}, {6,7}, ∅}**  
• Contains empty set ✗  
• **NOT a partition**

**P₂ = {{1,2}, {3,4,5}, {6,7}}**  
• No empty sets ✓  
• No overlap ✓  
• All elements included ✓  
• **IS a partition**

**P₃ = {{1,2,3}, {3,4,5}, {6,7}}**  
• Element 3 appears twice ✗  
• **NOT a partition**

**P₄ = {{1,2}, {3,4,5}, {6}}**  
• Missing element 7 ✗  
• **NOT a partition**

---
# #Homework Homework's


---
# #Discussion Discussions


---
