import constants
import reader
import action
import logger


def delete(file_name, global_action, user_message):
    path = constants.folder + file_name + '.csv'
    return delete_item(path, file_name, global_action, user_message)


def delete_item(path, file_name, global_action, user_message):
    response_str = ""
    if global_action == "":
        if file_name == constants.phonebook_db_file_name:
            logger.log_data(user_message, "Command")
            response_str += reader.read_contacts(path)
            action.set_action("get_contact_id")
            response_str += f"\nУкажите ID удаляемой записи"
        return response_str
    elif global_action == "get_contact_id":
        logger.log_data(user_message, "Enter ID")
        contact_id = user_message
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
        action.set_action("")
        return f"Запись с ID {contact_id} удалена!"
