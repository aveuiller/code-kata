# https://adventofcode.com/2023/day/11
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
        return f.read().splitlines()


def distance(a: tuple, b: tuple) -> int:
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def expanded_column(galaxies_map: List[str], galaxy_position: int, expanded_mapping: dict[int, int], expansion_factor: int = 1) -> int:
    if cached := expanded_mapping.get(galaxy_position):
        return cached

    new_position = galaxy_position
    for i in range(galaxy_position):
        empty = True
        for line in galaxies_map:
            if line[i] != ".":
                empty = False
        if empty:
            new_position += expansion_factor
    # print(f"Position Mapping: {galaxy_position} - {new_position}")
    expanded_mapping[galaxy_position] = new_position
    return new_position


def main_01(galaxies_map: List[str], expansion_factor: int = 1) -> int:
    galaxy_regex = re.compile(r"(#)")
    total = 0
    galaxies = []
    j = 0
    expanded_mapping = {}

    for i in range(len(galaxies_map)):
        line = galaxies_map[i]
        for galaxy_match in re.finditer(galaxy_regex, line):
            column = expanded_column(galaxies_map, galaxy_match.start(), expanded_mapping, expansion_factor)
            galaxies.append((j, column))
        j += 1 if re.findall(galaxy_regex, line) else (expansion_factor + 1)

    # print(galaxies)
    for i, galaxy_a in enumerate(galaxies):
        for j, galaxy_b in enumerate(galaxies):
            if j > i:
                dist = distance(galaxy_a, galaxy_b)
                # print(f"Distance {i + 1} {galaxy_a} to {j + 1} {galaxy_b}: {dist}")
                total += dist
    return total


if __name__ == '__main__':
    # test = True
    test = False
    print(f"First Response: {main_01(load(test))}")
    print(f"Second Response: {main_01(load(test), expansion_factor=999999)}")
