import sys
from moudels.count_503 import count_error_lines

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename/path>")
    else:
        filename = sys.argv[1] #Get the filename from command line arguments
        total_error_lines = count_error_lines(filename) #Call the function to count error lines
        if total_error_lines is not None:
            print(f"Total number of 503 lines in the file {filename} are {total_error_lines}") #Print the total number of error lines
        # else:
        #     print(f"no error lines found in the file, {filename} is an empty file")