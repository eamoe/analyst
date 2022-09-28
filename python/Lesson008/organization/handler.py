from turtle import clear
import constants
import creator
import os
import reader
import remover
import updater

clear = lambda: os.system('clear')

def get_file_name(menu_item):
    match menu_item:
        case 0:
            return "departments"
        case 1:
            return "employees"
        case 2:
            return "salaries"
        case __:
            return -1
    

def command_handler(main_menu_item, sub_menu_item):
    file_name = get_file_name(main_menu_item)
    # Show list of items
    if sub_menu_item == 0:
        print(f"{constants.main_menu_items[main_menu_item].upper()}\n\n")
        reader.show_items(file_name)
        input("\nНажмите Enter, чтобы продолжить!")
    # Create a new item
    elif sub_menu_item == 1:
        message = creator.create_item(file_name)
        clear()
        input(f"{message}\nНажмите Enter, чтобы продолжить!")
    # Update an item
    elif sub_menu_item == 2:
        message = updater.update_item(file_name)
        print(f"\n{message}")
        input("Нажмите Enter, чтобы продолжить!")
    # Remove an item
    elif sub_menu_item == 3:
        message = remover.delete_item(file_name)
        print(f"\n{message}")
        input("Нажмите Enter, чтобы продолжить!")