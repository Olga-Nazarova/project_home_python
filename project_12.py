# Для натурального n создать словарь индекс-значение, состоящий из элементов
# последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
def isdigit(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

while True:
    n = input('Введите количество индексов словаря: \n')
    if isdigit(n):
        if (int(n) == 0):
            print('Некорректный ввод. Повторите')
            continue
        n = int(n)
        break
    else:
        print('Некорректный ввод. Повторите')

def get_dict(n):
    return {x: 3 * x + 1 for x in range(1, n+1)}
print(get_dict(n))

