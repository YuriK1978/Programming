# Реализовать функцию merge, которая принимает на вход два списка и возвращает словарь.
# Ключ из первого списка, значение из второго, упорядоченных по ключам (значений может быть больше, мы их откинем)

'''

lst1 = [6, 1, 2, 3, 7, 4, 5]
lst2 = ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'h', 'i', 'j']

def merge(keys, values):
    my_dct = dict(zip(keys, values))
    return dict(sorted(my_dct.items()))

print(merge(lst1, lst2))

'''
#Решение с оптимизацией: в sorted отправить zip:


lst1 = [6, 1, 2, 3, 7, 4, 5]
lst2 = ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'h', 'i', 'j']

def merge(keys, values):
    return dict(sorted(zip(keys, values)))

print(merge(lst1, lst2))



