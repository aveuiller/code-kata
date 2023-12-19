# https://adventofcode.com/2023/day/18
import re
import os
from typing import List, Optional, Tuple, Dict, Set
import pprint
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


UP = "U"
DOWN = "D"
LEFT = "L"
RIGHT = "R"
DIG_REGEX = re.compile(r'(?P<direction>[UDPLR])\s+(?P<length>\d+)\s+\(#(?P<color>[0-9a-f]+)\)')
DIRECTIONS = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}


def extend_vertically(dig_edges: Dict[int, Set[int]], location: int, length: int) -> Tuple[int, int]:
    fence = (location[1], location[1])
    offset = 1 if length > 0 else -1

    print(f"Location {location} to {location[0] + length, location[1]} - Fence {fence}")
    for i in range(location[0], location[0] + length + offset, offset):
        dig_edges.setdefault(i, set()).add(fence)
    return location[0] + length, location[1]


def extend_horizontally(dig_edges: Dict[int, Set[int]], location: int, length: int) -> Tuple[int, int]:
    fence = tuple(sorted((location[1], location[1] + length)))

    print(f"Location {location} to {location[0], location[1] + length} - Fence {fence}")
    dig_edges.setdefault(location[0], set()).add(fence)
    return location[0], location[1] + length


def reduce_fences(dig_edges: Dict[int, Set[int]]) -> Dict[int, Set[int]]:
    dig_result = {}
    for i, fences in dig_edges.items():
        fence_result = set()
        previous = None
        for fence in sorted(fences):
            if previous is None:
                previous = fence
            elif previous[1] >= fence[0]:
                previous = (previous[0], max(fence[1], previous[1]))
            else:
                fence_result.add(previous)
                previous = fence
        fence_result.add(previous)
        dig_result[i] = sorted(fence_result)
    return dig_result


def count_inside(dig_edges: Dict[int, Set[int]]) -> int:
    total = 0
    for _, fences in dig_edges.items():
        start = 0
        inside = False
        for fence in fences:
            if not inside:
                start = fence[0]
            if inside:
                total += fence[1] - start + 1
            inside = not inside

        # Impair number of fences, count the last one
        if inside:
            total += fence[1] - fence[0] + 1
    return total



def main_01(dig_plan: List[str]) -> int:
    dig_edges = {}
    location = (0, 0)
    for dig_order in dig_plan:
        matched = re.match(DIG_REGEX, dig_order)
        assert matched is not None, f"Unable to match {dig_order}"

        direction = matched.group("direction")
        length = int(matched.group("length"))
        if direction == UP:
            location = extend_vertically(dig_edges, location, -length)
        elif direction == DOWN:
            location = extend_vertically(dig_edges, location, length)
        elif direction == LEFT:
            location = extend_horizontally(dig_edges, location, -length)
        elif direction == RIGHT:
            location = extend_horizontally(dig_edges, location, length)

    dig_edges = reduce_fences(dig_edges)
    # pp.pprint(dig_edges)

    return count_inside(dig_edges)


def main_01_shoelace_algo(dig_plan: List[str]) -> int:
    area_shoelace = 0
    perimeter = 0
    prev_corner = (0, 0)

    for dig_order in dig_plan:
        matched = re.match(DIG_REGEX, dig_order)
        assert matched is not None, f"Unable to match {dig_order}"

        direction = matched.group("direction")
        length = int(matched.group("length"))

        step_x, step_y = DIRECTIONS[direction][0] * length, DIRECTIONS[direction][1] * length
        perimeter += abs(step_x + step_y)
        corner = (prev_corner[0] + step_x, prev_corner[1] + step_y)
        area_shoelace += prev_corner[1] * corner[0] - corner[1] * prev_corner[0]
        prev_corner = corner

    return int(abs(area_shoelace) + perimeter) // 2 + 1


def main_02(dig_plan: List[str]) -> int:
    area_shoelace = 0
    perimeter = 0
    prev_corner = (0, 0)
    directions_binding = "RDLU"
    
    for dig_order in dig_plan:
        matched = re.match(DIG_REGEX, dig_order)
        assert matched is not None, f"Unable to match {dig_order}"

        direction = directions_binding[int(matched.group("color")[-1], 16)]
        length = int(matched.group("color")[:5], 16)

        step_x, step_y = DIRECTIONS[direction][0] * length, DIRECTIONS[direction][1] * length
        perimeter += abs(step_x + step_y)
        corner = (prev_corner[0] + step_x, prev_corner[1] + step_y)
        area_shoelace += prev_corner[1] * corner[0] - corner[1] * prev_corner[0]
        prev_corner = corner

    return int(abs(area_shoelace) + perimeter) // 2 + 1

if __name__ == '__main__':
    test = True
    test = False
    print(f"First Response: {main_01_shoelace_algo(load(test))}")  # 47527
    print(f"Second Response: {main_02(load(test))}")  # 52240187443190
