from tools.array import random_array_unique
from tools.test import is_in_order


def insert_sort(nums):
    length = len(nums)
    for i in range(1, length):
        for j in range(i):
            if nums[i - j - 1] > nums[i]:
                if nums[i - j - 2] <= nums[i] or i - j == 1:
                    temp = nums[i]
                    for k in range(i, i - j - 1, -1):
                        nums[k] = nums[k - 1]
                    nums[i - j - 1] = temp
    return nums


# Scenario
x = random_array_unique(20)
print(x)
print(is_in_order(insert_sort(x)))
