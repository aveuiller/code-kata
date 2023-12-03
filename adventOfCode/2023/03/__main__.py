# https://adventofcode.com/2023/day/1
import re
import os
from typing import List, Optional
from functools import reduce

def load() -> List[str]:
    dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(dir, 'input.txt')) as f: 
        return f.readlines()

def is_part_number(schematic: List[str], line_index: int,
                   lower_boundary: int, upper_boundary: int) -> bool:
    alpharegex = re.compile(r"[^.0-9]")
    lower_i = max(0, line_index - 1)
    upper_i = min(len(schematic) , line_index + 2)
    for line in schematic[lower_i:upper_i]:
        lower_j = max(0, lower_boundary - 1)
        upper_j = min(len(line), upper_boundary + 2)
        if re.search(alpharegex, line[lower_j:upper_j].strip()):
            return True
    return False

def main_01(schematic: List[str]) -> int:
    total = 0
    for i, schem_line in enumerate(schematic):
        lower_boundary = 0
        upper_boundary = 0
        current_number = ''
        for j, schem_char in enumerate(schem_line):
            if schem_char.isnumeric():
                if j > 0 and not schem_line[j - 1].isnumeric():
                    lower_boundary = j
                    current_number = schem_char
                else:
                    current_number += schem_char
            else:
                if (j > 0 and schem_line[j - 1].isnumeric()) or j == len(schem_line):
                    upper_boundary = j - 1
                    if is_part_number(schematic, i, lower_boundary, upper_boundary):
                        total += int(current_number)
                    current_number = ''
    return total
     
def get_adjactent_numbers(schematic: List[str], line_index: int,
                          star_index: int) -> List[int]:
    digitregex = re.compile(r"[0-9]")
    lower_i, upper_i = max(0, line_index - 1), min(len(schematic), line_index + 2)    

    numbers = []
    for line in schematic[lower_i:upper_i]:
        current_u_j, current_l_j = 0, 0
        lower_j, upper_j = max(0, star_index - 1), min(len(line), star_index + 2)
        for j, char in enumerate(line[lower_j:upper_j].strip()):
            j_index = lower_j + j
            if j_index <= current_u_j:
                continue
            if char.isdigit():
                current_l_j, current_u_j = j_index, j_index
                while line[current_l_j - 1].isdigit():
                    current_l_j -= 1
                while line[current_u_j + 1].isdigit():
                    current_u_j += 1
                numbers.append(int(line[current_l_j:current_u_j + 1]))
    return numbers

def main_02(schematic: List[str]) -> int:
    total = 0
    for i, schem_line in enumerate(schematic):
        lower_boundary = 0
        upper_boundary = 0
        for star_index in re.finditer('\*', schem_line):
            numbers = get_adjactent_numbers(schematic, i, star_index.start())
            if len(numbers) >= 2:
                total += reduce(lambda x, y: x * y, numbers)
    return total
        

if __name__ == '__main__':
    print(f"First Response: {main_01(load())}")
    print(f"Second Response: {main_02(load())}")