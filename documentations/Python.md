# Python Complete Guide

# 1. Introduction

## What is Python?

Python is a high-level, interpreted, general-purpose programming language known for its simple syntax and readability, making it one of the most popular languages in the world.

---

## Why Python?

Python isn't just popular by accident - it's widely used because it solves real problems faster, cleaner and with less effort compared to many other languages.

1. **Simple & Readable Syntax**: Python feels almost like reading English, which makes it perfect for beginners and professionals alike.

```python
if age > 18:
    print("Eligible")
```

2. **Rapid Development (Write Less, Do More)**
* Fewer lines of code as compared to Java/C++
* Quick prototyping and faster delivery

3. **Huge Ecosystem and Libraries**
Python has libraries for almost everything:
* Data Science → Pandas, NumPy
* AI/ML → TensorFlow, PyTorch
* Web → FastAPI, Django

4. **Versatility**
Python is used in:
* Web Development
* Artificial Intelligence
* Data Analysis

5. **Strong Community Support**
* Millions of developers worldwide
* Tons of tutorials, documentations, and open-source projects

6. **Cross-Platform Compatibility**
Python works on:
* Windows
* Linux
* macOS

7. **Integration Friendly**
Python easily integrates with:
* Databases (PostgreSQL, MySQL)
* APIs
* Other languages

---

## Use Cases

* Web Development
* Data Science
* Machine Learning

---

# 2. Installation & Setup

## Install Python

* Go to: https://www.python.org/downloads/
* Click Download Python (latest version)
* Run Installer: Open the downloaded .exe file
* Check this box: **✔ Add Python to PATH**
* Click Install Now

---

## Verify Installation
Open command Prompt and run
```bash
python --version
```

---

## Setup IDE (VS Code)

1. **Install VS Code**
* Go to: https://code.visualstudio.com/
* Download and install VS Code for your OS
* Open VS Code after installation

2. **Install Python Extension**
Steps:
* Open VS Code
* Go to Extensions (Ctrl + Shift + X)
* Search for: Python
* Install the extension by Microsoft

3. **Select Python Interpreter**
Steps:
* Press Ctrl + Shift + P
* Search: Python: Select Interpreter
* Choose your Python version (e.g., Python 3.14)

If using virtual environment, select: ./venv/bin/python  OR  venv\Scripts\python.exe

4. **Recommended Extensions**

Install these for better productivity:

* Python (Microsoft)
* Pylance (better IntelliSense)
* Black Formatter (auto formatting)
* isort (import sorting)
* GitLens (Git support)

---

## Install pip

**What is pip?**
pip is Python’s package manager, used to install and manage external libraries.

**Step 1**
If pip is already installed
```bash
pip --version
```

**Step 2**

If pip is not installed

```bash
python -m ensurepip --upgrade
```

---

# 3. Python Basics

## Syntax

Python syntax is designed with a strong emphasis on **readability and simplicity**. Unlike many programming languages (like C, Java), Python:

* Uses **indentation instead of braces `{}`** to define code blocks
* **Indentation** means adding spaces at the beginning of a line of code to define its structure and grouping.
* Python uses indentation to determine:
  → Which statements belong to a block
  → Scope of conditions, loops, functions, classes
* Without proper indentation → Syntax error
* Avoids unnecessary symbols like semicolons (`;`)
* Encourages writing clean, human-readable code

---

### Key Rules of Python Syntax

1. **Indentation is mandatory**

   * Typically 4 spaces (not tabs)
   * Defines scope of loops, conditions, functions

2. **No semicolons required**

```python
x = 10
y = 20
```

3. **Case-sensitive language**

```python
name = "Ashish"
Name = "Different"  # Different variable
```

---

### Practical Examples

```python
# Correct indentation
if True:
    print("This works")

# Incorrect indentation → Error
# if True:
# print("Error")
```

---

## Variables

Variables in Python are **references to objects**, not containers of data like in C/C++.

