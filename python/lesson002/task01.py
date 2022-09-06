# Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0.56 -> 11

def calc_digits_sum(number_str):
    digits_list = [*number_str.replace('-', '').replace('.', '')]
    sum = 0
    for digit in digits_list:
        sum += int(digit)
    return sum


user_number_str = input("Введите вещественное число: ")

user_number = float(user_number_str)

print(f"Сумма цифр числа {user_number} равна {calc_digits_sum(user_number_str)}")