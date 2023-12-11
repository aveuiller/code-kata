# https://adventofcode.com/2023/day/10
import os, re, math
from typing import List, Optional
from functools import reduce


def load(test_mode: bool = False, name_override: Optional[str] = None) -> List[str]:
    dirname = os.path.dirname(os.path.abspath(__file__))
    input_file = 'input.txt'
    if test_mode:
        input_file = f"test_{input_file}"
    if name_override:
        input_file = name_override
    with open(os.path.join(dirname, input_file)) as f:
        return f.readlines()


# x, y
# --> y
# |
# v
# x
# Change axis, direction vector
DIRECTIONS = {
    "|": (0, 1),
    "-": (0, 1),
    "L": (1, 1),
    "J": (1, -1),
    "7": (1, 1),
    "F": (1, -1)
}
START = "S"
GROUND = "."
KEEP_DIR = ['|-']


def check_direction(current_pipe, dir_x, dir_y):
    assert (
        (dir_x == 1 and current_pipe in "|LJ") or (dir_x == -1 and current_pipe in "|7F")
        or (dir_y == 1  and current_pipe in "-7J") or (dir_y == -1  and current_pipe in "-LF") 
    )


def print_map(pipe_map: dict) -> None:
    print('- ' + ' '.join([str(i) for i in range(len(pipe_map[0]))]))
    print(' \n'.join((' '.join(str(i) + line) for i, line in enumerate(pipe_map))))



def main_01(pipe_map: List[str], return_count=False) -> int:
    visited = []

    x, y = 0, 0
    for i, line in enumerate(pipe_map):
        pipe_map[i] = line.replace("\n", "")
        try:
            j = line.index(START)
            x, y = (i, j)
            visited.append((x, y))
        except ValueError:
            pass

    # print_map(pipe_map)

    prev_x = None
    prev_y = None
    for new_x, new_y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        in_bound = 0 < x + new_x < len(pipe_map) and 0 < y + new_y < len(pipe_map[0])
        if in_bound and pipe_map[x + new_x][y + new_y] != GROUND:
            new_pipe = pipe_map[x + new_x][y + new_y]
            if (
                (new_x == 1 and new_pipe in "|LJ") or (new_x == -1 and new_pipe in "|7F")
                or (new_y == 1  and new_pipe in "-7J") or (new_y == -1  and new_pipe in "-LF") 
            ):
                prev_x, prev_y = x, y
                x += new_x
                y += new_y
                dir_x = x - prev_x
                dir_y = y - prev_y
                break

    assert prev_x is not None and prev_y is not None, "Unable to find start position"
    # print(f'Starting at ({x, y}) - from ({prev_x, prev_y})')
    current_pipe = pipe_map[x][y]
    loop_size = 0
    while current_pipe != START:
        loop_size += 1
        visited.append((x, y))
        # print(f"Position: ({x, y}) - pos: {loop_size} - {current_pipe} - vector: ({dir_x, dir_y})")
        if current_pipe not in KEEP_DIR:
            check_direction(current_pipe, dir_x, dir_y)
            change_direction, vector = DIRECTIONS.get(current_pipe)
            dir_x = (x - prev_x) * vector
            dir_y = (y - prev_y) * vector
            if change_direction:
                dir_x, dir_y = dir_y, dir_x

        prev_x = x
        prev_y = y
        x += dir_x
        y += dir_y
        current_pipe = pipe_map[x][y]
    
    if return_count:
        grid = [
            [
                '.' if (x, y) not in visited else pipe_map[x][y] for y in range(len(pipe_map[x]))
            ] for x in range(len(pipe_map))
        ]

        interior = 0
        for row in grid:
            for i, char in enumerate(row):
                if char == GROUND:
                    intersect = 0
                    corner_pipes = []
                    for j in range(i + 1, len(row)):
                        if row[j] in "|":
                            intersect += 1
                        if row[j] in "FL":
                            corner_pipes.append(row[j])
                        if len(corner_pipes) != 0 and row[j] == "J" and corner_pipes[-1] == "F" or row[j] == "7" and corner_pipes[-1] == "L":
                            corner_pipes.pop(-1)
                            intersect += 1

                    if intersect % 2 == 1:
                        interior += 1
        return interior
    else:
        return math.ceil(loop_size / 2)


if __name__ == '__main__':
    test = True
    test = False
    print(f"First Response: {main_01(load(test))}")
    if test:
        print(f"Second Response: {main_01(load(test, name_override='test_input_2.txt'))}")
        print(f"Second Response: {main_01(load(test, name_override='test_input_3.txt'))}")
        print(f"Second Response: {main_01(load(test, name_override='test_input_4.txt'))}")
    print(f"Second Response: {main_01(load(test), return_count=True)}")
