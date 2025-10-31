"""Extract paths that lead to 5xx errors from a given log file.
The function returns a list of (path, status) tuples and also prints them.
"""
import re
def log_file(filename):
    results = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                # Example log snippet: "GET /some/path HTTP/1.1" 502
                # Capture the path and the status code
                match = re.search(r'"[A-Z]+\s(.*?)\sHTTP/[0-9.]+"\s+(\d{3})', line)
                if match:
                    path, status = match.groups()
                    status = int(status)
                    if 500 <= status < 600:
                        results.append((path, status))
        # Print results for CLI usage
        for path, status in results:
            print(f"Path: {path}, Status: {status}")
        return results
    except FileNotFoundError:
        print(f"File {filename} not found.")
        print("Please provide a valid log file.")
        return []