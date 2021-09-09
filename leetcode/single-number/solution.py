from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_occurrence = set()
        multiple_occurrence = set()
        for ele in nums:
            if ele in multiple_occurrence:
                pass
            if ele in single_occurrence:
                single_occurrence.remove(ele)
                multiple_occurrence.add(ele)
            else:
                single_occurrence.add(ele)
        return single_occurrence.pop()


TEST_CASES = [
    {"nums": [2, 2, 1], "expected": 1},
    {"nums": [4, 1, 2, 1, 2], "expected": 4},
    {"nums": [4, 1, -1, 2, 1, 2, 5, 5, 6, -1, 4], "expected": 6},
    {"nums": [1], "expected": 1},
]


def testcase(nums, expected):
    result = Solution().singleNumber(nums)
    print(f"Test: {nums}")
    print(f"Result: {result}, Expected: {expected}")


def main():
    for case in TEST_CASES:
        testcase(**case)


main()
