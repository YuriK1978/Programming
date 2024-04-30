
import sys
from pympler import asizeof



list = []
# shallow size
print(sys.getsizeof(list))
# deep size
print(asizeof.asizeof(list))


# shallow size
tuple = ()
print(sys.getsizeof(tuple))
# deep size
print(asizeof.asizeof(tuple))


# shallow size
dict = {}
print(sys.getsizeof(dict))
#deep size
print(asizeof.asizeof(dict))