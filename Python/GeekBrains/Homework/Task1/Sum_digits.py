'''
Найдите сумму цифр трехзначного числа.
'''

n = 12345

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

print(sum_digits(n))

