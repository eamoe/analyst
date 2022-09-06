# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.
# Пример:
# Для n = 6 -> 14.072


number = int(input("Введите целое положительное число больше нуля: "))

def form_items_list(number):
    items_list = []
    for n in range(1, number + 1):
        items_list.append((1 + 1 / n) ** n)
    return items_list

def calc_items_sum(items):
    sum = 0
    for item in items:
        sum += item
    return sum

print(f"Сумма {number} элементов последовательности (1 + 1/n)^n равна: {round(calc_items_sum(form_items_list(number)), 3)}")
