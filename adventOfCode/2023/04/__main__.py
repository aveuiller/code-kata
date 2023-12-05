# https://adventofcode.com/2023/day/1
import os
import re
from typing import List


def load(test_mode: bool = False) -> List[str]:
    dirname = os.path.dirname(os.path.abspath(__file__))
    input_file = 'input.txt'
    if test_mode:
        input_file = f"test_{input_file}"
    with open(os.path.join(dirname, input_file)) as f:
        return f.readlines()


def card_matching_numbers_count(card):
    card_description = re.compile(
        r"Card\s+(?P<number>\d+):\s+(?P<winning>(\d+\s*)+)\s*\|\s*(?P<scratched>(\d+\s*)+)\s*\n?"
    )
    match = re.match(card_description, card)
    matches_count = len(set(match.group("winning").split()).intersection(match.group("scratched").split()))
    return matches_count


def main_01(cards: List[str]) -> int:
    total = 0
    for card in cards:
        if matches_count := card_matching_numbers_count(card):
            total += pow(2, matches_count - 1)

    return total


def main_02(cards: List[str]) -> int:
    total = 0
    copies = [0 for _ in range(len(cards))]
    for card in cards:
        current_copies = copies.pop(0) + 1
        total += current_copies
        if matches_count := card_matching_numbers_count(card):
            for i in range(matches_count):
                copies[i] += current_copies
    return total


if __name__ == '__main__':
    test = False
    print(f"First Response: {main_01(load(test))}")
    print(f"Second Response: {main_02(load(test))}")
