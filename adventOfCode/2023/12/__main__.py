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


@cache
def is_possible(spring: str, size: int) -> bool:
    pattern = r"^[#|\?]{" + str(size) + "}" + r"(\?|$)"
    return re.match(pattern, spring) is not None


@cache
def count_placements(springs: Tuple[str], broken_counts: Tuple[int]) -> int:
    if not broken_counts:
        return 1 if all(spring.replace("?", "") == "" for spring in springs) else 0
    if not springs:
        return 0

    first_spring = springs[0]
    remaining_springs = springs[1:]
    if not first_spring:
        return count_placements(remaining_springs, broken_counts)

    if first_spring[0] == BROKEN:
        return (
            count_placements((first_spring[broken_counts[0] + 1:],) + remaining_springs, broken_counts[1:])
            if is_possible(first_spring, broken_counts[0])
            else 0
        )
    res_when_empty = count_placements((first_spring[1:],) + remaining_springs, broken_counts)
    res_when_broken = count_placements((f"#{first_spring[1:]}",) + remaining_springs, broken_counts)
    return res_when_empty + res_when_broken


def compute_positions(gears: str, broken_counts: List[int]) -> int:
    broken_groups = gears.split('.')
    return count_placements(tuple(broken_groups), tuple(broken_counts))


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
