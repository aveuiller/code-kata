class Solution:
    ANY_COUNT = "*"
    ANY_CHAR = "."

    def isMatch(self, s: str, p: str) -> bool:
        return self.isMatch_DP(s, p)

    def isMatch_conditional(self, s: str, p: str) -> bool:
        s_pointer = 0
        p_pointer = 0
        while p_pointer < len(p) and s_pointer < len(s):
            if p[p_pointer] == self.ANY_CHAR:
                s_pointer += 1
                p_pointer += 1
            elif p[p_pointer] == self.ANY_COUNT:
                # Greediness missing
                if self.is_last_sequence_char(p, p_pointer, s, s_pointer):
                    p_pointer += 2
                    s_pointer += 1
                elif p[p_pointer - 1] == s[s_pointer] or p[p_pointer - 1] == self.ANY_CHAR:
                    s_pointer += 1
                else:
                    p_pointer += 1
            else:
                if p[p_pointer] != s[s_pointer]:
                    if p[p_pointer + 1] == self.ANY_COUNT:
                        p_pointer += 2
                    else:
                        return False
                else:
                    p_pointer += 1
                    s_pointer += 1

        return s_pointer == len(s) and (p_pointer == len(p) or p[-1] == self.ANY_COUNT)

    def is_last_sequence_char(self, p, p_pointer, s, s_pointer):
        next_s_is_empty_or_different = (s_pointer + 1 < len(s) and s[s_pointer + 1] != s[
            s_pointer]) or s_pointer + 1 == len(s)
        next_p_is_matching = p_pointer + 1 < len(p) and p[p_pointer + 1] == s[s_pointer]
        return next_p_is_matching and next_s_is_empty_or_different

    def isMatch_DP(self, s: str, p: str) -> bool:
        """
        Solution from
        https://leetcode.com/problems/regular-expression-matching/discuss/1006875/Python-or-Simple-DP-or-w-Video-Reference-and-Comments
        """
        # base case
        if '*' not in p and '.' not in p:
            return s == p

        # setup dp table
        m = len(s) + 1
        n = len(p) + 1

        # dp[i][j] represents if s[:i] matches the pattern p[:j]
        dp = [[False for _ in range(n)] for _ in range(m)]

        # empty string matches empty string
        dp[0][0] = True

        # This deals with patterns like a* or a*b* or a*b*c*
        for i in range(1, len(dp[0])):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]

        for i in range(1, m):
            for j in range(1, n):
                # if current pattern is a dot
                # or if current pattern has same character
                # as current text then the answer is the one
                # diagonally above(removing both chars)
                if p[j - 1] == '.' or (s[i - 1] == p[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1]

                # if its a star then it gets intresting.
                # first its automatically equal to [i][j-2]
                # since thats accounting for the STAR being of 0 length
                # aka a* being ''(empty). Then if that doesnt work
                # if the pattern is a dot(accounting for .*) or
                # previous pattern before * is simmilar as text
                # then its the answer above since your accounting for
                # removing last char of text
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = (dp[i][j] or dp[i - 1][j])
                    # else false by default

        # answer in last column/row
        return dp[-1][-1]


TEST_CASES = [
    {"s": "aa", "p": "a", "expected": False},
    {"s": "aa", "p": "a*", "expected": True},
    {"s": "ab", "p": ".*", "expected": True},
    {"s": "aab", "p": "c*a*b", "expected": True},
    {"s": "mississippi", "p": "mis*is*p*.", "expected": False},
    {"s": "abcd", "p": ".*e", "expected": False},
    {"s": "aaa", "p": "a*a", "expected": True},
    {"s": "aaa", "p": "ab*a*c*a", "expected": True},
]


def testcase(s, p, expected):
    result = Solution().isMatch(s, p)
    print(f"Test: {s} - {p}")
    print(f"Result: {result}, Expected: {expected}")


def main():
    for case in TEST_CASES:
        testcase(**case)


main()
