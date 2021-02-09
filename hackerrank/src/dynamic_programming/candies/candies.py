#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the candies function below.
def candies(n, arr):
    """
    Challenge: https://www.hackerrank.com/challenges/candies
    :param n:
    :param arr:
    :return:
    """
    candies_cnt = [1] * n

    count_candies(arr, candies_cnt)
    arr.reverse()
    candies_cnt.reverse()
    count_candies(arr, candies_cnt)

    # arr.reverse()
    # candies_cnt.reverse()
    # print(arr)
    # print(candies_cnt)
    return sum(candies_cnt)


def count_candies(arr, candies_cnt):
    for i, student in enumerate(arr):
        if i > 0:
            if arr[i - 1] < arr[i] and candies_cnt[i - 1] >= candies_cnt[i]:
                candies_cnt[i] = candies_cnt[i - 1] + 1


# Expected: 12
TEST_CASE_1 = [2, 4, 3, 5, 2, 6, 4, 5]
# Expected: 19
TEST_CASE_2 = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
# Expected: 22
#             [1, 2, 1, 2, 1, 2, 3, 4, 3, 2, 1]
TEST_CASE_3 = [2, 4, 2, 6, 1, 7, 8, 9, 4, 2, 1]


def main():
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input())
    # arr = []

    # for _ in range(n):
    #     arr_item = int(input())
    #     arr.append(arr_item)

    # result = candies(n, arr)
    result = candies(len(TEST_CASE_3), TEST_CASE_3)

    print(str(result) + '\n')
    # fptr.write(str(result) + '\n')
    # fptr.close()


if __name__ == '__main__':
    main()
