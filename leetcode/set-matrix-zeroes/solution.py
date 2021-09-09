from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zeroing_lines = set()
        zeroing_columns = set()
        for i, line in enumerate(matrix):
            for j, cell in enumerate(line):
                if cell == 0:
                    zeroing_lines.add(i)
                    zeroing_columns.add(j)

        for zeroing_line in zeroing_lines:
            matrix[zeroing_line] = [0 for _ in range(n)]
        for zeroing_column in zeroing_columns:
            for i in range(m):
                matrix[i][zeroing_column] = 0


TEST_CASES = [
    {"matrix": [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], "expected": [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]},
]


def testcase(matrix, expected):
    print(f"Test: {matrix}")
    Solution().setZeroes(matrix)
    print(f"Result: {matrix}, Expected: {expected}")


def main():
    for case in TEST_CASES:
        testcase(**case)


main()
