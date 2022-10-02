import constants


def show_items(file_name):
    contacts = ""
    path = constants.folder + file_name + '.csv'
    if file_name == constants.phonebook_db_file_name:
        contacts = read_contacts(path)
    return contacts


def read_contacts(path):
    with open(path, 'r') as file:
        lines = file.readlines()

    contacts_str = constants.your_contacts.upper()
    for line in lines:
        line = line.replace("\n", "")
        list_items = line.split(';')
        contacts_str += constants.contact_fields[0] + ': ' + list_items[0] + '\n'
        contacts_str += constants.contact_fields[1] + ': ' + list_items[1] + '\n'
        contacts_str += constants.contact_fields[2] + ': ' + list_items[2] + '\n'
        contacts_str += constants.contact_fields[3] + ': ' + list_items[3] + '\n'
        contacts_str += constants.contact_fields[4] + ': ' + list_items[4] + '\n'
        contacts_str += constants.contact_fields[5] + ': ' + list_items[5] + '\n\n'
    return contacts_str
