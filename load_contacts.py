import json
import os


def load_contacts(PATH_TO_CONTACTS):
    my_list = os.listdir(PATH_TO_CONTACTS)
    for file_name in my_list:
        if file_name.endswith(".json"):
            print(file_name.strip(".json"))



