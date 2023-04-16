from static import PATH_TO_CONTACTS
from add_contact import add_contact
from load_contacts import load_contacts
from edit_contact import edit_contact
from delete_contact import delete_contact
while True:
    print("1. Добавить контакт")
    print("2. Вывести список контактов")
    print("3. Редактировать контакт")
    print("4. Удалить контакт")
    print("5. Выйти")
    choice = input("Введите номер операции: ")
    if choice == "1":
        add_contact()
    elif choice == "2":                                                 #выводим список контактов
        print("Список контактов:")
        load_contacts(PATH_TO_CONTACTS)
    elif choice == "3":                                                 #Редактировать контакт
        edit_contact(PATH_TO_CONTACTS)
    elif choice == "4":                                                 #Удалить контакт
        delete_contact(PATH_TO_CONTACTS)
    elif choice == "5":                                                 #Выход из программы
        print("Выход из программы")
        break
    else:
        print("Неверный ввод. Повторите попытку")
