# https://adventofcode.com/2023/day/20
import os
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


def main_01(garden_map: List[str], steps: int = 6) -> int:
    return 0


if __name__ == '__main__':
    test = True
    # test = False
    if test:
        print(f"First Response: {main_01(load(test), 64)}")  # 3740
        print(f"All tests OK")
    else:
        print(f"First Response: {main_01(load(test), 64)}")  # 3740
        print(f"Second Response: {main_01(load(test))}, 26501365")  #
