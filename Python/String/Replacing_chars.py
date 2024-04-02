'''
Метод str.translate() позволяет заменить символы в строке с помощью заданной таблицы перевода. 
Это удобно для замены или удаления определенных символов из строки.

Синтаксис:

new_string = str.translate(table)

где:
str - это строка, к которой применяется метод translate();
table - это таблица перевода, которая должна быть создана с помощью метода str.maketrans().


text = 'Python tech code'
table
'''

text = 'Python tech code'
table = str.maketrans("eoy", '***')
result = text.translate(table)

print(result)