* In Python, a variable does not stores the actual data.
* Instead, it stores a reference (pointer) to an object that exists somewhere in memory.

Python uses:

* **Dynamic typing** → The data type of a variable is determined at runtime and no need to declare data type explicitly.
* Variable type is decided when the program runs and we can change the data type of a variable anytime.
* As we know, Python variables are just references to objects → The object has a type, not a variable.
* When we assign a new value → variable points to a new object.

* **Strong typing** → Type matters during operations.
* Strong Typing means that Python strictly enforces type rules, and cannot perform invalid operations incompatible types.
* In simple terms,
  → Python does not automatically converts types in unsafe ways.
  → Must explicitly convert types when needed.

---

### Internal Concept (Important)

```python
a = 10
b = a
```

→ Both `a` and `b` point to the **same object in memory**, not copies → In simple terms, Both a and b do not store separate copies of 10. Instead, they both reference (point to) the same object in memory.

---

### Dynamic Typing

```python
x = 10       # int
x = "Hello"  # now string
```

### Type Checking

```python
x = 10
print(type(x))  # <class 'int'>
```

---

### Naming Rules

* Must start with letter or underscore
* Cannot use keywords
* Case-sensitive

```python
_valid = 10
age = 25
# 1 age invalid
```

---

### Practical Examples

```python
name = "Ashish"
age = 25
is_active = True

print(name, age, is_active)
```

---

## Comments

Comments are used to:

* Explain code
* Improve readability
* Document logic

Python ignores comments during execution.

---

### Types of Comments

#### 1. Single-line Comment

```python
# This is a comment
```

---

#### 2. Multi-line Comment (Docstring style)

A docstring is a special type of string used to document Python modules, classes, functions, or methods.

It is writing using triple quotes (""" """ or ''' ''') and placed immediately after the definition.

→ Explains what the code does?
→ Helps other developers understand usage
→ Used by tools like help() and documentation generators
→ Used in functions, classes and modules.

```python
"""
This is a multi-line comment
Used for documentation
"""
```

*  Often used as **docstrings** in functions/classes

---

### Best Practices

* Write meaningful comments
* Avoid obvious comments

Bad:

```python
x = 10  # assigning 10
```

Good:

```python
# Store user age for eligibility check
age = 25
```

---

### Practical Example

```python
# Calculate area of rectangle
length = 10
width = 5
area = length * width
```

---

## Input / Output

Python provides built-in functions for interacting with users:

* `input()` → Takes user input (always returns string)
* `print()` → Displays output

---

### Important Concept

```python
age = input("Enter age: ")
```

→ `age` will be **string**, not integer

* The input() function in Python always returns data as a string (str), regardless of what the user types.

* How **input () works internally**?
→ Python displays the prompt → "Enter age: "
→ User types something (e.g., 25)
→ That input is read as text from the keyboard (stdin)
→ Python returns it as a string
→So, even if we type 25, Python treats it as "25"

* Why Python does this?
→ Input comes from the keyboard as raw text → Computers receive keyboard input as a sequence of characters (text), not typed values
→ Python does not assume the intended type → Python cannot safely guess what the user means?
→ Keeps behavior consistent and predictable → Always returning a string ensures uniform and reliable behavior.

---

### Type Conversion Required

```python
age = int(input("Enter age: "))
```

---

### Output Formatting

#### Basic Print

```python
print("Hello")
```

---

#### Multiple Values

```python
name = "Ashish"
age = 25
print(name, age)
```

---

#### f-Strings (Recommended)

An f-string (formatted string literal) is a way to embed variables or expressions directly inside a string using curly braces {}, introduced in Python 3.6.

```python
name = "Ashish"
print(f"My name is {name}")
```

#### How f-String works?

The prefix f before the string tells Python:
→ Evaluate expressions inside {} and insert their values here.
→ {name} is replaced with the value stored in the variable name.

