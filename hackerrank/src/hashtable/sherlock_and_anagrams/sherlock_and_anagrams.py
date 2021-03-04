#!/bin/python3

import math
import os
import random
import re
import sys


# Challenge: https://www.hackerrank.com/challenges/sherlock-and-anagrams
# Complete the sherlockAndAnagrams function below.
def compute_sized_anagrams(s, size):
    substrings = {}
    total = 0
    for i in range(len(s)):
        sub = ''.join(sorted(s[i:i + size]))
        if len(sub) < size:
            continue

        if sub not in substrings.keys():
            substrings[sub] = 1
        else:
            total += substrings[sub]
            substrings[sub] += 1

    return total


def sherlockAndAnagrams(s):
    nb_anagrams = 0
    for size in range(1, len(s)):
        nb_anagrams += compute_sized_anagrams(s, size)
    return nb_anagrams


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())

    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)
        fptr.write(str(result) + '\n')
        fptr.close()


if __name__ == '__main__':
    # main()
    print(sherlockAndAnagrams("abba"))

