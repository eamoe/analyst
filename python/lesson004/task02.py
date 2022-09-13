# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def find_factors(number):
    div = 2
    factors = []
    while div <= number:
        if number % div == 0:
            factors.append(div)
            number = number / div
        else:
            div = div + 1
    return factors

def print_expression(factors):
    factors_str = " * "
    return factors_str.join(map(str, factors))

number = int(input("Введите натуральное число: "))

factors = find_factors(number)
print(f"Разложение числа {number} на простые множители:")
print(f"{number} = {print_expression(factors)}")
