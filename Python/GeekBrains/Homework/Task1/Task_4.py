"""
Определите, можно ли от шоколадки размером a × b долек отломить c долек, если разрешается сделать один разлом по прямой
между дольками (то есть разломить шоколадку на два прямоугольника).

Выведите yes или no соответственно.
"""

a, b, c, = 3, 2, 6

if (c % a == 0 or c % b == 0) and a * b >= c:
    print('yes')
else:
    print('no')
