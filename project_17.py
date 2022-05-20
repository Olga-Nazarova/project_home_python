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

# 2 вариант
from dataclasses import replace

n = int(input('Введите натуральное положительное число \n'))
li = [x for x in range(-n,n+1)]
print(li)

with open('file.txt','w') as data:
    data.write('0\n')
    data.write('1\n')

path = 'file.txt'
data = open(path,'r')
res = 1
for line in data:
    number = line.replace('\n','')
    number = int(number)
    num_1 = li[number]
    res = res*num_1
print('Произведение элементов на указанных позициях =', res)
data.close()