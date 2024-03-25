from array import array
#a = array("i", [1, 2, 2, 3, 4, 5])
#b = array("i", [6, 7, 8])

#print(a)
#print(a[0])
#print(a[-1])
#print(a[1:-1])

#print(a[::-1]) # Reverse
#b = a.reverse() # Вернет none type, потому что reverse не возвращает никакого значения
#print(type(b)) 
#print(a.typecode) # Вернет тип массива - i, т.к. тип массива int.

#print(a*2)
#print(a + b)

#print(a.itemsize) # Вернет размер в байтах - 4.
#print(a.count(2)) # Вернет 2 - количество двоек в массиве - т.е. 2 двойки.

#c = a.tolist() # Вернет список
#print(c)
#print(type(c))

#print(a.index(2)) # Вернет индекс двойки - 1.

#a.insert(1, 555) # Добавление 555 в индекс 1.
#print(a)

# Заменить все четные элементы массива на 555.

a = array("i", list(range(25)))
for value in a:
    if value % 2 == 0:
        a[a.index(value)] = 555 # внутри [индекс]. Полуаем: a[от четного индекса] = 555.
print(a)