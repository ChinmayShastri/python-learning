import os
import re
import sys

def find_errors(log_file, limit=10):
    errors = []
    if not os.path.exists(log_file):
        print(f"[ERROR] Log file not found: {log_file}")
        return []

    with open(log_file, "r") as f:
        for line in f:
            if re.search(r'ERROR', line, re.IGNORECASE):
                errors.append(line.strip())

    print(f"\n✅ Total errors found: {len(errors)}")

    if errors:
        print(f"\nShowing first {min(limit, len(errors))} errors:\n")
        for e in errors[:limit]:
            print(e)

    return errors

if __name__ == "__main__":
    # Take log file from CLI, else default to /var/log/syslog
    log_file = sys.argv[1] if len(sys.argv) > 1 else "/var/log/syslog"
    find_errors(log_file)

#python custom_log_analyzer.py /path/to/the/app.log