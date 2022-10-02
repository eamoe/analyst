import constants
import reader
import action


def search(file_name, global_action, user_message):
    path = constants.folder + file_name + '.csv'
    if file_name == constants.phonebook_db_file_name:
        return search_data(path, global_action, user_message)


def search_data(path, global_action, user_message):
    response_str = ""
    if global_action == "":
        response_str += f"Имя: укажите значение для поиска или '/', чтобы пропустить данный критерий"
        action.set_action("find_last_name")
        return response_str
    elif global_action == "find_last_name":
        temp_data = action.read_temp_data() + user_message + ';'
        action.write_temp_data(temp_data)
        action.set_action("find_phone_number")
        response_str += f"Фамилия: укажите значение для поиска или '/', чтобы пропустить данный критерий"
        return response_str
    elif global_action == "find_phone_number":
        temp_data = action.read_temp_data() + user_message + ';'
        action.write_temp_data(temp_data)
        action.set_action("find_contact")
        response_str += f"Телефон: укажите значение для поиска или '/', чтобы пропустить данный критерий"
        return response_str
    elif global_action == "find_contact":
        temp_data = action.read_temp_data() + user_message + ';'
        temp_data_list = str(temp_data).split(";")
        first_name = temp_data_list[0]
        last_name = temp_data_list[1]
        phone_number = temp_data_list[2]
        with open(path, "r") as file:
            lines = file.readlines()
        search_list = []
        for line in lines:
            tmp_line = line.strip("\n")
            line_list = tmp_line.split(";")
            if line_list[1].lower() == first_name.lower() or first_name == '/':
                if line_list[2].lower() == last_name.lower() or last_name == '/':
                    if line_list[3] == phone_number or phone_number == '/':
                        search_list.append(line)

        if len(search_list) == 0:
            response_str = "Ничего не найдено!"
        else:
            for item in search_list:
                item = item.replace("\n", "")
                list_items = item.split(';')
                response_str += constants.contact_fields[0] + ': ' + list_items[0] + '\n'
                response_str += constants.contact_fields[1] + ': ' + list_items[1] + '\n'
                response_str += constants.contact_fields[2] + ': ' + list_items[2] + '\n'
                response_str += constants.contact_fields[3] + ': ' + list_items[3] + '\n'
                response_str += constants.contact_fields[4] + ': ' + list_items[4] + '\n'
                response_str += constants.contact_fields[5] + ': ' + list_items[5] + '\n\n'

        action.write_temp_data("")
        action.set_action("")

        return response_str
