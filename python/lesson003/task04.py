# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def convert_to_binary(number):
    
    zero = '0'
    one = '1'
    
    if number == 0:
        return zero
    elif number == 1:
        return one

    binary_str = ''
    threshold = 1
    while threshold * 2 <= number:
        threshold *= 2
    
    remainder = number - threshold
    binary_str += '1'
    i = 0
    while threshold > 1:
        i += 1
        threshold /= 2
        if threshold <= remainder:
            binary_str += '1'
            remainder -= threshold
        else:
            binary_str += '0'

    return binary_str

number = int(input("Введите число: "))

print(f"Число {number} в двоичном представлении: {convert_to_binary(number)}")
