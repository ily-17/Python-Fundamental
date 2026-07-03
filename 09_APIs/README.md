# 09 - APIs I (HTTP, Requests & REST)

## Overview

Application Programming Interfaces (APIs) allow applications to communicate and exchange data. Most modern applications interact with REST APIs using HTTP requests and JSON responses.

In this module, you'll learn how to send HTTP requests, consume REST APIs, and parse JSON data using Python's `requests` library.

---

# Learning Objectives

By the end of this module, you will be able to:

- Understand what an API is.
- Learn HTTP methods (GET, POST, PUT, DELETE).
- Use the requests library.
- Parse JSON responses.
- Handle API errors.
- Build applications using public APIs.

---

# 1. What is an API?

An API (Application Programming Interface) allows two applications to communicate.

Example:

```
Python Program
      │
      ▼
 REST API
      │
      ▼
 JSON Response
```

---

# 2. HTTP Methods

| Method | Purpose |
|---------|---------|
| GET | Retrieve data |
| POST | Create data |
| PUT | Update data |
| PATCH | Partially update data |
| DELETE | Delete data |

---

# 3. Installing Requests

```bash
pip install requests
```

---

# 4. Sending a GET Request

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

print(response.status_code)
```

---

# 5. Parsing JSON

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

data = response.json()

print(data[0]["name"])
```

---

# 6. HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
| 500 | Server Error |

---

# 7. Handling Errors

```python
import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    response.raise_for_status()

    print(response.json())

except requests.exceptions.RequestException as e:
    print("Request Failed:", e)
```

---

# Practice Exercises

### Exercise 1

Call the JSONPlaceholder Users API and print all user names.

### Exercise 2

Call the Random Joke API and print the joke.

### Exercise 3

Call the Cat Facts API and print one random fact.

### Exercise 4

Handle HTTP errors using try-except.

---

# Mini Project

Build an API Dashboard that allows users to:

- View weather information
- View users from a REST API
- Get a random joke

---

# Summary

In this module, you learned:

- APIs
- HTTP Methods
- REST APIs
- Requests Library
- JSON Parsing
- Error Handling
