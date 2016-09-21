from tools.array import random_array_unique
from tools.test import is_in_order
import time


def quick_sort(L, low, high):
    i = low
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j - 1
        L[i] = L[j]
        while i < j and L[i] <= key:
            i = i + 1
        L[j] = L[i]
    L[i] = key
    quick_sort(L, low, i - 1)
    quick_sort(L, j + 1, high)
    return L


# Scenario
x = random_array_unique(20)

y = [-1892, 5656, -1854, -8386, 2474, -6352, 3410, 7288, 8285, -3635, 5192, -8577, -4019, -9392, 2091, -3512, -9157,
     -4537, -9512, -3879]
print(x)
print(quick_sort(x, 0, 19))

start = time.clock()
print(is_in_order(quick_sort(x, 0, 19)))
end = time.clock()
print("Time : %f" % (end - start))
