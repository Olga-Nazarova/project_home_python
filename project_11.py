# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
import math
def isdigit(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

while True:
    n = input('Введите количество символов списка: \n')
    if isdigit(n):
        n = int(n)
        break
    else:
        print('Некорректный ввод. Повторите')
a = 1
print(a)
for i in list(range(n - 1)):
    a *= -3
    print(a)
