import view
import constants
import handler

def exit(main_menu_option):
    if main_menu_option == -1:
        return True
    else:
        return False

def start_app():
    is_exit = False
    while not is_exit:
        (main_menu_option, sub_menu_option) = view.show_menu()
        is_exit = exit(main_menu_option)
        if sub_menu_option != -1:
            handler.command_handler(main_menu_option, sub_menu_option)
        else:
            pass
    print("Работа завершена!")