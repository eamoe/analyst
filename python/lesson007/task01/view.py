import constants
from consolemenu import *
from consolemenu.items import *


def set_to_exit():
    return -1


def show_menu():
    menu_items = constants.menu_items
    menu = SelectionMenu(menu_items,
                        title = constants.menu_header.upper(),
                        subtitle = constants.choose_option_text,
                        exit_option_text = constants.return_menu_item)
    menu.show()
    menu.join()
    action = menu.selected_option
    if action == len(constants.menu_items):
        action = set_to_exit()
    return action
