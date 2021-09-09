from typing import List


class Solution:
    OPENING_CHAR = "("
    CLOSING_CHAR = ")"
    MARKER_A = 1
    MARKER_B = 0

    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        return self.maxDepthAfterSplit_trivial(seq)

    def maxDepthAfterSplit_trivial(self, seq: str) -> List[int]:
        if not seq:
            return [0]
        result = []
        a_depth = 0
        b_depth = 0
        for i, s in enumerate(seq):
            if s == self.OPENING_CHAR:
                if a_depth < b_depth:
                    a_depth += 1
                    result.append(self.MARKER_A)
                else:
                    result.append(self.MARKER_B)
                    b_depth += 1
            elif s == self.CLOSING_CHAR:
                if a_depth < b_depth:
                    b_depth -= 1
                    result.append(self.MARKER_B)
                else:
                    a_depth -= 1
                    result.append(self.MARKER_A)

        return result


TEST_CASES = [
    {"seq": "", "expected": [0]},
    {"seq": "()()()", "expected": [0, 0, 0, 0, 0, 0]},
    {"seq": "(()())", "expected": [0, 1, 1, 1, 1, 0]},
    {"seq": "()(())()", "expected": [0, 0, 0, 1, 1, 0, 0, 0]},
    {"seq": "()(()())((()))", "expected": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]},
]


def testcase(seq, expected):
    result = Solution().maxDepthAfterSplit(seq)
    print(f"Test: {seq}")
    print(f"Result: {result}, Expected: {expected}")


def main():
    for case in TEST_CASES:
        testcase(**case)


main()
