# !!! При создании пустого словаря используй {}, как в листе.

#my_dict = {'a': 1, 'b': 2, 'c': 3}
#keys = my_dict.keys() #получение представления ключей словаря

#for key in keys:
#    print(key)
    
#if 'a' in keys:
#    print('ключ \'а\' есть в словаре')
#else:
#    print('ключа \'а\' нет в словаре')



#...........Сортировка списка словарей
import operator

users = [
    {'name': 'Вася', 'salary': '100', 'age': 20},
    {'name': 'Петя', 'salary': '200', 'age': 25},
    {'name': 'Саша', 'salary': '200', 'age': 30},
    {'name': 'Маша', 'salary': '300', 'age': 24},
]
   
for item in sorted(users, key = operator.itemgetter('salary', 'age'), reverse = True):
    print(item)
                
