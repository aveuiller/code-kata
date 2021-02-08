#!/bin/python3


import os
import sys


class Hierarchy:
    """
    # Complete the solve function below.
    # Challenge: https://www.hackerrank.com/challenges/company-retreat/
    # TODO: Not started yet. Need to find the right data representation.
    """

    def __init__(self, supervisors) -> None:
        self.depth = 0
        self.hierarchy = {}
        self.supervisor = {}
        self._seed_hierarchy(supervisors)

    def _seed_hierarchy(self, supervisors):
        for employee, supervisor in enumerate(supervisors):
            employees = self.hierarchy.setdefault(supervisor, [])
            employees.append(employee)
            self.supervisor[employee] = supervisor

    def groups(self, max_person) -> int:
        return 4


def solve(supervisors, groups):
    """
    :param supervisors:
    :param groups:
    :return:
    """
    hierarchy = Hierarchy(supervisors)

    total_cost = 0
    for cost, max_person in groups:
        nb_groups = hierarchy.groups(max_person)
        total_cost += nb_groups * cost

    return total_cost % (pow(10, 9) + 7)


# Expected
# 46
TEST_SUPERISORS_1 = [1, 1, 3, 4, 2, 4]
TEST_GROUPS_1 = [[5, 3], [6, 2], [1, 1]]


def main():
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # nm = input().split()
    # n = int(nm[0])
    # m = int(nm[1])
    # supervisors = list(map(int, input().rstrip().split()))
    # groups = []
    # for _ in range(m):
    #     groups.append(list(map(int, input().rstrip().split())))

    supervisors = TEST_SUPERISORS_1
    groups = TEST_GROUPS_1
    result = solve(supervisors, groups)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()


if __name__ == '__main__':
    main()
