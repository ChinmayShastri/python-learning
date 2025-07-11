
# 🧵 Python String Data Type

In Python, a **string** is a sequence of characters enclosed in single quotes `' '`, double quotes `" "`, or triple quotes `''' '''` / `""" """`.

Strings are **immutable**, meaning once created, they cannot be changed — operations on strings return new strings.

---

## 🔤 Creating Strings

```python
s1 = "Hello"
s2 = 'Python'
s3 = '''This is
a multiline string'''
print(s1)
print(s2)
print(s3)
```

**Output:**
```
Hello
Python
This is
a multiline string
```

---

## ⚒️ Common String Methods and Built-in Functions

### 1. `.upper()` – Convert to uppercase
```python
text = "hello"
print(text.upper())
```
**Output:**
```
HELLO
```

---

### 2. `.lower()` – Convert to lowercase
```python
text = "HELLO"
print(text.lower())
```
**Output:**
```
hello
```

---

### 3. `.replace(old, new)` – Replace substring
```python
text = "I like Python"
print(text.replace("like", "love"))
```
**Output:**
```
I love Python
```

---

### 4. `.split(separator)` – Split string into list
```python
text = "apple,banana,cherry"
print(text.split(","))
```
**Output:**
```
['apple', 'banana', 'cherry']
```

---

### 5. `.strip()` – Remove leading/trailing whitespaces
```python
text = "  Hello World  "
print(text.strip())
```
**Output:**
```
Hello World
```

---

### 6. `len()` – Get the length of a string
```python
text = "Python"
print(len(text))
```
**Output:**
```
6
```

---

### 7. `.find(substring)` – Find index of first occurrence
```python
text = "I love Python"
print(text.find("Python"))
```
**Output:**
```
7
```

---

### 8. `.count(substring)` – Count occurrences
```python
text = "banana"
print(text.count("a"))
```
**Output:**
```
3
```

---

### 9. `.startswith()` / `.endswith()`
```python
url = "https://openai.com"
print(url.startswith("https"))
print(url.endswith(".com"))
```
**Output:**
```
True
True
```

---

### 10. String Concatenation
```python
first = "Hello"
second = "World"
print(first + " " + second)
```
**Output:**
```
Hello World
```

---

## 🧠 String Indexing and Slicing

### Indexing
```python
text = "Python"
print(text[0])   # First character
print(text[-1])  # Last character
```

**Output:**
```
P
n
```

### Slicing
```python
text = "Python Programming"
print(text[0:6])   # From index 0 to 5
print(text[7:])    # From index 7 to end
```

**Output:**
```
Python
Programming
```

---

## ✅ Summary of Common String Methods

| Method          | Description                              |
|-----------------|------------------------------------------|
| `upper()`       | Convert to uppercase                     |
| `lower()`       | Convert to lowercase                     |
| `replace()`     | Replace a substring                      |
| `split()`       | Split string into list                   |
| `strip()`       | Remove whitespace                        |
| `len()`         | Get length of string                     |
| `find()`        | Find index of a substring                |
| `count()`       | Count occurrences of a substring         |
| `startswith()`  | Check if string starts with a substring  |
| `endswith()`    | Check if string ends with a substring    |

---

Strings are powerful and heavily used in every Python program. Mastering them is key to handling text and data efficiently!
