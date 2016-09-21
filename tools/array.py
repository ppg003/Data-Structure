import random


def random_array_unique(n, min_num=-10000, max_num=10000):
    list_n = range(min_num, max_num + 1)
    return random.sample(list_n, n)
