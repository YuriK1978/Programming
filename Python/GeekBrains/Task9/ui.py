from logger import input_data, print_data, del_data


def interface():
    print("Добрый день! Вы в бот-справочнике от GeekBrains! \n 1 - запись данных \n 2 - вывод данных \n 3 - удаление данных")
    command = int(input('Введите число '))
    
    while command != 1 and command != 2 and command != 3:
        print("Неправильный ввод")
        command = int(input('Введите число из предложенных '))
    
    if command == 1:
        input_data()
        
    elif command == 2:
        print_data()
    
    elif command == 3:
        del_data()
        
        

