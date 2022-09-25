import view
import handler


def exit(menu_item):
    if menu_item == -1:
        return True
    else:
        return False


def start_app():
    is_exit = False
    while not is_exit:
        menu_item = view.show_menu()
        is_exit = exit(menu_item)
        if menu_item != -1:
            handler.command_handler(menu_item)
    print("Работа завершена!")
