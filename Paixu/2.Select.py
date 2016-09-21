from tools.array import random_array_unique
from tools.test import is_in_order


def select_sort(nums):
    length = len(nums)
    for i in range(length):
        cur_min = i
        for j in range(i + 1, length):
            if nums[j] < nums[cur_min]:
                cur_min = j
        if cur_min != i:
            nums[i], nums[cur_min] = nums[cur_min], nums[i]
    return nums

# Scenario
x = random_array_unique(20)
print(x)
print(is_in_order(select_sort(x)))