# Python Advanced Concepts

This repository contains practical examples of three important Python concepts used in production software.

* Decorators
* Generators
* Context Managers

These concepts are widely used in FastAPI, Flask, Django, LangChain, PyTorch, TensorFlow, Pandas, and many other Python libraries.

---

## Folder Structure

```
python-advanced/

decorators/
generators/
context_managers/
```

---

# Decorators

A decorator modifies or extends the behavior of a function without changing its source code.

Syntax

```python
@decorator
def function():
    ...
```

Examples included

* Execution Time Decorator
* Logging Decorator
* Retry Decorator

---

# Generators

Generators produce values one at a time instead of storing everything in memory.

They are ideal for

* Reading huge files
* Processing millions of records
* AI data pipelines
* Streaming APIs

Examples included

* Fibonacci Generator
* File Reader Generator
* Batch Generator

---

# Context Managers

Context managers automatically manage resources.

Common uses

* Opening files
* Database connections
* API sessions
* Locks
* Timers

Examples included

* Custom Context Manager
* Timer Context Manager
* File Context Manager

---

## Learning Goals

After completing this project you should understand

* How decorators work internally
* How generators save memory
* Why context managers prevent resource leaks
* How these concepts are used in production AI applications
