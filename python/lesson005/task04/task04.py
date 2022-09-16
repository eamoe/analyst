# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def from_to_file(path, data = None):
    if data != None:
        with open(path, 'w') as file:
            file.write(data)
    else:
        with open(path, 'r') as file:
            data = file.read()
        return data

def get_substrings(data):
    output_str = ""
    length = len(data)
    for i in range(0, length - 1):
        if data[i] == data[i + 1]:
            output_str += data[i]
        else:
            output_str += data[i] + " "
    output_str += data[length - 1]
    return output_str.split()

def compress_data(data):
    substrings = get_substrings(data)
    symbol_num_pairs = [element[0] + str(len(element)) for element in substrings]
    compressed_str = ''.join(map(str, symbol_num_pairs))
    return compressed_str
    

def decompress_data(data):
    output = ""
    number = 0
    symbol = ""
    for item in data:
        if item.isalpha() and item != symbol:
            output += symbol * int(number)
            symbol = item
            number = ""
        else:
            number += item
    output += symbol * int(number)
    return output


folder = "python/lesson005/task04/"

raw_data_file_name = "raw_data.txt"
raw_data = from_to_file(folder + raw_data_file_name)

compressed_data_file_name = "compressed_data.txt"
compressed_data = compress_data(raw_data)
from_to_file(folder + compressed_data_file_name, compressed_data)

decompressed_data_file_name = "decompressed_data.txt"
data_to_decompress = from_to_file(folder + compressed_data_file_name)
decompressed_data = decompress_data(data_to_decompress)
from_to_file(folder + decompressed_data_file_name, decompressed_data)

print(f"Данные для сжатия: {raw_data}")
print(f"Результат сжатия: {compressed_data}\n")
print(f"Распакованные данные: {decompressed_data}")
