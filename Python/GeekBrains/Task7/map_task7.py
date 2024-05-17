
# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

'''
Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя используется 
пробел. Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?

'''
data = '15 156 96 3 5 8 52 5'

# data = data.split()
# print(data)

data = list(map(int, data.split()))
print(data)