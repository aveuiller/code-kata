# https://adventofcode.com/2023/day/14
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


ROLLING_STONE = "O"
SQUARE_STONE = "#"


def main_01(rocks: List[str]) -> int:
    total = 0
    pending_rocks = [0 for _ in range(len(rocks[0]))]
    for i in range(len(rocks) - 1, -1, -1):
        for j, rock in enumerate(rocks[i]):
            if rock == ROLLING_STONE:
                pending_rocks[j] += 1

            if (rock == SQUARE_STONE or i == 0) and pending_rocks[j]:
                score_base = len(rocks) - i
                for k in range(1, pending_rocks[j] + 1):
                    total += score_base - k
                    if i == 0:
                        total += 1

                pending_rocks[j] = 0

        # print(f"{rocks[i]} - {i}")
        # print(total)
        # print(pending_rocks)

        total += 0

    return total


if __name__ == '__main__':
    test = True
    test = False
    print(f"First Response: {main_01(load(test))}")  # 105784
    print(f"Second Response: {main_01(load(test))}")  # 91286
