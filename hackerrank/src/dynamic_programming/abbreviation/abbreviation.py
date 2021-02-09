#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
# Expected: NO
TEST_CASE_1 = ["AfPZN", "APZNC"]
TEST_CASE_2 = ["AbcDE", "ABDE"]
TEST_CASE_3 = ["beFgH", "EFH"]
TEST_CASE_4 = ["sYOCa", "YOCN"]
# Expected: YES
TEST_CASE_5 = ["AgGN", "AGN"]
# Expected: YES
TEST_CASE_6 = [
    "BFZZVHdQYHQEMNEFFRFJTQmNWHFVXRXlGTFNBqWQmyOWYWSTDSTMJRYHjBNTEWADLgHVgGIRGKFQSeCXNFNaIFAXOiQORUDROaNoJPXWZXIAABZKSZYFTDDTRGZXVZZNWNRHMvSTGEQCYAJSFvbqivjuqvuzafvwwifnrlcxgbjmigkms",
    "BFZZVHQYHQEMNEFFRFJTQNWHFVXRXGTFNBWQOWYWSTDSTMJRYHBNTEWADLHVGIRGKFQSCXNFNIFAXOQORUDRONJPXWZXIAABZKSZYFTDDTRGZXVZZNWNRHMSTGEQCYAJSF"
]
# Expected: NO
TEST_CASE_7 = ["KXzQ", "K"]

sys.setrecursionlimit(10 ** 6)


def is_capitalizable(a, b):
    """
    # TODO: Still has timeouts
    """
    if not b:
        if not a:
            return True
        elif a[0].islower():
            return is_capitalizable(a[1:], b)
        else:
            return False
    elif not a:
        return False

    first_a = a[0]
    first_b = b[0] if b else ''

    if first_a.islower():
        if first_a.upper() == first_b:
            return is_capitalizable(a[1:], b) or is_capitalizable(a[1:], b[1:])
        else:
            return is_capitalizable(a[1:], b)
    elif first_a == first_b:
        return is_capitalizable(a[1:], b[1:])
    else:
        return False


def abbreviation(a, b):
    return 'YES' if is_capitalizable(a, b) else 'NO'


def main():
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())
    for q_itr in range(q):
        a = input()
        b = input()
        result = abbreviation(a, b)
        print(result)
    # fptr.write(result + '\n')

    # result = abbreviation(*TEST_CASE_7)
    # print(result)

    # fptr.close()


if __name__ == '__main__':
    main()
