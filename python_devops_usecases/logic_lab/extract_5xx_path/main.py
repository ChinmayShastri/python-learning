import sys
from moudels.paths import log_file


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename/path>")
    else:
        filename = sys.argv[1]  # Get the filename from command line arguments
        results = log_file(filename)  # Call the function to extract paths leading to 5xx errors
        if not results:
            print(f"No 5xx error paths found in the file {filename}.")