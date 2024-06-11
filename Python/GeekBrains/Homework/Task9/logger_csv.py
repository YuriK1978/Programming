import csv

from data_create_csv import name_data, surname_data, phone_data, address_data



def input_data():
    
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    
    with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
        
        file.write(f'{name},{surname},{phone},{address}')

    print('Данные записаны')   
    


def print_data():
    
    with open('data_second_variant.csv', encoding='utf-8', newline='') as csvfile:
    
        reader = csv.reader(csvfile)
       
        for row in reader:
            print(row)

def del_data():
    with open('data_second_variant.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        res = list(reader)

    for index, listelem in enumerate(res):
        print(index, listelem)

    id = int(input('Введите номер строки для удаления контакта: '))

    if id < 0 or id >= len(res):
        print("Неверный номер строки")
        return

    res.pop(id)

    with open('data_second_variant.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(res)

    print('Данные удалены')


def update_data():
    with open('data_second_variant.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        res = list(reader)

    for index, listelem in enumerate(res):
        print(index, listelem)

    id = int(input('Введите номер строки для редактирования данных: '))

    if id < 0 or id >= len(res):
        print("Неверный номер строки")
        return

    listelem = res[id]

    answer = int(input(f"Какие данные Вы хотите поменять?\n"
                       f"1. Имя\n"
                       f"2. Фамилия\n"
                       f"3. Номер телефона\n"
                       f"4. Адрес\n"
                       f"Введите ответ: "))

    while answer < 1 or answer > 4:
        print("Вы ошиблись!\nВведите корректный номер от 1 до 4")
        answer = int(input(f"Какие данные Вы хотите поменять?\n"
                           f"1. Имя\n"
                           f"2. Фамилия\n"
                           f"3. Номер телефона\n"
                           f"4. Адрес\n"
                           f"Введите ответ: "))

    if answer == 1:
        listelem[0] = name_data()
    elif answer == 2:
        listelem[1] = surname_data()
    elif answer == 3:
        listelem[2] = phone_data()
    elif answer == 4:
        listelem[3] = address_data()

    with open('data_second_variant.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(res)

    print("Данные успешно обновлены")
    