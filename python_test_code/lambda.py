containers = [
    {"name": "nginx", "mem": 512},
    {"name": "redis", "mem": 128},
    {"name": "db", "mem": 2048},
    {"name": "api", "mem": 1024},
]

# Sort by memory (descending)
top_containers = sorted(containers, key=lambda c: c["mem"], reverse=True) [:3]
for c in top_containers:
    print(c)