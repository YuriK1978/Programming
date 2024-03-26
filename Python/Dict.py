my_dict = {'a': 1, 'b': 2, 'c': 3}

keys = my_dict.keys() #получение представления ключей словаря

for key in keys:
    print(key)
    
if 'a' in keys:
    print('ключ \'а\' есть в словаре')
else:
    print('ключа \'а\' нет в словаре')



