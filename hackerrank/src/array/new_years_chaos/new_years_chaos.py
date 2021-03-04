#!/bin/python3

import math
import os
import random
import re
import sys

# Challenge: https://www.hackerrank.com/challenges/new-year-chaos/
def minimumBribes(q):
    nb_bribes = 0
    for pos, val in enumerate(q):
        if val - pos > 3:
            print("Too chaotic")
            return

        for x in q[max(val - 2, 0):pos]:
            if x > val:
                nb_bribes += 1
    print(nb_bribes)


def main():
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)


if __name__ == '__main__':
    main()
