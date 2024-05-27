# класс данных и тип данных это одно и то же:

# a = 3
# print(type(a))
# print(a.__class__)

# class Car:
#     pass

# c1 = Car()
# print(c1) #<__main__.Car object at 0x000001C95AB49C70>
# c2 = Car()
# print(c2) #<__main__.Car object at 0x0000022C39AB9D00>
# print(type(c1)) #<class '__main__.Car'>

from time import time
class Decor:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            sum_time = 0
            for _ in range(1_000_000):
                t1 = time()
                res = func(*args, **kwargs)
                t2 = time()
                sum_time += t2 - t1
            return res, sum_time   
        return wrapper
  
#@Decor() уходим от сахара
def power_i(i, j):
    return i ** j

print(power_i(2, 3))
# Decor() - создание экземпаляра класса Decor
# (power_i) - вызов его как функции
print(Decor()(power_i)(2, 3))


# a = 3
# print(type(a))
# print(a.__class__)

# class Car:
#     def __call__(self): # перегрузка метода соот-го операции вызова экземпляра класса как функции
#         print('hello!')

# c1 = Car()
# print(c1) 
# c2 = Car()
# print(c2) 
# print(type(c1)) 

# c1()