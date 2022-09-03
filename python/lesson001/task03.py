# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

def getNumber(coordinate):
    try:
        number = float(input(f'Введите координату {coordinate}: '))
    except:
        print('Введенное значение не является числом!')
    return number

def isZero(number):
    if number == 0:
        return True
    else:
        return False

def getQuadrant(x, y):
    quadrant = None
    if x > 0 and y > 0:
        quadrant = 1
    elif x < 0 and y > 0:
        quadrant = 2
    elif x < 0 and y < 0:
        quadrant = 3
    elif x > 0 and y < 0:
        quadrant = 4
    return quadrant

x = getNumber('X')
y = getNumber('Y')

if isZero(x) or isZero(y):
    print('Обе координаты должны быть отличны от нуля!')
else:
    print(f'Точка с координатами ({x}, {y}) находится в {getQuadrant(x, y)}-й четверти.')
