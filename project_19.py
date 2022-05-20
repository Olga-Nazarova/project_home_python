# Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора
# псевдослучайных чисел
import random
l = list(range(1, 20))
random.shuffle(l)
for i in l:
    print(i, end= ' ')