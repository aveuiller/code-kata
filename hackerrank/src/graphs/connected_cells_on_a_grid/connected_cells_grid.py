# !/bin/python3
from dataclasses import dataclass, field
import os
import sys
from typing import Dict, List, Optional


@dataclass
class CoordinateRange:
    min_x: int
    max_x: int


@dataclass
class Region:
    ranges: List[CoordinateRange] = field(default_factory=list)
    size: int = 0
    child: Optional['Region'] = None

    def matches(self, x):
        for coord_range in self.ranges:
            if coord_range.min_x - 1 <= x <= coord_range.max_x + 1:
                return True
        return False

    def _start_range(self, x):
        self.ranges.append(CoordinateRange(x, x))
        self.size += 1

    def update_range(self, x):
        if not self.ranges or x > self.ranges[-1].max_x + 1:
            self._start_range(x)
        else:
            self.ranges[-1].max_x = x
            self.size += 1


@dataclass
class Matrix:
    """
    # Challenge:
    # https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid
    """
    rows: int
    columns: int
    regions: Dict[int, List[Region]] = field(default_factory=dict)

    def add_row(self, row):
        y = len(self.regions.keys())
        # Anticipate fully empty rows
        self.regions[y] = []
        print(f"Add row n°{y} {row}")

        previous = 0
        current_region = None
        for x, val in enumerate(row):
            if previous == 0 and val == 1:
                matching = [r for r in self.previous_regions(y) if
                            r.matches(x)]
                if matching and len(matching) >= 1:
                    current_region = self.update_region(x, y, matching)
                else:
                    current_region = self.create_region(x, y)
            elif previous == 1 and val == 1:
                current_region.update_range(x)
                matching = [r for r in self.previous_regions(y) if
                            r.matches(x)]
                self._update_child_relationship(current_region, matching)
            else:
                # previous == 1 and val == 0
                # previous == 0 and val == 0
                pass
            previous = val

    def _update_child_relationship(self, current_region, matching):
        for m in matching:
            if m.child is None:
                current_region.size += m.size
                m.child = current_region

    def create_region(self, x, y):
        region = Region()
        region.update_range(x)
        self.regions.get(y, []).append(region)
        return region

    def update_region(self, x, y, matching):
        children = [m.child for m in matching if m.child is not None]
        if children:
            # Should be the same child for connected regions
            region = children[0]
            region.update_range(x)
        else:
            region = self.create_region(x, y)

        self._update_child_relationship(region, matching)
        return region

    def max_region(self):
        for key, value in self.regions.items():
            print(f"lvl n°{key} ({len(value)}): {value}")
        size_max = 0
        for region_levels in self.regions.values():
            size_max = max([size_max] + [r.size for r in region_levels])

        return size_max

    def previous_regions(self, y):
        return self.regions.get(y - 1, [])


# Expected: 5
TEST_GRID_1 = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0]
]
TEST_N_1 = 4
TEST_M_1 = 4

# Expected: 8
TEST_GRID_2 = [
    [1, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0]
]
TEST_N_2 = 4
TEST_M_2 = 5

# Expected: 10
TEST_GRID_3 = [
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0],
]
TEST_N_3 = 5
TEST_M_3 = 5

# Expected: 9
TEST_GRID_4 = [
    [1, 1, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
]
TEST_N_4 = 7
TEST_M_4 = 5


def main():
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input())
    # m = int(input())
    n = TEST_N_4
    m = TEST_M_4
    matrix = Matrix(n, m)

    # for _ in range(n):
    #     matrix.add_row(list(map(int, input().rstrip().split())))

    for row in TEST_GRID_4:
        matrix.add_row(row)

    print(str(matrix.max_region()) + '\n')
    # fptr.write(str(matrix.max_region()) + '\n')
    # fptr.close()


if __name__ == '__main__':
    main()
