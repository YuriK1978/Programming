#1) ChainMap нужен для логического объединения словарей для поиска информации, физического копирования словарей не происходит и если изменить один из исходников, то изменении отобразится и в chainMap. 
# Удобен для поиска информации, но при изменениях меняется первый словарь в наборе.

#2) Counter - удобный инструмент для подсчета элементов в последовательности, считает только с hashable типы (строки, числа, кортежи).
# hashable != immutable
#............................................................
#Counter сохраняет все в словари, а ключи словаря хешируемые!
#............................................................

#3) defaultdict нужен для создания словаря со значением по умолчанию. Значение подставляется при обращении к несуществующему ключу, что позволяет не писать лишней логики. В остальном аналогичен обычному словарю.

#4) deque - двунаправленная очередь, быстро вставляет элементы как в конец, так и начало, быстро достает с обоих концов. 
# Она потокобезопасна (thread-safe) и может быть использована для многопоточных операций, позволяет задать максимальный размер.

#5) namedtuple нужен для создания структуры данных, нечто среднее между стандартными типами и самописным классом. 
# Пригодится когда отдельный класс избыточен или ООП пока неизвестно. Неизменяемый, позволяет обращаться по имени атрибута (причем быстро), позволяет использовать индексы.

# ЕЩЕ: ChainMap, Counter, OrdrredDict - реализованы на Python/
# defaultdict, deque, namedtuple - реализованы на Си.                                               


#................конструктор collections.Counter()

#from collections import Counter

#counter = Counter('hello')
#print(counter) # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
#counter.update('world') # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1})
#print(counter.most_common(2)) #два наиболее частотных значения. Без передачи аргумента выводятся все элементы в порядке от наиболее частых к наиболее редким


#............................ChainMap

#from collections import ChainMap

#first = {1: 1, 2: 2, 3: 3}
#second = {4: 4, 5: 5}

#chain = ChainMap(first, second) # ЭТО ЛОГИЧЕСКОЕ ОБЪЕДИНЕНИЕ !!!ChainMap получает только ссылки!!! Память не расходуется!!!
#print(chain)
#print(5 in chain) # Ищет ключ 5, если есть выводит true

#....................................Defaultdict
#from collections import defaultdict

#a_dict = defaultdict(int)
    
#print(a_dict['jhdgfjsdhfg']) # Если мы обращаемся к ключу, которого нет, defaultdict выдаст 0, а не ошибку, как в стандартном словаре.
#print('1' in a_dict) # НО! Если мы спросим, есть ли такой ключ, то defaultdict выдаст false, т.к. его там нет!

#for char in 'hello world':
#    a_dict[char] += 1
    
#print(sorted(a_dict.items(), key = lambda x:x[1], reverse = True)) # !!! полностью совпадает с Counter
# ключ в lambda от 1, т.к. надо сортировать по цифрам (если 0 - то по буквам).
# reverse = True По умолчанию сортируется от маленького к большому, а нам надо наоборот.


#.................Мультисловарь - ключу соответствует список

#from collections import defaultdict

#a_dict = defaultdict(list)
#for char in 'hello':
#    a_dict(char).append(char)
    
#print(a_dict) # Мультисловарь: ключи - буквы, значение - список    

#....................................deque

#from collections import deque

#a_deque = deque()
#a_deque.append(1)
#print(a_deque)
#a_deque.appendleft(2) # вставка в начало работает гораздо быстрее вставки в начало списка (копирование и сдвиг добавляют время)
#print(a_deque)

#..................Добавление со сдвигом при максимальной длине 3.
#a_deque = deque([1, 2, 3], maxlen=3)
#print(a_deque)
#a_deque.append(4)
#print(a_deque)

#..................
#from collections import deque

#with open ('points.csv') as file:
#    a_degue = deque(file, maxlen=2) # передаем любой iterable, а файл есть таковой.

#for line in a_degue:
#    print(line.rstrip()) # rstrip удаляет переносы строк, которые есть в файле
    
# На выходе 0, 0 и 0, 0 на разных чтроках. Эти нули в файле points.csv "вытолкали" все числа (maxlen=2).


#..................namedtuple

#from collections import namedtuple
#tom = ('Tom', 4, 'yellow') - обычный кортеж
#cat = namedtuple('cat', 'name age color')

#tom = cat('Tom', 4, 'yellow')
#print(tom)
#print(tom[0])
#print(tom.name) # можем обратиться по атрибуту, как в простых классах. Здесь забыли про индексы и обратились по имени.
# В namedtuple обращение по атрибуту происходит быстрее, чем в обычных.

#..................
from collections import namedtuple
import csv

Point = namedtuple('Point', 'x, y')
with open ('points.csv') as file:
    for line in csv.reader(file):
        point = Point._make(line)
        print(point)