# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def from_to_file(path, data = None):
    if data != None:
        with open(path, 'w') as file:
            file.write(data)
    else:
        with open(path, 'r') as file:
            data = file.read()
        return data

def clean_data(data, pattern):
    output_list = [item for item in data if item.find(pattern) == -1]
    return ' '.join(map(str, output_list))


pattern_str = "абв"

folder = "python/lesson005/task01/"
input_file_name = "raw_data.txt"
output_file_name = "cleaned_data.txt"

raw_data = from_to_file(folder + input_file_name).split()

cleaned_data = clean_data(raw_data, pattern_str)

from_to_file(folder + output_file_name, cleaned_data)

print(raw_data)
print(cleaned_data)
