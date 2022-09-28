import constants
from consolemenu import *
from consolemenu.items import *

def set_to_exit():
    return -1


def show_menu():
    main_menu_option = show_main_menu()
    if main_menu_option == len(constants.main_menu_items):
        main_menu_option = set_to_exit()
        sub_menu_option = set_to_exit()
    else:
        sub_menu_option = show_sub_menu()
        if sub_menu_option == len(constants.sub_menu_items):
            sub_menu_option = set_to_exit()
    return (main_menu_option, sub_menu_option)


def show_main_menu():
    menu_items = constants.main_menu_items
    menu = SelectionMenu(menu_items,
                        f"{constants.main_menu_header.upper()}\n{constants.choose_option_text}",
                        exit_option_text = constants.exit_menu_item)
    menu.show()
    menu.join()
    return menu.selected_option

def show_sub_menu():
    menu_items = constants.sub_menu_items
    menu = SelectionMenu(menu_items,
                        f"{constants.choose_option_text}",
                        exit_option_text = constants.return_menu_item)
    menu.show()
    menu.join()
    return menu.selected_option