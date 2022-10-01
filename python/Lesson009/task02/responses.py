import messages
import controller


colon = ':'


def sample_responses(input_text):
    if str(input_text).find(colon) == -1:
        return messages.missing_colon_error
    else:
        user_message_list = str(input_text).lower().split(colon)
        user_message_length = len(user_message_list)
        user_command = (user_message_list[0]).strip()
        user_expression = user_message_list[1].replace(' ', '')
        if user_message_length > 2:
            return messages.multiple_expressions_error
        else:
            return controller.calc_expression(user_command, user_expression)
