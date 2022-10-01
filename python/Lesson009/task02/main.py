# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и комплексными числами,
# организовать меню,
# добавить систему логирования


import constants
from telegram.ext import *
import responses as responses


def start_command(update, context):
    update.message.reply_text(constants.welcome_message)


def help_command(update, context):
    update.message.reply_text(constants.capabilities_message)
    update.message.reply_text(constants.real_nums_cap)
    update.message.reply_text(constants.rational_nums_cap)
    update.message.reply_text(constants.complex_nums_cap)


def real_numbers_command(update, context):
    update.message.reply_text(constants.real_nums_example)


def rational_numbers_command(update, context):
    update.message.reply_text(constants.rational_nums_example)


def complex_numbers_command(update, context):
    update.message.reply_text(constants.complex_nums_example)


def handle_message(update, context):
    text = str(update.message.text)
    response = responses.sample_responses(text)
    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    
    print("Bot started...")

    updater = Updater(constants.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("realnumbers", real_numbers_command))
    dp.add_handler(CommandHandler("rationalnumbers", rational_numbers_command))
    dp.add_handler(CommandHandler("complexnumbers", complex_numbers_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    
    updater.idle()


main()
