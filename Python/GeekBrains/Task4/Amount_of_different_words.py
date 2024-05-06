'''
Пользователь вводит текст(строка). Словом считается 
последовательность непробельных символов идущих 
подряд, слова разделены одним или большим числом 
пробелов. Определите, сколько различных слов 
содержится в этом тексте.

Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells

Output: 13
'''

# stroka = input().split()

# set_1 = set()

# for i in stroka:
#     set_1.add(i.lower())

# print(len(set_1))

# Вариант №2 со знаками препинания
import string

text = "Gfg, is best: for ! Geeks ; gfG is best : for! gEeks;" 

for punctuation in string.punctuation:
    text = text.replace(punctuation, '') # убираем знаки препинания в нашей строке для корректной работы

print(text) 
res = set()
text = text.split()
for i in text:
    res.add(i.lower()) # переводим в нижний регистр каждое слово и добавляем во множество
        
print(len(res)) # считаем длину списка и выводим в консоль