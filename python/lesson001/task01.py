# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

user_input = input('Введите цифру: ')

if user_input.isnumeric():
    number = int(user_input)
else:
    number = -1
    print('Некорректное значение!')

if number == 0:
    print('Цифра должна быть больше нуля!')
if number > 0 and number <= 5:
    print('Нет, это не выходной день!')
elif number == 6 or number == 7:
    print('Да, это выходной день!')
