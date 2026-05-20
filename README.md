# Lime Compiler

A mini compiler/interpreter project built using Python for Compiler Design coursework.

The compiler supports:

- Arithmetic Expressions
- Variables
- IF Statements
- WHILE Loops
- Arrays
- Semantic Analysis
- Runtime Error Handling
- Three Address Code (TAC)
- Code Optimization
- Register Allocation
- Assembly Generation

---

# Compiler Structure

The project follows the standard compiler phases:

1. Lexical Analysis
2. Syntax Analysis
3. Semantic Analysis
4. Intermediate Code Generation
5. Code Optimization
6. Register Allocation
7. Assembly Generation
8. Interpretation / Execution

---

# Project Structure

```bash
LimeCompiler/
│
├── Lexer.py
├── Parser.py
├── Interpreter.py
├── TAC.py
├── Optimizer.py
├── RegisterAllocator.py
├── AssemblyGenerator.py
├── Token_class.py
├── AST.py
├── main.py
│
└── tests/
    └── lexer.lime
```

---

# Compiler Phases

## 1. Lexical Analysis

The lexical analyzer converts source code into tokens.

Example:

```lime
x = 10 + 20;
```

Token Stream:

```text
IDENTIFIER(x)
=
INT(10)
+
INT(20)
;
```

The lexer supports:

- Integers
- Floats
- Variables
- Operators
- Keywords
- Arrays

---

## 2. Syntax Analysis

The parser validates grammar rules and builds an Abstract Syntax Tree (AST).

Example:

```lime
print(5 + 2 * 3);
```

AST:

```text
PrintNode(
    BinOpNode(
        5 + (2 * 3)
    )
)
```

---

## 3. Semantic Analysis

Semantic analysis checks program meaning and variable validity.

Example:

```lime
print(z);
```

Output:

```text
Semantic Error: z is undefined.
```

---

## 4. Intermediate Code Generation

The compiler generates Three Address Code (TAC).

Example:

```lime
x = 5 + 5;
```

Generated TAC:

```text
t1 = 5 + 5
x = t1
```

---

## 5. Code Optimization

The optimizer performs constant folding.

Example:

Before optimization:

```text
t1 = 5 + 5
```

After optimization:

```text
t1 = 10
```

---

## 6. Register Allocation

Temporary variables are mapped into registers.

Example:

```text
t1 = y * 2    [R1]
t2 = x + t1   [R2]
```

---

## 7. Assembly Generation

The compiler converts TAC into assembly-like instructions.

Example:

```text
ADD t1, 5, 5
MOV x, t1
```

---

# Abstract Syntax Tree Nodes

The compiler uses AST nodes such as:

- NumberNode
- VariableNode
- AssignNode
- PrintNode
- IfNode
- WhileNode
- ArrayNode
- BinOpNode

---

# Supported Features

## Arithmetic Operations

Supported operators:

- `+`
- `-`
- `*`
- `/`
- `^`
- `%`

---

## Variables

```lime
x = 10;
y = 20;

print(x + y);
```

---

## IF Statements

```lime
if 1 then print(100);
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

# TEST CASES

---

# 1. Arithmetic

## Code

```lime
print(5 + 5 * 2);
```

## Expected Output

```text
15
```

---

# 2. Parentheses + Operator Precedence

## Code

```lime
print((5 + 5) * 2 - 3 / 4 ^ 2 % 10);
```

## Expected Output

```text
19.8125
```

---

# 3. Variables

## Code

```lime
x = 10;
y = 20;

print(x + y);
```

## Expected Output

```text
30
```

---

# 4. Variable Reuse

## Code

```lime
x = 5;

y = x * 10;

print(y + x);
```

## Expected Output

```text
55
```

---

# 5. IF Statement

## Code

```lime
if 1 then print(10 + 10);
```

## Expected Output

```text
20
```

---

# 6. IF Statement (False Condition)

## Code

```lime
if 0 then print(999);
```

## Expected Output

```text
IF BODY SKIPPED
```

---

# 7. While Loop

## Code

```lime
while 3 do print(2 + 2);
```

## Expected Output

```text
4
4
4
```

---

# 8. Nested Loops

## Code

```lime
while 2 do while 3 do print(1 + 1);
```

## Expected Output

```text
2
2
2
2
2
2
```

---

# 9. Arrays

## Code

```lime
array nums = [1,2,3,4];
```

## Expected Output

```text
ARRAY nums = [1, 2, 3, 4]
```

---

# 10. Arrays + Variables

## Code

```lime
x = 10;

array vals = [x, x + 5, x * 2];
```

## Expected Output

```text
ARRAY vals = [10, 15, 20]
```

---

# 11. Power Operator

## Code

```lime
print(2 ^ 8);
```

## Expected Output

```text
256
```

---

# 12. Modulus Operator

## Code

```lime
print(10 % 3);
```

## Expected Output

```text
1
```

---

# 13. Complex Expression

## Code

```lime
x = 10;
y = 5;

print((x + y) * 2 ^ 2 - 5 % 2);
```

## Expected Output

```text
59
```

---

# 14. Semantic Error

## Code

```lime
print(z);
```

## Expected Output

```text
Semantic Error: z is undefined.
```

---

# 15. Runtime Error

## Code

```lime
print(10 / 0);
```

## Expected Output

```text
Runtime Error: Division by zero.
```

---

# 16. String Rejection

## Code

```lime
"hello";
```

## Expected Output

```text
Semantic Error: Strings are not allowed.
```

---

# 17. Full Compiler Showcase

## Code

```lime
x = 10;
y = 5;

print(x + y * 2);

if 1 then print(x ^ 2);

while 3 do print(y + 1);

array nums = [1,2,3,4];
```

## Expected Output

```text
20
100
6
6
6
ARRAY nums = [1, 2, 3, 4]
```

---

# Example Compilation Flow

## Source Code

```lime
x = 10;
y = 5;

print(x + y * 2);
```

---

## Lexer Output

```text
IDENTIFIER(x)
=
INT(10)
;
IDENTIFIER(y)
=
INT(5)
;
PRINT
(
IDENTIFIER(x)
+
IDENTIFIER(y)
*
INT(2)
)
;
```

---

## Parser Output

```text
AssignNode(x)
AssignNode(y)
PrintNode(
    BinOpNode(
        x + (y * 2)
    )
)
```

---

## Three Address Code

```text
t1 = y * 2
t2 = x + t1
PRINT t2
```

---

## Optimized TAC

```text
t1 = y * 2
t2 = x + t1
PRINT t2
```

---

## Register Allocation

```text
t1 = y * 2    [R1]
t2 = x + t1   [R2]
```

---

## Assembly Output

```text
MUL t1, y, 2
ADD t2, x, t1
OUT t2
```

---

# Running the Compiler

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/lime-compiler.git
cd lime-compiler
```

---

## 2. Run Compiler

```bash
python main.py
```

---

# Technologies Used

- Python 3
- Recursive Descent Parsing
- AST Interpretation
- Three Address Code Generation

---

# Authors

- Ramzy Ayman
- Mina Samuel
- Yehia Essam
- Loay Amgad
- Pierre Gendy
- Ahmed Sayed

---

# Course

Compiler Design Project  
Faculty of Computer Science