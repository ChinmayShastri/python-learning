import subprocess
def check_service(service):
    result = subprocess.run(["systemctl", "is-active", service], capture_output=True, text=True)
    return result.stdout.strip()

service = ["nginx", "sshd", "docker"]
for service in service:
    print(f"Checking for, {service}")
    print(f"{service} service is", check_service(service))