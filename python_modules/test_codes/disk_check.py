import shutil
from datetime import datetime
import sys

# get disk usage for root filesystem
path = sys.argv[1] if len(sys.argv) > 1 else "/"
usage = shutil.disk_usage(path)
# setting time
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

total_gb = usage.total / (1024 ** 3)
used_gb  = usage.used  / (1024 ** 3)
free_gb  = usage.free  / (1024 ** 3)
percent_used = (usage.used / usage.total) * 100

# print(f"Total: {total_gb:.2f} GB")
# print(f"Used : {used_gb:.2f} GB")
# print(f"Free : {free_gb:.2f} GB")
# print(f"Used percentage: {percent_used:.2f}%")

# With open will open the file and will add the log in disk_check.log file
# append mode, auto-closes after block
with open("disk_check.log", "a") as f:   # append mode, auto-closes after block
    if percent_used >= 18:
        f.write(f"{timestamp} Disk utilised {percent_used:.2f}%, Clean up is required.\n")
    else:
        f.write(f"{timestamp} Disk utilisation is: {percent_used:.2f}%, We are safe.\n")