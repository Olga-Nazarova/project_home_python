# Строка содержит набор чисел. Показать большее и меньшее число. Символ-разделитель - пробел
import random

string = ""
for x in range(5, 21):
    a = random.randint(1, 20)
    string += f'{a} '

print(string)
print(type(string))

strings = string.split(" ")
strings = list(filter(None, strings))
numbers = [int(x) for x in strings]
print(numbers)
print(f'Максимальное число: {max(numbers)}')
print(f'Минимальное число: {min(numbers)}')