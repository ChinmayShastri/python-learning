
# 🧪 Python RegEx Function Examples

This document demonstrates practical examples using **Python RegEx functions** with the `re` module.

---

## 📘 1. `re.search()` – Search for a pattern in the string

```python
import re

log = "User root logged in from 10.0.0.5"
match = re.search(r'\d+\.\d+\.\d+\.\d+', log)
if match:
    print("IP Address found:", match.group())
```

**Output:**
```
IP Address found: 10.0.0.5
```

---

## 📘 2. `re.match()` – Match pattern only at the beginning

```python
import re

config = "interface=eth0"
if re.match(r'interface=.*', config):
    print("Valid interface config")
```

**Output:**
```
Valid interface config
```

---

## 📘 3. `re.findall()` – Find all occurrences

```python
import re

text = "nginx/1.18 docker/24.0 git/2.34"
versions = re.findall(r'\d+\.\d+(\.\d+)?', text)
print("Found versions:", versions)
```

**Output:**
```
Found versions: ['1.18', '24.0', '2.34']
```

---

## 📘 4. `re.sub()` – Substitute pattern with a new value

```python
import re

secrets = "password=abc123; token=xyz456"
masked = re.sub(r'=(\w+)', '=****', secrets)
print(masked)
```

**Output:**
```
password=****; token=****
```

---

## 📘 5. `re.split()` – Split string by pattern

```python
import re

env_string = "PATH=/usr/bin;HOME=/root;SHELL=/bin/bash"
env_list = re.split(r';', env_string)
for item in env_list:
    print(item)
```

**Output:**
```
PATH=/usr/bin
HOME=/root
SHELL=/bin/bash
```

---

These function examples are helpful in real-world DevOps scripting, config management, and log processing tasks.
