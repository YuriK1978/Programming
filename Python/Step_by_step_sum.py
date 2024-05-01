'''
[1, 2, 3, 4, 5] => [1, 3, 6, 10, 15] : 1+2=3, 1+2+3=6, 1+2+3+4=10, 1+2+3+4+5=15

'''

# Junior solution

list = [1, 2, 3, 4, 5]
list_rez = []
sum_ = 0
i = 0
while i < len(list):
    sum_ = sum_ + list[i]
    list_rez.append(sum_)
    i += 1


print(list_rez)


# Middle solution

