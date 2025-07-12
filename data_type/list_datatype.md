
# 📋 Python List Data Type

A **list** in Python is an ordered, mutable (changeable) collection of items. Lists can hold elements of any data type, including other lists.

Lists are one of the most commonly used data structures in Python — especially in tasks like automation, configuration parsing, and scripting in DevOps.

---

## 🧱 Creating a List

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)
```

**Output:**
```
['apple', 'banana', 'cherry']
```

---

## 🧰 Common List Operations

### 1. Accessing Elements
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])      # First element
print(fruits[-1])     # Last element
```

**Output:**
```
apple
cherry
```

---

### 2. Modifying Elements
```python
fruits[1] = "blueberry"
print(fruits)
```

**Output:**
```
['apple', 'blueberry', 'cherry']
```

---

### 3. Adding Elements
```python
fruits.append("date")
fruits.insert(1, "kiwi")
print(fruits)
```

**Output:**
```
['apple', 'kiwi', 'blueberry', 'cherry', 'date']
```

---

### 4. Removing Elements
```python
fruits.remove("cherry")
popped = fruits.pop()
print(fruits)
print("Removed:", popped)
```

**Output:**
```
['apple', 'kiwi', 'blueberry']
Removed: date
```

---

### 5. Slicing Lists
```python
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[2:5])   # From index 2 to 4
```

**Output:**
```
[2, 3, 4]
```

---

### 6. Iterating Over a List
```python
servers = ["web01", "web02", "db01"]
for server in servers:
    print("Pinging:", server)
```

**Output:**
```
Pinging: web01
Pinging: web02
Pinging: db01
```

---

## 🔧 DevOps Use Cases with Lists

### Example 1: Generating Server Inventory
```python
servers = ["web01", "web02", "db01"]
for server in servers:
    print(f"Connecting to {server}...")
```

**Output:**
```
Connecting to web01...
Connecting to web02...
Connecting to db01...
```

---

### Example 2: Parsing Package Versions
```python
packages = ["nginx:1.18", "docker:24.0", "git:2.34"]
for pkg in packages:
    name, version = pkg.split(":")
    print(f"Package: {name}, Version: {version}")
```

**Output:**
```
Package: nginx, Version: 1.18
Package: docker, Version: 24.0
Package: git, Version: 2.34
```

---

### Example 3: Filtering Failed Services
```python
services = ["nginx:running", "mysql:stopped", "docker:running"]
failed = [s for s in services if "stopped" in s]
print("Failed services:", failed)
```

**Output:**
```
Failed services: ['mysql:stopped']
```

---

### Example 4: Creating Ansible Inventory List
```python
hosts = ["web01", "web02", "db01"]
inventory = "[webservers]\n" + "\n".join(hosts[:2])
print(inventory)
```

**Output:**
```
[webservers]
web01
web02
```

---

## ✅ Summary of List Methods

| Method           | Description                                |
|------------------|--------------------------------------------|
| `append(item)`   | Add an item to the end                     |
| `insert(i, item)`| Insert item at specific index              |
| `remove(item)`   | Remove first occurrence of item            |
| `pop()`          | Remove and return last item                |
| `len(list)`      | Return number of items                     |
| `sort()`         | Sort the list in-place                     |
| `reverse()`      | Reverse the list in-place                  |
| `clear()`        | Remove all items from the list             |

---

Lists are essential in automation and DevOps tasks for processing sequences of items such as servers, services, logs, or packages. Knowing how to manipulate lists allows you to write efficient scripts and tools.
