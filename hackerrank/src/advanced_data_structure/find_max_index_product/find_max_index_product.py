#!/bin/python3

import os
import sys


def index_product(arr, index):
    """Performance timeout.

    :param arr:
    :param index:
    :return:
    """
    operations = [_find_right, _find_left]
    if index < len(arr) // 2:
        operations.reverse()

    result = 1
    for op in operations:
        result *= op(arr, index)
        if result == 0:
            return 0

    return result


def _find_left(arr, index):
    j = index - 1
    while j >= 0 and arr[j] <= arr[index]:
        j -= 1
    return j + 1 if j >= 0 else 0


def _find_right(arr, index):
    k = index + 1
    while k < len(arr) and arr[k] <= arr[index]:
        k += 1
    return k + 1 if k < len(arr) else 0


# Complete the solve function below.
def solve_bruteforce(arr):
    """Performance timeout

    :param arr:
    :return:
    """
    product = 0
    for i in range(len(arr) - 1, 0, -1):
        product = max(product, index_product(arr, i))
        if product >= i * (i - 1):
            break

    return product


def solve_stack(arr):
    """Works fine

    :param arr:
    :return:
    """
    to_analyze = [len(arr) - 1]
    max_product = 0
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            to_analyze.append(i)
        else:
            while to_analyze:
                previous = to_analyze.pop()
                if arr[previous] > arr[i + 1]:
                    max_product = max(max_product, (previous + 1) * (i + 1))
                    to_analyze.clear()
            to_analyze.append(i)
    return max_product


def solve(arr):
    """
    Challenge: https://www.hackerrank.com/challenges/find-maximum-index-product

    :param arr:
    :return:
    """
    return solve_stack(arr)


# Expected: 8
TEST_CASE_1 = [5, 4, 3, 4, 5]
# Expected 15
TEST_CASE_2 = [1, 2, 5, 4, 5]
# Expected 3
TEST_CASE_3 = [6, 1, 9, 3, 2]


def main():
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # arr_count = int(input())
    # arr = list(map(int, input().rstrip().split()))
    # result = solve(arr)

    result = solve(TEST_CASE_3)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()


if __name__ == '__main__':
    main()
