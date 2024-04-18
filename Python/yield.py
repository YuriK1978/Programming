#Любая функция, содержащая ключевое слово yield является функцией-генератором (независимо от наличия return) и при вызове возвращает объект-генератор.
#Важные моменты:
#1) ленивый, не выполняется пока не попросить значение
#2) одноразовый -при исчерпании кидает StopIteration (в for этого не видно, ибо for обрабатывает внутри и не показывает)
#3) после выполнения yield встает на паузу, при этом сохраняет все внутреннее состояние (аргументы, локальные переменные)
#4) при повторном запросе (next) продолжает работу с места остановки
#5) внутри объекта генератора инкапсулирована логика - что он должен делать
#Удобен при работе с большими данными, но и в целом может применяться там, где нам нужно получать наборы данных, обрабатывать их.

'''
squares = (e ** 2 for e in range(0, 11, 2))

def squares2():
    for e in range(0, 11, 2):
        yield e ** 2

        
gen = squares2()
print(next(gen)) # output: 0
'''
squares = (e ** 2 for e in range(0, 11, 2))

def squares2():
    for e in range(0, 11, 2):
        yield e ** 2
        
def pause():
    print("generator is working")
    while True:
        print(a)
        yield a
        
a = 10
gen = pause()
print(next(gen))
a = 20
print(next(gen))
