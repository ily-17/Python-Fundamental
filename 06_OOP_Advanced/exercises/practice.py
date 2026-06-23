"""
Practice: OOP II
Inheritance, Polymorphism, Encapsulation
"""

# ==========================================
# Exercise 1: Vehicle Hierarchy
# ==========================================

# Create a base class Vehicle
#
# Method:
# start()

# Create child classes:
# Car
# Bike
# Truck
#
# Override start() in each class.

# Example Output:
# Car Started
# Bike Started
# Truck Started


# ==========================================
# Exercise 2: Shape Hierarchy
# ==========================================

# Create a base class Shape
#
# Method:
# area()

# Create child classes:
# Rectangle
# Circle

# Override area() in each class.

# Rectangle:
# length = 10
# width = 5

# Circle:
# radius = 7

# Print calculated areas.


# ==========================================
# Exercise 3: Polymorphism
# ==========================================

# Store Car, Bike, and Truck
# objects inside a list.

# Loop through the list and call start().

# Example:
#
# vehicles = [Car(), Bike(), Truck()]
#
# for vehicle in vehicles:
#     vehicle.start()


# ==========================================
# Exercise 4: Bank Account
# ==========================================

# Create BankAccount class
#
# Private Variable:
# __balance

# Methods:
# deposit()
# withdraw()
# get_balance()

# Test:
#
# Deposit 5000
# Withdraw 1000
# Print balance


# ==========================================
# Exercise 5: Employee Hierarchy
# ==========================================

# Parent:
# Employee

# Child:
# Manager
# Developer

# Method:
# work()

# Override work() in child classes.

# Example Output:
#
# Manager manages team
# Developer writes code


# ==========================================
# Exercise 6: Animal Hierarchy
# ==========================================

# Parent:
# Animal

# Child:
# Dog
# Cat

# Method:
# sound()

# Demonstrate polymorphism using a list
# of animals.


# ==========================================
# Bonus Challenge
# ==========================================

# Create:
#
# Shape
# Rectangle
# Circle
# Triangle
#
# Store all shapes in a list.
#
# Loop through them and calculate area().
#
# This demonstrates true polymorphism.
