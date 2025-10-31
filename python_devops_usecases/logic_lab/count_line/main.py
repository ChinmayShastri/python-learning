import sys
from moudels.count import count_lines

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename/path>")
    else:
        filename = sys.argv[1] #Get the filename from command line arguments
        total_line = count_lines(filename) #Call the function to count lines
        if total_line is not None:
            print(f"Total number of lines in the file {filename} are {total_line}") #Print the total number of lines
        # else:
        #     print(f"no lines found in the file, {filename} is an empty file")