from fractions import Fraction
import constants
import logger


def handle_expression(expression):

    try:
        rational_numbers_list = extract_rational_numbers(expression)

        r_1 = initialize_rational_number(rational_numbers_list[0], rational_numbers_list[1])
        r_2 = initialize_rational_number(rational_numbers_list[2], rational_numbers_list[3])

        operation = get_operation(expression)

        response = str(calc_expression(r_1, r_2, operation))
    except:
        response = constants.excuse_message

    logger.log_data(expression, response)
    return response


def calc_expression(number1, number2, operation):
    match operation:
        case '/':
            result = number1 / number2
        case '*':
            result = number1 * number2
        case '-':
            result = number1 - number2
        case '+':
            result = number1 + number2
        case default:
            pass
    return result


def extract_rational_numbers(data):
    temp = data.replace("/", "|").replace("*", "|").replace("-", "|").replace("+", "|")
    temp_list = temp.split("|")

    return temp_list


def initialize_rational_number(numerator, denominator):
    rational_number = Fraction(int(numerator), int(denominator))

    return rational_number


def get_operation(data):
    temp = str(data).split("/")
    if temp[1].find('+') != -1:
        operation = '+'
    elif temp[1].find('-') != -1:
        operation = '-'
    elif temp[1].find('*') != -1:
        operation = '*'
    else:
        operation = '/'

    return operation
