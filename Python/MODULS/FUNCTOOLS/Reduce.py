'''
from functools import reduce

reduce(function, iterable[, initializer])

    function - пользовательская функция, принимающая 2 аргумента,
    iterable - итерируемая последовательность,
    initializer - начальное значение.

'''


# 1 Максимум с помощью reduce:
# from functools import reduce
# items = [1, 24, 17, 14, 9, 32, 2]
# reduce(lambda a,b: a if (a > b) else b, items)

# 2 Вычисление суммы всех элементов списка при помощи reduce() и lambda-функции:
from functools import reduce
items = [10, 20, 30, 40, 50]
reduce(lambda x,y: x + y, items)

