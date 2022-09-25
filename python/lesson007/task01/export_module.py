import constants


format_section_header = "\nФормат #"


def export_data(file_name):
    
    phonebook_db_path = constants.folder +  constants.phonebook_db_file_name + '.csv'
    exported_db_path = constants.folder + file_name + '.csv'

    export_format_option = get_format()
    
    if file_name == constants.exported_phonebook_file_name:
        with open(phonebook_db_path, 'r') as file:
            lines = file.readlines()
    
    data_to_export = []
    if export_format_option == 1:
        for line in lines:
            line = line.replace("\n", "")
            items_list = line.split(';')
            for item in items_list:
                data_to_export.append(item + '\n')
            data_to_export.append('\n')
    elif export_format_option == 2:
        data_to_export = lines
    else:
        return "Формат отсутствует!"
    
    with open(exported_db_path, 'w') as export_file:
        export_file.writelines(data_to_export)
    
    return f"Данные сохранены в файл: {exported_db_path}"


def print_export_format_1(n):
    print("\nИмя_" + n + "\nФамилия_" + n + "\nТелефон_" + n + "\nДата_создания_" + "\nДата_обновления_" + n)


def print_export_format_2(n):
    print(f"Имя_" + n + ";Фамилия_" + n + ";Телефон_" + n + ";Дата_создания_" + n + ";Дата_обновления_" + n)


def print_format_options():
    print("Выберите формат экспорта данных".upper())
    print(format_section_header + str(1))
    print_export_format_1(str(1))
    print_export_format_1(str(2))
    print(format_section_header + str(2))
    print_export_format_2(str(1))
    print_export_format_2(str(2))

def get_format():
    print_format_options()
    return int(input("\nУкажите необходимый формат (1 или 2): "))
