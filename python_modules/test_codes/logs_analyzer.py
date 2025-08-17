import os
import re

log_file = "/path/to/the/error.log"   # change this path to your log file

if os.path.exists(log_file):
    f = open(log_file, "r")   # open the file
    lines = f.readlines()     # read all lines into a list
    f.close()                 # close the file

    errors = []
    for line in lines:
        if re.search(r'ERROR', line, re.IGNORECASE):   # case-sensitive match
            errors.append(line.strip())

    # print results
    for e in errors:
        print(e)

    print("\nTotal errors found:", len(errors))
else:
    print("Log file not found:", log_file)