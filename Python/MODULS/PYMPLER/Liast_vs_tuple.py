from pympler import asizeof
import dis
from timeit import timeit


print(timeit("list()"))
print(timeit("tuple()"))
print(asizeof.asizeof(list()))
print(asizeof.asizeof(tuple()))

print(timeit("list()"))
print(timeit("[]")) # - в два раза быстрее

dis.dis("list()")
dis.dis("[]")
