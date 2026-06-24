---
type: class
status: archived
created: 2025-12-11
updated: 2025-12-19
area:
  - "[[Finals]]"
  - "[[Main Examples]]"
  - "[[Material]]"
tags:
  - "#class"
  - "#Textbook"
  - "#Homework"
  - "#Discussion"
next: "[[Finals]]"
---
# #Textbook Textbook & Videos
## 10.1
# Introduction to Graphs

• **What is a graph?** A graph is simply a set of vertices (dots/points) and edges (lines connecting the dots)

- You MUST have at least one vertex (vertices cannot be empty)
- You CAN have zero edges (edges can be empty - just isolated dots)
- Edges connect either one vertex (to itself) or two different vertices
- The endpoints are where the edges connect to vertices

• **Simple Graph** - This is the "basic" type of graph

- Each edge connects to different vertices
- No two edges connect the same pair of vertices
- Think of it like a clean, organized connection map
- Example: If you have vertices A, B, C, D, you can only have ONE edge between A and B
- What makes it NOT simple:
    - Adding a loop (like B connecting to itself)
    - Adding multiple edges between the same two vertices (like having two lines from A to D)

• **Multi Graph** - Allows multiple connections between same vertices

- You can have several edges connecting the same two vertices
- Example: Multiple roads between two cities
- Still NO loops allowed (no vertex connecting to itself)

• **Pseudo Graph** - The "anything goes" version

- Can have multiple edges between same vertices
- CAN have loops (vertices connecting to themselves)
- Basically combines multi graph + loops

• **Directed Graphs (Digraphs)** - Graphs with arrows showing direction

- Each edge has a direction (like one-way streets)
- Written as ordered pairs: if A points to B, we write (A,B)
- Example from Professor X: A→B, A→C, B→A, B→C, C→B, C→C
- The arrows matter! A→B is different from B→A

## Complete Graph Types Breakdown:

**Simple Graph:**

- Directed edges? NO (just regular lines)
- Multiple edges? NO
- Loops? NO

**Multi Graph:**

- Directed edges? NO
- Multiple edges? YES
- Loops? NO

**Pseudo Graph:**

- Directed edges? NO
- Multiple edges? YES
- Loops? YES

**Simple Directed Graph:**

- Directed edges? YES (arrows)
- Multiple edges? NO
- Loops? NO

**Directed Multi Graph:**

- Directed edges? YES
- Multiple edges? YES
- Loops? NO

**Mixed Graph:**

- Directed edges? BOTH (can have arrows AND regular lines)
- Multiple edges? YES
- Loops? YES
- This is the "kitchen sink" graph - you can literally have anything!

• **Mixed Graph Example:** Imagine a graph with vertices A, B, C where:

- A has a directed edge to B (A→B)
- B and C are connected with a regular undirected edge (B—C)
- C has a loop back to itself
- You could even have multiple connections between any of these!

• **Key Memory Trick:**

