import constants
import reader


def delete(file_name):
    path = constants.folder + file_name + '.csv'
    return delete_item(path, file_name)


def delete_item(path, file_name):
    
    if file_name == constants.phonebook_db_file_name:
        reader.read_contacts(path)
    
    contact_id = input("\n\nУкажите ID удаляемой записи: ")
    
    with open(path, "r") as file:
        lines = file.readlines()
    
    data_to_save = ""

    for line in lines:
        line_list = line.split(";")
        if line_list[0] == contact_id:
            pass
        else:
            data_to_save += line

    with open(path, "w") as file:
        file.write(data_to_save)

    return f"Запись с ID {contact_id} удалена!"
