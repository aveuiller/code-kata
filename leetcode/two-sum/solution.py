from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements = {ele: i for i, ele in enumerate(nums)}
        for i, ele in enumerate(nums):
            remainder = target - ele
            if remainder in elements and elements[remainder] != i:
                return [i, elements[remainder]]


def testcase_1():
    nums = [2, 7, 11, 15]
    target = 9
    result = Solution().twoSum(nums, target)
    expected = [0, 1]
    print(f"Test: {nums} -> {target}")
    print(f"Result: {result}, Expected: {expected}")


def testcase_2():
    nums = [3, 2, 4]
    target = 6
    result = Solution().twoSum(nums, target)
    expected = [1, 2]
    print(f"Test: {nums} -> {target}")
    print(f"Result: {result}, Expected: {expected}")


def testcase_3():
    nums = [3, 3]
    target = 6
    result = Solution().twoSum(nums, target)
    expected = [0, 1]
    print(f"Test: {nums} -> {target}")
    print(f"Result: {result}, Expected: {expected}")


testcase_1()
testcase_2()
testcase_3()
