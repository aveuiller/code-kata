#!/bin/python3
from dataclasses import dataclass, field

from typing import Dict, Optional


@dataclass
class DisjointSet:
    parent: Dict[int, int] = field(default_factory=dict)
    sizes: Dict[int, int] = field(default_factory=dict)

    def find(self, val: int) -> Optional[int]:
        if val is None or self.parent.get(val) is None:
            self.new_set(val)
            return val
        elif self.parent.get(val) == val:
            return val
        else:
            return self.find(self.parent.get(val))

    def union(self, x: int, y: int) -> None:
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent != y_parent:
            # Bigger set swallows the tinnier
            if self.sizes[x_parent] < self.sizes[y_parent]:
                x_parent, y_parent = y_parent, x_parent

            self.parent[y_parent] = x_parent
            self.sizes[x_parent] += self.sizes[y_parent]
            self.sizes.pop(y_parent)

    def new_set(self, val):
        if val not in self.parent:
            self.parent[val] = val
            self.sizes[val] = 1

    def biggest(self):
        return max(self.sizes.values())

    def tiniest(self):
        connected_sizes = set(self.sizes.values())
        return min(connected_sizes) if connected_sizes else 0


#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#
def componentsInGraph(gb):
    components = DisjointSet()
    for x, y in gb:
        found_x = components.find(x)
        found_y = components.find(y)

        if found_x != found_y:
            components.union(x, y)

    return components.tiniest(), components.biggest()


# Expected: 2, 4
TEST_CASE_1 = [
    [1, 6],
    [2, 7],
    [3, 8],
    [4, 9],
    [2, 6]
]
# Expected: 2, 3
TEST_CASE_2 = [
    [1, 5],
    [1, 6],
    [2, 4],
]
# Expected: 11, 25
TEST_CASE_3 = [
    [5, 56],
    [4, 51],
    [2, 53],
    [8, 52],
    [5, 43],
    [2, 80],
    [5, 47],
    [4, 79],
    [3, 75],
    [1, 67],
    [7, 61],
    [2, 57],
    [5, 47],
    [4, 63],
    [10, 79],
    [1, 57],
    [4, 42],
    [8, 79],
    [6, 53],
    [3, 74],
    [7, 60],
    [10, 79],
    [5, 46],
    [3, 50],
    [6, 57],
    [8, 71],
    [6, 74],
    [10, 44],
    [9, 80],
    [7, 59],
    [7, 74],
    [6, 55],
    [3, 77],
    [3, 53],
    [5, 50],
    [9, 70],
    [4, 72],
    [5, 73],
    [6, 70],
    [7, 46],
]


def main():
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input().strip())
    # gb = []
    # for _ in range(n):
    #     gb.append(list(map(int, input().rstrip().split())))
    # result = componentsInGraph(gb)

    result = componentsInGraph(TEST_CASE_3)
    print(result)
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()


if __name__ == '__main__':
    main()
