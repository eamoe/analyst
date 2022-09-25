import constants
from tabulate import tabulate


def show_items(file_name):
    path = constants.folder + file_name + '.csv'
    if file_name == constants.phonebook_db_file_name:
        read_contacts(path)


def read_contacts(path):
    
    contacts = []
    contacts.append(constants.contacts_header)
    
    with open(path, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        line = line.replace("\n", "")
        list_items = line.split(';')
        contacts.append(list_items)

    print(tabulate(contacts,
                headers='firstrow',
                tablefmt='fancy_grid',
                stralign='center',
                showindex=True,
                ))
