'''
На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. 
Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, чтобы все монетки лежали одной и той же стороной вверх.

Входные данные:
На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх, и равно 1, если i-я монетка лежит решкой вверх. 
Размер списка не превышает 1000 элементов.

Выходные данные:
Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.
Пример использования На входе:

coins = [0, 1, 0, 1, 1, 0]

На выходе: 3
'''
# Решение:
#1. Сравнить, сколько лежит орлои и решкой.
#2. Тех, что меньше - переворачиваем - считаем количество.
#3. Исключения: все 0 и все 1

coins = [0, 1, 0, 1, 1, 0]
#coins = [0, 0, 0, 0, 0, 0, 0]
#coins = [0, 0, 0, 1, 1, 1, 1]

if coins.count(0) & coins.count(1) == len(coins):
    print(0)
    
if coins.count(0) <= coins.count(1):
    print(coins.count(0))

else:
    print(coins.count(1))



