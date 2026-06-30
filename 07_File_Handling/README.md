# 07 - File Handling

## Overview

File handling allows Python programs to read, write, and manage data stored in files. It is essential for saving application data, processing CSV and JSON files, and handling errors gracefully.

---

## Learning Objectives

By the end of this module, you will be able to:

* Open and close files.
* Read from text files.
* Write and append to files.
* Work with JSON files.
* Read and write CSV files.
* Handle exceptions using `try`, `except`, `else`, and `finally`.

---

# 1. Opening a File

```python
file = open("sample.txt", "r")
```

Common File Modes:

| Mode | Description             |
| ---- | ----------------------- |
| `r`  | Read                    |
| `w`  | Write (overwrites file) |
| `a`  | Append                  |
| `x`  | Create new file         |
| `rb` | Read binary             |
| `wb` | Write binary            |

---

# 2. Reading Files

```python
file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()
```

---

# 3. Writing Files

```python
file = open("sample.txt", "w")

file.write("Hello Python!")

file.close()
```

---

# 4. Appending to Files

```python
file = open("sample.txt", "a")

file.write("\nWelcome!")

file.close()
```

---

# 5. Using the with Statement

Recommended because it automatically closes the file.

```python
with open("sample.txt", "r") as file:
    print(file.read())
```

---

# 6. Working with JSON

```python
import json

employee = {
    "name": "Shirley",
    "role": "AI Engineer"
}

with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)
```

Reading JSON:

```python
import json

with open("employee.json", "r") as file:
    data = json.load(file)

print(data)
```

---

# 7. Working with CSV

Writing CSV:

```python
import csv

with open("employees.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Role"])

    writer.writerow(["Shirley", "AI Engineer"])
```

Reading CSV:

```python
import csv

with open("employees.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)
```

---

# 8. Exception Handling

```python
try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Invalid input")
```

---

# 9. Multiple Exceptions

```python
try:
    file = open("demo.txt")
    number = int(input())

except FileNotFoundError:
    print("File not found")

except ValueError:
    print("Invalid number")
```

---

# 10. finally Block

```python
try:
    print("Working...")

finally:
    print("Cleanup completed")
```

---


# Mini Project: Notes Manager

Build a command-line Notes Manager that allows users to:

* Add notes
* View notes
* Delete notes
* Save notes in a text file
* Handle missing files gracefully using exceptions

---

# Summary

In this module, you learned:

* File Reading
* File Writing
* File Appending
* JSON
* CSV
* Exception Handling
* Context Managers (`with`)
