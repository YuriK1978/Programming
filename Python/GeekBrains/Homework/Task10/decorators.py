# Декоратор дополняет работу функции без изменения ее кода
# Функции - именные и анонимные

from time import time

def decor(func):
    def wrapper(*args, **kwargs):
        sum_time = 0
        for _ in range(1_000_000):
            t1 = time()
            res = func(*args, **kwargs)
            t2 = time()
            sum_time += t2 - t1
        return res, sum_time # return tuple
            
    return wrapper # return function object

    
#@decor               # это синтаксический сахар
def power_i(i, j):
    return i ** j

print(power_i(2, 3))


# @decor
# def get_sum(a, b):
#     return a + b

# print(get_sum(2, 3))

print(decor(power_i)(2, 3)) # обернули без сахара
# Здесь decor подменяет себя на wrapper