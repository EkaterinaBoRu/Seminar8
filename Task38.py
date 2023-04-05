"""Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных"""
import re
def writing_person():
    lastname = input("фамилия: ")
    name = input("имя: ")
    surname = input("отчество: ")
    tel = input("номер телефона: ")

    data = open("phonebook.txt", "a", encoding="utf-8")
    data.writelines(f"фамилия: {lastname} имя: {name} отчество: {surname} телефон: {tel}\n")
    data.close()

def search():
    lookfor = input("кого ищем?")
    with open("phonebook.txt", "r", encoding="utf-8") as data:
        for line in data:
            if lookfor in line:
                print(line)

def print_phonebook():
    with open("phonebook.txt", "r", encoding="utf-8") as data:
        for line in data:
            print(line)

def load():
    new_phonebook = input("введите ссылку: ")
    with open("new_phonebook.txt", "r", encoding="utf-8") as data:
        with open("phonebook.txt", "a+", encoding="utf-8") as data_1:
            for line in data:
                if line not in data_1:
                    data_1.write(line)
            data_1.write("\n")

def change_data():
    old_word = input("Введите имя или фамилию, которое нужно изменить: ")
    new_word = input("Введите имя или фамилию, на какое нужно изменить: ")
    with open ('phonebook.txt', 'r', encoding="utf-8") as data:
        old_data = data.read()
    new_data = old_data.replace(old_word, new_word, 1)
    with open ('phonebook.txt', 'w', encoding="utf-8") as data_1:
        data_1.write(new_data)

def delete_data():
    old_word = input("Введите имя или фамилию, данные о которых нужно удалить: ")
    data = open('phonebook.txt', 'r+', encoding="utf-8")
    Lines = data.readlines()
    data.seek(0)
    for line in Lines:
        if old_word not in line.split():
            data.write(line)
    data.truncate()
    data.close()


print("""1- добавление,
2- поиск,
3- вывод на экран,
4- импорт в файл,
5- изменение данных в файле,
6- удаление строки""")

ask = int(input("Выберите действие: "))
if ask ==1:
    writing_person()
elif ask==2:
    search()
elif ask==3:
    print_phonebook()
elif ask==4:
    load()
elif ask==5:
    change_data()
elif ask==6:
    delete_data()
else:
    print("нет такой команды")

