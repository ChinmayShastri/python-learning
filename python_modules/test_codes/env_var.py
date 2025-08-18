import os
import json

des_file = "env_backup.json"
print(f"Writing all Environment Variables to: {des_file}")

# Convert os.environ (which is a mapping) into a real Python dictionary using dict()
env_vars = dict(os.environ)

# Write as JSON, The json module lets you write Python objects into a JSON file.
with open(des_file, "w") as f:
    json.dump(env_vars, f, indent=4) #Format it nicely with 4 spaces indentation.

print(f"Environment variables saved to {des_file}")