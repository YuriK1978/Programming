#................... Две проверки на вхождение элементов:

#a = (1, 2)
#b = (1, 2, 3, 4)
#print(tuple(set(a) & set(b)) == a)
# Output: true


a = (1, 2, 3, 4)
b = (1, 2)
contains_all = all(elem in a for elem in b)
print(contains_all)


#................... 