
# Topic: Variables – Local and Global

## What is a Variable?
A **variable** in Python is a named reference to a value. Variables can be defined within different scopes, which affects their accessibility.

## Scope of Variables
- **Local Variable**: Defined inside a function and accessible only within that function.
- **Global Variable**: Defined outside all functions and accessible throughout the program.

## Local Variables
```python
def configure_server():
    config_path = "/etc/server/config.yml"  # local variable
    print("Config path:", config_path)

configure_server()
# print(config_path)  # Error: NameError
```

## Global Variables
```python
deployment_env = "production"  # global variable

def print_env():
    print("Deploying to:", deployment_env)

print_env()
```

## Modifying Global Variables
To modify a global variable inside a function, use the `global` keyword.

```python
build_count = 0

def trigger_build():
    global build_count
    build_count += 1

trigger_build()
print("Total builds triggered:", build_count)
```

## DevOps Use Case: Shared Deployment Settings
```python
# Global config used across multiple functions
deploy_config = {"env": "staging", "replicas": 3}

def update_env(new_env):
    global deploy_config
    deploy_config["env"] = new_env

def show_config():
    print(deploy_config)

update_env("production")
show_config()
```

## Best Practices
- Avoid overusing global variables; they make code harder to maintain and test.
- Use function parameters and return values to pass data where possible.
- Encapsulate logic in classes or modules for better structure.

## Use Case: Local Logging in a Scripted Pipeline
```python
def run_step(step_name):
    log_message = f"Running step: {step_name}"  # local variable
    print(log_message)

run_step("Install dependencies")
```

## Use Case: Global Debug Mode
```python
debug_mode = True

def log(msg):
    if debug_mode:
        print("[DEBUG]", msg)

log("Starting deployment process...")
```

## Summary
Understanding the difference between local and global variables helps manage state correctly in automation scripts. Use local variables for temporary data and global variables sparingly for shared configuration or state.
