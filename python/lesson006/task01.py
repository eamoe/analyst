# Задача: предложить улучшения кода для уже решённых задач (4 задачи из любых семинаров, кроме первого):
# С помощью использования лямбд, filter, map, zip, enumerate, list comprehension
# В ответе должны присутствовать старые и новые варианты решений.


# Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input("Введите целое положительное число: "))

factorial_list = []
for i in range(1, number + 1):
    factorial_list.append(factorial(i))

print(f"(OLD) Набор произведений для числа {number}: {factorial_list}")


# Новое решение
def create_factorial_list(n):
    factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)
    return [factorial(i) for i in range(1, n + 1)]

output_message = f"(NEW) Набор произведений для числа {number}: "
print(output_message, create_factorial_list(number))
