# 03 - Conditionals & Loops

## Overview

Conditionals allow programs to make decisions based on conditions, while loops allow repetitive execution of code blocks.

These concepts are fundamental for building dynamic and intelligent applications.

---

## Learning Objectives

By the end of this module, you will be able to:

* Use if, elif, and else statements.
* Write nested conditional statements.
* Use for loops and while loops.
* Control loop execution using break and continue.
* Solve real-world problems using conditionals and loops.

---

# 1. Conditional Statements

## if Statement

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

---

## if-else Statement

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## if-elif-else Statement

```python
score = 85

if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("Fail")
```

---

## Nested if

```python
age = 25
salary = 50000

if age >= 18:
    if salary >= 30000:
        print("Loan Approved")
```

---

# 2. Logical Operators in Conditions

```python
age = 25
salary = 50000

if age > 18 and salary > 30000:
    print("Eligible")
```

```python
if age < 18 or salary > 30000:
    print("Condition Met")
```

```python
if not age < 18:
    print("Adult")
```

---

# 3. For Loops

A for loop iterates over a sequence.

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

---

## Loop Through List

```python
skills = ["Python", "Java", "SQL"]

for skill in skills:
    print(skill)
```

---

# 4. While Loops

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# 5. break Statement

Stops loop execution.

```python
for i in range(10):
    if i == 5:
        break

    print(i)
```

---

# 6. continue Statement

Skips current iteration.

```python
for i in range(5):

    if i == 2:
        continue

    print(i)
```

---

# 7. Nested Loops

```python
for row in range(3):
    for col in range(3):
        print(row, col)
```

---

# 8. Loop Else

```python
for i in range(3):
    print(i)
else:
    print("Loop completed")
```

---

# Common Errors

## IndentationError

```python
if True:
print("Hello")
```

Correct:

```python
if True:
    print("Hello")
```

---

# Practice Exercises

### Exercise 1

Check whether a person is eligible to vote.

### Exercise 2

Print numbers from 1 to 10 using a for loop.

### Exercise 3

Print even numbers from 1 to 20.

### Exercise 4

Use a while loop to print numbers from 10 to 1.

### Exercise 5

Print multiplication table of 5.

---

# Summary

In this module, you learned:

* if statements
* if-else statements
* elif statements
* Nested conditions
* for loops
* while loops
* break
* continue
* Nested loops

Next Module → **04_Functions**
