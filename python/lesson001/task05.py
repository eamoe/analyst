# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

def getCoordinates(point):
    print(f'Точка {point}')
    try:
        x = float(input(f'Введите координату X: '))
        y = float(input(f'Введите координату Y: '))
    except:
        print('Введенное значение не является числом!')
    return (x, y)

def calcDistance(point_a, point_b):
    distance = ((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)**0.5
    return distance

point_a = getCoordinates('A')
point_b = getCoordinates('B')

print(f"Расстояние между точками {point_a} и {point_b} равно {calcDistance(point_a, point_b):.3f}")
