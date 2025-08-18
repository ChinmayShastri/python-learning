
# 📦 Python Modules – Practical Guide

A **module** in Python is simply a file containing Python definitions, functions, or classes. Modules help organize code into separate files, making it **reusable, maintainable, and scalable** — vital for DevOps automation scripts.

---

## 🧱 Creating and Using a Module

### 1️⃣ Create a file called `utils.py`:

```
# utils.py
def greet(name):
    return f"Hello, {name}!"
```

### 2️⃣ Use the module in another file:

```
# main.py
import utils

print(utils.greet("Admin"))
```

**Output:**
```
Hello, Admin!
```

---

## 🔧 Built-in Modules Examples (Real Use Cases)

### 1️⃣ Using `os` for Environment Management

```
import os

print("Current working directory:", os.getcwd())
print("Environment PATH:", os.getenv("PATH"))
```

**Example Output:**
```
Current working directory: /home/user
Environment PATH: /usr/local/bin:/usr/bin:/bin
```

---

### 2️⃣ Using `subprocess` to Check Service Status

```
import subprocess

def check_service(service):
    result = subprocess.run(["systemctl", "is-active", service], capture_output=True, text=True)
    return result.stdout.strip()

print("Nginx service is", check_service("nginx"))
```

**Example Output:**
```
Nginx service is active
```

---

### 3️⃣ Using `shutil` to Create Backups

```
import shutil

def backup_file(src, dest):
    shutil.copy(src, dest)
    print(f"Backup created: {dest}")

backup_file("/etc/hosts", "/tmp/hosts_backup")
```

**Example Output:**
```
Backup created: /tmp/hosts_backup
```

---

### 4️⃣ Using `datetime` for Logging

```
from datetime import datetime

def log_message(message):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{time}] {message}")

log_message("Deployment started.")
```

**Example Output:**
```
[2025-08-06 10:30:00] Deployment started.
```

---

## 🛠️ DevOps Use Case: Custom Monitoring Module

### `monitor.py`:
```
import shutil
import psutil  # third-party module (pip install psutil)

def check_disk(path="/"):
    total, used, free = shutil.disk_usage(path)
    return f"Disk Usage: {used // (2**30)}GB used out of {total // (2**30)}GB"

def check_cpu():
    return f"CPU Usage: {psutil.cpu_percent()}%"
```

### `main.py`:
```
import monitor

print(monitor.check_disk())
print(monitor.check_cpu())
```

**Example Output:**
```
Disk Usage: 30GB used out of 100GB
CPU Usage: 15.2%
```

---

## ✅ Summary

- **Modules** break code into separate files for better organization.
- Use **built-in modules** for tasks like file handling, logging, or system commands.
- Create **custom modules** for reusable scripts across multiple projects.
