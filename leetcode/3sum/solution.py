from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.threeSum_pointers(nums)

    def threeSum_pointers(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for k, pivot in enumerate(nums):
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            i = k + 1
            j = len(nums) - 1
            while i < j:
                three_sum = nums[i] + nums[j] + pivot
                if three_sum > 0:
                    j -= 1
                elif three_sum < 0:
                    i += 1
                else:
                    triplet = [nums[i], nums[j], nums[k]]
                    result.append(triplet)
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1
        return result

    def threeSum_bigSpace(self, nums: List[int]) -> List[List[int]]:
        two_sums = dict()
        for i, ele1 in enumerate(nums):
            for j, ele2 in enumerate(nums):
                if i != j:
                    remainder = - (ele2 + ele1)
                    indexes = two_sums.setdefault(remainder, [])
                    indexes.append([i, j])

        result = []
        for k, ele in enumerate(nums):
            indexes = two_sums.get(ele)
            if indexes:
                for two_indexes in indexes:
                    if k not in two_indexes:
                        triplet = [nums[ind] for ind in two_indexes] + [ele]
                        triplet.sort()
                        if triplet not in result:
                            result.append(triplet)
        result.sort()
        return result


TEST_CASES = [
    {"nums": [-1, 0, 1, 2, -1, -4], "expected": [[-1, -1, 2], [-1, 0, 1]]},
    {"nums": [], "expected": []},
    {"nums": [0], "expected": []},
    {"nums": [3, 0, -2, -1, 1, 2], "expected": [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]},
    {"nums": [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4],
     "expected": [[-4, 0, 4], [-4, 1, 3], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, -1, 2],
                  [-1, 0, 1]]},
]


def testcase(nums, expected):
    result = Solution().threeSum(nums)
    print(f"Test: {nums}")
    print(f"Result: {result}, Expected: {expected}")


def main():
    for case in TEST_CASES:
        testcase(**case)


main()
