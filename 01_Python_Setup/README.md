# 01 - Python Setup

## Overview

Before writing Python programs, we need to set up a development environment. This section covers Python installation, IDE configuration, running Python scripts, and using the Python REPL.

---

## Learning Objectives

By the end of this module, you will be able to:

* Install Python on your system.
* Verify Python installation.
* Configure VS Code or PyCharm for Python development.
* Run Python programs from the command line and IDE.
* Use the Python REPL for interactive coding.

---

## 1. Installing Python

### Download Python

Visit the official Python website:

https://www.python.org/downloads/

Download the latest stable version for your operating system.

### Verify Installation

Open a terminal and run:

```bash
python --version
```

or

```bash
python3 --version
```

Example Output:

```text
Python 3.13.0
```

---

## 2. Setting Up VS Code

### Install VS Code

Download VS Code from:

https://code.visualstudio.com/

### Install Python Extension

1. Open VS Code
2. Navigate to Extensions
3. Search for "Python"
4. Install the Microsoft Python Extension

### Select Python Interpreter

Press:

```text
Ctrl + Shift + P
```

Search:

```text
Python: Select Interpreter
```

Choose your installed Python version.

---

## 3. Setting Up PyCharm

### Install PyCharm

Download from:

https://www.jetbrains.com/pycharm/

### Create a New Project

1. Open PyCharm
2. Click New Project
3. Select Python Interpreter
4. Create Project

---

## 4. Creating Your First Python Program

Create a file named:

```text
hello.py
```

Add the following code:

```python
print("Hello, Python!")
```

---

## 5. Running Python Scripts

### From Terminal

Navigate to the file location:

```bash
python hello.py
```

Output:

```text
Hello, Python!
```

### From VS Code

* Open the file
* Click Run ▶
* View output in terminal

### From PyCharm

* Right-click the file
* Select Run

---

## 6. Python REPL

REPL stands for:

```text
Read
Evaluate
Print
Loop
```

Start REPL:

```bash
python
```

Example:

```python
>>> 10 + 5
15

>>> print("Welcome")
Welcome
```

Exit REPL:

```python
>>> exit()
```

---

## 7. Useful Commands

Check Python Version:

```bash
python --version
```

Locate Python Installation:

```bash
where python
```

(Mac/Linux)

```bash
which python
```

Check Installed Packages:

```bash
pip list
```

Install Package:

```bash
pip install requests
```

---

## Common Issues

### Python Not Found

Error:

```text
'python' is not recognized
```

Solution:

* Reinstall Python
* Enable "Add Python to PATH" during installation

### pip Not Found

Run:

```bash
python -m pip --version
```

---

## Practice Exercises

### Exercise 1

Verify your Python installation.

### Exercise 2

Create a file named:

```text
welcome.py
```

Print your name and profession.

### Exercise 3

Use the Python REPL to calculate:

```python
25 * 4
100 / 5
10 + 20
```

---

## Summary

In this module, you learned:

* How to install Python
* How to configure VS Code and PyCharm
* How to run Python scripts
* How to use the Python REPL
* Basic Python development workflow

Next Module → **02_Variables_DataTypes_Operators**
