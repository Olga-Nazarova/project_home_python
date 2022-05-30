#Написать программу преобразования десятичного числа в двоичное
def choice():
    while True:
        selector = None
        try:
            selector = int(input('Введите число которое необходимо преобразовать в двоичное:\n'))
            return selector
        except ValueError:
            print('\n Некорректный ввод! Повторите: \n')

n = choice()
b = ''

while n > 0:
    b = str(n % 2) + b
    n = n // 2

print(b)