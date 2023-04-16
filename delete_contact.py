import json
import os

def delete_contact(PATH_TO_CONTACTS):
    my_list = os.listdir(PATH_TO_CONTACTS)
    for file_name in my_list:
        if file_name.endswith(".json"):
            print(file_name)
    delete_name = input('Введите полное имя контакта, который нужно удалить: ')
    for file_name in my_list:
        if file_name == delete_name:
            os.remove(os.path.join(PATH_TO_CONTACTS, file_name))
            print(f"Контакт {delete_name} удален.")
            break
    else:
        print(f"Контакт {delete_name} не найден.")
