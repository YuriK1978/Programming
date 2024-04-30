'''
Дана последовательность из N целых чисел и число 
K. Необходимо сдвинуть всю последовательность 
(сдвиг - циклический) на K элементов вправо, K – 
положительное число.

Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
'''
# list1 = [5, 4, 6, 7, -10]
# k = int(input())
# k = k % len(list1) # Если к = длине списка, сдви на еденицу.

# list_res = []

# for i in range(k):
#     list_res.append(list1[len(list1) - 1 - i]) # -1: т.к. начинаем с нулевого индекса
# print(list_res)

# for i in range(len(list1) - k): # -к, т.к. первые к-элементов уже записали в первом цикле
#     list_res.append(list1[i])
# print(list_res)
   

# Второй вариант - короткий.

a = [1, 2, 3, 4, 5]
print(a)
k = 3
for i in range(k):
    a.append(a.pop(0))
print(a)