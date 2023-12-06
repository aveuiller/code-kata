# https://adventofcode.com/2023/day/1
import os
from typing import List


def load(test_mode: bool = False) -> List[str]:
    dirname = os.path.dirname(os.path.abspath(__file__))
    input_file = 'input.txt'
    if test_mode:
        input_file = f"test_{input_file}"
    with open(os.path.join(dirname, input_file)) as f:
        return f.readlines()


def _is_winning(time:int, distance: int, time_held: int) -> bool:
    return (time - time_held) * time_held > distance


def main_01(races: List[str], remove_spaces: bool = False) -> int:
    total = 1
    if remove_spaces:
        times = list(map(int, [races[0].split(":")[-1].replace(" ", "")]))
        distances = list(map(int, [races[1].split(":")[-1].replace(" ", "")]))
    else:
        times = list(map(int, races[0].split(":")[-1].split()))
        distances = list(map(int, races[1].split(":")[-1].split()))

    for time, distance in zip(times, distances):
        # print(f"Race conditions: {time} - {distance}")
        lower_limit = 0
        while not _is_winning(time, distance, lower_limit):
            lower_limit += 1
        upper_limit = time
        while not _is_winning(time, distance, upper_limit):
            upper_limit -= 1
        
        # print(f"Winning under {(upper_limit - lower_limit + 1)} conditions")
        total *= (upper_limit - lower_limit + 1)
    return total


if __name__ == '__main__':
    test = False
    print(f"First Response: {main_01(load(test))}")
    print(f"Second Response: {main_01(load(test), remove_spaces=True)}")
