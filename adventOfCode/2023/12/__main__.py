# https://adventofcode.com/2023/day/12
import os
import re
from functools import cache
from typing import List, Optional, Tuple


def load(test_mode: bool = False, name_override: Optional[str] = None) -> List[str]:
    dirname = os.path.dirname(os.path.abspath(__file__))
    input_file = 'input.txt'
    if test_mode:
        input_file = f"test_{input_file}"
    if name_override:
        input_file = name_override
    with open(os.path.join(dirname, input_file)) as f:
        return f.read().splitlines()


BROKEN = "#"
WORKING = "."
UNKNOWN = "?"

def main_01(gears_records: List[str], unfold: bool = False) -> int:
    total = 0
    for record in gears_records:
        gears, broken = record.split(" ")
        if unfold:
            gears = UNKNOWN.join([gears] * 5)
            broken = ','.join([broken] * 5)
        broken = list(map(int, broken.split(',')))

        positions = compute_positions(gears, broken)
        total += positions

    return total


if __name__ == '__main__':
    test = True
    test = False
    print(f"First Response: {main_01(load(test))}")
    print(f"Second Response: {main_01(load(test), unfold=True)}")
