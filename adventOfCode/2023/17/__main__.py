# https://adventofcode.com/2023/day/16
import heapq
import os
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


class Grid:
    def __init__(self, grid_map: List[str],
                 consecutive_steps_lower_limit: int = 0,
                 consecutive_steps_upper_limit: int = 3):
        self.x_max = len(grid_map)
        self.y_max = len(grid_map[0])
        self.grid = grid_map
        self.consecutive_steps_lower_limit = consecutive_steps_lower_limit
        self.consecutive_steps_upper_limit = consecutive_steps_upper_limit

    def get_heat(self, x, y):
        return int(self.grid[x][y])

    def is_inside(self, x, y):
        return (0 <= x < self.x_max) and (0 <= y < self.y_max)

    @property
    def last_cell(self) -> Tuple[int, int]:
        return self.x_max - 1, self.y_max - 1

    def show(self, visited: Set['Path'], paths: List['Path'] = None) -> None:
        showed = ""
        if paths is None:
            paths = []

        for i in range(self.x_max):
            for j in range(self.y_max):
                if (i, j) in (path.position for path in paths):
                    showed += "O"
                else:
                    showed += '#' if (i, j) in (v.position for v in visited) else '.'
            showed += "\n"
        print(showed)


class Path:
    def __init__(self, grid: Grid, start: Tuple[int, int], vector: Tuple[int, int], heat: int, sequence: int):
        self.grid = grid
        self.position = start
        self.vector = vector
        self.heat = heat
        self.sequence = sequence

    def hops(self) -> List['Path']:
        vectors = []

        if self.sequence > self.grid.consecutive_steps_lower_limit:
            vectors += [
                (self.vector[1], self.vector[0]),
                (self.vector[1] * -1, self.vector[0] * -1)
            ]

        if self.sequence < self.grid.consecutive_steps_upper_limit:
            vectors.append(self.vector)
        nexts = []
        for vector in vectors:
            next_position = tuple(pos + vec for pos, vec in zip(self.position, vector))
            if self.grid.is_inside(*next_position):
                nexts.append(
                    Path(
                        self.grid,
                        next_position,
                        vector,
                        self.heat + self.grid.get_heat(*next_position),
                        self.sequence + 1 if vector == self.vector else 1
                    )
                )
        return nexts

    @property
    def distance_score(self) -> int:
        return self.heat

    def __hash__(self):
        return hash(f'{self.position}:{self.vector}:{self.vector}')

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __lt__(self, other):
        return self.distance_score < other.distance_score

    def __str__(self):
        return f"Path: {self.position} -> {self.vector}, {self.heat}, {self.sequence}"


def search(grid_map: List[str], start_x, start_y,
           consecutive_steps_lower_limit: int = 0,
           consecutive_steps_upper_limit: int = 3) -> int:
    grid = Grid(grid_map, consecutive_steps_lower_limit, consecutive_steps_upper_limit)
    paths: List[Path] = [
        Path(grid, (start_x, start_y), (0, 1), 0, 1),
        Path(grid, (start_x, start_y), (1, 0), 0, 1),
    ]

    visited = set()
    while paths:
        # print(f"Remaining paths: {len(paths)}")
        path = heapq.heappop(paths)

        # print(f"Checking {path} - Cost: {path.distance_score}")
        if path in visited:
            continue

        if path.position == grid.last_cell and path.sequence >= grid.consecutive_steps_lower_limit:
            # grid.show(visited)
            return path.heat
        else:
            for hop in path.hops():
                heapq.heappush(paths, hop)

        visited.add(path)

    return -1


def main_01(grid: List[str]) -> int:
    return search(grid, 0, 0)


def main_02(grid: List[str]) -> int:
    return search(grid, 0, 0,
                  consecutive_steps_lower_limit=4,
                  consecutive_steps_upper_limit=10)


if __name__ == '__main__':
    test = True
    test = False
    print(f"First Response: {main_01(load(test))}")  # 1004
    print(f"Second Response: {main_02(load(test))}")  # 1171