---

#### Format Method

The .format() method is an older (but still widely used) way to insert values into a string.

→ {} → Placeholder inside the string
→ .format(25) → Supplies the value to replace {}

```python
print("My age is {}".format(25))
```

---

### Input Example

```python
name = input("Enter your name: ")
print(f"Hello {name}")
```

---

### Practical Mini Program

```python
# Simple calculator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2

print(f"Sum is: {sum}")
```

---

### Key Takeaways

* `input()` → Always returns string
* Use `int()`, `float()` for conversion
* Prefer **f-strings** for output formatting
* Keep I/O logic clean and simple

---

# Summary

| Concept      | Key Idea                         |
| ------------ | -------------------------------- |
| Syntax       | Indentation-based, readable      |
| Variables    | References to objects            |
| Comments     | Improve readability              |
| Input/Output | User interaction using built-ins |

---

# 4. Data Types

## Numbers

Numbers in Python represent numeric values and are **immutable** (cannot be changed after creation).

### Types of Numbers:

* **int** → Integer (e.g., 10, -5)
* **float** → Decimal (e.g., 3.14)
* **complex** → Complex numbers (e.g., 2 + 3j)

---

### Internal Concepts

* Python integers have **arbitrary precision** → no overflow → Python integers can grow to any size limited only by memory, so they don’t overflow like fixed-size integers in languages like C/C++.
* Floats are based on **IEEE 754 double precision** → Python floats follow the IEEE 754 standard, meaning they store numbers in a fixed 64-bit format, which can cause small precision errors.
* All numbers are objects in Python

---

### Practical Examples

```python
x = 10          # int
y = 3.14        # float
z = 2 + 3j      # complex

print(type(x))  # <class 'int'>
```

---

### Common Operations

```python
a = 10
b = 3

print(a + b)   # Addition
print(a / b)   # Float division
print(a // b)  # Floor division
print(a % b)   # Modulus
print(a ** b)  # Power
```

---

## Strings

Strings are **immutable sequences of characters** used to represent text.

---

### Key Concepts

* Indexed (supports indexing & slicing)
* Immutable → operations create new strings
* Supports Unicode

---

### Practical Examples

```python
text = "Hello"

print(text[0])      # H
print(text[1:4])    # ell
print(text.upper()) # HELLO
```

---

### String Formatting (f-string)

```python
name = "Ashish"
print(f"Hello {name}")
```

---

### Immutability

```python
s = "hello"
# s[0] = 'H' -> Error
```

---

## Lists

Lists are **ordered, mutable collections** that can store multiple items of different types.

---

### Internal Concepts

* Implemented as **dynamic arrays**
* Supports resizing
* Allows duplicates

---

### Practical Examples

```python
nums = [1, 2, 3]

nums.append(4)
nums.remove(2)

print(nums)
```

---

### Common Operations

```python
nums = [1, 2, 3]

nums[0] = 10       # Modify
nums.insert(1, 5)  # Insert
nums.pop()         # Remove last
```

---

### List Comprehension

List comprehension is a concise way to create lists using a single line of code by combining a loop and optional condition.

```python
squares = [x*x for x in range(5)]
```

---

## Tuples

### Definition

Tuples are **ordered, immutable collections**.

---

### Key Concepts

* Faster than lists (less overhead)
* Immutable → safer for fixed data
* Can be used as dictionary keys

---

### Practical Examples

```python
t = (1, 2, 3)

print(t[0])
```

---

### Immutability

```python
# t[0] = 10 -> Error
```

---

### Tuple Unpacking

```python
a, b = (1, 2)
```

---

## Sets

Sets are **unordered collections of unique elements**.

---

### Internal Concepts

* Implemented using **hash tables** → A set in Python is internally backed by a hash table (same concept as dictionaries, but only keys).

A **hash** is a fixed-size integer value generated from a Python object using a hash function.

---

