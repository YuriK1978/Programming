
# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))

# print(res)

# Файл Pairs_in_list.py перепишем с помощью map and filter:

data = [1, 2, 3, 5, 8, 15, 23, 38]     

res = map(int, data)

res = filter(lambda x: x % 2 == 0, res)

res = list(map(lambda x: (x, x**2), res))
print(res)