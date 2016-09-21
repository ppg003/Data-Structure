from tools.array import random_array_unique
from tools.test import is_in_order


def merge(left, right):
    res = []
    length_left = len(left)
    length_right = len(right)
    i, j = 0, 0
    while i < length_left and j < length_right:
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    while i < length_left:
        res.append(left[i])
        i += 1

    while j < length_right:
        res.append(right[j])
        j += 1

    return res


def merge_sort(nums):
    length = len(nums)
    len_sublist = 1
    while len_sublist <= length:
        len_sublist_2 = len_sublist * 2
        left = nums[:len_sublist]
        # print("left : %s" % left)
        if len_sublist_2 <= length:
            # print("lll : %s" % nums[len_sublist:len_sublist_2])
            right = merge_sort(nums[len_sublist:len_sublist_2])
        else:
            # print("lll : %s" % nums[len_sublist:])
            right = merge_sort(nums[len_sublist:])
        # print("right : %s" % right)
        # print("lr : %s" % merge(left, right))
        nums = merge(left, right) + nums[len_sublist_2:]
        # print("nums : %s" % nums)
        len_sublist = len_sublist_2
        # print("length : %s" % len_sublist)
    return nums


# Scenario
x = random_array_unique(20)
print(x)
print(merge_sort(x))
print(is_in_order(merge_sort(x)))
