from datetime import datetime as dt


def log_data(input_data, output_data):

    date = dt.now().date()
    time = dt.now().strftime('%H:%M')

    with open('log.csv', 'a') as file:
        log_template = 'date;{};time;{};expression;{};result;{}\n'
        file.write(log_template.format(date,
                                       time,
                                       input_data,
                                       output_data))
