
# 🧩 Python Functions – Real Examples

A **function** in Python is a block of reusable code that performs a specific task. Functions improve code modularity, readability, and reuse — crucial in automation and DevOps scripting.

---

## 🧱 Basic Function Syntax

```python
def greet(name):
    return f"Hello, {name}!"
```

Call it like this:

```python
print(greet("Admin"))
```

**Output:**
```
Hello, Admin!
```

---

## 🔧 Real-World DevOps Examples

### 1️⃣ Check Service Status

```python
import subprocess

def check_service_status(service):
    result = subprocess.run(["systemctl", "is-active", service], capture_output=True, text=True)
    return result.stdout.strip()

print("Docker status:", check_service_status("docker"))
```

**Output:**
```
Docker status: active
```

---

### 2️⃣ Create a Backup File

```python
import shutil

def backup_file(src, dest):
    shutil.copy(src, dest)
    print(f"Backup created at {dest}")

backup_file("/etc/nginx/nginx.conf", "/tmp/nginx_backup.conf")
```

**Output:**
```
Backup created at /tmp/nginx_backup.conf
```

---

### 3️⃣ Check Disk Usage

```python
import shutil

def get_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)
    return {
        "total": f"{total // (2**30)} GB",
        "used": f"{used // (2**30)} GB",
        "free": f"{free // (2**30)} GB"
    }

usage = get_disk_usage()
print("Disk Usage:", usage)
```

**Output (example):**
```
Disk Usage: {'total': '100 GB', 'used': '30 GB', 'free': '70 GB'}
```

---

### 4️⃣ Log a Message with Timestamp

```python
from datetime import datetime

def log_message(msg):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{time}] {msg}")

log_message("Deployment started")
```

**Output:**
```
[2025-07-31 10:00:00] Deployment started
```

---

## ✅ Summary

| Feature         | Benefit                             |
|----------------|-------------------------------------|
| Reusability     | Write once, use anywhere            |
| Modularity      | Break complex tasks into functions  |
| Maintainability | Easier to update and debug          |

Functions are at the core of writing clean, maintainable, and automated scripts in DevOps.

