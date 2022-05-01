# Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.
from random import randint
k = 3
file = open("poly1.txt", 'w+')
file.write(str(randint(1, 100))+' * x ^ '+str(k))
file.close()

file1 = open("poly2.txt", 'w+')
file1.write(str(randint(1, 100)) + ' * x + ' + str(randint(1, 100)))
file1.close()

with open("poly1.txt") as file:
    int_number = file.read()
    print(int_number)

with open("poly2.txt") as file:
    int_number2 = file.read()
    print(int_number2)

file3 = open("poly3.txt", 'w+')
file3.write(f'({int_number}) + ({int_number2})')
file3.close()

with open("poly3.txt") as file:
    int_number3 = file.read()
    print(int_number3)