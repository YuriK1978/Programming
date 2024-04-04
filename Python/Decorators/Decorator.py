from time import perf_counter
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        res = func(*args, **kwargs)
        print(perf_counter() - start)
        return res
    return wrapper

@timer
def func(a, b):
    return a + b

print(func(5, 10))

        
        