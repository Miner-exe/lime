# Lime Programming Language

Lime is a mini compiler/interpreter project built using Python.

The project demonstrates the practical phases of compiler construction including:

- Lexical Analysis
- Parsing
- Abstract Syntax Tree (AST)
- Three Address Code (TAC)
- Optimization
- Register Allocation
- Assembly Generation
- Semantic Analysis
- Interpretation / Execution

---

# Features

## Arithmetic Operations

Supported operators:

```lime
+
-
*
/
%
^
```

Example:

```lime
(5 + 5) * 2;
```

---

## Variables & Assignment

```lime
x = 10;
y = 5;

x + y;
```

---

## Print Statements

```lime
print(5 + 5);
```

---

## Operator Precedence

```lime
2 + 3 * 4;
```

Output:

```text
14
```

---

## Parentheses Support

```lime
(2 + 3) * 4;
```

Output:

```text
20
```

---

## IF Statements

```lime
if 1 then print(7 * 8);
```

---

## WHILE Loops

```lime
while 3 do print(2 + 2);
```

---

## Arrays

```lime
array nums = [1,2,3,4];
```

---

## Semantic Analysis

Detects:
- Undefined variables
- Invalid string usage
- Invalid expressions

Example:

```lime
x + y;
```

Output:

```text
Semantic Error:
x is undefined.
```

---

## Runtime Error Handling

Example:

```lime
10 / 0;
```

Output:

```text
Runtime Error:
Division by zero.
```

---

# Compiler Pipeline

The source code passes through multiple compiler phases:

```text
Source Code
    ↓
Lexer
    ↓
Tokens
    ↓
Parser
    ↓
AST
    ↓
Three Address Code (TAC)
    ↓
Optimizer
    ↓
Register Allocation
    ↓
Assembly Generation
    ↓
Interpreter
    ↓
Final Result
```

---

# Project Structure

```text
lime/
│
├── AST.py
├── AssemblyGenerator.py
├── Interpreter.py
├── Lexer.py
├── Optimizer.py
├── Parser.py
├── RegisterAllocator.py
├── TAC.py
├── Token_class.py
├── main.py
│
└── tests/
    └── lexer.lime
```

---

# Example Full Program

```lime
x = 10;
y = 5;

print(x + y * 2);

if 1 then print(x ^ 2);

while 3 do print(y + 1);

array nums = [1,2,3,4];
```

---

# Example Output

```text
20
100
[6, 6, 6]
[1, 2, 3, 4]
```

---

# Intermediate Code Example

Input:

```lime
print(x + y * 2);
```

Generated TAC:

```text
t1 = y * 2
t2 = x + t1
PRINT t2
```

---

# Optimized Code Example

Before Optimization:

```text
t1 = 5 + 5
```

After Optimization:

```text
t1 = 10
```

---

# Assembly Generation Example

```asm
MOV x, 10
MOV y, 5
MUL t1, y, 2
ADD t2, x, t1
OUT t2
```

---

# Test Cases

## Test Case 1 — Basic Arithmetic

### Input

```lime
(5 + 5) * 2;
```

### Expected Output

```text
20
```

---

## Test Case 2 — Variables

### Input

```lime
x = 10;
y = 5;

x + y;
```

### Expected Output

```text
15
```

---

## Test Case 3 — Print Statement

### Input

```lime
x = 10;

print(x + 5);
```

### Expected Output

```text
15
```

---

## Test Case 4 — Operator Precedence

### Input

```lime
2 + 3 * 4;
```

### Expected Output

```text
14
```

---

## Test Case 5 — Parentheses Priority

### Input

```lime
(2 + 3) * 4;
```

### Expected Output

```text
20
```

---

## Test Case 6 — Power & Modulus

### Input

```lime
2 ^ 3 % 3;
```

### Expected Output

```text
2
```

---

## Test Case 7 — IF Statement

### Input

```lime
if 1 then print(7 * 8);
```

### Expected Output

```text
56
```

---

## Test Case 8 — WHILE Loop

### Input

```lime
while 3 do print(2 + 2);
```

### Expected Output

```text
[4, 4, 4]
```

---

## Test Case 9 — Arrays

### Input

```lime
array nums = [1,2,3,4];
```

### Expected Output

```text
[1, 2, 3, 4]
```

---

## Test Case 10 — Semantic Error

### Input

```lime
x + y;
```

### Expected Output

```text
Semantic Error:
x is undefined.
```

---

## Test Case 11 — Runtime Error

### Input

```lime
10 / 0;
```

### Expected Output

```text
Runtime Error:
Division by zero.
```

---

## Test Case 12 — String Rejection

### Input

```lime
"hello";
```

### Expected Output

```text
Semantic Error:
Strings are not allowed.
```

---

# Technologies Used

- Python 3
- Recursive Descent Parsing
- AST Interpretation
- Three Address Code Generation

---

# Educational Purpose

This project was built for educational and presentation purposes to demonstrate how compilers and interpreters work internally.

The project covers most practical compiler phases including:
- lexical analysis
- parsing
- semantic analysis
- intermediate code generation
- optimization
- code generation
- execution

---

# How To Run

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/lime.git
```

---

## 2. Open Project

```bash
cd lime
```

---

## 3. Write Lime Code

Edit:

```text
tests/lexer.lime
```

---

## 4. Run Compiler

```bash
python main.py
```

---

# Authors

- Ramzy Ayman
- Mina Samuel
- Yehia Essam
- Loay Amgad
- Pierre Gendy
- Ahmed Sayed