# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

from os import path
import re

file_base = "base.txt"

all_data = []
id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global all_data, id

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            id = int(all_data[-1][0])

        return all_data


def show_all():
    if not all_data:
        print("Empty data")
    else:
        print(*all_data, sep="\n")


def add_new_contact():
    global id
    array = ['surname', 'name', 'surname_2', 'phone_number']
    string = ''
    for i in array:
        string += input(f"enter {i} ") + " "
    id += 1

    with open(file_base, 'a', encoding="utf-8") as f:
        f.write(f'{id} {string}\n')


def search():
    global all_data, id
    name = exist_contact(0,input('Vvedite dannie dla poiska: '))

    if name:
        print(*name,sep="\n")
    else:
        print('Net sovpadenii')




def exist_contact(rec_id, data):
    """Проверка записи в базе

    :type data: проверка записи
    :type rec_id: проверка id
    """

    if rec_id:
        candidates = [i for i in all_data if rec_id in i[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates


def delete():
    global id, all_data
    show_all()
    print("Vvedite dannie abonenta k-ogo vi hotite udalit': ")
    name = input()
    with open(file_base, 'w', encoding="utf-8") as f:
        for str in all_data:
            if name not in str:
                f.write(f'{str}\n')


def overwriting():
    global id, all_data
    show_all()
    print("Vvedite starie dannie abonenta: ")
    name = input()
    print("Vvedite novie dannie abonenta': ")
    name2 = input()
    with open(file_base, 'a', encoding="utf-8") as f:
        for str in all_data:
            if name in str:
                f.write(str.replace(name, name2))
        with open(file_base, 'w', encoding="utf-8") as f:
            for str in all_data:
                if name not in str:
                    f.write(f'{str}\n')


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search\n"
                       "4. Search/record\n"
                       "5. Delete\n"
                       "6. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search()
            case "4":
                overwriting()
            case "5":
                delete()
            case "6":
                play = False
            case _:
                print("Try again!\n")


main_menu()
