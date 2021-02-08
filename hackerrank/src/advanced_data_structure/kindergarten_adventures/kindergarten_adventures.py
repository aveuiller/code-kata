#!/bin/python3
import operator
import os


class Kindergarten:
    """
    # Challenge:
    # https://www.hackerrank.com/challenges/kindergarten-adventures/problem
    # TODO: Timeout at the moment.
    """

    def __init__(self, size) -> None:
        self.size = size
        self.finishing = [self.size for _ in range(self.size)]

    def solve(self):
        return self.finishing.index(max(self.finishing)) + 1

    def add_student_time(self, student: int, extra_time: int):
        for i in range(extra_time):
            self.finishing[(student - i) % self.size] -= 1


# Expected: 1
TEST_CASE_1 = [0, 1, 2]
TEST_CASE_COUNT_1 = 3

# Expected: 2
TEST_CASE_2 = [1, 0, 0]
TEST_CASE_COUNT_2 = 3


def main():
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t_count = int(input())
    kg = Kindergarten(t_count)
    # kg = Kindergarten(TEST_CASE_COUNT_1)
    for i, entry in enumerate(input().rstrip().split()):
        # for i, entry in enumerate(TEST_CASE_1):
        kg.add_student_time(i, int(entry))

    start_id = kg.solve()
    print(start_id)
    # fptr.write(str(start_id) + '\n')
    # fptr.close()


if __name__ == '__main__':
    main()
