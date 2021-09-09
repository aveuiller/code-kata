from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        i = 1
        while i < len(intervals):
            if intervals[i][0] < intervals[i - 1][1]:
                intervals.pop(i)
                count += 1
            else:
                i += 1
        return count


TEST_CASES = [
    {"intervals": [[1, 2], [2, 3], [3, 4], [1, 3]], "expected": 1},
    {"intervals": [[1, 2], [1, 2], [1, 2]], "expected": 2},
    {"intervals": [[1, 2], [2, 3]], "expected": 0},
    {"intervals": [[1, 2], [2, 3], [3, 4], [-100, -2], [5, 7]], "expected": 0},
    {"intervals": [[1, 2], [2, 3], [3, 4], [-100, -2], [5, 7], [-50, -2]], "expected": 1},
    {"intervals": [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]], "expected": 2},
]


def testcase(intervals, expected):
    result = Solution().eraseOverlapIntervals(intervals)
    print(f"Test: {intervals}")
    print(f"Result: {result}, Expected: {expected}")


def main():
    for case in TEST_CASES:
        testcase(**case)


main()
