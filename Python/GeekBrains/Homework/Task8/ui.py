import csv

from logger import input_data, print_data, seach_contact, change_contact, delete_contact


def interface():
    print("Добрый день! Это бот-телефонный справочник.\n",
          "1 - Записать данные\n", 
          "2 - Вывести данные\n",
          "3 - Найти контакт\n",
          "4 - Измененить данные\n",
          "5 - Удалить данные\n")
    command = int(input("Введите код операции: "))

    while command != 1 and command != 2 and command != 3 and command != 4 and command != 5:
        print("Неверный код операции!")
        command = int(input("Введите номер операции: "))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        seach_contact()
    elif command == 4:
        change_contact()
    elif command == 5:
        delete_contact()

