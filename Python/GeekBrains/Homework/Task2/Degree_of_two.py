'''
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

10 -> 1 2 4 8

2**0 = 1
2**1 = 2
2**2 = 4
2**3 = 8
2**4 = 16 > 10
'''
n = 10
i = 0
res = 0
while res <= n:
        res = 2**i 
        if res <= n:
                print(res)
                i = i + 1 
    
    
    
