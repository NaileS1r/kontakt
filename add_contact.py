import json
from static import PATH_TO_CONTACTS
from plus_count import plus_count, COUNTER_FILE
with open(COUNTER_FILE,"r") as f:
    counter = int(f.read())
def add_contact():
    global counter
    name = input('Введите фамилию и имя через пробел: ')
    phone = input('Введите номер телефона: ')
    email = input('Введите адрес электронной почты: ')
    bday = input("Введите дату вашего рождения")
    id = counter
    contact = {'name': name,
               'phone': phone,
               'email': email,
               'bday': bday,
               'id': counter
               }
    filename = plus_count(name)
    print(f"Контакт добавлен,ваш id:{counter}")
    with open(f"{PATH_TO_CONTACTS}/{filename}", "w") as f:
        json.dump(contact, f)
