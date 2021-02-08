#!/bin/python3

import math
import os
import random
import re
import sys


def rotateLeft(d, arr):
    """
    # Complete the 'rotateLeft' function below.
    #
    # The function is expected to return an INTEGER_ARRAY.
    # The function accepts following parameters:
    #  1. INTEGER d
    #  2. INTEGER_ARRAY arr
    :param d:
    :param arr:
    :return:
    """
    return arr[d:] + arr[:d]


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = rotateLeft(d, arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()


if __name__ == '__main__':
    print(rotateLeft(2, [1, 2, 3, 4, 5]))
