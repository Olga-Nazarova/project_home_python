# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
def isstr(value):
    try:
        str(value)
        return True
    except ValueError:
        return False

while True:
    n = input('Задайте первую строку: \n')
    if isstr(n):
        n = str(n)
        break
    else:
        print('Некорректный ввод. Повторите')

while True:
    s = input('Задайте вторую строку: \n')
    if isstr(s):
        n = str(s)
        break
    else:
        print('Некорректный ввод. Повторите')


t = 0
for first in range(len(s) - len(n) + 1):
    if s[first:first+len(n)] == n:
        t += 1
print(t)
