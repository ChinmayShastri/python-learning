import re
import pandas as pd
import sys

def parse_log_line(line: str):
    """
    Extracts path and status code from a typical log line.
    Works with formats like:
    127.0.0.1 - - [06/Oct/2025:08:00:01 +0000] "GET /api/v1/users HTTP/1.1" 503 232 "-" "curl/7.64.1"
    """
    # Regex for HTTP method, path, and status code
    pattern = r'\"[A-Z]+\s(?P<path>\/[^\s]*)[^\"]*\"\s(?P<status>\d{3})'
    match = re.search(pattern, line)
    
    if match:
        return {
            "path": match.group("path"),
            "status_code": int(match.group("status"))
        }
    return None


def load_log_data(file_path: str) -> pd.DataFrame:
    """
    Reads a .log file line by line and extracts path + status_code.
    Returns a pandas DataFrame.
    """
    records = []
    with open(file_path, "r") as f:
        for line in f:
            parsed = parse_log_line(line)
            if parsed:
                records.append(parsed)

    if not records:
        raise ValueError("No valid log entries found. Please check log format.")

    df = pd.DataFrame(records)
    return df


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m modules.log_parser <path_to_logfile>")
        sys.exit(1)

    log_file = sys.argv[1]
    df = load_log_data(log_file)
    print(df.head())
