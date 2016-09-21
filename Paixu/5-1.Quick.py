from tools.array import random_array_unique
from tools.test import is_in_order
from tools.test import same_element
import time


def quick_sort(A):
    length = len(A)
    index_pivot = 0
    index_right = length

    if length in [0, 1]:
        return A

    pivot = A[index_pivot]
    print("pivot : %s" % pivot)

    if length == 2:
        if A[0] > A[1]:
            A[0], A[1] = A[1], A[0]
        return A

    for i in range(length):
        if A[i] > pivot:
            index_right = i
            # print("index right : %s" % index_right)
            break

    for i in range(index_right + 1, length):
        if A[i] < pivot:
            A[index_right], A[i] = A[i], A[index_right]
            index_right += 1
    if index_right == 0:
        A[index_pivot], A[length - 1] = A[length - 1], A[index_pivot]
        index_right = length
    else:
        A[index_pivot], A[index_right - 1] = A[index_right - 1], A[index_pivot]
    print("nums : %s" % A)
    print("index right : %s" % index_right)
    nums_left = A[index_pivot:index_right - 1]
    nums_right = A[index_right:len(A) + 1]
    print("left : %s" % nums_left)
    print("right : %s" % nums_right)

    A = quick_sort(nums_left) + [pivot] + quick_sort(nums_right)

    return A


# Scenario
x = random_array_unique(20)

y = [-1892, 5656, -1854, -8386, 2474, -6352, 3410, 7288, 8285, -3635, 5192, -8577, -4019, -9392, 2091, -3512, -9157,
     -4537, -9512, -3879]

z = [5, 4, 3, 2]

z2 = [5, 7, 9, 2, 6, 1, 4]
print(z)
z_sort = quick_sort(z)
print(z_sort)
print(same_element(z, z_sort))

start = time.clock()
print(is_in_order(quick_sort(z)))
end = time.clock()
print("Time : %f" % (end - start))
