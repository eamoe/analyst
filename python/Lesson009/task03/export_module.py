import constants


def generate_export_files():
    phonebook_db_path = constants.folder + constants.phonebook_db_file_name + '.csv'
    exported_db_path_1 = constants.folder + constants.export_format_1 + '.txt'
    exported_db_path_2 = constants.folder + constants.export_format_2 + '.txt'

    with open(phonebook_db_path, 'r') as file:
        lines = file.readlines()

    data_to_export_1 = []
    data_to_export_2 = lines
    for line in lines:
        line = line.replace("\n", "")
        items_list = line.split(';')
        for item in items_list:
            data_to_export_1.append(item + '\n')
        data_to_export_1.append('\n')

    with open(exported_db_path_1, 'w') as export_file_1:
        export_file_1.writelines(data_to_export_1)

    with open(exported_db_path_2, 'w') as export_file_2:
        export_file_2.writelines(data_to_export_2)
