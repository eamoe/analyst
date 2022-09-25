from unique_id import *
from datetime import datetime as dt
import constants

def generate_id():
    return get_unique_id(length = constants.contact_id_length,
                        excluded_chars="{%!#}*->$;@~:&,^_<[]`=/'\?.()|+\"")


def create_item(file_name):
    path = constants.folder + file_name + '.csv'
    if file_name == constants.phonebook_db_file_name:
        return create_contact(path)


def create_contact(path):
    print("Cоздание контакта".upper())
    contact_id = generate_id().lower()
    first_name = input("Имя: ")
    last_name = input("Фамилия: ")
    phone_number = input("Номер телефона: ")
    created = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
    updated = created
    
    with open(path, 'a') as file:
        file.write("{};{};{};{};{};{}\n"
            .format(contact_id, first_name, last_name, phone_number, created, updated))

    return f"\nСоздан контакт:" \
            + f"\nID = {contact_id}" \
            + f"\nИмя = {first_name}" \
            + f"\nФамилия = {last_name}" \
            + f"\nТелефон = {phone_number}"
