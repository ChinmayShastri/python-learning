# Fibonacci Spiral in ASCII Art
import math

def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    return fib_seq

def draw_fibonacci_spiral(n):
    fib_seq = fibonacci(n)
    grid_size = max(fib_seq) + 2
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    x, y = grid_size // 2, grid_size // 2

    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # Left, Down, Right, Up
    direction_index = 0

    for fib in fib_seq:
        for _ in range(fib):
            grid[y][x] = '*'
            dx, dy = directions[direction_index]
            x, y = x + dx, y + dy

        direction_index = (direction_index + 1) % 4

    for row in grid:
        print(''.join(row))

# Run the program with Fibonacci sequence length
draw_fibonacci_spiral(12)
