
# 🔍 Python Regular Expressions (RegEx)

**Regular Expressions (RegEx)** are sequences of characters used to match patterns in text. Python provides the `re` module to work with regular expressions.

In DevOps, RegEx is extremely useful for parsing logs, validating config files, extracting data from command outputs, and automating text manipulations.

---

## 📦 Importing the `re` Module

```python
import re
```

---

## 🧰 Common RegEx Functions in Python

| Function           | Description                                |
|--------------------|--------------------------------------------|
| `re.search()`      | Searches for a match in the string         |
| `re.match()`       | Checks for a match at the beginning        |
| `re.findall()`     | Returns all matches as a list              |
| `re.sub()`         | Substitutes matched pattern with a string  |
| `re.split()`       | Splits string by the matched pattern       |

---

## 📘 Useful RegEx Patterns

| Pattern     | Matches                          |
|-------------|----------------------------------|
| `.`         | Any character except newline     |
| `\d`        | Digit (0–9)                      |
| `\D`        | Non-digit                        |
| `\w`        | Word character                   |
| `\W`        | Non-word character               |
| `\s`        | Whitespace                       |
| `^`         | Start of string                  |
| `$`         | End of string                    |
| `[]`        | Any character inside brackets    |
| `|`         | OR operator                      |
| `*`, `+`, `?`, `{}` | Repetition qualifiers    |

---

## 🔧 DevOps Use Cases with RegEx

### Example 1: Extracting IP Addresses from Logs

```python
import re

log = "Accepted connection from 192.168.1.10 on port 22"
ip = re.search(r'\d+\.\d+\.\d+\.\d+', log)
print(ip.group())
```

**Output:**
```
192.168.1.10
```

---

### Example 2: Validating a Linux Username

```python
username = "admin_user01"
if re.match(r'^[a-z_][a-z0-9_-]{0,31}$', username):
    print("Valid username")
else:
    print("Invalid username")
```

**Output:**
```
Valid username
```

---

### Example 3: Masking Secrets in Configuration Files

```python
config = "password=MySecret123"
masked = re.sub(r'password=.*', 'password=******', config)
print(masked)
```

**Output:**
```
password=******
```

---

### Example 4: Finding All Installed Versions

```python
output = "nginx/1.18.0 docker/24.0.5 git/2.34.1"
versions = re.findall(r'\d+\.\d+(\.\d+)?', output)
print(versions)
```

**Output:**
```
['1.18.0', '24.0.5', '2.34.1']
```

---

### Example 5: Splitting Environment Variables

```python
env = "PATH=/usr/bin;HOME=/home/user;SHELL=/bin/bash"
env_vars = re.split(r';', env)
for var in env_vars:
    print(var)
```

**Output:**
```
PATH=/usr/bin
HOME=/home/user
SHELL=/bin/bash
```

---

## ✅ Summary

- Use `re.search()` and `re.findall()` to extract patterns.
- Use `re.sub()` to sanitize or modify configuration data.
- Use RegEx to validate syntax like usernames, IPs, domains, emails, etc.
- Essential for log parsing and CI/CD automation scripting.

---

**Regular expressions are a DevOps engineer's best friend** for automating analysis and processing of textual data across logs, configs, and CLI tools.
