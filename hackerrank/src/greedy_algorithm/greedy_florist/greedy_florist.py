#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    """
    Challenge: https://www.hackerrank.com/challenges/greedy-florist
    :param k:
    :param c:
    :return:
    """
    c.sort()
    served = k
    price = sum(c[-k:])
    n = len(c)
    nb_purchases = 1
    while served < n:
        lower_bound = (nb_purchases + 1) * -k
        if lower_bound < -n:
            lower_bound = 0
        upper_bound = nb_purchases * -k
        price += sum([f * (nb_purchases + 1)
                      for f in c[lower_bound:upper_bound]])
        served += abs(upper_bound - lower_bound) - 1
        nb_purchases += 1
    return price


TEST_CASE_K_1 = 3
TEST_CASE_F_1 = [1, 3, 5, 7, 9]

# Expected: 163 578 911
TEST_CASE_K_2 = 3
TEST_CASE_F_2 = [
    390225, 426456, 688267, 800389, 990107, 439248, 240638, 15991,
    874479, 568754, 729927, 980985, 132244, 488186, 5037, 721765,
    251885, 28458, 23710, 281490, 30935, 897665, 768945, 337228,
    533277, 959855, 927447, 941485, 24242, 684459, 312855, 716170,
    512600, 608266, 779912, 950103, 211756, 665028, 642996,
    262173, 789020, 932421, 390745, 433434, 350262, 463568,
    668809, 305781, 815771, 550800]


def main():
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # nk = input().split()
    # n = int(nk[0])
    # k = int(nk[1])
    # c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(TEST_CASE_K_2, TEST_CASE_F_2)

    print(minimumCost)
    # fptr.write(str(minimumCost) + '\n')
    # fptr.close()


if __name__ == '__main__':
    main()
