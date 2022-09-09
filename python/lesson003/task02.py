# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


def mult_pairs(input_list):
    output_list = []
    
    length = len(input_list)
    if length % 2 == 0:
        stop = int(length / 2)
    else:
        stop = int(length / 2) + 1
    
    for i in range(0, stop):
        output_list.append(input_list[i] * input_list[len(input_list) - i -1])
    return output_list

input_list = [2, 3, 5, 6]

print(f"Список: {input_list}")
print(f"Произведение пар чисел списка: {mult_pairs(input_list)}")
