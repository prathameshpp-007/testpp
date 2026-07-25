# Python Programming Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Variables and Data Types](#variables-and-data-types)
3. [Control Flow](#control-flow)
4. [Functions](#functions)
5. [Lists and Dictionaries](#lists-and-dictionaries)
6. [File Handling](#file-handling)

## Introduction

Python is a versatile, high-level programming language known for its simplicity and readability. It supports multiple programming paradigms including procedural, object-oriented, and functional programming.

```python
print("Hello, Python!")
```

## Variables and Data Types

Python supports various data types:

- **Strings**: `name = "Alice"`
- **Integers**: `age = 25`
- **Floats**: `height = 5.9`
- **Booleans**: `is_active = True`
- **Lists**: `numbers = [1, 2, 3, 4, 5]`
- **Dictionaries**: `person = {"name": "Bob", "age": 30}`

```python
x = 10
y = 20
total = x + y
print(f"Total: {total}")
```

## Control Flow

### If-Else Statements

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")
```

### Loops

**For Loop:**
```python
for i in range(5):
    print(f"Iteration {i}")
```

**While Loop:**
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## Functions

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))
```

## Lists and Dictionaries

### Working with Lists

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits)

# List comprehension
squares = [x**2 for x in range(5)]
print(squares)
```

### Working with Dictionaries

```python
student = {
    "name": "Charlie",
    "age": 22,
    "courses": ["Math", "Science"]
}

print(student["name"])
student["gpa"] = 3.8
```

## File Handling

```python
# Writing to a file
with open("data.txt", "w") as file:
    file.write("Python is awesome!")

# Reading from a file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

## Tips and Best Practices

- Use meaningful variable names
- Follow PEP 8 style guidelines
- Use comments to explain complex logic
- Test your code regularly
- Use virtual environments for projects

---

**Happy Coding!** 🐍