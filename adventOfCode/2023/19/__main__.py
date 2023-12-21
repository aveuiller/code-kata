# https://adventofcode.com/2023/day/19
import os
import pprint
import re
import sys
from functools import reduce
from typing import List, Optional, Tuple, Dict, Iterator

pp = pprint.PrettyPrinter(depth=4)


def load(test_mode: bool = False, name_override: Optional[str] = None) -> List[str]:
    dirname = os.path.dirname(os.path.abspath(__file__))
    input_file = 'input.txt'
    if test_mode:
        input_file = f"test_{input_file}"
    if name_override:
        input_file = name_override
    with open(os.path.join(dirname, input_file)) as f:
        return f.read().splitlines()


class Condition:
    PARSING = re.compile(r"(?:(?P<operand>[xmas])(?P<operator>[<>])(?P<value>\d+):)?(?P<workflow>\w+)")

    def __init__(self, definition: str):
        self.definition = definition
        match = re.match(self.PARSING, definition).groupdict()
        self.operand = match.get("operand")
        self.operator = match.get("operator")
        self.value = int(match.get("value")) if match.get("value") else None
        self.expression = None
        if self.operand and self.operator and self.value:
            self.expression = f"{self.operand}{self.operator}{self.value}"
        self.workflow = match.get("workflow")

    def next_workflow(self, x: int, m: int, a: int, s: int) -> Optional[str]:
        return self.workflow if self.expression is None or eval(f"{self.expression}") else None

    def __repr__(self):
        return f"Condition({self.expression}, {self.workflow})"

    def revert(self) -> 'Condition':
        copy = Condition(self.definition)
        if copy.expression is not None:
            copy.operator = '>' if self.operand == '<' else '<'
            copy.value = self.value + 1 if self.operand == '<' else self.value - 1
        return copy


class Workflow:
    PARSING = re.compile(r"(?P<name>\w+){(?P<conditions>.*)}")

    def __init__(self, declaration: str):
        match = re.match(self.PARSING, declaration)
        self.name = match.group("name")
        self.conditions = self.extract(match.group("conditions").split(","))

    def extract(self, conditions: List[str]) -> List[Condition]:
        return [Condition(condition) for condition in conditions]

    @staticmethod
    def parse_values(values: str) -> Dict[str, int]:
        val = {}
        for entry in values.replace("{", "").replace("}", "").split(","):
            name, value = entry.split("=")
            val[name] = int(value)
        return val

    def sort(self, values: str, workflows: Dict[str, 'Workflow']) -> bool:
        return self.sort_xmas(**self.parse_values(values), workflows=workflows)

    def sort_xmas(self, x: int, m: int, a: int, s: int, workflows: Dict[str, 'Workflow']) -> bool:
        for condition in self.conditions:
            result = condition.next_workflow(x, m, a, s)
            if result is None:
                continue

            if result == "A":
                return True
            elif result == "R":
                return False
            else:
                return workflows[result].sort_xmas(x, m, a, s, workflows)

    def __repr__(self):
        return f"Workflow({self.conditions})"


def main_01(xmas_sort: List[str]) -> int:
    total = 0
    workflows = {}
    for line in xmas_sort:
        if re.match(Workflow.PARSING, line):
            workflow = Workflow(line)
            workflows[workflow.name] = workflow
        elif line:
            if workflows.get("in").sort(line, workflows):
                total += reduce(lambda x, y: x + y, Workflow.parse_values(line).values(), 0)
        else:
            print(workflows)
    return total


class Limits:
    def __init__(self, base_min: int = 1, base_max: int = 4000):
        self.base_min = base_min
        self.base_max = base_max
        self.limits = {letter: (self.base_min, self.base_max) for letter in "xmas"}

    def __hash__(self):
        hashcode = ""
        for a, b in self.limits.items():
            hashcode += f"{a}:{b}"
        return hash(hashcode)

    def __eq__(self, other):
        return self.limits == other.limits

    def copy(self) -> 'Limits':
        copy = Limits(self.base_min, self.base_max)
        copy.limits = self.limits
        return copy

    @staticmethod
    def merge_all(limits: Iterator['Limits']) -> 'Limits':
        wider_limit = Limits(sys.maxsize, 0)
        for limit in limits:
            for letter, value in limit.limits.items():
                wider_limit.unblock(letter, value)
        return wider_limit

    def merge(self, single_limits: 'Limits') -> None:
        for letter, value in single_limits.limits.items():
            self.unblock(letter, value)

    def unblock(self, letter: str, value: Tuple[int, int]) -> None:
        limit = self.limits[letter]
        limit = min(value[0], limit[0]), max(value[1], limit[1])
        self.limits[letter] = limit

    def restrict(self, condition: Condition) -> None:
        # print(f'\t\t\tRestricting {condition.expression}')
        if condition.expression is None:
            return

        limit = self.limits[condition.operand]
        if condition.operator == "<":
            limit = limit[0], min(limit[1], condition.value)
        elif condition.operator == ">":
            limit = max(limit[0], condition.value), limit[1]
        self.limits[condition.operand] = limit

    def __repr__(self):
        return f"Limit({self.limits})"


def fence_condition(condition: Condition) -> Optional[bool]:
    if condition.workflow == "A":
        return True
    elif condition.workflow == "R":
        return None
    return False


def discover_conditions(
        workflows: Dict[str, Workflow], conditions: List[Condition]
) -> List[Limits]:
    # print(f"\tDiving into {condition}")
    # if current_limits is None:
    #     current_limits = Limits()
    # current_limits.restrict(condition)1

    cond = conditions[0]
    if cond.workflow == "A":
        limit = Limits()
        limit.restrict(cond)
        return [limit]
    elif cond.workflow == "R":
        return []

    depth = discover_conditions(workflows, workflows.get(cond.workflow).conditions)
    for limit in depth:
        limit.restrict(cond)

    breadth = discover_conditions(workflows, conditions[1:]) if len(conditions) > 1 else []
    for limit in breadth:
        limit.restrict(cond.revert())

    return depth + breadth


def main_02(xmas_sort: List[str]) -> int:
    workflows = {}
    for line in xmas_sort:
        if re.match(Workflow.PARSING, line):
            workflow = Workflow(line)
            workflows[workflow.name] = workflow
        else:
            break

    total = 0
    discovered = discover_conditions(workflows, workflows.get("in").conditions)

    for limits in discovered:
        print(limits)
        subtotal = 1
        for low, high in limits.limits.values():
            subtotal *= high - low + 1
        total += subtotal
    return total


if __name__ == '__main__':
    test = True
    test = False
    print(f"First Response: {main_01(load(test))}")  # 432434
    print(f"Second Response: {main_02(load(test))}")  # 132557544578569
