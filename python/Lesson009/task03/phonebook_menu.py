def show_menu():
    menu_str = ""
    menu_str += "Телефонная книга\n".upper()
    menu_str += "/showcontacts" + " - " + "показать список" + "\n"
    menu_str += "/addcontact" + " - " + "добавить" + "\n"
    menu_str += "/updatecontact" + " - " + "обновить" + "\n"
    menu_str += "/removecontact" + " - " + "удалить" + "\n"
    menu_str += "/findcontact" + " - " + "найти" + "\n"
    menu_str += "/exportcontacts" + " - " + "экспортировать" + "\n"
    menu_str += "/importcontacts" + " - " + "импортировать" + "\n"

    return menu_str
