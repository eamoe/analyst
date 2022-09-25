import constants
from tabulate import tabulate


def search(file_name):
    path = constants.folder + file_name + '.csv'
    if file_name == constants.phonebook_db_file_name:
        return search_data(path)


def search_data(path):
    print("\n\nУкажите параметры поиска или нажмите Enter")
    first_name = input("Имя: ")
    last_name = input("Фамилия: ")
    phone_number = input("Телефон: ")

    with open(path, "r") as file:
        lines = file.readlines()

    data_to_show = []
    data_to_show.append(constants.contacts_header)

    for line in lines:
        line = line.strip("\n")
        line_list = line.split(";")
        if (line_list[1].lower() == first_name.lower() or first_name == '') \
            and (line_list[2].lower() == last_name.lower() or last_name == '') \
            and (line_list[3].lower() == phone_number.lower() or phone_number == ''):
            data_to_show.append(line_list)
    
    if data_to_show.count == 1:
        print("Ничего не найдено!")
    else:
        print(tabulate(data_to_show,
                headers='firstrow',
                tablefmt='fancy_grid',
                stralign='center',
                showindex=True,
                ))
