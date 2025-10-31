#In this lab we will just build a code where we will count the number of lines in a log file
import sys

def count_lines(filename):
    try:
        with open(filename, 'r') as f: #Open the file called filename, 'r' for reading (text mode by default), and call it f inside this block
            total_lines = sum(1 for line in f) #Sum up 1 for each line in the file
        return total_lines #Return the total number of lines
    except FileNotFoundError:
        print(f"File you mentioned {filename} not found")
        return None

