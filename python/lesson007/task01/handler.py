import constants
import creator
import os
import reader
import remover
import updater
import searcher
import export_module
import import_module


clear = lambda: os.system('clear')


def get_file_name(menu_item):
    match menu_item:
        case 0 | 1 | 2 | 3 | 4:
            return constants.phonebook_db_file_name
        case 5:
            return constants.exported_phonebook_file_name
        case 6:
            return input("укажите путь к файлу: ")
        case __:
            return -1
    

def command_handler(menu_item):
    file_name = get_file_name(menu_item)
    # Show list of items
    if menu_item == 0:
        print(constants.menu_items[menu_item].upper() + '\n')
        reader.show_items(file_name)
        input(constants.continue_message)
    # Create a new item
    elif menu_item == 1:
        message = creator.create_item(file_name)
        clear()
        input(constants.continue_message)
    # Update an item
    elif menu_item == 2:
        message = updater.update(file_name)
        print(message)
        input(constants.continue_message)
    # Remove an item
    elif menu_item == 3:
        message = remover.delete(file_name)
        print(message)
        input(constants.continue_message)
    # Find the contact
    elif menu_item == 4:
        searcher.search(file_name)
        input(constants.continue_message)
    # Export phonebook database
    elif menu_item == 5:
        message = export_module.export_data(file_name)
        print(message)
        input(constants.continue_message)
    # Import phonebook database
    elif menu_item == 6:
        message = import_module.import_data(file_name)
        print(message)
        input(constants.continue_message)
