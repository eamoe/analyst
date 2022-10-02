def get_action():
    with open("action.csv", 'r') as file:
        action = file.read()
    return action


def set_action(action):
    with open("action.csv", 'w') as file:
        file.write(action)


def write_temp_data(data):
    with open("temp_data.csv", 'w') as file:
        file.write(data)


def read_temp_data():
    with open("temp_data.csv", 'r') as file:
        data = file.read()
    return data
