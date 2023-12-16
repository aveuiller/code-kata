# https://adventofcode.com/2023/day/14
import os
import re
from typing import List, Optional
from collections import OrderedDict


def load(test_mode: bool = False, name_override: Optional[str] = None) -> List[str]:
    dirname = os.path.dirname(os.path.abspath(__file__))
    input_file = 'input.txt'
    if test_mode:
        input_file = f"test_{input_file}"
    if name_override:
        input_file = name_override
    with open(os.path.join(dirname, input_file)) as f:
        return f.read().splitlines()


def appendix_1a(entry: str, previous_result: int = 0) -> int:
    result = previous_result
    for letter in entry:
        result = ((result + ord(letter)) * 17) % 256
    assert 0 <= result <= 255, f"bad value: {result}" 
    return result


def main_01(codes: List[str]) -> int:
    total = 0
    for entries in codes:
        for entry in entries.split(","):
            total += appendix_1a(entry)
    return total


def main_02(codes: List[str]) -> int:
    boxes = [OrderedDict() for _ in range(256)]
    box_ops = re.compile(r"(?P<label>\w+)(?P<operation>=|-)(?P<code>\d)?")
    total = 0
    for entries in codes:
        for entry in entries.split(","):
            match = re.match(box_ops, entry)
            label = match.group("label")
            hash = appendix_1a(label)

            if match.group("operation") == "-":
                if label in boxes[hash]:
                    del boxes[hash][label]
            elif match.group("operation") == "=":
                boxes[hash][label] = match.group("code")
            else:
                assert False, "Unknown operation"
        
    for i, box in enumerate(boxes):
        for j, (label, code) in enumerate(box.items()):
            score = (i + 1) * (j + 1) * int(code)
            total += score
    return total


if __name__ == '__main__':
    test = True
    test = False
    print(f"First Response: {main_01(load(test))}")
    print(f"Second Response: {main_02(load(test))}")
