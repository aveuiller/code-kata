# https://adventofcode.com/2023/day/20
import os
from functools import cache
from typing import List, Optional, Dict, Tuple, Iterator


def load(test_mode: bool = False, name_override: Optional[str] = None) -> List[str]:
    dirname = os.path.dirname(os.path.abspath(__file__))
    input_file = 'input.txt'
    if test_mode:
        input_file = f"test_{input_file}"
    if name_override:
        input_file = name_override
    with open(os.path.join(dirname, input_file)) as f:
        return f.read().splitlines()


START = "S"
ROCK = "#"
GARDEN = "."
FILLED = "O"


def show(garden_map: List[str], next_spots: List[Tuple[int, int]] = None) -> None:
    showed = ""
    if next_spots is None:
        next_spots = []

    for i, row in enumerate(garden_map):
        for j, cell in enumerate(row):
            if (i, j) in next_spots:
                showed += "O"
            else:
                showed += cell
        showed += "\n"
    print(showed)


@cache
def find_start(garden_map: str) -> Tuple[int, int]:
    for i, row in enumerate(garden_map.split()):
        for j, cell in enumerate(row):
            if cell == START:
                return i, j


@cache
def get_accessible_spots(garden_map: str, start: Tuple[int, int]) -> List[Tuple[int, int]]:
    result = []
    x, y = start
    map_split = garden_map.split()
    split = map_split
    for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
        if map_split[i % len(split)][j % len(split[0])] != ROCK:
            result.append((i, j))
    return result


def main_01(garden_map: List[str], steps: int = 6) -> int:
    garden_map = '\n'.join(garden_map)
    next_spots = [find_start(garden_map)]

    for _ in range(steps):
        # print(f"{len(set(next_spots))} - {set(next_spots)}")
        # show(garden_map, next_spots)

        current_spots = set(next_spots)
        next_spots = []

        for spot in current_spots:
            next_spots += list(get_accessible_spots(garden_map, spot))

    # print(f"{len(set(next_spots))} - {set(next_spots)}")
    # show(garden_map, next_spots)
    return len(set(next_spots))


if __name__ == '__main__':
    test = True
    test = False
    if test:
        assert main_01(load(test), 6) == 16
        print(f"Tests 6 OK")
        assert main_01(load(test), 10) == 50
        print(f"Tests 10 OK")
        assert main_01(load(test), 50) == 1594
        print(f"Tests 50 OK")
        assert main_01(load(test), 100) == 6536
        print(f"Tests 100 OK")
        assert main_01(load(test), 500) == 167004
        print(f"Tests 500 OK")
        assert main_01(load(test), 1000) == 668697
        print(f"Tests 1000 OK")
        assert main_01(load(test), 5000) == 16733044
        print(f"Tests 5000 OK")
        print(f"All tests OK")
    else:
        print(f"First Response: {main_01(load(test), 64)}")  # 3740
        print(f"Second Response: {main_01(load(test), 26501365)}")  #
