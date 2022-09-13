# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def get_coeff(min, max):
    return random.randint(min, max + 1)

def form_polynomial_srt(k):
    
    elements = []
    polynomial_str = " + "

    for i in range(k, -1, -1):
        if i == 0:
         elements.append(f"{get_coeff(1, 100)}")
        elif i == 1:
            elements.append(f"{get_coeff(1, 100)}*x")
        else:
            elements.append(f"{get_coeff(1, 100)}*x^{i}")
    
    polynomial_str = polynomial_str.join(elements)
    polynomial_str += " = 0"
    
    return polynomial_str

polynomial_degree = int(input("Введите степень многочлена: "))
polynomial_str = form_polynomial_srt(polynomial_degree)
print(polynomial_str)

directory = 'python/lesson004/task004_polynomial/'
file_name = 'resulted_polynomial.txt'
with open(directory + file_name, 'w') as data:
    data.write(polynomial_str + '\n')

print(f"Результат записан в файл: {directory + file_name}")
