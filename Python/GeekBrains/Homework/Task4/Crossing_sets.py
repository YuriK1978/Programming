'''
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
На вход подается 2 числа через пробел: n m
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

Пример

На входе:


var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел
На выходе:


3 5
'''


var2 = '10 30 50 70 90' 
var3 = '10 20 30 40 50' 


numbers_n = set(list(map(int, var2.split())))
numbers_m = set(list(map(int, var3.split())))

# Вариант1
for i in numbers_n:
    if i in numbers_m:
        print(i, end=' ')

# Вариант2
# a = sorted(numbers_n & numbers_m)
# for i in a:
#     print(i, end=' ')

