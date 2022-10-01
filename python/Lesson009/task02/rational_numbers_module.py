from fractions import Fraction


def handle_expression(expression):

    rational_numbers_list = extract_rational_numbers(expression)

    r_1 = initialize_rational_number(rational_numbers_list[0], rational_numbers_list[1])
    r_2 = initialize_rational_number(rational_numbers_list[2], rational_numbers_list[3])

    operation = get_operation(expression)

    match operation:
        case '/':
            result = r_1 / r_2
        case '*':
            result = r_1 * r_2
        case '-':
            result = r_1 - r_2
        case '+':
            result = r_1 + r_2
        case default:
            pass

    return str(result)


def extract_rational_numbers(data):

    temp = data.replace("/", "|").replace("*", "|").replace("-", "|").replace("+", "|")
    temp_list = temp.split("|")

    return temp_list


def initialize_rational_number(numerator, denominator):

    rational_number = Fraction(int(numerator), int(denominator))

    return rational_number


def get_operation(data):

    temp = str(data).split("/")
    temp = temp[1][1:]
    temp = temp[:-1]
    if temp == '':
        temp = '/'

    return temp
