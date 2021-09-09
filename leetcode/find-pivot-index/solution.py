from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1


TEST_CASES = [
    {"nums": [1, 7, 3, 6, 5, 6], "expected": 3},
    {"nums": [1, 2, 3], "expected": -1},
    {"nums": [2, 1, -1], "expected": 0},
    {"nums": [-1, -1, -1, -1, -1, 0], "expected": 2},
]


def testcase(nums, expected):
    result = Solution().pivotIndex(nums)
    print(f"Test: {nums}")
    print(f"Result: {result}, Expected: {expected}")


def main():
    for case in TEST_CASES:
        testcase(**case)


main()
