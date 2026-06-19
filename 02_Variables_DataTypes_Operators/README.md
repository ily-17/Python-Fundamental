# 02 - Variables, Data Types & Operators

## Overview

Variables are used to store data in memory. Python provides several built-in data types and operators that allow developers to perform calculations, comparisons, and logical operations.

Understanding variables, data types, and operators is fundamental to writing Python programs.

---

## Learning Objectives

By the end of this module, you will be able to:

* Create and use variables.
* Understand Python data types.
* Convert between data types.
* Use arithmetic, comparison, logical, and assignment operators.
* Write expressions and evaluate results.

---

# 1. Variables

A variable is a named storage location used to hold data.

## Syntax

```python
name = "John"
age = 25
salary = 50000
```

## Example

```python
name = "Shirley"
role = "AI Engineer"

print(name)
print(role)
```

Output:

```text
Shirley
AI Engineer
```

---

# 2. Variable Naming Rules

### Valid Names

```python
name = "John"
user_age = 25
salary2025 = 10000
```

### Invalid Names

```python
2name = "John"
user-age = 25
class = "Python"
```

Rules:

* Must start with a letter or underscore (_)
* Cannot start with a number
* Cannot contain spaces
* Cannot use Python keywords

---

# 3. Data Types

Python provides several built-in data types.

## Integer (int)

```python
age = 25
```

## Float

```python
salary = 50000.75
```

## String (str)

```python
name = "Shirley"
```

## Boolean (bool)

```python
is_active = True
```

## List

```python
skills = ["Python", "Java", "SQL"]
```

## Tuple

```python
coordinates = (10, 20)
```

## Set

```python
numbers = {1, 2, 3}
```

## Dictionary

```python
employee = {
    "name": "Shirley",
    "role": "AI Engineer"
}
```

---

# 4. Checking Data Types

Use type() to determine a variable's data type.

```python
name = "Python"

print(type(name))
```

Output:

```text
<class 'str'>
```

---

# 5. Type Conversion

## Integer to String

```python
age = 25

print(str(age))
```

## String to Integer

```python
number = "100"

print(int(number))
```

## Integer to Float

```python
value = 50

print(float(value))
```

---

# 6. Operators

Operators are used to perform operations on variables and values.

---

## Arithmetic Operators

| Operator | Description    | Example |
| -------- | -------------- | ------- |
| +        | Addition       | 5 + 3   |
| -        | Subtraction    | 5 - 3   |
| *        | Multiplication | 5 * 3   |
| /        | Division       | 5 / 3   |
| //       | Floor Division | 5 // 3  |
| %        | Modulus        | 5 % 3   |
| **       | Exponent       | 5 ** 2  |

### Example

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

---

## Comparison Operators

| Operator | Meaning               |
| -------- | --------------------- |
| ==       | Equal                 |
| !=       | Not Equal             |
| >        | Greater Than          |
| <        | Less Than             |
| >=       | Greater Than or Equal |
| <=       | Less Than or Equal    |

### Example

```python
age = 18

print(age >= 18)
```

Output:

```text
True
```

---

## Logical Operators

| Operator | Meaning              |
| -------- | -------------------- |
| and      | Both conditions true |
| or       | Any condition true   |
| not      | Reverse condition    |

### Example

```python
age = 25
salary = 50000

print(age > 18 and salary > 30000)
```

Output:

```text
True
```

---

## Assignment Operators

```python
x = 10

x += 5
x -= 2
x *= 3
```

---

# 7. String Operations

## Concatenation

```python
first_name = "Shirley"
last_name = "Deborah"

print(first_name + " " + last_name)
```

## Repetition

```python
print("Python " * 3)
```

---

# 8. Multiple Variable Assignment

```python
x, y, z = 10, 20, 30

print(x)
print(y)
print(z)
```

---

# 9. Constants

Python does not support true constants.

Convention:

```python
PI = 3.14159
MAX_USERS = 100
```

Use uppercase names to indicate constants.

---

# Common Errors

## NameError

```python
print(name)
```

If variable is not defined:

```text
NameError: name 'name' is not defined
```

---

## TypeError

```python
age = 25

print(age + " years")
```

Fix:

```python
print(str(age) + " years")
```

---

# Practice Exercises

### Exercise 1

Create variables for:

* Name
* Age
* Profession

Print them.

### Exercise 2

Calculate:

```python
25 + 10
50 - 20
8 * 7
100 / 5
```

### Exercise 3

Check whether:

```python
age = 18
```

is greater than or equal to 18.

### Exercise 4

Convert:

```python
"500"
```

into an integer.

### Exercise 5

Create a dictionary representing an employee.

---

# Summary

In this module, you learned:

* Variables
* Data Types
* Type Conversion
* Arithmetic Operators
* Comparison Operators
* Logical Operators
* Assignment Operators
* String Operations

Next Module → **03_Conditionals_Loops**
