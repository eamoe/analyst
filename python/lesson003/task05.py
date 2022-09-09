# Задайте число.
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

import math

fib_numbers = {}

def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        if number not in fib_numbers:
            fib_numbers[number] = fibonacci(number - 1) + fibonacci(number - 2)
        return fib_numbers[number]

number = int(input("Введите целое число: "))

fibonacci_list = []
for i in range(-number, number + 1):
    if i < 0:
        fibonacci_list.append(int(math.pow(-1, i + 1)) * fibonacci(abs(i)))
    else:
        fibonacci_list.append(fibonacci(i))

print(fibonacci_list)