# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

def get_quadrant():
    try:
        return int(input(f'Введите номер четверти: '))
    except:
        print('Некорректное значение!')
        return -1

def get_coord_range(quadrant):
    if quadrant == 1:
        x = (0, '+∞')
        y = (0, '+∞')
    elif quadrant == 2:
        x = (0, '-∞')
        y = (0, '+∞')
    elif quadrant == 3:
        x = (0, '-∞')
        y = (0, '-∞')
    elif quadrant == 4:
        x = (0, '+∞')
        y = (0, '-∞')
    return (x, y)

quadrant = get_quadrant()
if quadrant in range(1, 5):
    coordinates = get_coord_range(quadrant)
    print(f"Диапазон возможных значений:\nПо оси OX: {coordinates[0]}\nПо оси OY: {coordinates[1]}")
else:
    print("Попробуйте снова!")
