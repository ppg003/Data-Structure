import time
from functools import wraps


def runtime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.clock()
        res = func(*args, **kwargs)
        end = time.clock()
        print("Time : %f" % (end - start))
        return res

    return wrapper
