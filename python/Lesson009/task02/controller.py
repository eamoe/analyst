import real_numbers_module
import rational_numbers_module
import complex_numbers_module
import messages
import logger


real_mode = 'real'
rational_mode = 'rational'
complex_mode = 'complex'


def calc_expression(mode, expression):

    result = ''

    if check_expression(expression) == -1:
        return messages.incorrect_expression

    try:
        if mode == real_mode:
            result = real_numbers_module.handle_expression(expression)
        elif mode == rational_mode:
            result = rational_numbers_module.handle_expression(expression)
        elif mode == complex_mode:
            result = complex_numbers_module.handle_expression(expression)
        else:
            return messages.incorrect_command
    except:
        result = messages.calc_error

    logger.log_data(expression, result)

    return result


def check_expression(expression):

    for item in [*expression]:
        if item not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                        '.', '-', '+', '/', '*', 'i', '(', ')']:
            return -1

    return 0
