import constants
import reader
from datetime import datetime as dt


def update(file_name):
    path = constants.folder + file_name + '.csv'
    if file_name == constants.phonebook_db_file_name:
        return update_item(path)


def update_item(path):
    
    reader.read_contacts(path)
    
    contact_id = input("\n\nУкажите ID изменяемой записи: ")
    
    with open(path, "r") as file:
        lines = file.readlines()
    
    data_to_save = ""

    for line in lines:
        tmp_line = line.strip("\n")
        line_list = tmp_line.split(";")
        if line_list[0] == contact_id:
            new_contact_id = line_list[0]
            new_first_name = input("Имя (укажите новое значение или нажмите Enter): ")
            if new_first_name == "":
                new_first_name = line_list[1]
            new_last_name = input("Фамалия (укажите новое значение или нажмите Enter): ")
            if new_last_name == "":
                new_last_name = line_list[2]
            new_phone_number = input("Телефон (укажите новое значение или нажмите Enter): ")
            if new_phone_number == "":
                new_phone_number = line_list[3]
            new_created = line_list[4]
            new_updated = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
            data_to_save += '{};{};{};{};{};{}\n'.format(new_contact_id, new_first_name, new_last_name, new_phone_number, new_created, new_updated)
        else:
            data_to_save += line
                

    with open(path, "w") as file:
        file.write(data_to_save)

    return f"Запись с ID {contact_id} обновлена!"
