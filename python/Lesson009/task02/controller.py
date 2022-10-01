import real_numbers_module
import rational_numbers_module
import complex_numbers_module
import messages


real_mode = 'real'
rational_mode = 'rational'
complex_mode = 'complex'


def calc_expression(mode, expression):
    if mode == real_mode:
        return real_numbers_module.handle_expression(expression)
    elif mode == rational_mode:
        return rational_numbers_module.handle_expression(expression)
    elif mode == complex_mode:
        return complex_numbers_module.handle_expression(expression)
    else:
        return messages.incorrect_command
