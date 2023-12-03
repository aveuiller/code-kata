# https://adventofcode.com/2023/day/1

import os
from typing import List, Optional

def load() -> List[str]:
    dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(dir, 'input.txt')) as f: 
        return f.readlines()

def find_digit(line: str, index: int, extended_values: Optional[dict] = None, reversed: bool = False) -> Optional[int]:
    step = -1 if reversed else 1
    if extended_values is None:
        extended_values = {}

    if line[index].isnumeric():
        return int(line[index])
    else:
        for alpha_representation, val in extended_values.items():
            if line[index:index+len(alpha_representation)] == alpha_representation[::step]:
                return int(val)
    return None

def main(lines: List[str], extended_values: Optional[dict] = None):
    if extended_values is None:
        extended_values = {}

    total = 0
    for line in lines:
        for i in range(len(line)):
            if found := find_digit(line, i, extended_values):
                total += found * 10
                break
        for i in range(len(line)):
            if found := find_digit(line[::-1], i, extended_values, reversed=True):
                total += found
                break
    return total

if __name__ == '__main__':
    extended_values = {"one": 1,"two": 2,"three": 3,"four": 4,"five": 5,"six": 6,"seven": 7,"eight": 8,"nine": 9}
    print(f"First Response: {main(load())}")
    print(f"Second Response: {main(load(), extended_values)}")