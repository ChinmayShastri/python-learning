# In this lab we will count the number of 503 lines in a log file
import sys
import re

def count_error_lines(filename):
    try:
        with open(filename, 'r') as f:
            error_lines = sum(1 for line in f if re.search(r'503', line, re.IGNORECASE))
            return error_lines
    except FileNotFoundError:
        print(f"File you mentioned {filename} not found")
        print(f"Please provide a valid file name or path")
        return None