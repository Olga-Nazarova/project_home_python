# Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30
def isdigit(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

while True:
    a = input('Введите число: \n').replace(',', '.')
    if isdigit(a):
        b = int(a)
        break
    else:
        print('Некорректный ввод. Повторите')

if (b % 5 == 0 and b % 10 == 0) or (b % 15 == 0 and b % 30 != 0):
    print(f'Число {b} кратно числам 5, 10, 15 и не кратно 30')
else:
    print(f'Число {b} не кратно числам 5, 10, 15')