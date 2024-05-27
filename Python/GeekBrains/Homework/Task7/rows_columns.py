'''
Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, 
вычисляющую элемент по номеру строки и столбца. По умолчанию номер столбца и строки = 9.

Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.

Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

Если строк меньше двух, выдайте текст
ОШИБКА! Размерности таблицы должны быть больше 2!.

Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

Между элементами должен быть 1 пробел, в конце строки пробел не нужен.

Пример

На входе:
print_operation_table(lambda x, y: x * y, 3, 3)
На выходе:

1 2 3
2 4 6 
3 6 9
'''

# Решение:
# n - число столбцов (элементов в строке) и строк (итераций первой строки)
# Первая строка от 1 до 6
# Вторая (2) строка - первая (1), умноженная на 2
# Третья (3) строка - первая (1), умноженная на 3
# ...
# Шестая (6) строка - первая (1), умноженная на 6


# def print_operation_table(operation, num_rows, num_columns): 
#     for i in range(1, num_rows + 1): 
#         a = [] 
#         for j in range(1, num_columns + 1): 
#             a.append(str(operation(i, j))) 
        
#         print(" ".join(f"{e:<4}" for e in a)) 
    
# print_operation_table(lambda x, y: x * y, 3, 3)


# Вариант stackoverflow:

# from math import log10

# def printOperationTable(operation, numRows, numColumns):
#     if operation(1,1)==2:
#         print(1,end='\t')

#     colSize = int(log10(operation(numRows+1, numColumns+1)))+2

#     for row in range(1, numRows+1):
#         for column in range(1, numColumns+1):
#             if operation(1,1)==2:
#                 column=column-1
#             print("{:>{}}".format(operation(row,column), colSize), end='\t')
#         print()  

# printOperationTable(lambda x,y: x*y, 3, 3)

# Вариант 2
# def print_operation_table(operation, numRows, numColumns):
#     if numRows >2:
#         for row in range(1, numRows+1):
#             for column in range(1, numColumns+1):
#                 print(operation(row,column), end='\t')
#             print()
#     else:
#         print("error")
        
# print_operation_table(lambda x,y: x*y, 3, 3)


# Вариант принятый системой.

def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows < 3 or num_columns < 3:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        lst = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
        for i in lst:
            print(*[f'{x}' for x in i])