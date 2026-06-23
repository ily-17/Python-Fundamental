# 06 - OOP Advanced

## Overview

Object-Oriented Programming becomes more powerful with concepts like inheritance, polymorphism, and encapsulation. These concepts help build scalable, reusable, and maintainable software systems.

---

## Learning Objectives

By the end of this module, you will be able to:

* Understand inheritance.
* Reuse code through parent-child relationships.
* Implement polymorphism.
* Protect data using encapsulation.
* Build real-world OOP applications.

---

# 1. Inheritance

Inheritance allows a class to inherit attributes and methods from another class.

## Parent Class

```python
class Animal:

    def speak(self):
        print("Animal makes a sound")
```

## Child Class

```python
class Dog(Animal):
    pass
```

## Usage

```python
dog = Dog()
dog.speak()
```

Output:

```text
Animal makes a sound
```

---

# 2. Method Overriding

A child class can provide its own implementation.

```python
class Animal:

    def speak(self):
        print("Animal sound")


class Dog(Animal):

    def speak(self):
        print("Bark")
```

Usage:

```python
dog = Dog()
dog.speak()
```

Output:

```text
Bark
```

---

# 3. Polymorphism

Polymorphism means "many forms".

Different objects can respond to the same method call differently.

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")
```

Usage:

```python
animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

Output:

```text
Bark
Meow
```

---

# 4. Encapsulation

Encapsulation hides internal data and exposes controlled access.

## Private Attributes

Use double underscore (`__`).

```python
class BankAccount:

    def __init__(self):
        self.__balance = 0
```

Direct access:

```python
account = BankAccount()

# account.__balance
```

Produces:

```text
AttributeError
```

---

# 5. Getter Methods

```python
class BankAccount:

    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return self.__balance
```

---

# 6. Setter Methods

```python
class BankAccount:

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount
```

Usage:

```python
account = BankAccount()

account.deposit(1000)

print(account.get_balance())
```

Output:

```text
1000
```

---

# Real-World Example

```python
class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):

    def start(self):
        print("Car Started")


class Bike(Vehicle):

    def start(self):
        print("Bike Started")
```

Usage:

```python
vehicles = [Car(), Bike()]

for vehicle in vehicles:
    vehicle.start()
```

Output:

```text
Car Started
Bike Started
```

---

# Practice Exercises

### Exercise 1

Create:

```python
Animal
Dog
Cat
```

Use inheritance.

---

### Exercise 2

Override a method in a child class.

---

### Exercise 3

Demonstrate polymorphism using:

```python
Car
Bike
Truck
```

---

### Exercise 4

Create a BankAccount class with:

* deposit()
* withdraw()
* get_balance()

---

### Exercise 5

Create:

```python
Employee
Manager
Developer
```

using inheritance.

---

# Mini Project: Banking System

Build a banking system that supports:

* Create account
* Deposit money
* Withdraw money
* View balance

Requirements:

* Use encapsulation for balance.
* Use inheritance for account types.
* Use methods for operations.

---

# Summary

In this module, you learned:

* Inheritance
* Method Overriding
* Polymorphism
* Encapsulation
* Private Attributes
* Getter and Setter Methods

Next Module → **07_File_Handling**
