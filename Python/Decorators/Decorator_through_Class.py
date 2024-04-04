from time import perf_counter
from functools import update_wrapper # update для сохранения какой-то инфо

class Timer:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func
        
    def __call__(self, *args, **kwargs):
        start = perf_counter()
        res = self.func(*args, **kwargs)
        print(perf_counter() - start)
        return res

@Timer
def func(a, b):
    return a + b

print(func(10, 5)) 

    
        

        