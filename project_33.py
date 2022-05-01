# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint
def isdigit(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

while True:
    k = str(input('Введите нарутальную степень: \n'))
    if isdigit(k) and (int(k) != 0):
        k = int(k)
        break
    else:
        print('Некорректный ввод. Повторите')

file = open("polynom.txt", 'w+')
while k > 1:
    file.write(str(randint(1, 100))+' * x ^'+str(k)+'+')
    k -= 1
file.write(str(randint(1, 100)) + '*x+' + str(randint(1, 100)) + '=0')
file.close()