#### What is a **Hash Table**?
→ A data structure that stores values using a hash function
→ Each element is converted into a hash value (integer)
→ That hash decides where the element is stored in memory

---

#### Why duplicates are not allowed?

Because:

→ Each element is stored using its hash
→ If two elements are equal → they have the same hash
→ Python detects this and ignores duplicates

---

### Practical Examples

```python
s = {1, 2, 3, 3}
print(s)  # {1, 2, 3}
```

---

### Set Operations

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a | b)  # Union
print(a & b)  # Intersection
print(a - b)  # Difference
```

---

## Dictionaries

Dictionaries store data in **key-value pairs**.

---

### Practical Examples

```python
user = {
    "name": "Ashish",
    "age": 25
}

print(user["name"])
```

---

### Common Operations

```python
user["email"] = "test@gmail.com"  # Add
user.pop("age")                   # Remove
```

---

### Iteration

```python
for key, value in user.items():
    print(key, value)
```

---

## Type Casting

Type casting is the process of **converting one data type to another**.

---

### Why Needed?

* User input is always string
→ input() reads data from keyboard as raw text
→ Python does not guess the intended type
→ Everything is treated as a string by default

* Operations require specific types → Different operations expect specific data types.

| Function  | Converts To |
| --------- | ----------- |
| `int()`   | Integer     |
| `float()` | Decimal     |
| `str()`   | String      |
| `bool()`  | Boolean     |

---

### Practical Examples

```python
x = int("10")
y = float("3.14")
z = str(100)
```

---

### Casting Between Collections

Casting between collections means converting one collection type (like String, list, set, tuple) into another.

Python provides built-in functions: list(), set() and tuple().

```python
list("abc")        # ['a', 'b', 'c']
set([1, 2, 2])     # {1, 2}
tuple([1, 2, 3])   # (1, 2, 3)
```

| Feature    | list()        | tuple()     | set()          |
| ---------- | ------------- | ----------- | -------------- |
| Storage    | Dynamic array | Fixed array | Hash table     |
| Order      | Preserved     | Preserved   | Not guaranteed |
| Duplicates | Allowed       | Allowed     | Removed        |
| Mutability | Mutable       | Immutable   | Mutable        |

---

### Error Handling

```python
# int("abc") -> ValueError
```

* Python tries to:

→ Read the string "abc"
→ Convert it into an integer

* But:

→ "abc" is not a numeric string
→ So conversion fail

---

# 5. Control Flow

## if-else

The `if-else` statement is used to **control the execution flow** of a program based on conditions.

Python evaluates conditions as **True or False (Boolean logic)**.

### How It Works?

* If condition is `True` → executes `if` block
* Else → executes `else` block

---

### Practical Example

```python
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

### Multiple Conditions

```python
marks = 85

if marks >= 90:
    print("A")
elif marks >= 70:
    print("B")
else:
    print("C")
```

---

### Truthy & Falsy Values

Python treats some values as False:

* `False`
* `0`
* `None`
* Empty (`""`, `[]`, `{}`)

```python
if "":
    print("True")
else:
    print("False")  # Runs
```

---

## Nested Conditions

Nested conditions mean placing one `if` statement **inside another**.

* Used when decisions depend on multiple levels of logic.

---

### Practical Example

```python
age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Allowed")
    else:
        print("ID required")
else:
    print("Not allowed")
```

---

### Best Practice

Avoid too many nested conditions → use logical operators instead:

```python
if age >= 18 and has_id:
    print("Allowed")
```

---

## Loops

Loops are used to **repeat a block of code multiple times**.

Types:

* `for` loop → iterate over sequence
* `while` loop → run until condition is False

---

## for loop

A `for` loop is used to iterate over:

* Lists
* Strings
* Tuples
* Ranges
* Any iterable object

---

### Internal Concept

Python uses the **iterator protocol**:

Python loops work by converting objects into iterators using `iter()` and fetching elements one-by-one using `next()`.

