from typing import List


class Solution:
    """
    Used Example: https://leetcode.com/problems/uncrossed-lines/discuss/651057/Python-by-O(-m*n-)-DP-w-Graph
    """

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        first = [-1] + nums1
        second = [-1] + nums2

        m = len(first)
        n = len(second)

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                if first[i] == second[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[-1][-1]


TEST_CASES = [
    {"nums1": [1, 4, 2], "nums2": [1, 2, 4], "expected": 2},
    {"nums1": [1, 4, 2, 3], "nums2": [1, 2, 3, 4], "expected": 3},
    {"nums1": [2, 5, 1, 2, 5], "nums2": [10, 5, 2, 1, 5, 2], "expected": 3},
    {"nums1": [1, 3, 7, 1, 7, 5], "nums2": [1, 9, 2, 5, 1], "expected": 2},
    {"nums1": [3], "nums2": [3, 3, 2], "expected": 1},
]


def testcase(nums1, nums2, expected):
    result = Solution().maxUncrossedLines(nums1, nums2)
    print(f"Test: {nums1} - {nums2}")
    print(f"Result: {result}, Expected: {expected}")


def main():
    for case in TEST_CASES:
        testcase(**case)


main()
