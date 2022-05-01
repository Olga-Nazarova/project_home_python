# Вывести на экран числа от -N до N
num = abs(int(input('Введите число \n')))
for i in range(-num, num + 1):
    print(i, end=' ')