# https://adventofcode.com/2023/day/16
import os
from functools import cache
from typing import List, Optional, Tuple, Set


def load(test_mode: bool = False, name_override: Optional[str] = None) -> List[str]:
    dirname = os.path.dirname(os.path.abspath(__file__))
    input_file = 'input.txt'
    if test_mode:
        input_file = f"test_{input_file}"
    if name_override:
        input_file = name_override
    with open(os.path.join(dirname, input_file)) as f:
        return f.read().splitlines()


EMPTY = "."
ENERGIZED = "#"
MIRRORS_VECTOR_FACTOR = {
    "/": -1,
    "\\": 1
}

# Split on non-empty vector's key
SPLITTERS = {
    "-": 0,
    "|": 1
}


def show_grid(grid: List[str], energized: Set[Tuple[int, int]]) -> None:
    showed = ""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            showed += ENERGIZED if (i, j) in energized else EMPTY
        showed += "\n"
    print(showed)


def prepare_beams():
    VISITED_PIPES = set()

    @cache
    def follow_beam(grid: str, start_x: int, start_y: int, vector: Tuple[int, int]) -> Set[Tuple[int, int]]:
        energized = set()
        grid = grid.splitlines()
        x = start_x
        y = start_y
        # print(f"Checking ({x}, {y}) with vector {vector}")

        max_x = len(grid)
        max_y = len(grid[0])
        while 0 <= x < max_x and 0 <= y < max_y:
            energized.add((x, y))
            # show_grid(grid, energized)

            cell = grid[x][y]
            if cell in MIRRORS_VECTOR_FACTOR.keys():
                factor = MIRRORS_VECTOR_FACTOR.get(cell)
                vector = (vector[1] * factor, vector[0] * factor)
            elif cell in SPLITTERS.keys() and vector[SPLITTERS.get(cell)] != 0:
                vector = (vector[1], vector[0])
                if (x, y) not in VISITED_PIPES:
                    VISITED_PIPES.add((x, y))
                    energized = energized.union(
                        follow_beam("\n".join(grid), x + vector[0], y + vector[1], vector)
                    )
                vector = (vector[0] * -1, vector[1] * -1)

            x += vector[0]
            y += vector[1]
        return energized

    return follow_beam


def energized_count(grid: List[str], start_x: int, start_y: int, vector: Tuple[int, int]) -> int:
    energy_count = len(prepare_beams()("\n".join(grid), start_x, start_y, vector))
    # print(f"Followed beams for arguments ({start_x}, {start_y}), {vector}: {energy_count}")
    return energy_count


def main_01(grid: List[str]) -> int:
    return energized_count(grid, 0, 0, (0, 1))


def main_02(grid: List[str]) -> int:
    maxed_energy = 0
    x_max = (len(grid) - 1)
    y_max = (len(grid[0]) - 1)

    # Leftmost + Rightmost
    for i in range(0, x_max + 1):
        maxed_energy = max(maxed_energy, energized_count(grid, i, 0, (0, 1)))
        maxed_energy = max(maxed_energy, energized_count(grid, i, y_max, (0, -1)))

    # Up and Down
    for i in range(0, y_max + 1):
        maxed_energy = max(maxed_energy, energized_count(grid, 0, i, (1, 0)))
        maxed_energy = max(maxed_energy, energized_count(grid, x_max, i, (-1, 0)))

    return maxed_energy


if __name__ == '__main__':
    test = True
    test = False
    print(f"First Response: {main_01(load(test))}")  # 6994
    print(f"Second Response: {main_02(load(test))}")  # 7488
