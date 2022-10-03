import constants


def send_files(update, context):

    chat_id = str(update.message.chat_id)

    phonebook_db_path = constants.folder + constants.phonebook_db_file_name + '.csv'
    exported_db_path_1 = constants.folder + constants.export_format_1 + '.txt'
    exported_db_path_2 = constants.folder + constants.export_format_2 + '.txt'

    with open(phonebook_db_path, 'r') as file:
        lines = file.readlines()

    data_to_export_2 = lines
    with open(exported_db_path_2, 'w') as export_file_2:
        export_file_2.writelines(data_to_export_2)

    data_to_export_1 = []
    for line in lines:
        line = line.replace("\n", "")
        items_list = line.split(';')
        for item in items_list:
            data_to_export_1.append(item + '\n')
        data_to_export_1.append('\n')
    with open(exported_db_path_1, 'w') as export_file_1:
        export_file_1.writelines(data_to_export_1)

    if data_to_export_2 == "":
        update.message.reply_text("Нет данных для выгрузки")
    else:
        update.message.reply_text("Формат 1")
        with open(constants.folder + constants.export_format_1 + '.txt', "rb") as file:
            context.bot.send_document(chat_id=chat_id, document=file,
                                      filename=constants.export_format_1 + '.txt')

    if len(data_to_export_1) == 0:
        update.message.reply_text("Нет данных для выгрузки")
    else:
        update.message.reply_text("Формат 2")
        with open(constants.folder + constants.export_format_2 + '.txt', "rb") as file:
            context.bot.send_document(chat_id=chat_id, document=file,
                                      filename=constants.export_format_2 + '.txt')
