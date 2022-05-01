# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

while True:
    x = input('Введите точку Х: \n').replace(',', '.')
    if isfloat(x):
        x = float(x)
        break
    else:
        print('Некорректный ввод. Повторите')

while True:
    y = input('Введите точку Y: \n').replace(',', '.')
    if isfloat(y):
        y = float(y)
        break
    else:
        print('Некорректный ввод. Повторите')


if (x > 0) and (y > 0):
    print('Точка с координатами x и y находится в I четверти')
elif (x < 0) and (y > 0):
    print('Точка с координатами x и y находится в II четверти')
elif (x < 0) and (y < 0):
    print('Точка с координатами x и y находится в III четверти')
elif (x > 0) and (y < 0):
    print('Точка с координатами x и y находится в IV четверти')
elif (x == 0) and ( y !=0):
    print('Точка с координатами x и y находится на оси Y')
elif (y == 0) and (x!= 0):
    print('Точка с координатами x и y находится на оси X')
else:
    print('Точка находится в X0, Y0')