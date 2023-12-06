# https://adventofcode.com/2023/day/1
import os
import re
import sys
from typing import List


def load(test_mode: bool = False) -> List[str]:
    dirname = os.path.dirname(os.path.abspath(__file__))
    input_file = 'input.txt'
    if test_mode:
        input_file = f"test_{input_file}"
    with open(os.path.join(dirname, input_file)) as f:
        return f.readlines()


# Input reminder: seed -> soil -> fertilizer -> water -> light -> temperature -> humidity -> location
def main_01(almanach: List[str]) -> int:
    seeds = list(map(int, almanach.pop(0).split(':')[-1].split()))
    updated = set()
    for line in almanach:
        line = line.split()
        if len(line) == 3:
            dest, src, rnge = map(int, line)
            for i, seed in enumerate(seeds):
                if src <= seed < src + rnge and i not in updated:
                    seeds[i] = seed - src + dest
                    updated.add(i)
        elif len(line) > 0:
            updated = set()

    return min(seeds)


def main_02(almanach: List[str]) -> int:
    seeds_def = almanach.pop(0).split(':')[-1]
    seeds = []
    for match in re.finditer(r"(\d+\s+\d+)", seeds_def):
        s_start, s_len = list(map(int, match.group(0).split()))
        seeds.append([s_start, s_start + s_len])
    updated = set()
    new_seeds = []
    for line in almanach:
        line = line.split()
        if len(line) == 3:
            m_dest, m_start, m_range = map(int, line)
            m_end = m_start + m_range
            for i, (s_start, s_end) in enumerate(seeds):
                if i not in updated:
                    # Ensure intersection
                    lower_bound = max(s_start, m_start)
                    upper_bound = min(s_end, m_end)
                    if upper_bound > lower_bound:
                        if s_start < m_start:
                            new_seeds.append([s_start, m_start - 1])
                        if s_end > m_end:
                            new_seeds.append([m_end + 1, s_end])
                        if s_start >= m_start or s_end <= m_end:
                            m_src_to_dst = m_dest - m_start
                            seeds[i] = [lower_bound + m_src_to_dst, upper_bound + m_src_to_dst]
                        updated.add(i)
        elif len(line) > 0:
            seeds += new_seeds
            new_seeds = []
            updated = set()

    seeds += new_seeds
    return min([seed[0] for seed in seeds])


if __name__ == '__main__':
    test = False
    print(f"First Response: {main_01(load(test))}")
    print(f"Second Response: {main_02(load(test))}")
