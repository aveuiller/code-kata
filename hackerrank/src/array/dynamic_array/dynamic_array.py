#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    last_answer = 0
    for operation, x, y in queries:
        sub_array = arr[(x ^ last_answer) % n]
        if operation == 1:
            sub_array.append(y)
        elif operation == 2:
            last_answer = sub_array[y % len(sub_array)]
            yield last_answer

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    result = dynamicArray(n, queries)
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()
    print('\n'.join(map(str, result)))
