import constants


format_section_header = "\nФормат #"


def upload_database(file_path):
    
    phonebook_db_path = constants.folder + constants.phonebook_db_file_name + '.csv'
    imported_db_path = file_path

    import_format_option = define_format(imported_db_path)

    data_to_import = []
    data_str = ""
    
    if import_format_option == 1:
    
        with open(imported_db_path, 'r') as file:
            lines = file.readlines()
    
        for line in lines:
            if line == '\n':
                data_str = data_str[:-1]
                data_str += '\n'
                data_to_import.append(data_str)
                list_items = data_str.split(';')
                if len(list_items[0]) != constants.contact_id_length:
                    break
                data_str = ""
            else:
                line = line.replace("\n", "")
                data_str += line
                data_str += ';'

    elif import_format_option == 2:
        with open(imported_db_path, 'r') as file:
            lines = file.readlines()
        data_to_import = lines

    if len(data_to_import) == 0:
        return "Действие отменено!"
    else:
        with open(phonebook_db_path, 'w') as import_file:
            import_file.writelines(data_to_import)
    
        return f"Данные успешно импортированы!"


def define_format(imported_file):
    with open(imported_file, 'r') as file:
        lines = file.readlines()

    data_format = 2
    for line in lines:
        tmp_line = line.replace("\n", "")
        list_items = tmp_line.split(';')
        if len(list_items) == len(constants.contact_fields)\
                and len(list_items[0]) == constants.contact_id_length:
            continue
        else:
            data_format = 1
            break

    return data_format
