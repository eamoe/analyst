import constants
import logger


def handle_expression(expression):

    try:
        result = eval(expression)
        response = str(round(float(result), 2))
    except:
        response = constants.excuse_message

    logger.log_data(expression, response)
    return response
