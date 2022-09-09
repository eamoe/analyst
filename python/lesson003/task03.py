# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def get_fraction_length(number):
    scale = 0
    while number < 1:
        number *= 10
        scale += 1
    return scale

def max_diff_fraction(input_list):
    min_fraction = input_list[0] - int(input_list[0])
    max_fraction = input_list[0] - int(input_list[0])
    for item in input_list:
        if item - int(item) == 0.0:
            if str(item).find('.') != -1:
                min_fraction = 0.0
        else:
            fraction = item - int(item)
            if fraction > max_fraction:
                max_fraction = fraction
            elif fraction < min_fraction:
                min_fraction = fraction
    if min_fraction == 0.0:
        output = round(max_fraction, get_fraction_length(max_fraction))
    else:
        output = int((max_fraction - min_fraction) * (10 ** get_fraction_length(min_fraction))) / (10 ** get_fraction_length(min_fraction))
    return output 

input_list = [1.1, 1.2, 3.1, 5, 10.01]

print(f"Список: {input_list}")
print(f"Разница между максимальным и минимальным значением дробной части элементов равна: {max_diff_fraction(input_list)}")
