'''
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. 
В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.

На входе:
s = 12
p = 27

На выходе:
3 9
'''

s = 12
p = 27

for x in range(s):
    for y in range(p):
        if s == x + y and p == x * y:
            print(f'первое число ="{x}", второе число ="{y}"')

#Второй вариант:

# res = []
# for i in range(a + b):
#     if i == (a * i - b)**0.5:
#         res.append(i)
# print(*res if len(res) == 2 else res + res)