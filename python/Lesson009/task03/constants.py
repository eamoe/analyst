API_KEY = 'YOUR_API_KEY'

db_file_name = "phonebook_db"

contact_fields = ["ID", "Имя", "Фамилия", "Телефон", "Создан", "Обновлен"]
your_contacts = "Ваши контакты\n\n"

menu_header = "Телефонная книга"
welcome_message = 'Я помогу вам работать со списком контактов,' \
                  'а также экспортировать данные в удобном формате ' \
                  'и импортировать данные в мою БД.'
help_message = 'Для начала воспользуйтесь командой /help'

menu_items = ["Список контактов",
              "Новый контакт",
              "Изменить контакт",
              "Удалить контакт",
              "Найти",
              "Экспорт",
              "Импорт"]

folder = "db_files/"
phonebook_db_file_name = "phonebook_db"
exported_phonebook_file_name = "exported_phonebook_db"

contact_id_length = 7

export_format_1 = "export_format_1"
export_format_2 = "export_format_2"

log_file_name = "log.csv"


def imported_file_name():
    return folder + "imported_database.txt"
