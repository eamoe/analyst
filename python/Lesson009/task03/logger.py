import constants
from datetime import datetime as dt


def log_data(input_data, output_data):

    date = dt.now().date()
    time = dt.now().strftime('%H:%M')
    log_file_path = constants.folder + constants.log_file_name
    with open(log_file_path, 'a') as file:
        log_template = 'date;{};time;{};user_message;{};response;{}\n'
        file.write(log_template.format(date,
                                       time,
                                       input_data,
                                       output_data))
