# 04 - Functions

## Overview

Functions are reusable blocks of code that perform specific tasks. They help organize code, reduce duplication, and improve maintainability.

Functions are one of the most important concepts in Python programming.

---

## Learning Objectives

By the end of this module, you will be able to:

* Create and call functions.
* Pass arguments to functions.
* Return values from functions.
* Use default parameters.
* Work with `*args` and `**kwargs`.
* Understand local and global scope.
* Use lambda functions.

---

# 1. Creating Functions

## Syntax

```python
def function_name():
    print("Hello Python")
```

## Example

```python
def greet():
    print("Welcome to Python")

greet()
```

Output:

```text
Welcome to Python
```

---

# 2. Function Parameters

```python
def greet(name):
    print("Hello", name)

greet("Shirley")
```

Output:

```text
Hello Shirley
```

---

# 3. Multiple Parameters

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Output:

```text
30
```

---

# 4. Return Values

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

---

# 5. Default Parameters

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Shirley")
```

Output:

```text
Hello Guest
Hello Shirley
```

---

# 6. Keyword Arguments

```python
def employee(name, role):
    print(name, role)

employee(role="AI Engineer", name="Shirley")
```

---

# 7. *args

Allows multiple positional arguments.

```python
def add_numbers(*args):
    print(sum(args))

add_numbers(10, 20, 30)
```

Output:

```text
60
```

---

# 8. **kwargs

Allows multiple keyword arguments.

```python
def display_info(**kwargs):

    for key, value in kwargs.items():
        print(key, ":", value)

display_info(
    name="Shirley",
    role="AI Engineer"
)
```

---

# 9. Variable Scope

## Local Scope

```python
def demo():
    x = 100
    print(x)

demo()
```

---

## Global Scope

```python
name = "Python"

def show():
    print(name)

show()
```

---

# 10. Lambda Functions

Anonymous one-line functions.

```python
square = lambda x: x * x

print(square(5))
```

Output:

```text
25
```

---

# 11. Recursive Functions

A function calling itself.

```python
def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

Output:

```text
120
```

---

# Common Errors

## Missing Arguments

```python
def add(a, b):
    return a + b

add(10)
```

Error:

```text
TypeError: missing required positional argument
```

---

# Practice Exercises

### Exercise 1

Create a function that prints your name.

### Exercise 2

Create a function that adds two numbers.

### Exercise 3

Create a function that returns the square of a number.

### Exercise 4

Create a function using `*args`.

### Exercise 5

Create a function using `**kwargs`.

### Exercise 6

Create a recursive factorial function.

---

# Summary

In this module, you learned:

* Function creation
* Parameters
* Return values
* Default arguments
* Keyword arguments
* *args
* **kwargs
* Variable scope
* Lambda functions
* Recursion

Next Module → **05_OOP_Basics**
