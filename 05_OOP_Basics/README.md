# 05 - Object-Oriented Programming (OOP) Basics

## Overview

Object-Oriented Programming (OOP) is a programming paradigm that organizes code using classes and objects. It helps create reusable, maintainable, and scalable applications.

Python supports OOP through classes, objects, attributes, and methods.

---

## Learning Objectives

By the end of this module, you will be able to:

* Understand OOP concepts.
* Create classes and objects.
* Define attributes and methods.
* Use constructors (`__init__`).
* Build simple real-world models using classes.

---

# 1. What is a Class?

A class is a blueprint for creating objects.

Example:

```python
class Employee:
    pass
```

---

# 2. What is an Object?

An object is an instance of a class.

```python
class Employee:
    pass

emp1 = Employee()
emp2 = Employee()
```

---

# 3. Attributes

Attributes store information about an object.

```python
class Employee:

    def __init__(self):
        self.name = "Shirley"
        self.role = "AI Engineer"
```

---

# 4. The **init** Constructor

The `__init__()` method runs automatically when an object is created.

```python
class Employee:

    def __init__(self, name, role):
        self.name = name
        self.role = role
```

Create object:

```python
emp = Employee("Shirley", "AI Engineer")
```

---

# 5. Accessing Attributes

```python
print(emp.name)
print(emp.role)
```

Output:

```text
Shirley
AI Engineer
```

---

# 6. Methods

Methods define object behavior.

```python
class Employee:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")
```

Usage:

```python
emp = Employee("Shirley")
emp.greet()
```

Output:

```text
Hello, I am Shirley
```

---

# 7. self Keyword

`self` refers to the current object instance.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Every object gets its own value for `self.name`.

---

# 8. Multiple Objects

```python
class Student:

    def __init__(self, name):
        self.name = name

student1 = Student("John")
student2 = Student("Mary")

print(student1.name)
print(student2.name)
```

Output:

```text
John
Mary
```

---

# Real-World Example

```python
class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} started")
```

Usage:

```python
car = Car("Toyota", "Camry")
car.start()
```

---

# Practice Exercises

### Exercise 1

Create a Student class with:

* name
* age

### Exercise 2

Create an Employee class with:

* name
* salary

### Exercise 3

Create a Car class with:

* brand
* model
* start() method

### Exercise 4

Create multiple objects from the same class.

### Exercise 5

Create a Book class with:

* title
* author
* display_details() method

---

# Summary

In this module, you learned:

* Classes
* Objects
* Attributes
* Methods
* self keyword
* **init** constructor

Next Module → **06_OOP_Advanced**
