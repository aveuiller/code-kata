# https://adventofcode.com/2023/day/1
import re
import os
from typing import List, Optional
from functools import reduce

def load() -> List[str]:
    dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(dir, 'input.txt')) as f: 
        return f.readlines()

def main_01(games: List[str]) -> int:
    cubes = {'red': 12, 'green': 13, 'blue': 14}
    color_regex = re.compile(r"(?P<amount>\d+)\s(?P<color>red|green|blue)")

    total = 0
    for i, game in enumerate(games):
        possible = True
        for match in re.finditer(color_regex, game):
            if int(match.group("amount")) > cubes.get(match.group("color"), 0):
                possible = False
                break
        if possible:
            total += i + 1
    return total

def main_02(games: List[str]) -> int:
    color_regex = re.compile(r"(?P<amount>\d+)\s(?P<color>red|green|blue)")

    total = 0
    for game in games:
        cubes = {'red': 0, 'green': 0, 'blue': 0}
        for match in re.finditer(color_regex, game):
            amount = int(match.group("amount"))
            color = match.group("color")
            cubes[color] = max(cubes.get(color, 0), amount)
        total += reduce(lambda x, y: x * y, cubes.values())
    return total
        

if __name__ == '__main__':
    print(f"First Response: {main_01(load())}")
    print(f"Second Response: {main_02(load())}")