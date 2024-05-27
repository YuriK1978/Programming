
from time import time

# декоратор с параметром

def outer(param):
    def decor(func):
        def wrapper(*args, **kwargs):
            sum_time = 0
            for _ in range(param):
                t1 = time()
                res = func(*args, **kwargs)
                t2 = time()
                sum_time += t2 - t1
            return res, sum_time     
        return wrapper 
    return decor

    
#@outer(1_000_000)
def power_i(i, j):
    return i ** j

print(power_i(2, 3))

# без сахара rem строка 20.
print(outer(1_000_000)(power_i)(2, 3))