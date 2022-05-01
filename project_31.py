#Составить список простых множителей натурального числа N
def isdigit(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

while True:
    n = str(input('Введите число n: \n'))
    if isdigit(n) and n % 2 == 0:
        b = int(n)
        break
    else:
        print('Некорректный ввод. Повторите')

factors = []
d = 2
m = n
while d * d <= n:
        if n % d == 0:
            factors.append(d)
            n//=d
        else:
            d += 1
factors.append(n)
print('{} = {}' .format(m, factors))
