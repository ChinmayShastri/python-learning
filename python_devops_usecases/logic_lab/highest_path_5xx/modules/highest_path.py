#This code will give with path has highest number of 5xx errors

import re 
from collections import Counter

def highest_path(logfile):
    path_counter = Counter()
    try:
        with open(logfile, 'r') as f:
            for line in f:
                # Example log snippet: "GET /some/path HTTP/1.1" 502
                match = re.search(r'"[A-Z]+\s(.*?)\sHTTP/[0-9.]+"\s+(\d{3})', line)
                if match:
                    path, status = match.groups()
                    status = int(status)
                    if 500 <= status < 600:
                        path_counter[path] += 1 #path_counter[path] += 1, here we are counting the number of times each path has 5xx errors

        if not path_counter:
            print("No 5xx errors found in the log file.")
            return None
        
        # Find the path with the highest number of 5xx errors
        # path_counter.most_common(1), here 1 means we want the top 1 most common element
        highest_path, highest_count = path_counter.most_common(1)[0] 
        print(f"Path with highest 5xx errors: {highest_path} (Count: {highest_count})")

        highest_3_paths = path_counter.most_common(3) # path_counter.most_common(3), here 3 means we want the top 3 most common elements
        print("Top 3 paths with highest 5xx errors:")
        for path, count in highest_3_paths:
            print(f"Path: {path}, Total {count} 5xx Errors")
        return highest_path, highest_count
    except FileNotFoundError:
        print(f"File {logfile} not found.")
        print("Please provide a valid log file.")
        return None