- Simple = Clean and basic (no extras)
- Multi = Multiple roads between cities
- Pseudo = Multi + loops (pseudo means "fake" - it's like a fake simple graph)
- Directed = One-way streets with arrows
- Mixed = Chaos allowed (everything is permitted)
## 10.2
# Graph Theory Terminology

## Undirected Graphs Terminology

**Adjacent Vertices (Neighbors)**  
• Vertices connected directly by an edge  
• Example: If A and B have an edge between them, they're adjacent/neighbors  
• If B and C don't have a direct edge, they're NOT adjacent

**Incident Edge**  
• An edge that connects two specific vertices  
• Example: "Edge B is incident with vertices E and B" means edge B connects those two points

**Neighborhood Notation: N(v)**  
• The set of ALL vertices connected to a specific vertex  
• Example: If vertex E connects to A, B, and C, then N(E) = {A, B, C}  
• D wouldn't be included if it's not directly connected to E

**Degree of a Vertex**  
• Count of ALL edges connected to that vertex  
• **IMPORTANT**: Self-loops count TWICE (since it's both in and out of the same vertex)  
• Examples from the graph:

- Degree of A = 4 (including the self-loop counted twice)
- Degree of B = 2
- Degree of E = 3
- Degree of C = 3
- Degree of D = 0

**Special Vertex Types**  
• **Isolated Vertex**: Degree = 0 (like vertex D - not connected to anything)  
• **Pendant Vertex**: Degree = 1 (connected to only one other vertex)

## The Handshaking Theorem

**The Problem Setup**  
• 6 people in a room, each shakes hands with every other person  
• Question: How many total handshakes?

**Manual Counting Method**  
• A shakes with B, C, D, E, F = 5 handshakes  
• B shakes with C, D, E, F = 4 more (already counted A-B)  
• C shakes with D, E, F = 3 more  
• D shakes with E, F = 2 more  
• E shakes with F = 1 more  
• Total: 5 + 4 + 3 + 2 + 1 = 15 handshakes

**The Mathematical Formula**  
• **Key Insight**: Every handshake involves TWO people, so we double-count  
• If we count degrees: 6 people × 5 handshakes each = 30  
• But this counts each handshake twice, so actual handshakes = 30 ÷ 2 = 15

**Handshaking Theorem Formula**  
• **2m = Σ(degrees of all vertices)**  
• Where m = number of edges  
• This works because every edge contributes 1 to the degree of each of its two endpoints

**Practice Problem**  
• 10 vertices, each with degree 6  
• Sum of all degrees = 10 × 6 = 60  
• Number of edges = 60 ÷ 2 = 30 edges

## Directed Graphs Terminology

**Key Difference**: Direction matters! Arrows show the flow direction

**Adjacent Relationships**  
• **Adjacent TO**: A is adjacent TO B (arrow goes from A to B)  
• **Adjacent FROM**: B is adjacent FROM A (same arrow, viewed from B's perspective)  
• **Initial vertex**: Starting point of an edge  
• **Terminal/End vertex**: Ending point of an edge

**Degree Types**  
• **In-degree**: Number of arrows COMING INTO a vertex  
• **Out-degree**: Number of arrows GOING OUT OF a vertex  
• Example for vertex B:

- In-degree of B = 2 (two arrows pointing into B)
- Out-degree of B = 1 (one arrow leaving B)

**Critical Relationship for Directed Graphs**  
• **Sum of all in-degrees = Sum of all out-degrees = Number of edges**  
• **Why this works**: Every edge has exactly one starting point (adds 1 to out-degree) and one ending point (adds 1 to in-degree)  
• When you add a new edge, you simultaneously add 1 in-degree and 1 out-degree

**Logical Proof**  
• Add edge from B to C:

- Increases out-degree of B by 1
- Increases in-degree of C by 1
- Total edges increases by 1  
    • This maintains the balance: in-degrees = out-degrees = edge count
# Special Types of Graphs

## Complete Graphs (K_n)

• **What it is**: A simple graph where EVERY vertex connects to EVERY other vertex exactly once  
• **Notation**: K_n (where n = number of vertices)  
• **Key rule**: No loops, no multiple edges (that's what makes it "simple")  
• **Examples**:

- K_1: Just one lonely vertex with no edges (can't connect to itself!)
- K_2: Two vertices with one edge between them
- K_3: Three vertices, each connected to the other two (triangle shape)
- K_4: Four vertices, each connected to all three others  
    • **Memory trick**: Think of it like a party where everyone shakes hands with everyone else exactly once

## Cycles (C_n)

• **What it is**: Vertices connected in a circle/loop pattern  
• **Minimum requirement**: Need at least 3 vertices (makes sense - 2 vertices would just be a line!)  
• **Connection pattern**: v₁ → v₂ → v₃ → v₄ → ... → v_n → back to v₁  
• **Examples**:

- C_3: Triangle (3 vertices in a circle)
- C_4: Square (4 vertices in a circle)  
    • **Memory trick**: Like a necklace of beads connected in order

## Wheels (W_n)

• **What it is**: Take a cycle and add one "hub" vertex in the center that connects to ALL vertices in the cycle  
• **Construction**: Cycle + 1 central vertex + spokes to every cycle vertex  
• **Examples**:

- W_3: Triangle with center point (looks like a wheel with 3 spokes)
- W_4: Square with center point (looks like a wheel with 4 spokes)  
    • **Memory trick**: Literally looks like a bicycle wheel with spokes!

## Hypercubes/n-Cubes (Q_n)

• **What it is**: Graph where vertices represent all possible n-bit binary strings  
• **Notation**: Q_n (where n = length of bit strings)  
• **Total vertices**: 2^n vertices (since there are 2^n possible n-bit strings)  
• **Connection rule**: Two vertices are connected if their bit strings differ by EXACTLY one bit  
• **Construction process**:

- Start with Q_1: vertices "0" and "1" connected by one edge
- For Q_2: Take two copies of Q_1, add "0" prefix to one copy, "1" prefix to other, then connect corresponding vertices
- Keep doubling and adding prefixes for higher dimensions  
    • **Examples**:
- Q_1: Two vertices (0, 1) with one edge
- Q_2: Four vertices (00, 01, 10, 11) - forms a square
- Q_3: Eight vertices - forms a 3D cube  
    • **Memory trick**: Think of computer memory addresses - neighboring addresses differ by one bit

## Bipartite Graphs

• **What it is**: A simple graph where vertices can be split into TWO groups such that:

- No vertex in group 1 connects to another vertex in group 1
- No vertex in group 2 connects to another vertex in group 2
- Edges ONLY go between the two groups  
    • **Key insight**: It's like two teams where teammates never directly connect, only opponents do

### How to Test if a Graph is Bipartite (Graph Coloring Method):

1. **Pick any vertex and color it blue**
2. **Color all its neighbors green** (since they can't be the same color)
3. **For each green vertex, color all ITS neighbors blue**
4. **Continue this pattern**
5. **Check for conflicts**: If you ever need to color a vertex that's already colored differently, it's NOT bipartite
6. **Success**: If you can color the whole graph with just two colors without conflicts, it IS bipartite

### Example Walkthrough:

• Start with vertex A (blue)  
• A connects to G, F, E, C → color them all green  
• Check: Are any green vertices connected to each other? If YES → not bipartite  
• If NO → continue coloring their neighbors blue  
• Keep checking for color conflicts

## Complete Bipartite Graphs (K_m,n)

• **What it is**: A bipartite graph where EVERY vertex in group 1 connects to EVERY vertex in group 2  
• **Notation**: K_m,n (where m = size of first group, n = size of second group)  
• **Examples**:

- K_2,3: One group has 2 vertices, other has 3 vertices, and all 2 connect to all 3
- K_4,4: Two groups of 4 vertices each, every vertex connects to all 4 in the opposite group  
    • **Memory trick**: Like a complete graph, but split into two teams where everyone on team 1 knows everyone on team 2 (but teammates don't know each other)

## Key Testing Strategy for Exams:

• **For complete graphs**: Count vertices and check if every vertex connects to every other vertex  
• **For cycles**: Look for circular connection pattern with no "shortcuts"  
• **For wheels**: Find the cycle + identify the central hub vertex  
• **For bipartite**: Use the two-coloring method - if it works, it's bipartite!  
• **For complete bipartite**: First confirm it's bipartite, then check if it's "complete" (every vertex in one group connects to every vertex in the other group)

---
# #Homework Homework's


---
# #Discussion Discussions


---
