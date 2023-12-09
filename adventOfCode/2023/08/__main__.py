# https://adventofcode.com/2023/day/8
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

def _build_instructions(instructions: str) -> List[int]:
    return list(map(int, instructions.split()[0].replace('L', '0').replace('R', '1')))


def _build_nodes(directions: List[str]) -> dict[str, List[str]]:
    node_regex = re.compile(r'(?P<origin>\w+)\s+=\s+\((?P<left>\w+)\s*,\s+(?P<right>\w+)\)')
    nodes = {}
    for node in directions:
        match = re.match(node_regex, node)
        if match:
            nodes[match.group("origin")] = [match.group("left"), match.group("right")]
    return nodes

def main_01(directions: List[str]) -> int:
    start = "AAA"
    end = "ZZZ"
    lr_instructions = _build_instructions(directions.pop(0))
    nodes = _build_nodes(directions)

    i = 0
    current_node = start
    while current_node != end:
        current_node = nodes[current_node][lr_instructions[i % len(lr_instructions)]]
        i += 1

    return i

def lcm(outs: List[int]) -> int:
    result = 1
    for i in outs:
        result = result * i // math.gcd(result, i)
    return result

def _converging_at(nodes_outputs: dict[str, dict[str, List[int]]]) -> Optional[int]:
    rates = []
    for outputs in nodes_outputs:
        # Not enough data to compute
        if not outputs:
            return None

        for _, ends in outputs.items():
            # Not enough data to compute
            if len(ends) < 2:
                return None
    
            rates.append(ends[1] - ends[0])
    print(nodes_outputs)
    print(rates)
    print(lcm(rates))
    return lcm(rates)

def main_02(directions: List[str]) -> int:
    start_suffix = "A"
    end_suffix = "Z"
    lr_instructions = _build_instructions(directions.pop(0))
    nodes = _build_nodes(directions)

    i = 0
    current_nodes = [node for node in nodes.keys() if node.endswith(start_suffix)]
    nodes_outputs = [dict() for _ in current_nodes]
    while not all([node.endswith(end_suffix) for node in current_nodes]):
        for j in range(len(current_nodes)):
            current_nodes[j] = nodes[current_nodes[j]][lr_instructions[i % len(lr_instructions)]]
            
            if current_nodes[j].endswith(end_suffix):
                nodes_outputs[j].setdefault(current_nodes[j], []).append(i)
                if end := _converging_at(nodes_outputs):
                    return end
        i += 1

    return i


if __name__ == '__main__':
    # test = True
    test = False
    print(f"First Response: {main_01(load(test))}")
    print(f"Second Response: {main_02(load(test))}")
    # print(f"Second Response: {main_02(load(test, name_override='test_input_2.txt'))}")