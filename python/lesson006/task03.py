


# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


import math


def mult_pairs(input_list):
    output_list = []
    
    length = len(input_list)
    if length % 2 == 0:
        stop = int(length / 2)
    else:
        stop = int(length / 2) + 1
    
    for i in range(0, stop):
        output_list.append(input_list[i] * input_list[len(input_list) - i - 1])
    return output_list

input_list = [10, 2, 7]

print(f"Список: {input_list}")
print(f"(OLD) Произведение пар чисел списка: {mult_pairs(input_list)}")


# Новое решение
def mult_pairs_new(in_list):
    half_len = int(len(in_list)/ 2)
    if half_len == 0:
        return [in_list[0]**2]
    else:
        return [a * b for a, b in zip(in_list[0:half_len + 1], in_list[:half_len - 1:-1])]


print(f"Список: {input_list}")
print(f"(NEW) Произведение пар чисел списка: {mult_pairs_new(input_list)}")
