from unique_id import *
from datetime import datetime as dt
import constants
import action
import logger


def generate_id():
    return get_unique_id(length=constants.contact_id_length,
                         excluded_chars="{%!#}*->$;@~:&,^_<[]`=/'\?.()|+\"")


def create_item(file_name, global_action, user_message):
    path = constants.folder + file_name + '.csv'
    if file_name == constants.db_file_name:
        return create_contact(path, global_action, user_message)


def create_contact(path, global_action, user_message):
    if global_action == "":
        logger.log_data(user_message, "Command")
        action.write_temp_data("")
        action.set_action("add_last_name")
        return f"Укажите имя"
    elif global_action == "add_last_name":
        logger.log_data(user_message, "Enter first name")
        temp_data = action.read_temp_data() + user_message + ';'
        action.write_temp_data(temp_data)
        action.set_action("add_phone_number")
        return f"Укажите фамилию"
    elif global_action == "add_phone_number":
        logger.log_data(user_message, "Enter last name")
        temp_data = action.read_temp_data() + user_message + ';'
        action.write_temp_data(temp_data)
        action.set_action("create_contact")
        return f"Укажите телефон"
    elif global_action == "create_contact":
        logger.log_data(user_message, "Enter phone number")
        temp_data = action.read_temp_data() + user_message + ';'
        temp_data_list = str(temp_data).split(";")
        contact_id = str(generate_id()).lower()
        first_name = str(temp_data_list[0]).capitalize()
        last_name = str(temp_data_list[1]).capitalize()
        phone_number = temp_data_list[2]
        created = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
        updated = created
        with open(path, 'a') as file:
            file.write("{};{};{};{};{};{}\n".format(contact_id,
                                                    first_name,
                                                    last_name,
                                                    phone_number,
                                                    created,
                                                    updated))
        action.write_temp_data("")
        action.set_action("")
        response_str = f"Создан новый контакт:\n" \
                       f"ID: {contact_id}\n" \
                       f"Имя: {first_name}\n" \
                       f"Фамилия: {last_name}\n" \
                       f"Телефон: {phone_number}\n"
        return response_str
