# https://adventofcode.com/2023/day/12
import os
import re
from functools import cache
from typing import List, Optional, Tuple
from itertools import chain


def load(test_mode: bool = False, name_override: Optional[str] = None) -> List[str]:
    dirname = os.path.dirname(os.path.abspath(__file__))
    input_file = 'input.txt'
    if test_mode:
        input_file = f"test_{input_file}"
    if name_override:
        input_file = name_override
    with open(os.path.join(dirname, input_file)) as f:
        return f.read().splitlines()


def row(mirrors: List[str], index: int) -> str:
    return mirrors[index]


def column(mirrors: List[str], index: int) -> str:
    return ''.join([row[index]  for row in mirrors])


def count_diffs(a: str, b: str, previous_diffs: int, break_at: int = 1):
    diffs = previous_diffs
    for ca, cb in zip(a,b):
        if ca != cb:
            diffs += 1
            if diffs > break_at:
                return diffs
    return diffs


def find_mirror(mirrors: List[str], primary_size: int, transformation, smudged: bool = False) -> int:
    for i in range(primary_size - 1):
        valid = True
        diffs = 0

        for j in range(min(i + 1, primary_size - i - 1)):
            element_a = transformation(mirrors, i - j)
            element_b = transformation(mirrors, i + j + 1)
            if smudged:
                diffs = count_diffs(element_a, element_b, diffs)
                if diffs > 1:
                    valid = False
                    break
            else:
                if element_a != element_b:
                    valid = False
                    break
            # print(f"\tCompared {transformation.__name__} {element_a} and {element_b} at {i} (total diff {diffs})")

        if (not smudged and valid) or (smudged and diffs == 1):
            return i + 1

    return 0


def main_01(mirrors: List[str], smudged: bool = False) -> int:
    columns_to_the_left = 0
    rows_above = 0
    last_mirror = 0
    mirrors.append('')

    for i, line in enumerate(mirrors):
        if not line:
            print(" \n".join(mirrors[last_mirror:i]))

            mirror_row = find_mirror(mirrors[last_mirror:i], i - last_mirror, row, smudged)
            print(f"Row: {mirror_row}")
            if mirror_row:
                rows_above += mirror_row
            else:
                mirror_column = find_mirror(mirrors[last_mirror:i], len(mirrors[i - 1]), column, smudged)
                if not mirror_column:
                    raise ValueError
                print(f"Column: {mirror_column}")
                columns_to_the_left += mirror_column

            last_mirror = i + 1
    return columns_to_the_left + rows_above * 100


if __name__ == '__main__':
    test = True
    test = False
    print(f"First Response: {main_01(load(test))}")  # 33975
    print(f"Second Response: {main_01(load(test), smudged=True)}")  # 29083
