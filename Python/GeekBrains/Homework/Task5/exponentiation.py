'''
Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.

Функция не должна ничего выводить, только возвращать значение.

Пример:
a = 3; b = 5 -> 243 (3⁵)
a = 2; b = 3 -> 8 

'''


def pow(a, b):
    return a if b == 1 else a * pow(a, b - 1)

print(pow(3, 5))



