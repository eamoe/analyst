# Вычислить число π c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# https://completerepair.ru/kak-vychislit-chislo-pi

from decimal import Decimal

def unsigned_leibniz_term(n):
    return 1 / (2 * n + 1)

def calc_pi(precision):
    n = 0
    term = unsigned_leibniz_term(n)
    sum = term
    while term > precision / 10:
        n += 1
        term = unsigned_leibniz_term(n)
        sum += (-1)**n * term
    return (sum * 4)

precision = float(input("Введите точность, с которой необходимо определить число Pi: "))
print(calc_pi(precision))
