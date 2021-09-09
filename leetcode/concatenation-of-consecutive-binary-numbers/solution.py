import math


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binary = "".join(self.to_binary(i) for i in range(1, n + 1))
        return int(self.to_decimal(binary) % 1_000_000_007)

    def to_binary(self, n: int) -> str:
        return bin(n)[2:]

    def to_decimal(self, binary) -> int:
        return int(binary, 2)


TEST_CASES = [
    {"n": 1, "expected": 1},
    {"n": 3, "expected": 27},
    {"n": 12, "expected": 505379714},
    {"n": 42, "expected": 727837408},
]


def testcase(n, expected):
    result = Solution().concatenatedBinary(n)
    print(f"Test: {n}")
    print(f"Result: {result}, Expected: {expected}")


def main():
    for case in TEST_CASES:
        testcase(**case)


main()
