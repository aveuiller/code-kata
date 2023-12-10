# https://adventofcode.com/2023/day/9
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
        return f.readlines()


def reduce_forward(count, prev_deriv):
    return count + prev_deriv[-1]


def reduce_backward(count, prev_deriv):
    return count - prev_deriv[0]


def main_01(sensors: List[str], reverse_filling: bool = False) -> int:
    total = 0
    for sensor in sensors:
        derivative = [list(map(int, sensor.split()))]
        while any(derivative[-1]):
            computed = []
            for i in range(1, len(derivative[-1])):
                computed.append(derivative[-1][i] - derivative[-1][i - 1])
            derivative.append(computed)

        if reverse_filling:
            value = 0
            for i in range(len(derivative) - 1, -1, -1):
                value = derivative[i][0] - value
            total += value
        else:
            total += reduce(lambda count, prev_deriv: count + prev_deriv[-1], derivative, 0)
    return total


if __name__ == '__main__':
    # test = True
    test = False
    print(f"First Response: {main_01(load(test))}")
    print(f"Second Response: {main_01(load(test), reverse_filling=True)}")
