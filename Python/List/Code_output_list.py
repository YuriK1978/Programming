# !!! Изменяемые типы для аргумента по умолчанию - ЗЛО!!!
# Они будут преследовать нас на протяжении всей программы.
# Исправить тпк: none в аргументе, в теле проверка на none. 
# Смотри пример List\default_argument.py

def extend_list(value, lst = []):
    lst.append(value)
    return lst

list1 = extend_list(10)
list2 = extend_list(123, [])
list3 = extend_list('a') 

print(list1) 
print(list2) 
print(list3) 

# Output:
#[10, 'a']
#[123]
#[10, 'a']