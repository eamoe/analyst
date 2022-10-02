# Прикрутить бота к задачам с предыдущего семинара:
# Создать телефонный справочник
# с возможностью импорта и экспорта данных в нескольких форматах.


import constants
from telegram.ext import *
import phonebook_menu
import responses
import export_module


def start_command(update, context):
    update.message.reply_text(constants.menu_header.upper())
    update.message.reply_text(constants.welcome_message)
    update.message.reply_text(constants.help_message)


def phone_book_command(update, context):
    update.message.reply_text(phonebook_menu.show_menu())


def handle_message(update, context):
    text = str(update.message.text)
    response = responses.sample_responses(text)
    update.message.reply_text(response)


def export_database_command(update, context):
    chat_id = str(update.message.chat_id)
    path = constants.folder + constants.phonebook_db_file_name + '.csv'
    export_module.generate_export_files()

    update.message.reply_text("Файлы сгенерированы в 2-х форматах".upper())

    update.message.reply_text("Формат 1")
    with open(constants.folder + constants.export_format_1 + '.txt', "rb") as file:
        context.bot.send_document(chat_id=chat_id, document=file,
                                  filename=constants.export_format_1 + '.txt')

    update.message.reply_text("Формат 2")
    with open(constants.folder + constants.export_format_2 + '.txt', "rb") as file:
        context.bot.send_document(chat_id=chat_id, document=file,
                                  filename=constants.export_format_2 + '.txt')


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():

    print("Bot started...")

    updater = Updater(constants.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", phone_book_command))
    dp.add_handler(CommandHandler("exportcontacts", export_database_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


main()
