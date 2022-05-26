# Определить, присутствует ли в заданном списке строк, некоторое число
import random
def check(lines, number):
    count = 0
    for i in lines:
        if int(i) == number: count += 1
    print(f'Число {number} присутствует в списке строк {count} раз')

lst = [random.randint(5, 15) for i in range(random.randint(10, 20))]
lines = [str(x) for x in lst]
num = random.randint(5, 15)
print(f'Загаданное число: {num}')
print(f'Список строк: {lines}')

check(lines, num)