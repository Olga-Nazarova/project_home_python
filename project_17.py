# Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число
from random import randint
def isdigit(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

while True:
    x = str(input('Введите натуральное положительное число \n'))
    if isdigit(x) and (int(x) != 0) and (int(x) < 11):
        x = abs(int(x))
        break
    else:
        print('Некорректный ввод. Повторите: ')

for i in range(-x, x + 1):
    print(i, end=' ')


my_file = open("file.txt", 'w+')
my_file.write(f'{str(randint(1, 6))} \n')
my_file.write(f'{str(randint(1, 6))} \n')
my_file.close()

with open("file.txt") as file:
    int_number = file.read()
    print()
    print(int_number)



