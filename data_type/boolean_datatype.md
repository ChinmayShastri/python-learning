
# Data Type: Boolean

## What is a Boolean?
A **Boolean** in Python represents one of two values: `True` or `False`. It is commonly used in conditional statements and control flow.

### Key Characteristics:
- Only two possible values: `True` and `False`
- The result of comparison and logical operations
- Used extensively in condition checking

## Creating Booleans
```python
is_deployed = True
has_errors = False
```

## DevOps Use Case Example
Checking whether a deployment was successful:

```python
deployment_status_code = 200
is_successful = deployment_status_code == 200

if is_successful:
    print("Deployment was successful.")
else:
    print("Deployment failed.")
```

## Boolean Expressions
Boolean values are typically the result of comparison or logical operations.

### Comparison Operators
```python
version = "1.2.3"
is_latest = version == "1.2.3"  # True
```

### Logical Operators
```python
is_ready = True
has_capacity = False

if is_ready and has_capacity:
    print("Proceed with deployment")
else:
    print("Conditions not met")
```

## Use Case: Monitoring System Health
```python
cpu_ok = True
memory_ok = True
disk_ok = False

system_healthy = cpu_ok and memory_ok and disk_ok

if not system_healthy:
    print("One or more systems are unhealthy!")
```

## Truthy and Falsy Values
Python evaluates some values as `False` in a boolean context:
- `None`
- `False`
- `0`, `0.0`
- `''`, `[]`, `{}`, `set()`

```python
logs = []

if not logs:
    print("No logs found")
```

## Use Case: Validate Required Configuration
```python
config = {
    "url": "https://example.com",
    "auth_token": None
}

if config["auth_token"]:
    print("Token present, proceeding with API call")
else:
    print("Missing auth token")
```

## Summary
Booleans are critical in DevOps workflows to manage flow control, validate configuration, check service health, and enforce conditions in scripts and automation logic.
