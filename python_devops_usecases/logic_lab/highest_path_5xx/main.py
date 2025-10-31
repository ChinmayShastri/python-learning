import sys
from modules.highest_path import highest_path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename/path>")
    else:
        filename = sys.argv[1]  # Get the filename from command line arguments
        results = highest_path(filename)  # Call the function to find the path with highest 5xx errors
        if not results:
            print(f"No 5xx error paths found in the file {filename}.")