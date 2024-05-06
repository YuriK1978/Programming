# 1
from functools import reduce
print(reduce(lambda a, b: a + b, [1, 2, 3]))
# Output: 6
'''
Например reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) вычисляет ((((1 + 2) +3) +4) +5). 
Левый аргумент x - это накопленное значение, а правый аргумент y - это следующий элемент iterable.
'''


# 2
