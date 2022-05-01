# Вычислить число  c заданной точностью d
from math import acos
def isdigit(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

while True:
    n = str(input('Введите число n: \n'))
    if isdigit(n):
        b = int(n)
        break
    else:
        print('Некорректный ввод. Повторите')

def printValueOfPi(n) :
    b = '{:.' + str(n) + 'f}'
    pi = b.format(2 * acos(0.0))
    print(pi)
if __name__ == "__main__":
    printValueOfPi(n)