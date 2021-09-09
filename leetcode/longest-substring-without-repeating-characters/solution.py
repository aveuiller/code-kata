class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxsize = 0
        for lower_index, letter in enumerate(s):
            upper_index = lower_index
            while upper_index + 1 < len(s) and s[upper_index + 1] not in s[lower_index:upper_index + 1]:
                upper_index = upper_index + 1
            maxsize = max(maxsize, upper_index - lower_index + 1)
        return maxsize


def testcase_1():
    entry = "abcabcbb"
    result = Solution().lengthOfLongestSubstring(entry)
    expected = 3
    print(f"Test: {entry}")
    print(f"Result: {result}, Expected: {expected}")


def testcase_2():
    entry = "bbbbb"
    result = Solution().lengthOfLongestSubstring(entry)
    expected = 1
    print(f"Test: {entry}")
    print(f"Result: {result}, Expected: {expected}")


def testcase_3():
    entry = "pwwkew"
    result = Solution().lengthOfLongestSubstring(entry)
    expected = 3
    print(f"Test: {entry}")
    print(f"Result: {result}, Expected: {expected}")


testcase_1()
testcase_2()
testcase_3()
