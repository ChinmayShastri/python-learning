# from datetime import datetime

# time = datetime.date().strftime("%Y-%m-%d %H:%M:%S")
# print(time)

from datetime import datetime

def log_message(message):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{time}] {message}")

log_message("Deployment started.")