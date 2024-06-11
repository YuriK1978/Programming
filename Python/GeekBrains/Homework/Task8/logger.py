import csv

from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"Выберите вариант записи данных:\n\n"
                    f"вариант 1: \n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"вариант 2: \n"
                    f"{name};{surname};{phone};{address}\n"
                    f"Выберите вариант: "))
    
    while var != 1 and var != 2:
        print("Такого варианта записи нет!")
        var = int(input("Выберите вариант записи данных:"))

    if var == 1:
       with open('data_first_variant.csv', 'a', encoding='utf-8') as data:
           data.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as data:
           data.write(f"{name};{surname};{phone};{address}\n\n")


def print_data():
    print("Список контактов №1:\n")
    with open('data_first_variant.csv', 'r', encoding='utf-8') as data:
        data_first = data.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i + 1]))
                j = i
        print(*data_first_list)       

    print("Список контактов №2:\n")
    with open('data_second_variant.csv', 'r', encoding='utf-8') as data:
        data_second = data.readlines()
        print(*data_second)


def seach_contact():
    seach = input("Введите данные для поиска контакта: ").capitalize()
    
    with open('data_first_variant.csv', 'r', encoding='utf-8') as data: 
        contacts_first_phonebook = data.read().split('\n\n')
        for contact in contacts_first_phonebook:
            if seach in contact:
                print(contact)

    with open('data_second_variant.csv', 'r', encoding='utf-8') as data: 
        contacts_second_phonebook = data.read().split('\n\n')
        for contact in contacts_second_phonebook:
            if seach in contact:
                print(contact)


def change_contact():
    search_to_change = input("Введите данные контакта для изменения: ").capitalize()

    with open('data_first_variant.csv', 'r+', encoding='utf-8') as data:
        contacts_first_phonebook = data.read().split('\n\n')
        data.seek(0)

        for i_contact in range(len(contacts_first_phonebook)):
            if search_to_change in contacts_first_phonebook[i_contact]:
                var = input("Что нужно изменить?:"
                             "\n 1) name\n 2) surname\n 3) phone\n 4) address?\n"
                             "Введите параметр: ")
                list_contact = contacts_first_phonebook[i_contact].split('\n')
                
                if var == "name":
                    change = input("Введите имя для изменения: ").capitalize()
                    list_contact[0] = change
                    contact = '\n'.join(list_contact)
                    
                    contacts_first_phonebook[i_contact] = contact

                    data.truncate(0)
                    data.write('\n\n'.join(contacts_first_phonebook))

                    print("Контакт изменён\n", contact)
                    return
                
                elif var == "surname":
                    change = input("Введите фамилию для изменения: ").capitalize()
                    list_contact[1] = change
                    contact = '\n'.join(list_contact)
                    
                    contacts_first_phonebook[i_contact] = contact

                    data.truncate(0)
                    data.write('\n\n'.join(contacts_first_phonebook))

                    print("Контакт изменён\n", contact)
                    return
                
                elif var == "phone":
                    change = input("Введите номер телефона для изменения: ").capitalize()
                    list_contact[2] = change
                    contact = '\n'.join(list_contact)
                    
                    contacts_first_phonebook[i_contact] = contact

                    data.truncate(0)
                    data.write('\n\n'.join(contacts_first_phonebook))

                    print("Контакт изменён\n", contact)
                    return
                
                elif var == "address":
                    change = input("Введите город для изменения: ").capitalize()
                    list_contact[3] = change
                    contact = '\n'.join(list_contact)
                    
                    contacts_first_phonebook[i_contact] = contact

                    data.truncate(0)
                    data.write('\n\n'.join(contacts_first_phonebook))

                    print("Контакт изменён\n", contact)
                    return

    print("Контакт не найден")


def delete_contact():
    search_to_change = input("Введите данные контакта, который нужно удалить: ").capitalize()

    with open('data_first_variant.csv', 'r+', encoding='utf-8') as data:
        contacts_first_phonebook = data.read().split('\n\n')
        data.seek(0)
        
        contacts_new_phonebook = []

        for i_contact in range(len(contacts_first_phonebook)):
            if search_to_change in contacts_first_phonebook[i_contact]:
                contacts_new_phonebook = contacts_first_phonebook[:i_contact] + contacts_first_phonebook[i_contact + 1:]
                print(f"Контакт удален")

    with open('data_first_variant.csv', 'w', encoding='utf-8') as data1:
        data1.write('\n\n'.join(contacts_new_phonebook))
        data1.seek(0)

    return contacts_new_phonebook
