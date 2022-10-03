import constants
import reader
from datetime import datetime as dt
import action
import logger


def update(file_name, global_action, user_message):
    path = constants.folder + file_name + '.csv'
    if file_name == constants.phonebook_db_file_name:
        return update_item(path, global_action, user_message)


def update_item(path, global_action, user_message):
    response_str = ""
    if global_action == "":
        logger.log_data(user_message, "Command")
        response_str += reader.read_contacts(path)
        response_str += f"Укажите ID изменяемой записи"
        action.set_action("update_first_name")
        return response_str
    elif global_action == "update_first_name":
        logger.log_data(user_message, "Enter ID")
        temp_data = action.read_temp_data() + user_message + ';'
        action.write_temp_data(temp_data)
        action.set_action("update_last_name")
        response_str += f"Укажите новое имя или введите '/', чтобы оставить прошлое значение"
        return response_str
    elif global_action == "update_last_name":
        logger.log_data(user_message, "Enter first name")
        temp_data = action.read_temp_data() + user_message + ';'
        action.write_temp_data(temp_data)
        action.set_action("update_phone_number")
        response_str += f"Укажите новую фамилию или введите '/', чтобы оставить прошлое значение"
        return response_str
    elif global_action == "update_phone_number":
        logger.log_data(user_message, "Enter last name")
        temp_data = action.read_temp_data() + user_message + ';'
        action.write_temp_data(temp_data)
        action.set_action("update_contact")
        response_str += f"Укажите новый телефон или введите '/', чтобы оставить прошлое значение"
        return response_str
    elif global_action == "update_contact":
        logger.log_data(user_message, "Enter phone number")
        temp_data = action.read_temp_data() + user_message + ';'
        temp_data_list = str(temp_data).split(";")
        contact_id = temp_data_list[0]
        first_name = temp_data_list[1]
        last_name = temp_data_list[2]
        phone_number = temp_data_list[3]
        with open(path, "r") as file:
            lines = file.readlines()
        data_to_save = ""
        for line in lines:
            tmp_line = line.strip("\n")
            line_list = tmp_line.split(";")
            if line_list[0] == contact_id:
                new_contact_id = contact_id
                if first_name == '/':
                    new_first_name = line_list[1]
                else:
                    new_first_name = first_name
                if last_name == '/':
                    new_last_name = line_list[2]
                else:
                    new_last_name = last_name
                if phone_number == '/':
                    new_phone_number = line_list[3]
                else:
                    new_phone_number = phone_number
                new_created = line_list[4]
                new_updated = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
                template_str = '{};{};{};{};{};{}\n'
                data_to_save += template_str.format(new_contact_id,
                                                    str(new_first_name).capitalize(),
                                                    str(new_last_name).capitalize(),
                                                    new_phone_number,
                                                    new_created,
                                                    new_updated)
            else:
                data_to_save += line

        action.write_temp_data("")
        action.set_action("")

        with open(path, "w") as file:
            file.write(data_to_save)

        return f"Запись с ID {contact_id} обновлена!"
