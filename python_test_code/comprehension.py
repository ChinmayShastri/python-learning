ip = ["10.0.0.2", "10.0.5.2", "192.168.5.2", "172.32.50.2", "10.0.0.6"]

web_subnet = [ip for ip in ip if ip.startswith("10.0.")]

print("The server in web_subnet are:", web_subnet)

servers = [
    {"name": "web1", "status": "running"},
    {"name": "web2", "status": "running"},
    {"name": "web3", "status": "running"},
    {"name": "web4", "status": "error"},
    {"name": "web5", "status": "stopped"},
]

running_status = [server["name"] for server in servers if server["status"] == "running"]

print("The running servers are:", running_status)