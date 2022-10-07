import telebot
import constants
import real_numbers_module
import rational_numbers_module
import complex_numbers_module

bot = telebot.TeleBot(constants.API_KEY)

calc_mode_buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
calc_mode_buttons.row(telebot.types.KeyboardButton(constants.real_nums_btn_label),
                      telebot.types.KeyboardButton(constants.rational_nums_btn_label))
calc_mode_buttons.row(telebot.types.KeyboardButton(constants.complex_nums_btn_label),
                      telebot.types.KeyboardButton(constants.unknown_btn_label))
calc_mode_buttons.row(telebot.types.KeyboardButton(constants.log_message_header))

operation_buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
operation_buttons.row(telebot.types.KeyboardButton('+'),
                      telebot.types.KeyboardButton('-'))
operation_buttons.row(telebot.types.KeyboardButton('*'),
                      telebot.types.KeyboardButton('/'))

del_buttons = telebot.types.ReplyKeyboardRemove()


@bot.message_handler()
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text=constants.use_calc_mode_message,
                     reply_markup=calc_mode_buttons)
    bot.register_next_step_handler(msg, answer)


def answer(msg: telebot.types.Message):
    if msg.text == constants.real_nums_btn_label:
        bot.register_next_step_handler(msg, real_nums_calc)
        bot.send_message(chat_id=msg.from_user.id,
                         text=constants.real_nums_example,
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    elif msg.text == constants.rational_nums_btn_label:
        bot.register_next_step_handler(msg, rational_counter)
        bot.send_message(chat_id=msg.from_user.id,
                         text=constants.rational_nums_example,
                         reply_markup=del_buttons)
    elif msg.text == constants.complex_nums_btn_label:
        bot.register_next_step_handler(msg, complex_counter)
        bot.send_message(chat_id=msg.from_user.id,
                         text=constants.complex_nums_example,
                         reply_markup=del_buttons)
    elif msg.text == constants.unknown_btn_label:
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id,
                         text=constants.unknown_response)
    elif msg.text == constants.log_message_header:
        send_log(msg)
    else:
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id,
                         text=constants.unknown_command_response)
        bot.send_message(chat_id=msg.from_user.id,
                         text=constants.use_calc_mode_message,
                         reply_markup=calc_mode_buttons)


def real_nums_calc(msg: telebot.types.Message):
    response = real_numbers_module.handle_expression(msg.text)
    bot.send_message(chat_id=msg.from_user.id,
                     text=response + constants.want_to_continue_message,
                     reply_markup=telebot.types.ReplyKeyboardRemove())


def rational_counter(msg: telebot.types.Message):
    response = rational_numbers_module.handle_expression(msg.text)
    bot.send_message(chat_id=msg.from_user.id,
                     text=response + constants.want_to_continue_message,
                     reply_markup=telebot.types.ReplyKeyboardRemove())


def complex_counter(msg: telebot.types.Message):
    response = complex_numbers_module.handle_expression(msg.text)
    bot.send_message(chat_id=msg.from_user.id,
                     text=response + constants.want_to_continue_message,
                     reply_markup=telebot.types.ReplyKeyboardRemove())


def send_log(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text=constants.log_message_header,
                     reply_markup=del_buttons)
    bot.send_document(chat_id=msg.from_user.id, document=open(constants.log_file_path, 'rb'))


bot.polling()
