
# 🔁 Python `return` Statement

The `return` statement in Python is used to exit a function and optionally pass back a value to the caller. It's an essential concept when creating **reusable functions**, especially in automation and scripting — common in DevOps tasks.

---

## 📘 Basic Usage

```python
def greet():
    return "Hello, World!"

message = greet()
print(message)
```

**Output:**
```
Hello, World!
```

---

## 📦 Returning Multiple Values

```python
def get_credentials():
    return "admin", "password123"

user, pwd = get_credentials()
print("User:", user)
print("Password:", pwd)
```

**Output:**
```
User: admin
Password: password123
```

---

## 🚫 Using `return` Without Value

```python
def log_message():
    print("This runs a task and logs it.")
    return

log_message()
```

**Output:**
```
This runs a task and logs it.
```

---

## 🧪 DevOps Use Case 1: Return Status from a Script

```python
def check_service_status():
    status = "running"
    return status

result = check_service_status()
print("Service is", result)
```

**Output:**
```
Service is running
```

---

## 🧪 DevOps Use Case 2: Get Disk Space and Return

```python
def get_disk_space():
    used = "15GB"
    free = "85GB"
    return used, free

used_space, free_space = get_disk_space()
print("Used:", used_space)
print("Free:", free_space)
```

**Output:**
```
Used: 15GB
Free: 85GB
```

---

## ⚠️ Return Ends Function Execution

Once a `return` is hit, the function stops running.

```python
def example():
    print("Before return")
    return
    print("After return")  # This won't execute

example()
```

**Output:**
```
Before return
```

---

## ✅ Summary

| Feature             | Description                                 |
|---------------------|---------------------------------------------|
| `return value`      | Sends a result back from a function         |
| `return`            | Exits the function without returning a value|
| Multiple return     | Returns tuples of values                    |
| Ends execution      | No code runs after `return` inside function |

---

Using `return` makes your code **modular, reusable**, and **easier to test** — all essential practices in automation and scripting workflows.