```python
it = iter("abc")

while True:
    try:
        ch = next(it)
        print(ch)
    except StopIteration:
        break
```

| Concept         | Meaning             |
| --------------- | ------------------- |
| `iter()`        | Creates an iterator |
| `next()`        | Gets next value     |
| `StopIteration` | Signals end of loop |


---

### Practical Examples

```python
for i in range(5):
    print(i)
```

---

### Iterating Over List

```python
names = ["A", "B", "C"]

for name in names:
    print(name)
```

---

### With index

```python
for i, val in enumerate(names):
    print(i, val)
```

---

## while loop

A `while` loop runs **as long as a condition is True**.

---

### Practical Example

```python
i = 0

while i < 5:
    print(i)
    i += 1
```

---

### Infinite Loop

```python
while True:
    print("Runs forever")
```

Must use `break` to stop

---

## break, continue, pass

### break

Stops the loop immediately.

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

Output:
```
0 1 2
```

---

### continue

Skips current iteration and moves to next.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```
Output:

```
0 1 3 4
```

---

### pass
A **placeholder statement** that does nothing.

* Used when syntax requires a statement but you don’t want to execute anything.

```python
for i in range(5):
    pass
```

---

### Real Use Case

```python
def func():
    pass  # To be implemented later
```
---

# 6. Functions

A function is a **reusable block of code** that performs a specific task.

Functions help in:

* Code reusability
* Modularity
* Maintainability

In Python, functions are **first-class objects**, meaning:

* They can be assigned to variables
* Passed as arguments
* Returned from other functions

---

### Internal Concept

When a function is defined:

* Python creates a **function object**
* Stores it in memory
* The function name is just a **reference to that object**

---

### Syntax

```python
def function_name(parameters):
    # code block
    return value
```

---

### Practical Example

```python
def greet(name):
    return f"Hello {name}"

print(greet("Ashish"))
```

---

### Function Without Return

```python
def say_hello():
    print("Hello")
```

* Returns `None` implicitly

---

## Argument Types

### 1. Positional Arguments

Arguments are assigned based on their **position**.

```python
def add(a, b):
    return a + b

print(add(2, 3))  # a=2, b=3
```

---

### 2. Keyword Arguments

Arguments are passed using **parameter names**, order doesn't matter.

```python
print(add(b=3, a=2))
```

---

### 3. Default Arguments

Default values are used if no argument is provided.

```python
def greet(name="Guest"):
    print(f"Hello {name}")

greet()         # Guest
greet("Ashish") # Ashish
```

---

### Important (Mutable Default Pitfall)

```python
def func(lst=[]):
    lst.append(1)
    return lst
```

* This can cause unexpected behavior (same list reused)

---

### 4. *args (Variable Positional Arguments)

Allows passing **multiple positional arguments** as a tuple.

```python
def add(*args):
    return sum(args)

print(add(1, 2, 3, 4))
```

---

### 5. **kwargs (Variable Keyword Arguments)

Allows passing **multiple keyword arguments** as a dictionary.

```python
def print_info(**kwargs):
    print(kwargs)

print_info(name="Ashish", age=25)
```

---

## Lambda Functions

A lambda function is an **anonymous (unnamed) function** used for short, simple operations.

Key Features:

* Single expression only
* No `return` keyword
* Useful for quick operations

---

### Syntax

```python
lambda arguments: expression
```

```python
square = lambda x: x * x
print(square(5))
```

---

### With Built-in Functions

```python
nums = [1, 2, 3]

result = list(map(lambda x: x * 2, nums))
print(result)
```

---

### When NOT to Use

* Complex logic
* Multiple statements

* Use normal functions instead

---

## Recursion

Recursion is a technique where a function **calls itself**.

Used for:

* Tree/graph problems
* Divide-and-conquer algorithms

### Key Components

1. **Base Case** → Stops recursion
2. **Recursive Case** → Calls itself

```python
def factorial(n):
    if n == 1:          # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case
