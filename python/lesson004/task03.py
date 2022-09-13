# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def form_unique_list(input_list):
    
    elements = input_list.copy()
    
    frequency_dict = {}
    while len(elements) > 0:
        element = elements.pop()
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
    
    unique_elements = []
    for key, value in frequency_dict.items():
        if value == 1:
            unique_elements.append(key)
    
    return unique_elements

input_list = [1, 2, 7, 3, 4, 7, 2, 0, 8, 1]

print(f"Исходный список: {input_list}")
print(f"Список неповторяющихся элементов: {form_unique_list(input_list)}")
