# Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
# На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота.
# Достаточно сделать так, чтобы бот не брал конфет больше положенного или больше чем имеется в куче.
# b) Подумайте как наделить бота ""интеллектом"".
# Напоминаю, если перед пользователем будет лежать 29 конфет, то он, однозначно, проиграет.
# Достаточно довести игру до такой ситуации.

import random

def toss_coin():
    if random.randint(0, 1) == 0:
        coin_side = 1
    else:
        coin_side = -1
    return coin_side


def print_first_move_player(first_move):
    if first_move == 1:
        print("Начинает первый игрок!")
    else:
        print("Начинает второй игрок!")


def get_current_take(player, remainder, max_take, is_machine):
    if not is_machine:
        is_incorrect_move = True
        while is_incorrect_move:
            current_take = int(input(f"Игрок {player}, сколько конфет возьмете? "))
            if current_take > max_take or current_take <= 0:
                print(f"Можно брать не более {max_take} конфет за раз и не менее 1! Попробуйте снова!")
            else:
                is_incorrect_move = False
    else:
        if remainder > max_take:
            if remainder % max_take == 0 or remainder % max_take == 1:
                current_take = random.randint(1, max_take)
            else:
                current_take = remainder % max_take - 1
        else:
            current_take = remainder
        print(f"Игрок {player} взял конфет: {current_take}")
    return current_take

def flip_turn(turn):
    if turn == -1:
            turn = 1
    else:
        turn = -1
    return turn


def next_move(turn):
    if turn == -1:
        player = 2
    else:
        player = 1
    return player


def is_game_over(remainder, player):
    if remainder <= 0:
        print(f"Победил {players[player -1]}")


def game(candies_number, max_take, turn, is_machine):
    
    remainder = candies_number
    
    while remainder > 0:
        
        print(f"Осталось конфет: {remainder}")
        
        player = next_move(turn)

        if is_machine and player == 2:
            current_take = get_current_take(player, remainder, max_take, 1)
        else:
            current_take = get_current_take(player, remainder, max_take, 0)
        
        remainder = remainder - current_take
        
        is_game_over(remainder, player)
        
        turn = flip_turn(turn)



candies_number = 101
max_take = 28
players = ["игрок 1", "Робот"]

turn = toss_coin()
print_first_move_player(turn)

game(candies_number, max_take, turn, 1)
