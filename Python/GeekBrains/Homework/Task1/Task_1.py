"""
    Найдите сумму цифр трехзначного числа n.
    Результат сохраните в перменную res.
"""

n = 123
first_num = n // 100
second_num = n // 10 % 10
last_num = n % 10
res = first_num + second_num + last_num

print(res)
