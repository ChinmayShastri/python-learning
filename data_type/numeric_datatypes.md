
# 🔢 Python Numeric Data Types:-

In Python, **numeric data types** are used to store numbers. Python supports three main types of numeric data:

1. **int** – Integer numbers (e.g., -10, 0, 23)
2. **float** – Floating point (decimal) numbers (e.g., 3.14, -0.001)
3. **complex** – Complex numbers (e.g., 2 + 3j)

---

## 🧠 1. `int` – Integer
- Whole numbers, both positive and negative, without decimals.

```python
a = 10
b = -5
print(a + b)
```

**Output:**
```
5
```

---

## 🧠 2. `float` – Floating Point Number
- Numbers with decimal places.

```python
pi = 3.14159
radius = 2.5
area = pi * (radius ** 2)
print(area)
```

**Output:**
```
19.6349375
```

---

## 🧠 3. `complex` – Complex Numbers
- Numbers in the form `a + bj`, where `a` is the real part and `b` is the imaginary part.

```python
z = 2 + 3j
print(z.real)     # Real part
print(z.imag)     # Imaginary part
```

**Output:**
```
2.0
3.0
```

---

## 🧪 Additional Examples

### Example 1: Integer Division and Modulus
```python
a = 10
b = 3
print(a // b)  # Integer division
print(a % b)   # Remainder
```

**Output:**
```
3
1
```

---

### Example 2: Type Checking
```python
x = 42
y = 3.14
z = 2 + 5j

print(type(x))
print(type(y))
print(type(z))
```

**Output:**
```
<class 'int'>
<class 'float'>
<class 'complex'>
```

---

### Example 3: Converting Between Types
```python
a = 5
b = float(a)
c = int(3.9)

print(b)
print(c)
```

**Output:**
```
5.0
3
```

---

## ✅ Summary

| Type     | Description                   | Example      |
|----------|-------------------------------|--------------|
| `int`    | Integer numbers                | `42`, `-7`   |
| `float`  | Decimal numbers                | `3.14`, `0.0`|
| `complex`| Complex numbers (real + imag)  | `2 + 3j`     |

---

Next, we’ll dive into **String Data Types**. Stay tuned! ✨
