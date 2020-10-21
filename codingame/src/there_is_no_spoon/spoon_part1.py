import sys
import math

DEBUG = False

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
input_grid = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    input_grid.append([char for char in line])

if DEBUG:
    print(f"width: {width}; height: {height}", file=sys.stderr, flush=True)
    print(f"Grid: {input_grid}", file=sys.stderr, flush=True)


def delete_node(grid, x, y):
    grid[y][x] = "."

def next_right_node(grid, x, y):
    try:
        line = grid[y]
        if DEBUG:
            print(f"-- Checking line: {line}", file=sys.stderr, flush=True)
        next_x = line.index('0')
    except ValueError:
        return -1, -1
    else:
        return next_x, y

def next_bottom_node(grid, x, y):
    for next_y in range(y, len(grid)):
        if DEBUG:
            print(f"-- Checking for bottom: {x}, {next_y}", file=sys.stderr, flush=True)

        if grid[next_y][x] == "0":
            return x, next_y
    return -1, -1

def main(grid):
    for y, line in enumerate(grid):
        for x, node in enumerate(line):
            if node == "0":
                delete_node(grid, x, y)
                if DEBUG:
                    print(f"Handling: {x}, {y}", file=sys.stderr, flush=True)
                    print(f"New grid: {grid}", file=sys.stderr, flush=True)
                rx, ry = next_right_node(grid, x, y)
                bx, by = next_bottom_node(grid, x, y)
                result = f"{x} {y} {rx} {ry} {bx} {by}"
                if DEBUG:
                    print(f"Result: {result}", file=sys.stderr, flush=True)
                print(result)

main(input_grid)