```

---

### Execution Flow

```
factorial(3)
→ 3 * factorial(2)
→ 3 * (2 * factorial(1))
→ 3 * (2 * 1)
→ 6
```

---

### Important Concepts

#### Recursion Limit

The recursion limit is the maximum number of times a function can call itself (directly or indirectly) before Python stops it.

Python has a recursion limit:

```python
import sys
print(sys.getrecursionlimit())
```

---

#### Why Recursion Limit exists?

To prevent infinite recursion and protect program from:

* **Crashing**

A crash happens when a program suddenly stops execution due to an error it cannot safely handle.

**What happens Internally?**
* Function keeps calling itself forever
* Python reaches recursion limit
* Raises error: RecursionError: maximum recursion depth exceeded
* Python stops (crashes) the program to protect the system

**Why Crash Happens?**
* Program enters invalid or unsafe state
* Resources (like memory) are being overused
* Python forces termination to avoid damage

* **Memory Overflow (stack overflow)**

* A special memory area called the call stack which stores function calls, local variables and execution context.

* When too many function calls fill up the stack memory.

**What is Limit didn't exists?**

Without recursion limit:
* Stack keeps growing
* Memory gets exhausted
* Program or even system may crash

---

#### Stack Behavior

Each recursive call:

* Adds a new frame to call stack
* Can cause **stack overflow** if too deep

### Tail Recursion (Note)

Tail recursion is a special type of recursion where the recursive calls is the last operation in the function

A function is tail recursive if it returns the result of the recursive call directly, without doing any extra work after it.


---

### What "does not optimize tail recursion" means?

In some languages like C, **Tail Call Optimization (TCO)** happens:

If a function is tail recursive:
* The compiler reuses the sane stack frame
* No new memory is used for each cell

Result:
* No stack growth
* No recursion limit issue

Python does **not optimize tail recursion**, so iteration is often preferred.

Even if function is tail recursive:

```python
def func(n):
    if n == 0:
        return
    return func(n-1)
```

Python will:
* Create a new stack frame for every call
* Keep all previous calls in memory

Result:
* Stack keeps growing
* Eventually hits recursion limit

---

# 7. Modules & Packages

## Importing Modules

A **module** is a single Python file (`.py`) that contains code such as functions, variables, or classes.

Importing allows you to **reuse code** from other modules.

### How Python Imports Work (Internals)?

When you write:

```python
import math
```

Python:

1. Checks **built-in modules**
2. Checks current directory
3. Searches in `sys.path`
4. Loads module into memory
5. Caches it in `sys.modules`
6. So module is loaded **only once**

### Import Variants

#### 1. Basic Import

```python
import math
print(math.sqrt(16))
```

#### 2. Import Specific Function

```python
from math import sqrt
print(sqrt(16))
```

#### 3. Alias Import

```python
import numpy as np
```

#### 4. Import All (Not Recommended)

```python
from math import *
```

### Best Practices

* Use specific imports
* Avoid `*`
* Use aliases for large libraries

## Creating Modules

Any `.py` file is a module.

Helps in:

* Code organization
* Reusability
* Separation of concerns

### Practical Example

Create file: `utils.py`

```python
def add(a, b):
    return a + b

def greet(name):
    return f"Hello {name}"
```

### Use Module

```python
import utils

print(utils.add(2, 3))
```

### Special Variable: `__name__`

```python
if __name__ == "__main__":
    print("Running directly")
```
Prevents code from executing when imported

## Packages Structure

A **package** is a collection of multiple modules organized in directories.

Used for large-scale applications


### Import from Package

```python
from utils.math_utils import add
```

### Why Packages?

* Organize code logically
* Avoid naming conflicts
* Scalable architecture

---

## **init**.py

`__init__.py` marks a directory as a **Python package**.

### What It Does?

* Initializes package
* Can run setup code
* Controls imports

### Example

```python
# utils/__init__.py

