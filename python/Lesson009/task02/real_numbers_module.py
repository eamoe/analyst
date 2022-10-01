def handle_expression(expression):

    result = eval(expression)
    result = str(round(float(result), 2))

    return result
