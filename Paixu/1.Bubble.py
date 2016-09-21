from tools.array import random_array_unique
from tools.test import is_in_order
from tools.runtime import runtime

@runtime
def bubble_sort(nums):
    length = len(nums)
    swap = True
    while swap:
        swap = False
        for i in range(length - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swap = True
    return nums

# Scenario
x = random_array_unique(20)
print(x)
print(is_in_order(bubble_sort(x)))
