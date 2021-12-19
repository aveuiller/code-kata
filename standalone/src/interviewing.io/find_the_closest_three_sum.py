# E.g. [-1, 2, 1, -4], target = 1
import math


# https://www.youtube.com/watch?v=3O7GMz5D7pU
def closest_three_sum(nums, target):
    # return closest_n_sum_recursive(nums, 3, target)
    return closest_three_sum_iterative(nums, target)


def closest_three_sum_iterative(nums, target):
    nums.sort()
    result = math.inf
    for i in range(len(nums)):
        selected = nums[i]
        result = min(result, selected + closest_two_sum_iterative(nums[i + 1:], target - selected))
    return result


def closest_two_sum_iterative(nums, target):
    a = 0
    b = len(nums) - 1
    diff = math.inf
    closest = 0

    while a < b:
        new_sum = nums[a] + nums[b]
        new_diff = abs(target - new_sum)
        if new_diff < diff:
            closest = new_sum
            diff = new_diff

        if new_sum > target:
            b -= 1
        else:
            a += 1
    return closest


def closest_n_sum_recursive(nums, n, target):
    if n <= 0 or not nums or len(nums) < n:
        return math.inf

    if n == 2:
        return closest_two_sum_iterative(nums, target)

    # if n == 1:
    #     closest = nums[0]
    #     for val in nums[1:]:
    #         if abs(target - value - val) < abs(target - value - closest):
    #             closest = val
    #     return value + closest

    remaining_nums = nums
    closest = math.inf
    for i in range(len(nums)):
        selected = nums[i]
        remaining_nums = remaining_nums[:i] + remaining_nums[i + 1:]

        if not remaining_nums:
            break

        found = selected + closest_n_sum_recursive(remaining_nums, n - 1, target - selected)
        if abs(target - found) < abs(target - closest):
            closest = found

        if found == target:
            return found

    return closest


def main():
    print(closest_three_sum([-1, 2, 1, -4], 1))  # Expected 2
    # print(closest_three_sum([-1, 2, 1, -4], 2))  # Expected 2
    # print(closest_three_sum([-1, 2, 1, -4], 3))  # Expected 2
    # print(closest_three_sum([-1, -2, 1, 4], -10))  # Expected -2


if __name__ == '__main__':
    main()
