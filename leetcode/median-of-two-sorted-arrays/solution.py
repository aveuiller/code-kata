from math import ceil
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median_index = ((len(nums1) + len(nums2)) // 2) + 1
        pair_elements_amount = (len(nums1) + len(nums2)) % 2 == 0
        i = 0
        j = 0
        previous = None
        current = None

        if not nums1 and not nums2:
            return 0

        while i + j != median_index:
            previous = current
            if j >= len(nums2) or (i < len(nums1) and nums1[i] < nums2[j]):
                current = nums1[i]
                i += 1
            else:
                current = nums2[j]
                j += 1

        return (previous + current) / 2 if pair_elements_amount else current


TEST_CASES = [
    {"nums1": [1, 3], "nums2": [2], "expected": 2},
    {"nums1": [1, 2], "nums2": [3, 4], "expected": 2.5},
    {"nums1": [0, 0], "nums2": [0, 0], "expected": 0},
    {"nums1": [], "nums2": [1], "expected": 1},
    {"nums1": [2], "nums2": [], "expected": 2},
    {"nums1": [], "nums2": [], "expected": 0},
]


def testcase(nums1, nums2, expected):
    result = Solution().findMedianSortedArrays(nums1, nums2)
    print(f"Test: {nums1} - {nums2}")
    print(f"Result: {result}, Expected: {expected}")


def main():
    for case in TEST_CASES:
        testcase(**case)


main()
