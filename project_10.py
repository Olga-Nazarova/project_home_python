# Найти расстояние между двумя точками пространства
import math
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

while True:
    a = input('Программа рассчитывает расстояние между точками в пространстве 2D или 3D. Введите 1 для рассчёта в 2D или 2 для рассчёта в 3D: \n').replace(',', '.')
    if isfloat(a):
        if (float(a) < 1) or (float(a) > 2):
            print('Некорректный ввод. Повторите')
            continue
        a = float(a)
        break

    else:
        print('Некорректный ввод. Повторите')

if a == 1:
    print('Вы выбрали рассчёт в 2D. Для рассчёта программе нужны координаты x1, x2, y1, y2')
    x1 = int(input('Введите x1: \n').replace(',', '.'))
    x2 = int(input('Введите x2: \n').replace(',', '.'))
    y1 = int(input('Введите y1: \n').replace(',', '.'))
    y2 = int(input('Введите y2: \n').replace(',', '.'))
    result = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    print(f'Расстояние между точками в 2D равно {result}')

if a == 2:
    print('Вы выбрали рассчёт в 3D. Для рассчёта программе нужны координаты x1, x2, y1, y2, z1, z2')
    x1 = int(input('Введите x1: \n').replace(',', '.'))
    x2 = int(input('Введите x2: \n').replace(',', '.'))
    y1 = int(input('Введите y1: \n').replace(',', '.'))
    y2 = int(input('Введите y2: \n').replace(',', '.'))
    z1 = int(input('Введите z1: \n').replace(',', '.'))
    z2 = int(input('Введите z2: \n').replace(',', '.'))
    result = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) + math.pow(z2 - z1, 2))
    print(f'Расстояние между точками в 3D равно {result}')

