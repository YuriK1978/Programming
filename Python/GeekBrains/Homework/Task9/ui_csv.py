from logger_csv import input_data, print_data, del_data, update_data


def interface():
    print("Добрый день! Вы в бот-справочнике! \n 1 - запись новых данных \n 2 - вывод справочника \n 3 - удаление данных \n 4 - редактирование данных")
    command = int(input('Введите число '))
    
    while command != 1 and command != 2 and command != 3 and command != 4:
        print("Неправильный ввод")
        command = int(input('Введите число из предложенных '))
    
    if command == 1:
        input_data()
        
    elif command == 2:
        print_data()
    
    elif command == 3:
        del_data()
        
    elif command == 4:
        update_data() 
        
        

