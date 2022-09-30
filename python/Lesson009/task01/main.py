# Создайте программу для игры в "Крестики-нолики" при помощи виртуального окружения и PIP

from tabulate import tabulate
import emoji


empty_cell = ''
initial_state = [[empty_cell, empty_cell, empty_cell],
                 [empty_cell, empty_cell, empty_cell],
                 [empty_cell, empty_cell, empty_cell]]
red_circle = emoji.emojize(':pizza:', language='en')
white_circle = emoji.emojize(':hamburger:', language='en')
alphabet = [red_circle, white_circle]


def update_state(state, row, column, symbol):
    state[row - 1][column - 1] = symbol
    return state


def print_field(state):
    print(tabulate(state,
                tablefmt='fancy_grid',
                stralign='center'))


def empty_fields_check(current_state):
    empty_fields = 0
    for row in current_state:
        for column in row:
            if column == '':
                empty_fields += 1
    if empty_fields == 0:
        check = True
    else:
        check = False
    return check


def win_line_check(cs):
    if cs[0][0] == cs[0][1] == cs[0][2] and cs[0][0] in alphabet:
        return True
    elif cs[1][0] == cs[1][1] == cs[1][2] and cs[1][0] in alphabet:
        return True
    elif cs[2][0] == cs[2][1] == cs[2][2] and cs[2][0] in alphabet:
        return True
    elif cs[0][0] == cs[1][0] == cs[2][0] and cs[0][0] in alphabet:
        return True
    elif cs[0][1] == cs[1][1] == cs[2][1] and cs[0][1] in alphabet:
        return True
    elif cs[0][2] == cs[1][2] == cs[2][2] and cs[0][2] in alphabet:
        return True
    elif cs[0][0] == cs[1][1] == cs[2][2] and cs[0][0] in alphabet:
        return True
    elif cs[2][0] == cs[1][1] == cs[0][2] and cs[2][0] in alphabet:
        return True


def is_game_over(current_state):
    if empty_fields_check(current_state) or win_line_check(current_state):
        return True
    else:
        return False


def get_move(player, state):
    check = False
    while not check:
        
        row_str = input(f"Игрок {player}, выберите строку: ")
        column_str = input(f"Игрок {player}, выберите столбец: ")
        
        if row_str.isdigit() and int(row_str) > 0 and int(row_str) <= 3:
            row = int(row_str)
        else:
            row = -1
        
        if column_str.isdigit() and int(column_str) > 0 and int(column_str) <= 3:
            column = int(column_str)
        else:
            column = -1
        
        if state[row - 1][column - 1] in alphabet or row == -1 or column == -1:
            print("Некорректный ход! Попробуйте снова!")
        else:
            check = True
    return (row, column)


def turn_move(player):
    if player == 1:
        return (2, alphabet[0])
    else:
        return (1, alphabet[1])


player = 2
symbol = alphabet[0]
game_state = initial_state
print_field(game_state)


while not is_game_over(game_state):
    (player, symbol) = turn_move(player)
    (row, column) = get_move(player, game_state)
    game_state = update_state(game_state, row, column, symbol)
    print_field(game_state)


print("Игра окончена!")
