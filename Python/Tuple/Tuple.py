# Tuple (кортеж) - неизменяемый, упорядоченный, обычно хранит значения разных типов, O(1) доступ к элементу.
# Tuple (кортеж) - неизменяемый, потому что как хранил ссылки нв объект, так и хранит.
# Если заранее известен размер, то не используй append, т.к. Python видя изменение, резервирует больше памяти, которая потом не используется.

#................... Две проверки на вхождение элементов:

#a = (1, 2)
#b = (1, 2, 3, 4)
#print(tuple(set(a) & set(b)) == a)
# Output: true


#a = (1, 2, 3, 4)
#b = (1, 2)
#contains_all = all(elem in a for elem in b)
#print(contains_all)


#................... Slicing

"""
tuple = (1, 2, 3, 4, 5)

def slice_func(tuple):
    return tuple[::-1]

print(slice_func(tuple))

"""

#...............Магия изменение кортежа try/exept при неатомарной операции.
'''
new_list = []
tuple = (new_list, 2, 3, 4, 5)

print(tuple)

try:
    tuple[0] += ['oops']  
except:
    pass

print(tuple) 

# На выходе: (['oops'], 2, 3, 4, 5)
# Потому, что += неатомарная операция. Сначала списку присваивается 'oops' (это можно), 
# а потом попытается изменить первый элемент кортежа и упадет с ошибкой.

'''

#new_list = []
#print(dir(new_list))
# Методы List: 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

#tuple = ()
#print(dir(tuple))
# Методы Tuple 'count', 'index'

#string = 'fortran'
#print(dir(string))
#'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 
# 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 
# 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 
# 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 
# 'title', 'translate', 'upper', 'zfill'