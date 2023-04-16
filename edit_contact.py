import json                 ##try
import os

def edit_contact(PATH_TO_CONTACTS):
    my_list = os.listdir(PATH_TO_CONTACTS)
    for file_name in my_list:
        if file_name.endswith(".json"):
            print(file_name)
    edit_name = input('Введите полное имя контакта, который нужно отредактировать: ')
    for file_name in my_list:
        if file_name == edit_name:
            print("Для редактирования имени введите 1" '\n'
                  "Для редактирования телефона введите 2" '\n'
                  "Для редактирования email введите 3" '\n'
                  "Для редактирования даты рождения введите 4")
            choice = int(input())
            if choice == 1:
                new_name = input("Введите корректное имя: ")
                print("Ваше имя отредактировано.")
                with open(os.path.join(PATH_TO_CONTACTS, file_name), "r") as file:
                    contacts = json.load(file)
                with open(os.path.join(PATH_TO_CONTACTS, file_name), "w") as f:
                    contacts['name'] = new_name
                    json.dump(contacts, f)
            elif choice == 2:
                new_phone = input("Введите корректный номер")
                print("Ваш номер отредактирован.")
                with open(os.path.join(PATH_TO_CONTACTS, file_name), "r") as file:
                    contacts = json.load(file)
                with open(os.path.join(PATH_TO_CONTACTS, file_name), "w") as f:
                    contacts['phone'] = new_phone
                    json.dump(contacts, f)

            elif choice == 3:
                new_email = input("Введите корректный email")
                print("Ваш email отредактирован.")
                with open(os.path.join(PATH_TO_CONTACTS, file_name), "r") as file:
                    contacts = json.load(file)
                with open(os.path.join(PATH_TO_CONTACTS, file_name), "w") as f:
                    contacts['email'] = new_email
                    json.dump(contacts, f)

            elif choice == 4:
                new_bday = input("Введите корректную дату")
                print("Ваша дата рождения отредактирована.")
                with open(os.path.join(PATH_TO_CONTACTS, file_name), "r") as file:
                    contacts = json.load(file)
                with open(os.path.join(PATH_TO_CONTACTS, file_name), "w") as f:
                    contacts['bday'] = new_bday
                    json.dump(contacts, f)



