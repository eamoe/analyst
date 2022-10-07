import logger


imaginary_unit = 'i'


def handle_expression(expression):

    complex_operation_list = extract_complex_numbers(expression)
    operation = complex_operation_list[1].strip()
    z_1 = initialize_complex_number(complex_operation_list[0])
    z_2 = initialize_complex_number(complex_operation_list[2])

    match operation:
        case '/':
            result = z_1 / z_2
        case '*':
            result = z_1 * z_2
        case '-':
            result = z_1 - z_2
        case '+':
            result = z_1 + z_2
        case default:
            pass

    real = result.real
    imag = result.imag

    if imag < 0:
        response = str(round(real, 3)) + str(round(imag, 3)) + imaginary_unit
    else:
        response = str(round(real, 3)) + '+' + str(round(imag, 3)) + imaginary_unit

    logger.log_data(expression, response)
    return response


def extract_complex_numbers(data):

    temp = data.replace("(", "|").replace(")", "|")
    temp = temp[1:]
    temp = temp[:-1]
    temp_list = temp.split("|")

    return temp_list


def initialize_complex_number(complex_number_str):

    if complex_number_str.find('+') != -1:
        temp_list = complex_number_str.split('+')
        real = float(temp_list[0])
        imag = float(temp_list[1][:-1])
    elif complex_number_str.find('-') != -1:
        temp_list = complex_number_str.split('-')
        real = float(temp_list[0])
        imag = float(temp_list[1][:-1]) * (-1)

    complex_number = complex(real, imag)
    return complex_number