from .math_utils import add
```

Now you can do:

```python
from utils import add
```

### Important

* In modern Python (3.3+), it's optional
* But still recommended for clarity

## External Libraries (pip)

External libraries are packages developed by others and installed using **pip**.

Examples:

* FastAPI
* NumPy
* Requests

### Install Library

```bash
pip install requests
```

### Use Library

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
```

### Dependency Management

```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```

### Best Practices

* Always use virtual environments
* Pin versions in `requirements.txt`
* Avoid global installs

---

# 8. Object-Oriented Programming (OOP)

## Classes & Objects

OOP in Python is based on the concept of **objects representing real-world entities**.

* A **class** defines structure (attributes + methods)
* An **object** is a runtime instance of that class

Python is **object-oriented by design**:

* Everything is an object (even functions, integers, classes)

### Memory Model Insight

```python
class User:
    pass

u1 = User()
```

Internally:

* `User` → class object in memory
* `u1` → instance referencing class + its namespace

### Practical Example

```python
class User:
    def greet(self):
        return "Hello"

u = User()
print(u.greet())
```

## Constructor (`__init__`)

`__init__` is not technically a constructor but an **initializer**.

Actual object creation happens in:

* `__new__()` → allocates memory
* `__init__()` → initializes object

### Example

```python
class User:
    def __init__(self, name):
        self.name = name
```

## Inheritance

Inheritance enables **code reuse** and **hierarchical relationships**.

Python supports:

* Single inheritance
* Multiple inheritance
* Multilevel inheritance

| Type                   | Description                  | Example Structure |
| ---------------------- | ---------------------------- | ----------------- |
| Single Inheritance     | One parent → one child       | `A → B`           |
| Multiple Inheritance   | Multiple parents → one child | `A + B → C`       |
| Multilevel Inheritance | Chain of inheritance         | `A → B → C`       |


### Method Resolution Order (MRO)

Python uses **C3 linearization**:

Defines how methods are resolved?

### Example

```python
class Parent:
    def greet(self):
        print("Hello")

class Child(Parent):
    pass
```

## Multiple Inheritance

A class can inherit from multiple parents.

Problem: **Diamond Problem**

Python solves it using **MRO**

---

### Example

```python
class A:
    def show(self): print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass
```

## Encapsulation

Encapsulation restricts direct access to variables.

Python uses:

* `_protected`
* `__private` (name mangling)

---

### Example

```python
class User:
    def __init__(self):
        self.__password = "secret"
```

## Polymorphism

Same interface → different implementations.

Achieved via:

* **Method overriding**
Method overriding occurs when a child class provides its own implementation of a method that is already defined in its parent class.

This allows the child class to modify or extend the behavior of the inherited method.

```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):  # Overriding parent method
        print("Dog barks")

dog = Dog()
dog.speak()
```

* **Duck Typing**

Duck typing is a concept where the type of an object is determined by its behavior (methods/attributes) rather than its actual class.

"If it looks like a duck and behaves like a duck, it is treated as a duck."

```python
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()

make_sound(Dog())
make_sound(Cat())
```

---

## Abstraction

Abstraction hides implementation details.

Achieved using:

* Abstract base classes (`abc` module)

---

### Example

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

## Magic Methods

Magic methods define **object behavior**.

Examples:

* `__init__` → initialization
* `__str__` → string representation
* `__len__` → length

### Example

```python
class User:
    def __str__(self):
        return "User Object"
```

# 9. Error Handling

## try-except

Handles runtime errors without crashing program.

---

### Example

```python
try:
    x = int("abc")
except ValueError:
    print("Invalid")
```

## Multiple Exceptions

```python
try:
    pass
except (ValueError, TypeError):
    pass
```

## finally

Always executes (used for cleanup)

```python
finally:
    print("Closing resources")
```

