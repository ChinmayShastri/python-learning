
# Data Type: Dictionary

## What is a Dictionary?
A **dictionary** in Python is an unordered collection of key-value pairs. Each key is unique and maps to a specific value.

### Key Characteristics:
- Unordered (as of Python 3.6+, insertion order is preserved)
- Mutable
- Keys must be immutable
- Values can be of any data type

## Creating Dictionaries
```python
# Using curly braces
tool_versions = {"Ansible": "2.9", "Docker": "20.10", "Kubernetes": "1.21"}

# Using dict() constructor
tool_versions = dict(Ansible="2.9", Docker="20.10", Kubernetes="1.21")
```

## DevOps Use Case Example
Tracking the current version of tools in your CI/CD pipeline:

```python
tools = {
    "Docker": "20.10.8",
    "Terraform": "1.0.3",
    "Kubernetes": "1.21.1"
}

print(f"Docker version: {tools['Docker']}")
```

## Common Dictionary Operations

### Accessing Values
```python
docker_version = tools["Docker"]
```

### Adding or Updating Entries
```python
tools["Helm"] = "3.5.4"
tools["Docker"] = "20.10.9"  # update
```

### Removing Entries
```python
del tools["Terraform"]
tools.pop("Helm")
```

### Iterating Through Dictionary
```python
for tool, version in tools.items():
    print(f"{tool} - {version}")
```

### Check for Key Existence
```python
if "Kubernetes" in tools:
    print("Kubernetes is configured")
```

## Use Case: Environment Configuration
```python
env_config = {
    "dev": {"url": "dev.example.com", "replicas": 1},
    "prod": {"url": "prod.example.com", "replicas": 3}
}

# Access production config
print(env_config["prod"]["url"])
```

## Dictionary Comprehension
```python
# Convert list of tools into a dict with default version
tool_list = ["Docker", "Helm", "Ansible"]
default_versions = {tool: "latest" for tool in tool_list}
```

## Merging Dictionaries (Python 3.9+)
```python
a = {"Docker": "20.10"}
b = {"Terraform": "1.2.3"}
combined = a | b
```

## Summary
Dictionaries are essential for structured data storage and retrieval in DevOps, such as storing configuration data, mapping environments to settings, or tracking tool versions in infrastructure scripts.
