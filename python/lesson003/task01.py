# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def calc_odd_pos_sum(list):
    sum = 0
    for i in range(1, len(list), 2):
        sum += list[i]
    return sum

input_list = [2, 3, 5, 9, 3]

print(f"Список: {input_list}")
print(f"Сумма элементов списка, стоящих на нечётной позиции, равна: {calc_odd_pos_sum(input_list)}")