---

## raise

Manually trigger exceptions

```python
raise ValueError("Error")
```

## Custom Exceptions

Used for domain-specific errors

```python
class InvalidUserError(Exception):
    pass
```

# 10. File Handling

Files are handled via:

* File descriptor
* Buffering system

---

## Read

```python
with open("file.txt") as f:
    print(f.read())
```

## Write

```python
with open("file.txt", "w") as f:
    f.write("Hello")
```

## JSON

```python
import json
json.dumps({"name": "Ashish"})
```

## CSV

```python
import csv
```

---

# 11. Advanced Concepts

## Generators

Generators are a special type of function that produce values one at a time using yield, instead of returning all values at once.

They are used for lazy evaluation, meaning values are generated only when needed.

Generators produce values lazily.

A normal function:
* Executes completely
* Returns a single value using return

A generator:
* Pauses execution at yield
* Saves its state (local variables, instruction pointer)
* Resumes from where it left off
* Memory efficient

```python
def gen():
    yield 1
```

## Decorators

Decorators are functions that modify or extend the behavior of other functions without changing their actual code.

* Wrap functions to extend behavior.

* Used heavily in FastAPI

```python
def deco(func):
    def wrapper():
        return func()
    return wrapper
```

## Closures

A closure is a function that remembers variables from its enclosing scope, even after that outer function has finished execution.

```python
def outer(x):
    def inner():
        return x
    return inner

func = outer(10)
print(func())
```

## Context Managers

Context managers are used to manage resources automatically, ensuring proper setup and cleanup.

Manages resources automatically (`with`)

```python
with open("file.txt", "r") as f:
    data = f.read()
```

* f is a variable that refers to the opened file object.

Equivalent to:
```python
f = open("file.txt", "r")
try:
    data = f.read()
finally:
    f.close()
```

---

# 12. Standard Library

Python standard library = **batteries included**

This means:

* Python comes with a rich collection of built-in modules
* You do not need external libraries for most common tasks
* It provides ready-to-use solutions for:
  → File handling
  → OS interaction
  → Data processing
  → Functional programming

* `os` → The os module provides a way to interact with the operating system.
→ Acts as a bridge between Python and OS kernel
* `sys` → interpreter  → The sys module provides access to Python runtime and interpreter internals.
* `datetime` → time  → The datetime module is used for working with dates, times, and time intervals.

---

# 13. Dependency Management

Dependency management is the process of handling external libraries/packages required by a project in a controlled, reproducible, and isolated way.

It ensures:

→ Your project runs consistently across environments
→ Dependencies do not conflict with each other
→ Development, testing, and production setups remain stable

## Why Dependency Management is Critical?

→ Without proper management:

→ Different developers may have different versions of libraries
→ Code may work on one machine but fail on another
→ Upgrading one package may break others (dependency conflicts)

→ This is often called: "Works on my machine" problem

* `venv` → isolation → Separate project environments
* `requirements.txt` → reproducibility → Same dependencies everywhere
* `poetry` → modern tool → Lock specific versions

| Feature            | venv         | requirements.txt   | poetry               |
| ------------------ | ------------ | ------------------ | -------------------- |
| Purpose            | Isolation    | Dependency listing | Full management tool |
| Dependency Resolve | No           | No                 | Yes                  |
| Lock File          | No           | No                 | Yes                  |
| Ease of Use        | Simple       | Simple             | Advanced             |
| Best For           | All projects | Small/medium       | Production systems   |

---

# 14. Testing

Ensures correctness.

* Unit testing - testing individual components (smallest units) of code in isolation. (unit = function, method or class). It ensures each piece of code works correctly on it own.
* Integration testing - checks how multiple components work together. Ensures interactions between modules is correct.

---

# 15. Logging & Debugging

Logging = production monitoring - recording what application is doing during execution
Debugging = development analysis - process of finding and fixing bugs in code

---