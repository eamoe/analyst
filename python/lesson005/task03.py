# Создайте программу для игры в ""Крестики-нолики"".
# Пример интерфейса:
#    |   | 0
# -----------    
#    |   |
# -----------
#    | X |
# Ввод можно реализовать через введение двух чисел (номеров строки и столбца).

# Создайте программу для игры в "Крестики-нолики".


from operator import is_
from sre_parse import State


initial_state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def update_state(state, row, column, symbol):
    state[row][column] = symbol
    return state


def print_field(state):
    for row in state:
        field_str = "| " + " | ".join(map(str, row)) + " |"
        length = len(field_str)
        print("-" * length)
        print(field_str)
    print("-" * length)


def empty_fields_check(current_state):
    empty_fields = 0
    for row in current_state:
        for column in row:
            if column == ' ':
                empty_fields += 1
    if empty_fields == 0:
        check = True
    else:
        check = False
    return check

def win_line_check(cs):
    if cs[0][0] == cs[0][1] == cs[0][2] and cs[0][0] in ['x', 'o']:
        return True
    elif cs[1][0] == cs[1][1] == cs[1][2] and cs[1][0] in ['x', 'o']:
        return True
    elif cs[2][0] == cs[2][1] == cs[2][2] and cs[2][0] in ['x', 'o']:
        return True
    elif cs[0][0] == cs[1][0] == cs[2][0] and cs[0][0] in ['x', 'o']:
        return True
    elif cs[0][1] == cs[1][1] == cs[2][1] and cs[0][1] in ['x', 'o']:
        return True
    elif cs[0][2] == cs[1][2] == cs[2][2] and cs[0][2] in ['x', 'o']:
        return True
    elif cs[0][0] == cs[1][1] == cs[2][2] and cs[0][0] in ['x', 'o']:
        return True
    elif cs[2][0] == cs[1][1] == cs[0][2] and cs[2][0] in ['x', 'o']:
        return True

def is_game_over(current_state):
    if empty_fields_check(current_state) or win_line_check(current_state):
        return True
    else:
        return False

def get_move(player, symbol, state):
    check = False
    while not check:
        row = int(input(f"Игрок {player}, выберите строку: "))
        column = int(input(f"Игрок {player}, выберите столбец: "))
        if state[row][column] == 'x' or state[row][column] == 'o':
            print("Некорректный ход! Попробуйте снова!")
        else:
            check = True
    return (row, column)


def turn_move(player):
    if player == 1:
        return (2, 'o')
    else:
        return (1, 'x')

player = 2
symbol = 'o'
game_state = initial_state
print_field(game_state)

while not is_game_over(game_state):
    (player, symbol) = turn_move(player)
    (row, column) = get_move(player, symbol, game_state)
    game_state = update_state(game_state, row, column, symbol)
    print_field(game_state)

print("Игра окончена!")