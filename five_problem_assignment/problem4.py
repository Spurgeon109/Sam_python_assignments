import time
import datetime
import logging
from functools import wraps

def log_decorator(f):
    logging.basicConfig(filename='{}'.format(f.__name__), level = logging.INFO)
    @wraps(f)
    def inner(*args, **kwargs):
        logging.info("{0} function time stamp: {1}".format(f.__name__, datetime.datetime.now()))
        return f(*args, **kwargs)
    return inner


def time_decorator(f):
    @wraps(f)
    def inner(*args, **kwargs):
        t1 = time.perf_counter()
        f(*args, **kwargs)
        t2 = time.perf_counter() - t1
        print("{0} function Ran in {1}".format(f.__name__, t2))
        print("check {0}.log file for log info".format(f.__name__))
    return inner


@log_decorator
@time_decorator
def print_sqr(li):
    print("Original function name is print_sqr. It just prints the squares of {}".format(li))
    print("===================")
    print(list(map(lambda x : x * x, li)))
    print("===================")


print_sqr([1, 2, 3, 4, 5])