#!/bin/python3
import math
import os
import random
import re
import sys


# Complete the matchingStrings function below.
def matchingStrings(mapping, queries):
    """
    # Challenge: https://www.hackerrank.com/challenges/sparse-arrays/problem

    :param strings:
    :param queries:
    :return:
    """
    return [mapping.get(string, 0) for string in queries]


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    strings_count = int(input())
    strings = []

    mapping = {}
    for _ in range(strings_count):
        strings_item = input()
        count = mapping.setdefault(strings_item, 0)
        mapping[strings_item] = count + 1

    queries_count = int(input())
    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(mapping, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')
    fptr.close()


if __name__ == '__main__':
    main()
