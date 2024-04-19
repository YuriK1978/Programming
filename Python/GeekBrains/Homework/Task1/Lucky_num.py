'''
: Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет счастливость билета.

385916 -> yes
123456 -> no

'''

print("введите 6-е число")
n = input()

def first_three(n: str) -> int:
    
    first = int(n[0:3])
    s = 0
    while first:
        s += first % 10
        first //= 10
    return s

print(first_three(n))


def second_three(n: str) -> int:
    
    second = int(n[3:])
    s = 0
    while second:
        s += second % 10
        second //= 10
    return s

print(second_three(n))

def comparison(result1: int, result2: int) -> str:
    
    if result1 == result2:
        print("Lucky number!")
    else:
        print("Not a lucky number")
        

comparison(first_three(n), second_three(n))
