# 08 - Virtual Environments, pip, Project Structure & Modules

## Overview

As Python projects grow, it becomes important to organize code into reusable modules, manage dependencies, and isolate project environments. This module introduces virtual environments, pip, project structure, and Python modules.

---

## Learning Objectives

By the end of this module, you will be able to:

- Create and activate virtual environments.
- Install and manage packages using pip.
- Understand Python project structure.
- Create and import custom modules.
- Package code into reusable modules.

---

# 1. Virtual Environments

A virtual environment is an isolated Python environment for a project.

## Create

```bash
python -m venv venv
```

## Activate

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Deactivate

```bash
deactivate
```

---

# 2. pip

Install packages

```bash
pip install requests
```

List installed packages

```bash
pip list
```

Upgrade package

```bash
pip install --upgrade requests
```

Uninstall package

```bash
pip uninstall requests
```

Export dependencies

```bash
pip freeze > requirements.txt
```

Install from requirements.txt

```bash
pip install -r requirements.txt
```

---

# 3. Python Project Structure

Example:

```text
my_project/
│
├── main.py
├── requirements.txt
├── README.md
│
├── calculator/
│   ├── __init__.py
│   ├── operations.py
│   └── utils.py
│
└── tests/
```

---

# 4. Python Modules

A module is simply a Python file.

Example:

operations.py

```python
def add(a, b):
    return a + b
```

main.py

```python
from operations import add

print(add(10, 20))
```

---

# 5. Packages

A package is a folder containing an __init__.py file.

Example:

calculator/

```
calculator/
│
├── __init__.py
├── operations.py
└── utils.py
```

Import package

```python
from calculator.operations import add
```

---

# 6. requirements.txt

Example

```
requests==2.32.0
pandas==2.2.2
numpy==2.0.1
```

---



# Mini Project

Package a Calculator application into reusable modules.

Project structure:

```text
calculator_package/
│
├── main.py
├── calculator/
│   ├── __init__.py
│   ├── operations.py
│   └── utils.py
└── requirements.txt
```

---

# Summary

In this module, you learned:

- Virtual Environments
- pip
- requirements.txt
- Project Structure
- Modules
- Packages
