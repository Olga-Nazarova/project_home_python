# Показать первую цифру дробной части числа
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

while True:
    a = str(input('Введите дробное число: \n').replace(',', '.'))
    if isfloat(a):
        break
    else:
        print('Некорректный ввод. Повторите')

number = abs(float(a))
result = int(number*10 % 10)
print(result)