def is_in_order(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


def same_element(nums1, nums2):
    if len(nums1) != len(nums2):
        return False

    if set(nums1) != set(nums2):
        return False

    return True
