import constants


format_section_header = "\nФормат #"


def import_data(file_name):
    
    phonebook_db_path = constants.folder +  constants.phonebook_db_file_name + '.csv'
    imported_db_path = file_name

    import_format_option = get_format()
    
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
                data_str = ""
            else:
                line = line.replace("\n", "")
                data_str += line
                data_str += ';'

    elif import_format_option == 2:
        with open(imported_db_path, 'r') as file:
            lines = file.readlines()
        data_to_import = lines
    else:
        return "Действие отменено!"
    
    with open(phonebook_db_path, 'w') as import_file:
        import_file.writelines(data_to_import)
    
    return f"Данные импортированы: {phonebook_db_path}"

def print_import_format_1(n):
    print("\nИмя_" + n + "\nФамилия_" + n + "\nТелефон_" + n + "\nДата_создания_" + "\nДата_обновления_" + n)


def print_import_format_2(n):
    print(f"Имя_" + n + ";Фамилия_" + n + ";Телефон_" + n + ";Дата_создания_" + n + ";Дата_обновления_" + n)


def print_format_options():
    print("\nУкажите формат импортируемых данных".upper())
    print(format_section_header + str(1))
    print_import_format_1(str(1))
    print_import_format_1(str(2))
    print(format_section_header + str(2))
    print_import_format_2(str(1))
    print_import_format_2(str(2))

def get_format():
    print_format_options()
    print("\nВажно! ".upper() + "Текущие данные будут заменены! Укажите 0, если хотите отменить действие.")
    return int(input("\nВыберите формат в котором представлены данные (1 или 2): "))
